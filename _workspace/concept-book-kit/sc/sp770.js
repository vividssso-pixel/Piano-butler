const { start } = require('/home/claude/pbtest/kit/contentharness');
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
(async () => {
  const H = await start(process.argv[2]); let bad = 0;
  const q0 = await H.open({ path: '?view=path', w: 390, h: 900 }); const ids = await q0.evaluate(() => pathStageIds(PATH_STAGES[0])); await q0.close();
  for (const id of ids) for (const kind of ['spread', 'teacher', 'work']) {
    const p = await H.open({ path: '?book=' + kind + '&ch=' + id, w: 900, h: 1200 }); await sleep(1100);
    const ov = await p.evaluate(() => [...document.querySelectorAll('.bk-page')].filter(el => el.scrollHeight > el.clientHeight + 2).length);
    if (ov || p._errs.length) { bad++; console.log('BAD', kind, id, ov, p._errs[0] || ''); }
    await p.close();
  }
  console.log('spread/teacher/work bad', bad); await H.close();
})();
