// Screenshots of the chapter 1 guide page (draft build), desktop and phone; checks for sideways scroll and spills
const { chromium } = require('playwright'); const path = require('path');
const NM = path.resolve(__dirname, 'node_modules');
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const file = 'file://' + path.resolve(__dirname, '../guide/lessons/posture-and-hand-shape.html');
  for (const [w, tag] of [[1100, 'desk'], [390, 'phone']]) {
    const ctx = await b.newContext({ viewport: { width: w, height: 900 }, deviceScaleFactor: tag === 'phone' ? 2 : 1 });
    const p = await ctx.newPage(); const errs = [];
    p.on('pageerror', e => errs.push(e.message));
    await p.route('**/fonts.googleapis.com/**', r => r.fulfill({ contentType: 'text/css', body:
      [400, 500, 600, 700, 800].map(x => `@font-face{font-family:'Inter';font-weight:${x};src:url(file://${NM}/@fontsource/inter/files/inter-latin-${x}-normal.woff2) format('woff2');}`).join('') +
      [700, 800, 900].map(x => `@font-face{font-family:'Playfair Display';font-weight:${x};src:url(file://${NM}/@fontsource/playfair-display/files/playfair-display-latin-${x}-normal.woff2) format('woff2');}`).join('') }));
    await p.route(/googlesyndication|googletagmanager|gstatic/, r => r.fulfill({ body: '' }));
    await p.goto(file); await p.evaluate(() => document.querySelectorAll('img').forEach(i => i.loading = 'eager')); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(400);
    const info = await p.evaluate(() => {
      const sw = document.documentElement.scrollWidth, cw = document.documentElement.clientWidth;
      const spill = [...document.querySelectorAll('svg.pic')].filter(s => { const r = s.getBoundingClientRect(), q = s.parentElement.getBoundingClientRect(); return r.right > q.right + 1 || r.left < q.left - 1; }).length;
      const imgs = [...document.images].map(i => i.naturalWidth);
      return { sw, cw, spill, imgs, h: document.documentElement.scrollHeight };
    });
    console.log(tag, JSON.stringify(info), errs.join('|'));
    await p.screenshot({ path: '../guide/shot374-' + tag + '.png', fullPage: true });
    await ctx.close();
  }
  await b.close();
})().catch(e => { console.error('CRASH', e); process.exit(1); });
