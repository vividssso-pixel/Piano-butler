// Phase 377: the chapter map is the Piano Butler's House
const { start } = require('./contentharness');
const ok = (c, m) => { console.log((c ? 'PASS ' : 'FAIL ') + m); if (!c) process.exitCode = 1; };
(async () => {
  const H = await start(process.env.BUILD || 'drills.t377.html');
  const store = { pb_lesson_steps_v1: JSON.stringify({ 'posture-hands': { 0: 1, 1: 1, 3: 1, 5: 1, 6: 1, 7: 1 }, 'first-steps': { 0: 1 } }), pb_steps_total_v1: JSON.stringify({ 'posture-hands': 6, 'first-steps': 9 }) };
  for (const [w, lang] of [[390, 'en'], [320, 'en'], [1024, 'en'], [390, 'ko']]) {
    const p = await H.open({ path: '', w, h: 900, store, lang }); await p.waitForTimeout(900);
    const r = await p.evaluate(() => {
      const m = document.querySelector('[data-house]'), svg = m.querySelector('svg'), sb = svg.getBoundingClientRect();
      const rooms = [...m.querySelectorAll('[data-chapter]')];
      const here = rooms.filter(e => e.dataset.here === '1').map(e => e.dataset.chapter);
      const fig = m.querySelector('[data-testid="map-figure"]'), fb = fig && fig.getBoundingClientRect();
      const hereRoom = rooms.find(e => e.dataset.here === '1'), hb = hereRoom && hereRoom.getBoundingClientRect();
      const texts = [...svg.querySelectorAll('text')].filter(t => { const b = t.getBoundingClientRect(); return b.right > sb.right + 1 || b.left < sb.left - 1; }).map(t => t.textContent);
      return { order: rooms.map(e => e.dataset.chapter).join(','), want: pathIds().join(','), floors: m.querySelectorAll('[data-map-stage]').length, here,
        status: rooms.slice(0, 3).map(e => e.dataset.status).join(','), count: document.querySelector('[data-testid="map-count"]').textContent,
        figOnFloor: !!(fb && hb && fb.bottom > hb.top - 4 && fb.top < hb.bottom + 4), roles: rooms.every(e => e.getAttribute('role') === 'button' && e.getAttribute('tabindex') === '0' && e.getAttribute('aria-label')),
        out: texts, sw: document.documentElement.scrollWidth, cw: document.documentElement.clientWidth };
    });
    const tag = w + 'px ' + lang + ': ';
    ok(r.order === r.want, tag + 'H1 26 rooms in the map\'s order');
    ok(r.floors === 7, tag + 'H2 seven floors');
    ok(r.here.join() === 'first-steps' && r.status === 'done,started,new', tag + 'H3 one "you are here" (chapter 2), chapter 1 done: ' + r.here + ' / ' + r.status);
    ok(lang === 'ko' ? /26개 챕터 중 1개 완료/.test(r.count) : /1 of 26 chapters done/.test(r.count), tag + 'H4 ' + r.count);
    ok(r.figOnFloor, tag + 'H5 the siblings stand on the floor of the room you are in');
    ok(r.roles, tag + 'H6 every room is a button with a name');
    ok(r.out.length === 0 && r.sw <= r.cw, tag + 'H7 nothing runs off the drawing or the screen' + (r.out.length ? ' ' + r.out.join(' | ') : '') + ' (' + r.sw + '/' + r.cw + ')');
    ok(p._errs.length === 0, tag + 'H8 no errors ' + p._errs.join('|').slice(0, 160));
    if (w === 390 && lang === 'en') {
      await p.click('[data-house] [data-chapter="tempo"]'); await p.waitForTimeout(400);
      ok(/drill=tempo/.test(await p.evaluate(() => location.search)), 'H9 tapping a room opens that chapter');
      await p.goto(H.base + '/drills.html'); await p.waitForTimeout(800);
      await p.focus('[data-house] [data-chapter="scales"]'); await p.keyboard.press('Enter'); await p.waitForTimeout(400);
      ok(/drill=scales/.test(await p.evaluate(() => location.search)), 'H10 Enter on a focused room opens it');
    }
    await p.context().close();
  }
  await H.close();
})().catch(e => { console.error('CRASH', e); process.exit(1); });
