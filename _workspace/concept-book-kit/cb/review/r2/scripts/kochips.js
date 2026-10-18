const { start } = require('/home/claude/pbtest/kit/contentharness');
const OUT = '/home/claude/pbtest/cb/review/r2/shots/';
(async () => {
  const H = await start('drills.t485.html');
  for (const w of [320, 360]) for (const lang of ['ko', 'en']) {
    const p = await H.open({ path: '?tool=cb-p-scales&lock=1', w, h: 860, lang, dsf: 2 }); await p.waitForTimeout(1300);
    const sp = (await p.$$('[data-cb="shapes-pad"]'))[0]; await sp.scrollIntoViewIfNeeded();
    const chips = await sp.evaluate(el => [...el.querySelectorAll('button')].slice(0, 3).map(b => { const r = b.getBoundingClientRect(); return b.innerText.replace(/\n/g, '/') + ' ' + Math.round(r.width) + 'x' + Math.round(r.height); }));
    const box = await sp.boundingBox(); await p.screenshot({ path: OUT + 'kochips-' + lang + w + '.png', clip: { x: box.x, y: box.y, width: box.width, height: 180 } });
    const so = await p.$('[data-cb-tool="sharps-order"]'); await so.scrollIntoViewIfNeeded();
    const btns = await so.evaluate(el => [...el.querySelectorAll('button')].map(b => { const r = b.getBoundingClientRect(); return b.innerText.replace(/\n/g, '/') + ' ' + Math.round(r.width) + 'x' + Math.round(r.height); }));
    const bb = await so.boundingBox(); await p.screenshot({ path: OUT + 'sobtn-' + lang + w + '.png', clip: { x: bb.x, y: bb.y + bb.height - 140, width: bb.width, height: 140 } });
    console.log(lang, w, 'shape chips', JSON.stringify(chips), 'order buttons', JSON.stringify(btns));
    await p.context().close();
  }
  await H.close();
})();
