// The house map: phone and desktop, a learner partway through chapter 2; rooms, order, taps, no errors
const { start } = require('./contentharness');
(async () => {
  const H = await start(process.env.BUILD || 'drills.t377.html');
  const store = { pb_lesson_steps_v1: JSON.stringify({ 'posture-hands': { 0: 1, 1: 1, 3: 1, 5: 1, 6: 1, 7: 1 }, 'first-steps': { 0: 1 } }), pb_steps_total_v1: JSON.stringify({ 'posture-hands': 6, 'first-steps': 9 }) };
  for (const [w, tag] of [[390, 'phone'], [1000, 'desk']]) {
    const p = await H.open({ path: '', w, h: 900, store });
    await p.waitForTimeout(900);
    const r = await p.evaluate(() => ({ layout: document.querySelector('[data-house]') && document.querySelector('[data-house]').dataset.layout,
      rooms: [...document.querySelectorAll('[data-house] [data-chapter]')].map(e => e.dataset.chapter + ':' + e.dataset.status + (e.dataset.here === '1' ? '*' : '')),
      kids: !!document.querySelector('[data-house] [data-testid="map-figure"] path'), sw: document.documentElement.scrollWidth, count: (document.querySelector('[data-testid="map-count"]') || {}).textContent }));
    console.log(tag, JSON.stringify(r).slice(0, 900), 'errs', p._errs.join('|').slice(0, 200));
    const el = await p.$('[data-house]'); await el.screenshot({ path: '../shots/house377-' + tag + '.png' });
    if (tag === 'desk') { await p.click('[data-house] [data-chapter="note-names"]'); await p.waitForTimeout(500); console.log(' tap note-names ->', await p.evaluate(() => location.search)); }
    await p.context().close();
  }
  await H.close();
})().catch(e => { console.error('CRASH', e); process.exit(1); });
