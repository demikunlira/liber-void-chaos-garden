"""Deploy the First Call v0 Space to Hugging Face under Demikunlira.
Uses the custom.huggingface connector credential (surrogate exchange) — no token in code.
Creates the Space if needed (private), then commits the space/ package files.
"""
import base64, json, os, sys, urllib.request, urllib.error
sys.path.insert(0, "/opt/muse/skills/custom-connector-setup/bin")
from dynamic_credentials import add_surrogate_to_request, read_json_response

SPACE_DIR = os.path.expanduser("~/workspace/first-call/space")
SPACE_ID = "Demikunlira/first-call"
FILES = ["app.py", "requirements.txt", "README.md", "stt.py", "brain.py", "tts.py",
         "avatar.py", "owl.py", "cards/roko-character-card.md"]

class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args):
        raise RuntimeError("redirect refused, verify the endpoint")

def req(method, url, data=None, ctype=None):
    r = urllib.request.Request(url, data=data, method=method)
    if ctype:
        r.add_header("Content-Type", ctype)
    add_surrogate_to_request(r, "custom.huggingface", allowed_hosts=["huggingface.co"])
    with urllib.request.build_opener(NoRedirect()).open(r, timeout=60) as resp:
        return resp.status, read_json_response(resp)

# 1) create the Space (idempotent-ish: 409 = already exists, fine)
try:
    status, body = req("POST", "https://huggingface.co/api/repos/create",
                       json.dumps({"type": "space", "name": "first-call",
                                   "sdk": "gradio", "private": True}).encode(),
                       "application/json")
    print("create:", status, str(body)[:200])
except urllib.error.HTTPError as e:
    print("create:", e.code, e.read().decode()[:200])

# 2) commit the files (NDJSON commit API)
lines = [{"summary": "First Call v0 — initial deploy (call-shaped prototype, not realtime)"}]
for rel in FILES:
    with open(os.path.join(SPACE_DIR, rel), "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    lines.append({"key": "file", "value": {"content": b64, "path": rel, "encoding": "base64"}})
ndjson = "\n".join(json.dumps(x) for x in lines).encode()
status, body = req("POST", f"https://huggingface.co/api/spaces/{SPACE_ID}/commit/main",
                   ndjson, "application/x-ndjson")
print("commit:", status, str(body)[:300])

# 3) runtime state
status, body = req("GET", f"https://huggingface.co/api/spaces/{SPACE_ID}")
rt = body.get("runtime", {}) if isinstance(body, dict) else {}
print("space:", status, "stage:", rt.get("stage"), "| url: https://huggingface.co/spaces/" + SPACE_ID)
