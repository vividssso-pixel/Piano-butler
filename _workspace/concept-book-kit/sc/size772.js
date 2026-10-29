// How heavy is drills.html? First paint and memory under a slower CPU and network, gzip on (as the live site).
// Usage: node size772.js drills.t771.html
const http = require('http'), fs = require('fs'), zlib = require('zlib'), path = require('path');
const { chromium } = require('playwright');
const A3 = '/home/claude/pbtest/a3', NM = '/home/claude/pbtest/kit/node_modules';
const FILE = A3 + '/' + (process.argv[2] || 'drills.t771.html');
const GZ = zlib.gzipSync(fs.readFileSync(FILE), { level: 9 });
(async () => {
  const srv = http.createServer((req, res) => { const u = req.url.split('?')[0];
    if (u === '/drills.html') { res.writeHead(200, { 'content-type': 'text/html', 'content-encoding': 'gzip' }); return res.end(GZ); }
    if (u === '/blank.html') { res.writeHead(200, { 'content-type': 'text/html' }); return res.end('<!doctype html><title>b</title>'); }
    res.writeHead(404); res.end(); });
  await new Promise(r => srv.listen(0, r)); const base = 'http://localhost:' + srv.address().port;
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const nets = { wifi: { down: 20e6 / 8, up: 5e6 / 8, lat: 30 }, slow: { down: 4e6 / 8, up: 1e6 / 8, lat: 150 } };
  const runs = [['desktop', 1, null], ['iPad-ish (CPU x4), good wifi', 4, 'wifi'], ['older phone (CPU x6), weak network', 6, 'slow']];
  for (const path0 of ['?view=path', '?drill=first-steps']) for (const [name, cpu, net] of runs) {
    const t = [];
    for (let rep = 0; rep < 2; rep++) {
      const ctx = await browser.newContext({ viewport: { width: 820, height: 1180 } }); const p = await ctx.newPage();
      await p.route('**/cdnjs.cloudflare.com/ajax/libs/react/**', r => r.fulfill({ path: NM + '/react/umd/react.production.min.js', contentType: 'text/javascript' }));
      await p.route('**/cdnjs.cloudflare.com/ajax/libs/react-dom/**', r => r.fulfill({ path: NM + '/react-dom/umd/react-dom.production.min.js', contentType: 'text/javascript' }));
      await p.route('**/cdnjs.cloudflare.com/ajax/libs/babel-standalone/**', r => r.fulfill({ body: '', contentType: 'text/javascript' }));
      await p.route('**/fonts.googleapis.com/**', r => r.fulfill({ body: '', contentType: 'text/css' }));
      await p.route('**/fonts.gstatic.com/**', r => r.fulfill({ body: '' }));
      await p.goto(base + '/blank.html'); await p.evaluate(() => localStorage.setItem('pb_mode_v1', 'student'));
      const cdp = await ctx.newCDPSession(p);
      await cdp.send('Network.enable'); await cdp.send('Network.setCacheDisabled', { cacheDisabled: true });
      if (net) await cdp.send('Network.emulateNetworkConditions', { offline: false, downloadThroughput: nets[net].down, uploadThroughput: nets[net].up, latency: nets[net].lat });
      await cdp.send('Emulation.setCPUThrottlingRate', { rate: cpu });
      const t0 = Date.now(); await p.goto(base + '/drills.html' + path0, { waitUntil: 'commit' });
      await p.waitForSelector('#root *', { timeout: 120000 }); const tPaint = Date.now() - t0;
      await p.waitForLoadState('load'); const tLoad = Date.now() - t0;
      const m = await p.evaluate(() => { const n = performance.getEntriesByType('navigation')[0]; return { dl: Math.round(n.responseEnd - n.requestStart), dcl: Math.round(n.domContentLoadedEventEnd), heap: performance.memory ? Math.round(performance.memory.usedJSHeapSize / 1e6) : null }; });
      t.push({ paint: tPaint, load: tLoad, ...m }); await ctx.close();
    }
    const best = t.sort((a, b) => a.paint - b.paint)[0];
    console.log(path0.padEnd(20), name.padEnd(40), 'download', (best.dl / 1000).toFixed(1) + 's', '| first screen', (best.paint / 1000).toFixed(1) + 's', '| memory', best.heap + ' MB');
  }
  console.log('size', (fs.statSync(FILE).size / 1e6).toFixed(2), 'MB; gzip', (GZ.length / 1e6).toFixed(2), 'MB');
  await browser.close(); srv.close();
})();
