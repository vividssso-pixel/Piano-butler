const { start } = require('/home/claude/pbtest/kit/contentharness');
const SH = '/tmp/claude-0/-home-claude/c245f740-5546-5c71-9064-9bfc4952b3ac/scratchpad/shots/bk/';
(async () => {
  const H = await start('drills.t767.html'); const sleep = (ms) => new Promise(r => setTimeout(r, ms));
  const p0 = await H.open({ path: '?view=path', w: 390, h: 900 });
  const lv = await p0.evaluate(() => { const ids = pathStageIds(PATH_STAGES[0]); return ids.map(id => [id, chkLevels(id).filter(l => !l.noPrint).map(l => l.n)]); });
  console.log(JSON.stringify(lv)); await p0.close();
  for (const [id, lvs] of lv.slice(0, 7)) { if (!lvs.length) continue;
    const p = await H.open({ path: '?print=1&drill=' + id + '&level=' + lvs[0] + '&n=2', w: 760, h: 1400 }); await sleep(800);
    await p.screenshot({ path: SH + 'pw-' + id + '.png', fullPage: true }); console.log(id, p._errs.slice(0, 1)); await p.close(); }
  await H.close();
})();
