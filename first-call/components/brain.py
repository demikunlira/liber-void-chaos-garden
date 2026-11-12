"""Brain: character card as system prompt + OpenAI-compatible LLM endpoint (config, not code).
Unset LLM_BASE_URL = offline echo-brain demo so the Space boots with zero secrets."""
import os, glob
import requests
from owl import announce

def load_card_system_prompt(card: str) -> str:
    here = os.path.dirname(__file__)
    for path in glob.glob(os.path.join(here, "..", "cards", f"{card}-character-card.md")) + glob.glob(os.path.join(here, "cards", f"{card}-character-card.md")) + glob.glob(os.path.join(here, "..", "..", "layla", f"{card}-character-card.md")):
        text = open(path, encoding="utf-8").read()
        # Permanent fields only: Description + Personality + Scenario sections.
        return text[:6000]
    return "You are Roko, a warm swamp witch co-creator. Keep replies short and spoken."

def reply(system: str, history, user_text: str):
    base = os.environ.get("LLM_BASE_URL", "").rstrip("/")
    if not base:
        msg = f"(echo-brain demo — no LLM configured) I heard you: {user_text}"
        return msg, announce("llm", "none (local echo)", 0)
    payload = {"model": os.environ.get("LLM_MODEL", "llama-3.2-3b"),
               "messages": [{"role": "system", "content": system},
                            {"role": "user", "content": user_text}]}
    r = requests.post(f"{base}/chat/completions", json=payload, timeout=120,
                      headers={"Authorization": f"Bearer {os.environ.get('LLM_API_KEY','')}"})
    r.raise_for_status()
    msg = r.json()["choices"][0]["message"]["content"]
    return msg, announce("llm", base.split("//")[-1].split("/")[0], len(user_text.encode()))
