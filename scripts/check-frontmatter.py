#!/usr/bin/env python3
"""check-frontmatter.py — validate chapter frontmatter and directory parity."""

import os
import re
import sys
import tomllib
from pathlib import Path

SRC_ZH = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("src/zh")
SRC_EN = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("src/en")

VALID_DIFFICULTY = {"★", "★★", "★★★"}
VALID_STATUS = {"complete", "draft", "planned", "missing"}
VALID_PATHS = {"green", "blue", "red"}
PREREQ_RE = re.compile(r"^[IVX]+-\d{2}$")

SPECIAL_FILES = {"preface.md", "bibliography.md", "index.md"}
SKIP_FILES = {"SUMMARY.md"}

errors = []


def parse_frontmatter(filepath: Path) -> dict | None:
    """Extract TOML frontmatter between --- markers."""
    text = filepath.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None
    end = text.find("---", 3)
    if end == -1:
        return None
    try:
        return tomllib.loads(text[3:end])
    except Exception as e:
        errors.append(f"{filepath}: invalid TOML frontmatter: {e}")
        return None


def check_chapter(filepath: Path, fm: dict):
    rel = filepath.relative_to(filepath.parents[2])  # relative to src/zh or src/en
    lang = "zh" if "/zh/" in str(filepath) else "en"

    # difficulty
    diff = fm.get("difficulty")
    if diff and diff not in VALID_DIFFICULTY:
        errors.append(f"{rel}: invalid difficulty '{diff}'")
    elif not diff and filepath.name not in SPECIAL_FILES:
        errors.append(f"{rel}: missing difficulty")

    # prerequisites (format + existence)
    prereqs = fm.get("prerequisites", [])
    src_dir = filepath.parents[1]  # src/zh or src/en
    for pr in prereqs:
        if not PREREQ_RE.match(pr):
            errors.append(f"{rel}: invalid prerequisite format '{pr}'")
        else:
            # Check referenced chapter exists
            part_num = pr.split("-")[0]  # e.g., "II"
            ch_num = int(pr.split("-")[1])  # e.g., 03
            parts_map = {"I":"01-life","II":"02-foundations","III":"03-analytic-nt",
                         "IV":"04-zeta","V":"05-rh","VI":"06-generalizations","VII":"07-reflections"}
            part_dir = parts_map.get(part_num, "")
            found = False
            for f in src_dir.rglob(f"part-{part_dir}/*.md"):
                if f"chapter-{ch_num:02d}" in f.name:
                    found = True
                    break
            if not found:
                errors.append(f"{rel}: prerequisite {pr} references non-existent chapter")

    # paths
    paths = fm.get("paths", [])
    for p in paths:
        if p not in VALID_PATHS:
            errors.append(f"{rel}: invalid path '{p}'")

    # keywords
    keywords = fm.get("keywords", [])
    if keywords and filepath.name not in SPECIAL_FILES:
        if len(keywords) < 2:
            errors.append(f"{rel}: keywords need at least 2, got {len(keywords)}")
        if len(keywords) > 6:
            errors.append(f"{rel}: keywords max 6, got {len(keywords)}")

    # status fields
    for status_field in ("zh-status", "en-status"):
        val = fm.get(status_field)
        if val and val not in VALID_STATUS:
            errors.append(f"{rel}: invalid {status_field} '{val}'")

    # missing-note required when status=missing
    for status_field, note_field in [("zh-status", "zh-missing-note"), ("en-status", "en-missing-note")]:
        if fm.get(status_field) == "missing":
            note = fm.get(note_field)
            if not note or not str(note).strip():
                errors.append(f"{rel}: {status_field}=missing but {note_field} is empty")


def main():
    all_files = set()

    for lang_dir in (SRC_ZH, SRC_EN):
        if not lang_dir.exists():
            continue
        for md_file in lang_dir.rglob("*.md"):
            all_files.add(md_file.relative_to(lang_dir))
            fm = parse_frontmatter(md_file)
            if md_file.name in SKIP_FILES:
                continue
            if fm is None:
                errors.append(f"{md_file.relative_to(lang_dir.parent)}: missing or broken frontmatter")
                continue
            check_chapter(md_file, fm)

    # Directory parity: every .md in zh has a counterpart in en (and vice versa)
    zh_files = {f for f in all_files if (SRC_ZH / f).exists()}
    en_files = {f for f in all_files if (SRC_EN / f).exists()}

    for f in zh_files - en_files:
        fname = Path(f).name
        if fname not in SPECIAL_FILES and fname != "SUMMARY.md":
            errors.append(f"PARITY: {f} exists in zh/ but not en/")

    for f in en_files - zh_files:
        fname = Path(f).name
        if fname not in SPECIAL_FILES and fname != "SUMMARY.md":
            errors.append(f"PARITY: {f} exists in en/ but not zh/")

    if errors:
        print(f"\n{len(errors)} validation error(s):\n")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    else:
        print("All frontmatter valid. Directory parity: OK.")
        sys.exit(0)


if __name__ == "__main__":
    main()
