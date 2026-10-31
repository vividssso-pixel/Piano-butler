// Build EC, call 41: the Reference on screen (seven tables, doors into rooms, the Scales map and the dictionary inside) and on
// paper (five A4 pages, no overflow); the Home's Quick line; the Books tab. Usage: node ec805.js drills.t805.html
const { start } = require('/home/claude/pbtest/kit/contentharness');
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
(async () => {
  const H = await start(process.argv[2] || 'drills.t805.html'); let bad = 0;
  const say = (ok, ...a) => { if (!ok) bad++; console.log(ok ? 'ok  ' : 'BAD ', ...a); };
  for (const lang of ['en', 'ko']) {
    const p = await H.open({ path: '?teacher=1&view=home', w: 400, h: 1200, dsf: 1, lang }); await sleep(1100);
    const quick = await p.evaluate(() => [...document.querySelectorAll('[data-testid="home-quick"] [data-quick]')].map(e => e.getAttribute('data-quick')));
    await p.locator('[data-quick="reference"]').click(); await sleep(1300);
    const r = await p.evaluate(() => ({ secs: [...document.querySelectorAll('[data-ref-sec]')].map(e => e.getAttribute('data-ref-sec')), doors: document.querySelectorAll('[data-ref-door]').length,
      keys: document.querySelectorAll('[data-ref-table="keys"] svg').length, scales: [...document.querySelectorAll('[data-ref-scale]')].map(e => e.getAttribute('data-ref-scale')), terms: document.querySelectorAll('[data-ref-term]').length,
      blank: [...document.querySelectorAll('[data-ref-term]')].filter(b => !b.innerText.trim()).length, w: document.scrollingElement.scrollWidth }));
    say(quick.includes('reference') && !quick.includes('scales-map') && r.secs.length === 7 && r.doors > 60 && r.keys >= 15 && r.scales.length === 7 && r.terms === 79 && r.blank === 0 && r.w <= 402 && !p._errs.length, lang, 'the Reference: seven tables, doors, keys, scales, every term named', JSON.stringify({ quick, ...r, secs: r.secs.length }), p._errs.slice(0, 1));
    // the patterns are counted, not typed: the major scale reads T T S T T T S
    const maj = await p.locator('[data-ref-scale="maj"]').innerText(); say(/T\s*T\s*S\s*T\s*T\s*T\s*S/.test(maj.replace(/\n/g, ' ')), lang, 'the major scale’s steps', maj.replace(/\s+/g, ' '));
    // the Scales map inside, a term's card, a door
    await p.locator('[data-ref-scalesmap]').click(); await sleep(500); const floors = await p.locator('[data-smap-floor]').count();
    await p.locator('[data-ref-term="tie"]').click(); await sleep(500); const card = await p.evaluate(() => document.body.innerText.includes('tie') || document.body.innerText.includes('붙임줄'));
    say(floors === 9 && card && !p._errs.length, lang, 'the Scales map and a term’s card inside', floors);
    await p.keyboard.press('Escape').catch(() => {}); await sleep(200);
    await p.close();
    const q = await H.open({ path: '?tool=reference', w: 400, h: 1200, dsf: 1, lang }); await sleep(1200);
    await q.locator('[data-ref-door="rhythm-3"]').first().click(); await sleep(1100);
    say(/drill=rhythm-3/.test(await q.evaluate(() => location.search)) && !q._errs.length, lang, 'a door opens its room', await q.evaluate(() => location.search)); await q.close();
  }
  // on paper
  for (const lang of ['en', 'ko']) { const b = await H.open({ path: '?book=reference&lang=' + lang, w: 900, h: 1300, dsf: 1 }); await sleep(1800);
    const o = await b.evaluate(() => [...document.querySelectorAll('.bk-page')].map(pg => { const bd = pg.querySelector('.bk-body'); return bd.scrollHeight - bd.clientHeight; }));
    say(o.length === 5 && o.every(x => x <= 2) && !(await b.locator('[data-ref-door]').count()) && !b._errs.length, lang, 'on paper: five pages, nothing over, no buttons', JSON.stringify(o), b._errs.slice(0, 1)); await b.close(); }
  // the Books tab
  const k = await H.open({ path: '?teacher=1&view=books', w: 900, h: 1200, dsf: 1 }); await sleep(1100);
  say(await k.locator('[data-ref-book]').count() === 1 && !k._errs.length, 'the Books tab has the Reference'); await k.close();
  console.log('bad', bad); await H.close();
})();
