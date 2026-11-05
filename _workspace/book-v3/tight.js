// Crop chosen snippets in pout.json to their drawn content (+ margin), so grand staves are not lost in empty space. Usage: node tight.js pout.json key1 key2 ...
const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const [f,...keys]=process.argv.slice(2);const P=JSON.parse(fs.readFileSync(f));const b=await chromium.launch();const p=await b.newPage();
for(const k of keys){await p.setContent('<div style="width:900px">'+P[k].replace('<svg ','<svg width="900" ')+'</div>');
 const vb=await p.evaluate(()=>{const s=document.querySelector('svg');const M=s.getScreenCTM().inverse();let x0=1e9,y0=1e9,x1=-1e9,y1=-1e9;
  s.querySelectorAll('g.staff path, use, g.verse text, g.syl text, text tspan').forEach(e=>{const r=e.getBoundingClientRect();if(!r.width&&!r.height)return;[[r.left,r.top],[r.right,r.bottom]].forEach(([x,y])=>{const q=new DOMPoint(x,y).matrixTransform(M);x0=Math.min(x0,q.x);y0=Math.min(y0,q.y);x1=Math.max(x1,q.x);y1=Math.max(y1,q.y);});});
  const m=(y1-y0)*0.06;return [x0-m,y0-m,x1-x0+2*m,y1-y0+2*m].map(v=>v.toFixed(1)).join(' ');});
 const ov=P[k].match(/viewBox="([^"]*)"/)[1].split(' ').map(Number), iv=P[k].match(/class="definition-scale"[^>]*viewBox="([^"]*)"/)[1].split(' ').map(Number), kx=iv[2]/ov[2];
 const [x,y,w,h]=vb.split(' ').map(Number);
 P[k]=P[k].replace(/viewBox="[^"]*"/,'viewBox="0 0 '+w.toFixed(1)+' '+h.toFixed(1)+'"').replace(/(class="definition-scale"[^>]*viewBox=")[^"]*"/,'$1'+[(x-ov[0])*kx,(y-ov[1])*kx,w*kx,h*kx].map(v=>v.toFixed(1)).join(' ')+'"');console.log(k,vb);}
fs.writeFileSync(f,JSON.stringify(P));await b.close();})();
