# Workflow: from BASE + Colab to this repo

Everything here works in a browser. No terminal or local Python needed.

## The weekly loop

```
 BASE explainer ──► ARENA Colab ──► Save to GitHub ──► NOTES.md ──► (table updates itself)
  read + self-check   do exercises    from Colab menu   5–10 lines     via GitHub Action
```

### 1. Read the BASE explainer (arena.baseresearch.org/weeks/…)
- Read it and run or edit its small examples. They run in BASE's browser runner, so
  nothing is saved; that's fine.
- **Answer the self-check questions in your own words before revealing the answers.**
  Write them straight into the "BASE explainer: self-check answers" part of that
  section's `NOTES.md` (step 4). This is your evidence for the explainer.
- If an edited example taught you something, paste the snippet into `NOTES.md` too.
- New terms → one line each in `notes/glossary.md` (optional).

### 2. Do the ARENA exercises in Colab
- Open the **exercises** Colab linked from the BASE week page (not the solutions one).
- **File → Save a copy in Drive** straight away and work in that copy. Otherwise your
  work can be lost or overwritten.
- Pick a GPU runtime only when the notebook asks for one.
- Do the week's core parts first, then stretch work. Using the solutions notebook when
  stuck is expected; note it in `NOTES.md`.
- When your key plot appears (e.g. loss/accuracy curve), right-click → save image as
  `key_result.png`.

### 3. Save the notebook to GitHub (end of every session)
In your Drive copy: **File → Save a copy in GitHub**, then:
- Repository: `<you>/gear-arena-portfolio`, branch `main`
- File path: the section folder + notebook name, e.g.
  `chapter0_fundamentals/0.2_cnns_resnets/0.2_CNNs_exercises.ipynb`
- Keep **Include a link to Colaboratory** ticked
- Commit message: what you did, e.g. `0.2: SimpleMLP passes tests`
- Click OK

Use the **same path every time** for that section. GitHub keeps each save as a new
version, so the history shows your steady progress. That history is evidence too.

### 4. Update the section's NOTES.md (on github.com)
Open the section folder on GitHub → `NOTES.md` → pencil icon ✏️:
- Fill in self-check answers, what you built, what you learned, where you got stuck.
- Upload your figure: in the section's `figures/` folder, **Add file → Upload files** →
  `key_result.png`.
- When the section is finished, set `status: done`, `completed: 2026-10-20`, `hours: 6`
  at the top, and paste your Colab link into `colab:`.
- **Commit changes.**

### 5. The progress table updates itself
Saving a `NOTES.md` triggers a GitHub Action that rebuilds the README progress table
within about a minute. Check the **Actions** tab if it doesn't appear.
Also tick off the week in `notes/weekly-log.md`.

## Starting a new week
1. Check `notes/weekly-log.md` for which ARENA section(s) the week covers.
2. On GitHub: **Add file → Create new file**, type the path, e.g.
   `chapter1_transformer_interp/1.1_transformers_from_scratch/NOTES.md`
   (typing `/` creates folders), paste in `templates/SECTION_NOTES.md`, and fill in
   `section`, `title` and `base_week` at the top. Commit.
   - Weeks with two sections (e.g. week 5: 1.4.1 and 1.4.2) get two folders.
   - If you do have Python locally: `python scripts/new_section.py 1.1 "Transformers from scratch" --week 2`.
3. Put the folder link in the week's row of `notes/weekly-log.md`.

## Background: how ARENA's material is set up
- Each ARENA section has an **exercises** Colab (blank functions to fill in) and a
  **solutions** Colab (reference). Only save your exercises notebook here.
- ARENA's own repo (now `ARENA-education/ARENA_materials`) has one folder per section,
  with both notebooks plus `solutions.py`, `tests.py` and `utils.py`. This repo mirrors
  that one-folder-per-section layout, using ARENA's section numbers.
- BASE links point to ARENA's live `main` branch, so a notebook can change later.
  Optionally record the commit hash in `arena_commit:`.

## Keep it clean
- **Never commit API keys.** From week 9 (evals) you'll use OpenAI/Anthropic keys: store
  them in Colab **Secrets** (🔑 in the left sidebar) and read them with
  `from google.colab import userdata; userdata.get("OPENAI_API_KEY")`. Check no key
  appears in a cell or output before saving to GitHub.
- **Big notebooks:** if one is over about 20 MB, clear the heaviest outputs first (keep
  the ones that show results).
- No model weights or datasets in the repo. Link to W&B runs in `NOTES.md` instead.

## Turning it into a portfolio
- After each chapter, add your best 1–2 results to **Highlights** in the README.
- Anything beyond the exercises goes in `projects/`. One small extension tied to your
  own research beats ten more finished notebooks.
- Pin the repo on your GitHub profile and link it from your CV.
