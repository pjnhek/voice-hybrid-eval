# Rule-based evaluator (more reliable than LLM)
from typing import Dict, Any

def check_bot_expect_enhanced(bot_text: str, expect: Dict[str, Any]) -> bool:
    """Enhanced rule-based evaluation with better matching."""
    if not expect:
        return True
    
    bot_lower = bot_text.lower()
    
    # Support keys
    if "contains" in expect:
        # Single substring (case-insensitive)
        return expect["contains"].lower() in bot_lower
    
    elif "contains_any" in expect:
        # List of substrings; pass if any present (case-insensitive)
        if not isinstance(expect["contains_any"], list):
            return False
        
        for substring in expect["contains_any"]:
            if substring.lower() in bot_lower:
                return True
        return False
    
    # If unknown key present, return False
    return False
