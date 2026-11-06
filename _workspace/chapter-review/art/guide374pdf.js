// The draft guide page as one long PDF page, as it looks on screen (for Sohyun to read)
const { chromium } = require('playwright'); const path = require('path');
const NM = path.resolve(__dirname, 'node_modules');
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const p = await b.newPage({ viewport: { width: 1000, height: 900 } });
  await p.route('**/fonts.googleapis.com/**', r => r.fulfill({ contentType: 'text/css', body:
    [400, 500, 600, 700, 800].map(x => `@font-face{font-family:'Inter';font-weight:${x};src:url(file://${NM}/@fontsource/inter/files/inter-latin-${x}-normal.woff2) format('woff2');}`).join('') +
    [700, 800, 900].map(x => `@font-face{font-family:'Playfair Display';font-weight:${x};src:url(file://${NM}/@fontsource/playfair-display/files/playfair-display-latin-${x}-normal.woff2) format('woff2');}`).join('') }));
  await p.route(/googlesyndication|googletagmanager|gstatic/, r => r.fulfill({ body: '' }));
  await p.goto('file://' + path.resolve(__dirname, '../guide/lessons/posture-and-hand-shape.html'));
  await p.evaluate(() => document.querySelectorAll('img').forEach(i => i.loading = 'eager'));
  await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(600);
  await p.emulateMedia({ media: 'screen' });
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  await p.pdf({ path: process.argv[2], width: '1000px', height: (h + 10) + 'px', printBackground: true, pageRanges: '1' });
  console.log('height', h);
  await b.close();
})();
