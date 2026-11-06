// Phase 436 (+438: no frames, the dome in your room, no lamps): the five levels and the centred house -- plaques "LEVEL n" / "n층" centred; each room's number and name
// centred over its picture; one name size and one picture height per floor; the hall's words centred; the path's
// order and numbers; "easier after"; the end-of-chapter line; the books count from the path; the small house.
const { start } = require('./contentharness');
const ok = (c, m) => { console.log((c ? 'PASS ' : 'FAIL ') + m); if (!c) process.exitCode = 1; };
const WANT = 'posture-hands,first-steps,pulse,note-names,note-values,staff,whole-staff,time-signatures,reading-steps,dynamics,tones,pitch-range,tempo,rhythm,ledger-lines,scales,piano-story,key-signatures,signs,intervals,chords,composers,melody,form,terms,styles';
(async () => {
  const H = await start(process.env.BUILD);
  const store = { pb_lesson_steps_v1: JSON.stringify({ 'posture-hands': { 0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1 }, 'first-steps': { 0: 1 } }), pb_steps_total_v1: JSON.stringify({ 'posture-hands': 6, 'first-steps': 9 }) };
  for (const [w, lang] of [[390, 'en'], [390, 'ko'], [1024, 'en'], [1440, 'ko'], [320, 'en']]) {
    const p = await H.open({ path: '', w, h: 900, store, lang }); await p.waitForTimeout(900);
    if (await p.$('[data-door]')) { await p.click('[data-door]'); await p.waitForTimeout(1500); }
    const tag = w + 'px ' + lang + ': ';
    const r = await p.evaluate(() => {
      const m = document.querySelector('[data-house]'), sv = m.querySelector('[data-house-view] svg');
      const rooms = [...m.querySelectorAll('[data-chapter]')].map(e => ({ id: e.dataset.chapter, b: e.querySelector('rect').getBoundingClientRect() }));
      const texts = [...sv.querySelectorAll('text')].map(t => ({ t: t.textContent, b: t.getBoundingClientRect(), st: t.getAttribute('style') || '', fs: +t.getAttribute('font-size'), fill: t.getAttribute('fill') }));
      const squares = [...sv.querySelectorAll('rect[width="17"]')].map(r => r.getBoundingClientRect());
      const frames = [...sv.querySelectorAll('g[transform*="scale(0.8)"]')].map(p => { const b = p.getBoundingClientRect(), ty = +(/translate\(\S+ (\S+)\)/.exec(p.getAttribute('transform')) || [0, 0])[1]; return { left: b.left, width: b.width, top: b.top, height: b.height, ty }; });   // Phase 438: the pictures hang without frames; their height on the wall is the group's own y
      const inR = (b, R) => b.left + b.width / 2 > R.left && b.left + b.width / 2 < R.right && b.top + b.height / 2 > R.top && b.top + b.height / 2 < R.bottom;
      const per = rooms.map(R => {
        const sq = squares.find(b => inR(b, R.b)), names = texts.filter(x => /Cormorant/.test(x.st) && inR(x.b, R.b)).sort((a, b) => a.b.top - b.b.top);
        const pic = frames.filter(b => inR(b, R.b) && b.width > 3 && b.width < 60)[0];
        const first = names[0], grpL = sq ? sq.left : NaN, grpR = first ? first.b.right : NaN, cx = R.b.left + R.b.width / 2;
        return { id: R.id, here: m.querySelector('[data-chapter="' + R.id + '"]').dataset.here === '1', off: Math.abs((grpL + grpR) / 2 - cx), off2: names[1] ? Math.abs(names[1].b.left + names[1].b.width / 2 - cx) : 0, inside: names.every(n => n.b.left >= R.b.left && n.b.right <= R.b.right) && sq && sq.left >= R.b.left, fs: first ? first.fs : 0, picTop: pic ? Math.round(pic.ty) : null, rowTop: Math.round(R.b.top) };
      });
      const plaques = texts.filter(x => /Cinzel/.test(x.st) && /^(LEVEL \d|\d층)$/.test(x.t));
      const sb = sv.getBoundingClientRect();
      const hall = texts.filter(x => /^(Your butler|welcomes you\.|버틀러가|맞아 줘요\.)$/.test(x.t));
      return { order: rooms.map(x => x.id).join(','), per, plaques: plaques.map(x => ({ t: x.t, off: Math.abs(x.b.left + x.b.width / 2 - (sb.left + sb.width / 2)), fill: x.fill })),
        hallOff: hall.length === 2 ? Math.abs((hall[0].b.left + hall[0].b.right) / 2 - (hall[1].b.left + hall[1].b.right) / 2) : -1,
        foot: texts.some(x => /floor by floor, any room first|한 층씩, 방은 마음대로/i.test(x.t)),
        dome: (() => { const f = m.querySelector('[data-testid="map-figure"]'), hr = m.querySelector('[data-here="1"] rect'); if (!f || !hr) return false; const a = f.getBoundingClientRect(), b = hr.getBoundingClientRect(); return !!f.querySelector('g[transform*="scale(0.66)"]') && a.left >= b.left && a.right <= b.right && a.top >= b.top && a.bottom <= b.bottom + 1; })(),
        lamps: sv.querySelectorAll('[fill="url(#vmglow)"]').length, frames0: [...sv.querySelectorAll('path')].filter(p => p.getAttribute('stroke-width') === '1.1' && /A4 4/.test(p.getAttribute('d') || '')).length, sw: document.documentElement.scrollWidth, cw: document.documentElement.clientWidth };
    });
    ok(r.order === WANT, tag + 'L1 26 rooms in the levels\' order');
    ok(r.plaques.length === 5 && r.plaques.every(x => x.off < 1.5) && r.plaques.map(x => x.t).join() === (lang === 'ko' ? '5층,4층,3층,2층,1층' : 'LEVEL 5,LEVEL 4,LEVEL 3,LEVEL 2,LEVEL 1'), tag + 'L2 five plaques, centred: ' + r.plaques.map(x => x.t + '@' + x.off.toFixed(1)).join(' '));
    ok(r.plaques.find(x => /1/.test(x.t)).fill === '#e4572e', tag + 'L3 your floor\'s plaque is coral');
    const bad = r.per.filter(x => !(x.off < 2 && x.off2 < 2 && x.inside));
    ok(!bad.length, tag + 'C1 every room\'s number and name centred, inside the room ' + JSON.stringify(bad.slice(0, 3)));
    const rows = {}; r.per.filter(x => !x.here).forEach(x => { (rows[x.rowTop] = rows[x.rowTop] || []).push(x); });   // your room has the dome
    const uneven = Object.values(rows).filter(rw => new Set(rw.map(x => x.picTop)).size > 1 || new Set(rw.map(x => x.fs)).size > 1);
    ok(!uneven.length, tag + 'C2 one name size and one picture height in each row ' + JSON.stringify(uneven.map(rw => rw.map(x => x.id + ':' + x.fs + '/' + x.picTop)).slice(0, 2)));
    ok(r.hallOff < 2, tag + 'C3 the hall\'s two lines centred on each other (' + r.hallOff.toFixed(1) + ')');
    ok(r.foot, tag + 'C4 the footer: floor by floor, any room first');
    ok(r.dome, tag + 'G1 your room: its picture under the glass dome, inside the room (no Clara)');
    ok(r.lamps === 0, tag + 'G2 no lamps, no glow (' + r.lamps + ')');
    ok(r.sw <= r.cw, tag + 'C5 no sideways scroll');
    await p.context().close();
  }
  // the path's numbers and the end-of-chapter line
  const q = await H.open({ path: '', w: 900, h: 900, store, lang: 'en' }); await q.waitForTimeout(800);
  const nums = await q.evaluate(() => ({ nn: bkChapterNo('note-names'), st: bkChapterNo('staff'), ws: bkChapterNo('whole-staff'), ll: bkChapterNo('ledger-lines'), tn: bkChapterNo('tones'), n: pathIds().length, lv: PATH_STAGES.length }));
  ok(nums.nn === 4 && nums.st === 6 && nums.ws === 7 && nums.ll === 15 && nums.tn === 11 && nums.n === 26 && nums.lv === 5, 'N1 the numbers: ' + JSON.stringify(nums));
  await q.context().close();
  for (const [id, want, lang] of [['staff', /That was the last room on Level 1\. Next floor: Level 2\./, 'en'], ['pulse', /Level 1 of 5/, 'en'], ['staff', /1층의 마지막 방이에요\. 다음 층: 2층\./, 'ko'], ['tones', /5층 중 2층/, 'ko']]) {
    const c = await H.open({ path: '?drill=' + id, w: 900, h: 900, store, lang }); await c.waitForTimeout(900);
    const txt = await c.evaluate(() => document.body.innerText);
    ok(want.test(txt), 'E1 ' + id + ' ' + lang + ': ' + want);
    await c.context().close();
  }
  // easier after: a student sees it while the rooms before are unfinished; a teacher sees "builds on"
  const stu = await H.open({ path: '?drill=reading-steps&lock=0&student=1', w: 900, h: 900, store, lang: 'en' }); await stu.waitForTimeout(900);
  const a1 = await stu.evaluate(() => { const e = document.querySelector('[data-testid="after-note"]'); return e ? e.textContent : null; });
  console.log('   after-note (default view): ' + a1);
  ok(a1 && /6 · Reading the Staff/.test(a1) && /8 · Time Signatures/.test(a1), 'A1 reading-steps: easier after 6 and 8 -- ' + a1);
  await stu.context().close();
  const done = { pb_lesson_steps_v1: JSON.stringify({ staff: { 0: 1, 1: 1 }, 'time-signatures': { 0: 1, 1: 1 } }), pb_steps_total_v1: JSON.stringify({ staff: 2, 'time-signatures': 2 }) };
  const s2 = await H.open({ path: '?drill=reading-steps', w: 900, h: 900, store: done, lang: 'en' }); await s2.waitForTimeout(900);
  const a2 = await s2.evaluate(() => ({ note: (document.querySelector('[data-testid="after-note"]') || {}).textContent || null, teacher: UI_TEACHER }));
  ok(a2.teacher ? /Builds on/.test(a2.note) : a2.note === null, 'A2 both rooms done: ' + JSON.stringify(a2));
  await s2.context().close();
  const s3 = await H.open({ path: '?drill=posture-hands', w: 900, h: 900, store, lang: 'en' }); await s3.waitForTimeout(900);
  ok(await s3.evaluate(() => !document.querySelector('[data-testid="after-note"]')), 'A3 the first room has no line');
  await s3.context().close();
  // the books count from the path
  const bk = await H.open({ path: '?book=lesson&ch=staff&lang=en', w: 900, h: 1200 }); await bk.waitForTimeout(2500);
  const bt = await bk.evaluate(() => document.body.innerText);
  ok(/Chapter 7 · The Whole Staff/.test(bt) && /same skip as in Chapter 4/.test(bt) && /CHAPTER 6/.test(bt), 'B1 Reading the Staff: CHAPTER 6, "Next: Chapter 7", "the skip in Chapter 4"');
  await bk.context().close();
  const fr = await H.open({ path: '?book=work&ch=front&lang=en', w: 900, h: 1200 }); await fr.waitForTimeout(2500);
  const mini = await fr.evaluate(() => { const h = document.querySelector('[data-bk-house]'); if (!h) return null; const tx = [...h.querySelectorAll('text')].map(t => t.textContent); return { lv: tx.filter(x => /^LEVEL \d$/.test(x)).length, stage: tx.some(x => /GETTING STARTED|READING NOTES/.test(x)) }; });
  ok(mini && mini.lv === 5 && !mini.stage, 'B2 the small house: five LEVEL rows ' + JSON.stringify(mini));
  ok(/numbered 1 to 26/.test(await fr.evaluate(() => document.body.innerText)), 'B5 the Workbook\'s house page: numbered 1 to 26');
  await fr.context().close();
  const bk2 = await H.open({ path: '?book=lesson&ch=whole-staff&lang=ko', w: 900, h: 1200 }); await bk2.waitForTimeout(2500);
  const bt2 = await bk2.evaluate(() => document.body.innerText);
  ok(/6챕터에서는 클라라/.test(bt2) || /In Chapter 6 you read/.test(bt2), 'B3 The Whole Staff points back to chapter 6');
  await bk2.context().close();
  const lb = await H.open({ path: '?book=lesson&ch=ledger-lines&lang=en', w: 900, h: 1200 }); await lb.waitForTimeout(2500);
  const lt = await lb.evaluate(() => document.body.innerText);
  ok(/CHAPTER 15/.test(lt) && /like in Chapter 7/.test(lt) && /is Chapter 7's G/.test(lt), 'B4 Ledger Lines is chapter 15 and points back to chapter 7');
  await lb.context().close();
  await H.close();
})();
