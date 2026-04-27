# --------------------------------------------------
# 🔱 SHIV AI VIDEO STUDIO PRO
# 👤 Owner: Shri Ram Nag | 📺 PAISAWALA20
# ✅ Works: Browser | Google Colab | VS Code Preview
# --------------------------------------------------

import gradio as gr

HTML_UI = r"""
<!DOCTYPE html>
<html lang="hi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
<title>Shiv AI Video Studio</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=DM+Sans:wght@300;400;500&display=swap');
*{box-sizing:border-box;margin:0;padding:0}
:root{
  --bg:#05080e;--s1:#0b0f18;--s2:#111827;--bd:#1e2d40;
  --acc:#3b82f6;--acc2:#06b6d4;--tx:#eef2f7;--mu:#556070;
  --ok:#22c55e;--err:#ef4444;--warn:#f59e0b;
}
html,body{background:var(--bg);color:var(--tx);font-family:'DM Sans',sans-serif;min-height:100vh;-webkit-font-smoothing:antialiased}
.app{max-width:500px;margin:0 auto;padding-bottom:60px}

/* Top bar */
.topbar{padding:14px 16px 0;display:flex;align-items:center;justify-content:space-between}
.logo{font-family:'Syne',sans-serif;font-weight:800;font-size:20px;letter-spacing:-0.5px;color:var(--tx)}
.logo b{color:var(--acc)}
.chip{font-size:10px;background:#0f1e30;color:var(--acc2);padding:4px 10px;border-radius:20px;border:1px solid #1a3a50;letter-spacing:0.3px}

/* Hero */
.hero{padding:18px 16px 12px}
.ht{font-family:'Syne',sans-serif;font-size:26px;font-weight:800;line-height:1.2;letter-spacing:-0.8px}
.ht em{font-style:normal;color:var(--acc)}
.hs{font-size:12px;color:var(--mu);margin-top:5px}

/* Canvas */
.cv-wrap{margin:0 16px;border-radius:14px;overflow:hidden;border:1px solid var(--bd);background:var(--s1);position:relative}
.cv-wrap canvas{width:100%;display:block}
.cv-over{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:10px;background:rgba(5,8,14,0.7)}
.cv-over.h{display:none}
.pi{width:54px;height:54px;border-radius:50%;border:2px solid rgba(255,255,255,0.12);display:flex;align-items:center;justify-content:center}
.cv-lbl{font-size:12px;color:var(--mu)}

/* Status */
.sbar{margin:10px 16px;background:var(--s1);border:1px solid var(--bd);border-radius:10px;padding:10px 14px;display:flex;align-items:center;gap:8px;min-height:40px}
.dot{width:7px;height:7px;border-radius:50%;background:var(--mu);flex-shrink:0;transition:background .3s}
.dot.go{background:var(--acc);animation:blink 1.2s infinite}
.dot.ok{background:var(--ok)}
.dot.er{background:var(--err)}
@keyframes blink{0%,100%{opacity:1}50%{opacity:.3}}
#stxt{font-size:12px;color:var(--mu);flex:1;line-height:1.4}

/* Steps */
.steps{margin:10px 16px;display:grid;grid-template-columns:repeat(3,1fr);gap:8px}
.step{background:var(--s1);border:1px solid var(--bd);border-radius:10px;padding:10px 6px;text-align:center;transition:all .25s}
.step.go{border-color:var(--acc);background:#0a1a2e}
.step.ok{border-color:var(--ok);background:#071a0f}
.sn{font-size:10px;color:var(--mu);font-weight:700;margin-bottom:3px}
.sl{font-size:11px;font-weight:500}
.step.go .sn{color:var(--acc)}
.step.ok .sl{color:var(--ok)}

/* Panel */
.panel{margin:10px 16px;background:var(--s1);border:1px solid var(--bd);border-radius:14px;overflow:hidden}
.ph{padding:11px 14px;border-bottom:1px solid var(--bd);display:flex;align-items:center;justify-content:space-between}
.pt{font-size:13px;font-weight:500;display:flex;align-items:center;gap:6px;color:var(--tx)}
.pb{padding:13px 14px}
.eg-btn{background:none;border:none;color:var(--mu);font-size:11px;cursor:pointer;font-family:'DM Sans',sans-serif}
.eg-btn:hover{color:var(--acc)}

/* Inputs */
textarea{width:100%;background:var(--bg);border:1px solid var(--bd);border-radius:10px;color:var(--tx);font-family:'DM Sans',sans-serif;font-size:13px;padding:10px 12px;resize:none;outline:none;transition:border-color .2s;line-height:1.6}
textarea:focus{border-color:var(--acc)}
select{width:100%;background:var(--bg);border:1px solid var(--bd);border-radius:8px;color:var(--tx);font-size:12px;padding:8px 10px;outline:none;cursor:pointer;font-family:'DM Sans',sans-serif}
select:focus{border-color:var(--acc)}
input[type=range]{width:100%;accent-color:var(--acc);cursor:pointer;height:4px}
.rr{display:flex;align-items:center;gap:8px}
.rv{font-size:11px;color:var(--acc);min-width:30px;text-align:right;font-weight:500}
.sg{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.sf{display:flex;flex-direction:column;gap:5px}
.sf label{font-size:11px;color:var(--mu)}

/* Voices */
.vg{display:grid;grid-template-columns:1fr 1fr;gap:6px;margin-bottom:12px}
.vb{background:var(--bg);border:1px solid var(--bd);border-radius:8px;padding:8px 10px;cursor:pointer;text-align:left;transition:all .15s;color:var(--tx);font-family:'DM Sans',sans-serif}
.vb:hover{border-color:var(--acc2)}
.vb.sel{border-color:var(--acc);background:#0a1a2e}
.vn{font-size:12px;font-weight:500}
.vd{font-size:10px;color:var(--mu);margin-top:2px}

/* Strip */
.strip{display:flex;gap:6px;overflow-x:auto;padding-bottom:4px;scrollbar-width:thin;scrollbar-color:var(--bd) transparent}
.thumb{width:90px;height:56px;border-radius:8px;border:1px solid var(--bd);flex-shrink:0;background:var(--s2);overflow:hidden;display:flex;align-items:center;justify-content:center;font-size:10px;color:var(--mu);position:relative}
.thumb.loading::after{content:'';position:absolute;inset:0;background:linear-gradient(90deg,transparent,rgba(59,130,246,.15),transparent);animation:sh 1.5s infinite}
@keyframes sh{0%{transform:translateX(-100%)}100%{transform:translateX(200%)}}

/* Generate Button */
.gbtn{width:calc(100% - 32px);margin:12px 16px 0;padding:15px;border:none;border-radius:14px;background:linear-gradient(135deg,#1d4ed8 0%,#0284c7 100%);color:#fff;font-family:'Syne',sans-serif;font-weight:700;font-size:16px;cursor:pointer;letter-spacing:.3px;transition:opacity .2s,transform .1s;position:relative;overflow:hidden;display:block}
.gbtn:hover{opacity:.9}
.gbtn:active{transform:scale(.98)}
.gbtn:disabled{opacity:.35;cursor:not-allowed}
.gbtn .sw{position:absolute;inset:0;background:linear-gradient(90deg,transparent,rgba(255,255,255,.12),transparent);transform:translateX(-100%)}
.gbtn.loading .sw{animation:slide 1.4s infinite}
@keyframes slide{0%{transform:translateX(-100%)}100%{transform:translateX(200%)}}

/* Download Row */
.dlr{margin:10px 16px;display:flex;gap:8px}
.dlb{flex:1;padding:11px;border:1px solid var(--bd);border-radius:10px;background:var(--s1);color:var(--tx);font-size:12px;font-weight:500;cursor:pointer;transition:all .15s;text-align:center;font-family:'DM Sans',sans-serif}
.dlb:hover{border-color:var(--acc);background:#0a1a2e}
.dlb:disabled{opacity:.3;cursor:not-allowed}

/* Progress bar */
.prog-wrap{margin:0 16px 0;display:none}
.prog-wrap.show{display:block}
.prog-bar{height:3px;background:var(--bd);border-radius:2px;overflow:hidden;margin-top:6px}
.prog-fill{height:100%;background:var(--acc);width:0%;transition:width .3s;border-radius:2px}
.prog-txt{font-size:10px;color:var(--mu);margin-top:4px;text-align:right}

.footer{text-align:center;padding:20px 16px 0;font-size:11px;color:var(--mu);line-height:1.8}
.footer strong{color:var(--acc2)}

/* Scrollbar */
::-webkit-scrollbar{width:4px;height:4px}
::-webkit-scrollbar-track{background:var(--bg)}
::-webkit-scrollbar-thumb{background:var(--bd);border-radius:2px}
</style>
</head>
<body>
<div class="app">

<div class="topbar">
  <div class="logo">SHIV <b>AI</b></div>
  <div class="chip">VIDEO STUDIO PRO</div>
</div>

<div class="hero">
  <div class="ht">Script se<br><em>Video</em> banao</div>
  <div class="hs">Shri Ram Nag · PAISAWALA20 · Free · No API Key Required</div>
</div>

<div class="cv-wrap" id="cvWrap">
  <canvas id="cv" width="800" height="450"></canvas>
  <div class="cv-over" id="cvo">
    <div class="pi">
      <svg width="20" height="20" viewBox="0 0 20 20">
        <polygon points="6,3 17,10 6,17" fill="rgba(255,255,255,0.5)"/>
      </svg>
    </div>
    <div class="cv-lbl">Preview yahan dikhega</div>
  </div>
</div>

<div class="sbar"><div class="dot" id="dot"></div><div id="stxt">Script likhein aur Generate karein</div></div>

<div class="steps">
  <div class="step" id="st1"><div class="sn">01</div><div class="sl">Script</div></div>
  <div class="step" id="st2"><div class="sn">02</div><div class="sl">Images</div></div>
  <div class="step" id="st3"><div class="sn">03</div><div class="sl">Video</div></div>
</div>

<div class="prog-wrap" id="pw">
  <div class="prog-bar"><div class="prog-fill" id="pf"></div></div>
  <div class="prog-txt" id="pt">0%</div>
</div>

<!-- Script Panel -->
<div class="panel">
  <div class="ph">
    <div class="pt">📝 Script / Voiceover Text</div>
    <button class="eg-btn" onclick="loadEg()">Example load karo ↗</button>
  </div>
  <div class="pb">
    <textarea id="sc" rows="5" placeholder="Yahan Hindi ya English mein script likhein...

Har sentence automatically ek alag scene ban jayega.
Jitne zyada sentences, utne zyada scenes!"></textarea>
    <div style="margin-top:6px;display:flex;justify-content:space-between;align-items:center">
      <span style="font-size:11px;color:var(--mu)" id="wc">0 words</span>
      <span style="font-size:11px;color:var(--acc2)" id="sc2"></span>
    </div>
  </div>
</div>

<!-- Voice Panel -->
<div class="panel">
  <div class="ph"><div class="pt">🎙️ Voice Settings</div></div>
  <div class="pb">
    <div class="vg" id="vg"></div>
    <div class="sg">
      <div class="sf">
        <label>Speed</label>
        <div class="rr">
          <input type="range" id="spd" min="0.5" max="1.8" step="0.1" value="0.85"
            oninput="document.getElementById('spv').textContent=parseFloat(this.value).toFixed(1)">
          <span class="rv" id="spv">0.9</span>
        </div>
      </div>
      <div class="sf">
        <label>Pitch</label>
        <div class="rr">
          <input type="range" id="pit" min="0.5" max="2" step="0.1" value="1"
            oninput="document.getElementById('ptv').textContent=parseFloat(this.value).toFixed(1)">
          <span class="rv" id="ptv">1.0</span>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- Video Settings Panel -->
<div class="panel">
  <div class="ph"><div class="pt">🎬 Video Settings</div></div>
  <div class="pb">
    <div class="sg">
      <div class="sf">
        <label>Image Style</label>
        <select id="sty">
          <option value="cinematic film still, dramatic lighting">Cinematic</option>
          <option value="realistic photo, 8k, DSLR">Realistic Photo</option>
          <option value="anime art, Studio Ghibli style">Anime</option>
          <option value="digital concept art, vivid colors">Digital Art</option>
          <option value="oil painting, impressionist">Oil Painting</option>
          <option value="3d render, octane render, photorealistic">3D Render</option>
          <option value="watercolor painting, soft edges">Watercolor</option>
          <option value="ancient Indian art, Mughal miniature style">Indian Art</option>
        </select>
      </div>
      <div class="sf">
        <label>Aspect Ratio</label>
        <select id="ar" onchange="updateRatio()">
          <option value="16:9">16:9 YouTube</option>
          <option value="9:16">9:16 Reels</option>
          <option value="1:1">1:1 Square</option>
        </select>
      </div>
      <div class="sf">
        <label>FPS</label>
        <select id="fps">
          <option value="8">8 fps — Fast</option>
          <option value="12" selected>12 fps — Normal</option>
          <option value="24">24 fps — Smooth</option>
        </select>
      </div>
      <div class="sf">
        <label>Seconds / Scene</label>
        <div class="rr">
          <input type="range" id="dur" min="2" max="7" step="1" value="3"
            oninput="document.getElementById('dv').textContent=this.value+'s'">
          <span class="rv" id="dv">3s</span>
        </div>
      </div>
    </div>
    <!-- Ken Burns toggle -->
    <div style="margin-top:10px;display:flex;align-items:center;gap:8px">
      <input type="checkbox" id="kb" checked style="accent-color:var(--acc);width:14px;height:14px">
      <label for="kb" style="font-size:12px;color:var(--mu);cursor:pointer">Ken Burns effect (slow zoom)</label>
    </div>
  </div>
</div>

<!-- Scene Preview Panel -->
<div class="panel" id="prevP" style="display:none">
  <div class="ph">
    <div class="pt">🖼️ Scene Images</div>
    <span style="font-size:11px;color:var(--mu)" id="ic"></span>
  </div>
  <div class="pb">
    <div class="strip" id="strip"></div>
  </div>
</div>

<button class="gbtn" id="gbtn" onclick="startGen()">
  <span class="sw"></span>
  ⚡ Generate Video
</button>

<div class="dlr">
  <button class="dlb" id="dlv" disabled onclick="doDownload()">⬇ Download Video</button>
  <button class="dlb" id="dla" disabled onclick="playAudio()">🔊 Play Voiceover</button>
</div>

<div class="footer">
  <strong>Pollinations.AI</strong> · Browser TTS · Canvas API · 100% Free<br>
  🔱 Shri Ram Nag · PAISAWALA20
</div>

</div><!-- /app -->

<script>
// ═══════════════════════════════════════════
//  STATE
// ═══════════════════════════════════════════
const VOICES=[
  {id:'hm',name:'Shiv (Hindi)',  desc:'Hindi Male',  lang:'hi-IN',gender:'male'},
  {id:'hf',name:'Devi (Hindi)',  desc:'Hindi Female', lang:'hi-IN',gender:'female'},
  {id:'em',name:'Arjun (Eng)',   desc:'English Male', lang:'en-US',gender:'male'},
  {id:'ef',name:'Priya (Eng)',   desc:'English Female',lang:'en-US',gender:'female'},
];
let selV=VOICES[0];
let genImgs=[];    // HTMLImageElement per scene
let genScenes=[];  // scene text per scene
let isGen=false;

// ═══════════════════════════════════════════
//  INIT
// ═══════════════════════════════════════════
function initVoices(){
  const g=document.getElementById('vg'); g.innerHTML='';
  VOICES.forEach(v=>{
    const b=document.createElement('button');
    b.className='vb'+(v.id===selV.id?' sel':'');
    b.innerHTML=`<div class="vn">${v.name}</div><div class="vd">${v.desc}</div>`;
    b.onclick=()=>{selV=v;initVoices()};
    g.appendChild(b);
  });
}
function updateRatio(){
  const c=document.getElementById('cv');
  const ar=document.getElementById('ar').value;
  if(ar==='9:16'){c.width=450;c.height=800;}
  else if(ar==='1:1'){c.width=600;c.height=600;}
  else{c.width=800;c.height=450;}
  blackCanvas();
}
function blackCanvas(){
  const c=document.getElementById('cv');
  const ctx=c.getContext('2d');
  ctx.fillStyle='#05080e';
  ctx.fillRect(0,0,c.width,c.height);
}
function loadEg(){
  document.getElementById('sc').value=
    'जय श्री राम। भारत एक महान देश है। यहाँ की नदियाँ और पहाड़ बहुत सुंदर हैं। शिव की कृपा से यह देश हमेशा उन्नति करे। जय हिंद।';
  upWC();
}
function upWC(){
  const t=document.getElementById('sc').value.trim();
  const wc=t?t.split(/\s+/).length:0;
  document.getElementById('wc').textContent=wc+' words';
  const sc=splitScenes(t);
  document.getElementById('sc2').textContent=t?(sc.length+' scenes'):'';
}
document.getElementById('sc').oninput=upWC;

// ═══════════════════════════════════════════
//  STATUS / STEP HELPERS
// ═══════════════════════════════════════════
function setS(msg,state='go'){
  document.getElementById('stxt').textContent=msg;
  document.getElementById('dot').className='dot '+state;
}
function setStep(n,st){document.getElementById('st'+n).className='step '+st;}
function setProgress(pct,label){
  const pw=document.getElementById('pw');
  pw.classList.add('show');
  document.getElementById('pf').style.width=pct+'%';
  document.getElementById('pt').textContent=label||Math.round(pct)+'%';
}
function hideProgress(){document.getElementById('pw').classList.remove('show');}

// ═══════════════════════════════════════════
//  SCENE SPLITTING
// ═══════════════════════════════════════════
function splitScenes(text){
  if(!text.trim())return[];
  // Split on sentence-ending punctuation
  const raw=text
    .replace(/([।\.!\?؟])\s*/g,'$1|||')
    .split('|||')
    .map(s=>s.trim())
    .filter(s=>s.length>2);
  if(!raw.length)return[text.trim()];
  // Merge very short fragments
  const out=[];
  let buf='';
  for(const s of raw){
    buf+=(buf?' ':'')+s;
    if(buf.split(/\s+/).length>=4){out.push(buf);buf='';}
  }
  if(buf)out.push(buf);
  return out;
}

// ═══════════════════════════════════════════
//  IMAGE LOADING — multi-fallback, CORS safe
// ═══════════════════════════════════════════
function buildImgUrl(prompt,w,h,seed,service){
  const ep=encodeURIComponent(prompt);
  if(service===0)
    return `https://image.pollinations.ai/prompt/${ep}?width=${w}&height=${h}&nologo=true&seed=${seed}&model=flux`;
  if(service===1)
    return `https://image.pollinations.ai/prompt/${ep}?width=${w}&height=${h}&nologo=true&seed=${seed+1}&model=turbo`;
  // service 2: smaller size fallback
  return `https://image.pollinations.ai/prompt/${ep}?width=${Math.min(w,512)}&height=${Math.min(h,512)}&nologo=true&seed=${seed+2}`;
}

function loadImg(url){
  return new Promise((res,rej)=>{
    const img=new Image();
    img.crossOrigin='anonymous';
    const tid=setTimeout(()=>rej(new Error('timeout')),40000);
    img.onload=()=>{clearTimeout(tid);res(img);};
    img.onerror=()=>{clearTimeout(tid);rej(new Error('load error'));};
    img.src=url;
  });
}

async function fetchSceneImg(prompt,w,h){
  const seed=Math.floor(Math.random()*99999);
  for(let s=0;s<3;s++){
    try{
      const url=buildImgUrl(prompt,w,h,seed,s);
      const img=await loadImg(url);
      return img;
    }catch(e){
      await sleep(800);
    }
  }
  // Return null — draw placeholder
  return null;
}

function makePrompt(scene,style){
  const clean=scene.replace(/[।!?\.]/g,'').substring(0,100).trim();
  return `${clean}, ${style}, high quality, detailed, vibrant`;
}

// ═══════════════════════════════════════════
//  CANVAS DRAWING
// ═══════════════════════════════════════════
function drawFrame(ctx,img,W,H,frameIdx,totalFrames,sceneText,kenBurns){
  const p=totalFrames>1?frameIdx/(totalFrames-1):0;
  ctx.clearRect(0,0,W,H);

  if(img){
    if(kenBurns){
      const sc=1+p*0.04;
      const dx=-(W*(sc-1))/2 * (0.5+p*0.5);
      const dy=-(H*(sc-1))/2;
      ctx.save();
      ctx.translate(dx,dy);
      ctx.scale(sc,sc);
      ctx.drawImage(img,0,0,W,H);
      ctx.restore();
    }else{
      ctx.drawImage(img,0,0,W,H);
    }
  }else{
    // Placeholder gradient
    const gp=ctx.createLinearGradient(0,0,W,H);
    gp.addColorStop(0,'#0a1628');gp.addColorStop(1,'#050810');
    ctx.fillStyle=gp;ctx.fillRect(0,0,W,H);
    ctx.fillStyle='rgba(59,130,246,0.08)';
    ctx.beginPath();ctx.arc(W/2,H/2,Math.min(W,H)*0.3,0,Math.PI*2);ctx.fill();
  }

  // Bottom gradient
  const grad=ctx.createLinearGradient(0,H*0.5,0,H);
  grad.addColorStop(0,'rgba(0,0,0,0)');
  grad.addColorStop(1,'rgba(0,0,0,0.82)');
  ctx.fillStyle=grad;ctx.fillRect(0,0,W,H);

  // Subtitle
  const fs=Math.max(14,Math.round(W*0.027));
  ctx.font=`500 ${fs}px DM Sans, sans-serif`;
  ctx.fillStyle='rgba(255,255,255,0.95)';
  ctx.textAlign='center';
  ctx.shadowColor='rgba(0,0,0,0.95)';
  ctx.shadowBlur=12;

  const maxW=W*0.88;
  const words=sceneText.split(' ');
  let line='',lines=[];
  for(const w of words){
    const test=line+(line?' ':'')+w;
    if(ctx.measureText(test).width>maxW && line){lines.push(line);line=w;}
    else{line=test;}
  }
  if(line)lines.push(line);
  const lh=fs*1.45;
  const startY=H-lh*(lines.length)+fs*0.4-12;
  lines.slice(0,3).forEach((l,i)=>ctx.fillText(l,W/2,startY+i*lh));
  ctx.shadowBlur=0;

  // Progress bar
  ctx.fillStyle='rgba(255,255,255,0.08)';
  ctx.fillRect(0,H-3,W,3);
  ctx.fillStyle='#3b82f6';
  ctx.fillRect(0,H-3,W*p,3);

  // Watermark
  ctx.font=`400 ${Math.max(9,Math.round(W*0.018))}px DM Sans`;
  ctx.fillStyle='rgba(255,255,255,0.25)';
  ctx.textAlign='right';
  ctx.fillText('🔱 SHIV AI · PAISAWALA20',W-10,16);
  ctx.textAlign='center';
}

function addThumb(img,sceneIdx){
  const strip=document.getElementById('strip');
  const wrap=document.createElement('div');
  wrap.className='thumb';
  if(img){
    const tc=document.createElement('canvas');
    tc.width=90;tc.height=56;
    tc.style.cssText='width:90px;height:56px;display:block';
    tc.getContext('2d').drawImage(img,0,0,90,56);
    wrap.appendChild(tc);
  }else{
    wrap.innerHTML='<span style="color:var(--err);font-size:16px">✗</span>';
  }
  strip.appendChild(wrap);
}

// ═══════════════════════════════════════════
//  MAIN GENERATE
// ═══════════════════════════════════════════
async function startGen(){
  if(isGen)return;
  const script=document.getElementById('sc').value.trim();
  if(!script){setS('Script likhein pehle!','er');return;}

  const scenes=splitScenes(script);
  if(!scenes.length){setS('Valid script likhein','er');return;}

  isGen=true;
  genImgs=[];genScenes=scenes;
  const btn=document.getElementById('gbtn');
  btn.disabled=true;btn.classList.add('loading');
  btn.childNodes[1].textContent=' Generating...';
  document.getElementById('dlv').disabled=true;
  document.getElementById('dla').disabled=true;
  document.getElementById('cvo').classList.add('h');

  const style=document.getElementById('sty').value;
  const fps=parseInt(document.getElementById('fps').value);
  const dur=parseInt(document.getElementById('dur').value);
  const kb=document.getElementById('kb').checked;
  const cv=document.getElementById('cv');
  const ctx=cv.getContext('2d');
  const W=cv.width,H=cv.height;
  const FPF=fps*dur;  // frames per scene

  // ── Step 1: Script parsed
  setStep(1,'go');setStep(2,'');setStep(3,'');
  setS(`Script → ${scenes.length} scenes`);
  setProgress(5,'Parsing...');
  await sleep(400);
  setStep(1,'ok');

  // ── Step 2: Generate images
  setStep(2,'go');
  document.getElementById('prevP').style.display='block';
  document.getElementById('strip').innerHTML='';
  document.getElementById('ic').textContent=scenes.length+' scenes';

  for(let i=0;i<scenes.length;i++){
    const pct=10+Math.round((i/scenes.length)*50);
    setS(`Image ${i+1}/${scenes.length} generate ho rahi hai...`);
    setProgress(pct,`Image ${i+1}/${scenes.length}`);

    // Show loading thumb
    const strip=document.getElementById('strip');
    const wrap=document.createElement('div');
    wrap.className='thumb loading';
    wrap.innerHTML='<span style="font-size:10px;color:var(--mu)">⏳</span>';
    strip.appendChild(wrap);

    const prompt=makePrompt(scenes[i],style);
    const img=await fetchSceneImg(prompt,W,H);
    genImgs.push(img);

    // Update thumb
    wrap.classList.remove('loading');
    wrap.innerHTML='';
    if(img){
      const tc=document.createElement('canvas');
      tc.width=90;tc.height=56;tc.style.cssText='width:90px;height:56px;display:block';
      tc.getContext('2d').drawImage(img,0,0,90,56);
      wrap.appendChild(tc);
      // Show on main canvas
      drawFrame(ctx,img,W,H,0,FPF,scenes[i],kb);
    }else{
      wrap.innerHTML='<span style="color:var(--err);font-size:16px">✗</span>';
    }
  }

  setStep(2,'ok');

  // ── Step 3: Render preview animation
  setStep(3,'go');
  setS('Video preview render ho raha hai...');

  let totalF=scenes.length*FPF;
  let done=0;
  for(let i=0;i<scenes.length;i++){
    for(let f=0;f<FPF;f++){
      drawFrame(ctx,genImgs[i]||null,W,H,f,FPF,scenes[i],kb);
      done++;
      if(f%Math.max(1,Math.floor(FPF/6))===0){
        const pct=60+Math.round((done/totalF)*38);
        setProgress(pct,`Rendering ${Math.round(done/totalF*100)}%`);
        await sleep(1);
      }
    }
  }

  setStep(3,'ok');
  setProgress(100,'Complete!');
  setS('Video ready hai! Download karo 🎉','ok');

  document.getElementById('dlv').disabled=false;
  document.getElementById('dla').disabled=false;
  isGen=false;
  btn.disabled=false;btn.classList.remove('loading');
  btn.childNodes[1].textContent=' Generate Again';

  await sleep(2000);
  hideProgress();
}

// ═══════════════════════════════════════════
//  VIDEO DOWNLOAD (MediaRecorder)
// ═══════════════════════════════════════════
async function doDownload(){
  if(!genImgs.length){setS('Pehle generate karo!','er');return;}
  const cv=document.getElementById('cv');
  const ctx=cv.getContext('2d');
  const W=cv.width,H=cv.height;
  const fps=parseInt(document.getElementById('fps').value);
  const dur=parseInt(document.getElementById('dur').value);
  const kb=document.getElementById('kb').checked;
  const FPF=fps*dur;

  // Pick best supported mime
  const mimes=['video/webm;codecs=vp9','video/webm;codecs=vp8','video/webm','video/mp4'];
  let mime='video/webm';
  for(const m of mimes){try{if(MediaRecorder.isTypeSupported(m)){mime=m;break;}}catch(e){}}

  let stream;
  try{stream=cv.captureStream(fps);}
  catch(e){setS('captureStream nahi chala — Chrome use karein','er');return;}

  const chunks=[];
  const rec=new MediaRecorder(stream,{mimeType:mime,videoBitsPerSecond:5000000});
  rec.ondataavailable=e=>{if(e.data&&e.data.size>0)chunks.push(e.data);};
  rec.onstop=()=>{
    const blob=new Blob(chunks,{type:mime});
    const url=URL.createObjectURL(blob);
    const a=document.createElement('a');
    a.href=url;
    a.download='ShivAI_Video_'+Date.now()+'.webm';
    document.body.appendChild(a);a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
    setS('Video download ho gayi! ✅','ok');
  };

  rec.start(100);
  setS('Recording video...','go');
  setProgress(0,'Recording...');

  let total=genScenes.length*FPF,done=0;
  for(let i=0;i<genScenes.length;i++){
    for(let f=0;f<FPF;f++){
      drawFrame(ctx,genImgs[i]||null,W,H,f,FPF,genScenes[i],kb);
      await sleep(Math.round(1000/fps));
      done++;
      setProgress(Math.round(done/total*100));
    }
  }
  rec.stop();
  hideProgress();
}

// ═══════════════════════════════════════════
//  VOICEOVER (Browser TTS)
// ═══════════════════════════════════════════
async function playAudio(){
  const sc=document.getElementById('sc').value.trim();
  if(!sc){setS('Script nahi hai!','er');return;}
  speechSynthesis.cancel();
  await sleep(200);
  const u=new SpeechSynthesisUtterance(sc);
  u.rate=parseFloat(document.getElementById('spd').value);
  u.pitch=parseFloat(document.getElementById('pit').value);
  u.lang=selV.lang;
  const allV=speechSynthesis.getVoices();
  const match=allV.find(v=>v.lang&&v.lang.startsWith(selV.lang.split('-')[0]));
  if(match)u.voice=match;
  u.onstart=()=>setS('Voice over play ho rahi hai...','go');
  u.onend=()=>setS('Voice over complete! ✅','ok');
  u.onerror=()=>setS('Voice over mein error — browser TTS check karein','er');
  speechSynthesis.speak(u);
}

// ═══════════════════════════════════════════
//  UTILS
// ═══════════════════════════════════════════
function sleep(ms){return new Promise(r=>setTimeout(r,ms));}

// ── Boot ──────────────────────────────────
initVoices();
blackCanvas();
// Pre-load voices
if(speechSynthesis.getVoices().length===0){
  speechSynthesis.addEventListener('voiceschanged',initVoices,{once:true});
}
</script>
</body>
</html>
"""

# ── Gradio App ─────────────────────────────────────
with gr.Blocks(
    title="🔱 Shiv AI Video Studio",
    theme=gr.themes.Base(),
    css="""
    body, .gradio-container, .main, .wrap {
        background: #05080e !important;
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100% !important;
    }
    footer { display: none !important; }
    .contain, .gap { padding: 0 !important; gap: 0 !important; }
    #component-0 { padding: 0 !important; }
    """
) as demo:
    gr.HTML(HTML_UI)

if __name__ == "__main__":
    demo.launch(
        share=True,
        server_name="0.0.0.0",
        server_port=7860,
        show_error=True,
        quiet=False
    )
