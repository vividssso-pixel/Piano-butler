const { start } = require('/home/claude/pbtest/kit/contentharness');
(async () => {
  const H = await start('drills.t485.html');
  for (const [lang, w] of [['en', 390], ['en', 320], ['ko', 390]]) {
    const p = await H.open({ path: '?teacher=1&tool=cb-p-scales', w, h: 860, lang, dsf: 1 }); await p.waitForTimeout(1200);
    const res = await p.evaluate(() => {
      const out = [];
      document.querySelectorAll('.pb-main svg text, .pb-main svg tspan').forEach(t => { if (!t.textContent.trim()) return; const svg = t.ownerSVGElement; const m = t.getScreenCTM(); if (!m) return;
        const fs = parseFloat(getComputedStyle(t).fontSize); const px = fs * Math.hypot(m.a, m.b);
        const zone = t.closest('[data-cb],[data-cb-tool],[data-lb-screen]'); const z = zone ? (zone.getAttribute('data-cb') || zone.getAttribute('data-cb-tool') || 'step' + zone.getAttribute('data-lb-screen')) : 'head';
        out.push([+px.toFixed(1), t.textContent.trim().slice(0, 14), z]); });
      out.sort((a, b) => a[0] - b[0]);
      const byZone = {}; out.forEach(o => { if (o[0] < 11) { byZone[o[2]] = byZone[o[2]] || []; if (byZone[o[2]].length < 6) byZone[o[2]].push(o[0] + ' ' + o[1]); } });
      return { n: out.length, under11: out.filter(o => o[0] < 11).length, byZone };
    });
    console.log(lang, w, JSON.stringify(res));
    await p.context().close();
  }
  await H.close();
})();
