// Build DX: The Piano's Story's free-play toys: the three keyboards and the bass, the strings, the pedal playground, 88 keys.
// Usage: node dx800.js drills.t800.html [shots]
const { start } = require('/home/claude/pbtest/kit/contentharness');
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
const SH = '/tmp/claude-0/-home-claude/c245f740-5546-5c71-9064-9bfc4952b3ac/scratchpad/';
(async () => {
  const H = await start(process.argv[2] || 'drills.t800.html'); let bad = 0;
  const say = (ok, ...a) => { if (!ok) bad++; console.log(ok ? 'ok  ' : 'BAD ', ...a); };
  for (const lang of ['en', 'ko']) {
    const p = await H.open({ path: '?drill=piano-story', w: 400, h: 1800, dsf: 1.5, lang }); await sleep(1200);
    const open = async (k) => { if (k) { await p.locator('section > button').nth(k).click(); await sleep(800); } const b = p.locator('section').nth(k).locator('[data-step-play]'); await b.scrollIntoViewIfNeeded(); return b; };
    const tapAt = async (loc, fx, fy) => { const bb = await loc.boundingBox(); await p.mouse.move(bb.x + bb.width * fx, bb.y + bb.height * fy); await p.mouse.down(); await sleep(120); await p.mouse.up(); await sleep(150); };
    // 1: the keyboards
    let b = await open(0); const keys = b.locator('[data-sps9="keys"]');
    await keys.locator('button.chip').nth(2).click(); await sleep(150);
    await tapAt(keys.locator('[data-key="64"]'), 0.5, 0.9); const m1 = await keys.evaluate(e => e.querySelector('div[style*="transition: width"]').style.width);
    await tapAt(keys.locator('[data-key="64"]'), 0.5, 0.1); const m2 = await keys.evaluate(e => e.querySelector('div[style*="transition: width"]').style.width);
    await keys.locator('[data-sps9-bass]').click(); await sleep(400); const bt = await keys.locator('[data-sps9-bass]').innerText(); await keys.locator('[data-sps9-bass]').click();
    say(parseFloat(m1) > parseFloat(m2) && /Stop|멈추기/.test(bt) && !p._errs.length, lang, 'keyboards: the front is louder on the piano; the bass starts', m1, m2, bt, p._errs.slice(0, 1));
    if (process.argv[3]) await keys.screenshot({ path: SH + 'dx-keys-' + lang + '.png' });
    // 3: the strings
    b = await open(2); const harp = b.locator('[data-sps9="harp"] svg'); const hb = await harp.boundingBox();
    await p.mouse.move(hb.x + hb.width * 0.08, hb.y + hb.height * 0.85); await p.mouse.down();
    for (let i = 1; i <= 12; i++) { await p.mouse.move(hb.x + hb.width * (0.08 + i * 0.07), hb.y + hb.height * 0.85); await sleep(25); }
    const wob = await b.evaluate(e => e.querySelectorAll('.sps9-ring').length); await p.mouse.up();
    say(wob >= 8 && !p._errs.length, lang, 'strings: a slide sounds every string it crosses', wob, p._errs.slice(0, 1));
    if (process.argv[3]) { await sleep(100); await b.locator('[data-sps9="harp"]').screenshot({ path: SH + 'dx-harp-' + lang + '.png' }); }
    // 4: the pedals
    b = await open(3); const pp = b.locator('[data-sps9="pedals"]'); const ped = (i) => pp.locator('[data-sps9-pedals] svg > g').nth(i + 1).click();
    const glow = () => pp.evaluate(e => [...e.querySelectorAll('[data-key]')].filter(r => r.getAttribute('fill') === '#f6b9a6').length);
    await tapAt(pp.locator('[data-key="60"]'), 0.5, 0.8); const g0 = await glow();
    await ped(2); await sleep(150); await tapAt(pp.locator('[data-key="64"]'), 0.5, 0.8); await tapAt(pp.locator('[data-key="67"]'), 0.5, 0.8); const g1 = await glow(); const st1 = await pp.locator('[data-sps9-status]').innerText();
    await ped(2); await sleep(200); const g2 = await glow();
    say(g0 === 0 && g1 === 2 && g2 === 0 && /Right pedal|오른쪽 페달/.test(st1) && !p._errs.length, lang, 'pedals: notes ring on with the right pedal, stop when it comes up', g0, g1, g2, p._errs.slice(0, 1));
    if (process.argv[3]) { await ped(2); await tapAt(pp.locator('[data-key="72"]'), 0.5, 0.8); await pp.screenshot({ path: SH + 'dx-pedals-' + lang + '.png' }); await ped(2); }
    // 5: 88 keys
    b = await open(4); const sl = b.locator('[data-sps9="slide"] svg'); const sb = await sl.boundingBox();
    await p.mouse.move(sb.x + 2, sb.y + sb.height * 0.85); await p.mouse.down();
    for (let i = 1; i <= 120; i++) { await p.mouse.move(sb.x + 2 + (sb.width - 4) * i / 120, sb.y + sb.height * 0.85); await sleep(8); }
    await p.mouse.up(); await sleep(200); const cs = await b.locator('[data-sps9-cs]').innerText();
    say(/all 8 Cs|C 8개 모두/.test(cs) && !p._errs.length, lang, '88 keys: a slide passes all eight Cs', cs.replace(/\s+/g, ' '), p._errs.slice(0, 1));
    if (process.argv[3]) await b.locator('[data-sps9="slide"]').screenshot({ path: SH + 'dx-slide-' + lang + '.png' });
    const over = await p.evaluate(() => document.scrollingElement.scrollWidth); say(over <= 402, lang, 'no sideways scroll', over);
    await p.close();
  }
  console.log('bad', bad); await H.close();
})();
