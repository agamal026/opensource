"""Exercise the snapshot utility against real local Git repositories."""

from __future__ import annotations

from contextlib import redirect_stderr, redirect_stdout
import importlib.util
import io
import json
import os
from pathlib import Path
import shutil
import stat
import subprocess
import tempfile
import unittest
from unittest import mock


MODULE_PATH = Path(__file__).resolve().parents[1] / "tools" / "workspace_snapshot.py"
SPEC = importlib.util.spec_from_file_location("workspace_snapshot", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
snapshot = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(snapshot)


@unittest.skipUnless(shutil.which("git"), "Git is required for integration tests")
class WorkspaceSnapshotTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(prefix="private-local-checkpoint-")
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.repo = self.root / "workspace with spaces"
        self.repo.mkdir()
        self.git("init", "-b", "main")
        self.git("config", "user.name", "Private Test Identity")
        self.git("config", "user.email", "private-test@example.invalid")
        self.git("config", "core.autocrlf", "false")
        self.git("remote", "add", "origin", "https://private-token@example.invalid/private/repository.git")
        for name in ("tracked.txt", "to rename secret name.txt", "staged.txt"):
            (self.repo / name).write_bytes(b"baseline\n")
        self.git("add", "--all")
        self.git("commit", "-m", "Initial local fixture")
        self.config = self.root / ".local" / "workspaces.json"
        self.config.parent.mkdir()
        self.write_config([{"id": "example", "path": str(self.repo)}])

    def git(self, *arguments: str) -> subprocess.CompletedProcess[bytes]:
        environment = {key: value for key, value in os.environ.items() if not key.startswith("GIT_")}
        environment.update(GIT_CONFIG_NOSYSTEM="1", GIT_CONFIG_GLOBAL=os.devnull, LC_ALL="C")
        return subprocess.run(
            ["git", "-C", str(self.repo), *arguments],
            check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=environment,
        )

    def write_config(self, workspaces: list[dict[str, str]]) -> None:
        self.config.write_text(json.dumps({"schema_version": 1, "workspaces": workspaces}), encoding="utf-8")

    def run_cli(self, *arguments: str) -> tuple[int, str, str]:
        stdout, stderr = io.StringIO(), io.StringIO()
        with redirect_stdout(stdout), redirect_stderr(stderr):
            code = snapshot.main(["--config", str(self.config), *arguments])
        return code, stdout.getvalue(), stderr.getvalue()

    def assert_no_private_details(self, text: str) -> None:
        for detail in (
            str(self.root), self.root.name, "private-token", "private-test@example.invalid",
            "Private Test Identity", "example.invalid", "secret name", "tracked.txt", "staged.txt",
        ):
            self.assertNotIn(detail, text)

    def test_clean_repository_and_exact_output_allowlist(self) -> None:
        code, text, stderr = self.run_cli()
        self.assertEqual((code, stderr), (0, ""))
        data = json.loads(text)
        self.assertEqual(set(data), {"schema_version", "captured_at", "complete", "workspaces"})
        self.assertTrue(data["complete"])
        item = data["workspaces"][0]
        self.assertEqual(set(item), {
            "id", "status", "branch", "detached", "head", "tracked_change_count",
            "staged_change_count", "untracked_count",
        })
        self.assertEqual(item["branch"], "main")
        self.assertFalse(item["detached"])
        self.assertEqual(item["head"], self.git("rev-parse", "HEAD").stdout.decode().strip())
        self.assertEqual((item["tracked_change_count"], item["staged_change_count"], item["untracked_count"]), (0, 0, 0))
        self.assert_no_private_details(text)

    def assert_mixed_change_counts(
        self, original: str, renamed: str, untracked: str, nested_untracked: str,
    ) -> None:
        (self.repo / "tracked.txt").write_bytes(b"unstaged edit\n")
        (self.repo / "staged.txt").write_bytes(b"staged edit\n")
        self.git("add", "staged.txt")
        # The same tracked record has both staged and unstaged changes.
        (self.repo / "staged.txt").write_bytes(b"later unstaged edit\n")
        self.git("mv", original, renamed)
        (self.repo / untracked).write_bytes(b"private draft\n")
        (self.repo / "private directory").mkdir()
        (self.repo / "private directory" / nested_untracked).write_bytes(b"more\n")
        code, text, stderr = self.run_cli()
        self.assertEqual((code, stderr), (0, ""))
        item = json.loads(text)["workspaces"][0]
        self.assertEqual((item["tracked_change_count"], item["staged_change_count"], item["untracked_count"]), (3, 2, 2))
        self.assert_no_private_details(text)

    def test_staged_unstaged_rename_and_untracked_with_spaces(self) -> None:
        self.assert_mixed_change_counts(
            "to rename secret name.txt", "renamed secret name.txt",
            "untracked secret name.txt", "another file",
        )

    @unittest.skipIf(os.name == "nt", "Windows filenames cannot contain newline characters")
    def test_newlines_in_workspace_rename_and_untracked_paths(self) -> None:
        self.repo = self.repo.rename(self.root / "workspace with spaces\nand newline")
        self.write_config([{"id": "example", "path": str(self.repo)}])
        self.git("mv", "to rename secret name.txt", "to rename\nsecret name.txt")
        self.git("commit", "-am", "Prepare newline path fixture")
        self.assert_mixed_change_counts(
            "to rename\nsecret name.txt", "renamed\nsecret name.txt",
            "untracked\nsecret name.txt", "another\nfile",
        )

    def test_detached_head_and_unborn_branch(self) -> None:
        self.git("checkout", "--detach", "HEAD")
        detached, code = snapshot.capture(self.config)
        self.assertEqual(code, 0)
        self.assertTrue(detached["workspaces"][0]["detached"])
        self.assertIsNone(detached["workspaces"][0]["branch"])
        self.assertIsNotNone(detached["workspaces"][0]["head"])
        self.git("checkout", "--orphan", "new-empty-branch")
        unborn, code = snapshot.capture(self.config)
        self.assertEqual(code, 0)
        self.assertFalse(unborn["workspaces"][0]["detached"])
        self.assertEqual(unborn["workspaces"][0]["branch"], "new-empty-branch")
        self.assertIsNone(unborn["workspaces"][0]["head"])

    def test_unresolved_merge_is_tracked_but_not_staged(self) -> None:
        self.git("checkout", "-b", "side")
        (self.repo / "tracked.txt").write_bytes(b"side edit\n")
        self.git("commit", "-am", "Side edit")
        self.git("checkout", "main")
        (self.repo / "tracked.txt").write_bytes(b"main edit\n")
        self.git("commit", "-am", "Main edit")
        with self.assertRaises(subprocess.CalledProcessError) as conflict:
            self.git("merge", "--no-edit", "side")
        self.assertEqual(conflict.exception.returncode, 1)
        data, code = snapshot.capture(self.config)
        self.assertEqual(code, 0)
        item = data["workspaces"][0]
        self.assertEqual((item["tracked_change_count"], item["staged_change_count"], item["untracked_count"]), (1, 0, 0))

    def test_partial_result_for_missing_directory_and_nonrepo(self) -> None:
        nonrepo = self.root / "private-not-a-repo"
        nonrepo.mkdir()
        self.write_config([
            {"id": "working", "path": str(self.repo)},
            {"id": "missing", "path": str(self.root / "private-missing")},
            {"id": "plain", "path": str(nonrepo)},
        ])
        code, text, stderr = self.run_cli()
        self.assertEqual((code, stderr), (1, ""))
        data = json.loads(text)
        self.assertFalse(data["complete"])
        self.assertEqual(data["workspaces"][0]["status"], "ok")
        self.assertEqual(data["workspaces"][1], {"id": "missing", "status": "error", "error": "unavailable_directory"})
        self.assertEqual(data["workspaces"][2], {"id": "plain", "status": "error", "error": "not_git_work_tree"})
        self.assert_no_private_details(text + stderr)

    def test_duplicate_ids_rejected_before_git_and_no_paths_leak(self) -> None:
        self.write_config([{"id": "duplicate", "path": str(self.repo)}, {"id": "duplicate", "path": "~/private-secret"}])
        with mock.patch.object(snapshot, "_git") as git:
            code, text, stderr = self.run_cli()
        git.assert_not_called()
        self.assertEqual((code, stderr), (2, ""))
        data = json.loads(text)
        self.assertFalse(data["complete"])
        self.assertEqual(data["workspaces"], [])
        self.assertEqual(data["error"], "duplicate_workspace_id")
        self.assert_no_private_details(text)
        self.assertNotIn("private-secret", text)

    def test_relative_paths_tilde_and_no_environment_expansion(self) -> None:
        self.write_config([{"id": "relative", "path": "../" + self.repo.name}])
        data, code = snapshot.capture(self.config)
        self.assertEqual(code, 0)
        self.assertEqual(data["workspaces"][0]["status"], "ok")
        with mock.patch.dict(os.environ, {"HOME": str(self.root), "USERPROFILE": str(self.root)}):
            self.write_config([{"id": "tilde", "path": "~/" + self.repo.name}])
            self.assertEqual(snapshot.capture(self.config)[1], 0)
            self.write_config([{"id": "literal", "path": "${HOME}/" + self.repo.name}])
            data, code = snapshot.capture(self.config)
        self.assertEqual(code, 1)
        self.assertEqual(data["workspaces"][0]["error"], "unavailable_directory")

    def test_git_does_not_refresh_index_or_use_inherited_git_paths(self) -> None:
        # The CLI must override built-in fsmonitor too, including on Windows.
        self.git("config", "core.fsmonitor", "true")
        index = self.repo / ".git" / "index"
        before = (index.read_bytes(), index.stat().st_mtime_ns)
        (self.repo / "tracked.txt").write_bytes(b"working tree edit\n")
        with mock.patch.dict(os.environ, {"GIT_DIR": str(self.root / "fake-git"), "GIT_INDEX_FILE": str(self.root / "fake-index")}):
            data, code = snapshot.capture(self.config)
        self.assertEqual(code, 0)
        self.assertEqual(data["workspaces"][0]["tracked_change_count"], 1)
        self.assertEqual((index.read_bytes(), index.stat().st_mtime_ns), before)
        self.assertFalse((self.repo / ".git" / "index.lock").exists())

    @unittest.skipIf(os.name == "nt", "Execution proof uses a POSIX shell hook")
    def test_posix_fsmonitor_hook_is_not_called(self) -> None:
        hook = self.root / "private-fsmonitor-hook"
        evidence = self.root / "hook-executed"
        hook.write_text("#!/bin/sh\nprintf called > '" + str(evidence).replace("'", "'\\''") + "'\n", encoding="utf-8")
        hook.chmod(0o700)
        self.git("config", "core.fsmonitor", str(hook))
        index = self.repo / ".git" / "index"
        before = (index.read_bytes(), index.stat().st_mtime_ns)
        (self.repo / "tracked.txt").write_bytes(b"working tree edit\n")
        data, code = snapshot.capture(self.config)
        self.assertEqual(code, 0)
        self.assertEqual(data["workspaces"][0]["tracked_change_count"], 1)
        self.assertEqual((index.read_bytes(), index.stat().st_mtime_ns), before)
        self.assertFalse(evidence.exists())
        self.assertFalse((self.repo / ".git" / "index.lock").exists())

    def test_atomic_output_replacement_and_failure_preserves_previous_result(self) -> None:
        output = self.root / "output" / "workspace-state.json"
        output.parent.mkdir()
        output.write_text("previous result\n", encoding="utf-8")
        code, stdout, stderr = self.run_cli("--output", str(output))
        self.assertEqual((code, stdout, stderr), (0, "", ""))
        old = output.read_bytes()
        self.assertTrue(json.loads(old)["complete"])
        if os.name != "nt":
            self.assertEqual(stat.S_IMODE(output.stat().st_mode), 0o600)
        with mock.patch.object(snapshot.os, "replace", side_effect=OSError("private output path")):
            code, stdout, stderr = self.run_cli("--output", str(output))
        self.assertEqual(code, 2)
        self.assertEqual(stdout, "")
        self.assertEqual(stderr, "error: output_unavailable\n")
        self.assertEqual(output.read_bytes(), old)
        self.assertEqual(list(output.parent.glob(".workspace-snapshot-*")), [])
        self.assert_no_private_details(stderr)

    def test_config_and_cli_errors_are_sanitized(self) -> None:
        for invalid, category in (
            ({"schema_version": True, "workspaces": []}, "unsupported_config_version"),
            ({"schema_version": 1, "workspaces": [{"id": "/private/label", "path": "x"}]}, "invalid_workspace_id"),
            ({"schema_version": 1, "workspaces": [{"id": "valid", "path": "\x00private"}]}, "invalid_workspace_path"),
        ):
            with self.subTest(category=category):
                self.config.write_text(json.dumps(invalid), encoding="utf-8")
                code, text, stderr = self.run_cli()
                self.assertEqual((code, stderr), (2, ""))
                self.assertEqual(json.loads(text)["error"], category)
                self.assertNotIn("private/label", text)
        self.config.write_text("{\"private-secret\": invalid}", encoding="utf-8")
        code, text, stderr = self.run_cli()
        self.assertEqual((code, stderr), (2, ""))
        self.assertEqual(json.loads(text)["error"], "invalid_config_json")
        self.assertNotIn("private-secret", text)
        with self.assertRaises(SystemExit) as raised, redirect_stderr(io.StringIO()) as errors:
            snapshot.main(["--secret-private-argument", "private value"])
        self.assertEqual(raised.exception.code, 2)
        self.assertNotIn("private", errors.getvalue())

    def test_missing_git_and_timeout_are_sanitized(self) -> None:
        for error, category in (
            (FileNotFoundError("private executable path"), "git_unavailable"),
            (subprocess.TimeoutExpired("private command", 20, output=b"private content"), "git_timeout"),
        ):
            with self.subTest(category=category), mock.patch.object(snapshot.subprocess, "run", side_effect=error):
                data, code = snapshot.capture(self.config)
            self.assertEqual(code, 1)
            self.assertFalse(data["complete"])
            self.assertEqual(data["workspaces"][0], {"id": "example", "status": "error", "error": category})
            self.assertNotIn("private", json.dumps(data))

    def test_output_cannot_overwrite_config(self) -> None:
        original = self.config.read_bytes()
        code, stdout, stderr = self.run_cli("--output", str(self.config))
        self.assertEqual((code, stdout, stderr), (2, "", "error: output_would_overwrite_config\n"))
        self.assertEqual(self.config.read_bytes(), original)


class PorcelainParserTests(unittest.TestCase):
    def test_truncated_rename_and_invalid_output_are_rejected(self) -> None:
        for value in (b"R  new-name\x00", b"M  no-final-nul", b"private unexpected text\x00", b"?? \x00"):
            with self.subTest(value=value), self.assertRaises(snapshot.SnapshotError) as raised:
                snapshot.count_changes(value)
            self.assertEqual(str(raised.exception), "invalid_git_output")


if __name__ == "__main__":
    unittest.main()
