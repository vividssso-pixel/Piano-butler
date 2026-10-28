// Build CS: the house as the teacher dashboard needs it (floors, rooms, theory marks, checkpoints), taken from a drills build
const { start } = require('/home/claude/pbtest/kit/contentharness');
(async () => {
  const H = await start(process.argv[2] || 'drills.t765.html');
  const p = await H.open({ path: '?view=path', w: 390, h: 900 });
  const d = await p.evaluate(() => {
    const floors = PATH_STAGES.map((st, k) => ({ k, name: st.en[0], extra: !!stageExtra(st), rooms: pathStageIds(st).map(id => [id, bkChapterNo(id), bkChapterName(id), THEORY_ROOM[id] || 0, CHECK_LV[id] ? 1 : 0]) }));
    const cps = checkFloors().map(f => ({ key: f.key, k: f.k, part: f.part || 0 }));
    return { floors, cps };
  });
  console.log(JSON.stringify(d));
  await H.close();
})();
