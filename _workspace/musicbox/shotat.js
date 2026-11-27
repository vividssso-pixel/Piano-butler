// node shotat.js <id> <text> <n>: close-up around the n-th table cell whose text is exactly <text>
const { chromium } = require('playwright');
(async () => { const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' }); const p = await b.newPage({ viewport: { width: 900, height: 1200 }, deviceScaleFactor: 2 });
  await p.goto('file://' + __dirname + '/lesson-' + process.argv[2] + '.html'); await p.waitForTimeout(900);
  const r = await p.evaluate(([t, n]) => { const c = [...document.querySelectorAll('.bgt td')].filter(e => e.textContent.trim().replace(/\s/g, ' ') === t)[+n || 0]; const q = c.getBoundingClientRect(); return [q.left, q.top + scrollY]; }, [process.argv[3], process.argv[4]]);
  await p.screenshot({ path: `${__dirname}/shots/_at-${process.argv[2]}.png`, fullPage: true, clip: { x: Math.max(0, r[0] - 90), y: Math.max(0, r[1] - 70), width: 240, height: 130 } }); await b.close(); })();
