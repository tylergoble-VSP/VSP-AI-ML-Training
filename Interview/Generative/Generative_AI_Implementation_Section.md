# Generative AI Implementation Section

## Purpose
- Assess ability to design and implement generative AI systems with reproducibility, traceability, and safety.
- Emphasize fundamentals (tokenization, generation, evaluation) over tool lock-in.

## Anonymized Role Alignment
- Project_A: Embeddings + LLM-based generation for assistive workflows.
- Project_B: Embeddings + clustering + retrieval for knowledge discovery.
- Note: All company and project names are anonymized in this document.

## Skill Matrix and 1-5 Scoring Rubric
Scoring scale (apply per skill area):
- 1: No working knowledge; cannot explain basic terms.
- 2: Surface-level familiarity; struggles to apply concepts.
- 3: Competent; can implement standard pipelines with guidance.
- 4: Strong; explains tradeoffs and validates outputs.
- 5: Expert; anticipates failure modes and designs robust evaluation.

Skill areas:
- Tokenization and context management (padding, truncation, max length).
- Model loading and device strategy (dtype, device_map, quantization).
- Generation control (temperature, top_p, top_k, repetition_penalty).
- Prompt design and structured outputs.
- Retrieval-Augmented Generation (chunking, embeddings, retrieval).
- Evaluation (metrics + golden prompts).
- Telemetry and token accounting.
- Safety and data handling (redaction, privacy).

## Evaluation Tracks (Junior / Mid / Senior)
Each track has a distinct scope, exercise, and expected artifacts. Use the shared 1–5 rubric but weight skills differently per track.

### Junior Track (Implementation Fundamentals)
Primary focus:
- Tokenization basics, model loading, deterministic generation, and token counting.
- Clear config usage (no hard-coded IDs or magic numbers).

Required artifacts:
- Config file (YAML) with model_id, tokenizer_id, seed, generation defaults.
- Minimal generation run with token accounting logs.
- Short write-up explaining parameter choices.

Rubric emphasis (high weight):
- Tokenization and context management
- Model loading and device strategy
- Telemetry and token accounting

### Mid Track (RAG + Evaluation)
Primary focus:
- Add embeddings, simple retrieval, and evaluation using golden prompts.
- Explain RAG vs fine-tuning tradeoffs with evidence.

Required artifacts:
- Small retrieval corpus + chunking strategy
- Embedding + retrieval pipeline
- Golden prompt evaluation summary

Rubric emphasis (high weight):
- Retrieval-Augmented Generation
- Evaluation (metrics + golden prompts)
- Safety and data handling

### Senior Track (Robustness + Traceability)
Primary focus:
- End-to-end reproducibility, failure mode analysis, and deterministic settings.
- Design for traceability and auditability.

Required artifacts:
- Telemetry logs with timestamps, seed, and model metadata
- Error handling for config validation and model load failures
- Written analysis of nondeterminism and mitigations

Rubric emphasis (high weight):
- Telemetry and token accounting
- Evaluation (metrics + golden prompts)
- Safety and data handling

## Sample Questions (Implementation + Reasoning)
Implementation:
- Explain how you would load a model and tokenizer without hard-coding IDs.
- Describe how you would count prompt vs completion tokens for local models.
- What logs would you persist for reproducibility and why?

Reasoning:
- When should you prefer RAG over fine-tuning?
- How do you detect hallucinations or factual drift in generated answers?
- What does “deterministic enough” mean when using GPU generation?

Debugging and adaptability:
- Given a generation pipeline producing inconsistent outputs, identify likely causes.
- Replace a framework-specific agent tool with a minimal custom loop.

### Scored Answer Examples (1-5) per Question

1) Explain how you would load a model and tokenizer without hard-coding IDs.
- 1: "I just put the model name in the code and load it."
- 2: "I'd read the model name from a config, but I'm not sure how."
- 3: "Use a config file or env var for model_id and pass it to AutoTokenizer and AutoModel."
- 4: "Load model_id and tokenizer_id from config with defaults, log them, and support optional revision."
- 5: "Config-driven loading (YAML/env + dataclass), explicit revision, dtype, device_map; validated inputs with clear errors and logged metadata for reproducibility."

2) Describe how you would count prompt vs completion tokens for local models.
- 1: "The model tells you how many tokens."
- 2: "I'd estimate based on text length."
- 3: "Tokenize the prompt and count input IDs; generated tokens are output length minus input length."
- 4: "Use tokenizer.encode or batch_encode_plus for prompt count; generated length from output IDs, log per request."
- 5: "Track per-request counts (prompt, completion, total) with tokenizer outputs, handle batch sizes, and persist to JSONL with timestamps."

3) What logs would you persist for reproducibility and why?
- 1: "I'd save the output text."
- 2: "Maybe keep the prompt and model name."
- 3: "Log config settings, seed, and outputs."
- 4: "Log seed, model_id, revision, dtype, device_map, generation params, and timing."
- 5: "Full run metadata: config + seed + dataset fingerprint, token counts, timing, git hash, and output artifact paths."

4) When should you prefer RAG over fine-tuning?
- 1: "Always fine-tune for better results."
- 2: "RAG is for when you have documents."
- 3: "RAG is better when facts change often; fine-tuning for behavior/style."
- 4: "Use RAG for fresh or large knowledge bases; fine-tune for consistent behavior and constrained domains."
- 5: "RAG for up-to-date, auditable, and large corpora; fine-tuning when task-specific behavior or format is needed, with cost/latency tradeoffs and eval evidence."

5) How do you detect hallucinations or factual drift in generated answers?
- 1: "You can't really tell."
- 2: "Manual review."
- 3: "Compare outputs to a reference or golden set."
- 4: "Use retrieval grounding, check citations, and evaluate against a validation set."
- 5: "Combine grounding checks (retrieval overlap), golden prompts, targeted factual tests, and monitoring for drift across time slices."

6) What does "deterministic enough" mean when using GPU generation?
- 1: "GPU is deterministic."
- 2: "Set a seed and it's deterministic."
- 3: "Some ops are non-deterministic, but you can reduce variance with seeds."
- 4: "Use fixed seeds and settings; accept minor nondeterminism due to GPU kernels."
- 5: "Define acceptable variance; fix seeds, disable sampling if needed, document nondeterministic GPU ops, and use golden tests with tolerances."

7) Given a generation pipeline producing inconsistent outputs, identify likely causes.
- 1: "The model is bad."
- 2: "Maybe the prompt is different."
- 3: "Sampling params, seed, and temperature may be different."
- 4: "Non-deterministic GPU ops, varying context length, or inconsistent preprocessing."
- 5: "Check seed management, sampling params, tokenizer version, device_map or dtype changes, prompt truncation, and any dependency drift."

8) Replace a framework-specific agent tool with a minimal custom loop.
- 1: "You can't without that tool."
- 2: "I'd try to copy the framework code."
- 3: "Write a loop: prompt to model to parse to call tool to append result."
- 4: "Implement a small state machine with tool registry, message history, and stop criteria."
- 5: "Minimal agent loop with explicit tool schema, structured outputs, error handling, and logging of each step for traceability."

## Hands-On Notebook Plan (Interview Exercises)
Notebook goal: implement reproducible GenAI pipelines with increasing scope by level.

Proposed notebook locations and naming:
- `notebooks/interview/01_GenAI_Implementation_Junior.ipynb`
- `notebooks/interview/02_GenAI_Implementation_Mid.ipynb`
- `notebooks/interview/03_GenAI_Implementation_Senior.ipynb`

Run order guidance (required in each notebook):
1. Load config (model_id, tokenizer_id, device, dtype, generation defaults).
2. Download nongated Hugging Face models (generation + embeddings).
3. Load tokenizer and model with explicit device strategy.
4. Run a small generation task with fixed seed.
5. Count tokens and log timing.
6. Evaluate against a tiny golden prompt set (and retrieval for mid/senior).

Candidate tasks (by level):
- Junior: Implement config parsing, a basic `generate()` wrapper, and token counting.
- Mid: Add embeddings + retrieval and summarize evaluation results.
- Senior: Add telemetry, robustness checks, and traceability notes.

Expected outcomes:
- Reproducible generation with clear parameters.
- Logs that support traceability and auditing.

## Evaluation Criteria (Anti-Recipe Checks)
- Can the candidate explain why each parameter matters?
- Do they avoid hard-coded model IDs and magic numbers?
- Do they produce a minimal but auditable pipeline?
- Can they explain tradeoffs in RAG vs fine-tuning?

## Traceability Notes
- Use timestamped outputs for any generated artifacts:
  - `outputs/logs/llm_tokens_<YYYYMMDD_HHMMSSZ>.jsonl`
  - `outputs/logs/llm_timing_<YYYYMMDD_HHMMSSZ>.jsonl`
  - `outputs/results/genai_eval_<YYYYMMDD_HHMMSSZ>.json`
- Record seed, model_id, revision, dtype, device_map, and quantization mode.
- Store golden prompts in a small fixture file with redacted samples:
  - `Interview/Generative/golden_prompts_fixture.json`
