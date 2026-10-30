// Build DO: the dictionary (call 31). Usage: node dict790.js drills.t790.html
const { start } = require('/home/claude/pbtest/kit/contentharness');
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
(async () => {
  const H = await start(process.argv[2] || 'drills.t790.html'); let bad = 0;
  const say = (ok, ...a) => { if (!ok) bad++; console.log(ok ? 'ok  ' : 'BAD ', ...a); };
  for (const lang of ['en', 'ko']) {
    const p = await H.open({ path: '?drill=scales', w: 420, h: 1500, dsf: 1, lang }); await sleep(1500);
    const chips = await p.locator('[data-term-chips] button').allInnerTexts(), links = await p.locator('.term-link').count();
    say(chips.length === 4 && links >= 1 && !p._errs.length, lang, 'Scales: chips', JSON.stringify(chips), 'links', links, p._errs.slice(0, 1));
    await p.locator('[data-term-chips] button').first().click(); await sleep(500);
    const card = p.locator('[data-term-card]'); const txt = await card.innerText().catch(() => '');
    say((await card.count()) === 1 && /13/.test(txt) && txt.length > 40, lang, 'card opens with the room and a definition', JSON.stringify(txt.slice(0, 80)));
    await p.locator('[data-term-check]').click(); await sleep(1200);
    say((await p.locator('[data-term-card] [data-testid="check-run"]').count()) === 1, lang, 'quick check: one question from the room');
    await p.locator('[data-term-card] [data-term-room]').click(); await sleep(900);
    const q = await p.evaluate(() => location.search);
    say(/drill=tones/.test(q) && (await p.locator('[data-term-card]').count()) === 0, lang, 'Go to the room opens chapter 13', q);
    await p.close();
    // a step's text: a link inside a step, once a page; a room with no earlier term: no chips
    const r = await H.open({ path: '?drill=posture-hands', w: 420, h: 1200, dsf: 1, lang }); await sleep(900);
    say((await r.locator('[data-term-chips]').count()) === 0 && (await r.locator('.term-link').count()) === 0 && !r._errs.length, lang, 'chapter 1: nothing to bring, no links', r._errs.slice(0, 1));
    await r.close();
  }
  // in print: no links, the 'Bring with you' line on the opener, no overflow
  const b = await H.open({ path: '?book=lesson&ch=scales', w: 900, h: 1300, dsf: 1 }); await sleep(1500);
  const pr = await b.evaluate(() => ({ links: document.querySelectorAll('.term-link').length, line: (document.querySelector('[data-term-print]') || {}).innerText || '', over: [...document.querySelectorAll('.bk-page')].map(pg => pg.scrollHeight - pg.clientHeight) }));
  say(pr.links === 0 && /Bring with you: .*ch\. 13/.test(pr.line) && pr.over.every(x => x <= 2), 'print: no links, the line on the opener', JSON.stringify(pr.line), 'overflow', JSON.stringify(pr.over));
  await b.close();
  console.log('bad', bad); await H.close();
})();
