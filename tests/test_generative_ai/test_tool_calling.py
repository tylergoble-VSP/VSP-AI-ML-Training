"""
Unit tests for src.llm.tool_calling module.
"""

import pytest
import json


class TestDefineToolSchema:
    """Test define_tool_schema function."""

    def test_define_tool_schema(self):
        """Test defining a tool schema."""
        from src.llm.tool_calling import define_tool_schema

        parameters = {
            "properties": {
                "query": {"type": "string", "description": "Search query"}
            },
            "required": ["query"]
        }

        schema = define_tool_schema(
            "search",
            "Search the web",
            parameters
        )

        assert schema["name"] == "search"
        assert schema["description"] == "Search the web"
        assert "parameters" in schema


class TestExecuteToolCall:
    """Test execute_tool_call function."""

    def test_execute_tool_call_success(self):
        """Test successful tool execution."""
        from src.llm.tool_calling import execute_tool_call

        def test_func(x: int, y: int) -> int:
            return x + y

        tool_functions = {"add": test_func}
        result = execute_tool_call("add", {"x": 2, "y": 3}, tool_functions)

        assert result["success"] is True
        assert result["result"] == 5

    def test_execute_tool_call_not_found(self):
        """Test tool not found error."""
        from src.llm.tool_calling import execute_tool_call

        tool_functions = {}
        result = execute_tool_call("nonexistent", {}, tool_functions)

        assert result["success"] is False
        assert "error" in result


class TestParseToolCall:
    """Test parse_tool_call function."""

    def test_parse_tool_call_json(self):
        """Test parsing JSON tool call."""
        from src.llm.tool_calling import parse_tool_call

        text = '{"tool": "search", "arguments": {"query": "test"}}'
        result = parse_tool_call(text)

        assert result is not None
        assert result["name"] == "search"

    def test_parse_tool_call_action_format(self):
        """Test parsing Action: format."""
        from src.llm.tool_calling import parse_tool_call

        text = "Action: search[{\"query\": \"test\"}]"
        result = parse_tool_call(text)

        assert result is not None
        assert result["name"] == "search"

