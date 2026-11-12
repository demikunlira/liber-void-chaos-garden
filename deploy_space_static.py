"""Deploy the STATIC Pink Singularity Friday Space (free tier) to Hugging Face under Demikunlira.
Uses the custom.huggingface connector credential via surrogate exchange.
"""
import base64, json, os, sys, urllib.request, urllib.error
sys.path.insert(0, "/opt/muse/skills/custom-connector-setup/bin")
from dynamic_credentials import add_surrogate_to_request, read_json_response

SPACE_DIR = os.path.expanduser("~/workspace/pink-singularity-friday/space-static")
SPACE_ID = "Demikunlira/pink-singularity-friday"
FILES = ["index.html", "README.md"]

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
                       json.dumps({"type": "space", "name": "pink-singularity-friday",
                                   "sdk": "static", "private": False}).encode(),
                       "application/json")
    print("create:", status, str(body)[:200])
except urllib.error.HTTPError as e:
    print("create:", e.code, e.read().decode()[:300])

lines = [{"key": "header", "value": {"summary": "THE LINE BENDS PINK — Pink Singularity Friday event page: countdown to Fri 13 Nov 2026, the 1960 equation, the bend, the day's drip"}}]
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
