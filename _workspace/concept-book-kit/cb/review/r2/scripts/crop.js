// Zoomed crops of the printed book: node crop.js <lang> <page> <x> <y> <w> <h> <name> [dsf]
// coordinates are CSS px relative to the page element ([data-lb-page=N])
const { start } = require('/home/claude/pbtest/kit/contentharness');
const OUT = '/home/claude/pbtest/cb/review/r2/shots/';
(async () => {
  const jobs = JSON.parse(process.argv[2]);
  const H = await start('drills.t485.html');
  const byLang = {};
  for (const j of jobs) (byLang[j.lang] = byLang[j.lang] || []).push(j);
  for (const lang in byLang) {
    const p = await H.open({ path: '?book=concept&ch=p-scales&lang=' + lang, w: 900, h: 1300, dsf: 3 });
    await p.waitForTimeout(2500);
    for (const j of byLang[lang]) {
      const pg = await p.$('[data-lb-page="' + j.page + '"]'); const b = await pg.boundingBox();
      await p.screenshot({ path: OUT + 'z-' + j.name + '.png', clip: { x: b.x + j.x, y: b.y + j.y, width: j.w, height: j.h }, fullPage: true });
    }
    await p.context().close();
  }
  await H.close();
})();
