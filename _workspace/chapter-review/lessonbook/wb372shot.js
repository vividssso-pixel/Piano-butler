const { start } = require('./contentharness');
(async () => {
  const H = await start(process.env.BUILD || 'drills.t372.html');
  for (const kind of ['work', 'teacher']) {
    const p = await H.open({ path: '?book=' + kind + '&ch=posture-hands&lang=en', w: 900, h: 1200 });
    await p.waitForTimeout(1500);
    const info = await p.$$eval('.bk-page', els => els.map(e => { const b = e.querySelector('.bk-body'); return b ? b.scrollHeight - b.clientHeight : null; }));
    const spill = await p.$$eval('.bk-page .pb-art', els => els.filter(a => { const b = a.getBoundingClientRect(), p = a.closest('.bk-body').getBoundingClientRect(); return b.bottom > p.bottom + 1 || b.right > p.right + 1; }).map(a => a.dataset.art));
    const rows = await p.$$eval('[data-map-row]', els => els.length);
    console.log(kind, 'pages', info.length, 'overflow', JSON.stringify(info), 'spill', JSON.stringify(spill), 'map rows', rows, 'errs', p._errs.join('|').slice(0, 200));
    await p.pdf({ path: '../rv1/' + kind + '372.pdf', preferCSSPageSize: true, printBackground: true });
    await p.context().close();
  }
  await H.close();
})().catch(e => { console.error('CRASH', e); process.exit(1); });
