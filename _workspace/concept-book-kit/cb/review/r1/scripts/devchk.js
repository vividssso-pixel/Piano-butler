// Prove the development React build is loaded and that warnings are captured (so devwarn.js's zero is real).
const http = require('http'), fs = require('fs'); const { chromium } = require('playwright'); const NM = '/home/claude/pbtest/kit/node_modules';
(async () => {
  const srv = http.createServer((req, res) => { const u = req.url.split('?')[0]; if (u === '/drills.html') { res.writeHead(200, { 'content-type': 'text/html' }); return res.end(fs.readFileSync('/home/claude/pbtest/a3/drills.t485.html')); } res.writeHead(404); res.end(); });
  await new Promise(r => srv.listen(0, r)); const base = 'http://localhost:' + srv.address().port;
  const br = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' }); const ctx = await br.newContext(); const p = await ctx.newPage(); const w = [];
  p.on('console', m => w.push(m.type() + ': ' + m.text().slice(0, 150)));
  const reqs = []; p.on('request', r => reqs.push(r.url()));
  await p.route('**/cdnjs.cloudflare.com/ajax/libs/react/**', r => r.fulfill({ path: NM + '/react/umd/react.development.js', contentType: 'text/javascript' }));
  await p.route('**/cdnjs.cloudflare.com/ajax/libs/react-dom/**', r => r.fulfill({ path: NM + '/react-dom/umd/react-dom.development.js', contentType: 'text/javascript' }));
  await p.route('**/cdnjs.cloudflare.com/ajax/libs/babel-standalone/**', r => r.fulfill({ body: '', contentType: 'text/javascript' }));
  await p.route('**/fonts.googleapis.com/**', r => r.fulfill({ body: '', contentType: 'text/css' }));
  await p.route('**/fonts.gstatic.com/**', r => r.fulfill({ body: '' }));
  await p.route('**/googletagmanager.com/**', r => r.fulfill({ body: '' }));
  await p.route('**/pagead2.googlesyndication.com/**', r => r.fulfill({ body: '' }));
  await p.goto(base + '/drills.html?teacher=1&tool=cb-p-scales'); await p.waitForTimeout(2500);
  console.log(await p.evaluate(() => [React.version, !!document.querySelector('[data-cb]')]));
  console.log(reqs.filter(u => /react|babel/.test(u)).map(u => u.slice(-60)));
  console.log(w.slice(0, 6));
  await p.evaluate(() => { const d = document.createElement('div'); document.body.appendChild(d); ReactDOM.createRoot(d).render(React.createElement('div', null, [React.createElement('span'), React.createElement('span')])); });
  await p.waitForTimeout(500); console.log('after a deliberate keyless list:', w.slice(-2));
  await br.close(); srv.close();
})();
