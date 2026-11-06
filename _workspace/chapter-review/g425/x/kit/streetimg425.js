// lessons/img/house.jpg (the guide front page's sharing picture, 1200 x 630): the street in two stretches, on white
const { chromium } = require('playwright'); const fs = require('fs'), path = require('path');
const SRC = process.argv[2], OUT = process.argv[3];
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const p = await b.newPage({ viewport: { width: 1200, height: 630 } });
  const NM = path.resolve(__dirname, 'node_modules');
  const ff = (fam, w, f, st = 'normal') => `@font-face{font-family:'${fam}';font-weight:${w};font-style:${st};src:url(file://${f})}`;
  const fonts = [ff('Inter', 600, NM + '/@fontsource/inter/files/inter-latin-600-normal.woff2'), ff('Inter', 700, NM + '/@fontsource/inter/files/inter-latin-700-normal.woff2'), ff('Inter', 800, NM + '/@fontsource/inter/files/inter-latin-800-normal.woff2'),
    ff('Playfair Display', 800, NM + '/@fontsource/playfair-display/files/playfair-display-latin-800-normal.woff2'), ff('Playfair Display', 700, NM + '/@fontsource/playfair-display/files/playfair-display-latin-700-italic.woff2', 'italic')].join('');
  const svg = fs.readFileSync(SRC, 'utf8').replace('<svg ', '<svg style="height:600px;width:auto;display:block;margin:15px auto" ');
  await p.setContent('<style>' + fonts + '</style><body style="margin:0;background:#ffffff;font-family:Inter,sans-serif">' + svg + '</body>');
  await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(400);
  await p.screenshot({ path: OUT, type: 'jpeg', quality: 86 });
  await b.close();
})();
