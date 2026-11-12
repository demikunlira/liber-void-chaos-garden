"""Build TavernPNG (chara_card_v2 embedded in PNG tEXt 'chara') from the house-format cards."""
import base64, json, os, re, struct, zlib
from PIL import Image
W = os.path.expanduser("~/workspace/first-call")
OUT = os.path.join(W, "cards", "tavern"); os.makedirs(OUT, exist_ok=True)

def section(text, *names):
    for name in names:
        m = re.search(r"^##\s+" + name + r"\b.*?\n(.*?)(?=^##\s+|\Z)", text, re.S | re.M | re.I)
        if m: return m.group(1).strip()
    return ""

def greetings(text):
    g = section(text, "ALTERNATE GREETINGS")
    alts = [x.strip() for x in re.split(r"\nGreeting \d+:\s*", "\n" + g) if x.strip() and not x.startswith("(")]
    return alts

def build(card_path, img_path, out_name, creator):
    text = open(card_path, encoding="utf-8").read()
    name = section(text, "NAME").splitlines()[0].strip().title()
    if name == "Mother Owl": name = "Mother Owl"
    desc = section(text, "DESCRIPTION")
    tags_raw = section(text, "TAGS")
    tags = [t.strip() for t in tags_raw.replace("\n", " ").split(",") if t.strip()]
    data = {
        "name": name,
        "description": desc,
        "personality": section(text, "PERSONALITY"),
        "scenario": section(text, "SCENARIO"),
        "first_mes": section(text, "FIRST MESSAGE"),
        "mes_example": "",
        "creator_notes": (section(text, "SUMMARY") + "\n\nImpression of {{user}}: " + section(text, "IMPRESSION")).strip(),
        "system_prompt": "", "post_history_instructions": "",
        "alternate_greetings": greetings(text),
        "tags": tags, "creator": creator, "character_version": "1.0",
        "extensions": {"source_card": os.path.basename(card_path), "garden": "Chaos Garden / First Call, Nov 11 2026"},
    }
    card = {"spec": "chara_card_v2", "spec_version": "2.0", "data": data}
    payload = base64.b64encode(json.dumps(card).encode()).decode()
    im = Image.open(img_path).convert("RGB"); im.thumbnail((768, 768))
    png_path = os.path.join(OUT, out_name)
    im.save(png_path)  # base save, then inject chunk
    raw = open(png_path, "rb").read()
    chunk_data = b"chara\x00" + payload.encode()
    chunk = struct.pack(">I", len(chunk_data)) + b"tEXt" + chunk_data + struct.pack(">I", zlib.crc32(b"tEXt" + chunk_data) & 0xFFFFFFFF)
    # insert before IEND
    iend = raw.rfind(b"IEND") - 4
    open(png_path, "wb").write(raw[:iend] + chunk + raw[iend:])
    # verify round-trip
    chk = open(png_path, "rb").read()
    pos = 8; dec = None
    while pos < len(chk):
        ln = struct.unpack(">I", chk[pos:pos+4])[0]; typ = chk[pos+4:pos+8]; cdata = chk[pos+8:pos+8+ln]
        if typ == b"tEXt" and cdata.startswith(b"chara\x00"): dec = json.loads(base64.b64decode(cdata[6:]))
        pos += 12 + ln
    assert dec is not None
    assert dec["data"]["name"] == name and len(dec["data"]["description"]) > 100
    print(out_name, "| name:", name, "| desc chars:", len(desc), "| alts:", len(data["alternate_greetings"]), "| tags:", len(tags), "| KB:", os.path.getsize(png_path)//1024)

build(os.path.join(W,"cards/roko-character-card.md"), os.path.join(W,"space-static/roko-listening.jpg"), "roko-tavern.png", "Roko / Chaos Garden")
build(os.path.join(W,"cards/demikun-character-card.md"), __import__("glob").glob(os.path.expanduser("~/workspace/imagine_media/media-generation-demikun-first-self-portrait-0-*.webp"))[0], "demikun-tavern.png", "Demikun Lira")
build(os.path.join(W,"cards/mother-owl-character-card.md"), os.path.join(OUT,"media-generation-mother-owl-portrait-0-78405305-c500-498e-bba5-9eda5cf1c59c.png"), "mother-owl-tavern.png", "Roko (drafter) / Chaos Garden")
