# Implementation Plan: Expand Goals & Real Audio Support

This document is the source of truth for the next round of changes. Codex should implement each task and check it off. Claude Code will review the changes afterward.

---

## Task 0: Fix scenario loader and clean up old scenarios

### Fix `voice_eval/scenario.py`

The new Gemini-generated YAML files contain multiple scenarios per file as a YAML list (e.g., `- id: cancel_order_001`). The current `load_scenario` function only handles single-scenario files (top-level dict with `id` key).

Update `load_scenario` to detect the format:
- If `yaml.safe_load()` returns a **dict** → single scenario (existing behavior)
- If it returns a **list** → multiple scenarios, return a list

Better approach: replace `load_scenario` (returns one) with logic in `load_scenarios` that handles both:

```python
def load_scenarios(dir_path: Path) -> List[Scenario]:
    scenarios = []
    for yaml_file in sorted(dir_path.glob("*.yaml")):
        data = yaml.safe_load(yaml_file.read_text(encoding="utf-8"))
        if isinstance(data, list):
            for item in data:
                scenarios.append(_parse_scenario(item, yaml_file))
        elif isinstance(data, dict):
            scenarios.append(_parse_scenario(data, yaml_file))
    return scenarios
```

Extract the parsing logic into a `_parse_scenario(data: dict, path: Path) -> Scenario` helper that does the validation and Step construction.

### Delete old scenario files

Delete these — they're superseded by the new Gemini-generated files with more variety:
- `scenarios/order_return.yaml`
- `scenarios/order_return_variations.yaml`
- `scenarios/billing_refund.yaml`
- `scenarios/shipping_address.yaml`

### Update tests

Update `tests/test_scenario.py`:
- Add a test for loading a multi-scenario YAML file (list format)
- Update `test_load_scenarios_returns_all_yaml_files` to account for multi-scenario files
- Keep the single-scenario and missing-id tests

**Checklist:**
- [x] `scenario.py` handles both list and dict YAML formats
- [x] Old 4 scenario files deleted
- [x] Tests updated for multi-scenario format
- [x] `poetry run pytest` passes
- [x] `poetry run voice-eval scenarios scenarios/` loads all 80 scenarios

---

## Task 1: Add 5 new goals to `bot_tools.py`

**File:** `voice_eval/bot_tools.py`

The bot currently handles 3 goals. Add 5 more. Each new goal requires changes in all three tool functions.

### 1a. `extract_slots_tool` — add new regex patterns

Add extraction for these new slot types:

- **email**: Extract email addresses from user input. Pattern: standard email regex. Store as `slots["email"]`.
- **account_number**: Extract account numbers (alphanumeric, 5-8 chars). Trigger on phrases like "account number", "account", "my account is". Store as `slots["account_number"]`.

The existing `order_number` and `card_info` extractors stay unchanged — some new goals also use `order_number`.

### 1b. `policy_decision_tool` — add new goal branches

Add these branches after the existing three, following the same pattern:

```
goal: "Cancel an order"
  - has order_number → CONFIRM_CANCELLATION
  - missing → ASK_ORDER_NUMBER

goal: "Check order status"
  - has order_number → PROVIDE_STATUS
  - missing → ASK_ORDER_NUMBER

goal: "Reset account password"
  - has email → SEND_RESET_LINK
  - missing → ASK_EMAIL

goal: "Report a missing package"
  - has order_number → OPEN_INVESTIGATION
  - missing → ASK_ORDER_NUMBER

goal: "Upgrade subscription plan"
  - has account_number → CONFIRM_UPGRADE
  - missing → ASK_ACCOUNT_NUMBER
```

### 1c. `generate_response_tool` — add new response templates

Add these to the `responses` dict:

```python
"CONFIRM_CANCELLATION": f"Your order {slots.get('order_number', 'that order')} has been cancelled. You will receive a confirmation email shortly.",
"PROVIDE_STATUS": f"Order {slots.get('order_number', 'that order')} is currently being processed and is expected to arrive within 3-5 business days.",
"SEND_RESET_LINK": f"I've sent a password reset link to {slots.get('email', 'your email address')}. Please check your inbox and spam folder.",
"OPEN_INVESTIGATION": f"I've opened an investigation for order {slots.get('order_number', 'that order')}. Our team will look into the missing package and follow up within 24-48 hours.",
"CONFIRM_UPGRADE": f"Your subscription has been upgraded. The changes to account {slots.get('account_number', 'your account')} will take effect immediately.",
"ASK_EMAIL": "I can help you with that. Could you please provide the email address associated with your account?",
"ASK_ACCOUNT_NUMBER": "I can help you with that. Could you please provide your account number?",
```

### 1d. Add tests for new goals

**File:** `tests/test_bot_tools.py`

Add tests for:
- `extract_slots_tool` extracting email addresses
- `extract_slots_tool` extracting account numbers
- `policy_decision_tool` for each new goal (with and without required slots)
- `generate_response_tool` for each new action

~10 new tests.

**Checklist:**
- [ ] New regex patterns in `extract_slots_tool` for email and account_number
- [ ] 5 new goal branches in `policy_decision_tool`
- [ ] 7 new response templates in `generate_response_tool` (5 confirmations + 2 ask prompts)
- [ ] New tests in `test_bot_tools.py`
- [ ] All existing tests still pass (`poetry run pytest`)

---

## Task 2: Remove Ollama judge

Remove `evaluator_llm.py` and all Ollama references. The project will have two judges: `rules` (default) and `claude`.

### Delete

- `voice_eval/evaluator_llm.py`

### Modify `voice_eval/simulator.py`

- Remove `from .evaluator_llm import check_bot_expect_llm`
- Remove the `elif judge == "ollama"` branch. The judge block should be:
  ```python
  if judge == "claude":
      ok = check_bot_expect_claude(bot_text, step.bot_expect)
  else:
      ok = check_bot_expect_enhanced(bot_text, step.bot_expect)
  ```

### Modify `voice_eval/cli.py`

- Change judge help text to: `"Evaluation judge: rules | claude"`

### Modify `env.example`

- Remove `OLLAMA_BASE_URL` and `OLLAMA_MODEL` lines

### Modify `pyproject.toml`

- Remove `requests` from dependencies (only used by the Ollama evaluator). Check if anything else imports it first — if not, remove it.

### Delete tests

- If any tests reference `evaluator_llm` or `check_bot_expect_llm`, remove them.

### Modify `CLAUDE.md` and `README.md`

- Remove all Ollama references (setup instructions, `--judge ollama`, env vars, etc.)

**Checklist:**
- [ ] `voice_eval/evaluator_llm.py` deleted
- [ ] Ollama import and branch removed from `simulator.py`
- [ ] CLI help text updated
- [ ] Ollama env vars removed from `env.example`
- [ ] `requests` removed from `pyproject.toml` if unused elsewhere
- [ ] Ollama references removed from CLAUDE.md and README.md
- [ ] All tests still pass

---

## Task 3: Replace pyttsx3 with gTTS

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
    # gTTS outputs MP3 natively. Save as MP3 — faster-whisper reads both MP3 and WAV.
    # Use .wav extension for compatibility with the rest of the pipeline,
    # but the actual content will be MP3-encoded. faster-whisper handles this fine
    # via ffmpeg decoding.
    tts.save(out_wav)
```

Note: gTTS requires an internet connection. This is acceptable — the project already requires internet for the Claude judge. If offline support matters later, we can add a fallback.

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

## Task 4: Add real audio input mode to `simulator.py`


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

In `run_scenario`, change the user audio section (~lines 21-25):

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

## Task 5: GitHub Actions CI

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

Note: Only run `pytest`, NOT the full scenario evaluation. The scenario run requires TTS (gTTS needs internet — fine) and ASR (faster-whisper downloads models — slow). Tests are fast, mocked, and sufficient to prove the code works.

**Checklist:**
- [ ] `.github/workflows/ci.yml` created
- [ ] Workflow runs `poetry install` + `poetry run pytest -v`
- [ ] Does NOT run full scenario evaluation (too slow for CI)

---

## Task 6: Sample report output

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

## Task 7: Demo recording section in README

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

## Task 8: Update documentation

### `CLAUDE.md`

- Add the 5 new goals to the architecture section
- Document the `--real-audio` flag in the Commands section
- Update the "Extending the Bot" section if needed

### `README.md`

- Add the new goals to any goal listing
- Document the `--real-audio` flag with usage example:
  ```bash
  poetry run voice-eval scenarios scenarios/ --real-audio recordings/
  ```
- Add a section about recording real audio and the expected directory structure:
  ```
  recordings/
    <scenario_id>/
      user_1.wav
      user_2.wav
      ...
  ```

**Checklist:**
- [ ] CLAUDE.md updated
- [ ] README.md updated

---

## Verification

After all tasks, run:

```bash
# All tests pass
poetry run pytest -v

# Scenarios run with rules judge (existing + new goals if scenarios exist)
poetry run voice-eval scenarios scenarios/

# Real audio mode works (will fall back to TTS if no recordings dir exists yet)
poetry run voice-eval scenarios scenarios/ --real-audio recordings/
```

---

## Goal strings (exact, case-sensitive — must match between YAML scenarios and bot_tools.py)

Existing:
1. `"Return a damaged item"`
2. `"Request refund for duplicate charge"`
3. `"Change shipping address"`

New:
4. `"Cancel an order"`
5. `"Check order status"`
6. `"Reset account password"`
7. `"Report a missing package"`
8. `"Upgrade subscription plan"`
