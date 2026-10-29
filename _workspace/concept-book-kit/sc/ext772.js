// First visit vs return visits: the app inline (as now) vs the app as its own cached file (app.js).
const { chromium } = require('playwright'); const http = require('http'), fs = require('fs'), zlib = require('zlib'), crypto = require('crypto');
const NM = '/home/claude/pbtest/kit/node_modules', A3 = '/home/claude/pbtest/a3';
const files = { '/inline/drills.html': A3 + '/drills.t771.html', '/ext/drills.html': A3 + '/ext/drills.html', '/ext/app.js': A3 + '/ext/app.js' };
const gz = {}; for (const k in files) { const b = fs.readFileSync(files[k]); gz[k] = { b: zlib.gzipSync(b, { level: 9 }), et: '"' + crypto.createHash('md5').update(b).digest('hex') + '"' }; }
(async () => {
  const srv = http.createServer((q, r) => { const u = q.url.split('?')[0]; const f = gz[u];
    if (!f) { r.writeHead(200, { 'content-type': 'text/html' }); return r.end('<!doctype html>'); }
    if (q.headers['if-none-match'] === f.et) { r.writeHead(304, { etag: f.et, 'cache-control': 'max-age=600' }); return r.end(); }
    r.writeHead(200, { 'content-type': u.endsWith('.js') ? 'text/javascript' : 'text/html', 'content-encoding': 'gzip', etag: f.et, 'cache-control': 'max-age=600' }); r.end(f.b); });
  await new Promise(r => srv.listen(0, r)); const base = 'http://localhost:' + srv.address().port;
  const br = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  for (const kind of ['inline', 'ext']) for (const [name, cpu, net] of [['iPad-ish (CPU x4), good wifi', 4, { d: 20e6 / 8, l: 30 }]]) {
    const ctx = await br.newContext(); const p = await ctx.newPage();
    for (const [pat, f] of [['react/', 'react/umd/react.production.min.js'], ['react-dom/', 'react-dom/umd/react-dom.production.min.js']]) await p.route('**/ajax/libs/' + pat + '**', r => r.fulfill({ path: NM + '/' + f, contentType: 'text/javascript' }));
    await p.route('**/babel-standalone/**', r => r.fulfill({ body: '' })); await p.route('**/fonts.g*/**', r => r.fulfill({ body: '' }));
    await p.goto(base + '/x'); await p.evaluate(() => localStorage.setItem('pb_mode_v1', 'student'));
    const cdp = await ctx.newCDPSession(p); await cdp.send('Network.enable');
    await cdp.send('Network.emulateNetworkConditions', { offline: false, downloadThroughput: net.d, uploadThroughput: net.d, latency: net.l });
    await cdp.send('Emulation.setCPUThrottlingRate', { rate: cpu });
    const out = [];
    for (let v = 1; v <= 4; v++) { await p.goto(base + '/x'); const t0 = Date.now(); await p.goto(base + '/' + kind + '/drills.html?view=path'); await p.waitForSelector('#root *', { timeout: 120000 }); out.push(((Date.now() - t0) / 1000).toFixed(1) + 's'); await p.waitForTimeout(1500); }
    console.log(kind.padEnd(7), name, '| visits 1, 2, 3, 4:', out.join(', '), p._e || ''); await ctx.close(); }
  await br.close(); srv.close(); })();
