// lessons/img/house.jpg: the wide house on paper, 1200 px wide (the page's sharing picture)
const { chromium } = require('playwright'); const fs = require('fs'), path = require('path');
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const p = await b.newPage({ viewport: { width: 1200, height: 630 } });
  const svg = fs.readFileSync(path.resolve(__dirname, '../guide/tools/lessons/svg/index/house-wide.svg'), 'utf8').replace('<svg ', '<svg style="height:600px;width:auto;display:block;margin:15px auto" ');
  await p.setContent('<body style="margin:0;background:#faf6ec;font-family:Inter,sans-serif">' + svg + '</body>');
  await p.screenshot({ path: path.resolve(__dirname, '../guide/lessons/img/house.jpg'), type: 'jpeg', quality: 86 });
  await b.close();
})();
