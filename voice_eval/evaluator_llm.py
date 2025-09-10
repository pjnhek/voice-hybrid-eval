# LLM-based evaluator using Ollama with Llama
from typing import Dict, Any
import requests
import json
import os

def check_bot_expect_llm(bot_text: str, expect: Dict[str, Any]) -> bool:
    """
    LLM-based evaluation that follows the same rules as evaluator_rules.py
    Uses Ollama with Llama to evaluate bot responses.
    """
    if not expect:
        return True
    
    # Create a prompt that follows the exact same logic as the rule-based evaluator
    prompt = _create_evaluation_prompt(bot_text, expect)
    
    try:
        result = _call_ollama_llm(prompt)
        llm_result = result.get("pass", False)
        debug_llm = os.getenv("DEBUG_LLM_EVALUATION", "false").lower() == "true"
        if debug_llm:
            print(f"DEBUG - LLM evaluation: {llm_result} (reason: {result.get('reason', 'N/A')})")
        return llm_result
    except Exception as e:
        print(f"Warning: LLM evaluation failed, falling back to rule-based: {e}")
        # Fallback to rule-based evaluation
        fallback_result = _fallback_rule_evaluation(bot_text, expect)
        debug_llm = os.getenv("DEBUG_LLM_EVALUATION", "false").lower() == "true"
        if debug_llm:
            print(f"DEBUG - Fallback evaluation: {fallback_result}")
        return fallback_result

def _create_evaluation_prompt(bot_text: str, expect: Dict[str, Any]) -> str:
    """Create a prompt that follows the exact same rules as evaluator_rules.py"""
    
    prompt = f"""Evaluate this bot response for a voice interaction test.

BOT RESPONSE: "{bot_text}"
EXPECTATION: {json.dumps(expect, indent=2)}

RULES (follow exactly like rule-based evaluator):
- 'contains': Check if phrase appears anywhere in bot response (case-insensitive substring match)
- 'contains_any': Check if ANY phrase from list appears anywhere in bot response (case-insensitive substring match)
- No valid expectation keys = Return True (pass by default)
- Use case-insensitive matching only

EXAMPLES:
- Expecting ["order number"] and bot says "Could you provide your order number?" → PASS
- Expecting ["initiated the return"] and bot says "I have initiated the return for that order" → PASS
- Expecting ["refund processed"] and bot says "Your refund has been processed" → PASS

RESPOND WITH JSON ONLY (no other text):
{{"pass": true/false, "reason": "brief explanation"}}"""

    return prompt

def _call_ollama_llm(prompt: str) -> Dict[str, Any]:
    """Call Ollama API with Llama model for evaluation""" 
    # Get configuration from environment variables
    ollama_base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    ollama_model = os.getenv("OLLAMA_MODEL", "llama3.2")
    debug_llm = os.getenv("DEBUG_LLM_EVALUATION", "false").lower() == "true"
    
    try:
        # Check if Ollama is running first
        test_response = requests.get(f"{ollama_base_url}/api/tags", timeout=5)
        if test_response.status_code != 200:
            raise Exception("Ollama not running")
            
    except requests.exceptions.RequestException:
        raise Exception("Ollama not running")
    
    try:
        # Ollama API endpoint
        url = f"{ollama_base_url}/api/generate"
        
        # Ollama API payload
        payload = {
            "model": ollama_model,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0.0,  # Deterministic responses
                "top_p": 0.0,
                "format": "json"  # Request JSON format
            }
        }
        
        # Make the API call
        response = requests.post(url, json=payload, timeout=30)
        response.raise_for_status()
        
        # Parse the response
        result = response.json()
        response_text = result.get("response", "").strip()
        
        # Try to extract JSON from the response
        try:
            # Look for JSON in the response - be more flexible
            json_start = response_text.find('{')
            json_end = response_text.rfind('}') + 1
            if json_start != -1 and json_end > json_start:
                json_str = response_text[json_start:json_end]
                parsed_json = json.loads(json_str)
                
                # Validate the response has the required fields
                if "pass" in parsed_json:
                    return parsed_json
                else:
                    raise ValueError("Missing 'pass' field in JSON response")
            else:
                raise ValueError("No JSON found in response")
                
        except (json.JSONDecodeError, ValueError) as e:
            # Try to extract just the boolean value from the response text
            response_lower = response_text.lower()
            if '"pass": true' in response_lower or '"pass":true' in response_lower:
                return {"pass": True, "reason": "Extracted from response text"}
            elif '"pass": false' in response_lower or '"pass":false' in response_lower:
                return {"pass": False, "reason": "Extracted from response text"}
            else:
                # If all else fails, return a conservative evaluation
                print(f"Warning: Failed to parse JSON from Ollama response: {response_text}")
                return {
                    "pass": False,
                    "reason": "Failed to parse LLM response"
                }
                
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error calling Ollama API: {e}")
    except Exception as e:
        raise Exception(f"Unexpected error in LLM evaluation: {e}")

def _fallback_rule_evaluation(bot_text: str, expect: Dict[str, Any]) -> bool:
    """Fallback to rule-based evaluation when LLM fails"""
    if not expect:
        return True
    
    bot_lower = bot_text.lower()
    
    # Support keys (same logic as evaluator_rules.py)
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
