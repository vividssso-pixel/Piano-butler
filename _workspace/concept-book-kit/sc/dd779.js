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
    const tabs = await p.$$eval('.pb-main > div:nth-of-type(2) button, .pb-main button', bs => bs.map(b => b.innerText.trim()).filter(x => /^(Home|Chapters|Books|Printables|Toolbox|Practice|홈|챕터|책|교구|도구함|연습)$/.test(x)));
    say(tabs.length === 5 && (tabs[2] === 'Books' || tabs[2] === '책') && (tabs[3] === 'Printables' || tabs[3] === '교구') && !tabs.some(x => /Toolbox|도구함/.test(x)), lang, 'tabs', JSON.stringify(tabs));   // Build DL: Printables; Build DN: no Toolbox
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
    say((await r.locator('[data-testid^="ckp-shelf-"]').count()) === 0 && !r._errs.length, lang, 'old ?view=toolbox (now the Home) has no books section', r._errs.slice(0, 1));
    await r.close();
    // Build DL: the Printables tab: every cut-out set as a card with a Print link; the Books tab has no cut-outs section
    const u = await H.open({ path: '?teacher=1&view=printables', w: 420, h: 1400, lang }); await sleep(800);
    const cards = await u.locator('[data-printable]').count(), prints = await u.locator('[data-printable] a[href*="book=cutouts"]').count(), purl = await u.evaluate(() => location.search);
    say(cards === 14 && prints === 14 && /view=printables/.test(purl) && !u._errs.length, lang, 'Printables tab: cards', cards, 'print links', prints, 'url', purl, u._errs.slice(0, 1));
    if (lang === 'en') await u.screenshot({ path: SH + 'printables-tab.png', fullPage: false });
    await u.locator('[data-printable] button').first().click(); await sleep(800);
    const active = await u.evaluate(() => { const b = [...document.querySelectorAll('.pb-main button')].find(x => /^(Printables|교구)$/.test(x.innerText.trim())); return b ? getComputedStyle(b).color : ''; });
    say(/drill=/.test(await u.evaluate(() => location.search)) && active === 'rgb(38, 41, 107)', lang, 'a chapter opened from a card stays under Printables (tab navy)', active);
    await u.close();
    const v = await H.open({ path: '?teacher=1&view=books', w: 420, h: 1400, lang }); await sleep(800);
    say((await v.locator('[data-cut-ch]').count()) === 0, lang, 'Books tab has no cut-outs section');
    await v.close();
  }
  console.log('bad', bad); await H.close();
})();
