const { chromium } = require('playwright');
(async () => { const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' }); const p = await b.newPage({ viewport: { width: 900, height: 1200 }, deviceScaleFactor: +(process.env.DPR || 1) });
  for (const s of process.argv.slice(2)) { await p.goto(`file://${process.cwd()}/lesson-${s}.html`); await p.waitForFunction(() => window.__paged); await p.waitForTimeout(200);
    const pgs = await p.$$('.pg'); for (let i = 0; i < pgs.length; i++) await pgs[i].screenshot({ path: `shots/_${s}-${i + 1}.png` }); }
  await b.close(); })();
