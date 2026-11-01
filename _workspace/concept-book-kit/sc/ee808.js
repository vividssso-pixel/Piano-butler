// Build EE (the rest of call 39, her 20:30 'only the ones better changed'): the staff under the 7th-chord keyboards only.
// The 'of a key' pad keeps its names hidden: no staff before the first key, then each found note joins it, spelt as the
// chips spell it (C♯ E♯ G♯ B for the dominant 7th of F♯); the four positions show the position's five notes; the chromatic
// and arpeggio pads have no staff. Usage: node ee808.js drills.t808.html
const { start } = require('/home/claude/pbtest/kit/contentharness');
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
(async () => {
  const H = await start(process.argv[2] || 'drills.t808.html'); let bad = 0;
  const say = (ok, ...a) => { if (!ok) bad++; console.log(ok ? 'ok  ' : 'BAD ', ...a); };
  for (const lang of ['en', 'ko']) {
    const p = await H.open({ path: '?drill=arps-6', w: 420, h: 1600, dsf: 1, lang }); await sleep(1300);
    await p.locator('section > button').nth(2).click(); await sleep(700);
    const box = p.locator('[data-s7="dom"]').first(), N = await p.evaluate(() => s7Notes('Fs', 'dom'));
    const before = await box.locator('[data-run-staff]').count();
    const tapKey = async (i) => { const pt = await box.evaluate((el, i) => { const svg = [...el.querySelectorAll('svg')].find(s => /Build the chord|화음 쌓기/.test(s.getAttribute('aria-label') || '')); const vb = svg.viewBox.baseVal, r = svg.getBoundingClientRect(), k = r.width / vb.width;
        const a = spIsW(-12) ? -12 : -13, w0 = spWIdx(a), x = 4 + (spWIdx(i) - w0 + (spIsW(i) ? 0.5 : 1)) * 14; return { x: r.left + x * k, y: r.top + (spIsW(i) ? r.height - 12 * k : r.height - 76 * k + 20 * k) }; }, i);
      await p.mouse.click(pt.x, pt.y); await sleep(250); };
    const counts = []; for (const x of N) { await tapKey(x); counts.push(await box.locator('[data-run-staff] ellipse').count()); }
    const items = await p.evaluate(() => spRunItems(s7Notes('Fs', 'dom'), s7Names('Fs', 'dom')));
    say(before === 0 && counts.join() === '1,2,3,4' && JSON.stringify(items.slice(0, 4)) === JSON.stringify([['q', 1, 28, '#'], ['q', 1, 30, '#'], ['q', 1, 32, '#'], ['q', 1, 34]]) && !p._errs.length, lang, 'the dominant 7th of F♯: no staff till the first key, then C♯ E♯ G♯ B one by one', counts.join(), JSON.stringify(items.slice(0, 4)), p._errs.slice(0, 1));
    await p.close();
    const q = await H.open({ path: '?drill=arps-7', w: 420, h: 1600, dsf: 1, lang }); await sleep(1300);
    await q.locator('section > button').nth(2).click(); await sleep(700);
    const inv = await q.locator('[data-a7="inv"] [data-run-staff] ellipse').count();
    const dimItems = await q.evaluate(() => spRunItems(s7Notes('Ab', 'dim'), s7Names('Ab', 'dim')).slice(0, 4).map(x => x[3] || ''));
    say(inv === 5 && dimItems.join() === ',b,b,b' && !q._errs.length, lang, 'the four positions: five notes on the staff; the diminished 7th of A♭ is G B♭ D♭ F♭', inv, dimItems.join(), q._errs.slice(0, 1));
    await q.close();
    const r = await H.open({ path: '?drill=scales-4', w: 420, h: 1600, dsf: 1, lang }); await sleep(1300);
    let n = 0; for (const k of [3, 4]) { await r.locator('section > button').nth(k).click(); await sleep(500); n += await r.locator('[data-run-staff]').count(); await r.locator('section > button').nth(k).click(); await sleep(200); }
    say(n === 0 && !r._errs.length, lang, 'the chromatic and arpeggio pads keep their keyboards alone', n); await r.close();
  }
  console.log('bad', bad); await H.close();
})();
