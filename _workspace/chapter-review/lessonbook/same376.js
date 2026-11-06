// The printed books must not change: Lesson Book, Workbook, Teacher copy and the side-by-side print, t373 vs t376
const { start } = require('./contentharness');
(async () => {
  const out = {};
  for (const b of ['drills.t373.html', 'drills.t376.html']) {
    const H = await start(b);
    for (const k of ['lesson', 'work', 'teacher', 'spread']) {
      const p = await H.open({ path: '?book=' + k + '&ch=posture-hands&lang=en', w: 900, h: 1200 });
      await p.waitForTimeout(1200);
      out[b + k] = await p.evaluate(() => document.querySelector('#root').innerHTML);
      out[b + k + 'err'] = p._errs.join('|');
      await p.context().close();
    }
    await H.close();
  }
  for (const k of ['lesson', 'work', 'teacher', 'spread']) {
    const a = out['drills.t373.html' + k], b = out['drills.t376.html' + k];
    let i = 0; while (i < a.length && a[i] === b[i]) i++;
    console.log(k, a === b ? 'SAME' : 'DIFF at ' + i + ': ' + JSON.stringify(a.slice(i - 80, i + 120)) + '\n   new: ' + JSON.stringify(b.slice(i - 80, i + 120)), out['drills.t376.html' + k + 'err']);
  }
})().catch(e => { console.error('CRASH', e); process.exit(1); });
