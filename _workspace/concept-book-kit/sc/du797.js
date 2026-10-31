// Build DU: the Piano's Story's 'Key, hammer, damper' pad (the string shakes, the pedals under it) and the redrawn instruments.
// Usage: node du797.js drills.t797.html
const { start } = require('/home/claude/pbtest/kit/contentharness');
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
(async () => {
  const H = await start(process.argv[2] || 'drills.t797.html'); let bad = 0;
  const say = (ok, ...a) => { if (!ok) bad++; console.log(ok ? 'ok  ' : 'BAD ', ...a); };
  for (const lang of ['en', 'ko']) {
    const p = await H.open({ path: '?drill=piano-story', w: 420, h: 1600, dsf: 1, lang }); await sleep(1500);
    const n = await p.locator('section > button').count(); for (let k = 1; k < n; k++) { if (await p.locator('[data-sps="action"]').count()) break; await p.locator('section > button').nth(k).click(); await sleep(400); }
    const pad = p.locator('[data-sps="action"]'); await pad.scrollIntoViewIfNeeded();
    const pedal = (i) => pad.locator('[data-sps-pedals] svg > g').nth(i + 1).click();   // the first g holds the hatch pattern
    const wob = () => pad.evaluate(e => e.querySelectorAll('.sps-wob').length);
    const hold = pad.locator('[data-sps-hold]'); const bb = await hold.boundingBox();
    // the right pedal down, hold the key, let go: the string keeps shaking; pedal up: it stops
    await pedal(2); await sleep(200);
    await p.mouse.move(bb.x + bb.width / 2, bb.y + bb.height / 2); await p.mouse.down(); await sleep(350);
    const during = await wob(); await p.mouse.up(); await sleep(350); const after = await wob();
    await pedal(2); await sleep(300); const off = await wob();
    // without the pedal, letting go stops it
    await p.mouse.move(bb.x + bb.width / 2, bb.y + bb.height / 2); await p.mouse.down(); await sleep(300); const d2 = await wob(); await p.mouse.up(); await sleep(300); const a2 = await wob();
    // the left pedal: two of three strings
    await pedal(0); await sleep(250); const una = await pad.innerText();
    say(during === 1 && after === 1 && off === 0 && d2 === 1 && a2 === 0 && /2 strings|현 2줄/.test(una) && !p._errs.length, lang, 'the string shakes; the right pedal keeps it; una corda: two strings', JSON.stringify([during, after, off, d2, a2]), p._errs.slice(0, 1));
    await p.close();
  }
  // the redrawn instruments: in the book's pictures, with their hatch patterns, and nothing overflows
  const b = await H.open({ path: '?book=lesson&ch=piano-story', w: 900, h: 1300, dsf: 1 }); await sleep(2000);
  const r = await b.evaluate(() => ({ pats: document.querySelectorAll('pattern[id^="pbinst"]').length, over: [...document.querySelectorAll('.bk-page')].map(pg => pg.scrollHeight - pg.clientHeight) }));
  say(r.pats >= 6 && r.over.every(x => x <= 2) && !b._errs.length, 'the book draws the new instruments, no overflow', JSON.stringify(r), b._errs.slice(0, 1));
  await b.close();
  const q = await H.open({ path: '?book=lesson&ch=piano-story-8', w: 900, h: 1300, dsf: 1 }); await sleep(2000);
  const r8 = await q.evaluate(() => ({ pats: document.querySelectorAll('pattern[id^="pbinst"]').length, over: [...document.querySelectorAll('.bk-page')].map(pg => pg.scrollHeight - pg.clientHeight) }));
  say(r8.pats >= 3 && r8.over.every(x => x <= 2) && !q._errs.length, 'the diploma room draws the new fronts', JSON.stringify(r8), q._errs.slice(0, 1));
  await q.close();
  // the Scale finder inside a scales room: closed, then open with its keyboard
  for (const ch of ['scales-3', 'scales', 'arps-7']) { const f = await H.open({ path: '?drill=' + ch, w: 420, h: 1400, dsf: 1 }); await sleep(1300);
    const n0 = await f.locator('[data-sf-hands]').count(); await f.locator('[data-lesson-finder] > button').click(); await sleep(700);
    const n1 = await f.locator('[data-lesson-finder] [data-sf-hands]').count();
    say(n0 === 0 && n1 === 1 && !f._errs.length, ch, 'the Scale finder in the chapter', n0, n1, f._errs.slice(0, 1)); await f.close(); }
  console.log('bad', bad); await H.close();
})();
