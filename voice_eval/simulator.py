# Voice interaction simulation engine with MCP
from pathlib import Path
from datetime import datetime
import uuid
from typing import Dict, List, Any

from .audio.tts import synthesize
from .audio.asr import transcribe
from .mcp_client import MCPClient
from .evaluator_rules import check_bot_expect_enhanced
from .evaluator_llm import check_bot_expect_llm
from .scenario import Scenario

def run_scenario(s: Scenario, audio_dir: Path, model_size: str = "tiny", judge: str = "rules") -> Dict[str, Any]:
    """Run a single scenario through the hybrid voice loop using MCP."""
    mcp_client = MCPClient()
    transcript = []
    slots = {}
    
    # For each Step
    for i, step in enumerate(s.steps, start=1):
        # Produce user audio from Step.user text
        user_text = step.user or ""
        user_wav = f"{audio_dir}/{s.id}/user_{i}.wav"
        synthesize(user_text, user_wav)
        
        # ASR on user audio
        user_transcript = transcribe(user_wav, model_size=model_size)
        
        # Extract slots using MCP tool
        slots_result = mcp_client.call_tool("extract_slots", {
            "user_input": user_transcript,
            "current_slots": slots
        })
        
        if slots_result.success:
            slots = slots_result.data
        else:
            print(f"DEBUG - Slot extraction failed: {slots_result.error}")
        
        # Get policy decision using MCP tool
        policy_result = mcp_client.call_tool("policy_decision", {
            "goal": s.goal,
            "user_input": user_transcript,
            "available_slots": slots
        })
        
        if not policy_result.success:
            print(f"DEBUG - Policy decision failed: {policy_result.error}")
            policy_result.data = {"action": "ASK_CLARIFY"}
        
        # Generate response using MCP tool
        response_result = mcp_client.call_tool("generate_response", {
            "action": policy_result.data["action"],
            "slots": slots
        })
        
        if not response_result.success:
            print(f"DEBUG - Response generation failed: {response_result.error}")
            response_result.data = {
                "action": "ASK_CLARIFY",
                "utterance": "I'm sorry, I encountered an error. Could you please try again?"
            }
        
        bot_text = response_result.data["utterance"]
        
        # bot TTS + evaluation
        bot_wav = f"{audio_dir}/{s.id}/bot_{i}.wav"
        synthesize(bot_text, bot_wav)
        
        # Evaluate based on judge type
        if judge == "llm":
            ok = check_bot_expect_llm(bot_text, step.bot_expect) if step.bot_expect else True
        else:  # rules (default)
            ok = check_bot_expect_enhanced(bot_text, step.bot_expect) if step.bot_expect else True
        
        # Append to transcript
        transcript.append({
            "turn": i,
            "user_text": user_text,
            "user_asr": user_transcript,
            "bot_text": bot_text,
            "action": response_result.data["action"],
            "slots": dict(slots),
            "pass": ok,
            "expectation": step.bot_expect or {},
            "user_wav": user_wav,
            "bot_wav": bot_wav,
        })
    
    # Compute metrics
    steps_expected = sum(1 for step in s.steps if step.bot_expect)
    steps_passed = sum(1 for entry in transcript if entry["pass"] and entry["expectation"])
    scenario_pass = (steps_passed == steps_expected)
    
    # Return result dict
    return {
        "scenario_id": s.id,
        "goal": s.goal,
        "scenario_pass": scenario_pass,
        "steps_expected": steps_expected,
        "steps_passed": steps_passed,
        "transcript": transcript
    }

def run_directory(dir_path: Path, audio_dir: Path, model_size: str = "tiny", judge: str = "rules") -> List[Dict[str, Any]]:
    """Load scenarios and run all using MCP."""
    from .scenario import load_scenarios
    
    scenarios = load_scenarios(dir_path)
    results = []
    
    for scenario in scenarios:
        result = run_scenario(scenario, audio_dir, model_size, judge)
        results.append(result)
    
    return results