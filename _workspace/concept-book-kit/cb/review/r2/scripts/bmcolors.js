const { start } = require('/home/claude/pbtest/kit/contentharness');
(async () => {
  for (const b of ['drills.t484.html', 'drills.t485.html']) {
    const H = await start(b);
    for (const path of ['?tool=cb-p-scales&lock=1', '?teacher=1&tool=build-major']) {
      if (b.includes('484') && path.includes('cb-p')) continue;
      const p = await H.open({ path, w: 390, h: 860, dsf: 1 }); await p.waitForTimeout(1300);
      const r = await p.evaluate(() => { const bm = document.querySelector('[data-cb-tool="build-major"]') || document.querySelector('.pb-main');
        const chips = [...bm.querySelectorAll('button')].slice(0, 8).map(x => { const cs = getComputedStyle(x); return x.innerText.trim() + ':' + cs.borderTopColor + '/' + cs.backgroundColor + '/h' + Math.round(x.getBoundingClientRect().height); });
        const rects = [...bm.querySelectorAll('svg rect')].map(r => r.getAttribute('fill') || getComputedStyle(r).fill); const cnt = {}; rects.forEach(f => cnt[f] = (cnt[f] || 0) + 1);
        const box = bm.closest('.try-box') || bm; const cs = getComputedStyle(box);
        return { chips, rectFills: cnt, box: cs.backgroundColor + ' ' + cs.borderTopColor }; });
      console.log(b, path, JSON.stringify(r));
      await p.context().close();
    }
    await H.close();
  }
})();
