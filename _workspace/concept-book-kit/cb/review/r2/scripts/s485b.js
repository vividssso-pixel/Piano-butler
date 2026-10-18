const { start } = require('/home/claude/pbtest/kit/contentharness');
const OUT = '/home/claude/pbtest/cb/review/r2/shots/orig/';
(async () => {
  const H = await start('drills.t485.html');
  for (const lang of ['en', 'ko']) for (const w of [390, 320]) {
    const p = await H.open({ path: '?teacher=1&tool=cb-p-scales', w, h: 860, lang, dsf: 1.5 }); await p.waitForTimeout(1500);
    const steps = await p.$$('[data-lb-screen]');
    if (w === 390) for (const s of steps) { const n = await s.getAttribute('data-lb-screen'); await s.screenshot({ path: OUT + 'step-' + lang + '-' + n + '.png' }); }
    const kp = await p.$('[data-cb="key-pad"]');
    for (const k of ['Gb', 'B', 'Db']) { const g = await kp.$('g[data-key="' + k + '"]'); if (g) { await g.click(); await p.waitForTimeout(300); } }
    const kpTxt = await kp.evaluate(e => e.innerText.replace(/\s+/g, ' '));
    if (w === 390) await kp.screenshot({ path: OUT + 'pad-key-' + lang + '.png' });
    const pads = await p.$$('[data-cb="shapes-pad"]');
    const out = [];
    for (const [pi, sp] of pads.entries()) {
      const chips = await sp.$$('button.chip');
      const lastChip = chips[pi === 0 ? 1 : 1]; await lastChip.click(); await p.waitForTimeout(200);
      const ab = await sp.$('g[data-key="Ab"]'); if (ab) { await ab.click(); await p.waitForTimeout(400); }
      if (w === 390) await sp.screenshot({ path: OUT + 'pad-shapes' + pi + '-' + lang + '.png' });
      out.push((await sp.evaluate(e => e.innerText.replace(/\s+/g, ' '))).slice(0, 260));
    }
    const hor = await p.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
    console.log(lang, w, 'steps', steps.length, 'pads', pads.length, 'hscroll', hor, '\n  key:', kpTxt.slice(-160), '\n  ', out.join('\n   '), '\n  errs', p._errs.join('|').slice(0, 200));
    await p.context().close();
  }
  await H.close();
})();
