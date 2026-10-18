const { start } = require('/home/claude/pbtest/kit/contentharness');
(async () => {
  const H = await start('drills.t486.html');
  for (const lang of ['en', 'ko']) for (const w of [320, 390]) {
    const p = await H.open({ path: '?teacher=1&tool=scale-finder', w, h: 900, lang });
    const L = lang === 'en', c = async (txt) => { const b = p.locator('button.chip', { hasText: txt }).first(); await b.click(); await p.waitForTimeout(200); };
    const info = {};
    await c(L ? 'Degree names' : '음계 이름');
    await c(L ? 'Minor' : '단조'); await c(L ? 'natural minor' : '자연 단음계');
    info.natural7 = await p.evaluate(() => (document.body.innerText.match(/7\s+[^\n]*?(subtonic|leading note|서브토닉|이끎음)[^\n]*/) || [''])[0]);
    await c(L ? 'melodic minor' : '가락 단음계');
    info.down = await p.evaluate(() => (document.body.innerText.match(/(Coming down|내려올 때는)[^\n]*/) || [''])[0]);
    // a form whose fingers are hidden: F# melodic
    await p.locator('button.chip', { hasText: /F♯m/ }).first().click().catch(() => {}); await p.waitForTimeout(250);
    info.note = await p.evaluate(() => (document.body.innerText.match(/(No finger numbers|손가락 번호를 보여)[^\n]*/) || ['(none)'])[0].slice(0, 60));
    info.legendHidden = await p.evaluate(() => { const l = [...document.querySelectorAll('div')].find(d => /1-2-3 (group|묶음)/.test(d.innerText) && d.children.length === 3); return l ? getComputedStyle(l).display : 'n/a'; });
    await p.screenshot({ path: `/home/claude/pbtest/sc/shots/b-${lang}-${w}-clash.png`, fullPage: true });
    const hs = await p.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
    const sizes = await p.evaluate(() => ['Degree names', '음계 이름', 'Build it', '직접 만들기', 'natural minor', '자연 단음계'].map(x => { const b = [...document.querySelectorAll('button')].find(y => y.innerText.trim() === x); return b ? x + ':' + Math.round(b.getBoundingClientRect().height) : null; }).filter(Boolean));
    const top = await p.evaluate(() => { const b = [...document.querySelectorAll('button')].find(y => /^(2 oct|2옥타브)$/.test(y.innerText.trim())); const card = b.closest('.try-box').getBoundingClientRect(); const r = b.getBoundingClientRect(); return Math.round(r.right - card.right); });
    console.log(lang, w, 'hs', hs, JSON.stringify(info), 'sizes', sizes.join(' '), '2oct past card edge:', top, 'errs', JSON.stringify(p._errs));
    await p.context().close();
  }
  await H.close();
})();
