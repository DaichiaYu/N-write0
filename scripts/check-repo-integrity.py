#!/usr/bin/env python3
"""Read-only structural checker for N-write0."""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WRITING = ROOT / "writing"


@dataclass
class Issue:
    level: str
    path: str
    message: str


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def frontmatter(text: str) -> dict[str, object]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end == -1:
        return {}
    data: dict[str, object] = {}
    current_key: str | None = None
    current_list: list[str] | None = None
    for line in text[4:end].splitlines():
        raw = line.rstrip()
        if not raw.strip():
            continue
        if raw.startswith("  - ") and current_key and current_list is not None:
            current_list.append(raw[4:].strip().strip('"'))
            data[current_key] = current_list
            continue
        if raw.startswith("  "):
            continue
        if ":" in raw:
            key, value = raw.split(":", 1)
            current_key = key.strip()
            value = value.strip()
            if not value:
                current_list = []
                data[current_key] = current_list
            else:
                current_list = None
                data[current_key] = value.strip('"')
    return data


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def check_required(issues: list[Issue]) -> None:
    required = [
        ROOT / "AGENTS.md",
        WRITING / "目錄.md",
        WRITING / "article-index.md",
        WRITING / "01-inbox" / "writing-dashboard.md",
        WRITING / "01-inbox" / "topic-candidates.md",
        WRITING / "08-ai-consensus" / "consensus-candidates.md",
    ]
    for path in required:
        if not path.exists():
            issues.append(Issue("ERROR", rel(path), "Required entry file is missing."))


def check_drafts(issues: list[Issue]) -> None:
    drafts = WRITING / "02-drafts"
    if not drafts.exists():
        return
    for path in drafts.rglob("*.md"):
        if path.name == "README.md":
            continue
        fm = frontmatter(read_text(path))
        if not fm:
            continue
        parts = path.relative_to(drafts).parts
        if not (len(parts) >= 3 and re.fullmatch(r"20\d\d", parts[0]) and re.fullmatch(r"\d\d", parts[1])):
            issues.append(Issue("WARN", rel(path), "Formal draft is not inside YYYY/MM."))
        content_id = str(fm.get("content_id", ""))
        language = str(fm.get("language", ""))
        if content_id and language:
            suffix = f".{language}.md"
            expected = path.name[:-len(suffix)] if path.name.endswith(suffix) else path.stem
            if content_id != expected:
                issues.append(Issue("WARN", rel(path), "content_id does not match filename stem."))
        primary_moc = str(fm.get("primary_moc", ""))
        if primary_moc and not (WRITING / "06-concepts" / f"{primary_moc}.md").exists():
            issues.append(Issue("ERROR", rel(path), f"Missing primary MOC: {primary_moc}"))
        series = str(fm.get("series", ""))
        if series:
            slug = re.sub(r"[^a-z0-9]+", "-", series.lower()).strip("-")
            if not (WRITING / "05-series" / slug / "README.md").exists():
                issues.append(Issue("WARN", rel(path), f"Series index may be missing: {slug}"))


def check_series(issues: list[Issue]) -> None:
    root = WRITING / "05-series"
    if not root.exists():
        return
    for path in root.glob("*.md"):
        if path.name != "README.md":
            issues.append(Issue("WARN", rel(path), "Use <series-slug>/README.md instead of flat files."))


def main() -> int:
    issues: list[Issue] = []
    check_required(issues)
    check_drafts(issues)
    check_series(issues)
    if not issues:
        print("OK: no obvious N-write0 integrity issues found.")
        return 0
    for issue in issues:
        print(f"{issue.level}: {issue.path}: {issue.message}")
    return 1 if any(issue.level == "ERROR" for issue in issues) else 0


if __name__ == "__main__":
    sys.exit(main())
