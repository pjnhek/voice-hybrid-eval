# Implementation Plan: Intent Detection Evaluation Framework

This document is the source of truth for remaining changes. Codex should implement each task and check it off. Claude Code will review the changes afterward.

---

## Completed Tasks (0–4.1)

- **Task 0:** Fix scenario loader and clean up old scenarios — DONE
- **Task 1:** Add 5 new goals to `bot_tools.py` — DONE
- **Task 2:** Remove Ollama judge — DONE
- **Task 3:** Replace rule-based bot with Claude-powered bot — DONE
- **Task 4:** Replace pyttsx3 with gTTS — DONE
- **Task 4.1:** Load `.env` with python-dotenv — DONE

---

## Task 5: Add real audio input mode to `simulator.py`

**Files:** `voice_eval/simulator.py`, `voice_eval/cli.py`

Add a `--real-audio` flag that tells the simulator to use pre-recorded audio files instead of generating them via TTS.

### How it works

When `--real-audio <directory>` is provided:
- For each scenario step, look for `<real-audio-dir>/<scenario_id>/user_<turn>.<ext>` where `<ext>` is any of: `.wav`, `.m4a`, `.mp3`, `.ogg`, `.flac`
- Check extensions in that order, use the first match
- If a file exists, skip TTS and use it directly for ASR transcription (faster-whisper uses ffmpeg internally, so all these formats work)
- If NO file is found for any extension, fall back to TTS as usual (so you can mix real and synthetic audio)
- Bot audio is always generated via TTS (that's fine — we're testing user-side ASR)

### Changes to `cli.py`

Add a new option to the `scenarios` command:

```python
real_audio: str = typer.Option(None, help="Directory with pre-recorded user audio files (.wav, .m4a, .mp3, .ogg, .flac)")
```

Pass it through to `run_directory` and `run_scenario`.

### Changes to `simulator.py`

Add a helper and update the user audio section in `run_scenario`:

```python
_AUDIO_EXTENSIONS = (".wav", ".m4a", ".mp3", ".ogg", ".flac")


def _find_real_audio(real_audio_dir: Path, scenario_id: str, turn: int) -> str | None:
    """Find a pre-recorded audio file for a given scenario turn."""
    for ext in _AUDIO_EXTENSIONS:
        candidate = real_audio_dir / scenario_id / f"user_{turn}{ext}"
        if candidate.exists():
            return str(candidate)
    return None


# ... in run_scenario, inside the step loop:

real_audio_file = None
if real_audio_dir:
    real_audio_file = _find_real_audio(Path(real_audio_dir), s.id, i)

if real_audio_file:
    user_wav = real_audio_file
    user_transcript = transcribe(user_wav, model_size=model_size)
else:
    user_wav = f"{audio_dir}/{s.id}/user_{i}.wav"
    synthesize(user_text, user_wav)
    user_transcript = transcribe(user_wav, model_size=model_size)
```

### Changes to `run_directory`

Add `real_audio_dir` parameter and pass through to `run_scenario`.

### Tests

**File:** `tests/test_simulator.py`

Test that when a real audio file exists at the expected path (any supported extension), TTS `synthesize` is NOT called for that step. Also test that the extension priority order works (`.wav` preferred over `.m4a` if both exist). Mock both `synthesize` and `transcribe`.

**Checklist:**
- [x] `--real-audio` option added to CLI
- [x] `_find_real_audio` helper checks all extensions in priority order
- [x] `run_scenario` checks for pre-recorded files before calling TTS
- [x] Falls back to TTS when no real audio file is found
- [x] `run_directory` passes `real_audio_dir` through
- [x] Tests in `tests/test_simulator.py` for real audio path and extension priority
- [x] All existing tests still pass

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
- [x] `.github/workflows/ci.yml` created
- [x] Workflow runs `poetry install` + `poetry run pytest -v`
- [x] Does NOT run full scenario evaluation (too slow for CI)

---

## Task 7: Intent detection mode

**This is the core feature change.** Currently the bot is handed the `goal` string in its system prompt — it already knows the customer's intent. This makes the evaluation shallow. Change the bot so it must **infer intent from the conversation itself**, then evaluate whether it detected the right one.

### Design overview

The `goal` field in YAML scenarios becomes **ground truth for evaluation**, not an instruction to the bot. The bot receives no goal — it must figure out what the customer wants from their utterances.

### Changes to `voice_eval/bot_brain.py`

**1. Add `detected_intent` to the structured output schema:**

```python
_BOT_RESPONSE_SCHEMA = {
    "type": "object",
    "properties": {
        "action": {"type": "string"},
        "utterance": {"type": "string"},
        "detected_intent": {"type": "string"},
    },
    "required": ["action", "utterance", "detected_intent"],
    "additionalProperties": False,
}
```

**2. Remove `goal` from the function signature. Replace the system prompt:**

```python
def generate_bot_response(
    client: Anthropic,
    user_input: str,
    slots: Dict[str, Any],
    conversation_history: List[HistoryEntry],
) -> Dict[str, Any]:
```

**3. New system prompt** (replaces `_create_system_prompt`):

```python
def _create_system_prompt(slots: Dict[str, Any]) -> str:
    extracted_info = (
        json.dumps(slots, indent=2, sort_keys=True)
        if slots
        else "No information extracted yet."
    )

    return f"""You are a customer service bot for a retail company. The customer is calling in and you must figure out what they need, then help them.

You have access to the following extracted information from the conversation:
{extracted_info}

For every response, you must:
1. Determine what the customer's intent is based on everything they've said so far.
2. Decide the next action to take.
3. Respond naturally to the customer.

Rules:
- If you need information from the customer (order number, card info, email, account number), ask for it politely.
- If you have enough information to fulfill the request, confirm the action and provide details.
- Be concise and professional. One to two sentences max.
- Do NOT make up order numbers, tracking info, or other specific data not in the extracted slots.
- When confirming an action, reference the specific information the customer provided.

Your detected_intent must be one of these exact strings:
- "Return a damaged item"
- "Request refund for duplicate charge"
- "Change shipping address"
- "Cancel an order"
- "Check order status"
- "Reset account password"
- "Report a missing package"
- "Upgrade subscription plan"

Valid actions: ASK_ORDER_NUMBER, ASK_CARD_INFO, ASK_EMAIL, ASK_ACCOUNT_NUMBER, ASK_CLARIFY,
CONFIRM_RETURN, CONFIRM_ADDRESS_CHANGE, CONFIRM_CANCELLATION, PROCESS_REFUND,
PROVIDE_STATUS, SEND_RESET_LINK, OPEN_INVESTIGATION, CONFIRM_UPGRADE"""
```

Key changes from the old prompt:
- No `goal` given — the bot must infer it
- `detected_intent` is required in the response, constrained to the 8 known intent strings
- The prompt explicitly tells the bot to determine intent from what the customer has said

### Changes to `voice_eval/simulator.py`

**1. Remove `goal` from the `generate_bot_response` call:**

```python
bot_response = generate_bot_response(
    client=client,
    user_input=user_transcript,
    slots=slots,
    conversation_history=conversation_history,
)

bot_text = bot_response["utterance"]
action = bot_response["action"]
detected_intent = bot_response["detected_intent"]
```

**2. Evaluate intent detection** — compare `detected_intent` against `s.goal`:

```python
intent_correct = detected_intent == s.goal
```

**3. Add intent fields to the transcript entry:**

```python
transcript.append({
    "turn": i,
    "user_text": user_text,
    "user_asr": user_transcript,
    "bot_text": bot_text,
    "action": action,
    "slots": dict(slots),
    "detected_intent": detected_intent,
    "expected_intent": s.goal,
    "intent_correct": intent_correct,
    "pass": ok,
    "error": error,
    "expectation": step.bot_expect or {},
    "user_wav": user_wav,
    "bot_wav": bot_wav,
})
```

**4. Add intent accuracy to scenario result:**

```python
intent_results = [entry["intent_correct"] for entry in transcript]
# Intent is considered correct if the bot got it right on the LAST turn
# (it may take 1-2 turns to figure it out, that's fine)
intent_detected = intent_results[-1] if intent_results else False
# Also track which turn the bot first got it right
first_correct_turn = None
for entry in transcript:
    if entry["intent_correct"]:
        first_correct_turn = entry["turn"]
        break

return {
    "scenario_id": s.id,
    "goal": s.goal,
    "scenario_pass": scenario_pass,
    "intent_detected": intent_detected,
    "first_correct_turn": first_correct_turn,
    "steps_expected": steps_expected,
    "steps_passed": steps_passed,
    "transcript": transcript,
}
```

### Changes to `voice_eval/reporters/markdown.py`

Update the report to show intent detection results.

**1. Add intent accuracy to the summary table:**

```python
f.write("| Scenario | Intent | Result | Steps Passed |\n")
f.write("|----------|--------|--------|--------------|\n")

for result in results:
    status = "✅ PASS" if result["scenario_pass"] else "❌ FAIL"
    intent = "✅" if result["intent_detected"] else "❌"
    first = f" (turn {result['first_correct_turn']})" if result["first_correct_turn"] else ""
    f.write(f"| {result['scenario_id']} | {intent}{first} | {status} | {result['steps_passed']}/{result['steps_expected']} |\n")
```

**2. Add an overall intent accuracy summary at the top:**

```python
total = len(results)
intent_correct = sum(1 for r in results if r["intent_detected"])
f.write(f"**Intent Detection Accuracy:** {intent_correct}/{total} ({100 * intent_correct // total}%)\n\n")
```

**3. Show intent per turn in the detailed section:**

```python
f.write(f"**Detected Intent:** {turn['detected_intent']}")
if turn['intent_correct']:
    f.write(" ✅\n\n")
else:
    f.write(f" ❌ (expected: {turn['expected_intent']})\n\n")
```

### Changes to `voice_eval/cli.py`

Update the summary print to include intent accuracy:

```python
intent_correct = sum(1 for r in results if r["intent_detected"])
print(f"{passed_scenarios}/{total_scenarios} scenarios passed")
print(f"Intent detection: {intent_correct}/{total_scenarios} correct")
```

### Tests

**File:** `tests/test_bot_brain.py`

Update existing tests — `generate_bot_response` no longer takes `goal`. Mock responses now include `detected_intent`. Add:
- Test that system prompt does NOT contain a goal/task instruction
- Test that system prompt lists all 8 valid intents
- Test that `detected_intent` is returned in the response dict

**File:** `tests/test_simulator.py`

Update existing tests — mock `generate_bot_response` returns now include `detected_intent`. Add:
- Test that transcript entries include `detected_intent`, `expected_intent`, `intent_correct`
- Test that `intent_detected` in result reflects last turn's intent correctness
- Test that `first_correct_turn` tracks when intent was first detected

**File:** `tests/test_markdown_report.py` (new)

- Test that report includes intent accuracy summary
- Test that per-turn output shows detected intent with ✅/❌

**Checklist:**
- [x] `bot_brain.py`: `goal` removed from function signature
- [x] `bot_brain.py`: system prompt rewritten — no goal, bot must infer intent
- [x] `bot_brain.py`: `detected_intent` added to structured output schema
- [x] `bot_brain.py`: `_create_system_prompt` no longer takes `goal`
- [x] `simulator.py`: `generate_bot_response` called without `goal`
- [x] `simulator.py`: `detected_intent` extracted from response and compared to `s.goal`
- [x] `simulator.py`: transcript entries include `detected_intent`, `expected_intent`, `intent_correct`
- [x] `simulator.py`: scenario result includes `intent_detected` and `first_correct_turn`
- [x] `reporters/markdown.py`: summary table shows intent column
- [x] `reporters/markdown.py`: overall intent accuracy percentage at top
- [x] `reporters/markdown.py`: per-turn detected intent with ✅/❌
- [x] `cli.py`: print includes intent accuracy
- [x] Tests updated in `test_bot_brain.py` (no goal, detected_intent in response)
- [x] Tests updated in `test_simulator.py` (intent tracking fields)
- [x] Tests added in `test_markdown_report.py` (intent in report)
- [x] All existing tests still pass

---

## Task 8: Sample report output

**File:** `out/report.md`

After all other tasks are done:
1. Run `poetry run voice-eval scenarios scenarios/` locally
2. Verify `out/report.md` shows intent detection accuracy and per-turn intent results
3. Verify non-empty ASR transcripts
4. Commit the updated `out/report.md`

Also make sure `.gitignore` does NOT ignore `out/report.md`.

**Checklist:**
- [x] `out/report.md` contains a fresh evaluation run
- [x] Report shows intent detection accuracy percentage
- [x] Report shows per-turn detected intent with ✅/❌
- [x] Report has non-empty ASR transcripts
- [ ] File is committed to the repo

---

## Task 8.1: Intent-routed action policy

**This replaces the current single broad Claude prompt with a two-stage flow.**

**Files:** `voice_eval/bot_brain.py`, `tests/test_bot_brain.py`

Keep intent detection LLM-driven, but stop asking the same prompt to infer intent, choose the workflow, and word the reply all at once.

### Design overview

The bot should work more like lightweight tool calling:

1. **Intent detection call**
   - Input: conversation history, latest ASR transcript, extracted slots
   - Output: exactly one of the 8 known intents

2. **Intent-routed response call**
   - Input: detected intent, conversation history, latest ASR transcript, extracted slots
   - Output: `action` + `utterance`
   - The prompt is now **intent-specific** and includes only the allowed actions and workflow rules for that intent

This keeps the model flexible where it helps most (intent classification), but constrains policy behavior after routing so the bot acts more like an agent choosing from a narrow tool set.

### Why this change is needed

The current broad prompt is already strong at intent detection, but it is too loose at workflow:
- It often asks for the wrong slot for a given intent
- It sometimes asks extra follow-up questions even when the benchmark expects a final action
- It often says the right thing semantically, but misses the exact confirmation wording the rules judge is looking for

The scenario suite is effectively an **intent-routing benchmark with one required slot per flow**. Once the relevant slot is present, the bot should usually perform the final action immediately.

### Changes to `voice_eval/bot_brain.py`

**1. Split bot generation into two internal stages**

Keep the public API the same:

```python
def generate_bot_response(
    client: Anthropic,
    user_input: str,
    slots: Dict[str, Any],
    conversation_history: List[HistoryEntry],
) -> Dict[str, Any]:
```

But internally split it into:

```python
def detect_intent(...) -> str
def generate_intent_response(...) -> Dict[str, str]
```

`generate_bot_response()` should orchestrate both calls and still return:

```python
{
    "action": "...",
    "utterance": "...",
    "detected_intent": "...",
}
```

This keeps `simulator.py` unchanged.

**2. Add a strict intent-detection schema**

Use a structured output schema constrained to the exact 8 allowed intents:

```python
_INTENT_DETECTION_SCHEMA = {
    "type": "object",
    "properties": {
        "detected_intent": {
            "type": "string",
            "enum": [
                "Return a damaged item",
                "Request refund for duplicate charge",
                "Change shipping address",
                "Cancel an order",
                "Check order status",
                "Reset account password",
                "Report a missing package",
                "Upgrade subscription plan",
            ],
        },
    },
    "required": ["detected_intent"],
    "additionalProperties": False,
}
```

**3. Add an intent policy map**

Create a single source of truth describing each routed workflow:

```python
_INTENT_POLICIES = {
    "Cancel an order": {
        "required_slot": "order_number",
        "ask_action": "ASK_ORDER_NUMBER",
        "final_action": "CONFIRM_CANCELLATION",
        "allowed_actions": ["ASK_ORDER_NUMBER", "CONFIRM_CANCELLATION"],
    },
    ...
}
```

Policy expectations for this benchmark:

- `Cancel an order`
  Ask only for `order_number`; once present, confirm cancellation
- `Change shipping address`
  Ask only for `order_number`; once present, confirm the shipping address change
- `Return a damaged item`
  Ask only for `order_number`; once present, confirm the return and mention a return label
- `Request refund for duplicate charge`
  Ask only for `card_info`; once present, process the refund
- `Check order status`
  Ask only for `order_number`; once present, provide status wording
- `Reset account password`
  Ask only for `email`; once present, send the reset link
- `Report a missing package`
  Ask only for `order_number`; once present, open an investigation
- `Upgrade subscription plan`
  Ask only for `account_number`; once present, confirm the upgrade

Important: for this benchmark, **do not ask unrelated follow-up questions** once the required slot is present.

**4. Add an intent-specific response schema**

The second call should use a dynamic schema restricted to the routed intent's allowed actions:

```python
{
    "type": "object",
    "properties": {
        "action": {"type": "string", "enum": allowed_actions},
        "utterance": {"type": "string"},
    },
    "required": ["action", "utterance"],
    "additionalProperties": False,
}
```

`detected_intent` should come from the first call, not be regenerated in the second call.

**5. Replace the broad system prompt with two focused prompt builders**

Add:

```python
def _create_intent_detection_prompt(slots: Dict[str, Any]) -> str
def _create_intent_action_prompt(intent: str, slots: Dict[str, Any]) -> str
```

The second prompt should explicitly say:
- what intent has already been chosen
- which slot is required for this intent
- which actions are valid for this intent
- when to ask for the missing slot
- when to perform the final action
- what wording should appear in a successful final response

### Response wording constraints for benchmark compatibility

Because the rules judge is substring-based, the routed prompts should steer final responses toward benchmark-friendly phrases:

- `CONFIRM_CANCELLATION`: include `cancelled` or `canceled`
- `CONFIRM_ADDRESS_CHANGE`: include `shipping address` and `updated` or `changed`
- `CONFIRM_RETURN`: include `return` and `return label`
- `PROCESS_REFUND`: include `refund`
- `PROVIDE_STATUS`: include `status`, `processing`, `shipped`, `delivered`, or `in transit`
- `SEND_RESET_LINK`: include `reset link` or `check your email`
- `OPEN_INVESTIGATION`: include `investigation`, `looking into`, or `investigate`
- `CONFIRM_UPGRADE`: include `upgraded`, `upgrade confirmed`, `subscription has been updated`, or `new plan`

### Tests

**File:** `tests/test_bot_brain.py`

Add tests for the new two-stage flow:

- `generate_bot_response()` makes two Claude calls
- The first call uses the 8-intent enum schema
- The second call only allows actions valid for the detected intent
- `Cancel an order` only allows `ASK_ORDER_NUMBER` or `CONFIRM_CANCELLATION`
- `Request refund for duplicate charge` only allows `ASK_CARD_INFO` or `PROCESS_REFUND`
- `Reset account password` only allows `ASK_EMAIL` or `SEND_RESET_LINK`
- `Upgrade subscription plan` only allows `ASK_ACCOUNT_NUMBER` or `CONFIRM_UPGRADE`
- Final return value still includes `action`, `utterance`, and `detected_intent`

No `simulator.py` interface changes should be needed if the return shape stays the same.

### Partial failure handling

Since `generate_bot_response` makes two calls internally, handle the case where intent detection succeeds but the action call fails. If the second call raises, `generate_bot_response` should catch the exception and return a fallback response that **preserves the detected intent**:

```python
{
    "action": "ASK_CLARIFY",
    "utterance": "I'm sorry, I encountered an error. Could you please try again?",
    "detected_intent": detected_intent,  # keep the successful intent
}
```

This way `simulator.py` doesn't need changes — it still gets a valid response dict. The intent detection result is preserved even when action generation fails.

Add a test for this: mock the first call to succeed, the second to raise, and assert the returned dict has the correct `detected_intent` but `action` is `"ASK_CLARIFY"`.

**Checklist:**
- [x] `bot_brain.py` split into intent-detection and intent-routed response stages
- [x] Intent detection schema constrained to the 8 exact intent strings
- [x] `_INTENT_POLICIES` added with required slot, ask action, final action, and allowed actions
- [x] Second-stage response schema restricted to actions valid for the detected intent
- [x] Intent-specific prompts added with explicit workflow rules
- [x] Final-response wording guidance added for benchmark compatibility
- [x] `tests/test_bot_brain.py` updated for the new two-call flow
- [x] Partial failure test: intent detection succeeds, action call fails → returns fallback with preserved `detected_intent`
- [x] Existing simulator/report tests still pass

---

## Task 9: Update documentation

### `CLAUDE.md`

- Update the architecture diagram — the pipeline is now: TTS → ASR → slot extraction (regex) → Claude bot brain (intent detection + response) → evaluation
- Remove references to `policy_decision_tool` and `generate_response_tool` as the active bot logic
- Add `bot_brain.py` to module responsibilities — note that it infers intent, not receives it
- Document the `--real-audio` flag in the Commands section
- Note that `ANTHROPIC_API_KEY` is required (bot + optional Claude judge)
- Document that the bot receives no goal — it must detect intent from the conversation

### `README.md`

- Update the project description: this is an **intent detection and dialogue evaluation framework**, not just a voice bot evaluator
- Update the architecture description to reflect intent detection
- Document the `--real-audio` flag with usage example
- Add a section about recording real audio and the expected directory structure:
  ```
  recordings/
    <scenario_id>/
      user_1.wav   (or .m4a, .mp3, .ogg, .flac)
      user_2.m4a
      ...
  ```
- Explain how intent detection is evaluated (bot returns `detected_intent`, compared against scenario `goal` as ground truth)
- Add a Sample Output section linking to `out/report.md`

**Checklist:**
- [ ] CLAUDE.md updated with intent detection architecture
- [ ] README.md updated with intent detection focus
- [ ] `--real-audio` documented in both
- [ ] Intent detection evaluation explained in README

---

## Verification

After all tasks, run:

```bash
# All tests pass
poetry run pytest -v

# Run with rules judge — bot detects intent, judge checks response keywords
poetry run voice-eval scenarios scenarios/

# Run with Claude judge — bot detects intent, Claude judges response quality
poetry run voice-eval scenarios scenarios/ --judge claude

# Real audio mode
poetry run voice-eval scenarios scenarios/ --real-audio recordings/
```

---

## Goal strings (exact, case-sensitive — ground truth labels in YAML, also the valid `detected_intent` values)

1. `"Return a damaged item"`
2. `"Request refund for duplicate charge"`
3. `"Change shipping address"`
4. `"Cancel an order"`
5. `"Check order status"`
6. `"Reset account password"`
7. `"Report a missing package"`
8. `"Upgrade subscription plan"`
