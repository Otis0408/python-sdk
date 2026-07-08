"""Tests for context-parameter detection (mcpserver utilities)."""

from mcp.server.mcpserver import Context
from mcp.server.mcpserver.utilities.context_injection import find_context_parameter


def test_find_context_parameter_detects_context_param() -> None:
    def fn(x: int, ctx: Context) -> str: ...

    assert find_context_parameter(fn) == "ctx"


def test_find_context_parameter_ignores_context_return_annotation() -> None:
    # get_type_hints() surfaces the return annotation under the "return" key;
    # a Context-returning function has no Context *parameter*, so the result
    # must be None (previously it returned the string "return").
    def fn(x: int) -> Context: ...

    assert find_context_parameter(fn) is None


def test_find_context_parameter_ignores_optional_context_return_annotation() -> None:
    def fn(x: int) -> Context | None: ...

    assert find_context_parameter(fn) is None
