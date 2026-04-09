# CLAUDE.md

This file provides guidance to Claude Code when working with code in this repository.

## What This Is

An intent detection and dialogue evaluation framework that simulates end-to-end voice conversations and scores bot responses against YAML-defined expectations.

## Setup

```bash
poetry install
```

`ffmpeg` is a required system dependency for `faster-whisper`.

```bash
# macOS
brew install ffmpeg
```

## Commands

```bash
# Run all scenarios (default: rules judge, tiny ASR model)
# Requires ANTHROPIC_API_KEY because the bot brain uses Claude
poetry run voice-eval scenarios scenarios/

# Full options
poetry run voice-eval scenarios scenarios/ --report out/report.md --audio-dir out/audio --model tiny --judge rules

# Use pre-recorded user audio when available, falling back to TTS otherwise
poetry run voice-eval scenarios scenarios/ --real-audio recordings/

# Claude judge (requires ANTHROPIC_API_KEY)
poetry run voice-eval scenarios scenarios/ --judge claude

# Larger ASR model for better transcription accuracy
poetry run voice-eval scenarios scenarios/ --model base

# Test suite
poetry run pytest
poetry run pytest -v
```

## Architecture

The system is a linear pipeline, orchestrated by `simulator.py`:

```text
YAML scenario -> for each step:
  user text -> TTS (gTTS) or pre-recorded user audio -> ASR (faster-whisper) -> transcript
  -> slot extraction (regex) -> Claude bot brain (intent detection + intent-routed response)
  -> evaluation (rules or Claude) -> transcript record
-> markdown report
```

Key design choice: the scenario `goal` is ground truth for evaluation only. The bot never receives that goal string. It must infer the customer's intent from the conversation and return a `detected_intent`, which is then compared against the scenario goal. There is no real MCP server in the runtime flow.

### Module Responsibilities

- `cli.py` — Typer CLI entry point. Wires `run_directory` to `write_markdown_report`.
- `simulator.py` — Core loop. `run_scenario()` processes one scenario step-by-step, accumulates slots across turns, and compares `detected_intent` against the scenario goal. `run_directory()` loads and iterates all YAML files.
- `bot_brain.py` — Claude-powered bot logic. Detects intent from the conversation, then generates an intent-routed action and utterance. It does not receive the scenario goal.
- `bot_tools.py` — Regex-based slot extraction helpers used before the bot brain runs.
- `tool_client.py` — Thin dispatch layer that currently maps the `extract_slots` tool to `bot_tools.py`.
- `evaluator_rules.py` — Deterministic substring-based expectation checks.
- `evaluator_claude.py` — Claude structured-output evaluator using the Anthropic API.
- `audio/tts.py` / `audio/asr.py` — TTS via gTTS, ASR via faster-whisper with int8 -> float32 fallback. ASR returns lowercased text.

### Extending the Bot

Adding a new conversation flow usually requires changes in three places:

1. Add or adjust regex patterns in `voice_eval/bot_tools.py` if the flow needs new slots.
2. Update the valid intent list, routing policy, and prompt guidance in `voice_eval/bot_brain.py`.
3. Add a YAML scenario in `scenarios/` with the exact ground-truth `goal` string used for evaluation.

The bot should still infer the intent from the conversation itself rather than being told the goal directly.

## Scenario Format

```yaml
id: unique_id
goal: "Exact goal string"
steps:
  - user: "What the user says"
    bot_expect:
      contains_any: ["phrase1", "phrase2"]
  - user: "Next turn"
    bot_expect:
      contains: "exact phrase"
```

## Environment Variables

Configured via `.env` (copy from `env.example`):

- `ANTHROPIC_API_KEY` (required for the Claude bot brain in normal scenario runs, and also for the optional `--judge claude` evaluator)
- `DEFAULT_ASR_MODEL` (default: `tiny`)
