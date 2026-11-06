// screenshots of the street map: phone and wide, en and ko, with chapter 1 done and chapter 2 started
const { start } = require('./contentharness');
(async () => {
  const H = await start(process.env.BUILD || 'drills.t425.html');
  const store = { pb_lesson_steps_v1: JSON.stringify({ 'posture-hands': { 0: 1, 1: 1, 3: 1, 5: 1, 6: 1, 7: 1 }, 'first-steps': { 0: 1 } }), pb_steps_total_v1: JSON.stringify({ 'posture-hands': 6, 'first-steps': 9 }) };
  for (const [w, lang] of (process.env.SIZES ? JSON.parse(process.env.SIZES) : [[390, 'en'], [1280, 'en'], [390, 'ko']])) {
    const p = await H.open({ path: '', w, h: 900, store, lang, dsf: 2 }); await p.waitForTimeout(900);
    const m = await p.$('[data-house]'); await m.screenshot({ path: 'p425/shot-' + w + '-' + lang + '.png' });
    console.log(w, lang, 'errs', p._errs.join('|').slice(0, 200));
    await p.context().close();
  }
  await H.close();
})().catch(e => { console.error('CRASH', e); process.exit(1); });
