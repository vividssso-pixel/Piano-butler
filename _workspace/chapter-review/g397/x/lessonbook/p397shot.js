const { start } = require('./contentharness');
(async () => {
  const H = await start(process.env.BUILD || 'drills.t397.html');
  for (const kind of (process.env.KINDS || 'lesson,work,teacher').split(',')) {
    const p = await H.open({ path: '?book=' + kind + '&ch=note-names&lang=' + (process.env.LANGX || 'en'), w: 900, h: 1200 });
    await p.waitForTimeout(1800);
    const pages = await p.$$('.bk-page');
    for (let i = 0; i < pages.length; i++) await pages[i].screenshot({ path: 'p397/' + kind + '-' + (i + 1) + '.png' });
    console.log(kind, pages.length, p._errs.join('|'));
    if (process.env.PDF) await p.pdf({ path: 'p397/' + kind + '.pdf', format: 'A4', printBackground: true, preferCSSPageSize: true });
    await p.context().close();
  }
  await H.close(); process.exit(0);
})().catch(e => { console.error('CRASH', e); process.exit(1); });
