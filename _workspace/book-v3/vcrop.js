// Tight crop of each workbook snippet (staff, clef, notes) with an even margin; records the true staff height (data-sh, in viewBox units).
const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const b=await chromium.launch();const p=await b.newPage();const W=JSON.parse(fs.readFileSync(process.argv[2]));const out={};
for(const [k,svg] of Object.entries(W)){ if(!svg.startsWith('<svg')){out[k]=svg;continue;}
 await p.setContent('<body style="margin:0">'+svg+'</body>');
 const r=await p.evaluate((K)=>{const s=document.querySelector('svg');const v=s.viewBox.baseVal;s.setAttribute('width',v.width*4);s.setAttribute('height',v.height*4);
  const R=s.getBoundingClientRect();const kx=v.width/R.width,ky=v.height/R.height;
  let x0=1e9,x1=-1e9,y0=1e9,y1=-1e9,s0=1e9,s1=-1e9;
  let n1=-1e9;s.querySelectorAll('path, use, text, rect, ellipse, polygon').forEach(e=>{if(e.closest('defs,symbol'))return;const q=e.getBoundingClientRect();if(!q.width&&!q.height)return;x0=Math.min(x0,q.left);x1=Math.max(x1,q.right);y0=Math.min(y0,q.top);y1=Math.max(y1,q.bottom);if(!e.parentNode.matches('g.staff'))n1=Math.max(n1,q.right)});
  if(K.startsWith('blank')) x1=Math.min(x1,x0+(y1-y0)*2.4);   // a blank staff only needs room for the clef and one note
  if(n1>-1e9 && s.querySelector('g.note, g.chord') && !K.startsWith('up')) x1=Math.min(x1,n1+ (y1-y0)*0.25);   // end the staff a little after the last sign, so the picture is not mostly empty lines
  s.querySelectorAll('g.staff > path').forEach(e=>{const q=e.getBoundingClientRect();s0=Math.min(s0,q.top);s1=Math.max(s1,q.bottom)});
  const t=u=>[v.x+(u[0]-R.left)*kx,v.y+(u[1]-R.top)*ky];const a=t([x0,y0]),c=t([x1,y1]);return [a[0],a[1],c[0],c[1],(s1-s0)*ky]},k);
 const [ax,ay,cx,cy,sh]=r; const m=sh>0?sh*0.35:(cy-ay)*0.14;
 out[k]=svg.replace('<svg ',`<svg data-sh="${sh>0?sh.toFixed(2):0}" `).replace(/viewBox="[^"]*"/,`viewBox="${(ax-m).toFixed(1)} ${(ay-m).toFixed(1)} ${(cx-ax+2*m).toFixed(1)} ${(cy-ay+2*m).toFixed(1)}"`);}
fs.writeFileSync(process.argv[3],JSON.stringify(out));await b.close();console.log(Object.keys(out).length)})();
