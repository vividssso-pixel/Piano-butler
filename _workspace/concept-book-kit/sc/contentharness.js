// Serve a drills build (no student link) for chapter-content tests
const http = require('http'), fs = require('fs'), path = require('path');
const { chromium } = require('playwright');
const A3 = path.resolve(__dirname, '../a3'), NM = path.resolve(__dirname, 'node_modules');
async function start(build) {
  const FILE = A3 + '/' + build;
  const fontFiles = n => n.startsWith('inter') ? NM + '/@fontsource/inter/files/' + n : n.startsWith('noto-music') ? NM + '/@fontsource/noto-music/files/' + n : n.startsWith('cinzel') ? NM + '/@fontsource/cinzel/files/' + n : n.startsWith('cormorant') ? NM + '/@fontsource/cormorant-garamond/files/' + n : NM + '/@fontsource/playfair-display/files/' + n;
  const srv = http.createServer((req, res) => { const u = req.url.split('?')[0];
    if (u.startsWith('/__fonts/')) { try { res.writeHead(200, { 'content-type': 'font/woff2' }); res.end(fs.readFileSync(fontFiles(u.slice(9)))); } catch (e) { res.writeHead(404); res.end(); } return; }
    if (u === '/drills.html') { res.writeHead(200, { 'content-type': 'text/html' }); return res.end(fs.readFileSync(FILE)); }
    if (u.endsWith('.app.js')) { try { const f = path.join(path.dirname(FILE), path.basename(u)); res.writeHead(200, { 'content-type': 'text/javascript' }); return res.end(fs.readFileSync(f)); } catch (e) { res.writeHead(404); return res.end(); } }   // Build CW: the app code in its own file
    if (u === '/blank.html') { res.writeHead(200, { 'content-type': 'text/html' }); return res.end('<!doctype html><title>b</title>'); }
    res.writeHead(404); res.end('nf'); });
  await new Promise(r => srv.listen(0, r)); const base = 'http://localhost:' + srv.address().port;
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  async function open(o = {}) {
    const ctx = await browser.newContext({ deviceScaleFactor: o.dsf || 1, viewport: { width: o.w || 390, height: o.h || 900 }, reducedMotion: o.reducedMotion || 'no-preference', ...(o.video ? { recordVideo: { dir: o.video, size: { width: o.w || 390, height: o.h || 900 } } } : {}) });
    const p = await ctx.newPage(); p._errs = []; p._reqs = [];
    p.on('pageerror', e => p._errs.push(e.message)); p.on('request', r => p._reqs.push(r.url()));
    const file = u => r => r.fulfill({ path: u, contentType: 'text/javascript' });
    await p.route('**/cdnjs.cloudflare.com/ajax/libs/react/**', file(NM + '/react/umd/react.production.min.js'));
    await p.route('**/cdnjs.cloudflare.com/ajax/libs/react-dom/**', file(NM + '/react-dom/umd/react-dom.production.min.js'));
    await p.route('**/cdnjs.cloudflare.com/ajax/libs/babel-standalone/**', r => r.fulfill({ body: '', contentType: 'text/javascript' }));
    await p.route('**/fonts.googleapis.com/**', r => { const ff = (fam, w, f) => `@font-face{font-family:'${fam}';font-weight:${w};font-style:normal;src:url(${base}/__fonts/${f}) format('woff2');}`; r.fulfill({ contentType: 'text/css', body: [400, 500, 600, 700, 800, 900].map(w => ff('Inter', w, `inter-latin-${w}-normal.woff2`)).join('') + [400, 500, 600, 700, 800, 900].map(w => ff('Playfair Display', w, `playfair-display-latin-${w}-normal.woff2`) + ff('Playfair Display', w, `playfair-display-latin-${w}-italic.woff2`).replace('font-style:normal', 'font-style:italic')).join('') + [600, 700].map(w => ff('Cinzel', w, `cinzel-latin-${w}-normal.woff2`) + ff('Cormorant Garamond', w, `cormorant-garamond-latin-${w}-normal.woff2`) + ff('Cormorant Garamond', w, `cormorant-garamond-latin-${w}-italic.woff2`).replace('font-style:normal', 'font-style:italic')).join('') + `@font-face{font-family:'Noto Music';src:url(${base}/__fonts/noto-music-music-400-normal.woff2) format('woff2');}` }); });
    await p.route('**/fonts.gstatic.com/**', r => r.fulfill({ body: '' }));
    await p.goto(base + '/blank.html');
    await p.evaluate((st) => { localStorage.setItem('pb_mode_v1', 'student'); for (const k in st) localStorage.setItem(k, st[k]); }, o.store || {});
    await p.goto(base + '/drills.html' + (o.path || '')); await p.waitForSelector('#root *'); await p.waitForTimeout(900);
    if (o.lang === 'ko') { const b = await p.$('button.chip:has-text("한국어")'); if (b) { await b.click(); await p.waitForTimeout(500); } }
    await p.evaluate(() => document.fonts.ready);
    return p;
  }
  return { open, base, close: async () => { await browser.close(); srv.close(); } };
}
module.exports = { start };
