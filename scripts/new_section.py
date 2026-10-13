#!/usr/bin/env python3
"""Scaffold a folder for one ARENA section.

Usage:
    python scripts/new_section.py 1.2 "Intro to mech interp"
    python scripts/new_section.py 0.2 "CNNs & ResNets" --week 1 --colab https://colab.research.google.com/...

Creates  chapterN_<name>/<X.Y>_<slug>/  with NOTES.md (from the template)
and an empty figures/ folder. Never overwrites an existing NOTES.md.
"""
import argparse
import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHAPTERS = {
    "0": "chapter0_fundamentals",
    "1": "chapter1_transformer_interp",
    "2": "chapter2_rl",
    "3": "chapter3_llm_evals",
    "4": "chapter4_alignment_science",
}


def slugify(text: str) -> str:
    text = re.sub(r"[^\w\s-]", "", text.lower())
    return re.sub(r"[\s-]+", "_", text).strip("_")


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("section", help='ARENA section number, e.g. "1.2" or "1.4.1"')
    p.add_argument("title", help="Section title")
    p.add_argument("--colab", default="", help="Link to your saved Colab copy")
    p.add_argument("--commit", default="", help="ARENA commit hash the notebook came from")
    p.add_argument("--week", default="", help="BASE course week number (1-12)")
    args = p.parse_args()

    chapter = args.section.split(".")[0]
    if chapter not in CHAPTERS:
        raise SystemExit(f"Unknown chapter '{chapter}'. Expected one of {sorted(CHAPTERS)}.")

    folder = ROOT / CHAPTERS[chapter] / f"{args.section}_{slugify(args.title)}"
    (folder / "figures").mkdir(parents=True, exist_ok=True)
    (folder / "figures" / ".gitkeep").touch()

    notes = folder / "NOTES.md"
    if notes.exists():
        print(f"Already exists, left untouched: {notes.relative_to(ROOT)}")
        return

    t = (ROOT / "templates" / "SECTION_NOTES.md").read_text()
    t = t.replace('section: "X.Y"', f'section: "{args.section}"')
    t = t.replace('title: "Section title"', f'title: "{args.title}"')
    t = t.replace("base_week:      ", f"base_week: {args.week}", 1)
    t = t.replace("status: not-started", "status: in-progress")
    t = t.replace("started:   ", f"started: {date.today().isoformat()}", 1)
    t = t.replace('colab: ""', f'colab: "{args.colab}"')
    t = t.replace('arena_commit: ""', f'arena_commit: "{args.commit}"')
    t = t.replace("# X.Y Section title", f"# {args.section} {args.title}")
    notes.write_text(t)
    print(f"Created {folder.relative_to(ROOT)}/")


if __name__ == "__main__":
    main()
