const { start } = require('/home/claude/pbtest/kit/contentharness');
(async () => {
  const H = await start('drills.t485.html');
  for (const path of ['?teacher=1&tool=cb-p-scales', '?drill=scales&tab=learn', '?drill=key-signatures&tab=learn']) {
    const p = await H.open({ path, w: 390, h: 860 });
    const labs = await p.$$eval('[data-five-checks] button[aria-label]', a => a.map(b => b.getAttribute('aria-label')));
    const bad = labs.filter(l => /object/.test(l));
    console.log(path + ': five-check buttons=' + labs.length + ' with [object]=' + bad.length + ' e.g. ' + JSON.stringify(labs.slice(0, 2)));
    const imgs = await p.$$eval('[role=img]', a => a.map(x => x.getAttribute('aria-label')).filter(x => !x || /undefined|object/.test(x)));
    console.log('   role=img without a good label: ' + imgs.length + ' ' + JSON.stringify(imgs.slice(0, 4)));
    await p.context().close();
  }
  await H.close();
})();
