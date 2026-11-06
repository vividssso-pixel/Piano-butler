const { start } = require('./contentharness');
const ok = (c, m) => { console.log((c ? 'PASS ' : 'FAIL ') + m); if (!c) process.exitCode = 1; };
const SONG = /Hot Cross Buns|핫 크로스 번|Mary Had|떴다 떴다|Old MacDonald|올드 맥도날드|Rain Rain|레인 레인/;
(async () => {
  const H = await start(process.env.BUILD || 'drills.t399.html');
  for (const ch of ['first-steps', 'note-names']) for (const lang of ['en', 'ko']) {
    const p = await H.open({ path: '?drill=' + ch, w: 390, h: 900, lang });
    const txt = await p.evaluate(() => document.querySelector('.fade-up').innerText);
    const m = SONG.exec(txt); ok(!m, 'app ' + ch + ' ' + lang + ' no songs' + (m ? ': ' + m[0] : ''));
    ok(p._errs.length === 0, 'app ' + ch + ' ' + lang + ' no errors ' + p._errs.join('|').slice(0, 100));
    await p.context().close();
    for (const kind of ['lesson', 'work', 'teacher', 'spread']) {
      const q = await H.open({ path: '?book=' + kind + '&ch=' + ch + '&lang=' + lang, w: 900, h: 1200 });
      await q.waitForTimeout(1500);
      const info = await q.$$eval('.bk-page', els => els.map(e => { const b = e.querySelector('.bk-body'); return b ? b.scrollHeight - b.clientHeight : null; }));
      const t2 = await q.evaluate(() => document.body.innerText); const m2 = SONG.exec(t2);
      ok(info.every(v => v <= 1) && !m2 && q._errs.length === 0, kind + ' ' + ch + ' ' + lang + ': ' + info.length + ' pages fit ' + JSON.stringify(info) + ', no songs' + (m2 ? ' -- ' + m2[0] : '') + ' ' + q._errs.join('|').slice(0, 80));
      await q.context().close();
    }
  }
  await H.close(); process.exit(process.exitCode || 0);
})();
