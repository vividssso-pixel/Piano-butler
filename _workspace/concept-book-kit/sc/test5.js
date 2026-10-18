// Phase 487b: the Key finder. Interactions, phone widths, both languages.
const { start } = require('/home/claude/pbtest/kit/contentharness');
const OUT = '/home/claude/pbtest/sc/shots/';
(async () => {
  const H = await start('drills.t487.html');
  for (const lang of ['en', 'ko']) for (const w of [320, 390]) {
    const p = await H.open({ path: '?teacher=1&tool=key-finder', w, h: 900, lang });
    const L = lang === 'en';
    const log = [];
    const hs = async (tag) => { const o = await p.evaluate(() => ({ hs: document.documentElement.scrollWidth - document.documentElement.clientWidth })); log.push(tag + ' hs=' + o.hs); };
    const btn = async (txt, cls = 'button') => { const b = p.locator(cls, { hasText: txt }).first(); if (await b.count()) { await b.click(); await p.waitForTimeout(220); return true; } log.push('MISSING ' + txt); return false; };
    const result = async () => p.evaluate(() => { const els = [...document.querySelectorAll('div')].filter(d => /=\s*\S+.*\/|샤프·플랫 없음|No sharps or flats/.test(d.textContent) && d.children.length === 0); return els.map(e => e.textContent).slice(0, 2).join(' || '); });
    await hs('open');
    await p.screenshot({ path: OUT + `kf-${lang}-${w}-open.png`, fullPage: true });
    // add three sharps one by one: A major / F# minor
    for (let i = 0; i < 3; i++) await btn(L ? '+ Next one' : '+ 다음 하나');
    log.push('3sharps: ' + await result());
    await p.screenshot({ path: OUT + `kf-${lang}-${w}-3sharps.png`, fullPage: true });
    // flats: 4 flats = Ab major
    await btn(L ? 'Flats' : '플랫', 'button.chip');
    for (let i = 0; i < 4; i++) await btn(L ? '+ Next one' : '+ 다음 하나');
    log.push('4flats: ' + await result());
    await p.screenshot({ path: OUT + `kf-${lang}-${w}-4flats.png`, fullPage: true });
    // all seven
    for (let i = 0; i < 3; i++) await btn(L ? '+ Next one' : '+ 다음 하나');
    log.push('7flats: ' + await result());
    await hs('7flats');
    // circle: click each of the 12 slots, record the result; then the alt chip
    const slots = await p.locator('svg g[role=button]').count();
    log.push('slots=' + slots);
    const res = [];
    for (let i = 0; i < slots; i++) { await p.locator('svg g[role=button]').nth(i).click({ force: true }); await p.waitForTimeout(120); res.push(await result()); }
    log.push('circle: ' + res.join(' ; '));
    await hs('circle');
    // sections
    await btn(L ? 'Place them yourself' : '직접 놓아 보기', 'button.chip'); await hs('place');
    await p.screenshot({ path: OUT + `kf-${lang}-${w}-place.png`, fullPage: true });
    await btn(L ? 'Relative minor' : '나란한조', 'button.chip'); await hs('minor');
    await p.screenshot({ path: OUT + `kf-${lang}-${w}-minor.png`, fullPage: true });
    console.log(lang, w, log.join(' | '), 'errs=' + JSON.stringify(p._errs));
    await p.context().close();
  }
  await H.close();
})();
