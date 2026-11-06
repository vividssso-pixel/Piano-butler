// Phase 436 (from houseimg428.js): five floors. lessons/img/house.jpg (the guide front page's sharing picture, 1200 x 630): the townhouse on the left, its name on the right, on white
//   node houseimg428.js house-og.svg house.jpg
const { chromium } = require('playwright'); const fs = require('fs'), path = require('path');
const SRC = process.argv[2], OUT = process.argv[3];
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const p = await b.newPage({ viewport: { width: 1200, height: 630 } });
  const NM = path.resolve(__dirname, 'node_modules');
  const ff = (fam, w, f, st = 'normal') => `@font-face{font-family:'${fam}';font-weight:${w};font-style:${st};src:url(data:font/woff2;base64,${fs.readFileSync(f).toString('base64')}) format('woff2')}`;   // inline: a blank page cannot read file:// fonts
  const fonts = [ff('Inter', 600, NM + '/@fontsource/inter/files/inter-latin-600-normal.woff2'), ff('Inter', 700, NM + '/@fontsource/inter/files/inter-latin-700-normal.woff2'), ff('Inter', 800, NM + '/@fontsource/inter/files/inter-latin-800-normal.woff2'),
    ff('Playfair Display', 800, NM + '/@fontsource/playfair-display/files/playfair-display-latin-800-normal.woff2'), ff('Playfair Display', 900, NM + '/@fontsource/playfair-display/files/playfair-display-latin-900-normal.woff2'), ff('Playfair Display', 800, NM + '/@fontsource/playfair-display/files/playfair-display-latin-800-italic.woff2', 'italic'),
    ff('Cinzel', 700, NM + '/@fontsource/cinzel/files/cinzel-latin-700-normal.woff2'), ff('Cormorant Garamond', 700, NM + '/@fontsource/cormorant-garamond/files/cormorant-garamond-latin-700-normal.woff2'), ff('Cormorant Garamond', 700, NM + '/@fontsource/cormorant-garamond/files/cormorant-garamond-latin-700-italic.woff2', 'italic')].join('');
  const svg = fs.readFileSync(SRC, 'utf8').replace('<svg ', '<svg style="height:610px;width:auto;display:block" ');
  await p.setContent('<style>' + fonts + '</style><body style="margin:0;background:#ffffff;font-family:Inter,sans-serif;display:flex;align-items:center;justify-content:center;gap:64px;height:630px;padding:0;box-sizing:border-box">'
    + '<div style="flex:none;padding-top:10px">' + svg + '</div>'
    + '<div style="color:#26296b"><div style="font-family:Cinzel,serif;font-weight:700;font-size:22px;letter-spacing:0.14em;color:#e4572e">26 chapters · one room each</div>'
    + '<div style="font-family:\'Playfair Display\',serif;font-weight:900;font-size:64px;line-height:1.02;margin:10px 0 18px">The Piano<br>Butler’s house</div>'
    + '<div style="font-family:\'Cormorant Garamond\',serif;font-style:italic;font-weight:700;font-size:31px;line-height:1.25;color:#26296b">Five floors,<br>a room for each chapter.</div></div></body>');
  await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(500);
  await p.screenshot({ path: OUT, type: 'jpeg', quality: 86 });
  await b.close();
})();
