// Build EI: the Grade 2 Workbooks, fun first. Each changed part is there (and what it replaced is gone), every page of
// the two Workbooks and their Teacher copies fits, Rhythm, Grade 3 keeps its own pages, and the word lines are right.
// Usage (from a3): node ../sc/ei812.js drills.t812.html
const { start } = require('/home/claude/pbtest/kit/contentharness');
const B = process.argv[2] || 'drills.t812.html';
let bad = 0; const ok = (c, m, x) => { if (!c) bad++; console.log((c ? 'ok   ' : 'BAD  ') + m, x === undefined ? '' : JSON.stringify(x)); };
const CH = {
  'rhythm-2': [['One beat a word', 'Three for two, two for three', 'Switch every beat'], ['Semiquaver sums', 'How many semiquavers?', 'Make up a bar']],
  melody: [['both the other way'], ['a motif of your own', 'my own']],
  'rhythm-3': [['Count the dotted rhythms', 'Count the minim beats', 'Count 3/8 and 9/8'], ['Semiquaver sums', 'Three for two, two for three']],
};
(async () => {
  const H = await start(B);
  for (const [ch, [want, gone]] of Object.entries(CH)) for (const kind of ['work', 'teacher']) {
    const p = await H.open({ path: '?book=' + kind + '&ch=' + ch + '&lang=en', w: 900, h: 1200 }); await p.waitForTimeout(2300);
    const r = await p.evaluate(() => ({ txt: document.body.innerText, over: [...document.querySelectorAll('.bk-page')].map(e => { const b = e.querySelector('.bk-body'); return b ? b.scrollHeight - b.clientHeight : 0; }) }));
    ok(r.over.every(x => x <= 0) && !p._errs.length, ch + ' ' + kind + ': nothing over, no errors', r.over);
    if (kind === 'work') {
      ok(want.every(w => r.txt.includes(w)), ch + ': the new parts (or, for Grade 3, its own)', want.filter(w => !r.txt.includes(w)));
      ok(gone.every(w => !r.txt.includes(w)), ch + ': the old parts gone', gone.filter(w => r.txt.includes(w)));
    }
    if (kind === 'work' && ch === 'rhythm-2') {
      const W = await p.evaluate(() => ({
        semiA: R2.semiA.items.filter(it => ['q', 'p', 's4', 't3'].includes(it[0])).map(it => ({ q: 1, p: 2, s4: 4, t3: 3 })[it[0]]).join(' '),
        line1: R2W_SEMI[0].words.map(r2wSyl).join(' '),
        beats: R2W_SEMI.concat(R2W_TRIP).map(l => l.words.length % l.bar === 0 && l.words.every(w => r2wNote(l.ts, w))),
        trip: R2W_TRIP.map(l => l.words.map(w => r2wNote(l.ts, w)).join(', ')),
        lines: document.querySelectorAll('[data-r2w]').length, cells: document.querySelectorAll('[data-word]').length,
      }));
      ok(W.semiA === W.line1, 'line 3 is the room’s own semiquaver line (pie, wa-ter-mel-on, ap-ple, pie: q s4 p q)', [W.semiA, W.line1]);
      ok(W.beats.every(Boolean) && W.lines === 4 && W.cells === 16, 'four word lines, every bar full, every word a note the room teaches', W);
      ok(W.trip[0] === 'a triplet, two quavers, a triplet, a crotchet' && W.trip[1] === 'a duplet, three quavers, a duplet, a dotted crotchet', 'three for two in 2/4, two for three in 6/8', W.trip);
    }
    await p.context().close();
  }
  console.log('bad', bad); await H.close(); process.exit(0);
})();
