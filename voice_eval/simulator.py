# Voice interaction simulation engine
import logging
from pathlib import Path
from typing import Dict, List, Any

from anthropic import Anthropic

from .audio.tts import synthesize
from .audio.asr import transcribe
from .bot_brain import HistoryEntry, generate_bot_response
from .tool_client import ToolClient
from .evaluator_claude import check_bot_expect_claude
from .evaluator_rules import check_bot_expect_enhanced
from .scenario import Scenario, load_scenarios


logger = logging.getLogger(__name__)

_AUDIO_EXTENSIONS = (".wav", ".m4a", ".mp3", ".ogg", ".flac")


def _find_real_audio(real_audio_dir: Path, scenario_id: str, turn: int) -> str | None:
    """Find a pre-recorded audio file for a given scenario turn."""
    for ext in _AUDIO_EXTENSIONS:
        candidate = real_audio_dir / scenario_id / f"user_{turn}{ext}"
        if candidate.exists():
            return str(candidate)
    return None


def run_scenario(
    s: Scenario,
    audio_dir: Path,
    model_size: str = "tiny",
    judge: str = "rules",
    real_audio_dir: str | Path | None = None,
) -> Dict[str, Any]:
    """Run a single scenario through the hybrid voice loop."""
    client = Anthropic()
    tool_client = ToolClient()
    transcript = []
    slots = {}
    conversation_history: List[HistoryEntry] = []
    real_audio_root = Path(real_audio_dir) if real_audio_dir is not None else None

    for i, step in enumerate(s.steps, start=1):
        user_text = step.user or ""
        real_audio_file = None
        if real_audio_root is not None:
            real_audio_file = _find_real_audio(real_audio_root, s.id, i)

        if real_audio_file:
            user_wav = real_audio_file
        else:
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
            logger.warning("Slot extraction failed: %s", slots_result.error)

        error = None
        try:
            bot_response = generate_bot_response(
                client=client,
                goal=s.goal,
                user_input=user_transcript,
                slots=slots,
                conversation_history=conversation_history,
            )
        except Exception as exc:
            error = str(exc)
            logger.warning("Bot response generation failed: %s", exc)
            bot_response = {
                "action": "ASK_CLARIFY",
                "utterance": "I'm sorry, I encountered an error. Could you please try again?",
            }

        bot_text = bot_response["utterance"]
        action = bot_response["action"]
        conversation_history.append({"user": user_transcript, "bot": bot_text})

        bot_wav = f"{audio_dir}/{s.id}/bot_{i}.wav"
        synthesize(bot_text, bot_wav)

        if error is not None:
            ok = False
        elif judge == "claude":
            ok = check_bot_expect_claude(bot_text, step.bot_expect)
        else:
            ok = check_bot_expect_enhanced(bot_text, step.bot_expect)

        transcript.append({
            "turn": i,
            "user_text": user_text,
            "user_asr": user_transcript,
            "bot_text": bot_text,
            "action": action,
            "slots": dict(slots),
            "pass": ok,
            "error": error,
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


def run_directory(
    dir_path: Path,
    audio_dir: Path,
    model_size: str = "tiny",
    judge: str = "rules",
    real_audio_dir: str | Path | None = None,
) -> List[Dict[str, Any]]:
    """Load scenarios and run all of them."""
    scenarios = load_scenarios(dir_path)
    results = []

    for scenario in scenarios:
        result = run_scenario(
            scenario,
            audio_dir,
            model_size,
            judge,
            real_audio_dir=real_audio_dir,
        )
        results.append(result)

    return results
