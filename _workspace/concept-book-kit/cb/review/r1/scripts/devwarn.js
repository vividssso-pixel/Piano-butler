// React development build: key warnings, hook warnings, prop warnings while opening the concept book (print + screen)
// and tapping through the pads; compared with the same routes in t484 where they exist.
const http = require('http'), fs = require('fs');
const { chromium } = require('playwright');
const NM = '/home/claude/pbtest/kit/node_modules';
async function run(build, paths) {
  const srv = http.createServer((req, res) => { const u = req.url.split('?')[0]; if (u === '/drills.html') { res.writeHead(200, { 'content-type': 'text/html' }); return res.end(fs.readFileSync('/home/claude/pbtest/a3/' + build)); } res.writeHead(404); res.end(); });
  await new Promise(r => srv.listen(0, r)); const base = 'http://localhost:' + srv.address().port;
  const br = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const out = {};
  for (const [path, act] of paths) {
    const ctx = await br.newContext({ viewport: { width: 390, height: 860 } }); const p = await ctx.newPage(); const w = [];
    p.on('console', m => { if (m.type() === 'error' || m.type() === 'warning') w.push(m.text().slice(0, 300)); });
    p.on('pageerror', e => w.push('PAGEERROR ' + e.message));
    await p.route('**/cdnjs.cloudflare.com/ajax/libs/react/**', r => r.fulfill({ path: NM + '/react/umd/react.development.js', contentType: 'text/javascript' }));
    await p.route('**/cdnjs.cloudflare.com/ajax/libs/react-dom/**', r => r.fulfill({ path: NM + '/react-dom/umd/react-dom.development.js', contentType: 'text/javascript' }));
    await p.route('**/cdnjs.cloudflare.com/ajax/libs/babel-standalone/**', r => r.fulfill({ body: '', contentType: 'text/javascript' }));
    await p.route('**/fonts.googleapis.com/**', r => r.fulfill({ body: '', contentType: 'text/css' }));
    await p.route('**/fonts.gstatic.com/**', r => r.fulfill({ body: '' }));
    await p.route('**/googletagmanager.com/**', r => r.fulfill({ body: '' }));
    await p.goto(base + '/drills.html' + path); await p.waitForTimeout(2500);
    if (act) await act(p);
    out[path] = [...new Set(w.filter(x => !/Failed to load resource|favicon|audio\//.test(x)))];
    await ctx.close();
  }
  await br.close(); srv.close(); return out;
}
const tap = async (p) => {
  for (const sel of ['[data-cb="key-pad"] g[data-key]', '[data-cb="shapes-pad"] button.chip', '[data-cb="shapes-pad"] g[data-key]']) { const els = await p.$$(sel); for (const e of els.slice(0, 13)) { try { await e.click({ timeout: 500 }); } catch (x) {} } }
  const got = await p.$$('button:has-text("Got it")'); for (const g of got) { try { await g.click({ timeout: 500 }); await p.waitForTimeout(100); } catch (x) {} }
  const five = await p.$$('[data-five-checks] button'); for (const f of five.slice(0, 4)) { try { await f.click({ timeout: 500 }); } catch (x) {} }
  await p.waitForTimeout(500);
};
(async () => {
  const P485 = [['?book=concept&ch=p-scales&lang=en'], ['?book=concept&ch=p-scales&lang=ko'], ['?teacher=1&tool=cb-p-scales', tap], ['?teacher=1&view=toolbox'], ['?tool=cb-p-scales&lock=1'], ['?book=lesson&ch=scales'], ['?drill=scales&tab=learn']];
  const a = await run('drills.t485.html', P485);
  const b = await run('drills.t484.html', [['?book=lesson&ch=scales'], ['?drill=scales&tab=learn'], ['?teacher=1&view=toolbox']]);
  for (const k in a) { console.log('485 ' + k + ': ' + a[k].length); a[k].slice(0, 8).forEach(x => console.log('     ' + x.replace(/\s+/g, ' ').slice(0, 260))); }
  for (const k in b) { console.log('484 ' + k + ': ' + b[k].length); b[k].slice(0, 5).forEach(x => console.log('     ' + x.replace(/\s+/g, ' ').slice(0, 200))); }
})();
