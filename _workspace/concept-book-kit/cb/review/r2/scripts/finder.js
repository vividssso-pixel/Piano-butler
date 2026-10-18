const { start } = require('/home/claude/pbtest/kit/contentharness');
(async () => {
  const H = await start('drills.t485.html');
  for (const k of ['Gb', 'F%23', 'Db', 'B']) {
    const p = await H.open({ path: '?tool=scale-finder&key=' + k + '&lock=1', w: 390, h: 860, dsf: 1 }); await p.waitForTimeout(1500);
    const r = await p.evaluate(() => { const inp = document.querySelector('input'); const act = [...document.querySelectorAll('button.active, .chip.active')].map(b => b.innerText.trim()).slice(0, 4);
      const body = document.body.innerText; const m = body.match(/([A-G][♯♭#b]?[^\n]{0,12}(major|minor))/); return { input: inp && inp.value, active: act, first: m && m[1], url: location.search }; });
    console.log(k, JSON.stringify(r), p._errs.join('|').slice(0, 100));
    await p.context().close();
  }
  await H.close();
})();
