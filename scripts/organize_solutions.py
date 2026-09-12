#!/usr/bin/env python3
"""
organize_solutions.py

Reorganizes a PushMyCode-pushed repo so that:
  - GFG (GeeksforGeeks) problems go into "GFG Solutions/"
  - Everything else is split into top-level "DSA/" or "SQL/"
    based on the language of the solution file
  - The existing easy/medium/hard difficulty grouping (if present)
    is preserved underneath.

Safe to run repeatedly (idempotent) and preserves git history by
using `git mv` when run inside a git repository.

Usage:
    python3 scripts/organize_solutions.py            # do it
    python3 scripts/organize_solutions.py --dry-run   # preview only
"""
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# Folder names that should never be touched / recursed into.
IGNORE_DIRS = {".git", ".github", "scripts", "node_modules", "DSA", "SQL", "GFG Solutions"}

DIFFICULTIES = {"easy", "medium", "hard"}

# extension -> is this SQL?
SQL_EXTENSIONS = {".sql"}

PLATFORM_PATTERNS = [
    ("gfg", re.compile(r"geeksforgeeks\.(com|org)", re.I)),
    ("hackerrank", re.compile(r"hackerrank\.com", re.I)),
    ("leetcode", re.compile(r"leetcode\.com", re.I)),
    ("codechef", re.compile(r"codechef\.com", re.I)),
]


def is_git_repo(path: Path) -> bool:
    return (path / ".git").exists()


def detect_platform(readme_text: str, path_parts) -> str:
    for name, pattern in PLATFORM_PATTERNS:
        if pattern.search(readme_text):
            return name
    # fallback: look at folder names already in the path (e.g. "gfg", "hackerrank")
    lowered = [p.lower() for p in path_parts]
    for name, _ in PLATFORM_PATTERNS:
        if name in lowered:
            return name
    return "unknown"


def detect_is_sql(files, readme_text: str) -> bool:
    for f in files:
        if f.suffix.lower() in SQL_EXTENSIONS:
            return True
    m = re.search(r"\*\*Language:\*\*\s*([A-Za-z0-9+#]+)", readme_text, re.I)
    if m and "sql" in m.group(1).lower():
        return True
    return False


def find_difficulty(path_parts):
    for p in path_parts:
        if p.lower() in DIFFICULTIES:
            return p.lower()
    return None


def is_problem_leaf(dirpath: Path, filenames) -> bool:
    """A leaf problem folder = has a README.md AND at least one other file,
    and none of its immediate children are directories we'd want to recurse into."""
    lower_names = {f.lower() for f in filenames}
    has_readme = "readme.md" in lower_names
    has_other_file = any(f.lower() != "readme.md" for f in filenames)
    return has_readme and has_other_file


def build_target(rel_parts, slug, difficulty, platform, is_sql) -> Path:
    if platform == "gfg":
        top = "GFG Solutions"
    else:
        top = "SQL" if is_sql else "DSA"

    if difficulty:
        return Path(top) / difficulty / slug
    return Path(top) / slug


def move_folder(src: Path, dst: Path, use_git: bool, dry_run: bool):
    if src.resolve() == dst.resolve():
        return False  # already in place

    if dst.exists():
        print(f"  ! SKIP (target already exists): {dst}")
        return False

    print(f"  {src.relative_to(REPO_ROOT)}  ->  {dst.relative_to(REPO_ROOT)}")
    if dry_run:
        return True

    dst.parent.mkdir(parents=True, exist_ok=True)

    if use_git:
        result = subprocess.run(
            ["git", "mv", str(src.relative_to(REPO_ROOT)), str(dst.relative_to(REPO_ROOT))],
            cwd=REPO_ROOT, capture_output=True, text=True,
        )
        if result.returncode != 0:
            print(f"    git mv failed ({result.stderr.strip()}), falling back to plain move")
            shutil.move(str(src), str(dst))
    else:
        shutil.move(str(src), str(dst))
    return True


def cleanup_empty_dirs(root: Path):
    """Remove now-empty directories left behind after moving problem folders out."""
    for dirpath, dirnames, filenames in os.walk(root, topdown=False):
        p = Path(dirpath)
        if p == root:
            continue
        if p.name in IGNORE_DIRS or any(part in IGNORE_DIRS for part in p.relative_to(root).parts):
            continue
        try:
            if not any(p.iterdir()):
                p.rmdir()
        except OSError:
            pass


def main():
    dry_run = "--dry-run" in sys.argv
    use_git = is_git_repo(REPO_ROOT) and shutil.which("git") is not None

    moved_any = False

    # Walk top-down but skip our own target/ignored directories.
    for dirpath, dirnames, filenames in os.walk(REPO_ROOT, topdown=True):
        dirnames[:] = [d for d in dirnames if d not in IGNORE_DIRS]
        p = Path(dirpath)
        rel_parts = p.relative_to(REPO_ROOT).parts
        if any(part in IGNORE_DIRS for part in rel_parts):
            continue

        if not is_problem_leaf(p, filenames):
            continue

        readme_path = p / "README.md"
        readme_text = readme_path.read_text(errors="ignore") if readme_path.exists() else ""
        files = [p / f for f in filenames]

        platform = detect_platform(readme_text, rel_parts)
        is_sql = detect_is_sql(files, readme_text)
        difficulty = find_difficulty(rel_parts)
        slug = p.name

        target = REPO_ROOT / build_target(rel_parts, slug, difficulty, platform, is_sql)

        if move_folder(p, target, use_git, dry_run):
            moved_any = True
        # prevent os.walk from descending into a folder we just moved
        dirnames[:] = []

    if not dry_run:
        cleanup_empty_dirs(REPO_ROOT)

    if not moved_any:
        print("Nothing to reorganize — repo already sorted.")
    elif dry_run:
        print("\n(dry run — no files were actually moved)")


if __name__ == "__main__":
    main()
