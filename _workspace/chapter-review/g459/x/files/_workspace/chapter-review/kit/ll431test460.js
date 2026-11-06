// Phase 431: the lid cross shows, Clara's C from both lands on the opener, question numbers in the answer boxes
// (not over the notes, no 'e.g.'), and the fold on the Five Cs page (book and screen).
const { start } = require('./contentharness');
let pass = 0, fail = 0; const ok = (c, m) => { if (c) { pass++; console.log('PASS ' + m); } else { fail++; console.log('FAIL ' + m); } };
(async () => {
  const H = await start(process.env.BUILD || 'drills.t431.html');
  for (const lang of ['en', 'ko']) {
    const p = await H.open({ path: '?book=lesson&ch=ledger-lines&lang=' + lang, w: 1100, h: 1400 });
    const r = await p.evaluate(() => { const pg = [...document.querySelectorAll('.bk-page')];
      const p2 = pg[1], marks = [...p2.querySelectorAll('svg text')].filter(t => /[✓✗]/.test(t.textContent));
      const inside = marks.map(t => (+t.getAttribute('y')) - (+t.closest('svg').getAttribute('viewBox').split(' ')[1]));   // the mark's room above it, in each picture
      const op = pg[0].querySelector('svg[role=img]'); const p6 = pg[5];
      return { marks: marks.length, inside, opener: op.getAttribute('aria-label'), opC: [...op.querySelectorAll('ellipse')].length,
        fold: [...p6.querySelectorAll('line')].some(l => l.getAttribute('stroke-dasharray') === '6 5'), p6t: p6.innerText, p6svg: [...p6.querySelectorAll('svg text')].map(t => t.textContent).join('|') }; });
    ok(r.marks === 4 && r.inside.every(v => Math.abs(v - r.inside[0]) < 0.01) && r.inside[0] >= 11, 'B1 ' + lang + ' the lid picture\'s cross has as much room as the other three ' + JSON.stringify(r.inside));
    ok(/again over the bass staff|낮은음자리표 오선 위, 두 번/.test(r.opener), 'B2 ' + lang + ' the opener shows Clara\'s C from both lands');
    ok(r.fold && /fold here|여기서 접어요/.test(r.p6svg), 'B3 ' + lang + ' Five Cs is folded at Clara\'s ladder');
    ok(lang === 'en' ? /high C on low C/.test(r.p6t) && /Fold partners/.test(r.p6t) : /높은 도는 낮은 도/.test(r.p6t) && /접기 짝/.test(r.p6t), 'B4 ' + lang + ' the words: high C meets low C, fold partners at the piano');
    ok(['High C', 'Low C', 'Treble C', 'Bass C'].every(w => lang === 'ko' || r.p6svg.includes(w)), 'B5 ' + lang + ' the five Cs are named in the picture');
    await p.context().close();
  }
  for (const ch of ['staff', 'whole-staff', 'ledger-lines']) {
    const p = await H.open({ path: '?book=work&ch=' + ch + '&lang=en', w: 1100, h: 1400 });
    const r = await p.evaluate(() => { const nums = [...document.querySelectorAll('.bk-page span')].filter(s => /^\d+$/.test(s.textContent.trim()) && s.style.fontStyle === 'italic' && s.style.position === 'absolute');
      const inBox = nums.map(n => { const box = n.parentElement, b = box.getBoundingClientRect(), q = n.getBoundingClientRect(); return box.style.border ? q.left >= b.left && q.right <= b.right && q.top >= b.top && q.bottom <= b.bottom : true; });
      const eg = [...document.querySelectorAll('.bk-page span')].filter(s => s.textContent.trim() === 'e.g.').length;
      return { n: nums.length, inBox: inBox.filter(Boolean).length, eg }; });
    ok(r.n > 0 && r.inBox === r.n, 'W1 ' + ch + ' every question number sits inside its answer box (' + r.inBox + '/' + r.n + ')');
    ok(r.eg === 0, 'W2 ' + ch + ' no e.g. over the example (' + r.eg + ')');
    await p.context().close();
  }
  for (const lang of ['en', 'ko']) {
    const p = await H.open({ path: '?drill=ledger-lines', w: 390, h: 1200, lang, reducedMotion: 'reduce' });
    await p.waitForTimeout(1500);
    const btn = await p.$('button:has-text("' + (lang === 'en' ? 'Fold it' : '접기') + '")'); ok(!!btn, 'A1 ' + lang + ' the fold is on screen');
    if (btn) { await btn.click(); await p.waitForTimeout(500); }
    const txt = await p.evaluate(() => document.body.innerText);
    ok(lang === 'en' ? /High C ↔ low C/.test(txt) : /높은 도 ↔ 낮은 도/.test(txt), 'A2 ' + lang + ' folded: high C meets low C');
    ok(lang === 'en' ? /middle C/.test(txt) && !/Clara's C/.test(txt) : /가운데 도/.test(txt), 'A3 ' + lang + ' the fold says middle C (Phase 449: no more Clara\'s C)');
    ok(!p._errs.length, 'A4 ' + lang + ' no errors ' + p._errs.slice(0, 1));
    if (lang === 'en') { const f = await p.$('.try-box:has(button:has-text("Fold"))'); if (f) await f.screenshot({ path: '/tmp/fold431.png' }); }
    await p.context().close();
  }
  console.log(pass + ' passed, ' + fail + ' failed'); await H.close(); process.exit(fail ? 1 : 0);
})();
