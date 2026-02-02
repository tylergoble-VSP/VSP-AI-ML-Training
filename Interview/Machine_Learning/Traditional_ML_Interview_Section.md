# Traditional ML Interview Section

## Purpose
- Assess traditional ML fundamentals, statistical reasoning, and model validation discipline.
- Favor adaptability and core logic over framework-specific recipes.

## Anonymized Role Alignment
- Project_A: Embeddings + classification models for business decision support.
- Project_B: Embeddings + clustering for segmentation and discovery.
- Note: All company and project names are anonymized in this document.

## Skill Matrix and 1-5 Scoring Rubric
Scoring scale (apply per skill area):
- 1: No working knowledge; cannot explain basic terms.
- 2: Surface-level familiarity; struggles to apply concepts.
- 3: Competent; can apply standard techniques with guidance.
- 4: Strong; explains tradeoffs and validates results.
- 5: Expert; anticipates failure modes and designs robust evaluation.

Skill areas:
- Python fundamentals for data workflows (dataframes, vectorization, debugging).
- ML problem framing (supervised vs unsupervised vs survival/reinforcement).
- Feature engineering and data leakage detection.
- Model selection and bias/variance tradeoffs.
- Evaluation metrics (classification, regression, clustering).
- Statistical assumptions and diagnostics (residuals, homoscedasticity, multicollinearity).
- Drift monitoring and retraining strategy.
- Communication: explain model behavior in business terms.

## Sample Questions (Fundamentals + Applied Reasoning)
Fundamentals:
- When would you choose a classifier vs a clustering model for a business question?
- Explain homoscedasticity to a non-technical stakeholder.
- What does data leakage look like, and how do you detect it?

Applied reasoning:
- Given a churn dataset with class imbalance, what metrics and techniques do you use?
- You see a sudden performance drop in production. What is your triage plan?
- How would you validate that a clustering solution is meaningful for operations?

Debugging and adaptability:
- Show a small pipeline with a subtle bug (leakage or label shift) and ask the candidate to identify the issue.
- Ask them to replace one model type with another and justify the tradeoffs.

### Scored Answer Examples (1-5) per Question

1) When would you choose a classifier vs a clustering model for a business question?
- 1: "Classifier is always better."
- 2: "Classifier is for labeled data, clustering is when you don't have labels."
- 3: "Use classification when the target label exists; clustering for grouping without labels."
- 4: "Classifier when you need predicted outcomes; clustering for segmentation discovery and hypothesis generation."
- 5: "Classifier for decision automation with labeled outcomes; clustering for exploratory segmentation, then validate usefulness with business KPIs and stability checks."

2) Explain homoscedasticity to a non-technical stakeholder.
- 1: "It's a math thing about errors."
- 2: "It means the model errors are kind of even."
- 3: "The prediction errors stay about the same across the range of data."
- 4: "Errors are consistently sized; if they grow, the model becomes less reliable at certain values."
- 5: "Error spread is stable across inputs; if not, certain segments are riskier, so we re-check assumptions or transform data."

3) What does data leakage look like, and how do you detect it?
- 1: "It happens when data leaks."
- 2: "When test data is used in training."
- 3: "Leakage is when future or target info sneaks into features; detect by checking feature sources and timing."
- 4: "Look for unrealistically high metrics, validate time splits, and inspect features for post-outcome fields."
- 5: "Use strict time-based splits, feature audits, and leakage tests; explain how leakage inflates metrics and fails in production."

4) Given a churn dataset with class imbalance, what metrics and techniques do you use?
- 1: "Accuracy."
- 2: "Maybe precision."
- 3: "Use precision, recall, F1, and consider class weights or resampling."
- 4: "Use PR-AUC, confusion matrix, threshold tuning, and stratified splits."
- 5: "PR-AUC + cost-sensitive thresholds, class weighting or SMOTE with caution, and calibrate probabilities for business actions."

5) You see a sudden performance drop in production. What is your triage plan?
- 1: "Retrain the model."
- 2: "Check the data."
- 3: "Compare training vs production data; check drift and pipeline changes."
- 4: "Validate data integrity, monitor drift metrics, and confirm feature distributions and label delays."
- 5: "Run a systematic triage: data pipeline health, drift diagnostics, label lag, and rollback plan; document findings and remediation."

6) How would you validate that a clustering solution is meaningful for operations?
- 1: "If it looks good on a plot."
- 2: "If the clusters are separated."
- 3: "Use silhouette or similar metrics and check business interpretability."
- 4: "Combine stability checks, silhouette, and business validation with downstream outcomes."
- 5: "Validate with stability over time, business KPIs, stakeholder review, and testing impact on operational decisions."

## Hands-On Notebook Plan (Interview Exercise)
Notebook goal: validate ML fundamentals, debugging, and evaluation clarity.

Proposed notebook location and naming:
- `notebooks/interview/01_Traditional_ML_Interview.ipynb`

Run order guidance (required in notebook):
1. Load data and inspect schema and distributions.
2. Define target + baseline split.
3. Train a baseline model and log metrics.
4. Perform diagnostics (assumptions, residuals, leakage checks).
5. Improve model with feature engineering.
6. Summarize results in business terms.

Candidate tasks:
- Implement a train/validation split and justify it.
- Compute and interpret at least two metrics.
- Diagnose at least one failure mode (e.g., leakage or drift).
- Write a short business summary paragraph.

Expected outcomes:
- Reproducible pipeline and clear evaluation logic.
- Clear rationale for model choice and metrics.

## Evaluation Criteria (Anti-Recipe Checks)
- Can the candidate justify why a model is appropriate for the problem?
- Do they identify assumptions and how to verify them?
- Can they reason about metrics beyond “higher is better”?
- Do they explain results in plain business language?

## Traceability Notes
- Use timestamped outputs for any generated artifacts:
  - `outputs/results/ml_interview_metrics_<YYYYMMDD_HHMMSSZ>.csv`
  - `outputs/logs/ml_interview_notes_<YYYYMMDD_HHMMSSZ>.md`
- Record seed, dataset fingerprint, and model choice in a metadata sidecar:
  - `outputs/results/ml_interview_metadata_<YYYYMMDD_HHMMSSZ>.json`

## Detailed Evaluation Plan (Traditional ML Skills)

### 1) Pre-Interview Setup (Internal)
- Choose a role focus: Project_A (embeddings + classification) or Project_B (embeddings + clustering).
- Select a small, fixed dataset that matches the focus and is easy to explain.
- Prepare a clean baseline notebook and a variant with one subtle issue (leakage or label shift).
- Predefine the evaluation rubric and scoring sheet (1-5 per skill area).

### 2) Interview Flow and Timing (60-75 minutes)
1. Context and role framing (5 min)
2. Fundamentals and reasoning questions (15-20 min)
3. Hands-on notebook exercise (25-30 min)
4. Debugging and tradeoff discussion (10-15 min)
5. Business communication summary (5 min)

### 3) Scoring Structure (1-5 per category)
Score each category independently, then compute an overall score.
- Core ML fundamentals
- Data quality and leakage awareness
- Model selection and evaluation
- Debugging and adaptability
- Business communication

### 4) Fundamentals and Reasoning (Question Sheet)
Use the existing sample questions and scored examples.
Add follow-ups to probe depth:
- Ask for concrete examples of failures they have seen.
- Ask how they would verify assumptions.
- Ask what tradeoffs they would accept and why.

### 5) Hands-On Notebook Exercise
Goal: verify practical competence and structured thinking.
Required tasks:
- Load and inspect data (shape, missing values, class balance).
- Define a baseline model and evaluate with at least two metrics.
- Identify one potential risk (leakage, bias, or drift).
- Improve the model or evaluation approach with a clear rationale.
Expected outputs:
- Metrics table and a brief written summary.
- One visual diagnostic (confusion matrix, residual plot, or cluster plot).

### 6) Debugging and Adaptability
Provide a small pipeline with a hidden issue.
Expected actions:
- Detect the issue through reasoning or targeted checks.
- Explain why it is harmful in production.
- Propose a fix and validate the improvement.

### 7) Business Communication Check
Ask for a 3-5 sentence summary:
- Problem framing in business terms
- Why the chosen model is appropriate
- Key risks and monitoring plan

### 8) Pass/Borderline/Reject Guidelines
- Pass: Scores 3+ in all categories, at least one category at 4+.
- Borderline: One category at 2 but shows strong growth signals.
- Reject: Multiple categories at 1-2 with weak reasoning or inability to explain.

### 9) Post-Interview Documentation
- Complete the scoring sheet and short notes.
- Save artifacts using the traceability naming rules.
- Record any decisions in a short summary for hiring review.
