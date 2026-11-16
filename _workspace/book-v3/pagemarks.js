// Her 16 Nov ("point, pop up or animate, even when it is in the book, 최상으로"): the fine map of each Handbook page for
// Read & listen. Every word on the page with its box, and every keyboard picture with its keys (white and black, each
// with its letter when the picture prints one). Boxes are fractions of the page. Usage: node pagemarks.js pitch [pages...]
const {chromium}=require('playwright'); const fs=require('fs');
const POPS=process.argv[2]==='--pops'; if(POPS) process.argv.splice(2,1);
const part=process.argv[2]||'pitch'; const want=new Set(process.argv.slice(3));
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:900,height:1200}});
const FILE=part.endsWith('.html');
if(FILE){await p.goto('file://'+part);await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(1500);}
else if(POPS){await p.setViewportSize({width:760,height:1000});await p.goto('file:///tmp/claude-0/pk/pops_'+part+'.html');await p.evaluate(()=>document.fonts.ready);}
else{await p.goto('file:///mnt/user-data/outputs/pilot/'+part+'-pilot.html');await p.waitForFunction(()=>document.body.dataset.fit,null,{timeout:90000});}
const OUT=await p.evaluate(([want,POPS])=>{const R={};
 for(const s of document.querySelectorAll(POPS?'section.pop':'section.mk,section.pg')){const pg=POPS?'pop:'+s.id:s.querySelector('.foot span').textContent.trim(); if(want.length&&!want.includes(pg)) continue;
  const S=s.getBoundingClientRect(); const fr=r=>[(r.left-S.left)/S.width,(r.top-S.top)/S.height,r.width/S.width,r.height/S.height].map(v=>+v.toFixed(4));
  const fw=s.querySelector('.fitw')||s; const words=[]; let bi=0;
  // words, block by block (a block = the nearest p / li / td / h1 / h3 / .lead / box line), in reading order
  // every text node outside the pictures' svg, grouped by its block (p, li, td, heading, caption, or the nearest element)
  const groups=new Map(); const tw=document.createTreeWalker(fw,NodeFilter.SHOW_TEXT); let n;
  while((n=tw.nextNode())){ const pe=n.parentElement; if(!pe||pe.closest('svg,style,script,.top,.foot,.plinks,.links')||!n.textContent.trim()) continue; if(getComputedStyle(pe).visibility==='hidden') continue;
   const blk=pe.closest('p,li,td,th,h1,h2,h3,h4,figcaption')||pe; if(!groups.has(blk)) groups.set(blk,[]); groups.get(blk).push(n);}
  for(const [el,nodes] of groups){const ws=[];
   for(const n of nodes){const t=n.textContent; const re=/[A-Za-z0-9♯♭’'-]+/g; let m;
    while((m=re.exec(t))){const rg=document.createRange(); rg.setStart(n,m.index); rg.setEnd(n,m.index+m[0].length); const rs=[...rg.getClientRects()].filter(r=>r.width>0); if(!rs.length) continue;
     ws.push({w:m[0],r:fr(rs[0])});}}
   if(ws.length) words.push({b:bi++,tag:el.tagName.toLowerCase(),cls:String(el.className||''),ws});}
  // keyboards: an svg with five or more tall white rects side by side
  const kbs=[];
  for(const sv of fw.querySelectorAll('svg')){const rects=[...sv.querySelectorAll('rect')].map(r=>({e:r,b:r.getBoundingClientRect(),f:(r.getAttribute('fill')||'').toLowerCase()}));
   const whites=rects.filter(r=>r.b.height>r.b.width*2.2&&r.b.width>3&&r.f&&r.f!=='none'&&!/^#(26296b|1d1f4f|222|000|2a2c6b|1f2160)/.test(r.f)).sort((a,b)=>a.b.left-b.b.left);
   const blacks=rects.filter(r=>r.b.height>r.b.width*2&&r.b.width>2&&/^#(26296b|1d1f4f|222|000|2a2c6b|1f2160)/.test(r.f));
   if(whites.length<3) continue;
   const H=Math.max(...whites.map(w=>w.b.height)); const ws2=whites.filter(w=>w.b.height>H*0.8);
   const texts=[...sv.querySelectorAll('text')].map(t=>({t:t.textContent.trim(),b:t.getBoundingClientRect()})).filter(t=>/^[A-G][♯♭#b]?$/.test(t.t));
   const keyOf=(bx)=>{const cx=bx.left+bx.width/2; const lab=texts.find(t=>{const tx=t.b.left+t.b.width/2;return Math.abs(tx-cx)<bx.width*0.45&&t.b.top>bx.top+bx.height*0.4&&t.b.top<bx.bottom+bx.height*0.35;});return lab?lab.t:null;};
   const tags=[...sv.querySelectorAll('text')].map(t=>({t:t.textContent.trim(),b:t.getBoundingClientRect()})).filter(t=>/^(Very High|Very Low|Lowest|Highest|Middle|Bass|Treble|Low|High) C$/.test(t.t));
   const tagOf=(bx)=>{const cx=bx.left+bx.width/2; const g=tags.filter(t=>t.b.top>bx.bottom-bx.height*0.15&&t.b.top<bx.bottom+bx.height*0.9).sort((a,b)=>Math.abs(a.b.left+a.b.width/2-cx)-Math.abs(b.b.left+b.b.width/2-cx))[0]; return g&&Math.abs(g.b.left+g.b.width/2-cx)<Math.max(bx.width*0.6,6)?g.t:null;};
   kbs.push({r:fr(sv.getBoundingClientRect()),white:ws2.map(w=>({r:fr(w.b),n:keyOf(w.b),tag:tagOf(w.b)})),black:blacks.map(k=>({r:fr(k.b)}))});}
  // staff notes: staves are five evenly spaced long horizontal lines; noteheads are SMuFL noteheads (Verovio) or ellipses;
  // the pitch comes from the step above the bottom line and the clef (G, F) sitting on that staff
  const notes=[];
  for(const sv of fw.querySelectorAll('svg')){if(sv.parentElement.closest('svg')) continue; const SB=sv.getBoundingClientRect(); if(SB.height<30) continue;
   const hl=[...sv.querySelectorAll('line,path,rect,polyline')].map(e=>e.getBoundingClientRect()).filter(b=>b.width>Math.max(40,SB.width*0.25)&&b.height<3.2).map(b=>({y:b.top+b.height/2,x0:b.left,x1:b.right}));
   hl.sort((a,b)=>a.y-b.y); const ys=[]; for(const l of hl){ if(!ys.length||l.y-ys[ys.length-1].y>1.2) ys.push(l); }
   const staves=[]; let i=0;
   while(i+4<ys.length){const g=ys.slice(i,i+5); const d=g.slice(1).map((l,k)=>l.y-g[k].y); const m=d.reduce((a,b)=>a+b)/4;
    if(m>2&&d.every(x=>Math.abs(x-m)<m*0.18)&&g.every(l=>Math.abs(l.x0-g[0].x0)<m*2)){staves.push({top:g[0].y,bot:g[4].y,sp:m,x0:Math.min(...g.map(l=>l.x0)),x1:Math.max(...g.map(l=>l.x1))});i+=5;} else i++;}
   if(!staves.length) continue;
   const glyph=(el)=>{const h=(el.getAttribute('xlink:href')||el.getAttribute('href')||'');return h.slice(1,5);};
   const clefs=[...sv.querySelectorAll('use,text')].map(e=>{const g=e.tagName==='use'?glyph(e):'';const t=e.tagName==='text'?e.textContent:'';const k=(g==='E050'||t.includes('𝄞')||t.includes(''))?'G':(g==='E062'||t.includes('𝄢')||t.includes(''))?'F':null;return k?{k,b:e.getBoundingClientRect()}:null;}).filter(Boolean);
   staves.forEach((st,k)=>{const c=clefs.find(c=>{const cy=c.b.top+c.b.height/2;return cy>st.top-st.sp*2&&cy<st.bot+st.sp*2;}); st.clef=c?c.k:(staves.length===2?(k===0?'G':'F'):'G'); st.known=!!c;});
   const heads=[...sv.querySelectorAll('use,ellipse,text')].filter(e=>{if(e.tagName==='use') return /^E0A[0-4]$/.test(glyph(e)); if(e.tagName==='ellipse'){const b=e.getBoundingClientRect(); return b.width>2&&b.width<staves[0].sp*2.6&&b.height<staves[0].sp*1.6;} return /[-]/.test(e.textContent);});
   const accs=[...sv.querySelectorAll('use,text')].map(e=>{const g=e.tagName==='use'?glyph(e):'';const t=e.tagName==='text'?e.textContent.trim():'';const a=(g==='E262'||t==='♯'||t==='\uE262')?'#':(g==='E260'||t==='♭'||t==='\uE260')?'b':(g==='E261'||t==='♮'||t==='\uE261')?'n':null;return a?{a,b:e.getBoundingClientRect()}:null;}).filter(Boolean);
   for(const h of heads){const b=h.getBoundingClientRect(); const cx=b.left+b.width/2, cy=b.top+b.height/2;
    const ac=accs.find(a=>a.b.right<=b.left+2&&b.left-a.b.right<b.width*1.6&&a.b.top<cy&&a.b.bottom>cy); const acc=ac&&ac.a!=='n'?ac.a:'';
    const st=staves.reduce((best,s)=>{const d=cy<s.top?s.top-cy:cy>s.bot?cy-s.bot:0;return !best||d<best.d?{s,d}:best;},null).s;
    if(cx<st.x0-st.sp||cx>st.x1+st.sp) continue;
    const step=Math.round((st.bot-cy)/(st.sp/2)); const base=st.clef==='F'?18:30; const n=base+step;
    if(notes.some(o=>o.sv===SB&&Math.abs(o.x-cx)<st.sp*0.5&&Math.abs(o.cy-cy)<st.sp*0.35)) continue;
    notes.push({sv:SB,cy,r:fr(b),acc,n:'CDEFGAB'[((n%7)+7)%7],o:Math.floor(n/7),st:staves.indexOf(st),clef:st.clef,known:st.known,x:cx});}}
  notes.sort((a,b)=>a.x-b.x); notes.forEach(n=>{delete n.x;delete n.sv;delete n.cy;});
  R[pg]={words,kbs,notes};}
 return R;},[[...want],POPS]);
const F='/tmp/claude-0/pk/pagemarks.json'; const all=fs.existsSync(F)?JSON.parse(fs.readFileSync(F)):{}; Object.assign(all,OUT); fs.writeFileSync(F,JSON.stringify(all));
for(const [pg,v] of Object.entries(OUT)) console.log(pg,'blocks',v.words.length,'words',v.words.reduce((a,b)=>a+b.ws.length,0),'notes',(v.notes||[]).map(n=>n.n+(n.acc||'')+n.o).join(' ').slice(0,80),'keyboards',v.kbs.map(k=>k.white.length+'w/'+k.black.length+'b labels:'+k.white.map(w=>w.n||'.').join('')).join(' | '));
await b.close();})();
