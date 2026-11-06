const { start } = require('./contentharness');
(async () => {
  const H = await start(process.env.BUILD || 'drills.sf401.html');
  const p = await H.open({ path: '?book=lesson&ch=staff&lang=' + (process.env.LANGX || 'en') + '&draft=' + (process.env.DRAFT || '1'), w: 900, h: 1200 });
  await p.waitForTimeout(3500);
  const pages = await p.$$('.bk-page');
  const info = await p.$$eval('.bk-page', els => els.map(e => { const b = e.querySelector('.bk-body'); return b ? b.scrollHeight - b.clientHeight : null; }));
  console.log('pages', pages.length, 'overflow', JSON.stringify(info), 'errs', p._errs.join('|').slice(0, 300));
  require('fs').mkdirSync('p401', { recursive: true });
  for (let i = 0; i < pages.length; i++) await pages[i].screenshot({ path: 'p401/sf-p' + (i + 1) + '.png' });
  if (process.env.PDF) await p.pdf({ path: 'p401/lesson-draft.pdf', preferCSSPageSize: true, printBackground: true });
  await p.context().close(); await H.close(); process.exit(0);
})().catch(e => { console.error('CRASH', e); process.exit(1); });
