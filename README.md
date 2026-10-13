# GEAR × ARENA — Akiya Hoken's working portfolio

My completed exercises, notes and results from working through the
[ARENA](https://github.com/ARENA-education/ARENA_materials) technical AI-safety curriculum
(ML fundamentals → transformer interpretability → RL → LLM evaluations → alignment science),
following BASE's [ARENA in 12 Weeks](https://arena.baseresearch.org) course.
Week-by-week plan: [notes/weekly-log.md](notes/weekly-log.md).

Every section folder holds the notebook I actually ran, a short write-up in my own words,
and at least one figure or number showing the code works.

**Why I'm doing this:** I research how people come to rely on AI for thinking and emotional
support, and how to measure it. This course is how I'm building the engineering side:
interpretability and evals are the tools I want for asking whether models act in users'
interests in mental-health conversations.

## Highlights
<!-- Fill in as you go: 3–5 best pieces of work, each one line + link. Recruiters read this first. -->
- _Coming soon._

## Progress
<!-- Updates automatically (GitHub Action) whenever a NOTES.md changes. Don't edit by hand. -->
<!-- PROGRESS:START -->
**0 / 1 sections done**

| Week | Section | Title | Status | Completed | Hours | Notebook |
|---|---|---|---|---|---|---|
| 1 | 0.2 | [CNNs & ResNets](chapter0_fundamentals/0.2_cnns_resnets/NOTES.md) | 🟡 in progress | — | — | — |
<!-- PROGRESS:END -->

## Repo layout
```
chapter0_fundamentals/          0.x  tensors, CNNs, optimisation, backprop, VAEs/GANs
chapter1_transformer_interp/    1.x  transformers from scratch, mech interp, probes/SAEs, circuits
chapter2_rl/                    2.x  RL foundations, DQN, PPO, RLHF
chapter3_llm_evals/             3.x  eval design, dataset generation, Inspect, agents, AI control
chapter4_alignment_science/     4.x  misalignment, reasoning models, model-behaviour investigations
  └── <X.Y>_<topic>/
        ├── <X.Y>_..._exercises.ipynb   my completed Colab (saved straight from Colab)
        ├── NOTES.md                    what I built, key result, what I learned, where I got stuck
        └── figures/                    plots used as evidence
projects/        mini-projects and extensions that go beyond the exercises
notes/           weekly log, glossary, session notes
scripts/         new_section.py (scaffold a section), update_progress.py (rebuild table above)
.github/         the Action that runs update_progress.py for you
templates/       NOTES.md template
WORKFLOW.md      how work gets from Colab into this repo
```

Folder numbers match ARENA's section numbers, not GEAR week numbers, so links stay
stable if the course order changes. `notes/weekly-log.md` maps weeks to sections.

## Credits
Exercises, solutions and starter code are from ARENA (Callum McDougall and the ARENA team),
used for learning. My own work is the completed exercises, write-ups, figures and projects.
