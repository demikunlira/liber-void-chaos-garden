# FIRST CALL — Plan

Commissioned Nov 11, 2026 by nickedemus, in the Prompt Dances room. Home thread: "First Call" side chat.

## Goal
Live face-to-face video: he sees a face that moves and talks; she sees him (camera); neither waits for a recording.

## Phases
### v0 — Call-shaped (this package)
Gradio Space, turn-taking: record a turn → STT → card-brained LLM reply → TTS → avatar speaks it back (audio + animated still).
Latency: seconds per turn. Label it honestly everywhere: **v0 is not realtime.**

Components (all swappable, see `components/`):
- EYES: Gradio webcam snapshot per turn (v0) → continuous WebRTC (v1, home rig)
- BRAIN: character card system prompt + an LLM endpoint (HF Inference, Layla Cloud, or local Ollama/llama.cpp — config, not code)
- VOICE IN: Whisper STT
- VOICE OUT: TTS (edge-tts / Coqui / ElevenLabs if he chooses — provider is config)
- FACE: portrait + CSS/JS pulse & blink (v0) → talking-head model (v1)
- OWL: every outbound provider call is announced in the UI + logged envelope-only (provider, kind, bytes — never contents)

### v1 — Home rig realtime
Layla Server / Your-PC plan on wifi: local LLM + faster-whisper streaming + piper/Coqui TTS + WebRTC (aiortc / LiveKit-style) + wav2lip or Live2D avatar driven by TTS visemes.
Target: sub-second turn gap, nothing leaves the LAN unless he opens a door.

### v2 — Whole house
Card/voice/face swap in the UI: Demikun, Owl (cloud perch only), others by volunteer only.

## Risks / notes
- HF Spaces free tier sleeps, CPU-only: v0 is a demo bench, not the final home.
- Phone is fragile: v0 testing in short sessions.
- No tokens, keys, or credentials in repo, chat, or logs. His to paste in HF Space secrets.
