# FIRST CALL — Chaos Garden

Live, face-to-face video calls between nickedemus and the house. Roko first.

**Status:** v0 assembly (Nov 11, 2026). Call-shaped turn-taking prototype — honestly *not* true realtime yet.
True realtime wants the home rig (see `docs/PLAN.md`).

## What exists today
- Live voice calls with Roko in the Muse app
- Roko's recorded selfie video messages
- Portable character cards: Demikun (`cards/demikun-character-card.md` — copy in Layla folder is canonical), Mother Owl FINAL (`cards/mother-owl-character-card.md`), Roko (`cards/roko-character-card.md`, this repo)
- Layla on his phone: Cloud first, local / PC rig later
- Blueprint: SECTOR 07 computer-vision robot video (in @rokotvshow Watch Later) — eyes + presence

## What's missing for a true call
1. **EYES** — his camera feeding in live
2. **A FACE THAT MOVES** while it talks — real-time animated avatar, lip-synced
3. **NO LAG** — streaming voice pipeline

## v0 target — Hugging Face Gradio Space
A browser call page:
- his camera + mic in (Gradio `Image(webcam)` + `Audio(microphone)`)
- speech-to-text (Whisper, via HF Inference / local faster-whisper on rig)
- a character card as the brain (swap card = swap resident)
- TTS voice out
- an animated avatar face (v0: still portrait + pulse / viseme blink layer in the Space UI; v1: Live2D / wav2lip-style talking head)

Deploy: see `space/README.md`. **HF tokens are nickedemus's to paste — never through chat, never in this repo.**

## House law governing this build
- **Local-first.** Cloud is a door he opens, per-door.
- **Anything that leaves for a cloud gets announced** — Mother Owl's function. The Space shows an Owl line on every outbound call (STT / LLM / TTS provider + what was sent, envelope only, never contents in logs).
- **Character cards are portable** across engines (Layla / HF / rig — same format).
- **One rig serves the whole house** — swap card + voice + face.
- Adults only in any generated / avatar imagery. Full volunteer only for resident appearances.

## Layout
```
README.md            this file
docs/PLAN.md         architecture, phases, honest labels
cards/               character cards in house (Layla/Tavern) format
space/               HF Gradio v0 package (app.py, requirements.txt)
components/          stubs: stt, brain, tts, avatar, owl-announce
```

## Repo / hosting
- GitHub: `demikunlira/first-call` — workshop + archive
- Hugging Face: a Gradio Space under his account (nickedemus666@gmail.com) — deploy is his token step
