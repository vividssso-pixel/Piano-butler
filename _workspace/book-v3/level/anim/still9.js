const {chromium}=require('playwright');const fs=require('fs');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1280,height:720}});
await p.goto('file:///tmp/claude-0/anim/film9.html');await p.waitForTimeout(1200);
// her 14 Nov: the printed book stays as simple as possible: the same scene without the wallpaper, window, chandelier and panels, and fewer notes
for (const [t, nm] of [[28, 's9a'], [82, 's9b']]) { const svg = await p.evaluate(x=>{setT(x); const s=document.getElementById('scene').cloneNode(true); s.removeAttribute('id'); s.setAttribute('viewBox','0 44 1280 676');
  s.querySelectorAll('.deco').forEach(e=>e.remove()); s.querySelectorAll('[id^=nt]').forEach((e,i)=>{ if(i%2) e.remove(); }); return s.outerHTML;}, t); fs.writeFileSync(`/tmp/claude-0/anim/${nm}.svg`, svg); }
await b.close();})();
