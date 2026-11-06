const { start } = require('./contentharness');
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const H = await start(process.env.BUILD);
  for (const kind of ['lesson', 'work', 'teacher']) {
    const p = await H.open({ path: '?book=' + kind + '&ch=tones&lang=en', w: 900, h: 1200 });
    await p.waitForTimeout(2800); await p.emulateMedia({ media: 'print' });
    await p.pdf({ path: 'pack437/' + kind + '.pdf', format: 'A4', printBackground: true, preferCSSPageSize: true });
    await p.context().close();
  }
  await H.close();
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const q = await (await b.newContext()).newPage();
  await q.goto('file://' + path.resolve('pack437/pack.html')); await q.waitForTimeout(800);
  await q.evaluate(() => document.fonts.ready);
  await q.pdf({ path: 'pack437/pack.pdf', format: 'A4', printBackground: true, preferCSSPageSize: true });
  console.log('pack overflow', JSON.stringify(await q.evaluate(() => [...document.querySelectorAll('.page')].map(e => e.scrollHeight - e.clientHeight))));
  await b.close();
})();
