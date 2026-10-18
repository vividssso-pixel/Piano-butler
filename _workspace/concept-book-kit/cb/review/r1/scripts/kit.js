const { start } = require('/home/claude/pbtest/kit/contentharness');
(async () => {
  const H = await start('drills.t485.html');
  for (const path of ['?kit=cb-p-scales,ssc-steps,ssc-g&kn=Scales%3A%20First&lock=1', '?teacher=1&kit=ssc-steps,ssc-g,ssc-f,skg-five&kn=First']) {
    const p = await H.open({ path, w: 390, h: 860 });
    const txt = await p.evaluate(() => document.body.innerText.replace(/\s+/g, ' ').slice(0, 600));
    console.log(path + '\n  ' + txt + '\n  errs=' + JSON.stringify(p._errs));
    await p.screenshot({ path: '/home/claude/pbtest/cb/review/r1/shots/kit-' + (path.includes('lock') ? 'student' : 'teacher') + '.png' });
    await p.context().close();
  }
  await H.close();
})();
