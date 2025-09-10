# Voice Hybrid Evaluation System

A comprehensive testing framework for evaluating conversational AI bots through realistic voice interactions. The system simulates complete voice conversations by generating audio, performing speech recognition, processing user intents, and evaluating bot responses using both rule-based and LLM-based evaluation methods.

## Features

- **Complete Voice Pipeline**: Text-to-Speech → Speech Recognition → Intent Processing → Response Generation
- **Rule-Based Processing**: Reliable, deterministic conversation logic using MCP (Model Context Protocol) tools
- **Dual Evaluation Methods**: Both rule-based and LLM-based evaluation with automatic fallback
- **Multiple Scenarios**: YAML-based test case definitions for different conversation flows
- **Audio Generation**: Real audio files for manual review and testing
- **Comprehensive Reporting**: Detailed markdown reports with pass/fail analysis

## Installation

We recommend using **Conda** to create a reproducible environment:

```bash
# Create Conda environment from YAML file and Activate
conda env create -f environment.yml -n vheval 
conda activate vheval
```

### Optional: LLM Judge Setup

To use LLM-based evaluation, install Ollama and pull the Llama model:

```bash
# Install Ollama (visit https://ollama.ai/ for installation instructions)
# Then pull the Llama model
ollama pull llama3.2

# Verify installation
ollama list
```

The system will automatically fall back to rule-based evaluation if Ollama is not available.

### Optional: Environment Configuration

You can customize the system behavior using environment variables. Copy `env.example` to `.env` and modify as needed:

```bash
cp env.example .env
```

**Available Configuration:**
- `OLLAMA_BASE_URL`: Ollama API URL (default: `http://localhost:11434`)
- `OLLAMA_MODEL`: Llama model name (default: `llama3.2`)
- `DEFAULT_ASR_MODEL`: Default ASR model size (default: `tiny`)
- `DEBUG_LLM_EVALUATION`: Enable debug output for LLM evaluation (default: `false`)

## Quickstart

```bash
python run.py scenarios scenarios --report out/report.md --audio-dir out/audio
```

## Project Structure

```
voice-hybrid-eval/
├── scenarios/                    # YAML test case definitions
│   ├── billing_refund.yaml      # Refund request scenarios
│   ├── order_return.yaml        # Item return scenarios
│   ├── order_return_variations.yaml  # Return scenarios with different phrasings
│   └── shipping_address.yaml    # Address change scenarios
├── voice_eval/                  # Core system modules
│   ├── audio/                   # Audio processing
│   │   ├── tts.py              # Text-to-speech synthesis
│   │   └── asr.py              # Speech recognition
│   ├── reporters/              # Report generation
│   │   └── markdown.py         # Markdown report writer
│   ├── cli.py                  # Command line interface
│   ├── evaluator_rules.py      # Rule-based evaluation logic
│   ├── evaluator_llm.py        # LLM-based evaluation logic
│   ├── mcp_client.py           # MCP tool interface
│   ├── mcp_tools.py            # Core conversation logic
│   ├── scenario.py             # Scenario loading and parsing
│   └── simulator.py            # Main simulation engine
├── out/                        # Generated outputs
│   ├── audio/                  # Generated audio files (gitignored)
│   └── report.md              # Sample evaluation report
├── run.py                      # Main entry point
├── requirements.txt            # Python dependencies
├── environment.yml             # Conda environment specification
├── .gitignore                  # Git ignore patterns
└── env.example                 # Environment configuration template
```

## Core Components

### 1. Scenario Management (`scenario.py`)

Defines test cases and expected behaviors using YAML configuration:

```yaml
id: billing_refund_001
goal: "Request refund for duplicate charge"
steps:
  - user: "I was charged twice for $45 last Friday."
    bot_expect:
      contains_any: ["card", "last four digits", "help you with that"]
  - user: "Card ending 1234"
    bot_expect:
      contains_any: ["refund initiated", "processed your refund", "credit issued"]
```

**Key Classes:**
- `Step`: Single conversation turn with user input and expected bot response
- `Scenario`: Complete test case with goal, steps, and acceptance criteria

### 2. Audio Processing (`audio/`)

#### Text-to-Speech (`tts.py`)
- **Technology**: `pyttsx3` (cross-platform TTS)
- **Function**: `synthesize(text, out_wav)` - Converts text to WAV audio files
- **Features**: Offline processing, no external API dependencies

#### Speech Recognition (`asr.py`)
- **Technology**: `faster-whisper` (OpenAI Whisper implementation)
- **Function**: `transcribe(wav_path, model_size)` - Converts audio to text
- **Features**: 
  - Multiple model sizes (tiny, base, small, medium, large)
  - Voice Activity Detection (VAD) filtering
  - Automatic fallback from int8 to float32 compute types
  - Returns lowercased transcript for robust matching

### 3. MCP Tools (`mcp_tools.py`)

Core conversation processing logic using rule-based approaches:

#### `extract_slots_tool(user_input, current_slots)`
- **Purpose**: Extract structured information from user speech
- **Extracts**:
  - Order numbers (handles commas: "12,345" → "12345")
  - Card information (last 4 digits)
- **Patterns**: Multiple regex patterns for robust extraction
- **Returns**: `ToolResult` with extracted slots

#### `policy_decision_tool(goal, user_input, available_slots)`
- **Purpose**: Determine bot's next action based on context
- **Actions**:
  - `ASK_ORDER_NUMBER`: Request order information
  - `ASK_CARD_INFO`: Request card information
  - `CONFIRM_RETURN`: Process return request
  - `CONFIRM_ADDRESS_CHANGE`: Process address change
  - `PROCESS_REFUND`: Process refund request
  - `ASK_CLARIFY`: Request clarification

#### `generate_response_tool(action, slots)`
- **Purpose**: Generate natural language responses
- **Templates**: Pre-defined response templates with slot substitution
- **Context**: Uses extracted information for personalized responses

### 4. MCP Client (`mcp_client.py`)

Interface layer for calling MCP tools:
- Tool registry and routing
- Error handling and fallbacks
- Consistent `ToolResult` interface

### 5. Simulation Engine (`simulator.py`)

Orchestrates the complete voice interaction loop:

**Process Flow:**
1. **Audio Generation**: Convert user text to speech using TTS
2. **Speech Recognition**: Transcribe user audio using ASR
3. **Slot Extraction**: Extract structured information from transcript
4. **Policy Decision**: Determine appropriate bot action
5. **Response Generation**: Create bot response text
6. **Bot Audio**: Convert bot response to speech
7. **Evaluation**: Check if bot response meets expectations
8. **Transcript Recording**: Store complete interaction data

**Key Features:**
- Conversation state management (slots persist across turns)
- Error handling with fallback responses
- Support for multiple ASR model sizes

### 6. Evaluation System

Both evaluation methods follow identical logic and produce consistent results:

#### Rule-Based Evaluation (`evaluator_rules.py`)
Rule-based evaluation for reliable, deterministic testing:

**Function**: `check_bot_expect_enhanced(bot_text, expect)`
- **Features**:
  - `contains`: Single substring matching
  - `contains_any`: Multiple substring matching (OR logic)
  - Case-insensitive matching
  - Robust and deterministic

#### LLM-Based Evaluation (`evaluator_llm.py`)
AI-powered evaluation using Ollama with Llama for more flexible judgment:

**Function**: `check_bot_expect_llm(bot_text, expect)`
- **Features**:
  - Uses Ollama API with Llama model
  - Follows the same rules as rule-based evaluation
  - Automatic fallback to rule-based evaluation if Ollama unavailable
  - JSON-structured responses for reliability
  - Same evaluation criteria: `contains` and `contains_any`
  - Debug output shows evaluation reasoning
  - Robust JSON parsing with fallback extraction

**Note**: Both evaluators produce identical results for the same inputs, ensuring consistency regardless of the chosen evaluation method.

### 7. Reporting System (`reporters/markdown.py`)

Generates comprehensive test reports with:
- Summary table with pass/fail status
- Detailed turn-by-turn analysis
- Audio file links for manual review
- Expected vs actual response comparison
- Pass/fail indicators for each step

### 8. Command Line Interface (`cli.py`)

User interface for running evaluations:

```bash
python run.py scenarios <scenarios_dir> [options]
```

**Options:**
- `--report`: Output report path (default: `out/report.md`)
- `--audio-dir`: Audio output directory (default: `out/audio`)
- `--model`: ASR model size (default: `tiny`)
- `--judge`: Evaluation method - `rules` (default) or `llm`

## Usage Examples

### Running All Scenarios
```bash
python run.py scenarios scenarios/
```

### Running with Different ASR Model
```bash
python run.py scenarios scenarios/ --model base
```

### Using LLM Judge
```bash
# Using LLM evaluation (requires Ollama with Llama)
python run.py scenarios scenarios/ --judge llm

# Using LLM with different model
python run.py scenarios scenarios/ --judge llm --model base
```

### Custom Output Location
```bash
python run.py scenarios scenarios/ --report custom/report.md --audio-dir custom/audio/
```

## Dependencies

### Core Libraries
- `faster-whisper==1.0.3`: Speech recognition
- `pyttsx3==2.90`: Text-to-speech synthesis
- `typer==0.12.5`: Command line interface
- `pyyaml==6.0.2`: Scenario file parsing
- `rich==13.9.2`: Terminal output formatting
- `pydub==0.25.1`: Audio processing
- `requests==2.31.0`: HTTP requests (for LLM evaluation)

### Optional Dependencies
- `ollama`: For LLM-based evaluation (install from https://ollama.ai/)
- `llama3.2`: Llama model for evaluation (install with `ollama pull llama3.2`)

### System Dependencies (via Conda)
- `ffmpeg`: Audio processing
- `av`: Python audio/video library

## Performance Considerations

### ASR Model Sizes
- **tiny**: Fastest, least accurate (~39 MB)
- **base**: Balanced speed/accuracy (~74 MB)
- **small**: Better accuracy (~244 MB)
- **medium**: High accuracy (~769 MB)
- **large**: Best accuracy (~1550 MB)

### Optimization Strategies
- Lazy model loading
- Audio file caching
- Batch processing
- Rule-based processing for reliability
- LLM evaluation with automatic fallback
- Debug output only when needed (can be disabled)

## Scenario Format

Scenarios are defined in YAML files with the following structure:

```yaml
id: unique_scenario_id
goal: "Primary user intent description"
steps:
  - user: "What the user will say"
    bot_expect:
      contains_any: ["expected", "phrases", "in response"]
  - user: "Next user input"
    bot_expect:
      contains: "single expected phrase"
acceptance:
  # Overall success criteria (optional)
```

## Adding New Scenarios

1. Create a new YAML file in the `scenarios/` directory
2. Define the scenario with appropriate steps and expectations
3. Run the evaluation: `python run.py scenarios scenarios/`
4. Check the generated report in `out/report.md`

## Output Files

- **Report**: Markdown file with detailed evaluation results (sample included in `out/report.md`)
- **Audio**: WAV files for each conversation turn (user and bot) - generated in `out/audio/`
- **Transcripts**: Complete conversation logs with ASR results

## Troubleshooting

### Common Issues
1. **ASR Transcription Errors**: Try different model sizes or check audio quality
2. **TTS Issues**: Ensure pyttsx3 is properly installed
3. **Import Errors**: Verify all dependencies are installed via conda
4. **LLM Evaluation Issues**: 
   - Ensure Ollama is running (`ollama serve`)
   - Verify Llama model is installed (`ollama list`)
   - Check Ollama API is accessible (`curl http://localhost:11434/api/tags`)
   - System automatically falls back to rule-based evaluation if LLM fails
   - Check environment configuration in `.env` file if using custom settings

### Debug Mode
The system includes debug output for troubleshooting:
- Slot extraction results
- Policy decisions
- Response generation
- Evaluation results (both rule-based and LLM)
- LLM evaluation reasoning and fallback behavior
