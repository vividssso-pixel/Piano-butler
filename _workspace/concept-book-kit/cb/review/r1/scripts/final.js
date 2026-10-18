// Final checks on the current build: what overflows at 320px, the "By the end" list text, and the same tool route on the shipped t484 for comparison.
const { start } = require('/home/claude/pbtest/kit/contentharness');
(async () => {
  for (const build of ['drills.t485.html', 'drills.t484.html']) {
    const H = await start(build);
    for (const path of (build.includes('485') ? ['?teacher=1&tool=cb-p-scales', '?teacher=1&tool=scale-finder'] : ['?teacher=1&tool=scale-finder'])) {
      const p = await H.open({ path, w: 320, h: 800 });
      await p.waitForTimeout(900);
      const r = await p.evaluate(() => { const W = document.documentElement.clientWidth, out = []; document.querySelectorAll('body *').forEach(e => { const b = e.getBoundingClientRect(); if (b.width && b.right > W + 1) out.push(e.tagName + '.' + (e.className && e.className.baseVal === undefined ? e.className : '') + ' r=' + Math.round(b.right) + ' "' + (e.innerText || '').replace(/\s+/g, ' ').slice(0, 50) + '"'); }); return [document.documentElement.scrollWidth, out.slice(0, 6)]; });
      console.log(build, path, JSON.stringify(r));
      if (path.includes('cb-p')) { const by = await p.evaluate(() => { const h = [...document.querySelectorAll('.lb-toc-h')].find(e => /By the end/.test(e.textContent)); return h ? [...h.parentElement.children].slice(1).map(d => d.innerText.slice(0, 40)) : null; }); console.log('  by the end:', JSON.stringify(by)); }
      await p.context().close();
    }
    await H.close();
  }
})();
