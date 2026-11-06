// Phase 444 (from 437, 441): chapter 7 (Tones & Semitones) -- the drill's seven levels, the Workbook's data, the book on screen
const { start } = require('./contentharness');
const ok = (c, m) => { console.log((c ? 'PASS ' : 'FAIL ') + m); if (!c) process.exitCode = 1; };
(async () => {
  const H = await start(process.env.BUILD || 'drills.t444.html');
  const p = await H.open({ path: '?drill=tones', w: 430, h: 900 }); await p.waitForTimeout(1200);
  const r = await p.evaluate(() => {
    const bad = []; const lv = TONES_DRILL.levels;
    lv.forEach((L) => { let prev = null; for (let k = 0; k < 3000; k++) { const q = TONES_DRILL.generate(L, prev); prev = q;
      if (q.choices && (!q.choices.includes(q.answer) || new Set(q.choices).size !== q.choices.length)) bad.push(L.n + ' choices ' + JSON.stringify(q));
      if ((L.kind === 'bname' || L.kind === 'enh') && q.choices.some(c => (c[1] === '#') !== (q.answer[1] === '#'))) bad.push(L.n + ' mixed signs ' + q.choices.join());
      if (L.kind === 'find' && (q.target < 0 || q.target > 23 || Math.abs(q.target - q.a) !== L.size)) bad.push(L.n + ' find ' + JSON.stringify(q));
      if (L.kind === 'staff' && PC_INFO[q.pc].white) bad.push(L.n + ' white ' + JSON.stringify(q));
      if ((L.kind === 'hw' || L.kind === 'wn') && (q.b - q.a === 1) !== (q.answer === 'half')) bad.push(L.n + ' hw ' + JSON.stringify(q));
      if (!TONES_DRILL.check(q, q.kind === 'find' ? q.target : q.kind === 'staff' ? q.pc + 12 : q.answer)) bad.push(L.n + ' check ' + JSON.stringify(q));
    } });
    const W = TN_WB, C = TN_CHK;
    const staffItems = [...W.draw.map(([d, a]) => [d, a]), ...W.read.tre, ...W.read.bas, ...W.colour.map(([, d, a]) => [d, a]), ...C.read.map(([, d, a]) => [d, a])];
    const white = staffItems.filter(([d, a]) => PC_INFO[tnDpc(d, a)].white);
    return { n: lv.length, kinds: lv.map(l => l.kind).join(), bad: bad.slice(0, 5), nbad: bad.length, white, same: W.same.map(([x, y]) => tnSamePc(x, y)) };
  });
  ok(r.n === 7, 'D1 seven levels: ' + r.kinds);
  ok(r.nbad === 0, 'D2 3000 questions a level: answers among the choices, one sign a level, keys on the keyboard, staff signs on black keys ' + JSON.stringify(r.bad));
  ok(r.white.length === 0, 'W1 every staff item in the Workbook lands on a black key ' + JSON.stringify(r.white));
  ok(r.same.filter(Boolean).length >= 3 && r.same.filter(x => !x).length >= 3, 'W2 "same key or not": some yes, some no ' + JSON.stringify(r.same));
  const learn = await p.evaluate(() => ({ steps: document.querySelectorAll('[id^="tones-step-"]').length, tries: document.querySelectorAll('.try-box').length, ttl: (document.querySelector('h2') || {}).textContent }));
  ok(learn.steps === 6 && learn.tries === 5, 'S1 the book on screen: 6 steps, 5 things that move ' + JSON.stringify(learn));
  const sf = async (key, dir) => p.evaluate(async ([key, dir]) => {
    const box = [...document.querySelectorAll('.try-box')].find(b => /Sharp up, flat down/.test(b.textContent));
    box.querySelector('[data-key="' + key + '"]').dispatchEvent(new MouseEvent('click', { bubbles: true }));
    await new Promise(r => setTimeout(r, 80));
    [...box.querySelectorAll('button')].find(b => b.textContent.includes(dir)).click();
    await new Promise(r => setTimeout(r, 120));
    return box.lastElementChild.textContent.trim();
  }, [key, dir]);
  const m1 = await sf(16, 'up'), m2 = await sf(12, 'down'), m3 = await sf(12, 'up'), m4 = await sf(23, 'up'), m5 = await sf(0, 'down');
  ok(/E♯: no attic between E and F.*white key F next door\. The same key! A sharp is not always a black key/.test(m1), 'P1 E sharp lands on the white key F: ' + m1);
  ok(/C♭: no attic between B and C.*white key B next door\. The same key! A flat is not always a black key/.test(m2), 'P2 C flat lands on the white key B: ' + m2);
  ok(/C♯: a half step up from C, into the attic on its right\. The neighbour on the other side calls it D♭/.test(m3), 'P3 C sharp is still the black key, also D flat: ' + m3);
  ok(/Off the end/.test(m4) && /Off the end/.test(m5), 'P4 only the two ends fall off the keyboard');
  ok(!p._errs.length, 'S2 no errors ' + p._errs.join('|'));
  await p.context().close();
  for (const [kind, n] of [['work', 6], ['teacher', 2], ['lesson', 7]]) {
    const b = await H.open({ path: '?book=' + kind + '&ch=tones&lang=en', w: 900, h: 1200 }); await b.waitForTimeout(2500);
    const k = await b.evaluate(() => ({ pages: document.querySelectorAll('.bk-page').length, txt: document.body.innerText }));
    ok(k.pages === n && !b._errs.length, 'B1 ' + kind + ': ' + k.pages + ' pages, no errors');
    if (kind === 'teacher') { const tx = k.txt.replace(/\u00a0-\u2060-/g, ' --'), rest = tx.replace('writing and drilling E♯ = F, B♯ = C, F♭ = E and C♭ = B (in the scales chapters; the book only says once that a sharp or a flat is not always a black key: E♯ is F)', '').replace('Thinking every sharp or flat is a black key (E♯ is the white key F).', '');
      ok(!/E♯|C♭|B♯|F♭/.test(rest) && rest.length < tx.length - 150, 'B2 the Teacher copy names E♯ only in the two notes (left for later, watch), no E♯ C♭ answer'); }
    if (kind === 'lesson') ok(!/black keys get their names/i.test(k.txt) && /not always a black key/.test(k.txt) && /very next key, black or white/.test(k.txt) && /hidden attic/.test(k.txt) && !/ --|-- /.test(k.txt), 'B4 the book never says sharps and flats are the black keys; it says once they are not always');
    if (kind === 'lesson') ok(!/G♯ A♯|D♯ E\./.test(k.txt) && /big house's first and second black keys/.test(k.txt), 'B3 page 3 names no sharps before page 5');
    await b.context().close();
  }
  await H.close();
})();
