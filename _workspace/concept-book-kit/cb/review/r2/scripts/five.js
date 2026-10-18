const { start } = require('/home/claude/pbtest/kit/contentharness');
const OUT = '/home/claude/pbtest/cb/review/r2/shots/';
(async () => {
  for (const b of ['drills.t484.html', 'drills.t485.html']) {
    const H = await start(b);
    for (const r of ['?teacher=1&drill=scales&tab=learn', '?teacher=1&drill=posture-hands&tab=learn', '?teacher=1&drill=key-signatures&tab=learn', '?tool=cb-p-scales&lock=1']) for (const lang of ['en', 'ko']) for (const w of [320, 360, 390]) {
      const p = await H.open({ path: r, w, h: 800, lang, dsf: 1.5 }); await p.waitForTimeout(1200);
      for (let k = 0; k < 15; k++) { const hd = await p.$$('[aria-expanded="false"]'); if (!hd.length) break; try { await hd[hd.length - 1].click({ timeout: 800 }); } catch (e) { break; } await p.waitForTimeout(120); }
      const o = await p.evaluate((vw) => { const bts = [...document.querySelectorAll('button')].filter(bt => /^\W*(Got it!|됐어요!)\s*$/.test(bt.innerText.trim()));
        return bts.map(bt => { const row = bt.parentElement.parentElement, rb = row.getBoundingClientRect(), bb = bt.getBoundingClientRect(); return Math.round(bb.right - rb.right) + '/' + Math.round(bb.right - vw) + '/h' + Math.round(bb.height); }); }, w);
      console.log(b.slice(8, 12), lang, w, r, 'gotit right-past-row/past-viewport:', [...new Set(o)].join(' ') || 'none');
      if (w === 320 && lang === 'en' && /scales&tab/.test(r)) { const g = await p.$('button:has-text("Got it!")'); if (g) { await g.scrollIntoViewIfNeeded(); await p.screenshot({ path: OUT + 'five-' + b.slice(8, 12) + '-ch16-320.png' }); } }
      await p.context().close();
    }
    await H.close();
  }
})();
