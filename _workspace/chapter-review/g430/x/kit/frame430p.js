// printed books: the frame is still there and sits inside its box (also on a zoomed page)
const { start } = require('./contentharness');
(async () => {
  let tot = 0, bad = 0;
  for (const B of ['drills.t429.html', 'drills.t430.html']) { const H = await start(B);
    for (const ch of 'posture-hands,first-steps,note-names,staff,whole-staff,ledger-lines'.split(',')) for (const z of [1, 1.12]) {
      const p = await H.open({ path: '?book=lesson&ch=' + ch + '&lang=en', w: 1280, h: 1000 });
      if (z !== 1) { await p.evaluate(z => { document.documentElement.style.zoom = z; }, z); await p.setViewportSize({ width: 1300, height: 1000 }); await p.waitForTimeout(400);
        await p.evaluate(() => document.querySelectorAll('.lb-pic').forEach(b => { b.style.paddingTop = (parseFloat(getComputedStyle(b).paddingTop) + 1) + 'px'; })); await p.waitForTimeout(400); }
      const r = await p.evaluate(() => [...document.querySelectorAll('.lb-pic')].map(b => { const bb = b.getBoundingClientRect(); const f = b.querySelector(':scope > svg[aria-hidden] path'); if (!f) return { f: 0 }; const fb = f.getBoundingClientRect(); return { f: 1, out: fb.right > bb.right - 2 || fb.bottom > bb.bottom - 2 || fb.left < bb.left + 2 }; }));
      const o = r.filter(x => x.out).length; if (B.includes('430')) { tot += r.length; bad += o + r.filter(x => !x.f).length; }
      console.log(B, ch, 'zoom', z, 'pics', r.length, 'frames', r.filter(x => x.f).length, 'out', o, p._errs.length ? 'ERR ' + p._errs[0] : '');
      if (ch === 'first-steps' && z === 1) { const b = await p.$('.lb-pic'); await b.screenshot({ path: '/tmp/fp-' + B + '.png' }); }
      await p.close(); }
    await H.close(); }
  console.log('t430 print pics', tot, 'bad', bad);
})();
