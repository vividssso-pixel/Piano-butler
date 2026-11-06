const { start } = require('./contentharness');
(async () => {
  const H = await start(process.env.BUILD || 'drills.t397.html');
  for (const [kind, ch] of (process.env.ONLY ? [['spread','posture-hands']] : [['lesson', 'note-names'], ['spread', 'note-names'], ['lesson', 'first-steps'], ['spread', 'first-steps'], ['spread', 'posture-hands'], ['work', 'first-steps']])) {
    const p = await H.open({ path: '?book=' + kind + '&ch=' + ch + '&lang=ko', w: 900, h: 1200 });
    await p.waitForTimeout(1600);
    const info = await p.$$eval('.bk-page', els => els.map(e => { const b = e.querySelector('.bk-body'); return b ? b.scrollHeight - b.clientHeight : null; }));
    console.log(kind, ch, 'ko', info.length, JSON.stringify(info), p._errs.join('|').slice(0, 100));
    await p.context().close();
  }
  await H.close(); process.exit(0);
})();
