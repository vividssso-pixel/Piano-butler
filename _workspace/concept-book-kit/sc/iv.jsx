// ─── Intervals, built in the Keys and staff style (her call 2026-10-23: "finish Intervals first, then Chords").
// Four groups: the number (count the letters), major / minor / perfect (count the half steps), hearing, and turning it over.
// Every lesson: the whole picture, one at a time, her turn. Keyboard first; the staff on request (and its own lesson).
// Teaching order (Sohyun, Phase 105): number first (the lower note is 1), then quality (count the half steps).
const ivqOrdEn = (n) => n === 1 ? 'unison' : n === 8 ? 'octave' : n + (n === 2 ? 'nd' : n === 3 ? 'rd' : 'th');
const ivqA = (n) => [n === 8 ? 'an octave' : n === 1 ? 'a unison' : 'a ' + ivqOrdEn(n), n === 8 ? '옥타브' : n + '도'];
const IVQ_QW = { P: ['perfect', '완전'], M: ['major', '장'], m: ['minor', '단'], A: ['augmented', '증'], d: ['diminished', '감'] };
const ivqNm = (q, n) => n === 8 && q === 'P' ? ['octave', '옥타브'] : [IVQ_QW[q][0] + ' ' + ivqOrdEn(n), IVQ_QW[q][1] + n + '도'];
const ivqAn = (q, n) => { const w = ivqNm(q, n); return [(/^[aeiou]/.test(w[0]) ? 'an ' : 'a ') + w[0], w[1]]; };
const IVQ_SCALE = [0, 2, 4, 5, 7, 9, 11, 12];   // a major scale, in half steps from the key note
const ivqWhite = (k) => [0, 2, 4, 5, 7, 9, 11].includes(((k % 12) + 12) % 12);
const ivqL = (k) => KQ_L[((k % 12) + 12) % 12] || '';
const ivqWhitesUp = (lo, n) => { const a = []; for (let k = lo; a.length < n; k++) if (ivqWhite(k)) a.push(k); return a; };   // n white keys from lo up (lo first)
const ivqWhitesDown = (hi, n) => { const a = []; for (let k = hi; a.length < n; k--) if (ivqWhite(k)) a.push(k); return a; };
const ivqCountW = (a, b) => { let c = 0; for (let k = Math.min(a, b); k <= Math.max(a, b); k++) if (ivqWhite(k)) c++; return c; };
const ivqPlay = (a, b, mode = 'mel') => {   // keys (C4 = 0): one after the other, together, or both
  if (mode !== 'harm') { playKey(a, 0.7); setTimeout(() => playKey(b, 0.7), 650); }
  if (mode !== 'mel') setTimeout(() => { playKey(a, 1.1); playKey(b, 1.1); }, mode === 'both' ? 1500 : 0);
};
const ivqCap = (txt, col = KQ.NV, big) => <div style={{ textAlign: 'center', fontSize: big ? 20 : 15, fontWeight: 900, color: col, margin: '6px 0 2px', textWrap: 'balance', wordBreak: 'keep-all' }}>{txt}</div>;
const ivqPlayBtn = (label, fn) => <button className="ghost-btn" style={{ ...scS.back, minWidth: 0, fontSize: 14, padding: '0 14px' }} onClick={fn}>{label}</button>;
// a keyboard object for kqKb (letters on the white keys, words or numbers above the keys, hop arrows)
const ivqKb = (o) => ({ oct: o.oct || 2, ks: o.ks || [0, 12], base: 0, plain: !!o.plain, marks: o.marks || {}, names: o.names || {}, ncol: o.ncol || {}, arcs: o.arcs || [], nonce: o.nonce || 0 });
const ivqKbEl = (o) => kqKb(ivqKb(o), (k) => playKey(k, 0.6));
// count the letters: the white keys from lo, numbered 1, 2, 3 ... (down from hi when down), the ends coral
const ivqLetters = (a, b, upto = 99, extra = {}) => {
  const down = b < a, n = ivqCountW(a, b), ks = down ? ivqWhitesDown(a, n) : ivqWhitesUp(a, n), m = {}, names = {}, ncol = {};
  ks.forEach((k, i) => { if (i >= upto) return; m[k] = i === 0 || i === n - 1 ? 'pick' : 'pass'; names[k] = String(i + 1); ncol[k] = i === 0 || i === n - 1 ? KQ.COD : KQ.NV; });
  if (upto < n) m[ks[n - 1]] = m[ks[n - 1]] || 'pass';
  return ivqKb({ ...extra, marks: { ...m, ...(extra.marks || {}) }, names: { ...names, ...(extra.names || {}) }, ncol: { ...ncol, ...(extra.ncol || {}) } });
};
// count the half steps: one arrow per hop, the hop's number on the key it lands on
const ivqHops = (a, b, upto = 99, extra = {}) => {
  const dir = b >= a ? 1 : -1, n = Math.abs(b - a), u = Math.min(upto, n), m = { [a]: 'pick' }, names = {}, ncol = {}, arcs = [];
  for (let i = 1; i <= u; i++) { const k = a + dir * i; arcs.push([k - dir, k, i === u && upto < 99, KQ.CO]); names[k] = String(i); ncol[k] = i === n ? KQ.COD : KQ.NV; m[k] = i === n ? 'pick' : 'pass'; }
  if (u < n) m[b] = 'pass';
  return ivqKb({ ...extra, marks: { ...m, ...(extra.marks || {}) }, names: { ...names, ...(extra.names || {}) }, ncol: { ...ncol, ...(extra.ncol || {}) }, arcs, nonce: u });
};
// a treble staff: two notes side by side (melodic) or one above the other (harmonic); a note is { d, acc } (middle C: d = 28)
function IvqStaff({ a, b, harm, colors = [], labels, width = 200, ladder }) {
  const c = CLEFS.treble, one = !b, notes = one ? [a] : [a, b]; if (one) b = a;
  const ys = [dY(c.high) - 18, dY(c.low) + 16, ...clefInkYs('treble', dY, 'treble')];
  notes.forEach(n => ys.push(dY(n.d) - 16, dY(n.d) + 12));
  const y0 = Math.min(...ys), y1 = Math.max(...ys) + (labels ? 20 : 0);
  const near = Math.abs(a.d - b.d) === 1, xOf = (i) => one ? width * 0.6 : harm ? width * 0.6 + (near && notes[i].d === Math.max(a.d, b.d) ? 13 : 0) : width * (i === 0 ? 0.45 : 0.78);
  const lo = a.d <= b.d ? 0 : 1;
  return <svg viewBox={`0 ${y0} ${width} ${y1 - y0}`} style={{ width: '100%', maxWidth: width * 1.6, display: 'block', margin: '0 auto' }}>
    {c.lines.map(l => <line key={l} x1="4" x2={width - 4} y1={dY(l)} y2={dY(l)} stroke={KQ.NV} strokeOpacity="0.55" strokeWidth="1.2"/>)}
    <ClefGlyph clef="treble" st="treble" yOf={(d) => dY(d)} ink={KQ.NV}/>
    {ladder && !one && Array.from({ length: Math.abs(b.d - a.d) + 1 }, (_, k) => { const from = Math.min(a.d, b.d), cnt = Math.abs(b.d - a.d), x1 = harm ? width * 0.3 : xOf(lo) + 14, x2 = harm ? width * 0.6 - 20 : xOf(1 - lo) - 14, x = cnt ? x1 + (k / cnt) * (x2 - x1) : x1;
      return <text key={'l' + k + ':' + ladder} x={x} y={dY(from + k) + 4} textAnchor="middle" fontSize="10" fontWeight="900" fill="#c8361b" style={{ animation: 'fadeUp 0.25s both', animationDelay: (k * 0.14) + 's' }}>{k + 1}</text>; })}
    {notes.map((nt, i) => { const x = xOf(i), y = dY(nt.d), col = colors[i] || KQ.NV, accX = harm && i === 1 - lo && (a.acc || 0) && (b.acc || 0) ? x - 30 : x - 17;
      return <g key={i + ':' + nt.d + ':' + (nt.acc || 0)}>
        {ledgersFor(nt.d, c.low, c.high).map(p => <line key={p} x1={x - 12} x2={x + 12} y1={dY(p)} y2={dY(p)} stroke={KQ.NV} strokeWidth="1.4"/>)}
        {nt.acc > 0 && <SharpShape x={accX} y={y} color={col}/>}
        {nt.acc < 0 && <FlatShape x={accX + 1} y={y} color={col}/>}
        <ellipse cx={x} cy={y} rx="7" ry="5" transform={`rotate(-20 ${x} ${y})`} fill={col}/>
        {labels && labels[i] && !harm && <text x={x} y={y1 - 5} textAnchor="middle" fontSize="11" fontWeight="800" fill={col}>{labels[i]}</text>}
      </g>; })}
    {labels && harm && <text x={width * 0.6} y={y1 - 5} textAnchor="middle" fontSize="11" fontWeight="800" fill={KQ.NV}>{labels.filter(Boolean).join(' + ')}</text>}
  </svg>;
}
const ivqStaffEl = (a, b, o = {}) => <div style={{ maxWidth: 360, margin: '0 auto' }}><IvqStaff a={a} b={b} {...o}/></div>;
// d (staff) to key (C4 = 0) and back
const ivqKeyOf = (n) => dMidiKey(n.d) + (n.acc || 0);
const IVQ_DW = { 0: 28, 2: 29, 4: 30, 5: 31, 7: 32, 9: 33, 11: 34 };
const ivqDOf = (k) => IVQ_DW[((k % 12) + 12) % 12] + 7 * Math.floor(k / 12);   // a white key's d
const ivqNum = (o) => kqT(o);
const ivqNumOpts = (from = 2) => [2, 3, 4, 5, 6, 7, 8].filter(x => x >= from).map(x => ({ id: String(x), label: () => kqT(ivqA(x)).replace(/^an? /, '') }));
const IVQ_SPEC = {};

// ══ 1. The number ══
// ── lesson 1: count the letters
IVQ_SPEC['iv-count'] = {
  title: ['Count the letters', '글자를 세어요'], allLine: ['An interval is the distance between two notes. Its number counts the letters from the lower note up to the higher one, both notes included. Tap a white key to count from C.', '음정은 두 음 사이의 거리예요. 음정의 숫자는 아래 음부터 위 음까지, 두 음을 모두 넣어서 글자를 세어요. 흰건반을 눌러 C부터 세어 보세요.'],
  fig: (c) => { const hi = typeof c.last === 'number' && ivqWhite(c.last) && c.last > 0 && c.last <= 12 ? c.last : 7, n = ivqCountW(0, hi);
    return { kb: ivqLetters(0, hi, typeof c.last === 'number' ? 99 : c.tk + 1, { ks: [0, 12] }), below: c.tk + 1 >= n || typeof c.last === 'number' ? ivqCap(kqT(['C to ' + ivqL(hi) + ': ' + ivqA(n)[0], 'C에서 ' + ivqL(hi) + '까지: ' + ivqA(n)[1]]), KQ.COD, true) : ivqCap(' '),
      staffAlt: ivqStaffEl({ d: 28 }, { d: 28 + n - 1 }, { ladder: hi, colors: [KQ.COD, KQ.COD] }) }; },
  steps: [
    { title: ['The lower note is 1', '아래 음이 1'], line: ['Start counting on the lower note itself. Here C is 1.', '아래 음 자기 자신부터 세기 시작해요. 여기서는 C가 1이에요.'], fig: () => ({ kb: ivqLetters(0, 4, 1, { ks: [0, 12] }) }) },
    { title: ['Count up to the higher note', '위 음까지 세어요'], line: ['C D E: three letters, so C to E is a 3rd.', 'C D E, 글자 세 개라서 C에서 E까지는 3도예요.'], fig: (c) => ({ kb: ivqLetters(0, 4, c.tk + 1, { ks: [0, 12] }), below: c.tk >= 2 ? ivqCap(kqT(['C to E: a 3rd', 'C에서 E까지: 3도']), KQ.COD, true) : ivqCap(' '),
      staffAlt: ivqStaffEl({ d: 28 }, { d: 30 }, { ladder: 1, colors: [KQ.COD, KQ.COD] }) }) },
    { title: ['2nd to octave', '2도부터 옥타브까지'], line: ['Count on and the numbers grow: 2nd, 3rd, 4th, 5th, 6th, 7th. Eight letters, from C up to the next C, make an octave.', '계속 세면 숫자가 커져요. 2도, 3도, 4도, 5도, 6도, 7도. C에서 다음 C까지 글자 여덟 개가 옥타브예요.'],
      fig: (c) => { const n = 2 + Math.min(Math.floor(c.tk / 2), 6), hi = ivqWhitesUp(0, n)[n - 1]; return { kb: ivqLetters(0, hi, 99, { ks: [0, 12] }), below: ivqCap(kqT(['C to ' + ivqL(hi) + ': ' + ivqA(n)[0], 'C에서 ' + ivqL(hi) + '까지: ' + ivqA(n)[1]]), KQ.COD, true) }; } },
    { title: ['Counting down', '아래로 세기'], line: ['Going down works the same: the higher note is 1, then count down the letters. G down to D: G F E D, a 4th.', '내려갈 때도 똑같아요. 위 음이 1이고, 글자를 거꾸로 세어요. G에서 D까지 G F E D, 4도예요.'], fig: (c) => ({ kb: ivqLetters(7, 2, c.tk + 1, { ks: [0, 12] }), below: c.tk >= 3 ? ivqCap(kqT(['G down to D: a 4th', 'G에서 D까지: 4도']), KQ.COD, true) : ivqCap(' ') }) },
  ],
  make: (n, prev) => { const kind = [0, 1, 0, 2][n % 4], W0 = [0, 2, 4, 5, 7, 9, 11];
    let s, g = 0; do { s = 2 + kqRnd(n < 4 ? 5 : 7); } while (prev && prev.s === s && g++ < 8);
    if (kind === 0) { const lo = kqPick(W0), hi = ivqWhitesUp(lo, s)[s - 1], seq = ivqWhitesUp(lo, s).map(ivqL).join(' ');
      return { s, kind: 'choice', cols: 4, prompt: ['What number is this interval? Count the letters from the lower key.', '이 음정은 몇 도일까요? 아래 건반부터 글자를 세어 보세요.'], opts: ivqNumOpts(), ans: String(s), ok: (v) => v === String(s), play: () => ivqPlay(lo, hi),
        fig: (c) => ({ kb: c.res ? ivqLetters(lo, hi, 99, { ks: [lo, lo + 12] }) : ivqKb({ ks: [lo, lo + 12], marks: { [lo]: 'pick', [hi]: 'pick' } }) }),
        yes: [seq + ': ' + s + ' letters, ' + ivqA(s)[0] + '.', seq + ', 글자 ' + s + '개라서 ' + ivqA(s)[1] + '예요.'], no: ['Count again with ' + ivqL(lo) + ' as 1: ' + seq + '. That is ' + ivqA(s)[0] + '.', ivqL(lo) + '부터 1로 다시 세어 보세요. ' + seq + ', ' + ivqA(s)[1] + '예요.'] }; }
    const up = kind === 1, a = up ? kqPick(W0) : kqPick(W0.map(x => x + 12)), ks = up ? ivqWhitesUp(a, s) : ivqWhitesDown(a, s), b = ks[s - 1], seq = ks.map(ivqL).join(' ');
    return { s, kind: 'key', retry: true, prompt: up ? ['Tap the key ' + ivqA(s)[0] + ' above the marked key.', '표시된 건반에서 ' + ivqA(s)[1] + ' 위의 건반을 눌러 보세요.'] : ['Tap the key ' + ivqA(s)[0] + ' below the marked key.', '표시된 건반에서 ' + ivqA(s)[1] + ' 아래의 건반을 눌러 보세요.'], play: () => playKey(a, 0.6),
      fig: (c) => ({ kb: c.res === 'ok' ? ivqLetters(a, b, 99, { ks: up ? [a, a + 12] : [a - 12, a] }) : ivqKb({ ks: up ? [a, a + 12] : [a - 12, a], marks: { [a]: 'pick' } }) }), ok: (k) => k === b,
      yes: [seq + ': ' + ivqA(s)[0] + (up ? ' up.' : ' down.'), seq + ', ' + (up ? '위로 ' : '아래로 ') + ivqA(s)[1] + '예요.'],
      no: (k) => k === a ? ['That is the marked key itself: it counts as 1. Count on from there.', '그건 표시된 건반 자신이에요. 그게 1이에요. 거기서부터 세어 보세요.']
        : !ivqWhite(k) ? ['Count on the white keys here: ' + seq + '.', '여기서는 흰건반으로 세어요. ' + seq + '.']
        : (up ? k < a : k > a) ? [up ? 'Go up: to the right of the marked key.' : 'Go down: to the left of the marked key.', up ? '위로, 표시된 건반의 오른쪽으로 가요.' : '아래로, 표시된 건반의 왼쪽으로 가요.']
        : ivqCountW(a, k) > 8 ? ['That is more than an octave away. Count ' + s + ' letters with ' + ivqL(a) + ' as 1.', '그건 옥타브보다 멀어요. ' + ivqL(a) + '를 1로 글자 ' + s + '개를 세어 보세요.'] : ['That is ' + ivqA(ivqCountW(a, k))[0] + '. Count ' + s + ' letters with ' + ivqL(a) + ' as 1.', '그건 ' + ivqA(ivqCountW(a, k))[1] + '예요. ' + ivqL(a) + '를 1로 글자 ' + s + '개를 세어 보세요.'] }; },
};

// ── lesson 2: on the staff, every line and space counts
const IVQ_ODD = (n) => n % 2 === 1;
IVQ_SPEC['iv-staff'] = {
  title: ['Intervals on the staff', '오선 위의 음정'], allLine: ['On the staff, count every line and every space from the lower note. The lower note is 1.', '오선에서는 아래 음부터 줄과 칸을 하나씩 모두 세어요. 아래 음이 1이에요.'],
  fig: (c) => ({ staff: ivqStaffEl({ d: 30 }, { d: 34 }, { ladder: 'all', colors: [KQ.COD, KQ.COD] }), below: ivqCap(kqT(['E to B: line 1 to line 3, a 5th', 'E에서 B: 1번 줄에서 3번 줄, 5도']), KQ.COD, true) }),
  steps: [
    { title: ['A 2nd: the very next place', '2도: 바로 다음 자리'], line: ['From a line to the space just above it, or from a space to the line just above. One step up the staff.', '줄에서 바로 위 칸으로, 또는 칸에서 바로 위 줄로. 오선에서 한 걸음이에요.'], fig: () => ({ staff: ivqStaffEl({ d: 30 }, { d: 31 }, { ladder: 2, colors: [KQ.COD, KQ.COD] }), kb: ivqLetters(4, 5, 99, { ks: [0, 12] }) }) },
    { title: ['A 3rd: the next line', '3도: 다음 줄'], line: ['From a line to the next line up, over the space between. A space to the next space works the same.', '줄에서 사이 칸을 건너 다음 줄로. 칸에서 다음 칸으로 가도 똑같아요.'], fig: () => ({ staff: ivqStaffEl({ d: 30 }, { d: 32 }, { ladder: 3, colors: [KQ.COD, KQ.COD] }), kb: ivqLetters(4, 7, 99, { ks: [0, 12] }) }) },
    { title: ['A 5th: one line skipped', '5도: 줄 하나 건너'], line: ['Line 1 to line 3: one line is skipped in between.', '1번 줄에서 3번 줄로. 사이에 줄 하나를 건너뛰어요.'], fig: () => ({ staff: ivqStaffEl({ d: 30 }, { d: 34 }, { ladder: 5, colors: [KQ.COD, KQ.COD] }), kb: ivqLetters(4, 11, 99, { ks: [0, 12] }) }) },
    { title: ['Odd stays, even swaps', '홀수는 그대로, 짝수는 바뀌어요'], line: ['3rds, 5ths and 7ths stay on the same kind: line to line, or space to space. 2nds, 4ths, 6ths and octaves swap: line to space, or space to line.', '3도, 5도, 7도는 같은 종류에 머물러요. 줄에서 줄, 칸에서 칸이에요. 2도, 4도, 6도, 옥타브는 바뀌어요. 줄에서 칸, 칸에서 줄이에요.'],
      fig: (c) => { const n = 2 + (Math.floor(c.tk / 2) % 7), odd = IVQ_ODD(n); return { staff: ivqStaffEl({ d: 30 }, { d: 30 + n - 1 }, { ladder: 'odd' + n, colors: [KQ.COD, KQ.COD] }), below: ivqCap(kqT(odd ? [ivqA(n)[0].replace(/^an? /, '') + ': line to line, it stays', ivqA(n)[1] + ': 줄에서 줄, 그대로'] : [ivqA(n)[0].replace(/^an? /, '') + ': line to space, it swaps', ivqA(n)[1] + ': 줄에서 칸, 바뀌어요']), odd ? KQ.NV : KQ.COD, true) }; } },
  ],
  make: (n, prev) => { let s, g = 0; do { s = 2 + kqRnd(7); } while (prev && prev.s === s && g++ < 8);
    const lo = 29 + kqRnd(Math.max(1, 40 - 29 - s + 1 - 1)), hi = lo + s - 1, a = { d: lo }, b = { d: hi }, harm = n % 2 === 1, onLine = lo % 2 === 0;
    if (n % 3 === 2) { const lands = IVQ_ODD(s) === onLine ? 'line' : 'space';
      return { s, kind: 'choice', cols: 2, prompt: onLine ? ['The lower note sits on a line. ' + ivqA(s)[0].replace(/^a/, 'A') + ' above it lands on…', '아래 음이 줄 위에 있어요. 그 위로 ' + ivqA(s)[1] + '는 어디에 앉을까요?'] : ['The lower note sits in a space. ' + ivqA(s)[0].replace(/^a/, 'A') + ' above it lands on…', '아래 음이 칸 안에 있어요. 그 위로 ' + ivqA(s)[1] + '는 어디에 앉을까요?'],
        opts: [{ id: 'line', label: () => t('A line', '줄') }, { id: 'space', label: () => t('A space', '칸') }], ans: lands, ok: (v) => v === lands,
        fig: (c) => ({ staff: c.res ? ivqStaffEl(a, b, { ladder: 'q' + n, colors: [KQ.COD, KQ.COD] }) : <div style={{ maxWidth: 360, margin: '0 auto' }}><IvqStaff a={a}/></div> }),
        yes: [IVQ_ODD(s) ? 'Odd numbers stay: ' + (onLine ? 'line to line.' : 'space to space.') : 'Even numbers swap: ' + (onLine ? 'line to space.' : 'space to line.'), IVQ_ODD(s) ? '홀수는 그대로예요. ' + (onLine ? '줄에서 줄.' : '칸에서 칸.') : '짝수는 바뀌어요. ' + (onLine ? '줄에서 칸.' : '칸에서 줄.')],
        no: [ivqA(s)[0].replace(/^a/, 'A') + (IVQ_ODD(s) ? ' is odd, so it stays: ' : ' is even, so it swaps: ') + (lands === 'line' ? 'a line.' : 'a space.'), ivqA(s)[1] + (IVQ_ODD(s) ? '는 홀수라서 그대로예요: ' : '는 짝수라서 바뀌어요: ') + (lands === 'line' ? '줄.' : '칸.')] }; }
    return { s, kind: 'choice', cols: 4, prompt: harm ? ['What number is this interval? The notes are played together.', '이 음정은 몇 도일까요? 두 음을 함께 쳐요.'] : ['What number is this interval? Count the lines and spaces.', '이 음정은 몇 도일까요? 줄과 칸을 세어 보세요.'], opts: ivqNumOpts(), ans: String(s), ok: (v) => v === String(s),
      play: () => ivqPlay(ivqKeyOf(a), ivqKeyOf(b), harm ? 'harm' : 'mel'),
      fig: (c) => ({ staff: ivqStaffEl(a, b, { harm, ladder: c.res ? 'q' + n : null, colors: c.res ? [KQ.COD, KQ.COD] : [] }), kb: c.res ? ivqLetters(ivqKeyOf(a), ivqKeyOf(b), 99, { ks: [ivqKeyOf(a), ivqKeyOf(a) + 12] }) : null }),
      yes: ['Yes, ' + ivqA(s)[0] + ': ' + s + ' lines and spaces, both notes included.', '맞아요. ' + ivqA(s)[1] + '예요. 두 음을 넣어 줄과 칸이 ' + s + '개예요.'], no: ['Count every line and space, with the lower note as 1. You get ' + s + ': ' + ivqA(s)[0] + '.', '아래 음을 1로 줄과 칸을 모두 세면 ' + s + '개, ' + ivqA(s)[1] + '예요.'] }; },
};

// ══ 2. Major, minor and perfect ══
// ── lesson 3: count the half steps
const IVQ_3RDS = [[0, 4, 'C', 'E'], [2, 5, 'D', 'F'], [4, 7, 'E', 'G'], [5, 9, 'F', 'A'], [7, 11, 'G', 'B'], [9, 12, 'A', 'C'], [11, 14, 'B', 'D'], [2, 6, 'D', 'F♯'], [9, 13, 'A', 'C♯'], [0, 3, 'C', 'E♭'], [7, 10, 'G', 'B♭'], [4, 8, 'E', 'G♯']];
IVQ_SPEC['iv-half'] = {
  title: ['Count the half steps', '반음을 세어요'], allLine: ['C to E and D to F are both 3rds, but they are not the same size. Count the half steps to see the difference.', 'C에서 E, D에서 F는 둘 다 3도지만 크기가 같지 않아요. 반음을 세어 보면 차이가 보여요.'],
  fig: () => ({ top: <>{ivqKbEl({ ...ivqHops(0, 4), ks: [0, 7] })}{ivqCap(kqT(['C to E: 4 half steps', 'C에서 E: 반음 4개']), KQ.COD)}</>, kb: { ...ivqHops(2, 5), ks: [0, 7] }, below: ivqCap(kqT(['D to F: 3 half steps', 'D에서 F: 반음 3개']), KQ.COD) }),
  steps: [
    { title: ['One half step', '반음 하나'], line: ['A half step goes to the very next key, black or white, with no key in between. E to F is a half step too: no black key sits between them.', '반음은 바로 옆 건반으로 가는 거예요. 검은건반이든 흰건반이든, 사이에 건반이 없어요. E에서 F도 반음이에요. 둘 사이에 검은건반이 없거든요.'],
      fig: () => ({ kb: ivqKb({ ks: [0, 7], marks: { 0: 'pick', 1: 'pick', 4: 'pick', 5: 'pick' }, arcs: [[0, 1, false, KQ.CO], [4, 5, false, KQ.CO]], names: { 1: '1', 5: '1' }, ncol: { 1: KQ.COD, 5: KQ.COD } }) }) },
    { title: ['C to E: 4', 'C에서 E: 4'], line: ['Hop key by key from C to E and count each hop: 4 half steps.', 'C에서 E까지 건반 하나씩 뛰며 세어 보세요. 반음 4개예요.'], fig: (c) => ({ kb: { ...ivqHops(0, 4, Math.min(c.tk + 1, 4)), ks: [0, 7] } }) },
    { title: ['D to F: 3', 'D에서 F: 3'], line: ['From D to F there are only 3 hops.', 'D에서 F까지는 3번만 뛰어요.'], fig: (c) => ({ kb: { ...ivqHops(2, 5, Math.min(c.tk + 1, 3)), ks: [0, 7] } }) },
    { title: ['Two sizes of 3rd', '3도의 두 가지 크기'], line: ['Both span three letters, so both are 3rds. The bigger one, 4 half steps, is a major 3rd. The smaller one, 3 half steps, is a minor 3rd.', '둘 다 글자 세 개라서 3도예요. 반음 4개인 큰 쪽이 장3도, 반음 3개인 작은 쪽이 단3도예요.'],
      fig: () => ({ top: <>{ivqKbEl({ ...ivqHops(0, 4), ks: [0, 7] })}{ivqCap(kqT(['C to E: 4 half steps, a major 3rd', 'C에서 E: 반음 4개, 장3도']), KQ.COD)}</>, kb: { ...ivqHops(2, 5), ks: [0, 7] }, below: ivqCap(kqT(['D to F: 3 half steps, a minor 3rd', 'D에서 F: 반음 3개, 단3도']), KQ.COD) }) },
  ],
  make: (n, prev) => { const kind = [0, 1, 2, 0, 2, 1][n % 6];
    if (kind === 0) { let r, g = 0; do { r = kqPick(IVQ_3RDS); } while (prev && prev.r === r && g++ < 8); const [a, b, A, B] = r, M = b - a === 4;
      return { r, kind: 'choice', cols: 2, prompt: ['Both notes are a 3rd apart. Major 3rd or minor 3rd? Count the half steps.', '두 음은 3도 떨어져 있어요. 장3도일까요, 단3도일까요? 반음을 세어 보세요.'], opts: [{ id: 'M', label: () => kqT(ivqNm('M', 3)) }, { id: 'm', label: () => kqT(ivqNm('m', 3)) }], ans: M ? 'M' : 'm', ok: (v) => v === (M ? 'M' : 'm'), play: () => ivqPlay(a, b, 'both'),
        fig: (c) => ({ kb: c.res ? { ...ivqHops(a, b), ks: [a, a + 12] } : ivqKb({ ks: [a, a + 12], marks: { [a]: 'pick', [b]: 'pick' } }) }),
        yes: [A + ' to ' + B + ': ' + (b - a) + ' half steps, ' + ivqAn(M ? 'M' : 'm', 3)[0] + '.', A + '에서 ' + B + ': 반음 ' + (b - a) + '개, ' + ivqNm(M ? 'M' : 'm', 3)[1] + '예요.'],
        no: [A + ' to ' + B + ' is ' + (b - a) + ' half steps. ' + (M ? '4 is a major 3rd.' : '3 is a minor 3rd.'), A + '에서 ' + B + '까지 반음 ' + (b - a) + '개예요. ' + (M ? '4개는 장3도예요.' : '3개는 단3도예요.')] }; }
    if (kind === 1) { const h = 1 + kqRnd(7), a = kqPick([0, 2, 4, 5, 7, 9, 11]), b = a + h, set = [...new Set([h, h + 1, h - 1 > 0 ? h - 1 : h + 2, h + 2])].slice(0, 4).sort((x, y) => x - y);
      return { kind: 'choice', cols: 4, prompt: ['How many half steps from the lower marked key to the higher one?', '아래 표시 건반에서 위 표시 건반까지 반음 몇 개일까요?'], opts: set.map(x => ({ id: String(x), label: String(x) })), ans: String(h), ok: (v) => v === String(h),
        fig: (c) => ({ kb: c.res ? { ...ivqHops(a, b), ks: [a, a + 12] } : ivqKb({ ks: [a, a + 12], marks: { [a]: 'pick', [b]: 'pick' } }) }),
        yes: [h === 1 ? 'One hop: 1 half step.' : h + ' hops: ' + h + ' half steps.', h + '번 뛰었어요. 반음 ' + h + '개예요.'], no: ['Hop key by key, black keys too. It is ' + h + (h === 1 ? ' hop.' : ' hops.'), '검은건반까지 건반 하나씩 뛰어 보세요. ' + h + '번이에요.'] }; }
    const M = Math.random() < 0.5, a = kqPick([0, 2, 4, 5, 7, 9]), b = a + (M ? 4 : 3);
    return { kind: 'key', retry: true, prompt: M ? ['Tap the key a major 3rd above the marked key: 4 half steps up.', '표시된 건반에서 장3도 위, 반음 4개 위의 건반을 눌러 보세요.'] : ['Tap the key a minor 3rd above the marked key: 3 half steps up.', '표시된 건반에서 단3도 위, 반음 3개 위의 건반을 눌러 보세요.'], play: () => playKey(a, 0.6),
      fig: (c) => ({ kb: c.res === 'ok' ? { ...ivqHops(a, b), ks: [a, a + 12] } : ivqKb({ ks: [a, a + 12], marks: { [a]: 'pick' } }) }), ok: (k) => k === b,
      yes: [(M ? '4' : '3') + ' half steps: ' + ivqAn(M ? 'M' : 'm', 3)[0] + '.', '반음 ' + (M ? '4' : '3') + '개, ' + ivqNm(M ? 'M' : 'm', 3)[1] + '예요.'],
      no: (k) => k <= a ? ['Go up: to the right of the marked key.', '위로, 표시된 건반의 오른쪽으로 가요.'] : ['That is ' + (k - a) + ' half step' + (k - a === 1 ? '' : 's') + ' up. ' + (M ? 'A major 3rd is 4.' : 'A minor 3rd is 3.'), '그건 반음 ' + (k - a) + '개 위예요. ' + (M ? '장3도는 4개예요.' : '단3도는 3개예요.')] }; },
};

// ── lesson 4: above the key note of a major scale every interval is major or perfect
const IVQ_KEYS = { C: { k: 0, names: ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C'] }, G: { k: 7, names: ['G', 'A', 'B', 'C', 'D', 'E', 'F♯', 'G'] }, D: { k: 2, names: ['D', 'E', 'F♯', 'G', 'A', 'B', 'C♯', 'D'] }, F: { k: 5, names: ['F', 'G', 'A', 'B♭', 'C', 'D', 'E', 'F'] } };
const ivqQOf = (n) => [2, 3, 6, 7].includes(n) ? 'M' : 'P';
const ivqShort = (n) => n === 8 ? ['8ve', '옥타브'] : [(ivqQOf(n) === 'M' ? 'M' : 'P') + n, (ivqQOf(n) === 'M' ? '장' : '완') + n];
const ivqTonicKb = (key, only, extra = {}) => { const K = IVQ_KEYS[key], m = {}, names = {}, ncol = {};
  IVQ_SCALE.forEach((s, i) => { const k = K.k + s, n = i + 1; if (n === 1) { m[k] = 'pick'; return; } if (only && !only.includes(n)) { m[k] = 'pass'; return; } m[k] = ivqQOf(n) === 'M' ? 'seg3' : 'seg4'; names[k] = kqT(ivqShort(n)); ncol[k] = ivqQOf(n) === 'M' ? KQ.COD : KQ.BL; });
  return ivqKb({ ks: [K.k, K.k + 12], ...extra, marks: { ...m, ...(extra.marks || {}) }, names, ncol }); };
IVQ_SPEC['iv-tonic'] = {
  title: ['Above the key note', '으뜸음 위의 음정'], allLine: ['Start on the key note of a major scale. Every note of the scale above it makes a major or a perfect interval. Tap one to hear it with the key note.', '장음계의 으뜸음에서 시작해요. 그 위 음계의 음은 모두 장음정이나 완전음정이 돼요. 하나를 눌러 으뜸음과 함께 들어 보세요.'],
  fig: (c) => { const i = typeof c.last === 'number' ? IVQ_SCALE.indexOf(c.last) : -1;
    return { kb: { ...ivqTonicKb('C'), onTap: (k) => { const j = IVQ_SCALE.indexOf(k); if (j > 0) setTimeout(() => ivqPlay(0, k, 'harm'), 300); } }, below: i > 0 ? ivqCap(kqT(['C to ' + IVQ_KEYS.C.names[i] + ': ' + ivqAn(ivqQOf(i + 1), i + 1)[0], 'C에서 ' + IVQ_KEYS.C.names[i] + ': ' + ivqNm(ivqQOf(i + 1), i + 1)[1]]), ivqQOf(i + 1) === 'M' ? KQ.COD : KQ.BL, true) : ivqCap(kqT(['M = major, P = perfect', '장 = 장음정, 완 = 완전음정'])) }; },
  steps: [
    { title: ['Major: 2nd, 3rd, 6th, 7th', '장음정: 2도, 3도, 6도, 7도'], line: ['From the key note C, the 2nd, 3rd, 6th and 7th above are major: 2, 4, 9 and 11 half steps.', '으뜸음 C에서 위로 2도, 3도, 6도, 7도는 장음정이에요. 반음 2개, 4개, 9개, 11개예요.'], fig: () => ({ kb: ivqTonicKb('C', [2, 3, 6, 7]) }) },
    { title: ['Perfect: 4th, 5th, octave', '완전음정: 4도, 5도, 옥타브'], line: ['The 4th, 5th and octave above are called perfect: 5, 7 and 12 half steps. Perfect intervals are never major or minor.', '위로 4도, 5도, 옥타브는 완전음정이라고 불러요. 반음 5개, 7개, 12개예요. 완전음정은 장음정도 단음정도 아니에요.'], fig: () => ({ kb: ivqTonicKb('C', [4, 5, 8]) }) },
    { title: ['Every major key', '모든 장조에서'], line: ['The scale pattern is the same in every major key, so the names are too. In G major, G to B is a major 3rd and G to D a perfect 5th.', '장음계 패턴은 모든 장조에서 같아서, 이름도 같아요. G장조에서 G에서 B는 장3도, G에서 D는 완전5도예요.'], fig: () => ({ kb: ivqTonicKb('G') }) },
  ],
  make: (n, prev) => { const key = ['C', 'G', 'D', 'F'][Math.floor(n / 2) % 4], K = IVQ_KEYS[key], kind = [0, 2, 1, 2][n % 4];
    let d, g = 0; do { d = 2 + kqRnd(7); } while (prev && prev.d === d && g++ < 8);
    const top = K.k + IVQ_SCALE[d - 1], q = ivqQOf(d), nm = K.names[d - 1], scaleM = (extra) => { const m = {}; IVQ_SCALE.forEach((s, i) => { m[K.k + s] = i === 0 ? 'pick' : 'pass'; }); return { ...m, ...extra }; };
    const head = [key + ' major', key + '장조'];
    if (kind === 0) return { d, kind: 'choice', cols: 2, prompt: ['In ' + head[0] + ', the marked note is ' + ivqA(d)[0] + ' above the key note. Major or perfect?', head[1] + '에서 표시된 음은 으뜸음 위로 ' + ivqA(d)[1] + '예요. 장음정일까요, 완전음정일까요?'],
      opts: [{ id: 'M', label: () => t('Major', '장음정') }, { id: 'P', label: () => t('Perfect', '완전음정') }], ans: q, ok: (v) => v === q, play: () => ivqPlay(K.k, top, 'both'),
      fig: (c) => ({ kb: c.res ? ivqTonicKb(key, [d]) : ivqKb({ ks: [K.k, K.k + 12], marks: scaleM({ [top]: 'pickB' }) }) }),
      yes: [key + ' to ' + nm + ': ' + ivqAn(q, d)[0] + '.', key + '에서 ' + nm + ': ' + ivqNm(q, d)[1] + '예요.'], no: [q === 'M' ? '2nds, 3rds, 6ths and 7ths above the key note are major.' : '4ths, 5ths and octaves above the key note are perfect.', q === 'M' ? '으뜸음 위의 2도, 3도, 6도, 7도는 장음정이에요.' : '으뜸음 위의 4도, 5도, 옥타브는 완전음정이에요.'] };
    if (kind === 1) { const all = [2, 3, 4, 5, 6, 7, 8];
      return { d, kind: 'choice', cols: 2, prompt: ['In ' + head[0] + ': name the interval from the key note up to the marked note.', head[1] + '에서 으뜸음부터 표시된 음까지의 음정 이름은?'], opts: all.map(x => ({ id: String(x), label: () => kqT(ivqNm(ivqQOf(x), x)) })), ans: String(d), ok: (v) => v === String(d), play: () => ivqPlay(K.k, top, 'both'),
        fig: (c) => ({ kb: c.res ? ivqTonicKb(key, [d]) : ivqKb({ ks: [K.k, K.k + 12], marks: scaleM({ [top]: 'pickB' }) }) }),
        yes: [key + ' to ' + nm + ': ' + ivqAn(q, d)[0] + '.', key + '에서 ' + nm + ': ' + ivqNm(q, d)[1] + '예요.'], no: ['Count the letters from ' + key + ': ' + K.names.slice(0, d).join(' ') + ', ' + ivqA(d)[0] + '. Above the key note it is ' + IVQ_QW[q][0] + '.', key + '부터 글자를 세어 보세요. ' + K.names.slice(0, d).join(' ') + ', ' + ivqA(d)[1] + '예요. 으뜸음 위라서 ' + IVQ_QW[q][1] + '음정이에요.'] }; }
    return { d, kind: 'key', retry: true, prompt: ['In ' + head[0] + ', tap the note ' + ivqAn(q, d)[0] + ' above the key note.', head[1] + '에서 으뜸음 위로 ' + ivqNm(q, d)[1] + '인 음을 눌러 보세요.'], play: () => playKey(K.k, 0.6),
      fig: (c) => ({ kb: c.res === 'ok' ? ivqTonicKb(key, [d]) : ivqKb({ ks: [K.k, K.k + 12], marks: scaleM() }) }), ok: (k) => k === top,
      yes: [key + ' to ' + nm + ': ' + ivqAn(q, d)[0] + '.', key + '에서 ' + nm + ': ' + ivqNm(q, d)[1] + '예요.'],
      no: (k) => { const i = IVQ_SCALE.indexOf(k - K.k); return i === 0 ? ['That is the key note itself: it is 1. Count ' + d + ' letters up from it.', '그건 으뜸음 자신이에요. 그게 1이에요. 거기서부터 글자 ' + d + '개를 세어 보세요.'] : i > 0 ? ['That is ' + ivqA(i + 1)[0] + ' above ' + key + '. Count ' + d + ' letters with ' + key + ' as 1.', '그건 ' + key + ' 위로 ' + ivqA(i + 1)[1] + '예요. ' + key + '를 1로 글자 ' + d + '개를 세어 보세요.'] : ['Stay on the notes of the scale, the marked keys: count ' + d + ' with ' + key + ' as 1.', '음계의 음, 표시된 건반에서 골라요. ' + key + '를 1로 ' + d + '개를 세어 보세요.']; } }; },
};

// ── lesson 5: a major interval one half step smaller is minor
const IVQ_MIN = [[3, 'E', 'E♭'], [6, 'A', 'A♭'], [2, 'D', 'D♭'], [7, 'B', 'B♭']];
const ivqPair = (n, q) => { const top = IVQ_SCALE[n - 1] - (q === 'm' ? 1 : 0); return top; };   // from C, in half steps
const ivqMinFig = (rows) => { const els = rows.map(([n, q], j) => { const b = ivqPair(n, q), nm = q === 'm' ? IVQ_MIN.find(r => r[0] === n)[2] : IVQ_KEYS.C.names[n - 1];
  return <React.Fragment key={j}>{ivqKbEl({ ...ivqHops(0, b), ks: [0, 12] })}{ivqCap(kqT(['C to ' + nm + ': ' + b + ' half step' + (b === 1 ? '' : 's') + ', ' + ivqAn(q, n)[0], 'C에서 ' + nm + ': 반음 ' + b + '개, ' + ivqNm(q, n)[1]]), q === 'm' ? KQ.COD : KQ.BL)}</React.Fragment>; });
  return { top: <>{els}</> }; };
IVQ_SPEC['iv-minor'] = {
  title: ['One half step smaller', '반음 하나 작게'], allLine: ['Bring the top note of a major interval down one half step and it becomes minor. The number stays the same.', '장음정의 위 음을 반음 하나 내리면 단음정이 돼요. 숫자는 그대로예요.'],
  fig: () => ({ ...ivqMinFig([[3, 'M'], [3, 'm']]), staffAlt: <div style={{ display: 'flex', gap: 8, justifyContent: 'center', flexWrap: 'wrap' }}><div style={{ flex: '1 1 150px', maxWidth: 220 }}><IvqStaff a={{ d: 28 }} b={{ d: 30 }} harm labels={['C', 'E']}/></div><div style={{ flex: '1 1 150px', maxWidth: 220 }}><IvqStaff a={{ d: 28 }} b={{ d: 30, acc: -1 }} harm labels={['C', 'E♭']}/></div></div> }),
  steps: [
    { title: ['3rds', '3도'], line: ['C to E is a major 3rd, 4 half steps. C to E♭ is a minor 3rd, 3 half steps. Both still span C D E.', 'C에서 E는 장3도, 반음 4개예요. C에서 E♭은 단3도, 반음 3개예요. 둘 다 C D E 세 글자에 걸쳐 있어요.'], fig: () => ivqMinFig([[3, 'M'], [3, 'm']]) },
    { title: ['6ths', '6도'], line: ['C to A is a major 6th, 9 half steps. C to A♭ is a minor 6th, 8.', 'C에서 A는 장6도, 반음 9개예요. C에서 A♭은 단6도, 8개예요.'], fig: () => ivqMinFig([[6, 'M'], [6, 'm']]) },
    { title: ['2nds and 7ths', '2도와 7도'], line: ['C to D♭ is a minor 2nd, 1 half step. C to B♭ is a minor 7th, 10.', 'C에서 D♭은 단2도, 반음 1개예요. C에서 B♭은 단7도, 10개예요.'], fig: () => ivqMinFig([[2, 'm'], [7, 'm']]) },
    { title: ['4ths, 5ths and octaves', '4도, 5도, 옥타브'], line: ['These are perfect, never major or minor. Only 2nds, 3rds, 6ths and 7ths come in two sizes.', '이 음정들은 완전음정이에요. 장음정도 단음정도 되지 않아요. 두 가지 크기가 있는 건 2도, 3도, 6도, 7도뿐이에요.'], fig: () => ({ kb: ivqTonicKb('C') }) },
  ],
  make: (n, prev) => { const kind = [0, 1, 0, 2][n % 4], roots = [[0, 28, 'C'], [5, 31, 'F'], [7, 32, 'G']];
    let pk2, g = 0; do { pk2 = [kqPick([2, 3, 4, 5, 6, 7, 8]), Math.random() < 0.5]; } while (prev && prev.pk === pk2[0] + ':' + pk2[1] && g++ < 8);
    const [nn, flat] = pk2, q = IV_PERFECT[nn] ? 'P' : flat ? 'm' : 'M', [rk, rd, rn] = kqPick(roots), top = ivBuild({ d: rd, acc: 0 }, nn, q), tk = ivqKeyOf(top), tn = ivName(top), semis = tk - rk;
    if (kind === 0) { const valid = (x, y) => x >= 2 && x <= 8 && (IV_PERFECT[x] ? y === 'P' : y !== 'P');
      const pool = [[nn, 'M'], [nn, 'm'], [nn - 1, 'M'], [nn - 1, 'm'], [nn + 1, 'M'], [nn + 1, 'm'], [nn - 1, 'P'], [nn + 1, 'P']].filter(([x, y]) => valid(x, y) && !(x === nn && y === q));
      const opts = shuffle([[nn, q], ...shuffle(pool.filter(([x]) => x === nn)).concat(shuffle(pool.filter(([x]) => x !== nn))).slice(0, 3)]);
      return { pk: nn + ':' + flat, kind: 'choice', cols: 2, prompt: ['Name the interval from ' + rn + ' up to ' + tn + '.', rn + '에서 ' + tn + '까지의 음정 이름은?'], opts: opts.map(([x, y]) => ({ id: y + x, label: () => kqT(ivqNm(y, x)) })), ans: q + nn, ok: (v) => v === q + nn, play: () => ivqPlay(rk, tk, 'both'),
        fig: (c) => ({ kb: c.res ? { ...ivqHops(rk, tk), ks: [rk, rk + 12] } : ivqKb({ ks: [rk, rk + 12], marks: { [rk]: 'pick', [tk]: 'pick' } }), staffAlt: ivqStaffEl({ d: rd }, top, { labels: [rn, tn] }) }),
        yes: [rn + ' to ' + tn + ': ' + semis + ' half steps, ' + ivqAn(q, nn)[0] + '.', rn + '에서 ' + tn + ': 반음 ' + semis + '개, ' + ivqNm(q, nn)[1] + '예요.'],
        no: ['First the letters: ' + ivqA(nn)[0] + '. Then the half steps: ' + semis + '. That makes ' + ivqAn(q, nn)[0] + '.', '먼저 글자를 세면 ' + ivqA(nn)[1] + '예요. 그다음 반음을 세면 ' + semis + '개예요. 그래서 ' + ivqNm(q, nn)[1] + '예요.'] }; }
    if (kind === 1) { const nm2 = [2, 3, 6, 7][kqRnd(4)], q2 = Math.random() < 0.5 ? 'm' : 'M', top2 = ivBuild({ d: rd, acc: 0 }, nm2, q2), tk2 = ivqKeyOf(top2), s2 = tk2 - rk;
      return { pk: nm2 + ':' + q2, kind: 'key', retry: true, prompt: ['Tap the key ' + ivqAn(q2, nm2)[0] + ' above ' + rn + '.', rn + ' 위로 ' + ivqNm(q2, nm2)[1] + '인 건반을 눌러 보세요.'], play: () => playKey(rk, 0.6),
        fig: (c) => ({ kb: c.res === 'ok' ? { ...ivqHops(rk, tk2), ks: [rk, rk + 12] } : ivqKb({ ks: [rk, rk + 12], marks: { [rk]: 'pick' } }) }), ok: (k) => k === tk2,
        yes: [rn + ' to ' + ivName(top2) + ': ' + s2 + ' half steps.', rn + '에서 ' + ivName(top2) + ': 반음 ' + s2 + '개예요.'],
        no: (k) => k <= rk ? ['Go up: to the right of ' + rn + '.', '위로, ' + rn + '의 오른쪽으로 가요.'] : ['That is ' + (k - rk) + ' half steps up. ' + ivqAn(q2, nm2)[0].replace(/^a/, 'A') + ' is ' + s2 + '.', '그건 반음 ' + (k - rk) + '개 위예요. ' + ivqNm(q2, nm2)[1] + '는 ' + s2 + '개예요.'] }; }
    const nm3 = [2, 3, 6, 7][kqRnd(4)], q3 = Math.random() < 0.5 ? 'm' : 'M', s3 = IVQ_SCALE[nm3 - 1] - (q3 === 'm' ? 1 : 0), set = shuffle([...new Set([s3, s3 + 1, s3 - 1, s3 + 2, s3 - 2].filter(x => x > 0))].slice(0, 4));
    return { pk: nm3 + ':' + q3, kind: 'choice', cols: 4, prompt: ['How many half steps make ' + ivqAn(q3, nm3)[0] + '?', ivqNm(q3, nm3)[1] + '는 반음 몇 개일까요?'], opts: set.map(x => ({ id: String(x), label: String(x) })), ans: String(s3), ok: (v) => v === String(s3),
      fig: (c) => ({ kb: c.res ? { ...ivqHops(0, s3), ks: [0, 12] } : ivqKb({ ks: [0, 12], marks: { 0: 'pick' } }) }),
      yes: [s3 + ' half steps' + (q3 === 'm' ? ': one fewer than the major ' + ivqOrdEn(nm3) + '.' : '.'), '반음 ' + s3 + '개예요' + (q3 === 'm' ? '. 장' + nm3 + '도보다 하나 적어요.' : '.')],
      no: [ivqAn('M', nm3)[0].replace(/^a/, 'A') + ' is ' + IVQ_SCALE[nm3 - 1] + ' half steps' + (q3 === 'm' ? '; the minor one is one fewer: ' + s3 + '.' : '.'), '장' + nm3 + '도는 반음 ' + IVQ_SCALE[nm3 - 1] + '개예요' + (q3 === 'm' ? '. 단음정은 하나 적은 ' + s3 + '개예요.' : '.')] }; },
};

// ══ 3. Hearing intervals ══
// ── lesson 6: melodic and harmonic
const ivqMHFig = (harm, a, b) => { const ka = ivqKeyOf(a), kb = ivqKeyOf(b);
  return { staff: ivqStaffEl(a, b, { harm, colors: [KQ.COD, KQ.COD] }), mid: <div style={{ textAlign: 'center', margin: '4px 0 6px' }}>{ivqPlayBtn(t('▶ Listen', '▶ 들어 보기'), () => ivqPlay(ka, kb, harm ? 'harm' : 'mel'))}</div>, kb: ivqKb({ ks: [0, 12], marks: { [ka]: 'pick', [kb]: 'pick' } }) }; };
IVQ_SPEC['iv-mh'] = {
  title: ['Melodic and harmonic', '선율 음정과 화성 음정'], allLine: ['Two notes one after the other make a melodic interval. Two notes played together make a harmonic interval.', '두 음을 하나씩 차례로 치면 선율 음정, 함께 치면 화성 음정이에요.'],
  fig: () => ({ top: <div style={{ display: 'flex', gap: 10, justifyContent: 'center', flexWrap: 'wrap' }}>
    {[false, true].map(h => <div key={String(h)} style={{ flex: '1 1 150px', maxWidth: 240, textAlign: 'center' }}><IvqStaff a={{ d: 28 }} b={{ d: 32 }} harm={h} colors={[KQ.COD, KQ.COD]}/>{ivqCap(h ? t('Together', '함께') : t('One after the other', '하나씩 차례로'), KQ.COD)}{ivqPlayBtn(t('▶ Listen', '▶ 들어 보기'), () => ivqPlay(0, 7, h ? 'harm' : 'mel'))}</div>)}</div> }),
  steps: [
    { title: ['One after the other', '하나씩 차례로'], line: ['Melodic: the notes are written side by side and played one at a time, like a tune.', '선율 음정: 음표를 나란히 쓰고, 노래처럼 하나씩 쳐요.'], fig: () => ivqMHFig(false, { d: 28 }, { d: 32 }) },
    { title: ['Together', '함께'], line: ['Harmonic: the notes are written one above the other and played at the same time.', '화성 음정: 음표를 위아래로 겹쳐 쓰고, 동시에 쳐요.'], fig: () => ivqMHFig(true, { d: 28 }, { d: 32 }) },
    { title: ['A 2nd together', '함께 치는 2도'], line: ['Two notes a 2nd apart are too close to stack, so one sits beside the other. They are still played together.', '2도 떨어진 두 음은 너무 가까워서 겹쳐 쓸 수 없어요. 하나를 옆으로 비켜 쓰고, 그래도 함께 쳐요.'], fig: () => ivqMHFig(true, { d: 30 }, { d: 31 }) },
  ],
  make: (n, prev) => { const harm = Math.random() < 0.5, s = 2 + kqRnd(7), lo = 28 + kqRnd(5), a = { d: lo }, b = { d: lo + s - 1 }, ka = ivqKeyOf(a), kb = ivqKeyOf(b), ans = harm ? 'h' : 'm';
    const opts = [{ id: 'm', label: () => t('Melodic: one after the other', '선율 음정: 하나씩') }, { id: 'h', label: () => t('Harmonic: together', '화성 음정: 함께') }];
    if (n % 2 === 0) return { kind: 'choice', cols: 1, prompt: ['Listen: one after the other, or together?', '들어 보세요. 하나씩 차례로일까요, 함께일까요?'], opts, ans, ok: (v) => v === ans, play: () => ivqPlay(ka, kb, harm ? 'harm' : 'mel'),
      fig: (c) => ({ staff: c.res ? ivqStaffEl(a, b, { harm, colors: [KQ.COD, KQ.COD] }) : null, kb: ivqKb({ ks: [ka, ka + 12], marks: c.res ? { [ka]: 'pick', [kb]: 'pick' } : {} }) }),
      yes: [harm ? 'Together: a harmonic interval.' : 'One after the other: a melodic interval.', harm ? '함께예요. 화성 음정이에요.' : '하나씩 차례로예요. 선율 음정이에요.'], no: [harm ? 'Both notes sounded at once: harmonic. Press ♪ Again and listen.' : 'One note, then the other: melodic. Press ♪ Again and listen.', harm ? '두 음이 한꺼번에 울렸어요. 화성 음정이에요. ♪ 다시를 눌러 들어 보세요.' : '한 음, 그다음 다른 음이었어요. 선율 음정이에요. ♪ 다시를 눌러 들어 보세요.'] };
    return { kind: 'choice', cols: 1, prompt: ['Melodic or harmonic?', '선율 음정일까요, 화성 음정일까요?'], opts, ans, ok: (v) => v === ans,
      fig: () => ({ staff: ivqStaffEl(a, b, { harm }) }), onPick: () => ivqPlay(ka, kb, harm ? 'harm' : 'mel'),
      yes: [harm ? 'One above the other: harmonic.' : 'Side by side: melodic.', harm ? '위아래로 겹쳐 있어요. 화성 음정이에요.' : '나란히 있어요. 선율 음정이에요.'], no: [harm ? 'The notes are stacked, one above the other: harmonic.' : 'The notes stand side by side: melodic.', harm ? '음표가 위아래로 겹쳐 있어요. 화성 음정이에요.' : '음표가 나란히 서 있어요. 선율 음정이에요.'] }; },
};

// ── lesson 7: hear the size
const IVQ_EAR = { M3: [4, 'M', 3], m3: [3, 'm', 3], P4: [5, 'P', 4], P5: [7, 'P', 5], P8: [12, 'P', 8] };
const ivqEarFig = (c, ids) => { const on = c.last && typeof c.last === 'object' && c.last.ear, e = on ? IVQ_EAR[on] : null;
  return { mid: <div style={{ display: 'flex', gap: 8, justifyContent: 'center', flexWrap: 'wrap', margin: '0 0 8px' }}>{ids.map(id => { const [h, q, n] = IVQ_EAR[id]; return <button key={id} className={'chip' + (on === id ? ' active' : '')} aria-pressed={on === id} style={{ ...KF_BTN, padding: '0 14px', fontSize: 14 }} onClick={() => { c.setLast({ ear: id }); ivqPlay(0, h, 'both'); }}>▶ {kqT(ivqNm(q, n))}</button>; })}</div>,
    kb: e ? { ...ivqHops(0, e[0]), ks: [0, 12] } : ivqKb({ ks: [0, 12], marks: { 0: 'pick' } }) }; };
IVQ_SPEC['iv-ear'] = {
  title: ['Hear the size', '크기를 들어요'], allLine: ['Tap an interval to hear it from C, one note after the other and then together. The bigger the interval, the wider the gap you hear.', '음정을 눌러 C에서부터 들어 보세요. 하나씩 친 다음 함께 쳐요. 음정이 클수록 귀에 들리는 거리도 넓어요.'],
  fig: (c) => ivqEarFig(c, ['m3', 'M3', 'P4', 'P5', 'P8']),
  steps: [
    { title: ['Major and minor 3rds', '장3도와 단3도'], line: ['Listen to both. The major 3rd is one half step wider than the minor 3rd.', '둘 다 들어 보세요. 장3도가 단3도보다 반음 하나 넓어요.'], fig: (c) => ivqEarFig(c, ['M3', 'm3']) },
    { title: ['4th and 5th', '4도와 5도'], line: ['Listen to C to F, then C to G. The 5th is two half steps wider.', 'C에서 F, 그다음 C에서 G를 들어 보세요. 5도가 반음 두 개 더 넓어요.'], fig: (c) => ivqEarFig(c, ['P4', 'P5']) },
    { title: ['The octave', '옥타브'], line: ['C and the next C up share a name. Played together, they sound almost like one note.', 'C와 그 위의 다음 C는 이름이 같아요. 함께 치면 거의 한 음처럼 들려요.'], fig: (c) => ivqEarFig(c, ['P8', 'P5']) },
  ],
  make: (n, prev) => { const set = [['M3', 'm3'], ['P4', 'P5', 'P8'], ['m3', 'M3', 'P5', 'P8']][n % 3]; let id, g = 0; do { id = kqPick(set); } while (prev && prev.id === id && g++ < 8);
    const [h, q, nn] = IVQ_EAR[id], r = kqPick([0, 2, 5, 7]), rn = ivqL(r);
    return { id, kind: 'choice', cols: set.length > 2 ? 2 : 2, prompt: ['Listen: which interval is it?', '들어 보세요. 어떤 음정일까요?'], opts: set.map(x => ({ id: x, label: () => kqT(ivqNm(IVQ_EAR[x][1], IVQ_EAR[x][2])) })), ans: id, ok: (v) => v === id, play: () => ivqPlay(r, r + h, 'both'),
      fig: (c) => ({ kb: c.res ? { ...ivqHops(r, r + h), ks: [r, r + 12] } : ivqKb({ ks: [r, r + 12], marks: { [r]: 'pick' } }) }),
      yes: ['Yes, ' + ivqAn(q, nn)[0] + ': ' + h + ' half steps.', '맞아요. ' + ivqNm(q, nn)[1] + ', 반음 ' + h + '개예요.'], no: ['It was ' + ivqAn(q, nn)[0] + ', ' + h + ' half steps up from ' + rn + '. Press ♪ Again to hear it once more.', ivqNm(q, nn)[1] + '였어요. ' + rn + '에서 반음 ' + h + '개 위예요. ♪ 다시를 눌러 한 번 더 들어 보세요.'] }; },
};

// ══ 4. Turning it over ══
// ── lesson 8: invert an interval
const ivqInvFig = (a, b, q1, q2, withHops) => { const n1 = ivqCountW(a, b), n2 = 9 - n1;
  return { top: <>{ivqKbEl(withHops ? { ...ivqHops(a, b), ks: [0, 16] } : ivqLetters(a, b, 99, { ks: [0, 16] }))}{ivqCap(kqT([ivqL(a) + ' up to ' + ivqL(b) + ': ' + (q1 ? ivqAn(q1, n1)[0] : ivqA(n1)[0]), ivqL(a) + '에서 ' + ivqL(b) + ': ' + (q1 ? ivqNm(q1, n1)[1] : ivqA(n1)[1])]), KQ.COD)}</>,
    kb: withHops ? { ...ivqHops(b, a + 12), ks: [0, 16] } : ivqLetters(b, a + 12, 99, { ks: [0, 16] }), below: <>{ivqCap(kqT([ivqL(b) + ' up to ' + ivqL(a) + ': ' + (q2 ? ivqAn(q2, n2)[0] : ivqA(n2)[0]), ivqL(b) + '에서 ' + ivqL(a) + ': ' + (q2 ? ivqNm(q2, n2)[1] : ivqA(n2)[1])]), KQ.COD)}{ivqCap(n1 + ' + ' + n2 + ' = 9', KQ.NV, true)}</> }; };
IVQ_SPEC['iv-invert'] = {
  title: ['Turn it upside down', '음정 뒤집기'], allLine: ['Move the lower note up an octave and the interval turns upside down. The two numbers always add up to 9.', '아래 음을 한 옥타브 위로 올리면 음정이 뒤집혀요. 두 숫자를 더하면 언제나 9예요.'],
  fig: () => ivqInvFig(0, 4),
  steps: [
    { title: ['A 3rd becomes a 6th', '3도는 6도로'], line: ['C up to E is a 3rd. Move the C up an octave: E up to C is a 6th.', 'C에서 E는 3도예요. C를 한 옥타브 올리면 E에서 C는 6도예요.'], fig: () => ivqInvFig(0, 4) },
    { title: ['Pairs that make 9', '합이 9인 짝'], line: ['2nd and 7th, 3rd and 6th, 4th and 5th: each pair adds up to 9. So do the unison and the octave, 1 and 8.', '2도와 7도, 3도와 6도, 4도와 5도. 짝마다 더하면 9예요. 1도와 옥타브, 1과 8을 더해도 9예요.'],
      fig: (c) => ({ mid: <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(92px, 1fr))', gap: 8, maxWidth: 440, margin: '6px auto' }}>{[[2, 7], [3, 6], [4, 5], [1, 8]].map(([x, y], i) => <div key={x} style={{ border: '1.5px solid ' + (i === Math.floor(c.tk / 2) % 4 ? KQ.CO : 'rgba(38,41,107,0.14)'), borderRadius: 10, padding: '10px 2px', textAlign: 'center', background: i === Math.floor(c.tk / 2) % 4 ? '#fbe3da' : '#fffefa', transition: 'all 0.3s' }}><div style={{ fontSize: 24, fontWeight: 900, color: KQ.NV, whiteSpace: 'nowrap', fontVariantNumeric: 'tabular-nums' }}>{x} ↔ {y}</div><div style={{ fontSize: 13, fontWeight: 800, color: KQ.COD }}>= 9</div></div>)}</div>,
        kb: (() => { const [x] = [[2, 7], [3, 6], [4, 5], [1, 8]][Math.floor(c.tk / 2) % 4]; const b = ivqWhitesUp(0, x)[x - 1]; return x === 1 ? ivqKb({ ks: [0, 16], marks: { 0: 'pick', 12: 'pick' }, names: { 0: '1', 12: '8' }, ncol: { 0: KQ.COD, 12: KQ.COD } }) : ivqLetters(0, b, 99, { ks: [0, 16] }); })() }) },
    { title: ['Major becomes minor', '장은 단으로'], line: ['Major turns into minor, and minor into major. Perfect stays perfect. C to E, a major 3rd, turns into E to C, a minor 6th.', '장음정은 단음정으로, 단음정은 장음정으로 바뀌어요. 완전음정은 그대로 완전음정이에요. 장3도 C–E를 뒤집으면 단6도 E–C가 돼요.'], fig: () => ivqInvFig(0, 4, 'M', 'm', true) },
  ],
  make: (n, prev) => { let nn, g = 0; do { nn = 2 + kqRnd(6); } while (prev && prev.nn === nn && g++ < 8); const inv = 9 - nn;
    if (n % 2 === 0) return { nn, kind: 'choice', cols: 4, prompt: [ivqA(nn)[0].replace(/^a/, 'A') + ' turned upside down becomes…', ivqA(nn)[1] + '를 뒤집으면…'], opts: ivqNumOpts(), ans: String(inv), ok: (v) => v === String(inv),
      fig: (c) => { const b = ivqWhitesUp(0, nn)[nn - 1]; return c.res ? ivqInvFig(0, b) : { kb: ivqLetters(0, b, 99, { ks: [0, 16] }) }; },
      yes: [nn + ' + ' + inv + ' = 9: ' + ivqA(inv)[0] + '.', nn + ' + ' + inv + ' = 9, ' + ivqA(inv)[1] + '예요.'], no: ['The two numbers add up to 9: ' + nn + ' + ' + inv + '. It becomes ' + ivqA(inv)[0] + '.', '두 숫자를 더하면 9예요. ' + nn + ' + ' + inv + ', ' + ivqA(inv)[1] + '가 돼요.'] };
    const q = IV_PERFECT[nn] ? 'P' : Math.random() < 0.5 ? 'M' : 'm', qi = q === 'P' ? 'P' : q === 'M' ? 'm' : 'M', ans = qi + inv;
    const cand = [[qi, inv], [q === 'P' ? 'M' : q, inv], [qi === 'P' ? 'M' : qi, nn], [q, nn]].map(([x, y]) => [IV_PERFECT[y] ? 'P' : x === 'P' ? 'M' : x, y]);
    const opts = cand.filter((v, i, a) => a.findIndex(w => w[0] === v[0] && w[1] === v[1]) === i);
    while (opts.length < 3) { const y = 2 + kqRnd(7), x = IV_PERFECT[y] ? 'P' : kqPick(['M', 'm']); if (!opts.some(w => w[0] === x && w[1] === y)) opts.push([x, y]); }
    return { nn, kind: 'choice', cols: 2, prompt: [ivqAn(q, nn)[0].replace(/^a/, 'A') + ' turned upside down is…', ivqNm(q, nn)[1] + '를 뒤집으면…'], opts: shuffle(opts).map(([x, y]) => ({ id: x + y, label: () => kqT(ivqNm(x, y)) })), ans, ok: (v) => v === ans,
      yes: [ivqAn(qi, inv)[0].replace(/^a/, 'A') + ': ' + nn + ' + ' + inv + ' = 9, and ' + (q === 'P' ? 'perfect stays perfect.' : IVQ_QW[q][0] + ' turns ' + IVQ_QW[qi][0] + '.'), ivqNm(qi, inv)[1] + '예요. ' + nn + ' + ' + inv + ' = 9, ' + (q === 'P' ? '완전은 그대로 완전이에요.' : IVQ_QW[q][1] + '음정은 ' + IVQ_QW[qi][1] + '음정이 돼요.')],
      no: ['Two things change: the number (' + nn + ' + ' + inv + ' = 9) and the kind (' + (q === 'P' ? 'perfect stays perfect' : IVQ_QW[q][0] + ' becomes ' + IVQ_QW[qi][0]) + '): ' + ivqNm(qi, inv)[0] + '.', '두 가지가 바뀌어요. 숫자(' + nn + ' + ' + inv + ' = 9)와 종류(' + (q === 'P' ? '완전은 그대로' : IVQ_QW[q][1] + '은 ' + IVQ_QW[qi][1] + '으로') + ')예요. ' + ivqNm(qi, inv)[1] + '예요.'],
      fig: (c) => { const b = ivqWhitesUp(0, nn)[nn - 1]; return c.res ? ivqInvFig(0, b) : { kb: ivqLetters(0, b, 99, { ks: [0, 16] }) }; } }; },
};

// ── lesson 9: the tritone
const IVQ_TRI = [[5, 11, 'F', 'B', 4], [11, 17, 'B', 'F', 5], [0, 6, 'C', 'F♯', 4], [0, 6, 'C', 'G♭', 5], [4, 10, 'E', 'B♭', 5], [10, 16, 'B♭', 'E', 4], [7, 13, 'G', 'C♯', 4], [2, 8, 'D', 'A♭', 5]];
IVQ_SPEC['iv-tritone'] = {
  title: ['The tritone', '트라이톤'], allLine: ['Six half steps make a tritone: exactly half an octave. Its name depends on how it is written.', '반음 6개가 트라이톤이에요. 딱 옥타브의 절반이에요. 어떻게 쓰느냐에 따라 이름이 달라요.'],
  fig: () => ({ kb: { ...ivqHops(5, 11), ks: [0, 12] }, below: ivqCap(kqT(['F to B: 6 half steps', 'F에서 B: 반음 6개']), KQ.COD, true) }),
  steps: [
    { title: ['Six half steps', '반음 여섯 개'], line: ['Count the hops from F to B: 6. A perfect 4th is 5 and a perfect 5th is 7, so the tritone sits right between them.', 'F에서 B까지 뛰며 세어 보세요. 6개예요. 완전4도는 5개, 완전5도는 7개라서 트라이톤은 그 딱 가운데예요.'], fig: (c) => ({ kb: { ...ivqHops(5, 11, Math.min(c.tk + 1, 6)), ks: [0, 12] } }) },
    { title: ['Augmented 4th', '증4도'], line: ['F to B spans four letters, F G A B, so it is a 4th. It is one half step bigger than a perfect 4th: an augmented 4th.', 'F에서 B는 F G A B 네 글자라서 4도예요. 완전4도보다 반음 하나 커서 증4도예요.'], fig: () => ({ kb: ivqLetters(5, 11, 99, { ks: [0, 12] }), below: ivqCap(kqT(['F to B: an augmented 4th', 'F에서 B: 증4도']), KQ.COD, true) }) },
    { title: ['Diminished 5th', '감5도'], line: ['B up to F spans five letters, B C D E F, so it is a 5th. It is one half step smaller than a perfect 5th: a diminished 5th.', 'B에서 위의 F까지는 B C D E F 다섯 글자라서 5도예요. 완전5도보다 반음 하나 작아서 감5도예요.'], fig: () => ({ kb: ivqLetters(11, 17, 99, { ks: [5, 19] }), below: ivqCap(kqT(['B to F: a diminished 5th', 'B에서 F: 감5도']), KQ.COD, true) }) },
  ],
  make: (n, prev) => { if (n % 3 === 2) return { kind: 'choice', cols: 4, prompt: ['How many half steps make a tritone?', '트라이톤은 반음 몇 개일까요?'], opts: ['5', '6', '7', '12'].map(x => ({ id: x, label: x })), ans: '6', ok: (v) => v === '6',
      fig: (c) => ({ kb: c.res ? { ...ivqHops(5, 11), ks: [0, 12] } : ivqKb({ ks: [0, 12] }) }), yes: ['Six: exactly half of the 12 in an octave.', '6개예요. 옥타브 12개의 딱 절반이에요.'], no: ['Six: between the perfect 4th (5) and the perfect 5th (7).', '6개예요. 완전4도(5개)와 완전5도(7개) 사이예요.'] };
    let r, g = 0; do { r = kqPick(IVQ_TRI); } while (prev && prev.r === r && g++ < 8); const [a, b, A, B, nn] = r, ans = nn === 4 ? 'A4' : 'd5';
    const L = 'CDEFGAB', i0 = L.indexOf(A[0]), seq = Array.from({ length: nn }, (_, j) => L[(i0 + j) % 7]).join(' ');
    const accOf = (x) => x.includes('♯') ? 1 : x.includes('♭') ? -1 : 0, nA = { d: 28 + i0 + (a >= 12 ? 7 : 0), acc: accOf(A) }, nB = { d: 28 + i0 + (a >= 12 ? 7 : 0) + nn - 1, acc: accOf(B) };
    return { r, kind: 'choice', cols: 2, prompt: [A + ' up to ' + B + ' is a tritone. Augmented 4th or diminished 5th? Count the letters.', A + '에서 위의 ' + B + '까지는 트라이톤이에요. 증4도일까요, 감5도일까요? 글자를 세어 보세요.'], opts: [{ id: 'A4', label: () => kqT(ivqNm('A', 4)) }, { id: 'd5', label: () => kqT(ivqNm('d', 5)) }], ans, ok: (v) => v === ans, play: () => ivqPlay(a, b, 'both'),
      fig: (c) => ({ staff: c.res ? ivqStaffEl(nA, nB, { ladder: 'tr' + n, colors: [KQ.COD, KQ.COD], labels: [A, B] }) : null, kb: c.res ? { ...ivqHops(a, b), ks: [Math.min(a, 0), Math.max(b, 12)] } : ivqKb({ ks: [Math.min(a, 0), Math.max(b, 12)], marks: { [a]: 'pick', [b]: 'pick' } }) }),
      yes: [seq + ': ' + nn + ' letters, so ' + ivqAn(nn === 4 ? 'A' : 'd', nn)[0] + '.', seq + ', 글자 ' + nn + '개라서 ' + ivqNm(nn === 4 ? 'A' : 'd', nn)[1] + '예요.'], no: ['The letters decide the name: ' + seq + ', ' + nn + ' letters, so ' + ivqAn(nn === 4 ? 'A' : 'd', nn)[0] + '.', '이름은 글자가 정해요. ' + seq + ', 글자 ' + nn + '개라서 ' + ivqNm(nn === 4 ? 'A' : 'd', nn)[1] + '예요.'] }; },
};

const ivqRow = (id, en, ko, bEn, bKo) => [id, en, ko, bEn, bKo, () => <KqEngine spec={IVQ_SPEC[id]}/>];
const IVQ_ROWS = [
  ivqRow('iv-count', 'Count the letters', '글자를 세어요', 'The lower note is 1: count up to the higher note.', '아래 음이 1, 위 음까지 세기.'),
  ivqRow('iv-staff', 'Intervals on the staff', '오선 위의 음정', 'Every line and space counts. Odd stays, even swaps.', '줄과 칸을 모두 세기. 홀수는 그대로, 짝수는 바뀌어요.'),
  ivqRow('iv-half', 'Count the half steps', '반음을 세어요', 'Two 3rds, two sizes: major and minor.', '3도 두 개, 크기 두 가지: 장과 단.'),
  ivqRow('iv-tonic', 'Above the key note', '으뜸음 위의 음정', 'In a major scale: major or perfect.', '장음계에서는 장음정이나 완전음정.'),
  ivqRow('iv-minor', 'One half step smaller', '반음 하나 작게', 'Major one half step smaller is minor.', '장음정에서 반음 하나 작으면 단음정.'),
  ivqRow('iv-mh', 'Melodic and harmonic', '선율 음정과 화성 음정', 'One after the other, or together.', '하나씩 차례로, 또는 함께.'),
  ivqRow('iv-ear', 'Hear the size', '크기를 들어요', 'Major and minor 3rds, 4th, 5th and octave by ear.', '장3도와 단3도, 4도, 5도, 옥타브를 귀로.'),
  ivqRow('iv-invert', 'Turn it upside down', '음정 뒤집기', 'The numbers add up to 9; major becomes minor.', '숫자의 합은 9, 장은 단으로.'),
  ivqRow('iv-tritone', 'The tritone', '트라이톤', 'Six half steps: augmented 4th or diminished 5th.', '반음 여섯 개: 증4도 또는 감5도.'),
];
IVQ_ROWS.forEach(([id, en, ko, benEn, bko, Comp]) => {
  TOOLS.push({ id, ch: 'concept', title: en, blurb: benEn, hidden: true, get kicker() { return TOOL_AREAS.find(a => a.id === 'pitch').name + ' · ' + homeCatById('p-intervals').name; }, C: Comp });
  TOOL_KO[id] = [ko, bko];
  const tl = TOOLS[TOOLS.length - 1], k = TOOL_KO[id], ti = tl.title, bl = tl.blurb; tl.titleEn = ti; tl.blurbEn = bl;
  Object.defineProperty(tl, 'title', { get: () => (LANG === 'ko' ? k[0] : ti), enumerable: true, configurable: true });
  Object.defineProperty(tl, 'blurb', { get: () => (LANG === 'ko' ? k[1] : bl), enumerable: true, configurable: true });
  TOOL_CONCEPT[id] = 'p-intervals';
});
