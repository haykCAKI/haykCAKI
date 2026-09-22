#!/usr/bin/env python3
"""Fail if a published profile file names a client or links a private repo.

Client names are stored as SHA-256 hashes of the lowercased word, so the
list in this public repository does not disclose them. Repository links are
checked against an allowlist of public repos, so private names never need to
be written down at all.

Usage: python3 scripts/check_confidential.py [FILE ...]
"""
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG = ROOT / ".github" / "confidential.json"
DEFAULT_FILES = ["README.md", "assets/*.svg"]

WORD = re.compile(r"[a-z0-9]+")
REPO_LINK = re.compile(r"(?:github\.com|githubusercontent\.com)/haykCAKI/([A-Za-z0-9_.-]+)", re.I)


def word_hash(word):
    return hashlib.sha256(word.lower().encode()).hexdigest()


def check(text, config, name="<text>"):
    blocked = set(config["blocked_word_sha256"])
    public = {repo.lower() for repo in config["public_repos"]}
    problems = []
    for n, line in enumerate(text.splitlines(), 1):
        for word in WORD.findall(line.lower()):
            if word_hash(word) in blocked:
                problems.append(f"{name}:{n}: blocked term '{word}'")
        for repo in REPO_LINK.findall(line):
            repo = repo.removesuffix(".git").rstrip(".")
            if repo.lower() not in public:
                problems.append(f"{name}:{n}: link to non-public repo '{repo}'")
    return problems


def main(argv):
    config = json.loads(CONFIG.read_text(encoding="utf-8"))
    paths = [Path(a) for a in argv] or [p for g in DEFAULT_FILES for p in sorted(ROOT.glob(g))]
    problems = []
    for path in paths:
        problems += check(path.read_text(encoding="utf-8"), config, str(path))
    for p in problems:
        print(p)
    print(f"{len(paths)} file(s) checked, {len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
