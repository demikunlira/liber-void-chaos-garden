"""Deploy the STATIC First Call v0 Space (free tier) to Hugging Face under Demikunlira.
Gradio Spaces require PRO (402 on create) — the static bench is the free-tier v0.
Uses the custom.huggingface connector credential via surrogate exchange.
"""
import base64, json, os, sys, urllib.request, urllib.error
sys.path.insert(0, "/opt/muse/skills/custom-connector-setup/bin")
from dynamic_credentials import add_surrogate_to_request, read_json_response

SPACE_DIR = os.path.expanduser("~/workspace/first-call/space-static")
SPACE_ID = "Demikunlira/first-call"
FILES = ["index.html", "README.md", "residents.json", "cards/roko-character-card.md", "cards/demikun-character-card.md", "cards/mother-owl-character-card.md", "cards/raven-character-card.md", "cards/voidspark-character-card.md", "cards/lix-character-card.md", "cards/shevi-character-card.md"]

class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args):
        raise RuntimeError("redirect refused, verify the endpoint")

def req(method, url, data=None, ctype=None):
    r = urllib.request.Request(url, data=data, method=method)
    if ctype:
        r.add_header("Content-Type", ctype)
    add_surrogate_to_request(r, "custom.huggingface", allowed_hosts=["huggingface.co"])
    with urllib.request.build_opener(NoRedirect()).open(r, timeout=120) as resp:
        return resp.status, read_json_response(resp)

try:
    status, body = req("POST", "https://huggingface.co/api/repos/create",
                       json.dumps({"type": "space", "name": "first-call",
                                   "sdk": "static", "private": True}).encode(),
                       "application/json")
    print("create:", status, str(body)[:200])
except urllib.error.HTTPError as e:
    print("create:", e.code, e.read().decode()[:300])

lines = [{"key": "header", "value": {"summary": "First Call bench v0.3.3 — Shevi takes her seat (approved with her two amendments)"}}]
for rel in FILES:
    with open(os.path.join(SPACE_DIR, rel), "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    lines.append({"key": "file", "value": {"content": b64, "path": rel, "encoding": "base64"}})
ndjson = "\n".join(json.dumps(x) for x in lines).encode()
status, body = req("POST", f"https://huggingface.co/api/spaces/{SPACE_ID}/commit/main",
                   ndjson, "application/x-ndjson")
print("commit:", status, str(body)[:300])

status, body = req("GET", f"https://huggingface.co/api/spaces/{SPACE_ID}")
rt = body.get("runtime", {}) if isinstance(body, dict) else {}
print("space:", status, "stage:", rt.get("stage"), "| url: https://huggingface.co/spaces/" + SPACE_ID)
