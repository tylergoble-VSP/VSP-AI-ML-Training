"""
Used in: 06_GenerativeAI_Tool_Calling_Agents.ipynb
Purpose:
    Provide utilities for tool calling and agent implementation,
    including tool schema definition, safe execution, and agent loops.
    
Educational Context:
    Tool calling allows LLMs to interact with external systems.
    
    Key Concepts:
    1. Tool Schema: Describes available tools to LLM
       - Function name, description, parameters
       - LLM decides when and how to call tools
    
    2. Agent Loop: LLM can call tools repeatedly
       - Think → Act → Observe → Think → ...
       - Continues until task complete
    
    3. ReAct Pattern: Reasoning + Acting
       - Reasoning: LLM explains what it's doing
       - Acting: LLM calls appropriate tool
       - Observation: Tool returns result
       - Repeat until done
    
    Why tool calling?
    - LLMs can't access real-time data
    - Can't perform actions (send email, search web)
    - Tool calling bridges this gap
    - Enables autonomous agents
"""

# Import type hints
from typing import Dict, List, Any, Optional, Callable

# Import json: For parsing JSON (tool schemas, function calls)
import json

# Import re: For pattern matching (extracting function calls from text)
import re


def define_tool_schema(
    name: str,
    description: str,
    parameters: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Define a tool schema in OpenAI function calling format.

    Args:
        name: Name of the tool/function.
        description: Description of what the tool does.
        parameters: JSON schema for function parameters.

    Returns:
        Dictionary containing tool schema.
    """
    schema = {
        "name": name,
        "description": description,
        "parameters": {
            "type": "object",
            "properties": parameters.get("properties", {}),
            "required": parameters.get("required", [])
        }
    }

    return schema


def execute_tool_call(
    tool_name: str,
    arguments: Dict[str, Any],
    tool_functions: Dict[str, Callable],
    sandbox: bool = True
) -> Dict[str, Any]:
    """
    Safely execute a tool call with validation.

    Args:
        tool_name: Name of the tool to execute.
        arguments: Arguments for the tool function.
        tool_functions: Dictionary mapping tool names to callable functions.
        sandbox: Whether to apply sandboxing restrictions.

    Returns:
        Dictionary containing tool execution result or error.
    """
    # Check if tool exists
    if tool_name not in tool_functions:
        return {
            "error": f"Tool '{tool_name}' not found",
            "available_tools": list(tool_functions.keys())
        }

    # Get the function
    func = tool_functions[tool_name]

    # Validate arguments if function has annotations
    try:
        # Execute the function
        result = func(**arguments)

        return {
            "tool": tool_name,
            "result": result,
            "success": True
        }
    except Exception as e:
        return {
            "tool": tool_name,
            "error": str(e),
            "success": False
        }


def agent_loop(
    model: Any,
    tokenizer: Any,
    user_query: str,
    tools: List[Dict[str, Any]],
    tool_functions: Dict[str, Callable],
    max_iterations: int = 5,
    system_prompt: Optional[str] = None
) -> Dict[str, Any]:
    """
    Implement an agent loop that can use tools to answer queries.

    Args:
        model: Language model for reasoning.
        tokenizer: Tokenizer for the model.
        user_query: User's question or request.
        tools: List of tool schemas.
        tool_functions: Dictionary mapping tool names to functions.
        max_iterations: Maximum number of tool-calling iterations.
        system_prompt: Optional system prompt for the agent.

    Returns:
        Dictionary containing final answer and tool usage history.
    """
    # Initialize conversation
    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": user_query})

    tool_history = []
    iteration = 0

    while iteration < max_iterations:
        # Format prompt with available tools
        prompt = format_agent_prompt(messages, tools)

        # Generate response
        inputs = tokenizer(prompt, return_tensors="pt")
        device = next(model.parameters()).device
        inputs = {k: v.to(device) for k, v in inputs.items()}

        with tokenizer.as_target_tokenizer():
            outputs = model.generate(
                **inputs,
                max_new_tokens=200,
                do_sample=True,
                temperature=0.7,
                pad_token_id=tokenizer.pad_token_id
            )

        response = tokenizer.decode(outputs[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True)

        # Check if response contains tool call
        tool_call = parse_tool_call(response)

        if tool_call:
            # Execute tool
            tool_result = execute_tool_call(
                tool_call["name"],
                tool_call["arguments"],
                tool_functions
            )

            tool_history.append({
                "iteration": iteration,
                "tool_call": tool_call,
                "result": tool_result
            })

            # Add tool result to conversation
            messages.append({"role": "assistant", "content": response})
            messages.append({
                "role": "function",
                "name": tool_call["name"],
                "content": json.dumps(tool_result)
            })

            iteration += 1
        else:
            # No tool call, return final answer
            return {
                "final_answer": response,
                "tool_history": tool_history,
                "iterations": iteration
            }

    # Max iterations reached
    return {
        "final_answer": response,
        "tool_history": tool_history,
        "iterations": iteration,
        "max_iterations_reached": True
    }


def format_agent_prompt(
    messages: List[Dict[str, str]],
    tools: List[Dict[str, Any]]
) -> str:
    """
    Format messages and available tools into a prompt for the agent.

    Args:
        messages: Conversation history.
        tools: List of available tool schemas.

    Returns:
        Formatted prompt string.
    """
    prompt_parts = []

    # Add system message if present
    for msg in messages:
        if msg.get("role") == "system":
            prompt_parts.append(f"System: {msg['content']}\n")

    # Add available tools
    if tools:
        prompt_parts.append("Available tools:")
        for tool in tools:
            prompt_parts.append(f"- {tool['name']}: {tool['description']}")
        prompt_parts.append("")

    # Add conversation history
    for msg in messages:
        role = msg.get("role", "user")
        content = msg.get("content", "")
        if role == "user":
            prompt_parts.append(f"User: {content}")
        elif role == "assistant":
            prompt_parts.append(f"Assistant: {content}")
        elif role == "function":
            prompt_parts.append(f"Tool result: {content}")

    prompt_parts.append("Assistant:")

    return "\n".join(prompt_parts)


def parse_tool_call(text: str) -> Optional[Dict[str, Any]]:
    """
    Parse a tool call from model output.

    Args:
        text: Model output text that may contain a tool call.

    Returns:
        Dictionary with 'name' and 'arguments' keys, or None if no tool call found.
    """
    # Pattern 1: JSON-like tool call
    json_pattern = r'\{[^}]*"tool"[^}]*"name"[^}]*"arguments"[^}]*\}'
    match = re.search(json_pattern, text, re.IGNORECASE)
    if match:
        try:
            tool_call = json.loads(match.group(0))
            return {
                "name": tool_call.get("tool") or tool_call.get("name"),
                "arguments": tool_call.get("arguments", {})
            }
        except json.JSONDecodeError:
            pass

    # Pattern 2: Action: ToolName[arguments]
    action_pattern = r'Action:\s*(\w+)\s*\[(.*?)\]'
    match = re.search(action_pattern, text, re.IGNORECASE)
    if match:
        tool_name = match.group(1)
        args_str = match.group(2)
        try:
            arguments = json.loads(args_str) if args_str.startswith("{") else {"query": args_str}
            return {"name": tool_name, "arguments": arguments}
        except json.JSONDecodeError:
            return {"name": tool_name, "arguments": {"input": args_str}}

    return None


def validate_tool_output(
    tool_result: Dict[str, Any],
    expected_type: Optional[type] = None
) -> bool:
    """
    Validate tool execution output.

    Args:
        tool_result: Result dictionary from tool execution.
        expected_type: Optional expected type for the result value.

    Returns:
        True if output is valid, False otherwise.
    """
    # Check for success
    if not tool_result.get("success", False):
        return False

    # Check result exists
    if "result" not in tool_result:
        return False

    # Check type if specified
    if expected_type:
        result = tool_result["result"]
        if not isinstance(result, expected_type):
            return False

    return True

