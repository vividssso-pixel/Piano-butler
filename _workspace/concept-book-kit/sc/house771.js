const { start } = require('/home/claude/pbtest/kit/contentharness');
(async () => { const H = await start(process.argv[2] || 'drills.t771.html'); const S = '/tmp/claude-0/-home-claude/c245f740-5546-5c71-9064-9bfc4952b3ac/scratchpad/shots/';
  for (const lang of ['en', 'ko']) { const p = await H.open({ path: '?view=chapters', w: 390, h: 1400, lang, dsf: 1 }); await p.waitForTimeout(1500);
    const door = p.locator('[data-hall] svg').first(); if (await door.count()) { await door.click(); await p.waitForTimeout(1800); }
    const hv = p.locator('[data-house-view]').first();
    const txt = await p.evaluate(() => [...document.querySelectorAll('[data-house-view] svg text')].map(x => x.textContent).join(' | '));
    const plaques = (txt.match(/(BEGINNER|PRELIM|GRADE \d|FLOOR[^|]*|\d층[^|]*)/g) || []);
    console.log(lang, /FLOOR|\d층/.test(txt) ? 'BAD' : 'ok', plaques.slice(0, 12).join(', '), p._errs.slice(0, 1));
    if (await hv.count()) await hv.screenshot({ path: S + 'house771-' + lang + '.png' });
    await p.close(); }
  await H.close(); })();
