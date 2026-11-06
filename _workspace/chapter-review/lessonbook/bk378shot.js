// The house in the books: the Workbook's opening pages and a chapter map page; every page fits
const { start } = require('./contentharness');
(async () => {
  const H = await start(process.env.BUILD || 'drills.t378.html');
  for (const [path, tag] of [['?book=work&ch=front&lang=en', 'front'], ['?book=work&ch=posture-hands&lang=en', 'ch1'], ['?book=work&ch=note-names&lang=en', 'notes']]) {
    const p = await H.open({ path, w: 900, h: 1200 }); await p.waitForTimeout(1500);
    const info = await p.$$eval('.bk-page', els => els.map(e => { const b = e.querySelector('.bk-body'); return b ? b.scrollHeight - b.clientHeight : null; }));
    const houses = await p.$$eval('[data-bk-house]', e => e.length);
    console.log(tag, 'pages', info.length, 'overflow', JSON.stringify(info), 'small houses', houses, 'errs', p._errs.join('|').slice(0, 160));
    await p.pdf({ path: '../shots/bk378-' + tag + '.pdf', preferCSSPageSize: true, printBackground: true, pageRanges: tag === 'notes' ? '1-2' : '1-3' });
    await p.context().close();
  }
  await H.close();
})().catch(e => { console.error('CRASH', e); process.exit(1); });
