// Build ED: the Reference takes in the book's whole reference section: twelve tables on screen (the staff and clefs to the
// instruments), doors into rooms, 'extra' on what the house doesn't teach, ♪ sounds; every scale and every chord spelt by
// the code; fifteen A4 pages on paper, nothing over; the Home's Quick line and the Books tab. Usage: node ed807.js drills.t807.html
const { start } = require('/home/claude/pbtest/kit/contentharness');
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
(async () => {
  const H = await start(process.argv[2] || 'drills.t807.html'); let bad = 0;
  const say = (ok, ...a) => { if (!ok) bad++; console.log(ok ? 'ok  ' : 'BAD ', ...a); };
  for (const lang of ['en', 'ko']) {
    const p = await H.open({ path: '?teacher=1&view=home', w: 400, h: 1200, dsf: 1, lang }); await sleep(1100);
    const quick = await p.evaluate(() => [...document.querySelectorAll('[data-testid="home-quick"] [data-quick]')].map(e => e.getAttribute('data-quick')));
    await p.locator('[data-quick="reference"]').click(); await sleep(1500);
    const r = await p.evaluate(() => ({ secs: [...document.querySelectorAll('[data-ref-sec]')].map(e => e.getAttribute('data-ref-sec')), doors: document.querySelectorAll('[data-ref-door]').length,
      extra: document.querySelectorAll('[data-ref-extra]').length, hear: document.querySelectorAll('[data-ref-hear]').length, notes: document.querySelectorAll('[data-ref-table="notes"] svg').length / 2,
      clefs: document.querySelectorAll('[data-ref-clef]').length, ts: document.querySelectorAll('[data-ref-ts]').length, all: document.querySelectorAll('[data-ref-allscale]').length,
      chords: document.querySelectorAll('[data-ref-chord]').length, signs: document.querySelectorAll('[data-ref-sign]').length, words: document.querySelectorAll('[data-ref-word]').length,
      periods: document.querySelectorAll('[data-ref-period]').length, fams: document.querySelectorAll('[data-ref-family]').length, terms: document.querySelectorAll('[data-ref-term]').length,
      blank: [...document.querySelectorAll('[data-ref-term],[data-ref-word]')].filter(b => !b.innerText.trim()).length, w: document.scrollingElement.scrollWidth }));
    say(quick.includes('reference') && r.secs.length === 12 && r.doors > 200 && r.extra > 60 && r.hear > 150 && r.notes === 12 && r.clefs === 4 && r.ts === 21 && r.all === 30 && r.chords === 11 && r.signs === 48
      && r.words > 230 && r.periods === 6 && r.fams === 5 && r.terms === 79 && r.blank === 0 && r.w <= 402 && !p._errs.length, lang, 'the Reference: twelve tables, every part there', JSON.stringify({ quick, ...r, secs: r.secs.join(' ') }), p._errs.slice(0, 1));
    // spelt by the code
    const sp = await p.evaluate(() => { const g = (k) => (document.querySelector('[data-ref-allscale="' + k + '"]') || {}).innerText || ''; return { cs: g('MC♯'), cb: g('MC♭'), as: g('mA♯'), gs: g('mG♯') }; });
    say(/C♯\s*D♯\s*E♯\s*F♯\s*G♯\s*A♯\s*B♯/.test(sp.cs) && /C♭\s*D♭\s*E♭\s*F♭\s*G♭\s*A♭\s*B♭/.test(sp.cb) && /G𝄪/.test(sp.as) && /F𝄪/.test(sp.gs) && /E♯\s*F𝄪/.test(sp.gs), lang, 'every scale spelt by its letters', JSON.stringify(sp).replace(/\\n/g, ' '));
    await p.locator('[data-ref-root="E♭"]').click(); await sleep(300);
    const dim7 = await p.evaluate(() => document.querySelector('[data-ref-chord="dim7"]').closest('[data-ref-table]').innerText);
    say(/E♭\s*G♭\s*B𝄫\s*D𝄫/.test(dim7) && /E♭\s*G\s*B♭\s*D♭/.test(dim7), lang, 'chords on E♭: the diminished 7th E♭ G♭ B𝄫 D𝄫, the dominant 7th E♭ G B♭ D♭');
    // the sounds play without an error; the Scales map, a term's card, a word group
    for (const k of ['scaM', 'sgpp', 'sgtrill', 'chdom7', 'ts6-8', 'wAllegro', 'eraclassical']) { const b = p.locator('[data-ref-hear^="' + k.slice(0, 2) + '"]').first(); await b.click().catch(() => {}); await sleep(120); }
    await p.locator('[data-ref-scalesmap]').click(); await sleep(500); const floors = await p.locator('[data-smap-floor]').count();
    await p.locator('[data-ref-term="tie"]').click(); await sleep(500); const card = await p.evaluate(() => document.body.innerText.includes('tie') || document.body.innerText.includes('붙임줄'));
    say(floors === 9 && card && !p._errs.length, lang, 'sounds, the Scales map and a term’s card inside', floors, p._errs.slice(0, 1));
    await p.close();
    const q = await H.open({ path: '?tool=reference', w: 400, h: 1200, dsf: 1, lang }); await sleep(1300);
    await q.locator('[data-ref-door="pitch-range"]').first().click(); await sleep(1100);
    say(/drill=pitch-range/.test(await q.evaluate(() => location.search)) && !q._errs.length, lang, 'a door opens its room', await q.evaluate(() => location.search)); await q.close();
  }
  for (const lang of ['en', 'ko']) { const b = await H.open({ path: '?book=reference&lang=' + lang, w: 900, h: 1300, dsf: 1 }); await sleep(2200);
    const o = await b.evaluate(() => [...document.querySelectorAll('.bk-page')].map(pg => { const bd = pg.querySelector('.bk-body'); return bd.scrollHeight - bd.clientHeight; }));
    say(o.length === 15 && o.every(x => x <= 2) && !(await b.locator('[data-ref-door]').count()) && !(await b.locator('[data-ref-hear]').count()) && !(await b.locator('[data-ref-root]').count()) && !b._errs.length, lang, 'on paper: fifteen pages, nothing over, no buttons', JSON.stringify(o), b._errs.slice(0, 1)); await b.close(); }
  const k = await H.open({ path: '?teacher=1&view=books', w: 900, h: 1200, dsf: 1 }); await sleep(1100);
  say(await k.locator('[data-ref-book]').count() === 1 && !k._errs.length, 'the Books tab has the Reference'); await k.close();
  console.log('bad', bad); await H.close();
})();
