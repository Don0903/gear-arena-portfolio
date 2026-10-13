#!/usr/bin/env python3
"""Rebuild the progress table in README.md from every section's NOTES.md.

Usage:
    python scripts/update_progress.py

Reads the front matter at the top of each chapter*/<section>/NOTES.md and writes
a table between the PROGRESS:START / PROGRESS:END markers in README.md.
Standard library only, so it also runs in Colab or a GitHub Action.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
START, END = "<!-- PROGRESS:START -->", "<!-- PROGRESS:END -->"
STATUS_ICON = {"done": "✅ done", "in-progress": "🟡 in progress", "not-started": "⚪ not started"}


def front_matter(text: str) -> dict:
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    data = {}
    if not m:
        return data
    for line in m.group(1).splitlines():
        if ":" not in line:
            continue
        key, val = line.split(":", 1)
        val = re.sub(r"\s+#.*$", "", val).strip().strip('"').strip("'")
        data[key.strip()] = val
    return data


def section_key(s: str):
    return [int(x) if x.isdigit() else x for x in s.split(".")]


def build_table() -> str:
    rows = []
    for notes in ROOT.glob("chapter*/*/NOTES.md"):
        fm = front_matter(notes.read_text())
        if not fm.get("section"):
            continue
        rel = notes.parent.relative_to(ROOT).as_posix()
        colab = fm.get("colab", "")
        rows.append((
            section_key(fm["section"]),
            f"| {fm.get('base_week', '') or '—'} "
            f"| {fm['section']} | [{fm.get('title', '')}]({rel}/NOTES.md) "
            f"| {STATUS_ICON.get(fm.get('status', ''), fm.get('status', ''))} "
            f"| {fm.get('completed', '') or '—'} "
            f"| {fm.get('hours', '') or '—'} "
            f"| {'[open](' + colab + ')' if colab else '—'} |",
        ))
    if not rows:
        return "_No sections started yet. Run `python scripts/new_section.py 0.0 \"Prerequisites\"`._"
    done = sum("✅" in r for _, r in rows)
    header = (f"**{done} / {len(rows)} sections done**\n\n"
              "| Week | Section | Title | Status | Completed | Hours | Notebook |\n"
              "|---|---|---|---|---|---|---|")
    return header + "\n" + "\n".join(r for _, r in sorted(rows))


def main() -> None:
    readme = README.read_text()
    if START not in readme or END not in readme:
        raise SystemExit("README.md is missing the PROGRESS markers.")
    before, rest = readme.split(START, 1)
    _, after = rest.split(END, 1)
    README.write_text(f"{before}{START}\n{build_table()}\n{END}{after}")
    print("README progress table updated.")


if __name__ == "__main__":
    main()
