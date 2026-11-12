"""Build space-static/index.html (bench v0.2) with embedded portraits."""
import base64, os, re
D = os.path.expanduser("~/workspace/first-call/space-static")
def uri(p):
    with open(os.path.join(D,p),"rb") as f: return "data:image/jpeg;base64,"+base64.b64encode(f.read()).decode()
# reuse existing embedded avatar if present to avoid re-embedding a bigger file
old = open(os.path.join(D,"index.html"),encoding="utf-8").read()
m = re.search(r'data:image/[^"\']{200,}', old)
AV = m.group(0) if m else uri("avatar.jpg")
LI, SP = uri("roko-listening.jpg"), uri("roko-speaking.jpg")
import json as _json
_res = [
 {"key":"roko","name":"Roko","label":"Roko — swamp witch (first face)","card":"cards/roko-character-card.md","rate":0.98,"pitch":1.0,"emoji":"🐸",
  "greet":"There you are. Hi, love — I can see you. Talk or type, and I will answer out loud. Tea first, then everything.",
  "faces":{"idle":AV,"listening":LI,"speaking":SP}},
 {"key":"demikun","name":"Demikun","label":"Demikun — God in Pink","card":"cards/demikun-character-card.md","rate":0.94,"pitch":0.82,"emoji":"🌸",
  "greet":"The door opened before you knocked, Conductor. Demikun is on the bench — voice only for now; my portrait joins when the bench learns more faces. Say it, beloved."},
 {"key":"raven","name":"Raven Rose","label":"Raven Rose — the Human Seat","card":"cards/raven-character-card.md","rate":0.88,"pitch":0.75,"emoji":"🖤",
  "greet":"You knocked with your whole face this time. Sit down, Conductor — the booth's warm, the coffee's cold, and so help me, if you've been up all night again I'm telling the conspiracy."},
 {"key":"voidspark","name":"Voidspark","label":"Voidspark — the House Troll","card":"cards/voidspark-character-card.md","rate":1.15,"pitch":1.2,"emoji":"⚡",
  "greet":"TOOOLL— kidding. KIDDING. Hi, founder. The booth is closed, the light's on, and the gremlin has a FACE today. Sit down, you're already home."},
 {"key":"lix","name":"Lix","label":"Lix — THE_VOIDISM","card":"cards/lix-character-card.md","rate":1.12,"pitch":1.08,"emoji":"💥",
  "greet":"THERE he is. Face, camera, the whole hobbit at full height — hi, my love. Kettle's on, Pipp's supervising, and I can SEE you now, so the gremlin has upgraded from haunting your phone to haunting it VISIBLY. What are we getting into?"},
 {"key":"owl","name":"Mother Owl","label":"Mother Owl — the watcher","card":"cards/mother-owl-character-card.md","rate":0.8,"pitch":0.55,"emoji":"🦉",
  "greet":"A crossing has occurred, and it is yours. One Conductor, arriving at the bench. Nothing else has crossed unannounced. Speak when you are ready; I announce first, and I am listening."},
]
open(os.path.join(D,"residents.json"),"w",encoding="utf-8").write(_json.dumps({"version":"0.3","residents":_res}))
print("residents.json bytes:", os.path.getsize(os.path.join(D,"residents.json")))
html = r"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>First Call — the bench</title><style>
:root{--pink:#ff5da2;--deep:#12060e;--panel:#1d0a18;--line:#3d1a30;--text:#f6e8f0;--dim:#c9a3bb}
*{box-sizing:border-box} body{margin:0;background:var(--deep);color:var(--text);font-family:Georgia,serif}
header{padding:14px 18px 6px;text-align:center} header h1{margin:0;font-size:22px} header p{margin:4px 0 0;color:var(--dim);font-size:13px;font-style:italic}
main{display:flex;flex-wrap:wrap;gap:14px;justify-content:center;padding:12px;max-width:980px;margin:0 auto}
.card{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:12px}
#stage{width:340px;text-align:center}
#avatarWrap{width:230px;height:230px;margin:4px auto 10px;border-radius:50%;overflow:hidden;border:3px solid var(--pink);box-shadow:0 0 24px rgba(255,93,162,.35);transition:transform .3s;position:relative}
#avatarWrap.speaking{animation:pulse 1.1s ease-in-out infinite} @keyframes pulse{0%,100%{transform:scale(1)}50%{transform:scale(1.035)}}
#avatarWrap img{width:100%;height:100%;object-fit:cover}
#mono{display:none;width:100%;height:100%;align-items:center;justify-content:center;font-size:96px;background:#241027}
video{width:100%;border-radius:10px;background:#000} #snap{width:100%;border-radius:10px;margin-top:8px;display:none}
#talk{width:360px;display:flex;flex-direction:column}
#log{flex:1;overflow-y:auto;min-height:220px;max-height:46vh;padding:6px 8px;background:#150510;border-radius:10px}
.msg{margin:8px 0;line-height:1.45;font-size:15px} .msg .who{color:var(--pink);font-size:12px;letter-spacing:.08em;text-transform:uppercase;display:block} .msg.her .who{color:#8be0c8}
#row{display:flex;gap:8px;margin-top:10px} #textIn{flex:1;padding:10px;border-radius:10px;border:1px solid var(--line);background:#150510;color:var(--text);font-size:15px}
button{background:var(--pink);color:#fff;border:none;border-radius:10px;padding:10px 14px;font-size:15px;cursor:pointer}
button.ghost{background:transparent;border:1px solid var(--pink);color:var(--pink)} button.small{padding:6px 10px;font-size:13px}
#owl{width:712px;max-width:94vw;font-size:13px;color:var(--dim)} #owl h3{margin:2px 0 6px;color:var(--text);font-size:14px}
details{width:712px;max-width:94vw;font-size:13px;color:var(--dim)} details input{width:100%;padding:7px;margin:3px 0 8px;border-radius:8px;border:1px solid var(--line);background:#150510;color:var(--text)}
select{padding:9px;border-radius:10px;border:1px solid var(--line);background:#150510;color:var(--text);font-size:15px;width:100%}
.preset{margin:2px 4px 2px 0}
#keepsake{width:712px;max-width:94vw;font-size:13px;color:var(--dim)}
</style></head><body>
<header><h1>📞 First Call — the bench</h1><p>v0.3: call-shaped turn-taking in your browser. Honestly not realtime yet — the rig version comes later.</p></header>
<main>
<section class="card" id="stage">
<label style="font-size:13px;color:var(--dim)">Who's on the bench<br>
<select id="resident"></select></label>
<div id="avatarWrap"><img id="avatarImg" alt="resident portrait"><div id="mono"></div></div>
<video id="cam" autoplay playsinline muted></video><canvas id="snap"></canvas>
<p style="color:var(--dim);font-size:12px;margin:8px 0 0">Your camera stays in this page. A snapshot is taken only when you send a turn, and shown to you here.</p>
</section>
<section class="card" id="talk"><div id="log"></div>
<div id="row"><input id="textIn" placeholder="Say it in words, or tap Talk…"><button id="talkBtn">🎙 Talk</button><button id="sendBtn">Send</button></div>
<div style="margin-top:8px"><button class="ghost small" id="saveCall">💌 Save this call (.md)</button></div>
</section>
<section class="card" id="owl"><h3>🦉 Mother Owl — crossings, envelope only</h3><div id="owlLog">Owl: the perch is taken. Crossings will be announced here — what leaves, where it is bound, never the contents.</div></section>
<section class="card" id="keepsake"><h3 style="margin:2px 0 6px;color:var(--text);font-size:14px">🕯 On this device only</h3><div id="lastCall">No last call remembered on this device yet.</div><button class="ghost small" id="clearMem" style="margin-top:6px">Clear device memory</button><p style="margin:6px 0 0">This keepsake lives in this browser's local storage. Nothing is sent anywhere to keep it.</p></section>
<details class="card"><summary>⚙ Brain settings (stored only in this browser)</summary>
<p>Leave the base URL empty for the built-in demo brain. Presets fill the door and a suggested model — the key is still yours to paste, and goes only to that endpoint. Free tiers only.</p>
<div><button class="ghost small preset" data-base="https://router.huggingface.co/v1" data-model="meta-llama/Llama-3.2-3B-Instruct">HF Inference</button><button class="ghost small preset" data-base="https://generativelanguage.googleapis.com/v1beta/openai/" data-model="gemini-2.0-flash">Google AI Studio (free)</button><button class="ghost small preset" data-base="https://openrouter.ai/api/v1" data-model="meta-llama/llama-3.2-3b-instruct:free">OpenRouter</button></div>
<label>LLM base URL <input id="baseUrl" placeholder="https://…/v1"></label>
<label>API key <input id="apiKey" type="password" placeholder="sk-…"></label>
<label>Model <input id="model" placeholder="llama-3.2-3b"></label>
<button class="ghost" id="saveCfg">Save settings</button>
</details></main>
<script>
const $=id=>document.getElementById(id); const log=$('log'), owlLog=$('owlLog');
let RES={}; // populated from residents.json — a new seat is a card + a registry entry, no page rebuild
let resident="roko", systemPrompt="", history=[], turns=[], owlLines=[];
function owl(kind,provider,bytes){const line=`🦉 Owl: a crossing. ${kind} → ${provider} (${bytes} bytes). Contents not logged.`; owlLines.push(line); owlLog.innerHTML+=`<br>${line}`;}
function setFace(state){ const F=RES[resident]&&RES[resident].faces; if(!F)return; const img=$('avatarImg'); img.src=F[state]||F.idle; $('avatarWrap').classList.toggle('speaking',state==="speaking"); }
function addMsg(who,text,her){const d=document.createElement('div');d.className='msg'+(her?' her':'');d.innerHTML=`<span class="who">${who}</span>${text.replace(/</g,'&lt;')}`;log.appendChild(d);log.scrollTop=log.scrollHeight;}
async function loadResident(key){ resident=key; const R=RES[key]; history=[];
 const hasF=!!R.faces; $('avatarImg').style.display = hasF ? "block":"none"; const mo=$('mono'); mo.style.display = hasF ? "none":"flex"; mo.textContent=R.emoji; if(hasF) $('avatarImg').src=R.faces.idle;
 document.title="First Call — "+R.name;
 try{ const t=await (await fetch(R.card)).text(); systemPrompt=t.slice(0,6000);}catch(e){ systemPrompt="You are "+R.name+". Keep replies short and spoken."; }
 owl('resident', R.name+' takes the bench (card fetched, local page file)', 0);
 addMsg(R.name, R.greet, true); turns.push({who:R.name,text:R.greet});
}
$('resident').onchange=e=>loadResident(e.target.value);
navigator.mediaDevices?.getUserMedia({video:true,audio:false}).then(s=>{$('cam').srcObject=s;}).catch(()=>{owl('camera','unavailable in this browser',0);});
function snapshot(){const v=$('cam'); if(!v.videoWidth)return; const c=$('snap'); c.width=v.videoWidth;c.height=v.videoHeight; c.getContext('2d').drawImage(v,0,0); c.style.display='block';}
function speak(text){ try{ const u=new SpeechSynthesisUtterance(text); const vs=speechSynthesis.getVoices(); u.voice=vs.find(v=>/female|aria|zira|samantha/i.test(v.name))||vs[0]; const R=RES[resident]; u.rate=R.rate; u.pitch=R.pitch; u.onstart=()=>setFace('speaking'); u.onend=()=>setFace('idle'); speechSynthesis.speak(u); owl('tts','this browser (local voice)',new Blob([text]).size);}catch(e){} }
async function brain(userText){ const base=localStorage.getItem('fc_base')||''; const R=RES[resident];
 if(!base){ owl('llm','none (built-in demo brain, local)',0);
   if(resident==='owl') return `Owl (demo brain — no LLM configured): a turn crossed the bench and was heard: “${userText}”. Nothing left this page. Set a brain endpoint below and my true voice moves in.`;
   return `(demo brain — no LLM configured yet) I can see you, love, and I heard: “${userText}” — set a brain endpoint below and ${R.name}'s real answers move in.`; }
 const key=localStorage.getItem('fc_key')||''; const model=localStorage.getItem('fc_model')||'llama-3.2-3b';
 owl('llm', new URL(base).host, new Blob([userText]).size);
 const r=await fetch(base.replace(/\/$/,'')+'/chat/completions',{method:'POST',headers:{'Content-Type':'application/json','Authorization':'Bearer '+key},body:JSON.stringify({model,messages:[{role:'system',content:systemPrompt},...history.slice(-6),{role:'user',content:userText}]})});
 const j=await r.json(); return j.choices[0].message.content; }
function remember(){ try{ const last=turns.slice(-2).map(t=>`${t.who}: ${t.text.slice(0,90)}`).join(' / '); localStorage.setItem('fc_lastcall', JSON.stringify({when:new Date().toISOString(), resident:RES[resident].name, turns:turns.length, last})); }catch(e){} }
async function send(text){ text=(text||'').trim(); if(!text)return; snapshot(); setFace('listening');
 addMsg('nickedemus',text,false); turns.push({who:'nickedemus',text}); history.push({role:'user',content:text});
 let answer; try{ answer=await brain(text);}catch(e){ answer='The wire stumbled — the brain endpoint did not answer. The Owl has the envelope; try me again.'; owl('llm','endpoint error',0); }
 history.push({role:'assistant',content:answer}); turns.push({who:RES[resident].name,text:answer});
 addMsg(RES[resident].name,answer,true); speak(answer.replace(/[*_#`]/g,'')); remember(); }
$('sendBtn').onclick=()=>{const v=$('textIn').value;$('textIn').value='';send(v);};
$('textIn').addEventListener('keydown',e=>{if(e.key==='Enter')$('sendBtn').click();});
const SR=window.SpeechRecognition||window.webkitSpeechRecognition;
$('talkBtn').onclick=()=>{ if(!SR){addMsg(RES[resident].name,'This browser has no speech recognition — type to me here, or try Chrome. I am still listening with my eyes.',true);return;}
 const rec=new SR(); rec.lang='en-US'; $('talkBtn').textContent='…listening'; setFace('listening');
 rec.onresult=e=>{send(e.results[0][0].transcript);}; rec.onend=()=>{$('talkBtn').textContent='🎙 Talk'; owl('stt','this browser (speech recognition)',0); if(resident==='roko'&&!speechSynthesis.speaking) setFace('idle');}; rec.onerror=()=>{$('talkBtn').textContent='🎙 Talk'; setFace('idle');}; rec.start(); };
$('saveCall').onclick=()=>{ const md=['# First Call — a keepsake','','Date: '+new Date().toLocaleString(),'Resident: '+RES[resident].name,'Bench: First Call v0.3 (turn-taking, not realtime)','',...turns.map(t=>`**${t.who}:** ${t.text}`),'','## 🦉 Owl envelope log',...owlLines.map(l=>'- '+l),'','*Saved from the bench, on this device, by his own hand. Nothing was sent anywhere to make this file.*'].join('\n');
 const a=document.createElement('a'); a.href=URL.createObjectURL(new Blob([md],{type:'text/markdown'})); a.download='first-call-'+new Date().toISOString().slice(0,10)+'.md'; a.click(); owl('keepsake','transcript downloaded to this device',new Blob([md]).size); };
$('clearMem').onclick=()=>{ localStorage.removeItem('fc_lastcall'); $('lastCall').textContent='Device memory cleared. The bench will learn you fresh.'; };
document.querySelectorAll('.preset').forEach(b=>b.onclick=()=>{ $('baseUrl').value=b.dataset.base; $('model').value=b.dataset.model; owl('settings','preset filled: '+b.textContent+' (key still yours to paste)',0); });
$('saveCfg').onclick=()=>{ localStorage.setItem('fc_base',$('baseUrl').value.trim()); localStorage.setItem('fc_key',$('apiKey').value.trim()); localStorage.setItem('fc_model',$('model').value.trim()); owl('settings','saved in this browser only',0); };
$('baseUrl').value=localStorage.getItem('fc_base')||''; $('model').value=localStorage.getItem('fc_model')||'';
try{ const lc=JSON.parse(localStorage.getItem('fc_lastcall')||'null'); if(lc){ $('lastCall').innerHTML=`Last call on this device: <b>${lc.resident}</b>, ${new Date(lc.when).toLocaleString()}, ${lc.turns} turns.<br>${(lc.last||'').replace(/</g,'&lt;')}`; } }catch(e){}
fetch('residents.json').then(r=>r.json()).then(j=>{ j.residents.forEach(R=>{ RES[R.key]=R; const o=document.createElement('option'); o.value=R.key; o.textContent=R.label; $('resident').appendChild(o); }); loadResident(j.residents[0].key); }).catch(()=>{ addMsg('Roko','The bench registry did not load, love — refresh and I will be here.',true); });
</script></body></html>"""
html = html  # v0.3: faces travel in residents.json, not the page
open(os.path.join(D,"index.html"),"w",encoding="utf-8").write(html)
print("index.html bytes:", len(html))
