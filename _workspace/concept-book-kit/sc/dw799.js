// Build DW (call 40): every make-it toy opens inside the step that teaches it; no MAKE YOUR OWN end card; nothing overflows.
// Usage: node dw799.js drills.t799.html [ko]
const { start } = require('/home/claude/pbtest/kit/contentharness');
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
(async () => {
  const H = await start(process.argv[2] || 'drills.t799.html'); let bad = 0; const lang = process.argv[3] || 'en';
  const say = (ok, ...a) => { if (!ok) bad++; console.log(ok ? 'ok  ' : 'BAD ', ...a); };
  const p0 = await H.open({ path: '?view=path', w: 420, h: 900, dsf: 1 }); await sleep(900);
  const at = await p0.evaluate(() => MAKE_AT); await p0.close();
  for (const [room, steps] of Object.entries(at)) {
    const p = await H.open({ path: '?drill=' + room, w: 400, h: 1400, dsf: 1, lang }); await sleep(900);
    const endCard = await p.locator('[data-make]').count();
    for (const [k, ids] of Object.entries(steps)) {
      if (+k > 0) { await p.locator('section > button').nth(+k).click(); await sleep(700); }
      for (const id of ids) {
        const box = p.locator('section').nth(+k).locator('[data-step-make="' + id + '"]');
        const n = await box.count();
        const r = n ? await box.evaluate(e => { const b = e.getBoundingClientRect(); return { h: Math.round(b.height), w: Math.round(b.width), sw: e.scrollWidth, cw: e.clientWidth, page: document.scrollingElement.scrollWidth }; }) : null;
        const title = await p.locator('section').nth(+k).locator(':scope > button').innerText().catch(() => '?');
        say(n === 1 && endCard === 0 && r && r.h > 60 && r.sw <= r.cw + 2 && r.page <= 402 && !p._errs.length, room, 'step', +k + 1, title.split('\n').pop(), id, JSON.stringify(r), p._errs.slice(0, 1));
      }
    }
    await p.close();
  }
  // back from a tool lands in the chapter again (it used to find the end card)
  const b = await H.open({ path: '?tool=black-key-jam&from=first-steps', w: 390, h: 1000 }); await sleep(600);
  const bt = b.locator('[data-testid="tool-back"]'); const txt = await bt.count() ? (await bt.innerText()).trim() : '(none)';
  if (await bt.count()) { await bt.click(); await sleep(800); }
  const inRoom = await b.evaluate(() => /Keyboard Patterns|Small house, big house/.test(document.body.innerText));
  say(/Keyboard Patterns/.test(txt) && inRoom && !b._errs.length, 'back from a tool', txt, inRoom); await b.close();
  console.log('bad', bad); await H.close();
})();
