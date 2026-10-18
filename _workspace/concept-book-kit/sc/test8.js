// Phase 489: the concept home. Walk the four levels, both languages, phone widths.
const { start } = require('/home/claude/pbtest/kit/contentharness');
const OUT = '/home/claude/pbtest/sc/shots/';
(async () => {
  const H = await start('drills.t489.html');
  for (const lang of ['en', 'ko']) for (const w of [320, 390]) {
    const L = lang === 'en';
    const p = await H.open({ path: '?teacher=1&view=home', w, h: 900, lang });
    const log = [];
    const hs = async (tag) => { const o = await p.evaluate(() => ({ hs: document.documentElement.scrollWidth - document.documentElement.clientWidth, url: location.search })); log.push(tag + ' hs=' + o.hs + ' ' + o.url); };
    const click = async (re) => { const b = p.locator('button, a', { hasText: re }).first(); if (await b.count()) { await b.click(); await p.waitForTimeout(350); return true; } log.push('MISSING ' + re); return false; };
    const txt = async () => (await p.evaluate(() => [...document.querySelectorAll('.pb-main')].pop().innerText)).replace(/\s+/g, ' ').slice(0, 140);
    await hs('L0'); await p.screenshot({ path: OUT + `h-${lang}-${w}-0.png`, fullPage: true });
    await click(L ? /^Pitch/ : /^음높이/); await hs('L1'); await p.screenshot({ path: OUT + `h-${lang}-${w}-1.png`, fullPage: true });
    await click(L ? /Scales and keys/ : /스케일과 조/); await hs('L2'); await p.screenshot({ path: OUT + `h-${lang}-${w}-2.png`, fullPage: true });
    await click(L ? /^2\s*Try/ : /^2\s*해 보기/); await hs('L3'); await p.screenshot({ path: OUT + `h-${lang}-${w}-3.png`, fullPage: true });
    await click(L ? /Key finder/ : /조 찾기/); log.push('tool: ' + await txt()); await hs('tool');
    await click(L ? /← Home/ : /← 홈/); log.push('back: ' + await txt() + ' | ' + await p.evaluate(() => location.search));
    await click(L ? /← Scales and keys/ : /← 스케일과 조/);   // to L2
    await click(L ? /^3\s*Check/ : /^3\s*확인하기/); log.push('check: ' + await txt()); await hs('check');
    await click(L ? /← Back/ : /← 뒤로/); log.push('after check: ' + await txt() + ' | ' + await p.evaluate(() => location.search));
    await click(L ? /^1\s*Learn/ : /^1\s*배우기/); log.push('learn: ' + await txt()); await hs('learn');
    console.log(lang, w, log.join('\n   '), '\n   errs=' + JSON.stringify(p._errs));
    await p.context().close();
  }
  await H.close();
})();
