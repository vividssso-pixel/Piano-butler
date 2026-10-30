// Build DR: her 31 Oct night asks, and calls 38 and 39. Usage: node dr794.js drills.t794.html
const { start } = require('/home/claude/pbtest/kit/contentharness');
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
(async () => {
  const H = await start(process.argv[2] || 'drills.t794.html'); let bad = 0;
  const say = (ok, ...a) => { if (!ok) bad++; console.log(ok ? 'ok  ' : 'BAD ', ...a); };
  // (1) stacked heads on lines touch: the hollow head is one space tall (ry 4.95 on a 10-unit space)
  const c = await H.open({ path: '?book=lesson&ch=chords', w: 900, h: 1300, dsf: 1 }); await sleep(1500);
  const heads = await c.evaluate(() => [...document.querySelectorAll('.bk-page')[1].querySelectorAll('ellipse[ry]')].map(e => e.getAttribute('ry')).filter(r => +r > 4));
  say(heads.length > 0 && heads.every(r => r === '4.95'), '1 hollow heads one space tall', JSON.stringify([...new Set(heads)]));
  await c.close();
  // (2) the melodic minor is one mountain, (6) the twins strip, (9) the staff under the keyboards
  const s2 = await H.open({ path: '?book=lesson&ch=scales-23', w: 900, h: 1300, dsf: 1 }); await sleep(1800);
  const m = await s2.evaluate(() => ({ hill: document.querySelectorAll('[data-mel-hill]').length, rows: document.querySelectorAll('[data-mel-hill] circle').length, strip: document.querySelectorAll('[data-twin-strip]').length, staff: document.querySelectorAll('[data-scf-staff]').length, melStaff: (document.querySelector('[data-scf-staff="G melodic minor"]') || {}).textContent || '', over: [...document.querySelectorAll('.bk-page')].map(pg => pg.scrollHeight - pg.clientHeight) }));
  say(m.hill >= 1 && m.rows === 15 * m.hill, '2 the mountain: fifteen notes', m.hill, m.rows);
  say(m.strip >= 2 && m.staff >= 5 && /F♯G F E♭/.test(m.melStaff.replace(/\s/g, '').replace('F♯G', 'F♯G ').replace('GF', 'G F ').replace('FE♭', 'F E♭')) || /F♯GFE♭/.test(m.melStaff.replace(/\s/g, '')), '6/9 twin strips and staffs; the mountain comes down F E♭', m.strip, m.staff, JSON.stringify(m.melStaff.replace(/\s/g, '').slice(0, 40)));
  say(m.over.every(x => x <= 2) && !s2._errs.length, '9 the Grade 2 book fits', JSON.stringify(m.over), s2._errs.slice(0, 1));
  await s2.close();
  // (3) triplets count 1 + a
  const r2 = await H.open({ path: '?book=lesson&ch=rhythm-2', w: 900, h: 1300, dsf: 1 }); await sleep(1800);
  const tx = await r2.evaluate(() => document.body.innerText);
  say(/1 \+ a/.test(tx) && !/trip let|trip-let/.test(tx), '3 triplets: 1 + a, no trip-let');
  await r2.close();
  // (4) four-voice stems flush and chords centred, (5) the staircase, (8) 12/8 in Rhythm 3
  const h3 = await H.open({ path: '?book=lesson&ch=harmony-3', w: 900, h: 1300, dsf: 1 }); await sleep(1800);
  const st = await h3.evaluate(() => { const ln = [...document.querySelectorAll('line')].filter(l => l.getAttribute('stroke-width') === '1.6' && Math.abs((+l.getAttribute('y2')) - (+l.getAttribute('y1'))) === 32); const el = ln.map(l => { const x = +l.getAttribute('x1'); const e = [...l.parentElement.querySelectorAll('ellipse')][0]; return e ? Math.abs(x - +e.getAttribute('cx')) : -1; }); return { n: ln.length, d: [...new Set(el.map(x => x.toFixed(1)))], stairs: document.querySelectorAll('[data-h3-stairs] rect').length }; });
  say(st.n > 0 && st.d.length === 1 && st.d[0] === '4.8' && st.stairs === 8, '4/5 stems at 4.8 from the head; eight stairs', JSON.stringify(st));
  await h3.close();
  const r3 = await H.open({ path: '?book=lesson&ch=rhythm-3', w: 900, h: 1300, dsf: 1 }); await sleep(1800);
  say(/12\/8/.test(await r3.evaluate(() => document.body.innerText)) && !r3._errs.length, '8 12/8 in Rhythm, Grade 3');
  await r3.close();
  // (7) a one-check page carries 'Write it here'
  for (const ch of ['melody-3', 'melody-4', 'melody-5']) { const p = await H.open({ path: '?book=lesson&ch=' + ch, w: 900, h: 1300, dsf: 1 }); await sleep(1800);
    const w = await p.evaluate(() => ({ n: document.querySelectorAll('[data-write-here]').length, over: [...document.querySelectorAll('.bk-page')].map(pg => pg.scrollHeight - pg.clientHeight) }));
    say(w.n === 1 && w.over.every(x => x <= 2) && !p._errs.length, '7 ' + ch + ': Write it here', JSON.stringify(w)); await p.close(); }
  // call 38: the Scales map on the Quick line, nine floors, the floors are doors
  for (const lang of ['en', 'ko']) { const p = await H.open({ path: '?teacher=1&view=home', w: 420, h: 1200, dsf: 1, lang }); await sleep(1000);
    await p.locator('[data-quick="scales-map"]').click(); await sleep(900);
    const r = await p.evaluate(() => ({ floors: document.querySelectorAll('[data-smap-floor]').length, chips: document.querySelectorAll('[data-scales-map] .chip').length, ids: [...document.querySelectorAll('[data-scales-map] .chip')].map(e => e.innerText).filter(x => /^[A-G][sb]?(mh?|mel|m)?\d$/.test(x)) }));
    await p.locator('[data-smap-floor="scales-8"] button').first().click(); await sleep(900);
    say(r.floors === 9 && r.chips > 60 && r.ids.length === 0 && /drill=scales-8/.test(await p.evaluate(() => location.search)) && !p._errs.length, lang, 'call 38 the Scales map: nine floors, names not ids, a door', JSON.stringify(r.ids), p._errs.slice(0, 1));
    await p.close(); }
  // call 39: the staff under the Scale finder's rooms' pictures on screen too
  const sc = await H.open({ path: '?drill=scales-3', w: 420, h: 1600, dsf: 1 }); await sleep(1500);
  const n = await sc.locator('section > button').count(); let staffs = 0; for (let k = 0; k < n; k++) { await sc.locator('section > button').nth(k).click(); await sleep(400); staffs += await sc.locator('[data-scf-staff]').count(); }
  say(staffs >= 2 && !sc._errs.length, 'call 39 staffs on screen in Scales, Grade 3', staffs, sc._errs.slice(0, 1));
  await sc.close();
  console.log('bad', bad); await H.close();
})();
