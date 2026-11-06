const { start } = require('./contentharness');
(async () => {
  const H = await start(process.env.BUILD || 'drills.t368.html');
  const p = await H.open({ path: '?book=lesson&ch=all&lang=en', w: 900, h: 1200 });
  await p.waitForTimeout(2500);
  const info = await p.$$eval('.lb-page', els => els.map(e => { const b = e.querySelector('.bk-body'); return b.scrollHeight - b.clientHeight; }));
  console.log('mixed: lb pages', info.length, 'overflow', JSON.stringify(info), 'chapters', await p.$$eval('.bk-chapter', e => e.length), 'errs', p._errs.join('|').slice(0, 200));
  await p.emulateMedia({ media: 'print' });
  const info2 = await p.$$eval('.lb-page', els => els.map(e => { const b = e.querySelector('.bk-body'); return [Math.round(e.getBoundingClientRect().height), b.scrollHeight - b.clientHeight]; }));
  console.log('print media:', JSON.stringify(info2));
  await p.pdf({ path: '../rv1/lball.pdf', preferCSSPageSize: true, printBackground: true });
  await H.close();
})().catch(e => { console.error('CRASH', e); process.exit(1); });
