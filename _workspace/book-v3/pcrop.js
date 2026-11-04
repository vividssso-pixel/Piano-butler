// Content box of each pitch snippet (outer viewBox units), so small figures can be cropped and drawn larger.
const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const b=await chromium.launch();const p=await b.newPage();const P=JSON.parse(fs.readFileSync(process.argv[2]));const out={};
for(const [k,svg] of Object.entries(P)){ if(!svg.startsWith('<svg')) continue;
 await p.setContent('<div style="width:800px">'+svg.replace('<svg ','<svg width="800" ')+'</div>');
 out[k]=await p.evaluate(()=>{const s=document.querySelector('svg');const vb=s.viewBox.baseVal;const R=s.getBoundingClientRect();const kk=vb.width/R.width;
  let x0=1e9,y0=1e9,x1=-1e9,y1=-1e9;s.querySelectorAll('g.system, text, g.verse, g.harm, g.dir, path, use').forEach(e=>{const q=e.getBoundingClientRect();if(!q.width&&!q.height)return;x0=Math.min(x0,q.left);y0=Math.min(y0,q.top);x1=Math.max(x1,q.right);y1=Math.max(y1,q.bottom)});
  const inner=s.querySelector('svg.definition-scale');return {vb:[vb.width,vb.height],box:[(x0-R.left)*kk,(y0-R.top)*kk,(x1-x0)*kk,(y1-y0)*kk],ivb:inner?inner.getAttribute('viewBox'):null}});}
fs.writeFileSync(process.argv[3],JSON.stringify(out));await b.close();console.log(Object.keys(out).length)})();
