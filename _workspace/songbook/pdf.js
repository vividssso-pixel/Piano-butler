const { chromium } = require('playwright');
(async () => { const b = await chromium.launch(require('fs').existsSync('/opt/pw-browsers/chromium') ? { executablePath: '/opt/pw-browsers/chromium' } : {}); const p = await b.newPage();
  await p.goto('file://' + process.argv[2]); await p.waitForTimeout(500);
  const over = await p.evaluate(() => [...document.querySelectorAll('.pg .body')].map(e => e.scrollHeight - e.clientHeight));
  console.log('over', JSON.stringify(over));
  await p.pdf({ path: process.argv[3], format: 'A4', printBackground: true, preferCSSPageSize: true }); await b.close(); })();
