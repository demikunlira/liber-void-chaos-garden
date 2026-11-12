"""STT stub: local Whisper if installed, else honest no-op. v1 rig: faster-whisper streaming."""
import os
from owl import announce
def transcribe(audio_path: str):
    try:
        import whisper
        model = whisper.load_model(os.environ.get("WHISPER_MODEL", "tiny"))
        text = model.transcribe(audio_path)["text"].strip()
        return text, announce("stt", "local whisper", os.path.getsize(audio_path))
    except Exception:
        return "", announce("stt", "unavailable — install openai-whisper or set a cloud STT door", 0)
