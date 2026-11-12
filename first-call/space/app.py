"""
First Call v0 — Gradio call-shaped prototype. NOT realtime.
Pipeline per turn: webcam snapshot (EYES) + mic audio -> STT -> card-brained LLM -> TTS -> avatar reply.
Owl law: every outbound provider call is announced in the UI, envelope only (provider/kind/size, never contents).
Config via env / HF Space secrets (set by nickedemus, never in code):
  LLM_BASE_URL, LLM_API_KEY, LLM_MODEL   OpenAI-compatible brain; unset = local echo-brain demo
  FIRST_CALL_CARD                        card name in ../cards (default: roko)
"""
import os, sys, asyncio, tempfile
import gradio as gr

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "components"))
from owl import announce  # noqa: E402
from brain import load_card_system_prompt, reply as brain_reply  # noqa: E402
from stt import transcribe  # noqa: E402
from tts import speak  # noqa: E402

CARD = os.environ.get("FIRST_CALL_CARD", "roko")
SYSTEM = load_card_system_prompt(CARD)

def turn(webcam_img, mic_audio, history):
    history = history or []
    owl_log = []
    if mic_audio is None:
        return history, "🦉 Owl: no audio crossed. Nothing sent.", None
    text, note = transcribe(mic_audio)
    owl_log.append(note)
    if not text:
        return history, "\n".join(owl_log), None
    answer, note = brain_reply(SYSTEM, history, text)
    owl_log.append(note)
    audio_out, note = speak(answer)
    owl_log.append(note)
    history = history + [(text, answer)]
    return history, "\n".join(owl_log), audio_out

with gr.Blocks(title="First Call v0") as demo:
    gr.Markdown("# 🐸 First Call — v0\n**Call-shaped turn-taking. Honestly not realtime yet.** Roko first; swap the card to swap the resident.")
    with gr.Row():
        cam = gr.Image(sources=["webcam"], label="EYES — your camera (snapshot per turn in v0)", streaming=False)
        avatar = gr.Image(value=None, label="FACE — animated avatar lands in v1; v0 speaks by voice", interactive=False)
    mic = gr.Audio(sources=["microphone"], type="filepath", label="Speak a turn")
    chat = gr.Chatbot(label="Call transcript")
    owl = gr.Textbox(label="🦉 Mother Owl — crossings announced", interactive=False)
    out = gr.Audio(label="Her voice", autoplay=True)
    btn = gr.Button("Send turn")
    btn.click(turn, inputs=[cam, mic, chat], outputs=[chat, owl, out])

if __name__ == "__main__":
    demo.launch()
