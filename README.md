# Voice Hybrid Eval

Voice Hybrid Eval is a voice-bot evaluation framework that simulates end-to-end conversations and scores each bot turn against YAML-defined expectations. It runs a full loop of TTS -> ASR -> slot extraction -> policy decision -> response generation -> evaluation, then writes a Markdown report for review.

## Installation

Poetry is the package manager for this project.

```bash
poetry install
```

`ffmpeg` is a required system dependency for audio handling through `faster-whisper`.

```bash
# macOS
brew install ffmpeg

# Ubuntu/Debian example
sudo apt-get install ffmpeg
```

If you want environment-variable based configuration, copy `env.example` to `.env` and fill in the values you need.

```bash
cp env.example .env
```

## Quickstart

Run all scenarios with the default rules judge:

```bash
poetry run voice-eval scenarios scenarios/
```

## Judges

- `rules`: deterministic substring matching via `voice_eval/evaluator_rules.py`
- `claude`: semantic grading via Claude structured outputs in `voice_eval/evaluator_claude.py`; requires `ANTHROPIC_API_KEY`
- `ollama`: local LLM grading via `voice_eval/evaluator_llm.py`; requires Ollama running with `llama3.2` available

Example commands:

```bash
# Rules judge
poetry run voice-eval scenarios scenarios/ --judge rules

# Claude judge
poetry run voice-eval scenarios scenarios/ --judge claude

# Ollama judge
poetry run voice-eval scenarios scenarios/ --judge ollama

# Larger ASR model
poetry run voice-eval scenarios scenarios/ --model base
```

To prepare the Ollama judge:

```bash
ollama pull llama3.2
```

## Testing

```bash
poetry run pytest
poetry run pytest -v
```

The Claude evaluator tests are mocked, so they do not need a real API key.

## Project Layout

- `voice_eval/cli.py` exposes the `voice-eval` CLI entry point.
- `voice_eval/simulator.py` orchestrates the voice simulation loop and selects the evaluation judge.
- `voice_eval/tool_client.py` dispatches the project’s rule-based bot tools.
- `voice_eval/bot_tools.py` contains slot extraction, policy, and response templates.
- `voice_eval/scenario.py` loads YAML scenarios.
- `voice_eval/reporters/markdown.py` writes the Markdown report.
- `tests/` contains the pytest suite for the tool layer, evaluators, and scenario loader.

## Architecture

The bot pipeline is intentionally rule-based. There is no actual MCP server in the runtime path, and the project now uses plain tool-oriented names to reflect that honestly:

```text
YAML scenario
  -> TTS (pyttsx3)
  -> ASR (faster-whisper)
  -> bot tools (regex slot extraction, rule-based policy, template responses)
  -> judge (rules, Claude, or Ollama)
  -> markdown report
```

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

- `ANTHROPIC_API_KEY`: required for the Claude judge
- `OLLAMA_BASE_URL`: Ollama API URL, default `http://localhost:11434`
- `OLLAMA_MODEL`: Ollama model name, default `llama3.2`
- `DEFAULT_ASR_MODEL`: default ASR model size, default `tiny`
- `DEBUG_LLM_EVALUATION`: enable Ollama-evaluator debug logging, default `false`

## Extending the Bot

To add a new conversation flow, update `voice_eval/bot_tools.py` in three places:

1. Add regex patterns in `extract_slots_tool` for any new slots.
2. Add a goal branch in `policy_decision_tool`.
3. Add or adjust templates in `generate_response_tool`.

Then add a matching YAML scenario under `scenarios/`.
