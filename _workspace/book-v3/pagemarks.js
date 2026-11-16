// Her 16 Nov ("point, pop up or animate, even when it is in the book, 최상으로"): the fine map of each Handbook page for
// Read & listen. Every word on the page with its box, and every keyboard picture with its keys (white and black, each
// with its letter when the picture prints one). Boxes are fractions of the page. Usage: node pagemarks.js pitch [pages...]
const {chromium}=require('playwright'); const fs=require('fs');
const POPS=process.argv[2]==='--pops'; if(POPS) process.argv.splice(2,1);
const part=process.argv[2]||'pitch'; const want=new Set(process.argv.slice(3));
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:900,height:1200}});
if(POPS){await p.setViewportSize({width:760,height:1000});await p.goto('file:///tmp/claude-0/pk/pops_'+part+'.html');await p.evaluate(()=>document.fonts.ready);}
else{await p.goto('file:///mnt/user-data/outputs/pilot/'+part+'-pilot.html');await p.waitForFunction(()=>document.body.dataset.fit,null,{timeout:90000});}
const OUT=await p.evaluate(([want,POPS])=>{const R={};
 for(const s of document.querySelectorAll(POPS?'section.pop':'section.mk')){const pg=POPS?'pop:'+s.id:s.querySelector('.foot span').textContent.trim(); if(want.length&&!want.includes(pg)) continue;
  const S=s.getBoundingClientRect(); const fr=r=>[(r.left-S.left)/S.width,(r.top-S.top)/S.height,r.width/S.width,r.height/S.height].map(v=>+v.toFixed(4));
  const fw=s.querySelector('.fitw')||s; const words=[]; let bi=0;
  // words, block by block (a block = the nearest p / li / td / h1 / h3 / .lead / box line), in reading order
  // every text node outside the pictures' svg, grouped by its block (p, li, td, heading, caption, or the nearest element)
  const groups=new Map(); const tw=document.createTreeWalker(fw,NodeFilter.SHOW_TEXT); let n;
  while((n=tw.nextNode())){ const pe=n.parentElement; if(!pe||pe.closest('svg,style,script')||!n.textContent.trim()) continue; if(getComputedStyle(pe).visibility==='hidden') continue;
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
   kbs.push({r:fr(sv.getBoundingClientRect()),white:ws2.map(w=>({r:fr(w.b),n:keyOf(w.b)})),black:blacks.map(k=>({r:fr(k.b)}))});}
  R[pg]={words,kbs};}
 return R;},[[...want],POPS]);
const F='/tmp/claude-0/pk/pagemarks.json'; const all=fs.existsSync(F)?JSON.parse(fs.readFileSync(F)):{}; Object.assign(all,OUT); fs.writeFileSync(F,JSON.stringify(all));
for(const [pg,v] of Object.entries(OUT)) console.log(pg,'blocks',v.words.length,'words',v.words.reduce((a,b)=>a+b.ws.length,0),'keyboards',v.kbs.map(k=>k.white.length+'w/'+k.black.length+'b labels:'+k.white.map(w=>w.n||'.').join('')).join(' | '));
await b.close();})();
