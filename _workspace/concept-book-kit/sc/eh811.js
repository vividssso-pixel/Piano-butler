// Build EH: the Grade 1 Workbooks, fun first. Each changed part is there (and what it replaced is gone), every page of the
// five Workbooks and their Teacher copies fits, and the answers that check themselves are right.
// Usage (from a3): node ../sc/eh811.js drills.t811.html
const { start } = require('/home/claude/pbtest/kit/contentharness');
const B = process.argv[2] || 'drills.t811.html';
let bad = 0; const ok = (c, m, x) => { if (!c) bad++; console.log((c ? 'ok   ' : 'BAD  ') + m, x === undefined ? '' : JSON.stringify(x)); };
const CH = {
  'six-eight': [['Words in twos and threes', 'Counts into notes', 'while you clap every quaver'], ['Listen this week', 'Write your own', 'someone claps']],
  terms: [['The term crossword', 'Build the term', 'One piece, four ways', 'Set a metronome'], ['make your own', 'Your teacher plays a scale', 'My own (11)', 'three ways']],
  intervals: [['The interval word', 'Both ways'], ['Your teacher plays six intervals']],
  chords: [['Major, then minor'], ['Your teacher plays six triads']],
  form: [['A again, written out'], ['make up your own B']],
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
      ok(!/[Yy]our teacher plays|[Aa]sk someone|someone (claps|plays)/.test(r.txt.replace(/Tick when your teacher says yes/g, '')), ch + ': nothing at home needs someone else');
    }
    if (kind === 'work' && ch === 'six-eight') {
      const E = await p.evaluate(() => ({ a: E8_WORDS[34], b: E8_WORDS[68], bank: E8_BANK, code: [...document.querySelectorAll('[data-e8code]')].map(e => e.dataset.e8code), kinds: e8cGroups(E8_CODE[0]).map(g => E8C_NAME[g.join()]), houses: document.querySelectorAll('[data-e8house]').length }));
      ok(E.a.length === 4 && E.b.length === 4 && E.bank.length === 7 && [...E.a.slice(1), ...E.b].sort().join() === E.bank.slice().sort().join(), 'the words: four in each bar, the bank is the other seven', E);
      ok(E.houses === 2, 'two bars to write in');
      ok(E.code.join(' ') === '02 012 02 0' && E.kinds.every(Boolean), 'counts into notes: the circles are the long-short row, every group one of the three kinds', E.kinds);
    }
    if (kind === 'work' && ch === 'terms') {
      const T = await p.evaluate(() => {
        const cells = xwCells(TMX_XW), keys = Object.keys(cells), grid = {}; keys.forEach(k => { grid[k] = cells[k]; });
        const runs = []; const rs = keys.map(k => +k.split(',')[0]), cs = keys.map(k => +k.split(',')[1]), R = Math.max(...rs) + 1, C = Math.max(...cs) + 1;
        for (let r = 0; r < R; r++) { let w = ''; for (let c = 0; c <= C; c++) { const x = grid[r + ',' + c]; if (x) w += x; else { if (w.length > 1) runs.push('A' + w); w = ''; } } }
        for (let c = 0; c < C; c++) { let w = ''; for (let r = 0; r <= R; r++) { const x = grid[r + ',' + c]; if (x) w += x; else { if (w.length > 1) runs.push('D' + w); w = ''; } } }
        const want = TMX_XW.map(([w, , , d]) => d + w).sort();
        const tiles = TMX_TILES.flat().sort().join('|'), parts = TMX_BUILD.map(tmxBuildOf).flatMap(e => [e.a, e.b]).sort().join('|');
        return { clash: keys.some(k => cells[k] === '!'), runs: runs.sort(), want, nums: xwNums(TMX_XW), drawn: +document.querySelector('[data-xw]').dataset.xw, n: keys.length,
          en: TMX_XW.map(([w]) => !!(tmxOf(w) && tmxOf(w).en)), tiles, parts, combos: TMX_BUILD.slice(0, 4).map(w => !!TMX_COMBO.find(x => x.w === w)), means: new Set(TMX_BUILD.map(x => tmxBuildOf(x).en)).size };
      });
      ok(!T.clash && T.runs.join() === T.want.join(), 'the crossword: every run of squares is one of its words, nothing else', T.runs);
      ok(T.drawn === T.n && T.n === TMX_XW_LEN(), 'the crossword: every square drawn', [T.drawn, T.n]);
      ok(Object.values(T.nums).sort().join() === '1,2,3,4,5' && T.en.every(Boolean), 'the crossword: clues 1 to 5, each the room’s own meaning', T.nums);
      ok(T.tiles === T.parts, 'build the term: the tiles are exactly the parts, each once', [T.tiles, T.parts]);
      ok(T.combos.every(Boolean) && T.means === 6, 'build the term: four pairs from the room, six different meanings', T.combos);
    }
    if (kind === 'work' && ch === 'intervals') {
      const I = await p.evaluate(() => ({ word: ivxWordOf(), ns: IVX_WORD.map(x => x[2]).join(' '), clefs: IVX_WORD.map(x => x[1]).join(' ') }));
      ok(I.word === 'CAGE' && I.ns === '6 8 7 6' && I.clefs === 'treble bass treble treble', 'the interval word: a 6th, an octave, a 7th, a 6th spell CAGE', I);
    }
    if (kind === 'work' && ch === 'form') {
      const F = await p.evaluate(() => FMX_TER.slice(0, 4).map(b => b.n.length).join(' '));
      ok(F === '4 3 4 1', 'A again: the four bars of A to copy', F);
    }
    await p.context().close();
  }
  console.log('bad', bad); await H.close(); process.exit(0);
})();
// the crossword's squares: all 44 letters, less one for each of its four crossings (cantabile with maestoso, leggiero and
// espressivo; sostenuto with espressivo)
function TMX_XW_LEN() { return 9 + 9 + 8 + 8 + 10 - 4; }
