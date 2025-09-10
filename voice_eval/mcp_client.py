# MCP Client for Voice Evaluation System
from typing import Dict, Any
from .mcp_tools import extract_slots_tool, policy_decision_tool, generate_response_tool, ToolResult

class MCPClient:
    def __init__(self):
        self.tools = {
            "extract_slots": extract_slots_tool,
            "policy_decision": policy_decision_tool,
            "generate_response": generate_response_tool
        }
    
    def call_tool(self, tool_name: str, arguments: Dict[str, Any]) -> ToolResult:
        """Call a specific MCP tool with arguments"""
        if tool_name not in self.tools:
            return ToolResult(success=False, data=None, error=f"Tool {tool_name} not found")
        
        try:
            return self.tools[tool_name](**arguments)
        except Exception as e:
            return ToolResult(success=False, data=None, error=str(e))
