// Build EF: the Beginner Workbooks, fun first. Each changed part is there (and what it replaced is gone), every page of
// the six Workbooks and their Teacher copies fits, and the answers that check themselves are right.
// Usage (from a3): node ../sc/ef809.js drills.t809.html
const { start } = require('/home/claude/pbtest/kit/contentharness');
const B = process.argv[2] || 'drills.t809.html';
let bad = 0; const ok = (c, m, x) => { if (!c) bad++; console.log((c ? 'ok   ' : 'BAD  ') + m, x === undefined ? '' : JSON.stringify(x)); };
const CH = {
  'note-values': [['The hidden note'], []],
  'hand-positions': [['The finger code', 'The same tune, higher', 'Fill in the mirror', 'The letter ladder', 'The bridge'], ['Make your own echo', 'Write your own tune', 'Draw the mirror']],
  dynamics: [['The voice ladder'], ['Number them, then the louder one']],
  'reading-steps': [['The secret word'], ['Draw it, then play it']],
  'time-signatures': [['Spot the wrong bar'], ['More time signatures']],
  tones: [['The step trail'], ['Half or whole?']],
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
      if (ch === 'note-values') ok(r.txt.split('Draw the sound lines').length - 1 === 2, 'note-values: "Draw the sound lines" twice now (pages 2 and 3), not three times', r.txt.split('Draw the sound lines').length - 1);
    }
    if (kind === 'work' && ch === 'note-values') {
      const k = await p.evaluate(() => [...document.querySelectorAll('[data-nv-hidden] g')].map(g => g.dataset.k));
      const shape = await p.evaluate(() => NV_HIDE.join(''));
      ok(k.length === shape.length && k.every((x, i) => (x === 'hd') === (shape[i] === 'X')), 'the hidden note: the 3-beat notes are exactly the picture', k.filter(x => x === 'hd').length);
    }
    if (kind === 'work' && ch === 'hand-positions') ok(await p.evaluate(() => HP_CODE.map(([h, pos, fs]) => fs.map(f => hpLetter(pos, h, f)).join('')).join(' ')) === 'EGG BAG FED DAD', 'the finger code spells EGG BAG FED DAD');
    if (kind === 'work' && ch === 'reading-steps') ok(await p.evaluate(() => SSK_WORDS.map(([d, mv]) => { const ds = [d]; mv.forEach(m => ds.push(ds[ds.length - 1] + m)); return ds.map(dName).join(''); }).join(' ')) === 'EGG FED', 'the secret words are EGG and FED');
    if (kind === 'work' && ch === 'time-signatures') ok(await p.evaluate(() => TS_WRONG.every(r => r.bars.every((b, i) => b.reduce((a, k) => a + NV_ROOM[k].b, 0) === r.top + (i + 1 === r.wrong ? 1 : 0)))), 'one bar a beat too long in each tune, every other bar full');
    if (kind === 'work' && ch === 'tones') ok(await p.evaluate(() => tnTrailKeys().join(' ')) === 'w1 b1 w3 w4 b4 b5 w5', 'the trail: D E♭ F G A♭ B♭ A');
    await p.context().close();
  }
  console.log('bad', bad); await H.close(); process.exit(0);
})();
