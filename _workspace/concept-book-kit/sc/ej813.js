// Build EJ: the Grade 3 Workbooks, fun first. Rhythm, Grade 3's three PLAYs play with words; its pages and Teacher copy fit;
// Rhythm, Grade 2 keeps its own; the words' notes are right.
// Usage (from a3): node ../sc/ej813.js drills.t813.html
const { start } = require('/home/claude/pbtest/kit/contentharness');
const B = process.argv[2] || 'drills.t813.html';
let bad = 0; const ok = (c, m, x) => { if (!c) bad++; console.log((c ? 'ok   ' : 'BAD  ') + m, x === undefined ? '' : JSON.stringify(x)); };
const CH = {
  'rhythm-3': [['Even, then dotted', 'One beat a word, in minims', 'Simple or compound?', 'Say one bar in words'], ['Long and short', 'Beats in a bar', 'How many beats in one bar?', 'Write S or C.']],
  'rhythm-2': [['One beat a word', 'Three for two, two for three'], ['Even, then dotted', 'in minims']],
};
(async () => {
  const H = await start(B);
  for (const [ch, [want, gone]] of Object.entries(CH)) for (const kind of ['work', 'teacher']) {
    const p = await H.open({ path: '?book=' + kind + '&ch=' + ch + '&lang=en', w: 900, h: 1200 }); await p.waitForTimeout(2300);
    const r = await p.evaluate(() => ({ txt: document.body.innerText, over: [...document.querySelectorAll('.bk-page')].map(e => { const b = e.querySelector('.bk-body'); return b ? b.scrollHeight - b.clientHeight : 0; }) }));
    ok(r.over.every(x => x <= 0) && !p._errs.length, ch + ' ' + kind + ': nothing over, no errors', r.over);
    if (kind === 'work') {
      ok(want.every(w => r.txt.includes(w)), ch + ': its parts', want.filter(w => !r.txt.includes(w)));
      ok(gone.every(w => !r.txt.includes(w)), ch + ': not the others', gone.filter(w => r.txt.includes(w)));
    }
    if (kind === 'work' && ch === 'rhythm-3') {
      const W = await p.evaluate(() => ({ dot: r3Ans(R3W_DOT), min: r3Ans(R3W_MIN), sc: R3_SC.map(ts => ts.join('/') + ' ' + r3ScWords(ts).length + (r3Compound(ts) ? 'C' : 'S')), cells: document.querySelectorAll('[data-r3sc]').length, lines: document.querySelectorAll('[data-r2w]').length }));
      ok(W.dot[0] === 'even: two quavers, two quavers, two quavers, a crotchet' && W.dot[1] === 'dotted: a dotted quaver and a semiquaver, a dotted quaver and a semiquaver, a dotted quaver and a semiquaver, a crotchet', 'even, then dotted', W.dot);
      ok(W.min[0] === 'a minim, two crotchets | four quavers, a minim' && W.min[1] === 'two crotchets, four quavers, a minim', 'the minim beat: pie a minim, wa-ter-mel-on four quavers', W.min);
      ok(W.sc.join(' ') === '9/8 3C 6/8 2C 3/8 3S 3/4 3S', 'simple or compound: the words count the beats', W.sc);
      ok(W.cells === 4 && W.lines === 4, 'four bars to say, four word lines', W);
    }
    await p.context().close();
  }
  console.log('bad', bad); await H.close(); process.exit(0);
})();
