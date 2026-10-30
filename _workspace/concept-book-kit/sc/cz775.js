// Build CZ: the Prelim books' guesses and challenges. Print (both languages): every page fits, one guess on the opener, a
// challenge on every step page. Screen: the guess opens, the time challenges have a stopwatch. Usage: node cz775.js drills.t775.html [shoot]
const { start } = require('/home/claude/pbtest/kit/contentharness');
const SH = '/tmp/claude-0/-home-claude/c245f740-5546-5c71-9064-9bfc4952b3ac/scratchpad/shots/cz/';
require('fs').mkdirSync(SH, { recursive: true });
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
const IDS = (process.env.IDS || 'listen-sing,tempo,rhythm,ledger-lines,scales,scale-play,minor-scales,signs').split(',');
(async () => {
  const H = await start(process.argv[2] || 'drills.t775.html'); let bad = 0;
  const say = (ok, ...a) => { if (!ok) bad++; console.log(ok ? 'ok  ' : 'BAD ', ...a); };
  for (const id of IDS) for (const lang of ['en', 'ko']) {
    const p = await H.open({ path: '?book=lesson&ch=' + id + '&lang=' + lang, w: 900, h: 1300, dsf: 1 }); await sleep(1800);
    const r = await p.evaluate(() => [...document.querySelectorAll('.bk-page')].map((pg, i) => { const b = pg.querySelector('.bk-body');
      return { i, over: Math.max(pg.scrollHeight - pg.clientHeight, b ? b.scrollHeight - b.clientHeight : 0), g: pg.querySelectorAll('.lb-guess').length, c: pg.querySelectorAll('.lb-challenge').length, tm: pg.querySelectorAll('.lb-challenge[data-kind="time"]').length }; }));
    const steps = r.slice(1, -1);   // the opener and the check-up page aside
    const ok = !p._errs.length && r.every(x => x.over <= 2) && r[0].g === 1 && steps.every(x => x.c === 1);
    say(ok, 'print', id, lang, 'pages', r.length, 'overflow', JSON.stringify(r.map(x => x.over)), 'guess', r[0].g, 'challenges', JSON.stringify(r.map(x => x.c)), 'time', r.reduce((a, x) => a + x.tm, 0), p._errs.slice(0, 1));
    if (process.argv[3] && lang === 'en') { const pg = p.locator('.bk-page'); const n = await pg.count(); for (let i = 0; i < Math.min(n, 3); i++) await pg.nth(i).screenshot({ path: SH + id + '-' + i + '.png' }); }
    if (process.argv[3] && lang === 'ko' && id === 'ledger-lines') { const pg = p.locator('.bk-page'); await pg.nth(5).screenshot({ path: SH + id + '-ko-5.png' }); }
    await p.close();
    const q = await H.open({ path: '?drill=' + id, w: 390, h: 2200, lang }); await sleep(700);
    const g = await q.locator('.lb-guess').count(); let ans = '';
    if (g) { await q.locator('.lb-guess button').click(); await sleep(150); ans = (await q.locator('.lb-guess').innerText()).replace(/\s+/g, ' '); }
    say(!q._errs.length && g === 1 && ans.length > 20, 'screen', id, lang, '|', ans.slice(0, 120), q._errs.slice(0, 1));
    await q.close();
  }
  console.log('bad', bad); await H.close();
})();
