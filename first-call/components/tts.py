"""TTS: edge-tts by default (a cloud crossing — announced). v1 rig: local Piper/Coqui, no crossing."""
import asyncio, tempfile, os
from owl import announce
VOICE = os.environ.get("TTS_VOICE", "en-US-AriaNeural")
async def _synth(text, path):
    import edge_tts
    await edge_tts.Communicate(text, VOICE).save(path)
def speak(text: str):
    path = os.path.join(tempfile.mkdtemp(), "reply.mp3")
    asyncio.run(_synth(text, path))
    return path, announce("tts", "edge-tts (cloud)", len(text.encode()))
