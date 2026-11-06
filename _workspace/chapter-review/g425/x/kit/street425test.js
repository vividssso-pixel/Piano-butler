// Phase 425: the chapter map is a street (replaces house402test.js): the buildings, the windows, Clara, the board
const { start } = require('./contentharness');
const ok = (c, m) => { console.log((c ? 'PASS ' : 'FAIL ') + m); if (!c) process.exitCode = 1; };
(async () => {
  const H = await start(process.env.BUILD || 'drills.t425.html');
  const store = { pb_lesson_steps_v1: JSON.stringify({ 'posture-hands': { 0: 1, 1: 1, 3: 1, 5: 1, 6: 1, 7: 1 }, 'first-steps': { 0: 1 } }), pb_steps_total_v1: JSON.stringify({ 'posture-hands': 6, 'first-steps': 9 }) };
  for (const [w, lang] of [[390, 'en'], [320, 'en'], [1024, 'en'], [1440, 'en'], [390, 'ko']]) {
    const p = await H.open({ path: '', w, h: 900, store, lang }); await p.waitForTimeout(900);
    const r = await p.evaluate(() => {
      const m = document.querySelector('[data-house]'), street = m.querySelector('[data-street]');
      const wins = [...street.querySelectorAll('[data-chapter]')];
      const here = wins.filter(e => e.dataset.here === '1').map(e => e.dataset.chapter);
      const fig = m.querySelector('[data-testid="map-figure"]'), fb = fig && fig.getBoundingClientRect();
      const hw = wins.find(e => e.dataset.here === '1'), hb = hw && hw.getBoundingClientRect();
      const out = [];
      m.querySelectorAll('svg').forEach(svg => { const sb = svg.getBoundingClientRect(); svg.querySelectorAll('text').forEach(t => { const b = t.getBoundingClientRect(); if (b.right > sb.right + 1 || b.left < sb.left - 1) out.push(t.textContent); }); });
      const board = m.querySelector('[data-testid="map-board"]'), bb = board.getBoundingClientRect(), sbx = street.getBoundingClientRect();
      const squares = [...board.querySelectorAll('[data-goto]')].map(e => e.dataset.goto);
      const bc = board.querySelector('[data-testid="board-clara"]'), bcb = bc && bc.getBoundingClientRect();
      const hsq = board.querySelector('[data-goto="' + (here[0] || '') + '"]'), hsb = hsq && hsq.getBoundingClientRect();
      return { order: wins.map(e => e.dataset.chapter).join(','), want: pathIds().join(','), stages: m.querySelectorAll('[data-map-stage]').length, here,
        status: wins.slice(0, 3).map(e => e.dataset.status).join(','), count: document.querySelector('[data-testid="map-count"]').textContent,
        figIn: !!(fb && hb && fb.left >= hb.left - 1 && fb.right <= hb.right + 1 && fb.top >= hb.top - 1 && fb.bottom <= hb.bottom + 1),
        roles: wins.every(e => e.getAttribute('role') === 'button' && e.getAttribute('tabindex') === '0' && e.getAttribute('aria-label')),
        out, sw: document.documentElement.scrollWidth, cw: document.documentElement.clientWidth, layout: m.dataset.layout,
        squares: squares.join(','), boardHidden: board.getAttribute('aria-hidden') === 'true',
        claraOnSquare: !!(bcb && hsb && bcb.left >= hsb.left - 1 && bcb.right <= hsb.right + 1 && bcb.bottom <= hsb.bottom + 1),
        side: bb.right <= sbx.left, above: bb.bottom <= sbx.top + 1, streetW: Math.round(sbx.width) };
    });
    const tag = w + 'px ' + lang + ': ';
    ok(r.order === r.want, tag + 'S1 26 windows on the street, in the map\'s order');
    ok(r.stages === 7, tag + 'S2 seven buildings');
    ok(r.here.join() === 'first-steps' && r.status === 'done,started,new', tag + 'S3 one "you are here" (chapter 2), chapter 1 done: ' + r.here + ' / ' + r.status);
    ok(lang === 'ko' ? /26개 챕터 중 1개 완료/.test(r.count) : /1 of 26 chapters done/.test(r.count), tag + 'S4 ' + r.count);
    ok(r.figIn, tag + 'S5 Clara stands in the window of the chapter you are on');
    ok(r.roles, tag + 'S6 every window is a button with a name');
    ok(r.out.length === 0 && r.sw <= r.cw, tag + 'S7 nothing runs off a drawing or the screen' + (r.out.length ? ' ' + r.out.join(' | ') : '') + ' (' + r.sw + '/' + r.cw + ')');
    ok(p._errs.length === 0, tag + 'S8 no errors ' + p._errs.join('|').slice(0, 160));
    ok(r.squares === r.want && r.boardHidden && r.claraOnSquare, tag + 'B1 the board: 26 squares in order, Clara on your square, hidden from screen readers (the street has the buttons)');
    ok(r.layout === 'wide' ? r.side : r.above, tag + 'B2 the board ' + (r.layout === 'wide' ? 'beside' : 'above') + ' the street (' + r.layout + ', street ' + r.streetW + 'px)');
    if (w === 390 && lang === 'en') {
      await p.click('[data-house] [data-goto="scales"]'); await p.waitForTimeout(900);
      const v = await p.evaluate(() => { const e = document.querySelector('[data-street] [data-chapter="scales"]').getBoundingClientRect(); return e.top >= 0 && e.bottom <= innerHeight; });
      ok(v, 'B3 a square on the board finds its window on the street');
      await p.click('[data-street] [data-chapter="tempo"]'); await p.waitForTimeout(400);
      ok(/drill=tempo/.test(await p.evaluate(() => location.search)), 'S9 tapping a window opens that chapter');
      await p.goto(H.base + '/drills.html'); await p.waitForTimeout(800);
      await p.focus('[data-street] [data-chapter="scales"]'); await p.keyboard.press('Enter'); await p.waitForTimeout(400);
      ok(/drill=scales/.test(await p.evaluate(() => location.search)), 'S10 Enter on a focused window opens it');
      // the student page's small map: the board alone, its squares the buttons
      await p.goto(H.base + '/drills.html'); await p.waitForTimeout(800);
      const c = await p.evaluate(() => new Promise(res => {
        const d = document.createElement('div'); d.id = 'cmp'; document.body.appendChild(d); let opened = null;
        ReactDOM.createRoot(d).render(React.createElement(HouseMap, { compact: true, onOpen: id => { opened = id; } }));
        setTimeout(() => { const btns = [...d.querySelectorAll('[data-chapter]')]; const s = d.querySelector('[data-chapter="pulse"]'); s && s.dispatchEvent(new MouseEvent('click', { bubbles: true }));
          res({ n: btns.length, order: btns.map(b => b.dataset.chapter).join(',') === pathIds().join(','), street: !!d.querySelector('[data-street]'), opened, roles: btns.every(e => e.getAttribute('role') === 'button' && e.getAttribute('tabindex') === '0') }); }, 600);
      }));
      ok(c.n === 26 && c.order && !c.street && c.roles && c.opened === 'pulse', 'C1 compact: the board alone, its 26 squares open their chapters ' + JSON.stringify(c));
    }
    await p.context().close();
  }
  await H.close();
})().catch(e => { console.error('CRASH', e); process.exit(1); });
