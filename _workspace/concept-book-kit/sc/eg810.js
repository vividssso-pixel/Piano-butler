// Build EG: the Prelim Workbooks, fun first. Each changed part is there (and what it replaced is gone), every page of the
// three Workbooks and their Teacher copies fits, and the answers that check themselves are right.
// Usage (from a3): node ../sc/eg810.js drills.t810.html
const { start } = require('/home/claude/pbtest/kit/contentharness');
const B = process.argv[2] || 'drills.t810.html';
let bad = 0; const ok = (c, m, x) => { if (!c) bad++; console.log((c ? 'ok   ' : 'BAD  ') + m, x === undefined ? '' : JSON.stringify(x)); };
const CH = {
  'ledger-lines': [['The ladder race'], ['How many ladders?']],
  'scale-play': [['The four-bar scale'], ['Beat puzzle', '15 seconds']],
  'minor-scales': [['Same keys, a new home', 'The step trail', 'The same tune, darker', 'Code breaker'], ['Key signature twins', 'The secret code', 'Listen this week', 'Ask someone']],
};
(async () => {
  const H = await start(B);
  for (const [ch, [want, gone]] of Object.entries(CH)) for (const kind of ['work', 'teacher']) {
    const p = await H.open({ path: '?book=' + kind + '&ch=' + ch + '&lang=en', w: 900, h: 1200 }); await p.waitForTimeout(2300);
    const r = await p.evaluate(() => ({ txt: document.body.innerText, over: [...document.querySelectorAll('.bk-page')].map(e => { const b = e.querySelector('.bk-body'); return b ? b.scrollHeight - b.clientHeight : 0; }) }));
    ok(r.over.every(x => x <= 0) && !p._errs.length, ch + ' ' + kind + ': nothing over, no errors', r.over);
    if (kind === 'work') {
      ok(want.every(w => r.txt.includes(w)), ch + ': the new parts', want.filter(w => !r.txt.includes(w)));
      ok(gone.every(w => !r.txt.includes(w)), ch + ': the old parts gone', gone.filter(w => r.txt.includes(w)));
    }
    if (kind === 'work' && ch === 'ledger-lines') {
      const R = await p.evaluate(() => ({ n: LL_RACE.map(([c, d]) => llRungCount(c, d)), path: llRacePath(), end: llRaceRun(0).end, off: LL_RACE.map((_, i) => i).filter(i => !llRacePath().includes(i)).map(i => { const r = llRaceRun(i); return { i, hit: r.path.some(s => llRacePath().includes(s)), end: r.end }; }), sq: document.querySelectorAll('[data-race]').length }));
      ok(R.end === 13 && R.path.join(' ') === '0 2 5 6 8 11', 'the race: right counts land exactly on the flag (squares 1 3 6 7 9 12, then 14)', R.path);
      ok(R.n.every(x => x >= 1 && x <= 3), 'every race note needs 1 to 3 ladders', R.n);
      ok(R.off.every(o => !o.hit && o.end > 13), 'from every square off the path the counts run past the flag', R.off.filter(o => o.hit || o.end <= 13));
      ok(R.sq === 14, '14 squares on the page', R.sq);
    }
    if (kind === 'work' && ch === 'scale-play') {
      const F = await p.evaluate(() => ['C', 'G'].map(k => spFourBar(k).join(' ')));
      ok(F[0] === 'C D E F G A B C B A G F E D C –' && F[1] === 'G A B C D E F♯ G F♯ E D C B A G –', 'the four-bar scale: 15 notes and the hold fill 16 beats', F);
    }
    if (kind === 'work' && ch === 'minor-scales') {
      const M = await p.evaluate(() => ({
        trail: msTrailMoves().join(' '), keys: msTrailKeys().join(' '), name: SP_SC[MS_TRAIL.nm].nm.slice(1).join(' '), har: msNames('E', 'harmonic').join(' '),
        twins: MS_TWINS.map(([M, m, hM, hm]) => SP_SC[M].nm.slice().sort().join() === SP_SC[m].nm.slice().sort().join() && ((hM - hm + 12) % 12) === 3 && SP_SC[M].nm[5] === SP_SC[m].nm[0]),
        tunes: MS_TUNES.map(([si, M, m]) => msTuneLetters(M, MT_SONGS[si][2]).join('') + '>' + msTuneLetters(m, MT_SONGS[si][2]).join('')),
      }));
      ok(M.trail === '2 1 2 2 1 3 1' && M.keys === '6 7 9 11 12 15 16', 'the step trail: T S T T S T½ S from E, the seventh on the E above', M);
      ok(M.har === 'E F♯ G A B C D♯ E' && M.name === 'F♯ G A B C D♯', 'the trail walks E harmonic minor as the room spells it', [M.har, M.name]);
      ok(M.twins.every(Boolean), 'each twin: the same keys, three half steps down, the major\'s 6th', M.twins);
      ok(M.tunes.join(' ') === 'EDCEDC>CBACBA EDCDEEE>CBABCCC BAGABBB>GF♯EF♯GGG AGFAGF>FEDFED', 'the tunes in major and in the minor twin', M.tunes);
    }
    await p.context().close();
  }
  console.log('bad', bad); await H.close(); process.exit(0);
})();
