const { start } = require('/home/claude/pbtest/kit/contentharness');
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
(async () => {
  const H = await start(process.argv[2]);
  const q0 = await H.open({ path: '?view=path', w: 390, h: 900 }); const ids = await q0.evaluate((all) => all ? pathIds() : pathStageIds(PATH_STAGES[0]), !!process.env.ALL); await q0.close();
  const out = [];
  for (const id of ids) {
    const p = await H.open({ path: '?book=lesson&ch=' + id, w: 900, h: 1200 }); await sleep(1200);
    const r = await p.evaluate(() => [...document.querySelectorAll('.bk-page')].map((pg, i) => [...pg.querySelectorAll('.lb-pic')].map(el => { const kids = [...el.children].filter(c => !c.matches('[class*=frame]')); const top = el.getBoundingClientRect(); let over = 0; kids.forEach(c => { const b = c.getBoundingClientRect(); over = Math.max(over, b.bottom - (top.bottom - 4), (top.top + 4) - b.top); }); return over > 1 ? (i + 1) + ':' + Math.round(over) : null; }).filter(Boolean)).flat());
    out.push(id + ' ' + JSON.stringify(r));
    await p.close();
  }
  console.log(out.join('\n'));
  await H.close();
})();
