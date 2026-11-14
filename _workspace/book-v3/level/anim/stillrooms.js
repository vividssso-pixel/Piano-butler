// print stills: the same scene, simpler (no wallpaper, window, chandelier, panels; fewer notes), cropped under the ceiling band
const {chromium}=require('playwright');const fs=require('fs');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1280,height:720}});
for (const rid of process.argv.slice(2)) { const meta=JSON.parse(fs.readFileSync(`/tmp/claude-0/anim/rooms/${rid}.meta.json`));
  await p.goto(`file:///tmp/claude-0/anim/rooms/${rid}.html`); await p.waitForTimeout(900);
  for (const [k, at] of [['a', meta.at[0]], ['b', meta.at[1]]]) { const svg = await p.evaluate(x=>{ setT(eval(x)); const s=document.getElementById('scene').cloneNode(true); s.removeAttribute('id'); s.setAttribute('viewBox','0 96 1280 624');
      s.querySelectorAll('.deco').forEach(e=>e.remove()); s.querySelectorAll('[id^=nt]').forEach((e,i)=>{ if(i%2) e.remove(); }); return s.outerHTML; }, at);
    fs.writeFileSync(`/tmp/claude-0/anim/rooms/${rid}-print-${k}.svg`, svg); } }
await b.close();})();
