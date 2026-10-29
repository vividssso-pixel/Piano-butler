const { chromium } = require('playwright'); const http = require('http'), fs = require('fs');
const NM = '/home/claude/pbtest/kit/node_modules', F = '/home/claude/pbtest/a3/drills.mark.html';
(async () => { const srv = http.createServer((q, r) => { r.writeHead(200, { 'content-type': 'text/html' }); r.end(q.url.startsWith('/d') ? fs.readFileSync(F) : '<!doctype html>'); }); await new Promise(r => srv.listen(0, r)); const base = 'http://localhost:' + srv.address().port;
  const br = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  for (const cpu of [1, 4]) { const ctx = await br.newContext(); const p = await ctx.newPage();
    for (const [pat, f] of [['react/', 'react/umd/react.production.min.js'], ['react-dom/', 'react-dom/umd/react-dom.production.min.js']]) await p.route('**/ajax/libs/' + pat + '**', r => r.fulfill({ path: NM + '/' + f, contentType: 'text/javascript' }));
    await p.route('**/babel-standalone/**', r => r.fulfill({ body: '' })); await p.route('**/fonts.g*/**', r => r.fulfill({ body: '' }));
    await p.goto(base + '/b'); await p.evaluate(() => localStorage.setItem('pb_mode_v1', 'student'));
    const cdp = await ctx.newCDPSession(p); await cdp.send('Emulation.setCPUThrottlingRate', { rate: cpu });
    await p.goto(base + '/drills.html?view=path'); await p.waitForSelector('#root *'); 
    const r = await p.evaluate(() => { const g = n => performance.getEntriesByName(n)[0].startTime; return { s0: Math.round(g('s0')), script: Math.round(g('s1') - g('s0')) }; });
    const paint = await p.evaluate(() => Math.round(performance.now()));
    console.log('CPU x' + cpu, 'page start to script', r.s0 + 'ms', '| the app script (parse + run)', r.script + 'ms', '| first screen by', paint + 'ms'); await ctx.close(); }
  await br.close(); srv.close(); })();
