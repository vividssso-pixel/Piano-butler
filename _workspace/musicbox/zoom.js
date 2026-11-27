// node zoom.js <id> <selector> <index> -> shots/_zoom.png (a close-up of one element, at 3x)
const { chromium } = require('playwright');
(async () => { const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' }); const p = await b.newPage({ viewport: { width: 900, height: 1200 }, deviceScaleFactor: 2 });
  await p.goto('file://' + __dirname + '/lesson-' + process.argv[2] + '.html'); await p.waitForTimeout(900);
  const e = p.locator(process.argv[3]).nth(+process.argv[4] || 0); const bb = await e.boundingBox();
  await p.screenshot({ path: __dirname + '/shots/_zoom.png', clip: { x: Math.max(0, bb.x - 30), y: Math.max(0, bb.y - 40), width: bb.width + 60, height: bb.height + 60 } });
  console.log(JSON.stringify(await e.evaluate(x => [...x.querySelectorAll('svg.clef')].map(s => { const r = s.getBoundingClientRect(), t = s.parentElement.getBoundingClientRect(); return [Math.round(r.left), Math.round(r.width), Math.round(t.left), Math.round(t.width)]; })))); await b.close(); })();
