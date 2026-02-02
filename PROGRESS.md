# PROGRESS

## Current Focus
- Interview materials for Traditional ML and Generative AI implementation.
- Stabilize notebook imports with a reusable repo-root path helper.
- Expand Random Forest regression example with diagnostics and tuning.

## Milestones
- Define anonymized interview section structure and scoring rubric.
- Create interview section documents under `Interview/`.
- Link materials from `AI interview discussion.md` and `README.md`.
- Add interview notebooks for GenAI (junior/mid/senior) with telemetry.
- Standardize notebook bootstrap cells and add guard tests.

## Backlog
- Add answer keys and reviewer guidance once notebook exercises are finalized.

## Known Issues
- None recorded.

## Decisions
- Company and project names are anonymized in new interview materials.
- Interview sections focus on fundamentals and adaptability over tool lock-in.
- Notebooks add the repo root to `sys.path` via `src/utils/pathing.py`.
- Regression sections include baselines, multiple metrics, and residual analysis.
- GenAI interview notebooks use YAML configs and timestamped logs for reproducibility.