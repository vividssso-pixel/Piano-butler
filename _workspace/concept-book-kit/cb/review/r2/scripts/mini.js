const { start } = require('/home/claude/pbtest/kit/contentharness');
(async () => {
  const H = await start('drills.t485.html');
  const p = await H.open({ path: '?teacher=1&tool=cb-p-scales', w: 390, h: 860, dsf: 1 }); await p.waitForTimeout(1300);
  const r = await p.evaluate(() => { const lad = document.querySelector('.cb-ladder'); const svgs = [...lad.querySelectorAll('svg')]; const s = svgs[svgs.length - 1];
    return svgs.map(s => ({ w: Math.round(s.getBoundingClientRect().width), aria: s.getAttribute('aria-hidden'), role: s.getAttribute('role'), label: s.getAttribute('aria-label'), texts: s.querySelectorAll('text').length, gkeys: s.querySelectorAll('g[data-key]').length, tab: s.querySelectorAll('[tabindex]').length })); });
  console.log(JSON.stringify(r));
  await H.close();
})();
