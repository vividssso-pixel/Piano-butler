const { start } = require('/home/claude/pbtest/kit/contentharness');
const SH = '/tmp/claude-0/-home-claude/c245f740-5546-5c71-9064-9bfc4952b3ac/scratchpad/shots/bk/';
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
(async () => {
  const H = await start(process.argv[2] || 'drills.t768.html'); let bad = 0;
  for (const id of (process.env.IDS || 'posture-hands,first-steps,pulse,note-names,hand-positions,ear-prep,note-values,staff').split(',')) for (const lang of ['en', 'ko']) {
    const p = await H.open({ path: '?drill=' + id, w: 390, h: 2000, lang }); await sleep(600);
    const g = await p.locator('.lb-guess').count(), c = await p.locator('.lb-challenge').count();
    let ans = '';
    if (g) { await p.locator('.lb-guess button').click(); await sleep(150); ans = (await p.locator('.lb-guess').innerText()).replace(/\s+/g, ' '); }
    const can = await p.evaluate(() => { const h = document.querySelector('.lb-can-h'); if (!h) return 'none'; const box = h.parentElement; const cs = getComputedStyle(box); const it = box.querySelector(':scope > div:not(.lb-can-h)'); return cs.borderTopWidth + ' / ' + (it ? getComputedStyle(it, '::before').width : '-'); });
    const ok = !p._errs.length && (id === process.env.NOG ? g === 0 : g === 1);
    if (!ok) bad++;
    console.log((ok ? 'ok  ' : 'BAD ') + id, lang, 'guess', g, 'challenges on the first step', c, '| can', can, '|', ans.slice(0, 90), p._errs.slice(0, 1));
    if (id === 'pulse') await p.screenshot({ path: SH + 'screen-pulse-' + lang + '.png' });
    await p.close();
  }
  console.log('bad', bad); await H.close();
})();
