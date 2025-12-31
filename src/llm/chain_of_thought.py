"""
Used in: 05_GenerativeAI_ChainOfThought_Reasoning.ipynb
Purpose:
    Provide utilities for Chain-of-Thought (CoT) prompting,
    including prompt formatting, reasoning extraction, and self-consistency decoding.
    
Educational Context:
    Chain-of-Thought (CoT) prompting improves LLM reasoning.
    
    Key Concepts:
    1. CoT Prompting: Ask model to show its reasoning steps
       - Instead of: "What is 2+2?" → "4"
       - Use: "What is 2+2? Let's think step by step: 2+2 = 4"
       - Model shows intermediate steps
    
    2. Few-Shot CoT: Provide examples with reasoning
       - Show model how to reason
       - Model learns the pattern
       - Improves complex reasoning tasks
    
    3. Self-Consistency: Generate multiple reasoning paths
       - Run CoT multiple times
       - Take majority vote on final answer
       - More reliable than single generation
    
    Why CoT works:
    - Breaks complex problems into steps
    - Reduces errors (can catch mistakes in reasoning)
    - Improves performance on math, logic, planning
    - Makes model reasoning transparent
"""

# Import type hints
from typing import List, Dict, Any, Optional

# Import re: Regular expressions for pattern matching
# Used to extract reasoning steps from model output
import re


def apply_cot_prompting(
    question: str,
    few_shot_examples: Optional[List[Dict[str, str]]] = None,
    cot_trigger: str = "Let's think step by step."
) -> str:
    """
    Format a prompt with Chain-of-Thought instructions.

    Args:
        question: The question or problem to solve.
        few_shot_examples: Optional list of example Q&A pairs with CoT reasoning.
        cot_trigger: Phrase to trigger CoT reasoning (e.g., "Let's think step by step.").

    Returns:
        Formatted prompt string with CoT instructions.
    """
    prompt_parts = []

    # Add few-shot examples if provided
    if few_shot_examples:
        for example in few_shot_examples:
            example_q = example.get("question", "")
            example_a = example.get("answer", "")
            example_cot = example.get("reasoning", "")
            
            prompt_parts.append(f"Q: {example_q}")
            if example_cot:
                prompt_parts.append(f"A: {example_cot}")
            prompt_parts.append(f"Therefore, the answer is: {example_a}\n")

    # Add the actual question with CoT trigger
    prompt_parts.append(f"Q: {question}")
    prompt_parts.append(f"A: {cot_trigger}")

    return "\n".join(prompt_parts)


def extract_reasoning_steps(
    text: str,
    step_pattern: Optional[str] = None
) -> List[str]:
    """
    Extract reasoning steps from model output.

    Args:
        text: Generated text containing reasoning.
        step_pattern: Optional regex pattern to match steps (default: numbered or bulleted).

    Returns:
        List of reasoning step strings.
    """
    if step_pattern is None:
        # Default pattern: matches numbered steps (1., 2., etc.) or bullet points
        step_pattern = r"(?:^|\n)(?:\d+\.|\*|\-)\s*(.+?)(?=\n(?:\d+\.|\*|\-)|\n\n|$)"

    # Find all matches
    matches = re.findall(step_pattern, text, re.MULTILINE | re.DOTALL)

    # Clean up matches
    steps = [match.strip() for match in matches if match.strip()]

    # If no structured steps found, try to split by common separators
    if not steps:
        # Try splitting by newlines and filtering
        lines = [line.strip() for line in text.split("\n") if line.strip()]
        # Filter lines that look like reasoning (not just answers)
        steps = [line for line in lines if len(line) > 10 and not line.startswith("Answer:")]

    return steps


def self_consistency_decode(
    model: Any,
    tokenizer: Any,
    prompt: str,
    num_samples: int = 5,
    temperature: float = 0.7,
    max_new_tokens: int = 200
) -> Dict[str, Any]:
    """
    Generate multiple reasoning paths and select the most consistent answer.

    Args:
        model: Loaded language model.
        tokenizer: Loaded tokenizer.
        prompt: Input prompt with CoT instructions.
        num_samples: Number of different reasoning paths to generate.
        temperature: Sampling temperature for diversity.
        max_new_tokens: Maximum tokens per generation.

    Returns:
        Dictionary containing all reasoning paths, final answers, and consensus.
    """
    from collections import Counter

    # Generate multiple samples
    all_outputs = []
    all_answers = []

    for _ in range(num_samples):
        # Generate one reasoning path
        inputs = tokenizer(prompt, return_tensors="pt")
        device = next(model.parameters()).device
        inputs = {k: v.to(device) for k, v in inputs.items()}

        with tokenizer.as_target_tokenizer():
            outputs = model.generate(
                **inputs,
                max_new_tokens=max_new_tokens,
                temperature=temperature,
                do_sample=True,
                pad_token_id=tokenizer.pad_token_id
            )

        # Decode output
        generated = tokenizer.decode(outputs[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True)
        all_outputs.append(generated)

        # Try to extract final answer
        answer = extract_final_answer(generated)
        if answer:
            all_answers.append(answer)

    # Find consensus answer (most common)
    if all_answers:
        answer_counts = Counter(all_answers)
        consensus_answer = answer_counts.most_common(1)[0][0]
        consensus_count = answer_counts[consensus_answer]
    else:
        consensus_answer = None
        consensus_count = 0

    return {
        "all_reasoning_paths": all_outputs,
        "all_answers": all_answers,
        "consensus_answer": consensus_answer,
        "consensus_count": consensus_count,
        "total_samples": num_samples,
        "agreement_rate": consensus_count / num_samples if num_samples > 0 else 0.0
    }


def extract_final_answer(text: str) -> Optional[str]:
    """
    Extract the final answer from reasoning text.

    Args:
        text: Text containing reasoning and answer.

    Returns:
        Extracted answer string, or None if not found.
    """
    # Common patterns for final answers
    patterns = [
        r"(?:Therefore|So|Thus|Hence|Answer|Final answer)[:\s]+(.+?)(?:\.|$)",
        r"(?:The answer is|Answer is)[:\s]+(.+?)(?:\.|$)",
        r"^(.+?)$"  # Fallback: return last line if no pattern matches
    ]

    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE | re.MULTILINE)
        if match:
            answer = match.group(1).strip()
            # Filter out very long answers (likely not the final answer)
            if len(answer) < 200:
                return answer

    return None


def evaluate_reasoning_quality(
    reasoning_steps: List[str],
    expected_answer: Optional[str] = None,
    actual_answer: Optional[str] = None
) -> Dict[str, Any]:
    """
    Evaluate the quality of reasoning steps.

    Args:
        reasoning_steps: List of reasoning step strings.
        expected_answer: Expected final answer (for correctness check).
        actual_answer: Actual final answer extracted.

    Returns:
        Dictionary containing quality metrics.
    """
    metrics = {
        "num_steps": len(reasoning_steps),
        "avg_step_length": 0.0,
        "total_reasoning_length": 0,
        "is_correct": None,
        "has_structure": len(reasoning_steps) > 0
    }

    if reasoning_steps:
        # Calculate average step length
        step_lengths = [len(step) for step in reasoning_steps]
        metrics["avg_step_length"] = sum(step_lengths) / len(step_lengths)
        metrics["total_reasoning_length"] = sum(step_lengths)

    # Check correctness if both answers provided
    if expected_answer and actual_answer:
        # Simple string matching (could be enhanced with semantic similarity)
        metrics["is_correct"] = expected_answer.lower().strip() == actual_answer.lower().strip()

    return metrics

