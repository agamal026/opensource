#!/usr/bin/env python3
"""Capture small, read-only Git checkpoints without exporting local source details.

Python 3.10+ and Git are the only dependencies. Configuration paths expand ``~``;
relative workspace paths are relative to the directory containing the config file.
Environment-variable expansion is deliberately not performed.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
from typing import Any


SCHEMA_VERSION = 1
GIT_TIMEOUT_SECONDS = 20
WORKSPACE_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9_.-]{0,63}\Z")
HEAD_SHA = re.compile(rb"(?:[0-9a-f]{40}|[0-9a-f]{64})\Z")
UNMERGED_STATUSES = {b"DD", b"AU", b"UD", b"UA", b"DU", b"AA", b"UU"}


class SnapshotError(Exception):
    """An error whose category is safe to include in a snapshot."""

    def __init__(self, category: str) -> None:
        super().__init__(category)
        self.category = category


def load_config(config_path: Path) -> list[tuple[str, Path]]:
    """Validate the complete config before inspecting any repository."""
    try:
        with config_path.open(encoding="utf-8") as handle:
            config = json.load(handle)
    except OSError:
        raise SnapshotError("config_unavailable") from None
    except (ValueError, UnicodeError):
        raise SnapshotError("invalid_config_json") from None

    if not isinstance(config, dict) or set(config) != {"schema_version", "workspaces"}:
        raise SnapshotError("invalid_config_schema")
    if type(config["schema_version"]) is not int or config["schema_version"] != SCHEMA_VERSION:
        raise SnapshotError("unsupported_config_version")
    if not isinstance(config["workspaces"], list):
        raise SnapshotError("invalid_config_schema")

    workspaces: list[tuple[str, Path]] = []
    seen: set[str] = set()
    config_directory = config_path.absolute().parent
    for entry in config["workspaces"]:
        if not isinstance(entry, dict) or set(entry) != {"id", "path"}:
            raise SnapshotError("invalid_workspace_entry")
        workspace_id, location = entry["id"], entry["path"]
        if not isinstance(workspace_id, str) or not WORKSPACE_ID.fullmatch(workspace_id):
            raise SnapshotError("invalid_workspace_id")
        if workspace_id in seen:
            raise SnapshotError("duplicate_workspace_id")
        if not isinstance(location, str) or not location or "\x00" in location:
            raise SnapshotError("invalid_workspace_path")
        seen.add(workspace_id)
        path = Path(os.path.expanduser(location))
        if not path.is_absolute():
            path = config_directory / path
        workspaces.append((workspace_id, path))
    return workspaces


def _git(path: Path, *arguments: str) -> subprocess.CompletedProcess[bytes]:
    # Inherited GIT_DIR/GIT_WORK_TREE/etc. must not redirect a configured workspace.
    environment = {key: value for key, value in os.environ.items() if not key.startswith("GIT_")}
    environment.update(GIT_OPTIONAL_LOCKS="0", GIT_TERMINAL_PROMPT="0", LC_ALL="C")
    command = [
        "git",
        "-c", "core.fsmonitor=false",
        "-c", "core.untrackedCache=false",
        "-c", "status.renames=true",
        "-C", str(path),
        *arguments,
    ]
    try:
        return subprocess.run(
            command,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            env=environment,
            timeout=GIT_TIMEOUT_SECONDS,
            check=False,
        )
    except FileNotFoundError:
        raise SnapshotError("git_unavailable") from None
    except subprocess.TimeoutExpired:
        raise SnapshotError("git_timeout") from None
    except OSError:
        raise SnapshotError("git_failed") from None


def count_changes(porcelain: bytes) -> dict[str, int]:
    """Count porcelain-v1 -z records, consuming a rename's second path once.

    Tracked count includes staged-only changes and unresolved conflicts. Staged
    count includes index changes, excluding unresolved conflicts. Untracked count
    is the number of individual untracked files (Git does not report empty dirs).
    Paths are deliberately never decoded, returned, or included in exceptions.
    """
    tracked = staged = untracked = 0
    if not porcelain:
        return {"tracked_change_count": 0, "staged_change_count": 0, "untracked_count": 0}
    if not porcelain.endswith(b"\x00"):
        raise SnapshotError("invalid_git_output")

    records = iter(porcelain[:-1].split(b"\x00"))
    for record in records:
        if len(record) < 4 or record[2:3] != b" ":
            raise SnapshotError("invalid_git_output")
        status = record[:2]
        if status == b"??":
            untracked += 1
            continue
        if status == b"!!":
            continue
        if any(code not in b" MADRCUT" for code in status) or status == b"  ":
            raise SnapshotError("invalid_git_output")
        tracked += 1
        if status not in UNMERGED_STATUSES and status[0] != ord(" "):
            staged += 1
        if b"R" in status or b"C" in status:
            original_path = next(records, None)
            if not original_path:
                raise SnapshotError("invalid_git_output")

    return {
        "tracked_change_count": tracked,
        "staged_change_count": staged,
        "untracked_count": untracked,
    }


def inspect_workspace(workspace_id: str, path: Path) -> dict[str, Any]:
    """Return only the documented allowlist, including a sanitized failure."""
    try:
        try:
            if not path.is_dir():
                raise SnapshotError("unavailable_directory")
        except OSError:
            raise SnapshotError("unavailable_directory") from None

        inside = _git(path, "rev-parse", "--is-inside-work-tree")
        if inside.returncode != 0 or inside.stdout.strip() != b"true":
            raise SnapshotError("not_git_work_tree")

        symbolic = _git(path, "symbolic-ref", "--quiet", "--short", "HEAD")
        if symbolic.returncode not in (0, 1):
            raise SnapshotError("git_failed")
        detached = symbolic.returncode == 1
        branch = None if detached else symbolic.stdout.rstrip(b"\n").decode("utf-8", errors="replace")
        if not detached and not branch:
            raise SnapshotError("invalid_git_output")

        revision = _git(path, "rev-parse", "--verify", "--quiet", "HEAD")
        if revision.returncode == 0:
            head_bytes = revision.stdout.strip()
            if not HEAD_SHA.fullmatch(head_bytes):
                raise SnapshotError("invalid_git_output")
            head: str | None = head_bytes.decode("ascii")
        elif revision.returncode == 1 and not detached:
            head = None  # Valid work tree on an unborn branch: no commit exists yet.
        else:
            raise SnapshotError("git_failed")

        changes = _git(
            path,
            "status", "--porcelain=v1", "-z", "--no-branch",
            "--untracked-files=all", "--ignore-submodules=none",
        )
        if changes.returncode != 0:
            raise SnapshotError("git_failed")
        return {
            "id": workspace_id,
            "status": "ok",
            "branch": branch,
            "detached": detached,
            "head": head,
            **count_changes(changes.stdout),
        }
    except SnapshotError as error:
        return {"id": workspace_id, "status": "error", "error": error.category}


def capture(config_path: Path) -> tuple[dict[str, Any], int]:
    snapshot: dict[str, Any] = {
        "schema_version": SCHEMA_VERSION,
        "captured_at": datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z"),
        "complete": False,
        "workspaces": [],
    }
    try:
        workspaces = load_config(config_path)
    except SnapshotError as error:
        snapshot["error"] = error.category
        return snapshot, 2
    snapshot["workspaces"] = [inspect_workspace(workspace_id, path) for workspace_id, path in workspaces]
    snapshot["complete"] = all(item["status"] == "ok" for item in snapshot["workspaces"])
    return snapshot, 0 if snapshot["complete"] else 1


def write_atomic(output_path: Path, text: str) -> None:
    """Replace output atomically; mode is 0600 on POSIX, inherited ACLs on Windows."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    temporary_path: Path | None = None
    try:
        descriptor, name = tempfile.mkstemp(prefix=".workspace-snapshot-", suffix=".tmp", dir=output_path.parent)
        temporary_path = Path(name)
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(text)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary_path, output_path)
        temporary_path = None
    finally:
        if temporary_path is not None:
            temporary_path.unlink(missing_ok=True)


class _ArgumentParser(argparse.ArgumentParser):
    def error(self, message: str) -> None:
        # argparse's default may echo arbitrary local paths or secret arguments.
        self.print_usage(sys.stderr)
        self.exit(2, "error: invalid_arguments\n")


def main(argv: list[str] | None = None) -> int:
    parser = _ArgumentParser(description=__doc__, prog="workspace_snapshot.py")
    parser.add_argument("--config", required=True, type=Path, help="Local workspace config JSON")
    parser.add_argument("--output", type=Path, help="Atomic JSON output; omit or use - for stdout")
    arguments = parser.parse_args(argv)
    config_path = Path(os.path.expanduser(str(arguments.config)))
    output_path = Path(os.path.expanduser(str(arguments.output))) if arguments.output is not None else None
    try:
        if output_path is not None and str(output_path) != "-" and output_path.resolve() == config_path.resolve():
            print("error: output_would_overwrite_config", file=sys.stderr)
            return 2
        snapshot, exit_code = capture(config_path)
        serialized = json.dumps(snapshot, indent=2, ensure_ascii=True) + "\n"
        if output_path is None or str(output_path) == "-":
            sys.stdout.write(serialized)
        else:
            write_atomic(output_path, serialized)
    except (OSError, RuntimeError):
        print("error: output_unavailable", file=sys.stderr)
        return 2
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
