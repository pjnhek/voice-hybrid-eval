# Text-to-speech synthesis module
import pyttsx3
from pathlib import Path


def synthesize(text: str, out_wav: str) -> None:
    """Synthesize text to speech and save as WAV file."""
    # Ensure parent directories exist
    Path(out_wav).parent.mkdir(parents=True, exist_ok=True)
    
    # Initialize engine once per call (simple and reliable)
    engine = pyttsx3.init()
    engine.save_to_file(text, out_wav)
    engine.runAndWait()


