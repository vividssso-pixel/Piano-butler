// Screen lesson in readable chunks: every step (and the opener) cut into 800 px tall pieces.
// SCR=en:390,ko:390  ONLY=2,3 (step numbers; 'top' = the opener)
const { start } = require('/home/claude/pbtest/kit/contentharness');
const OUT = '/home/claude/pbtest/cb/review/r2/shots/';
(async () => {
  const H = await start('drills.t485.html');
  const only = process.env.ONLY ? process.env.ONLY.split(',') : null;
  const path = process.env.PATH_Q || '?teacher=1&tool=cb-p-scales';
  for (const [lang, w] of (process.env.SCR || 'en:390,ko:390').split(',').map(x => x.split(':'))) {
    const p = await H.open({ path, w: +w, h: 900, lang, dsf: 1.5 });
    await p.waitForTimeout(1500);
    const total = await p.evaluate(() => document.documentElement.scrollHeight);
    // the opener: from the top to the first step
    const firstStep = await p.$('[data-lb-screen]');
    const fs = firstStep ? (await firstStep.boundingBox()).y : 1600;
    const parts = [['top', 0, fs]];
    for (const s of await p.$$('[data-lb-screen]')) { const n = await s.getAttribute('data-lb-screen'); const b = await s.boundingBox(); parts.push([n, b.y - 60, b.y + b.height]); }
    for (const [n, y0, y1] of parts) {
      if (only && !only.includes(String(n))) continue;
      let k = 0;
      for (let y = Math.max(0, y0); y < y1; y += 800, k++) {
        await p.screenshot({ path: OUT + 'c-' + lang + w + '-' + n + '-' + k + '.png', fullPage: true, clip: { x: 0, y, width: +w, height: Math.min(800, y1 - y, total - y) } });
      }
    }
    console.log(lang, w, 'parts', parts.map(x => x[0] + ':' + Math.round(x[2] - x[1])).join(' '), 'errs', p._errs.join('|'));
    await p.context().close();
  }
  await H.close();
})();
