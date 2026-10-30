// Build DD: the Books tab. Usage: node dd779.js drills.t779.html
const { start } = require('/home/claude/pbtest/kit/contentharness');
const SH = '/tmp/claude-0/-home-claude/c245f740-5546-5c71-9064-9bfc4952b3ac/scratchpad/shots/dd/';
require('fs').mkdirSync(SH, { recursive: true });
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
(async () => {
  const H = await start(process.argv[2] || 'drills.t779.html'); let bad = 0;
  const say = (ok, ...a) => { if (!ok) bad++; console.log(ok ? 'ok  ' : 'BAD ', ...a); };
  for (const lang of ['en', 'ko']) {
    const p = await H.open({ path: '?teacher=1', w: 420, h: 1400, lang }); await sleep(800);
    const tabs = await p.$$eval('.pb-main > div:nth-of-type(2) button, .pb-main button', bs => bs.map(b => b.innerText.trim()).filter(x => /^(Home|Chapters|Books|Toolbox|Practice|홈|챕터|책|도구함|연습)$/.test(x)));
    say(tabs.length === 5 && (tabs[2] === 'Books' || tabs[2] === '책'), lang, 'tabs', JSON.stringify(tabs));
    await p.locator('button:has-text("' + (lang === 'ko' ? '책' : 'Books') + '")').first().click(); await sleep(800);
    const n = await p.locator('[data-testid^="ckp-shelf-"]').count(), url = await p.evaluate(() => location.search), toolbox = await p.locator('text=/^(Activities|활동)$/').count();
    say(n >= 4 && /view=books/.test(url) && toolbox === 0, lang, 'Books tab: checkpoints', n, 'url', url, 'no Activities chip', toolbox === 0, p._errs.slice(0, 1));
    if (lang === 'en') await p.screenshot({ path: SH + 'books-tab.png', fullPage: false });
    // a chapter opened from the shelf stays under the Books tab, and back returns to the shelf
    const link = p.locator('.pb-main a[href*="drill="], .pb-main button:has-text("Pulse")').first();
    await p.close();
    const q = await H.open({ path: '?teacher=1&view=toolbox&sec=books', w: 420, h: 1200, lang }); await sleep(800);
    say((await q.locator('[data-testid^="ckp-shelf-"]').count()) >= 4 && /view=books/.test(await q.evaluate(() => location.search)), lang, 'old sec=books link lands on the Books tab');
    await q.close();
    const r = await H.open({ path: '?teacher=1&view=toolbox', w: 420, h: 1200, lang }); await sleep(800);
    say((await r.locator('[data-testid^="ckp-shelf-"]').count()) === 0 && !r._errs.length, lang, 'Toolbox has no books section', r._errs.slice(0, 1));
    await r.close();
  }
  console.log('bad', bad); await H.close();
})();
