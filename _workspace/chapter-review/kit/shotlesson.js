// Screenshot a lesson guide page (desktop full page + phone), check overflow, broken images, errors
const { chromium } = require('playwright');
const http = require('http'), fs = require('fs'), path = require('path');
const ROOT = path.resolve(__dirname, '../site367'), NM = path.resolve(__dirname, 'node_modules');
const PAGE = process.env.PAGE || '/lessons/posture-and-hand-shape.html', OUT = process.env.OUT || '../rv1/page';
(async () => {
  const srv = http.createServer((req, res) => { const u = decodeURIComponent(req.url.split('?')[0]); const f = path.join(ROOT, u);
    if (u.startsWith('/__fonts/')) { const n = u.slice(9); const ff = n.startsWith('inter') ? NM + '/@fontsource/inter/files/' + n : NM + '/@fontsource/playfair-display/files/' + n; try { res.writeHead(200, { 'content-type': 'font/woff2' }); return res.end(fs.readFileSync(ff)); } catch (e) { res.writeHead(404); return res.end(); } }
    try { const b = fs.readFileSync(f); res.writeHead(200, { 'content-type': f.endsWith('.html') ? 'text/html' : f.endsWith('.svg') ? 'image/svg+xml' : 'image/jpeg' }); res.end(b); } catch (e) { res.writeHead(404); res.end(); } });
  await new Promise(r => srv.listen(0, r)); const base = 'http://localhost:' + srv.address().port;
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  for (const [w, n] of [[1280, 'desk'], [390, 'phone']]) {
    const ctx = await browser.newContext({ viewport: { width: w, height: 900 } }); const p = await ctx.newPage();
    const errs = []; p.on('pageerror', e => errs.push(e.message));
    await p.route('**/fonts.googleapis.com/**', r => { const ff = (fam, wt, f) => `@font-face{font-family:'${fam}';font-weight:${wt};src:url(${base}/__fonts/${f}) format('woff2');}`; r.fulfill({ contentType: 'text/css', body: [400, 500, 600, 700, 800].map(x => ff('Inter', x, `inter-latin-${x}-normal.woff2`)).join('') + [700, 800, 900].map(x => ff('Playfair Display', x, `playfair-display-latin-${x}-normal.woff2`)).join('') }); });
    await p.route('**/fonts.gstatic.com/**', r => r.fulfill({ body: '' }));
    await p.route('**/googlesyndication.com/**', r => r.fulfill({ body: '', contentType: 'text/javascript' }));
    await p.route('**/googletagmanager.com/**', r => r.fulfill({ body: '', contentType: 'text/javascript' }));
    await p.goto(base + PAGE); await p.waitForTimeout(600);
    await p.evaluate(() => document.querySelectorAll('img').forEach(i => i.loading = 'eager')); await p.waitForTimeout(600);
    await p.screenshot({ path: OUT + '-' + n + '.png', fullPage: true });
    const over = await p.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
    const broken = await p.$$eval('img', els => els.filter(i => !i.complete || i.naturalWidth === 0).length);
    const h = await p.evaluate(() => document.documentElement.scrollHeight);
    console.log(n, 'height', h, 'overflow', over, 'broken images', broken, 'errors', errs.join('|'));
    if (n === 'desk') await p.pdf({ path: OUT + '.pdf', format: 'A4', printBackground: true, margin: { top: '12mm', bottom: '12mm', left: '10mm', right: '10mm' } });
    await ctx.close();
  }
  await browser.close(); srv.close();
})();
