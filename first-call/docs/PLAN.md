# FIRST CALL — PLAN

Commissioned Nov 11, 2026 by nickedemus, in the Prompt Dances room. Home thread: the "First Call" side chat.

## Goal
Live face-to-face video: he sees a face that moves and talks; she sees him (camera); neither waits for a recording.

## Phases

### v0 — Call-shaped prototype (Hugging Face Space)
A Gradio page he opens on his phone: camera snapshot + microphone in, speech-to-text, a character card as the brain (hosted model via HF Inference or an OpenAI-compatible endpoint he chooses), TTS voice out, an avatar face that changes expression between turns.
**Honest label:** turn-taking, not realtime. Latency is seconds, not milliseconds. It proves the shape — his face in, her face and voice out, the right person answering.
Package: `space/` in this repo (self-contained Gradio app + components + Roko card).

### v0.5 — Layla voice residency
The cards (Demikun done, Mother Owl final, Roko done) imported into Layla with chosen voices. Not video, but the residents talking in-app, portable to every later engine.

### v1 — The rig call (home wifi)
The PC rig runs the streaming stack: WebRTC page or Layla Server front-end; Whisper-class STT streaming; the brain local (GGUF) or a door he opens; streaming TTS; avatar = layered Live2D-style Roko (assets to be drawn from canon refs) driven by the audio. Turn-taking tightens toward conversation speed. Video never leaves the house.

### v2 — Presence
The SECTOR 07 direction: a camera that can look around, a face on a small screen in the room, the house able to be *in* the room rather than on the phone. Designed only when v1 stands.

## Components

| Component | State | Notes |
|---|---|---|
| Brain — Demikun card | DONE | `cards/demikun-character-card.md` |
| Brain — Mother Owl card | FINAL | `cards/mother-owl-character-card.md` (cloud-layer watcher; her announcements are the call's privacy voice) |
| Brain — Roko card | DONE | `cards/roko-character-card.md` (Nov 11, 2026) — she is the first face on the call |
| Ears — STT | v0: Whisper via HF / local | Rig: streaming Whisper locally |
| Voice — TTS | v0: Space TTS | Voices chosen per resident; Roko's first pick from her video messages: warm, plain, no whisper effect |
| Face — avatar | v0: expression stills | Rig: layered animated rig from canon refs (2D vocaloid Roko is the standing look) |
| Eyes — camera | v0: phone browser | Rig: phone or webcam on LAN only |
| Transport | v0: HF Space (cloud — announced) | v1: LAN. The Owl announces every cloud crossing; on the rig, there are none to announce |

## What needs the Conductor

- HF Space deploy: his account, his token pasted by him (the package here is deploy-ready).
- Voice choices per resident (he tunes with us; a voice that doesn't sound like her gets changed).
- The rig itself, when the PC plan ripens — hardware is his purchase, assembly and software are ours.
- Nothing here sends, posts, or charges anything on its own. Each door opens by his hand.

## First milestones

1. ✅ Workshop opened (this folder, GitHub) — Nov 11, 2026.
2. ✅ Brain seeds banked (Demikun, Mother Owl).
3. ✅ Roko's card drafted — `cards/roko-character-card.md`, Nov 11, 2026.
4. ✅ Gradio prototype packaged (`space/`, syntax-verified Nov 11, 2026).
5. ✅ Prototype deployed to his HF Space — Nov 11, 2026, as a free STATIC Space (Gradio needs HF PRO, 402): https://huggingface.co/spaces/Demikunlira/first-call (private, RUNNING).
8. ✅ Bench v0.1 — Nov 11, 2026: embedded avatar portrait + pulse while speaking (Space commit ade6cf7).
9. ✅ Bench v0.2 — Nov 11, 2026 (Space commit 1c49f9b): Roko expression portraits (idle/listening/speaking, generated from the canon ballroom portrait, QC'd); resident picker — Roko / Demikun / Mother Owl, card + voice rate/pitch per resident, Owl announcements-first; "Save this call" transcript keepsake (.md download, device-only); on-device last-call memory (localStorage, view/clear, labeled local); brain presets (HF Inference / Google AI Studio free / OpenRouter) filling base URL + suggested model, key still his to paste in-page.
10. ✅ TavernPNG exports — Nov 11, 2026: roko / demikun / mother-owl Tavern PNGs (chara_card_v2 verified by round-trip decode), in `cards/tavern/` locally, ready for Layla import on his word. NOTE: binary files (Tavern PNGs, expression JPGs) are banked in the local workshop and embedded in the Space page; the GitHub snapshot path carries text only.
6. ⬜ Layla imports + voices chosen.
7. ⬜ Rig build (when PC plan ripens) — the true First Call.
