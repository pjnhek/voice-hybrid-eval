from pathlib import Path

from gtts import gTTS


def synthesize(text: str, out_wav: str) -> None:
    """Synthesize text to speech and save as an audio file."""
    Path(out_wav).parent.mkdir(parents=True, exist_ok=True)
    tts = gTTS(text=text, lang="en")
    # gTTS outputs MP3 natively. faster-whisper can decode it via ffmpeg even
    # when callers pass a .wav path.
    tts.save(out_wav)

