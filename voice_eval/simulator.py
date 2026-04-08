# Voice interaction simulation engine
from pathlib import Path
from typing import Dict, List, Any

from .audio.tts import synthesize
from .audio.asr import transcribe
from .tool_client import ToolClient
from .evaluator_claude import check_bot_expect_claude
from .evaluator_rules import check_bot_expect_enhanced
from .scenario import Scenario


def run_scenario(s: Scenario, audio_dir: Path, model_size: str = "tiny", judge: str = "rules") -> Dict[str, Any]:
    """Run a single scenario through the hybrid voice loop."""
    tool_client = ToolClient()
    transcript = []
    slots = {}

    for i, step in enumerate(s.steps, start=1):
        user_text = step.user or ""
        user_wav = f"{audio_dir}/{s.id}/user_{i}.wav"
        synthesize(user_text, user_wav)

        user_transcript = transcribe(user_wav, model_size=model_size)

        slots_result = tool_client.call_tool("extract_slots", {
            "user_input": user_transcript,
            "current_slots": slots,
        })

        if slots_result.success:
            slots = slots_result.data
        else:
            print(f"DEBUG - Slot extraction failed: {slots_result.error}")

        policy_result = tool_client.call_tool("policy_decision", {
            "goal": s.goal,
            "user_input": user_transcript,
            "available_slots": slots,
        })

        if not policy_result.success:
            print(f"DEBUG - Policy decision failed: {policy_result.error}")
            policy_result.data = {"action": "ASK_CLARIFY"}

        response_result = tool_client.call_tool("generate_response", {
            "action": policy_result.data["action"],
            "slots": slots,
        })

        if not response_result.success:
            print(f"DEBUG - Response generation failed: {response_result.error}")
            response_result.data = {
                "action": "ASK_CLARIFY",
                "utterance": "I'm sorry, I encountered an error. Could you please try again?",
            }

        bot_text = response_result.data["utterance"]

        bot_wav = f"{audio_dir}/{s.id}/bot_{i}.wav"
        synthesize(bot_text, bot_wav)

        if judge == "claude":
            ok = check_bot_expect_claude(bot_text, step.bot_expect)
        else:
            ok = check_bot_expect_enhanced(bot_text, step.bot_expect)

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

    steps_expected = sum(1 for step in s.steps if step.bot_expect)
    steps_passed = sum(1 for entry in transcript if entry["pass"] and entry["expectation"])
    scenario_pass = (steps_passed == steps_expected)

    return {
        "scenario_id": s.id,
        "goal": s.goal,
        "scenario_pass": scenario_pass,
        "steps_expected": steps_expected,
        "steps_passed": steps_passed,
        "transcript": transcript,
    }


def run_directory(dir_path: Path, audio_dir: Path, model_size: str = "tiny", judge: str = "rules") -> List[Dict[str, Any]]:
    """Load scenarios and run all of them."""
    from .scenario import load_scenarios

    scenarios = load_scenarios(dir_path)
    results = []

    for scenario in scenarios:
        result = run_scenario(scenario, audio_dir, model_size, judge)
        results.append(result)

    return results
