// Phase 436 (from house428test): the plaques have no chess square now. Phase 426: the chapter map is the townhouse (replaces street425test.js): the hall first, the door, the house rising
// above the hall, 26 rooms in the map's order, Clara in your room, the week board, the compact map, the Workbook's page
const { start } = require('./contentharness');
const ok = (c, m) => { console.log((c ? 'PASS ' : 'FAIL ') + m); if (!c) process.exitCode = 1; };
(async () => {
  const H = await start(process.env.BUILD || 'drills.t426.html');
  const store = { pb_lesson_steps_v1: JSON.stringify({ 'posture-hands': { 0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1 }, 'first-steps': { 0: 1 } }), pb_steps_total_v1: JSON.stringify({ 'posture-hands': 6, 'first-steps': 9 }) };
  for (const [w, lang] of [[390, 'en'], [320, 'en'], [1024, 'en'], [1440, 'en'], [390, 'ko']]) {
    const p = await H.open({ path: '', w, h: 900, store, lang }); await p.waitForTimeout(900);
    const tag = w + 'px ' + lang + ': ';
    const a = await p.evaluate(() => { const m = document.querySelector('[data-house]'), d = m.querySelector('[data-door]'), sv = m.querySelector('[data-house-view] svg');
      return { layout: m.dataset.layout, door: !!(d && d.getAttribute('role') === 'button' && d.getAttribute('tabindex') === '0' && d.getAttribute('aria-label')), rooms: m.querySelectorAll('[data-chapter]').length,
        fox: !!m.querySelector('[data-house-view] image'), hint: /Tap the door|문을 눌러/.test(m.textContent), week: !!m.querySelector('[data-testid="map-week"]'), bottom: sv.getBoundingClientRect().bottom + scrollY }; });
    ok(a.layout === 'hall' && a.door && a.rooms === 0 && a.fox && a.hint, tag + 'H1 the map opens on the hall: the fox, the door (a button), no rooms yet, "tap the door"');
    ok(a.week, tag + 'W1 the week board stands above');
    await p.evaluate(() => { const d = document.querySelector('[data-door]'); d.scrollIntoView({ block: 'center' }); });
    const before = await p.evaluate(() => document.querySelector('[data-house-view] svg').getBoundingClientRect().bottom);
    await p.click('[data-door]'); await p.waitForTimeout(1500);
    const r = await p.evaluate(() => {
      const m = document.querySelector('[data-house]'), rooms = [...m.querySelectorAll('[data-chapter]')], sv = m.querySelector('[data-house-view] svg'), sb = sv.getBoundingClientRect();
      const here = rooms.filter(e => e.dataset.here === '1'), hb = here[0] && here[0].querySelector('rect').getBoundingClientRect();
      const fig = m.querySelector('[data-testid="map-figure"]'), fb = fig && fig.getBoundingClientRect();
      const out = []; sv.querySelectorAll('text').forEach(t => { const b = t.getBoundingClientRect(); if (b.right > sb.right + 1 || b.left < sb.left - 1) out.push(t.textContent); });
      const texts = [...sv.querySelectorAll('text')];
      return { layout: m.dataset.layout, order: rooms.map(e => e.dataset.chapter).join(','), want: pathIds().join(','), here: here.map(e => e.dataset.chapter), status: rooms.slice(0, 4).map(e => e.dataset.status).join(','),
        roles: rooms.every(e => e.getAttribute('role') === 'button' && e.getAttribute('tabindex') === '0' && e.getAttribute('aria-label')), bottom: sb.bottom,
        figIn: !!(fb && hb && fb.left >= hb.left - 1 && fb.right <= hb.right + 1 && fb.top >= hb.top - 1 && fb.bottom <= hb.bottom + 1), out, sw: document.documentElement.scrollWidth, cw: document.documentElement.clientWidth,
        count: document.querySelector('[data-testid="map-count"]').textContent, green: sv.querySelectorAll('rect[fill="#2b6e56"]').length, session: sessionStorage.getItem('pb_house_in_v1'),
        coralFloor: texts.some(t => /Cinzel/.test(t.getAttribute('style') || '') && t.getAttribute('fill') === '#e4572e'), classical: texts.some(t => /Cormorant/.test(t.getAttribute('style') || '')),
        fonts: [document.fonts.check('700 12px Cinzel'), document.fonts.check("700 15px 'Cormorant Garamond'")], kingLeft: (() => { const g = [...sv.querySelectorAll('g[transform]')].filter(x => /scale\(0\.3\)/.test(x.getAttribute('transform')) && x.querySelector('path')); return g.length; })() };
    });
    ok(r.layout === 'house' && r.session === '1', tag + 'H2 the door opens the house (and the session remembers)');
    ok(Math.abs(r.bottom - before) <= 3, tag + 'H3 the hall stays where it was, the floors rise above it (' + Math.round(before) + ' -> ' + Math.round(r.bottom) + ')');
    ok(r.order === r.want, tag + 'H4 26 rooms in the map\'s order');
    ok(r.here.join() === 'first-steps' && r.status === 'done,started,new,new', tag + 'H5 one "you are here" (chapter 2), chapter 1 done: ' + r.here + ' / ' + r.status);
    ok(r.figIn, tag + 'H6 Clara stands in the room of the chapter you are on');
    ok(r.roles, tag + 'H7 every room is a button with a name');
    ok(r.out.length === 0 && r.sw <= r.cw, tag + 'H8 nothing runs off the drawing or the screen' + (r.out.length ? ' ' + r.out.join(' | ') : '') + ' (' + r.sw + '/' + r.cw + ')');
    ok(lang === 'ko' ? /26개 챕터 중 1개 완료/.test(r.count) : /1 of 26 chapters done/.test(r.count), tag + 'H9 ' + r.count);
    ok(r.green >= 1 && r.coralFloor, tag + 'H10 chapter 1\'s number green, your floor\'s name coral');
    ok(r.classical && r.fonts.every(Boolean), tag + 'H11 the classical letters are in and loaded (Cinzel, Cormorant Garamond) ' + r.fonts);
    ok(p._errs.length === 0, tag + 'H12 no errors ' + p._errs.join('|').slice(0, 160));
    if (w === 390 && lang === 'en') {
      await p.click('[data-house] [data-chapter="tempo"]'); await p.waitForTimeout(400);
      ok(/drill=tempo/.test(await p.evaluate(() => location.search)), 'H13 tapping a room opens that chapter');
      await p.goto(H.base + '/drills.html'); await p.waitForTimeout(900);
      ok(await p.evaluate(() => document.querySelector('[data-house]').dataset.layout === 'house'), 'H14 back on the map in the same session: the house straight away');
      await p.focus('[data-house] [data-chapter="scales"]'); await p.keyboard.press('Enter'); await p.waitForTimeout(400);
      ok(/drill=scales/.test(await p.evaluate(() => location.search)), 'H15 Enter on a focused room opens it');
      await p.goto(H.base + '/drills.html'); await p.waitForTimeout(800);
      const c = await p.evaluate(() => new Promise(res => {
        sessionStorage.removeItem('pb_house_in_v1');
        const d = document.createElement('div'); d.id = 'cmp'; document.body.appendChild(d); let opened = null;
        ReactDOM.createRoot(d).render(React.createElement(HouseMap, { compact: true, onOpen: id => { opened = id; } }));
        setTimeout(() => { const hall = d.querySelector('[data-house]').dataset.layout, week = !!d.querySelector('[data-testid="map-week"]'); d.querySelector('[data-door]').dispatchEvent(new MouseEvent('click', { bubbles: true }));
          setTimeout(() => { const btns = [...d.querySelectorAll('[data-chapter]')]; const s = d.querySelector('[data-chapter="pulse"]'); s && s.dispatchEvent(new MouseEvent('click', { bubbles: true }));
            res({ hall, week, n: btns.length, order: btns.map(b => b.dataset.chapter).join(',') === pathIds().join(','), opened }); }, 900); }, 400);
      }));
      ok(c.hall === 'hall' && !c.week && c.n === 26 && c.order && c.opened === 'pulse', 'C1 compact (the student page): the hall, the door, 26 rooms that open their chapters, no week board ' + JSON.stringify(c));
    }
    await p.context().close();
  }
  // the door by keyboard, and with reduced motion: no swing, no rise, the house at once
  const k = await H.open({ path: '', w: 390, h: 900, store }); await k.waitForTimeout(900);
  await k.focus('[data-door]'); await k.keyboard.press('Enter'); await k.waitForTimeout(900);
  ok(await k.evaluate(() => document.querySelector('[data-house]').dataset.layout === 'house'), 'K1 Enter on the door opens the house');
  await k.context().close();
  const m = await H.open({ path: '', w: 390, h: 900, store, reducedMotion: 'reduce' }); await m.waitForTimeout(900);
  await m.click('[data-door]'); await m.waitForTimeout(120);
  ok(await m.evaluate(() => { const g = document.querySelector('[data-grow]'); return document.querySelector('[data-house]').dataset.layout === 'house' && getComputedStyle(g).animationName === 'none'; }), 'K2 reduced motion: the house at once, no rising');
  await m.context().close();
  // the Workbook's page to colour in: the wide house, 26 numbered rooms, no buttons on paper
  const b = await H.open({ path: '?book=work&ch=front&lang=en', w: 900, h: 1200 }); await b.waitForTimeout(2600);
  const wb = await b.evaluate(() => { const pg = [...document.querySelectorAll('.bk-page')].find(e => /The Piano Butler’s house/.test(e.querySelector('h1') ? e.querySelector('h1').textContent : '')); if (!pg) return null; const sv = pg.querySelector('svg[viewBox]'); return { vb: sv && sv.getAttribute('viewBox'), btns: pg.querySelectorAll('[role="button"]').length, nums: [...pg.querySelectorAll('svg text')].map(t => t.textContent).filter(x => /^\d+$/.test(x)).length }; });
  ok(wb && /^0 0 720 /.test(wb.vb) && wb.btns === 0 && wb.nums >= 26, 'P1 the Workbook\'s house to colour in: wide, numbered, no buttons ' + JSON.stringify(wb));
  await b.context().close();
  await H.close();
})().catch(e => { console.error('CRASH', e); process.exit(1); });
