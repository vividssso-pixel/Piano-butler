// Review pack, chapter 1: render the three books for one chapter to PDF and list overflow
const { start } = require('./contentharness');
const CH = process.env.CH || 'posture-hands', OUT = process.env.OUTDIR || '../rv1';
(async () => {
  const H = await start(process.env.BUILD || 'drills.t366.html');
  for (const kind of ['lesson', 'work', 'teacher']) {
    const p = await H.open({ path: '?book=' + kind + '&ch=' + CH + '&lang=en', w: 900 });
    await p.waitForTimeout(1200);
    const info = await p.$$eval('.bk-page', els => els.map(e => { const b = e.querySelector('.bk-body') || e; return b.scrollHeight - b.clientHeight; }));
    await p.pdf({ path: OUT + '/' + kind + '.pdf', preferCSSPageSize: true, printBackground: true });
    const txt = await p.evaluate(() => document.body.innerText);
    require('fs').writeFileSync(OUT + '/' + kind + '.txt', txt);
    console.log(kind, 'pages', info.length, 'overflow', JSON.stringify(info), 'errors', p._errs.join('|').slice(0, 200), 'db', p._reqs.filter(u => /supabase/.test(u)).length);
    await p.context().close();
  }
  await H.close();
})().catch(e => { console.error('CRASH', e); process.exit(1); });
