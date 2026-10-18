const { start } = require('/home/claude/pbtest/kit/contentharness');
const OUT = '/home/claude/pbtest/sc/shots/';
(async () => {
  const H = await start('drills.t486.html');
  for (const lang of ['en', 'ko']) for (const w of [320, 390]) {
    const p = await H.open({ path: '?teacher=1&tool=scale-finder', w, h: 900, lang });
    const log = [];
    const hs = async (tag) => { const o = await p.evaluate(() => ({ hs: document.documentElement.scrollWidth - document.documentElement.clientWidth })); log.push(tag + ' hscroll=' + o.hs); };
    await hs('open');
    const click = async (txt) => { const b = p.locator('button.chip', { hasText: txt }).first(); if (await b.count()) { await b.click(); await p.waitForTimeout(250); return true; } log.push('MISSING ' + txt); return false; };
    const L = lang === 'en';
    await p.screenshot({ path: OUT + `sf-${lang}-${w}-major.png`, fullPage: true });
    await click(L ? 'Degree names' : '음 이름'); await hs('names');
    await p.screenshot({ path: OUT + `sf-${lang}-${w}-names.png`, fullPage: true });
    await click(L ? 'Minor' : '단조');
    for (const f of (L ? ['Natural', 'Harmonic', 'Melodic'] : ['자연', '화성', '가락'])) {
      await click(f === 'Natural' || f === 'Harmonic' || f === 'Melodic' ? f + ' minor' : f + ' 단음계'); await hs('form ' + f);
      if (f === (L ? 'Melodic' : '가락')) await p.screenshot({ path: OUT + `sf-${lang}-${w}-melodic.png`, fullPage: true });
    }
    for (const s of (L ? ['Build it', 'Fingering patterns', 'Stamps', 'Modes'] : ['직접 만들기', '손가락 번호 패턴', '도장', '선법'])) {
      await click(s); await hs('sec ' + s);
      await p.screenshot({ path: OUT + `sf-${lang}-${w}-sec-${s.replace(/\W/g, '')}.png`, fullPage: true });
    }
    console.log(lang, w, log.join(' | '), 'errs=' + JSON.stringify(p._errs));
    await p.context().close();
  }
  await H.close();
})();
