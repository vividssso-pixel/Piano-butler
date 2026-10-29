const { start } = require('/home/claude/pbtest/kit/contentharness');
const SH = '/tmp/claude-0/-home-claude/c245f740-5546-5c71-9064-9bfc4952b3ac/scratchpad/shots/ckp/';
(async () => { const H = await start(process.argv[2] || 'drills.t773.html'); let bad = 0;
  for (const lang of ['en', 'ko']) { const p = await H.open({ path: '?teacher=1&view=toolbox&sec=books', w: 420, h: 1600, lang }); await new Promise(r => setTimeout(r, 900));
    let n = await p.locator('[data-testid^="ckp-shelf-"]').count();
    if (!n) { const b = p.locator('button:has-text("Books"), button:has-text("책")').first(); if (await b.count()) { await b.click(); await new Promise(r => setTimeout(r, 800)); n = await p.locator('[data-testid^="ckp-shelf-"]').count(); } }
    const hrefs = await p.$$eval('[data-testid^="ckp-shelf-"] a', as => as.map(a => a.getAttribute('href')));
    console.log(lang, n === 2 ? 'ok' : 'BAD', n, JSON.stringify(hrefs), p._errs.slice(0, 1)); if (n !== 2) bad++;
    if (n) await p.locator('[data-testid="ckp-shelf-0a"]').first().evaluate(e => e.closest('.card').scrollIntoView());
    if (n) await p.locator('[data-testid="ckp-shelf-0a"]').first().evaluate(e => e.closest('.card')).then(() => null);
    if (n) { const card = p.locator('[data-testid="ckp-shelf-0a"]').first().locator('xpath=ancestor::div[contains(@class,"card")][1]'); await card.screenshot({ path: SH + 'shelf-' + lang + '.png' }); }
    await p.close(); }
  console.log('bad', bad); await H.close(); })();
