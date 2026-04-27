import os
import torch
import gradio as gr
from diffusers import LTXVideoPipeline, DPMSolverMultistepScheduler
from diffusers.utils import export_to_video
import tempfile
import imageio
import numpy as np

# --------------------------------------------------
# 🔱 SHIV AI VIDEO GENERATOR (PRO)
# 👤 OWNER: SHRI RAM NAG | 📺 CHANNEL: PAISAWALA20
# --------------------------------------------------

HTML_UI = """
<!DOCTYPE html>
<html lang="hi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Shiv AI Video Studio</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;700;800&family=DM+Sans:wght@300;400;500&display=swap');
*{box-sizing:border-box;margin:0;padding:0}
:root{
  --bg:#070a0f;--surface:#0d1117;--surface2:#111827;--border:#1e2d3d;
  --accent:#3b82f6;--accent2:#06b6d4;--text:#f0f4f8;--muted:#64748b;
  --success:#22c55e;
}
body{background:var(--bg);color:var(--text);font-family:'DM Sans',sans-serif;min-height:100vh}
.studio{max-width:480px;margin:0 auto;padding:0 0 60px}
.topbar{padding:16px 16px 0;display:flex;align-items:center;justify-content:space-between}
.logo{font-family:'Syne',sans-serif;font-weight:800;font-size:20px;letter-spacing:-0.5px}
.logo span{color:var(--accent)}
.badge{font-size:10px;background:#1e2d3d;color:var(--accent2);padding:3px 10px;border-radius:20px;border:1px solid #1e3a4a}
.hero{padding:22px 16px 14px}
.hero-title{font-family:'Syne',sans-serif;font-size:28px;font-weight:800;line-height:1.15;letter-spacing:-1px}
.hero-title em{font-style:normal;color:var(--accent)}
.hero-sub{font-size:12px;color:var(--muted);margin-top:6px}
.canvas-wrap{margin:0 16px;border-radius:14px;overflow:hidden;border:1px solid var(--border);background:var(--surface);position:relative;aspect-ratio:16/9}
#previewCanvas{width:100%;height:100%;display:block}
.overlay{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px;pointer-events:none}
.overlay.hidden{display:none}
.play-icon{width:52px;height:52px;border-radius:50%;border:2px solid rgba(255,255,255,0.15);display:flex;align-items:center;justify-content:center}
.overlay-label{font-size:12px;color:var(--muted)}
.status-bar{margin:10px 16px;background:var(--surface);border:1px solid var(--border);border-radius:10px;padding:10px 14px;display:flex;align-items:center;gap:8px;min-height:42px}
.dot{width:7px;height:7px;border-radius:50%;background:var(--muted);flex-shrink:0;transition:background 0.3s}
.dot.active{background:var(--accent);animation:pulse 1.5s infinite}
.dot.done{background:var(--success)}
.dot.error{background:#ef4444}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:0.4}}
#statusText{font-size:12px;color:var(--muted);flex:1}
.steps{margin:10px 16px;display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px}
.step{background:var(--surface);border:1px solid var(--border);border-radius:10px;padding:10px 8px;text-align:center;transition:all 0.3s}
.step.active{border-color:var(--accent);background:#0d1e38}
.step.done{border-color:var(--success);background:#0a1f14}
.step-num{font-size:10px;color:var(--muted);font-family:'Syne',sans-serif;font-weight:700;margin-bottom:3px}
.step-label{font-size:11px;color:var(--text);font-weight:500}
.step.done .step-label{color:var(--success)}
.step.active .step-num{color:var(--accent)}
.panel{margin:12px 16px;background:var(--surface);border:1px solid var(--border);border-radius:14px;overflow:hidden}
.panel-head{padding:12px 14px;border-bottom:1px solid var(--border);display:flex;align-items:center;justify-content:space-between}
.panel-title{font-size:13px;font-weight:500;display:flex;align-items:center;gap:6px}
.panel-body{padding:14px}
textarea{width:100%;background:#070a0f;border:1px solid var(--border);border-radius:10px;color:var(--text);font-family:'DM Sans',sans-serif;font-size:13px;padding:10px 12px;resize:none;outline:none;transition:border-color 0.2s;line-height:1.5}
textarea:focus{border-color:var(--accent)}
.settings-grid{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.setting{display:flex;flex-direction:column;gap:5px}
.setting label{font-size:11px;color:var(--muted)}
select{width:100%;background:#070a0f;border:1px solid var(--border);border-radius:8px;color:var(--text);font-size:12px;padding:7px 10px;outline:none;cursor:pointer}
select:focus{border-color:var(--accent)}
input[type=range]{width:100%;accent-color:var(--accent);cursor:pointer}
.range-row{display:flex;align-items:center;gap:8px}
.range-row span{font-size:11px;color:var(--accent);min-width:28px;text-align:right}
.voices-grid{display:grid;grid-template-columns:1fr 1fr;gap:6px;margin-bottom:12px}
.vbtn{background:#070a0f;border:1px solid var(--border);border-radius:8px;padding:8px 10px;cursor:pointer;text-align:left;transition:all 0.15s;color:var(--text)}
.vbtn:hover{border-color:var(--accent2)}
.vbtn.sel{border-color:var(--accent);background:#0d1e38}
.vbtn .vn{font-size:12px;font-weight:500}
.vbtn .vd{font-size:10px;color:var(--muted);margin-top:2px}
.img-strip{display:flex;gap:6px;overflow-x:auto;padding-bottom:4px;scrollbar-width:thin;scrollbar-color:var(--border) transparent}
.thumb{width:88px;height:56px;border-radius:8px;border:1px solid var(--border);flex-shrink:0;background:var(--surface2);overflow:hidden;display:flex;align-items:center;justify-content:center;font-size:9px;color:var(--muted)}
.thumb.loading{animation:shimmer 1.5s infinite}
@keyframes shimmer{0%,100%{opacity:0.4}50%{opacity:0.9}}
.gen-btn{width:calc(100% - 32px);margin:14px 16px 0;padding:16px;border:none;border-radius:14px;background:linear-gradient(135deg,#1d4ed8,#0ea5e9);color:white;font-family:'Syne',sans-serif;font-weight:700;font-size:16px;cursor:pointer;letter-spacing:0.3px;transition:opacity 0.2s,transform 0.1s;position:relative;overflow:hidden}
.gen-btn:hover{opacity:0.9}
.gen-btn:active{transform:scale(0.98)}
.gen-btn:disabled{opacity:0.4;cursor:not-allowed}
.shimmer{position:absolute;inset:0;background:linear-gradient(90deg,transparent,rgba(255,255,255,0.12),transparent);transform:translateX(-100%)}
.gen-btn.loading .shimmer{animation:slide 1.5s infinite}
@keyframes slide{0%{transform:translateX(-100%)}100%{transform:translateX(200%)}}
.dl-row{margin:10px 16px;display:flex;gap:8px}
.dl-btn{flex:1;padding:12px;border:1px solid var(--border);border-radius:10px;background:var(--surface);color:var(--text);font-size:12px;font-weight:500;cursor:pointer;transition:all 0.15s;text-align:center}
.dl-btn:hover{border-color:var(--accent);background:#0d1e38}
.dl-btn:disabled{opacity:0.3;cursor:not-allowed}
.footer{text-align:center;padding:24px 16px 0;font-size:11px;color:var(--muted)}
.footer strong{color:var(--accent2)}
</style>
</head>
<body>
<div class="studio">

  <div class="topbar">
    <div class="logo">SHIV <span>AI</span></div>
    <div class="badge">VIDEO STUDIO PRO</div>
  </div>

  <div class="hero">
    <div class="hero-title">Script se<br><em>Video</em> banao</div>
    <div class="hero-sub">Shri Ram Nag | PAISAWALA20 | Free • No API Key</div>
  </div>

  <div class="canvas-wrap">
    <canvas id="previewCanvas" width="800" height="450"></canvas>
    <div class="overlay" id="overlay">
      <div class="play-icon">
        <svg width="20" height="20" viewBox="0 0 20 20"><polygon points="6,3 17,10 6,17" fill="rgba(255,255,255,0.6)"/></svg>
      </div>
      <div class="overlay-label">Preview yahan aayega</div>
    </div>
  </div>

  <div class="status-bar">
    <div class="dot" id="dot"></div>
    <div id="statusText">Script likhein aur Generate dabayein</div>
  </div>

  <div class="steps">
    <div class="step" id="s1"><div class="step-num">01</div><div class="step-label">Script</div></div>
    <div class="step" id="s2"><div class="step-num">02</div><div class="step-label">Images</div></div>
    <div class="step" id="s3"><div class="step-num">03</div><div class="step-label">Video</div></div>
  </div>

  <!-- Script Panel -->
  <div class="panel">
    <div class="panel-head">
      <div class="panel-title">📝 Script / Voiceover</div>
      <button style="background:none;border:none;color:var(--muted);font-size:11px;cursor:pointer" onclick="eg()">Example</button>
    </div>
    <div class="panel-body">
      <textarea id="sc" rows="5" placeholder="Yahan Hindi ya English mein script likhein...

Har sentence ek alag scene ban jayega."></textarea>
      <div style="margin-top:6px;display:flex;justify-content:space-between">
        <span style="font-size:11px;color:var(--muted)" id="wc">0 words</span>
        <span style="font-size:11px;color:var(--muted)" id="scount"></span>
      </div>
    </div>
  </div>

  <!-- Voice Panel -->
  <div class="panel">
    <div class="panel-head"><div class="panel-title">🎙️ Voice Settings</div></div>
    <div class="panel-body">
      <div class="voices-grid" id="vgrid"></div>
      <div class="settings-grid">
        <div class="setting">
          <label>Speed</label>
          <div class="range-row">
            <input type="range" id="spd" min="0.5" max="2" step="0.1" value="0.9" oninput="document.getElementById('spv').textContent=this.value">
            <span id="spv">0.9</span>
          </div>
        </div>
        <div class="setting">
          <label>Pitch</label>
          <div class="range-row">
            <input type="range" id="pit" min="0.5" max="2" step="0.1" value="1" oninput="document.getElementById('ptv').textContent=this.value">
            <span id="ptv">1.0</span>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Video Settings Panel -->
  <div class="panel">
    <div class="panel-head"><div class="panel-title">🎬 Video Settings</div></div>
    <div class="panel-body">
      <div class="settings-grid">
        <div class="setting">
          <label>Image Style</label>
          <select id="sty">
            <option value="cinematic film still">Cinematic</option>
            <option value="realistic photo, 8k">Realistic Photo</option>
            <option value="anime art style">Anime</option>
            <option value="digital concept art">Digital Art</option>
            <option value="oil painting style">Oil Painting</option>
            <option value="3d render, octane">3D Render</option>
            <option value="watercolor painting">Watercolor</option>
          </select>
        </div>
        <div class="setting">
          <label>Aspect Ratio</label>
          <select id="ar" onchange="updateRatio()">
            <option value="16:9">16:9 YouTube</option>
            <option value="9:16">9:16 Reels</option>
            <option value="1:1">1:1 Square</option>
          </select>
        </div>
        <div class="setting">
          <label>FPS</label>
          <select id="fps">
            <option value="8">8 fps (fast)</option>
            <option value="12" selected>12 fps (normal)</option>
            <option value="24">24 fps (smooth)</option>
          </select>
        </div>
        <div class="setting">
          <label>Sec per Scene</label>
          <div class="range-row">
            <input type="range" id="dur" min="2" max="6" step="1" value="3" oninput="document.getElementById('dv').textContent=this.value+'s'">
            <span id="dv">3s</span>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Image Preview Panel -->
  <div class="panel" id="prevPanel" style="display:none">
    <div class="panel-head">
      <div class="panel-title">🖼️ Generated Scenes</div>
      <span style="font-size:11px;color:var(--muted)" id="ic"></span>
    </div>
    <div class="panel-body">
      <div class="img-strip" id="strip"></div>
    </div>
  </div>

  <button class="gen-btn" id="gbtn" onclick="start()">
    <span class="shimmer"></span>
    ⚡ Generate Video
  </button>

  <div class="dl-row">
    <button class="dl-btn" id="dlv" disabled onclick="dlVideo()">⬇ Download Video</button>
    <button class="dl-btn" id="dla" disabled onclick="dlAudio()">🔊 Play Audio</button>
  </div>

  <div class="footer">
    Free • No API Key • <strong>Pollinations.AI</strong> + Browser TTS + Canvas<br>
    🔱 Owner: Shri Ram Nag | PAISAWALA20
  </div>
</div>

<script>
// ── State ──────────────────────────────────────────
const VOICES=[
  {id:'hm',name:'Shiv (Hindi M)',desc:'Hindi Male',lang:'hi-IN'},
  {id:'hf',name:'Devi (Hindi F)',desc:'Hindi Female',lang:'hi-IN'},
  {id:'em',name:'Arjun (Eng M)',desc:'English Male',lang:'en-US'},
  {id:'ef',name:'Priya (Eng F)',desc:'English Female',lang:'en-US'},
];
let selV=VOICES[0], imgs=[], frames=[], recording=false;

// ── Init ───────────────────────────────────────────
function initVoices(){
  const g=document.getElementById('vgrid');
  g.innerHTML='';
  VOICES.forEach(v=>{
    const b=document.createElement('button');
    b.className='vbtn'+(v.id===selV.id?' sel':'');
    b.innerHTML=`<div class="vn">${v.name}</div><div class="vd">${v.desc}</div>`;
    b.onclick=()=>{selV=v;initVoices()};
    g.appendChild(b);
  });
}

function updateRatio(){
  const c=document.getElementById('previewCanvas');
  const r=document.getElementById('ar').value;
  if(r==='9:16'){c.width=450;c.height=800;}
  else if(r==='1:1'){c.width=600;c.height=600;}
  else{c.width=800;c.height=450;}
}

function eg(){
  document.getElementById('sc').value=
    'भारत माता की जय। हमारे देश में अनेक नदियाँ और पहाड़ हैं। यहाँ के लोग परिश्रमी और साहसी हैं। शिव की कृपा से यह देश सदा उन्नति करे।';
  upWC();
}

function upWC(){
  const t=document.getElementById('sc').value.trim();
  const wc=t?t.split(/\s+/).length:0;
  document.getElementById('wc').textContent=wc+' words';
  const sc=splitScenes(t);
  document.getElementById('scount').textContent=t?sc.length+' scenes':'';
}
document.getElementById('sc').oninput=upWC;

// ── Helpers ────────────────────────────────────────
function setStatus(msg,state='active'){
  document.getElementById('statusText').textContent=msg;
  document.getElementById('dot').className='dot '+state;
}
function setStep(n,st){document.getElementById('s'+n).className='step '+st;}

function splitScenes(text){
  if(!text.trim())return[];
  const s=text.replace(/([।\.!\?])\s+/g,'$1|||').split('|||').filter(x=>x.trim().length>2);
  if(s.length<=1)return[text.trim()];
  const out=[];
  for(let i=0;i<s.length;i+=2){
    const c=s.slice(i,i+2).join(' ').trim();
    if(c)out.push(c);
  }
  return out;
}

function makePrompt(scene,style){
  const clean=scene.replace(/[।!?\.]/g,'').substring(0,120).trim();
  return `${clean}, ${style}, highly detailed, vivid colors, professional`;
}

async function fetchImg(prompt){
  const seed=Math.floor(Math.random()*99999);
  const c=document.getElementById('previewCanvas');
  const W=c.width,H=c.height;
  const url=`https://image.pollinations.ai/prompt/${encodeURIComponent(prompt)}?width=${W}&height=${H}&nologo=true&seed=${seed}`;
  return new Promise((res,rej)=>{
    const img=new Image();
    img.crossOrigin='anonymous';
    img.onload=()=>res(img);
    img.onerror=()=>rej(new Error('Image failed'));
    img.src=url;
    setTimeout(()=>rej(new Error('Timeout')),35000);
  });
}

function drawFrame(img,canvas,f,total,text){
  const ctx=canvas.getContext('2d');
  const W=canvas.width,H=canvas.height;
  const p=f/total;
  const sc=1+p*0.035;
  ctx.clearRect(0,0,W,H);
  ctx.save();
  ctx.translate(-(W*(sc-1))/2,-(H*(sc-1))/2);
  ctx.scale(sc,sc);
  ctx.drawImage(img,0,0,W,H);
  ctx.restore();
  // Gradient overlay bottom
  const grd=ctx.createLinearGradient(0,H*0.55,0,H);
  grd.addColorStop(0,'rgba(0,0,0,0)');
  grd.addColorStop(1,'rgba(0,0,0,0.75)');
  ctx.fillStyle=grd;
  ctx.fillRect(0,0,W,H);
  // Subtitle
  ctx.font=`500 ${Math.round(W*0.028)}px DM Sans, sans-serif`;
  ctx.fillStyle='rgba(255,255,255,0.95)';
  ctx.textAlign='center';
  ctx.shadowColor='rgba(0,0,0,0.9)';
  ctx.shadowBlur=10;
  const mw=W-W*0.1;
  const words=text.split(' ');
  let line='',lines=[];
  for(const w of words){
    if(ctx.measureText(line+w).width>mw){lines.push(line.trim());line='';}
    line+=w+' ';
  }
  if(line.trim())lines.push(line.trim());
  lines.slice(0,2).forEach((l,i)=>{
    ctx.fillText(l,W/2,H-H*0.08+i*H*0.045);
  });
  ctx.shadowBlur=0;
  // Progress bar
  ctx.fillStyle='rgba(255,255,255,0.15)';
  ctx.fillRect(0,H-3,W,3);
  ctx.fillStyle='#3b82f6';
  ctx.fillRect(0,H-3,W*p,3);
}

async function speakText(text){
  return new Promise(res=>{
    speechSynthesis.cancel();
    const u=new SpeechSynthesisUtterance(text);
    u.rate=parseFloat(document.getElementById('spd').value);
    u.pitch=parseFloat(document.getElementById('pit').value);
    u.lang=selV.lang;
    const allV=speechSynthesis.getVoices();
    const match=allV.find(v=>v.lang.startsWith(selV.lang.split('-')[0]));
    if(match)u.voice=match;
    u.onend=res;u.onerror=res;
    speechSynthesis.speak(u);
  });
}

// ── Main Generate ──────────────────────────────────
async function start(){
  const script=document.getElementById('sc').value.trim();
  if(!script){setStatus('Script likhein pehle!','error');return;}

  const btn=document.getElementById('gbtn');
  btn.disabled=true;
  btn.classList.add('loading');
  btn.querySelector('span+*')
  btn.childNodes[1].textContent=' Generating...';

  document.getElementById('dlv').disabled=true;
  document.getElementById('dla').disabled=true;
  document.getElementById('overlay').classList.add('hidden');
  imgs=[];frames=[];

  const style=document.getElementById('sty').value;
  const fps=parseInt(document.getElementById('fps').value);
  const dur=parseInt(document.getElementById('dur').value);
  const scenes=splitScenes(script);
  const FPS_FRAMES=fps*dur;

  setStep(1,'active');setStep(2,'');setStep(3,'');
  setStatus(`Script → ${scenes.length} scenes`);
  await sleep(500);
  setStep(1,'done');setStep(2,'active');

  // Show preview panel
  document.getElementById('prevPanel').style.display='block';
  document.getElementById('strip').innerHTML='';
  document.getElementById('ic').textContent=scenes.length+' scenes';

  const canvas=document.getElementById('previewCanvas');

  // Generate images
  for(let i=0;i<scenes.length;i++){
    setStatus(`Image ${i+1}/${scenes.length} generate ho rahi hai...`);
    const thumb=document.createElement('div');
    thumb.className='thumb loading';
    thumb.textContent='⏳';
    document.getElementById('strip').appendChild(thumb);
    try{
      const prompt=makePrompt(scenes[i],style);
      const img=await fetchImg(prompt);
      imgs.push(img);
      thumb.classList.remove('loading');
      thumb.textContent='';
      const tc=document.createElement('canvas');
      tc.width=88;tc.height=56;
      tc.getContext('2d').drawImage(img,0,0,88,56);
      tc.style.cssText='width:88px;height:56px;display:block';
      thumb.appendChild(tc);
      // Show on main canvas
      drawFrame(img,canvas,0,FPS_FRAMES,scenes[i]);
    }catch(e){
      imgs.push(null);
      thumb.classList.remove('loading');
      thumb.style.background='#1a0a0a';
      thumb.innerHTML='<span style="color:#ef4444;font-size:10px">❌</span>';
    }
  }

  setStep(2,'done');setStep(3,'active');
  setStatus('Video frames render ho rahe hain...');

  // Render all frames to canvas sequentially
  for(let i=0;i<scenes.length;i++){
    if(!imgs[i])continue;
    for(let f=0;f<FPS_FRAMES;f++){
      drawFrame(imgs[i],canvas,f,FPS_FRAMES,scenes[i]);
      if(f%4===0){
        setStatus(`Rendering scene ${i+1}/${scenes.length} — frame ${f+1}/${FPS_FRAMES}`);
        await sleep(1);
      }
    }
  }

  setStep(3,'done');
  setStatus('Ready! Download karo 🎉','done');
  document.getElementById('dlv').disabled=false;
  document.getElementById('dla').disabled=false;

  btn.disabled=false;
  btn.classList.remove('loading');
  btn.childNodes[1].textContent=' Generate Again';
}

// ── Download Video (WebM via MediaRecorder) ────────
async function dlVideo(){
  if(!imgs.length){setStatus('Pehle generate karo!','error');return;}
  const canvas=document.getElementById('previewCanvas');
  const fps=parseInt(document.getElementById('fps').value);
  const dur=parseInt(document.getElementById('dur').value);
  const scenes=splitScenes(document.getElementById('sc').value.trim());
  const FPS_FRAMES=fps*dur;
  let stream,rec,chunks=[];
  const mimeTypes=['video/webm;codecs=vp9','video/webm;codecs=vp8','video/webm'];
  let mime='video/webm';
  for(const m of mimeTypes){if(MediaRecorder.isTypeSupported(m)){mime=m;break;}}
  try{stream=canvas.captureStream(fps);}
  catch(e){setStatus('captureStream not supported — Chrome use karein','error');return;}
  rec=new MediaRecorder(stream,{mimeType:mime,videoBitsPerSecond:4000000});
  rec.ondataavailable=e=>{if(e.data&&e.data.size>0)chunks.push(e.data);};
  rec.onstop=()=>{
    const blob=new Blob(chunks,{type:mime});
    const url=URL.createObjectURL(blob);
    const a=document.createElement('a');
    a.href=url;a.download='ShivAI_Video.webm';
    document.body.appendChild(a);a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
    setStatus('Video downloaded! ✅','done');
  };
  rec.start(100);
  setStatus('Recording video...');
  for(let i=0;i<scenes.length;i++){
    if(!imgs[i])continue;
    for(let f=0;f<FPS_FRAMES;f++){
      drawFrame(imgs[i],canvas,f,FPS_FRAMES,scenes[i]);
      await sleep(Math.round(1000/fps));
    }
  }
  rec.stop();
}

async function dlAudio(){
  const sc=document.getElementById('sc').value.trim();
  if(!sc){setStatus('Script nahi hai!','error');return;}
  setStatus('Voice over play ho rahi hai...','active');
  await speakText(sc);
  setStatus('Audio play hua!','done');
}

function sleep(ms){return new Promise(r=>setTimeout(r,ms));}

// ── Boot ───────────────────────────────────────────
initVoices();
speechSynthesis.getVoices();
window.speechSynthesis.onvoiceschanged=initVoices;
</script>
</body>
</html>
"""

# ── Gradio Wrapper ─────────────────────────────────
with gr.Blocks(title="Shiv AI Video Studio", theme=gr.themes.Base()) as demo:
    gr.HTML("""
    <style>
    body, .gradio-container { background: #070a0f !important; padding: 0 !important; margin: 0 !important; }
    footer { display: none !important; }
    .contain { padding: 0 !important; }
    </style>
    """)
    gr.HTML(HTML_UI)

if __name__ == "__main__":
    demo.launch(
        share=True,
        server_name="0.0.0.0",
        server_port=7860,
        show_error=True
    )
