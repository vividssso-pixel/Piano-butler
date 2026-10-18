// Phase 489 (after review): labels, stale state, student view, reloads.
const { start } = require('/home/claude/pbtest/kit/contentharness');
(async () => {
  const H = await start('drills.t489.html');
  for (const lang of ['en', 'ko']) {
    const L = lang === 'en';
    const log = [];
    const open = async (path, w = 390) => H.open({ path, w, h: 900, lang });
    const main = async (p) => (await p.evaluate(() => [...document.querySelectorAll('.pb-main')].pop().innerText)).replace(/\s+/g, ' ');
    const url = async (p) => p.evaluate(() => location.search);
    const click = async (p, re, scope) => { const b = p.locator(scope || 'button, a', { hasText: re }).first(); if (await b.count()) { await b.click(); await p.waitForTimeout(350); return true; } log.push('MISSING ' + re); return false; };
    const R = (en, ko) => new RegExp(L ? en : ko);
    // 1. back labels
    let p = await open('?teacher=1&view=home&area=pitch&concept=p-scales');
    await click(p, R('^1\\s*Learn', '^1\\s*배우기')); log.push('learn back label: ' + (await main(p)).slice(0, 40) + ' | ' + await url(p));
    await click(p, R('← Scales and keys', '← 스케일과 조')); log.push('-> ' + await url(p));
    await click(p, R('^2\\s*Try', '^2\\s*해 보기')); await click(p, R('Scale finder', '스케일 찾기')); log.push('try->tool label: ' + (await main(p)).slice(0, 30));
    await click(p, R('← Try', '← 해 보기')); log.push('-> ' + await url(p));
    await click(p, R('More practice', '더 연습하기')); await click(p, R('Every F', '모든 F')); log.push('more->tool label: ' + (await main(p)).slice(0, 30));
    await click(p, R('← Try', '← 해 보기'));
    // 2. stale ret: tool from Try, then Practice tab, then a practice tool, back
    await click(p, R('Scale finder', '스케일 찾기')); await click(p, R('^Practice$', '^연습$'), '.pb-main button');
    log.push('practice tab url: ' + await url(p));
    // 3. Home tab resets to the five areas
    await click(p, R('^Home$', '^홈$'), '.pb-main button'); log.push('home tab -> ' + await url(p) + ' | ' + (await main(p)).slice(0, 40));
    // 4. Check: back label names the concept
    p = await open('?teacher=1&view=home&area=pitch&concept=p-scales');
    await click(p, R('^3\\s*Check', '^3\\s*확인하기')); log.push('check header: ' + (await main(p)).slice(0, 60) + ' | ' + await url(p));
    await click(p, R('← Scales and keys', '← 스케일과 조')); log.push('check back -> ' + await url(p));
    // 5. reloads keep Home context
    p = await open('?tool=scale-finder&ret=home&area=pitch&concept=p-scales&room=try');
    log.push('reload tool label: ' + (await main(p)).slice(0, 30)); await click(p, R('← Try', '← 해 보기')); log.push('-> ' + await url(p));
    p = await open('?teacher=1&drill=scales&tab=drill&level=1&ret=home&area=pitch&concept=p-scales');
    log.push('reload chapter: ' + (await main(p)).slice(0, 50)); await click(p, R('← Scales and keys', '← 스케일과 조')); log.push('-> ' + await url(p) + ' | ' + (await main(p)).slice(0, 40));
    // 6. student view never shows the teacher Home
    p = await open('?view=home'); log.push('no teacher: ' + (await main(p)).slice(0, 60) + ' | ' + await url(p));
    p = await open('?teacher=1&view=home'); await click(p, R('Student view', '학생 화면')); log.push('student view: ' + (await main(p)).slice(0, 60));
    // 7. level 0 has five choices; sizes of the new buttons
    p = await open('?teacher=1&view=home', 320);
    const sizes = await p.evaluate(() => [...document.querySelectorAll('.pb-main button')].filter(b => b.offsetParent && b.closest('.fade-up')).map(b => Math.round(b.getBoundingClientRect().height)));
    log.push('level0 button heights: ' + sizes.join(','));
    await click(p, R('^Pitch', '^음높이')); await click(p, R('Scales and keys', '스케일과 조')); await click(p, R('^2\\s*Try', '^2\\s*해 보기'));
    const sizes3 = await p.evaluate(() => [...document.querySelectorAll('.pb-main .fade-up button')].map(b => Math.round(b.getBoundingClientRect().height)));
    log.push('level3 button heights: ' + sizes3.join(','));
    console.log(lang + '\n   ' + log.join('\n   '));
    for (const c of H.pages || []) {}
  }
  await H.close();
})();
