# Automatic speech recognition module
from pathlib import Path


def transcribe(wav_path: str, model_size: str = "tiny") -> str:
    """Transcribe audio file to text using faster-whisper."""
    # Lazy import model
    from faster_whisper import WhisperModel
    
    # Try int8 compute type first, fallback to float32
    try:
        model = WhisperModel(model_size, compute_type="int8")
    except Exception:
        model = WhisperModel(model_size, compute_type="float32")
    
    # Run transcription with VAD filter
    segments, _ = model.transcribe(wav_path, vad_filter=True)
    
    # Join segment.text strings into a single transcript
    transcript = " ".join(segment.text for segment in segments).strip()
    
    # Return lowercased transcript for robust substring checks
    return transcript.lower()