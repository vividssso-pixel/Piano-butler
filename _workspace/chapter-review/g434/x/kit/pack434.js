const { start } = require('./contentharness');
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const H = await start(process.env.BUILD);
  const p = await H.open({ path: '?book=lesson&ch=tones&lang=en&draft=1', w: 900, h: 1200 });
  await p.waitForTimeout(2600);
  await p.emulateMedia({ media: 'print' });
  await p.pdf({ path: 'pack434/draft.pdf', format: 'A4', printBackground: true, preferCSSPageSize: true });
  await H.close();
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const q = await (await b.newContext()).newPage();
  await q.goto('file://' + path.resolve('pack434/pack.html')); await q.waitForTimeout(800);
  await q.evaluate(() => document.fonts.ready);
  await q.pdf({ path: 'pack434/pack.pdf', format: 'A4', printBackground: true, preferCSSPageSize: true });
  const over = await q.evaluate(() => [...document.querySelectorAll('.page')].map(e => e.scrollHeight - e.clientHeight));
  console.log('pack overflow', JSON.stringify(over));
  await b.close();
})();
