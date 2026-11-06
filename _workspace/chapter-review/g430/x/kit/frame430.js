// Is every .lb-pic frame inside its box? (online: .pb-main is zoomed 1.12 at >= 900px)
const { start } = require('./contentharness');
(async () => {
  const H = await start(process.env.BUILD || 'drills.t429.html'); let bad = 0, n = 0, frames = 0;
  for (const w of [390, 1280]) for (const ch of 'posture-hands,first-steps,note-names,staff,whole-staff,ledger-lines'.split(',')) {
    const p = await H.open({ path: '?drill=' + ch, w, h: 1000 });
    const r = await p.evaluate(() => [...document.querySelectorAll('.lb-pic')].map(b => { const bb = b.getBoundingClientRect(); const f = b.querySelector(':scope > svg[aria-hidden] path'); if (!f) return { f: 0 }; const fb = f.getBoundingClientRect(); return { f: 1, out: fb.right > bb.right + 0.5 || fb.bottom > bb.bottom + 0.5 }; }));
    const o = r.filter(x => x.out).length; n += r.length; frames += r.filter(x => x.f).length; bad += o;
    if (process.env.SHOT && w === 1280 && ch === 'first-steps') { const b = await p.$('.lb-pic'); if (b) await b.screenshot({ path: '/tmp/frame-' + ch + '.png' }); }
    console.log(w, ch, 'pics', r.length, 'frames', r.filter(x => x.f).length, 'out of box', o, p._errs.length ? 'ERR ' + p._errs[0] : '');
    await p.close();
  }
  console.log('TOTAL pics', n, 'frames', frames, 'out', bad); await H.close();
})();
