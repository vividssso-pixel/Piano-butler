// Build DZ: Rhythm, Grade 2's Split the beat (six ways, no dotted one); Grade 3's keeps seven.
const { start } = require('/home/claude/pbtest/kit/contentharness');
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
const SH = '/tmp/claude-0/-home-claude/c245f740-5546-5c71-9064-9bfc4952b3ac/scratchpad/';
(async () => {
  const H = await start(process.argv[2] || 'drills.t802.html'); let bad = 0;
  const say = (ok, ...a) => { if (!ok) bad++; console.log(ok ? 'ok  ' : 'BAD ', ...a); };
  for (const lang of ['en', 'ko']) {
    const p = await H.open({ path: '?drill=rhythm-2', w: 400, h: 1400, dsf: 1.5, lang }); await sleep(1200);
    await p.locator('section > button').nth(1).click(); await sleep(800);
    const m = p.locator('[data-step-make="mk-split2"]'); await m.scrollIntoViewIfNeeded();
    const seen = new Set(); const cell = m.locator('.choice-btn').nth(0);
    for (let i = 0; i < 7; i++) { seen.add((await cell.innerText()).replace(/\s+/g, ' ')); await cell.click(); await sleep(120); }
    const txt = await m.innerText();
    say(seen.size === 6 && ![...seen].some(x => /dotted|점8분/.test(x)) && /six ways|여섯 가지/.test(txt) && !p._errs.length, lang, 'rhythm-2: six ways, no dotted one', [...seen].join(' | '), p._errs.slice(0, 1));
    if (lang === 'ko') await m.screenshot({ path: SH + 'dz-split2.png' });
    await p.close();
  }
  // Split the beat, Grade 3 still has seven
  const r = await H.open({ path: '?drill=rhythm-3', w: 400, h: 1400, dsf: 1 }); await sleep(1100);
  const txt3 = await r.locator('[data-step-make="mk-split"]').innerText(); say(/seven ways/.test(txt3) && !r._errs.length, 'rhythm-3 keeps seven ways'); await r.close();
  console.log('bad', bad); await H.close();
})();
