# Implementation Plan: Expand Goals & Real Audio Support

This document is the source of truth for the next round of changes. Codex should implement each task and check it off. Claude Code will review the changes afterward.

---

## Task 0: Fix scenario loader and clean up old scenarios

**Status: DONE**

---

## Task 1: Add 5 new goals to `bot_tools.py`

**Status: DONE**

---

## Task 2: Remove Ollama judge

**Status: DONE**

---

## Task 3: Replace rule-based bot with Claude-powered bot

**This is a major architecture change.** The current bot pipeline uses regex slot extraction, hardcoded if/else policy decisions, and string templates for responses. Replace the policy decision and response generation steps with Claude API calls so the bot can actually understand and respond to users intelligently.

### What changes and what stays

**Keep as-is:**
- `extract_slots_tool` in `bot_tools.py` — regex slot extraction is fast and deterministic, a reasonable pre-processing step before the LLM
- `evaluator_claude.py` — the judge stays separate from the bot (different role, could use different models)
- `evaluator_rules.py` — keep the rules judge as a baseline

**Replace:**
- `policy_decision_tool` — currently a hardcoded if/else tree. Replace with a Claude call that understands the goal, conversation history, and extracted slots to decide the next action.
- `generate_response_tool` — currently a template lookup. Replace with a Claude call that generates a natural response.

**Simplify:** Merge policy decision + response generation into a single Claude call. There's no reason to make two API calls when one can decide what to do AND generate the response together.

### New file: `voice_eval/bot_brain.py`

Create a new module that replaces the policy + response pipeline with a single Claude call.

```python
"""LLM-powered bot brain using Claude for policy decisions and response generation."""
import json
from typing import Any, Dict, List

from anthropic import Anthropic


def generate_bot_response(
    goal: str,
    user_input: str,
    slots: Dict[str, Any],
    conversation_history: List[Dict[str, str]],
) -> Dict[str, Any]:
    """Use Claude to decide the next action and generate a response.
    
    Returns dict with keys: "action", "utterance"
    """
    client = Anthropic()

    system_prompt = f"""You are a customer service bot. Your current task is: {goal}

You have access to the following extracted information from the conversation:
{json.dumps(slots, indent=2) if slots else "No information extracted yet."}

Based on the conversation so far, decide what to do next and respond naturally.

Rules:
- If you need information from the customer (order number, card info, email, account number), ask for it politely.
- If you have enough information to fulfill the request, confirm the action and provide details.
- Be concise and professional. One to two sentences max.
- Do NOT make up order numbers, tracking info, or other specific data not in the extracted slots.
- When confirming an action, reference the specific information the customer provided (e.g., the order number).

You must respond with ONLY a JSON object (no other text):
{{"action": "<ACTION_NAME>", "utterance": "<your response to the customer>"}}

Valid actions: ASK_ORDER_NUMBER, ASK_CARD_INFO, ASK_EMAIL, ASK_ACCOUNT_NUMBER, ASK_CLARIFY,
CONFIRM_RETURN, CONFIRM_ADDRESS_CHANGE, CONFIRM_CANCELLATION, PROCESS_REFUND,
PROVIDE_STATUS, SEND_RESET_LINK, OPEN_INVESTIGATION, CONFIRM_UPGRADE"""

    messages = []
    for entry in conversation_history:
        messages.append({"role": "user", "content": entry["user"]})
        if "bot" in entry:
            messages.append({"role": "assistant", "content": entry["bot"]})
    
    # Add current turn
    messages.append({"role": "user", "content": user_input})

    response = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=256,
        system=system_prompt,
        messages=messages,
        output_config={
            "format": {
                "type": "json_schema",
                "name": "bot_response",
                "schema": {
                    "type": "object",
                    "properties": {
                        "action": {"type": "string"},
                        "utterance": {"type": "string"},
                    },
                    "required": ["action", "utterance"],
                    "additionalProperties": False,
                },
            }
        },
    )

    return json.loads(response.content[0].text)
```

Key design decisions:
- Uses `claude-haiku-4-5` for cost efficiency (this runs per conversation turn, not just evaluation)
- Structured output guarantees valid JSON — no parsing hacks
- System prompt includes the goal and extracted slots as context
- Conversation history is passed so Claude understands multi-turn context
- The action names stay the same as before for compatibility with evaluation

### Modify `voice_eval/simulator.py`

Replace the three tool calls (extract_slots → policy_decision → generate_response) with: extract_slots → `generate_bot_response`.

The new loop body should look like:

```python
from .bot_brain import generate_bot_response

# ... in run_scenario, inside the step loop:

# 1. Slot extraction (keep rule-based — fast, deterministic)
slots_result = tool_client.call_tool("extract_slots", {
    "user_input": user_transcript,
    "current_slots": slots,
})
if slots_result.success:
    slots = slots_result.data

# 2. Bot response (Claude-powered)
bot_response = generate_bot_response(
    goal=s.goal,
    user_input=user_transcript,
    slots=slots,
    conversation_history=conversation_history,
)

bot_text = bot_response["utterance"]
action = bot_response["action"]

# 3. Update conversation history for next turn
conversation_history.append({"user": user_transcript, "bot": bot_text})
```

Important changes to `run_scenario`:
- Add `conversation_history: List[Dict[str, str]] = []` alongside `slots = {}`
- Remove the `policy_decision` and `generate_response` tool calls
- Keep the `extract_slots` tool call
- Pass `conversation_history` to `generate_bot_response`
- After getting the response, append to `conversation_history`

### Keep `bot_tools.py` and `tool_client.py`

Don't delete them. `extract_slots_tool` is still used. The policy and response functions become dead code — leave them for now as a reference/fallback. They could be used later for a `--bot-mode rules` flag if desired.

### Modify `tool_client.py`

No changes needed — it still dispatches `extract_slots`.

### Add `--bot-mode` flag (optional, low priority)

Could add `--bot-mode rules|claude` to CLI to toggle between rule-based and LLM-powered bot. This lets you compare how the rule-based bot vs. the LLM bot handles the same scenarios. Nice for a portfolio story but not required for this task.

### Tests

**File:** `tests/test_bot_brain.py` (new)

- Mock `anthropic.Anthropic` like in `test_evaluator_claude.py`
- Test that `generate_bot_response` returns the expected dict shape
- Test that conversation history is passed to the API
- Test with empty slots vs populated slots
- ~4 tests

### Cost consideration

With 80 scenarios averaging 2 turns each = ~160 Claude Haiku calls for the bot + ~160 for the judge = ~320 API calls total. At Haiku pricing that's well under $0.10 for a full run.

**Checklist:**
- [ ] `voice_eval/bot_brain.py` created with `generate_bot_response` function
- [ ] `simulator.py` updated to use `generate_bot_response` instead of policy + response tools
- [ ] Conversation history tracked across turns in `run_scenario`
- [ ] `extract_slots_tool` still used for slot extraction
- [ ] Tests in `tests/test_bot_brain.py`
- [ ] All existing tests still pass (`poetry run pytest`)

---

## Task 4: Replace pyttsx3 with gTTS

**Files:** `voice_eval/audio/tts.py`, `pyproject.toml`

pyttsx3 produces robotic, sometimes near-silent audio that faster-whisper can't transcribe reliably (this is why scenarios show blank ASR transcripts). Replace it with gTTS (Google Text-to-Speech), which produces natural-sounding audio for free.

### Changes to `pyproject.toml`

- Remove `pyttsx3` from dependencies
- Add `gtts` to dependencies

### Changes to `voice_eval/audio/tts.py`

Replace the entire implementation:

```python
from pathlib import Path
from gtts import gTTS


def synthesize(text: str, out_wav: str) -> None:
    """Synthesize text to speech and save as audio file."""
    Path(out_wav).parent.mkdir(parents=True, exist_ok=True)
    tts = gTTS(text=text, lang="en")
    # gTTS outputs MP3 natively. faster-whisper reads both MP3 and WAV
    # via ffmpeg decoding, so the .wav extension is fine.
    tts.save(out_wav)
```

Note: gTTS requires an internet connection. This is acceptable — the project already requires internet for the Claude API. If offline support matters later, we can add a fallback.

### Update tests

If any existing tests mock or reference `pyttsx3`, update them to reference `gtts` instead.

### Run `poetry lock` and `poetry install` after changing deps.

**Checklist:**
- [ ] `pyttsx3` removed from `pyproject.toml`, `gtts` added
- [ ] `voice_eval/audio/tts.py` rewritten to use gTTS
- [ ] `poetry lock && poetry install` succeeds
- [ ] `poetry run voice-eval scenarios scenarios/` produces non-empty ASR transcripts
- [ ] All existing tests still pass

---

## Task 5: Add real audio input mode to `simulator.py`

**Files:** `voice_eval/simulator.py`, `voice_eval/cli.py`

Add a `--real-audio` flag that tells the simulator to use pre-recorded WAV files instead of generating them via TTS.

### How it works

When `--real-audio <directory>` is provided:
- For each scenario step, look for `<real-audio-dir>/<scenario_id>/user_<turn>.wav`
- If the file exists, skip TTS and use it directly for ASR transcription
- If the file does NOT exist, fall back to TTS as usual (so you can mix real and synthetic audio)
- Bot audio is always generated via TTS (that's fine — we're testing user-side ASR)

### Changes to `cli.py`

Add a new option to the `scenarios` command:

```python
real_audio: str = typer.Option(None, help="Directory with pre-recorded user WAV files")
```

Pass it through to `run_directory` and `run_scenario`.

### Changes to `simulator.py`

In `run_scenario`, change the user audio section:

```python
# Check for pre-recorded audio
real_wav = None
if real_audio_dir:
    candidate = Path(real_audio_dir) / s.id / f"user_{i}.wav"
    if candidate.exists():
        real_wav = str(candidate)

if real_wav:
    user_wav = real_wav
    user_transcript = transcribe(user_wav, model_size=model_size)
else:
    user_wav = f"{audio_dir}/{s.id}/user_{i}.wav"
    synthesize(user_text, user_wav)
    user_transcript = transcribe(user_wav, model_size=model_size)
```

### Changes to `run_directory`

Add `real_audio_dir` parameter and pass through to `run_scenario`.

### Add a test

**File:** `tests/test_simulator.py` (new file)

Test that when a real audio file exists at the expected path, TTS `synthesize` is NOT called for that step. Mock both `synthesize` and `transcribe`.

**Checklist:**
- [ ] `--real-audio` option added to CLI
- [ ] `run_scenario` checks for pre-recorded WAVs before calling TTS
- [ ] Falls back to TTS when real audio file is missing
- [ ] `run_directory` passes real_audio_dir through
- [ ] Test in `tests/test_simulator.py`
- [ ] All existing tests still pass

---

## Task 6: GitHub Actions CI

**File:** `.github/workflows/ci.yml` (new)

Add a CI workflow so employers can see green checkmarks without cloning.

```yaml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Install ffmpeg
        run: sudo apt-get update && sudo apt-get install -y ffmpeg

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.13"

      - name: Install Poetry
        run: pipx install poetry

      - name: Install dependencies
        run: poetry install

      - name: Run tests
        run: poetry run pytest -v
```

Note: Only run `pytest`, NOT the full scenario evaluation. The scenario run requires internet (gTTS, Claude API) and downloads ASR models — too slow for CI. Tests are fast, mocked, and sufficient to prove the code works.

**Checklist:**
- [ ] `.github/workflows/ci.yml` created
- [ ] Workflow runs `poetry install` + `poetry run pytest -v`
- [ ] Does NOT run full scenario evaluation (too slow for CI)

---

## Task 7: Sample report output

**File:** `out/report.md`

Make sure a sample evaluation report is committed to the repo so employers can see what the output looks like without running anything. This file already exists but may be stale after the gTTS switch and new goals.

After all other tasks are done:
1. Run `poetry run voice-eval scenarios scenarios/` locally
2. Verify `out/report.md` shows passing scenarios with non-empty ASR transcripts
3. Commit the updated `out/report.md`

Also make sure `.gitignore` does NOT ignore `out/report.md` (it currently doesn't — the audio files are ignored but the report is kept).

**Checklist:**
- [ ] `out/report.md` contains a fresh evaluation run with passing scenarios
- [ ] Report has non-empty ASR transcripts (proves gTTS works)
- [ ] File is committed to the repo

---

## Task 8: Demo recording section in README

**File:** `README.md`

Add a section near the top of the README (after the description, before installation) with a placeholder for a demo recording. The user (pnhek) will record this themselves — Codex just needs to add the markdown structure.

Add this section:

```markdown
## Demo

> A short walkthrough of installation, running scenarios, and viewing the evaluation report.

<!-- Replace the link below with your Loom/YouTube recording URL -->
[Watch the demo](https://example.com/your-demo-link)
```

Also add a note at the bottom of the README:

```markdown
## Sample Output

See [`out/report.md`](out/report.md) for a sample evaluation report generated by the framework.
```

**Checklist:**
- [ ] Demo section added to README with placeholder link
- [ ] Sample Output section added to README linking to `out/report.md`

---

## Task 9: Update documentation

### `CLAUDE.md`

- Update the architecture diagram — the pipeline is now: TTS → ASR → slot extraction (regex) → Claude bot brain → evaluation
- Remove references to `policy_decision_tool` and `generate_response_tool` as the active bot logic
- Add `bot_brain.py` to module responsibilities
- Document the `--real-audio` flag in the Commands section
- Note that `ANTHROPIC_API_KEY` is now required for both the bot and the Claude judge

### `README.md`

- Update the architecture description to reflect LLM-powered bot
- Document the `--real-audio` flag with usage example
- Add a section about recording real audio and the expected directory structure:
  ```
  recordings/
    <scenario_id>/
      user_1.wav
      user_2.wav
      ...
  ```
- Mention that the bot uses Claude Haiku for decisions/responses and optionally Claude for evaluation

**Checklist:**
- [ ] CLAUDE.md updated with new architecture
- [ ] README.md updated with new architecture
- [ ] `--real-audio` documented in both

---

## Verification

After all tasks, run:

```bash
# All tests pass
poetry run pytest -v

# Scenarios run with rules judge (bot is Claude-powered, judge is rule-based)
poetry run voice-eval scenarios scenarios/

# Scenarios run with Claude judge (bot AND judge are Claude-powered)
poetry run voice-eval scenarios scenarios/ --judge claude

# Real audio mode works (will fall back to TTS if no recordings dir exists yet)
poetry run voice-eval scenarios scenarios/ --real-audio recordings/
```

---

## Goal strings (exact, case-sensitive — must match between YAML scenarios and bot_brain.py system prompt)

1. `"Return a damaged item"`
2. `"Request refund for duplicate charge"`
3. `"Change shipping address"`
4. `"Cancel an order"`
5. `"Check order status"`
6. `"Reset account password"`
7. `"Report a missing package"`
8. `"Upgrade subscription plan"`
