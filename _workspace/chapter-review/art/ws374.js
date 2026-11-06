// Worksheet image for the chapter 1 guide page: Workbook page 2 ("Is this a good set-up?"), printed alone
const { start } = require('./contentharness');
(async () => {
  const H = await start(process.env.BUILD || 'drills.t373.html');
  const p = await H.open({ path: '?book=work&ch=posture-hands&lang=en&pages=2', w: 900, h: 1200 });
  await p.waitForTimeout(1500);
  const n = await p.$$eval('.bk-page', els => els.length);
  const head = await p.$$eval('.bk-page', els => els.map(e => e.innerText.slice(0, 120).replace(/\n/g, ' / ')));
  console.log('pages', n, JSON.stringify(head), 'errs', p._errs.join('|').slice(0, 200));
  await p.pdf({ path: '../guide/ws374.pdf', preferCSSPageSize: true, printBackground: true });
  await H.close();
})().catch(e => { console.error('CRASH', e); process.exit(1); });
