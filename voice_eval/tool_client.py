# Tool client for voice evaluation
from typing import Dict, Any
from .bot_tools import (
    ToolResult,
    extract_slots_tool,
    generate_response_tool,
    policy_decision_tool,
)


class ToolClient:
    def __init__(self):
        self.tools = {
            "extract_slots": extract_slots_tool,
            "policy_decision": policy_decision_tool,
            "generate_response": generate_response_tool,
        }

    def call_tool(self, tool_name: str, arguments: Dict[str, Any]) -> ToolResult:
        """Call a specific tool with arguments."""
        if tool_name not in self.tools:
            return ToolResult(success=False, data=None, error=f"Tool {tool_name} not found")

        try:
            return self.tools[tool_name](**arguments)
        except Exception as e:
            return ToolResult(success=False, data=None, error=str(e))
