// Build EB: The Piano's Story's play inside its pads (keyboards + bass, the pedal playground, the 88-key slide), Strum the
// strings in step 3; the house's pastel corner stones; the grand on longer legs; the toys that repeated their step are gone.
// Usage: node dx804.js drills.t804.html [shots]
const { start } = require('/home/claude/pbtest/kit/contentharness');
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
const SH = '/tmp/claude-0/-home-claude/c245f740-5546-5c71-9064-9bfc4952b3ac/scratchpad/';
(async () => {
  const H = await start(process.argv[2] || 'drills.t804.html'); let bad = 0;
  const say = (ok, ...a) => { if (!ok) bad++; console.log(ok ? 'ok  ' : 'BAD ', ...a); };
  for (const lang of ['en', 'ko']) {
    const p = await H.open({ path: '?drill=piano-story', w: 400, h: 1800, dsf: 1.5, lang }); await sleep(1200);
    const open = async (k) => { if (k) { await p.locator('section > button').nth(k).click(); await sleep(800); } return p.locator('section').nth(k); };
    const tapAt = async (loc, fx, fy) => { const bb = await loc.boundingBox(); await p.mouse.move(bb.x + bb.width * fx, bb.y + bb.height * fy); await p.mouse.down(); await sleep(120); await p.mouse.up(); await sleep(150); };
    // 1: Pluck, push or strike, with the keyboard and the bass inside it
    let sec = await open(0); const pad = sec.locator('[data-sps="sound"]'); await pad.scrollIntoViewIfNeeded();
    await pad.locator('button.chip').nth(2).click(); await sleep(150);
    const meter = () => pad.evaluate(e => e.querySelector('div[style*="transition: width"]').style.width);
    await tapAt(pad.locator('[data-sps9="keys"] [data-key="64"]'), 0.5, 0.9); const m1 = await meter();
    await tapAt(pad.locator('[data-sps9="keys"] [data-key="64"]'), 0.5, 0.1); const m2 = await meter();
    await pad.locator('[data-sps9-bass]').click(); await sleep(300); const bt = await pad.locator('[data-sps9-bass]').innerText();
    await pad.locator('button', { hasText: /^Quiz$|^퀴즈$/ }).click(); await sleep(500); const ch = await pad.locator('.choice-btn').count(); const keysGone = await pad.locator('[data-sps9="keys"]').count();
    say(parseFloat(m1) > parseFloat(m2) && /Stop|멈추기/.test(bt) && ch === 3 && keysGone === 0 && await sec.locator('[data-step-play]').count() === 0 && !p._errs.length, lang, 'step 1: the keyboard and the bass in the pad, its quiz stays', m1, m2, bt, ch, p._errs.slice(0, 1));
    if (process.argv[3] && lang === 'ko') { await pad.locator('button', { hasText: /Back|돌아가기|그만/ }).first().click().catch(() => {}); await sleep(300); await pad.screenshot({ path: SH + 'eb-sound.png' }); }
    // 2: Make a surprise!
    sec = await open(1); say(await sec.locator('[data-step-make="mk-surprise"]').count() === 1, lang, 'step 2: Make a surprise!');
    // 3: Strum the strings
    sec = await open(2); const harp = sec.locator('[data-sps9="harp"] svg'); await harp.scrollIntoViewIfNeeded(); const hb = await harp.boundingBox();
    await p.mouse.move(hb.x + hb.width * 0.08, hb.y + hb.height * 0.85); await p.mouse.down(); for (let i = 1; i <= 12; i++) { await p.mouse.move(hb.x + hb.width * (0.08 + i * 0.07), hb.y + hb.height * 0.85); await sleep(25); }
    const ring = await sec.evaluate(e => e.querySelectorAll('.sps9-ring').length); await p.mouse.up();
    say(ring >= 8 && await sec.locator('[data-step-play]').count() === 1, lang, 'step 3: Strum the strings', ring);
    // 4: The pedals, the playground inside
    sec = await open(3); const pp = sec.locator('[data-sps="pedals"]'); await pp.scrollIntoViewIfNeeded(); const ped = (i) => pp.locator('[data-sps9-pedals] svg > g').nth(i + 1).click();
    const glow = () => pp.evaluate(e => [...e.querySelectorAll('[data-key]')].filter(r => r.getAttribute('fill') === '#f6b9a6').length);
    await tapAt(pp.locator('[data-key="60"]'), 0.5, 0.8); const g0 = await glow();
    await ped(2); await sleep(150); await tapAt(pp.locator('[data-key="64"]'), 0.5, 0.8); await tapAt(pp.locator('[data-key="67"]'), 0.5, 0.8); const g1 = await glow();
    await ped(2); await sleep(200); const g2 = await glow();
    await pp.locator('button', { hasText: /^Quiz$|^퀴즈$/ }).click(); await sleep(400); const pq = await pp.locator('.choice-btn').count();
    say(g0 === 0 && g1 === 2 && g2 === 0 && pq === 2 && await sec.locator('[data-step-play]').count() === 0 && !p._errs.length, lang, 'step 4: the playground in The pedals, its quiz stays', g0, g1, g2, pq, p._errs.slice(0, 1));
    // 5: 88 keys, the slide in the pad; the grand on its longer legs
    sec = await open(4); const kp = sec.locator('[data-sps="keys"]'); await kp.scrollIntoViewIfNeeded(); const sl = kp.locator('[data-sps9="slide"] svg'); const sb = await sl.boundingBox();
    await p.mouse.move(sb.x + 2, sb.y + sb.height * 0.85); await p.mouse.down(); for (let i = 1; i <= 120; i++) { await p.mouse.move(sb.x + 2 + (sb.width - 4) * i / 120, sb.y + sb.height * 0.85); await sleep(8); }
    await p.mouse.up(); await sleep(200); const cs = await kp.locator('[data-sps9-cs]').innerText();
    const grand = await kp.evaluate(e => /scale\(0\.9163\)/.test(e.innerHTML) && /0 20\.88/.test(e.innerHTML));
    say(/all 8 Cs|C 8개 모두/.test(cs) && grand && await sec.locator('[data-step-play]').count() === 0 && !p._errs.length, lang, 'step 5: the slide in the pad, all eight Cs; the grand on longer legs', cs.replace(/\s+/g, ' '), grand, p._errs.slice(0, 1));
    if (process.argv[3] && lang === 'ko') await kp.screenshot({ path: SH + 'eb-keys.png' });
    const over = await p.evaluate(() => document.scrollingElement.scrollWidth); say(over <= 402, lang, 'no sideways scroll', over);
    await p.close();
  }
  // the toys that repeated their step are out of it
  for (const [room, tool] of [['dynamics', 'mk-dyn'], ['tempo', 'mk-tempo'], ['rhythm', 'make-card'], ['ledger-lines', 'mk-ladders'], ['note-names', 'mk-word'], ['harmony-4', 'mk-tunechords']]) {
    const p = await H.open({ path: '?drill=' + room, w: 400, h: 900, dsf: 1 }); await sleep(800);
    const n = await p.evaluate((x) => (MAKE_AT[x.room] ? Object.values(MAKE_AT[x.room]).flat().includes(x.tool) : false), { room, tool });
    say(!n && !p._errs.length, room, tool, 'not in a step'); await p.close(); }
  // the house: a pastel per floor on the corner stones
  const h = await H.open({ path: '?view=path', w: 430, h: 1200, dsf: 1 }); await sleep(1300);
  const tints = await h.evaluate(() => { const set = new Set(['#f6c4cf', '#bfe3d2', '#b9d4ec', '#d3c3ea', '#f3dc9a', '#e7a3b2']); const f = [...document.querySelectorAll('[data-house] svg rect[fill]')].map(r => r.getAttribute('fill')).filter(x => set.has(x)); return { n: f.length, kinds: [...new Set(f)] }; });
  say(tints.n > 40 && tints.kinds.length >= 4 && !h._errs.length, 'the house: pastel corner stones per floor', JSON.stringify(tints));
  await h.close();
  console.log('bad', bad); await H.close();
})();
