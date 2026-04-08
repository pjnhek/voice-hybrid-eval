# CLAUDE.md

This file provides guidance to Claude Code when working with code in this repository.

## What This Is

A voice-bot evaluation framework that simulates end-to-end voice conversations and scores bot responses against YAML-defined expectations.

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
poetry run voice-eval scenarios scenarios/

# Full options
poetry run voice-eval scenarios scenarios/ --report out/report.md --audio-dir out/audio --model tiny --judge rules

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
  user text -> TTS (pyttsx3) -> WAV -> ASR (faster-whisper) -> transcript
  -> slot extraction (regex) -> policy decision (rule tree) -> response generation (templates)
  -> evaluation (rules or Claude) -> transcript record
-> markdown report
```

Key design choice: the bot pipeline is still rule-based. The old `mcp_*` naming has been replaced with honest tool-oriented names. There is no real MCP server in the runtime flow. The only model-based evaluator is the optional Claude judge in `evaluator_claude.py`.

### Module Responsibilities

- `cli.py` — Typer CLI entry point. Wires `run_directory` to `write_markdown_report`.
- `simulator.py` — Core loop. `run_scenario()` processes one scenario step-by-step, accumulating slots across turns. `run_directory()` loads and iterates all YAML files.
- `bot_tools.py` — Three tool functions that form the bot brain: `extract_slots_tool`, `policy_decision_tool`, `generate_response_tool`.
- `tool_client.py` — Thin dispatch layer that maps tool names to functions.
- `evaluator_rules.py` — Deterministic substring-based expectation checks.
- `evaluator_claude.py` — Claude structured-output evaluator using the Anthropic API.
- `audio/tts.py` / `audio/asr.py` — TTS via pyttsx3, ASR via faster-whisper with int8 -> float32 fallback. ASR returns lowercased text.

### Extending the Bot

Adding a new conversation flow requires changes in three places in `bot_tools.py`:

1. New regex patterns in `extract_slots_tool` for any new slot types.
2. New goal branch in `policy_decision_tool` mapping slots to actions.
3. New action templates in `generate_response_tool`.

Then add a YAML scenario in `scenarios/` with a matching `goal` string and `bot_expect` assertions.

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

- `ANTHROPIC_API_KEY` (required for `--judge claude`)
- `DEFAULT_ASR_MODEL` (default: `tiny`)
