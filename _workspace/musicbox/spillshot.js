// node spillshot.js <id> -> shots/_sp-<id>-N.png, a close-up around each text that runs out of its cell
const { chromium } = require('playwright');
(async () => { const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' }); const p = await b.newPage({ viewport: { width: 900, height: 1200 }, deviceScaleFactor: 2 });
  await p.goto('file://' + __dirname + '/lesson-' + process.argv[2] + '.html'); await p.waitForTimeout(900);
  const r = await p.evaluate(() => { const o = []; for (const td of document.querySelectorAll('.bgt td')) { const q = td.getBoundingClientRect();
    for (const t of [...td.querySelectorAll('*')].concat([td])) for (const n of t.childNodes) { if (n.nodeType !== 3 || !n.textContent.trim()) continue; const rg = document.createRange(); rg.selectNodeContents(n); const x = rg.getBoundingClientRect();
      if (x.left < q.left - 1.5 || x.right > q.right + 1.5) o.push([x.left, x.top + scrollY, n.textContent.trim(), td.className, t.tagName]); } } return o; });
  let k = 0; for (const [x, y, t, c, tg] of r) { console.log(t, c, tg); await p.screenshot({ path: `${__dirname}/shots/_sp-${process.argv[2]}-${++k}.png`, fullPage: true, clip: { x: Math.max(0, x - 70), y: Math.max(0, y - 45), width: 160, height: 100 } }); } await b.close(); })();
