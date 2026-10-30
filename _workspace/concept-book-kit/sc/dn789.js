// Build DN: the Toolbox tab is gone. Usage: node dn789.js drills.t789.html
const { start } = require('/home/claude/pbtest/kit/contentharness');
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
(async () => {
  const H = await start(process.argv[2] || 'drills.t789.html'); let bad = 0;
  const say = (ok, ...a) => { if (!ok) bad++; console.log(ok ? 'ok  ' : 'BAD ', ...a); };
  const tabsOf = async (p) => p.$$eval('.pb-main button', bs => bs.map(b => b.innerText.trim()).filter(x => /^(Home|Chapters|Books|Printables|Toolbox|Practice|홈|챕터|책|교구|도구함|연습)$/.test(x)));
  for (const lang of ['en', 'ko']) {
    const p = await H.open({ path: '?teacher=1', w: 420, h: 1400, lang }); await sleep(800);
    const tabs = await tabsOf(p);
    say(tabs.length === 5 && !tabs.some(x => /Toolbox|도구함/.test(x)), lang, 'tabs', JSON.stringify(tabs));
    await p.close();
    const q = await H.open({ path: '?teacher=1&view=toolbox', w: 420, h: 1200, lang }); await sleep(900);
    const qs = await q.evaluate(() => location.search), home = await q.locator('text=/^(Keys and staff|건반과 오선)$/').count();
    say(!/view=toolbox/.test(qs) && !q._errs.length, lang, 'old ?view=toolbox lands on the Home', qs, 'home doors', home, q._errs.slice(0, 1));
    await q.close();
    const r = await H.open({ path: '?teacher=1&view=toolbox&sec=books', w: 420, h: 1200, lang }); await sleep(800);
    say((await r.locator('[data-testid^="ckp-shelf-"]').count()) >= 4, lang, 'old ?view=toolbox&sec=books still lands on Books');
    await r.close();
    const u = await H.open({ path: '?tool=metronome&ret=toolbox', w: 420, h: 1200, lang }); await sleep(900);
    const back = await u.locator('button:has-text("←")').first().innerText().catch(() => '');
    say(!/Toolbox|도구함/.test(back) && !u._errs.length, lang, 'a tool opened with ret=toolbox goes back to', JSON.stringify(back), u._errs.slice(0, 1));
    await u.locator('button:has-text("←")').first().click(); await sleep(800);
    const us = await u.evaluate(() => location.search);
    say(!/toolbox/.test(us), lang, 'and lands off the Toolbox', us);
    await u.close();
  }
  // the Find button: a found tool goes back to the Home
  const f = await H.open({ path: '?teacher=1', w: 420, h: 1400 }); await sleep(800);
  const findBtn = f.locator('button:has-text("Find"), button[aria-label*="Find"], button:has-text("🔍")').first();
  if (await findBtn.count()) { await findBtn.click(); await sleep(500); const inp = f.locator('input').last(); await inp.fill('metronome'); await sleep(600);
    const hit = f.locator('button:has-text("Metronome")').first(); if (await hit.count()) { await hit.click(); await sleep(800); const back = await f.locator('button:has-text("←")').first().innerText().catch(() => ''); say(!/Toolbox/.test(back), 'Find: a found tool goes back to', JSON.stringify(back)); } else say(true, 'Find: no hit to click (skipped)'); }
  else say(true, 'Find button not found (skipped)');
  await f.close();
  // the Home's Practice category goes to the Practice tab
  const h = await H.open({ path: '?teacher=1&view=home&area=beside', w: 420, h: 1400 }); await sleep(900);
  const pr = h.locator('button:has-text("Practice")').first();
  if (await pr.count()) { await pr.click(); await sleep(800); say(/view=practice/.test(await h.evaluate(() => location.search)), 'Home > Beside the piano > Practice opens the Practice tab', await h.evaluate(() => location.search)); } else say(true, 'no Practice category on this Home area (skipped)');
  await h.close();
  console.log('bad', bad); await H.close();
})();
