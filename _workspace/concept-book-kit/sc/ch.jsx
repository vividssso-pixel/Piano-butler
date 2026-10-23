// ─── Chords, built in the Keys and staff style (her call 2026-10-23 19:48, after Intervals).
// Three groups: building a triad, major and minor, chords in a key. Every lesson: the whole picture, one at a time, her turn.
// Keyboard first; the staff on request (and its own lesson). Words as in the older Chords pads: 근음, 3음, 5음; 장3화음, 단3화음;
// 으뜸화음 I, 버금딸림화음 IV, 딸림화음 V; blocked = 함께, broken = 펼쳐서; 기본 위치, 제1전위, 제2전위.
const CHQ_W = [0, 2, 4, 5, 7, 9, 11];
const chqPlay = (keys, mode = 'both') => {   // keys (C4 = 0): broken, blocked, or broken then blocked
  if (mode !== 'block') keys.forEach((k, i) => setTimeout(() => playKey(k, 0.6), i * 340));
  if (mode !== 'arp') setTimeout(() => keys.forEach(k => playKey(k, 1.2)), mode === 'block' ? 0 : keys.length * 340 + 150);
};
const chqTri = (r, q = 'major') => [r, r + (q === 'minor' ? 3 : q === 'dim' ? 3 : 4), r + (q === 'dim' ? 6 : 7)];
const chqWhiteTri = (r) => { const w = ivqWhitesUp(r, 5); return [w[0], w[2], w[4]]; };   // skip a key, skip a key
const chqQOfWhite = (r) => { const t = chqWhiteTri(r), a = t[1] - t[0], b = t[2] - t[1]; return a === 4 && b === 3 ? 'major' : a === 3 && b === 4 ? 'minor' : 'dim'; };
const CHQ_PART = [['root', '근음'], ['3rd', '3음'], ['5th', '5음']];
const chqQW = (q) => q === 'minor' ? ['minor triad', '단3화음'] : q === 'dim' ? ['diminished triad', '감3화음'] : ['major triad', '장3화음'];
const chqNames = (rootNm, q) => chxSpell(rootNm, q === 'dim' ? 'minor' : q).map(prettyNote);
// a triad on the keyboard: its three keys solid, words above (root 3rd 5th, or anything else)
const chqKb = (keys, o = {}) => { const m = {}, names = {}, ncol = {}, words = o.words === undefined ? CHQ_PART.map(kqT) : o.words;
  keys.forEach((k, j) => { m[k] = o.style ? o.style(j) : 'pick'; if (words && words[j] != null) { names[k] = words[j]; ncol[k] = j === 0 ? KQ.COD : j === 1 ? KQ.BL : KQ.NV; } });
  return ivqKb({ ks: o.ks || [Math.min(keys[0], 12 * Math.floor(keys[0] / 12)), Math.max(keys[0] + 12, keys[2])], ...o, marks: { ...(o.base || {}), ...m, ...(o.marks || {}) }, names: { ...names, ...(o.names || {}) }, ncol: { ...ncol, ...(o.ncol || {}) } }); };
// half steps root to 3rd (1 2 3 4, coral) and 3rd to 5th (1 2 3, blue), one arrow per hop
const chqHops2 = (keys, upto = 99, o = {}) => { const [a, b, c] = keys, m = { [a]: 'pick' }, names = {}, ncol = {}, arcs = []; let n = 0;
  for (let k = a + 1; k <= b && n < upto; k++, n++) { arcs.push([k - 1, k, n === upto - 1, KQ.CO]); names[k] = String(k - a); ncol[k] = KQ.COD; m[k] = k === b ? 'pickB' : 'pass'; }
  for (let k = b + 1; k <= c && n < upto; k++, n++) { arcs.push([k - 1, k, n === upto - 1, KQ.BL]); names[k] = String(k - b); ncol[k] = KQ.BL; m[k] = k === c ? 'pick' : 'pass'; }
  return ivqKb({ ks: o.ks || [a, Math.max(a + 12, c)], marks: m, names, ncol, arcs, nonce: Math.min(n, upto) }); };
const chqStaff = (chords, o = {}) => <div style={{ maxWidth: o.mw || 300, margin: '0 auto' }}><ChxStaff clef={o.clef || 'treble'} places={chords} width={o.width || 200} o={{ x0: 54, sideSize: 13, ...(o.o || {}) }}/></div>;
const chqNotes = (rootL, q, clef = 'treble') => chxNotes(rootL, q === 'dim' ? 'minor' : q, clef);
const chqTxt = (keysNames) => keysNames.join(' ');
const CHQ_SPEC = {};

// ══ 1. Building a triad ══
CHQ_SPEC['ch-stack'] = {
  title: ['Root, 3rd, 5th', '근음, 3음, 5음'], allLine: ['A triad is three notes stacked: a root, the 3rd above it and the 5th above it. On the white keys: skip a key, skip a key. Tap a white key to build its triad.', '3화음은 음 세 개를 쌓은 거예요. 근음, 그 위의 3음, 그 위의 5음이에요. 흰건반에서는 하나 건너, 하나 건너. 흰건반을 눌러 3화음을 만들어 보세요.'],
  fig: (c) => { const r = typeof c.last === 'number' && ivqWhite(c.last) && c.last >= 0 && c.last <= 11 ? c.last : 0, T = chqWhiteTri(r), nm = T.map(ivqL);
    return { kb: { ...chqKb(T, { ks: [0, 16] }), onTap: (k) => { if (ivqWhite(k) && k <= 11) setTimeout(() => chqPlay(chqWhiteTri(k), 'block'), 250); } }, below: ivqCap(kqT([chqTxt(nm) + ': the triad on ' + nm[0], nm[0] + ' 위의 3화음: ' + chqTxt(nm)]), KQ.COD, true),
      staffAlt: chqStaff([{ notes: chqNotes(nm[0], chqQOfWhite(r)), side: CHQ_PART.map(kqT) }]) }; },
  steps: [
    { title: ['The root', '근음'], line: ['Every triad starts on one note, its root, and is named after it. This is the triad on C.', '3화음은 음 하나에서 시작해요. 그 음이 근음이고, 3화음의 이름도 근음에서 와요. 이건 C 위의 3화음이에요.'], fig: () => ({ kb: chqKb([0, 4, 7], { ks: [0, 12], words: [kqT(CHQ_PART[0]), null, null], marks: { 4: null, 7: null }, base: {} }) }) },
    { title: ['Add the 3rd', '3음 더하기'], line: ['Skip one white key: C, skip D, then E. E is the 3rd, a 3rd above the root.', '흰건반 하나를 건너요. C, D는 건너고, E. E가 3음이에요. 근음에서 3도 위예요.'], fig: () => ({ kb: chqKb([0, 4, 7], { ks: [0, 12], words: [kqT(CHQ_PART[0]), kqT(CHQ_PART[1]), null], marks: { 2: 'pass', 7: null } }) }) },
    { title: ['Add the 5th', '5음 더하기'], line: ['Skip one more: E, skip F, then G. G is the 5th, a 5th above the root. C E G is the triad.', '하나 더 건너요. E, F는 건너고, G. G가 5음이에요. 근음에서 5도 위예요. C E G가 3화음이에요.'], fig: () => ({ kb: chqKb([0, 4, 7], { ks: [0, 12], marks: { 2: 'pass', 5: 'pass' } }), mid: <div style={{ textAlign: 'center', margin: '0 0 6px' }}>{ivqPlayBtn(t('▶ Listen', '▶ 들어 보기'), () => chqPlay([0, 4, 7]))}</div> }) },
    { title: ['Any white key', '어느 흰건반에서나'], line: ['The same skips work from every white key: D F A, E G B, F A C, G B D, A C E, B D F.', '어느 흰건반에서 시작해도 똑같이 건너요. D F A, E G B, F A C, G B D, A C E, B D F.'],
      fig: (c) => { const r = CHQ_W[Math.floor(c.tk / 2) % 7], T = chqWhiteTri(r); return { kb: chqKb(T, { ks: [0, 16] }), below: ivqCap(T.map(ivqL).join(' '), KQ.COD, true) }; } },
  ],
  make: (n, prev) => { const kind = [0, 1, 2, 1][n % 4]; let r, g = 0; do { r = kqPick(CHQ_W); } while (prev && prev.r === r && g++ < 8);
    const T = chqWhiteTri(r), L = ivqL(r), nm = T.map(ivqL), Li = 'CDEFGAB'.indexOf(L), row = (st) => st.map(s => 'CDEFGAB'[(Li + s) % 7]).join(' ');
    if (kind === 0) { const ans = row([0, 2, 4]), opts = shuffle([ans, row([0, 1, 2]), row([0, 2, 3]), row([0, 3, 5])]);
      return { r, kind: 'choice', cols: 2, prompt: ['Which three notes make the triad on ' + L + '?', L + ' 위의 3화음을 이루는 세 음은?'], opts: opts.map(x => ({ id: x, label: x })), ans, ok: (v) => v === ans,
        fig: (c) => ({ kb: c.res ? chqKb(T, { ks: [r, r + 12] }) : ivqKb({ ks: [r, r + 12], marks: { [r]: 'pick' } }) }), play: undefined,
        yes: [ans + ': skip a key, skip a key.', ans + ': 하나 건너, 하나 건너.'], no: ['From ' + L + ', skip a key, skip a key: ' + ans + '.', L + '에서 하나 건너, 하나 건너: ' + ans + '.'] }; }
    if (kind === 1) return { r, kind: 'multi', retry: true, targets: T, prompt: ['Tap the three notes of the triad on ' + L + '.', L + ' 위의 3화음의 세 음을 눌러 보세요.'], prog: (a, b) => ['Found ' + a + ' of ' + b + '. Keep going.', b + '개 중 ' + a + '개를 찾았어요. 계속해요.'],
      fig: () => ({ kb: ivqKb({ ks: [r, r + 12] }) }), yes: [nm.join(' ') + ': the triad on ' + L + '.', L + ' 위의 3화음: ' + nm.join(' ') + '.'],
      no: (k) => [(ivqWhite(k) ? 'That is ' + ivqL(k) + '. ' : 'Only white keys here. ') + 'The triad on ' + L + ' is ' + nm.join(' ') + ': skip a key, skip a key.', (ivqWhite(k) ? '그건 ' + ivqL(k) + ' 건반이에요. ' : '여기서는 흰건반만 써요. ') + L + ' 위의 3화음은 ' + ivqJ(nm.join(' '), '이에요', '예요') + '. 하나 건너, 하나 건너.'] };
    const opts = shuffle(nm.slice());
    return { r, kind: 'choice', cols: 3, prompt: ['These three keys make a triad. Which one is the root?', '이 세 건반은 3화음이에요. 근음은 어느 것일까요?'], opts: opts.map(x => ({ id: x, label: x })), ans: L, ok: (v) => v === L, play: () => chqPlay(T, 'block'),
      fig: (c) => ({ kb: c.res ? chqKb(T, { ks: [r, r + 12] }) : chqKb(T, { ks: [r, r + 12], words: null }) }),
      yes: [L + ': the 3rd and the 5th stack above it.', L + '예요. 그 위에 3음과 5음이 쌓여요.'], no: ['Stacked in skips, the lowest note is the root: ' + L + '.', '하나씩 건너 쌓으면 맨 아래 음이 근음이에요. ' + L + '예요.'] }; },
};

// ── on the staff: lines with lines, spaces with spaces
const CHQ_TREB = { E: 30, F: 31, G: 32, A: 33, B: 34, C: 28, D: 29 }, CHQ_BASS = { G: 18, A: 19, B: 20, C: 21, D: 22, E: 23, F: 24 };
const chqTriD = (d0) => [d0, d0 + 2, d0 + 4].map(d => IVX_N(d, 0));
CHQ_SPEC['ch-staff'] = {
  title: ['Triads on the staff', '오선 위의 3화음'], allLine: ['On the staff a triad is three notes stacked one above the other, all on lines or all in spaces.', '오선에서 3화음은 세 음을 위아래로 쌓은 모양이에요. 모두 줄 위에, 또는 모두 칸 안에 있어요.'],
  fig: () => ({ staff: chqStaff([{ notes: chqTriD(30), lab: 'E G B', lab2: t('lines', '줄') }, { notes: chqTriD(31), lab: 'F A C', lab2: t('spaces', '칸') }], { width: 240, mw: 340 }) }),
  steps: [
    { title: ['All on lines', '모두 줄 위에'], line: ['E G B: line 1, line 2, line 3. Each note is a 3rd above the one below.', 'E G B: 1번 줄, 2번 줄, 3번 줄. 음마다 아래 음보다 3도 위예요.'], fig: () => ({ staff: chqStaff([{ notes: chqTriD(30), side: ['E', 'G', 'B'] }]), kb: chqKb([4, 7, 11], { ks: [0, 12], words: ['E', 'G', 'B'] }) }) },
    { title: ['All in spaces', '모두 칸 안에'], line: ['F A C: space 1, space 2, space 3.', 'F A C: 1번 칸, 2번 칸, 3번 칸.'], fig: () => ({ staff: chqStaff([{ notes: chqTriD(31), side: ['F', 'A', 'C'] }]), kb: chqKb([5, 9, 12], { ks: [0, 12], words: ['F', 'A', 'C'] }) }) },
    { title: ['The root is at the bottom', '근음은 맨 아래'], line: ['Stacked like this, the lowest note is the root, and it names the triad: G B D is the triad on G.', '이렇게 쌓으면 맨 아래 음이 근음이고, 그 음이 3화음의 이름이 돼요. G B D는 G 위의 3화음이에요.'], fig: () => ({ staff: chqStaff([{ notes: chqTriD(32), side: CHQ_PART.map(kqT), hl: [0] }]), kb: chqKb([7, 11, 14], { ks: [0, 16] }) }) },
    { title: ['On the bass staff', '낮은음자리표 오선에서'], line: ['The bass staff works the same way. G B D sits on its bottom three lines.', '낮은음자리표 오선도 똑같아요. G B D는 아래 세 줄에 앉아요.'], fig: () => ({ staff: chqStaff([{ notes: chqTriD(18), side: ['G', 'B', 'D'] }], { clef: 'bass' }) }) },
  ],
  make: (n, prev) => { const clef = n % 3 === 2 ? 'bass' : 'treble', MAP = clef === 'bass' ? CHQ_BASS : CHQ_TREB; let L, g = 0; do { L = kqPick('CDEFGAB'.split('')); } while (prev && prev.L === L && g++ < 8);
    const d0 = MAP[L], nt = chqTriD(d0), Li = 'CDEFGAB'.indexOf(L), nm = [0, 2, 4].map(s => 'CDEFGAB'[(Li + s) % 7]), onLine = (d0 - (clef === 'bass' ? 18 : 30)) % 2 === 0;
    if (n % 2 === 0) { const opts = shuffle([L, ...shuffle('CDEFGAB'.split('').filter(x => x !== L && x !== nm[1] && x !== nm[2])).slice(0, 2), nm[1]]);
      return { L, kind: 'choice', cols: 4, prompt: clef === 'bass' ? ['Bass staff: which triad is this? Name its root.', '낮은음자리표 오선: 어떤 3화음일까요? 근음을 골라요.'] : ['Which triad is this? Name its root.', '어떤 3화음일까요? 근음을 골라요.'], opts: opts.map(x => ({ id: x, label: x })), ans: L, ok: (v) => v === L,
        fig: (c) => ({ staff: chqStaff([{ notes: nt, side: c.res ? nm : null, hl: c.res ? [0] : [] }], { clef }) }),
        yes: ['The triad on ' + L + ': ' + nm.join(' ') + ', all ' + (onLine ? 'on lines.' : 'in spaces.'), L + ' 위의 3화음: ' + nm.join(' ') + ', 모두 ' + (onLine ? '줄 위에 있어요.' : '칸 안에 있어요.')], no: ['The lowest note is the root: ' + L + '. The triad is ' + nm.join(' ') + '.', '맨 아래 음이 근음이에요. ' + L + '예요. 3화음은 ' + ivqJ(nm.join(' '), '이에요', '예요') + '.'] }; }
    const ans = nm.join(' '), wrong = [[0, 1, 2], [0, 2, 3], [1, 3, 5]].map(st => st.map(s => 'CDEFGAB'[(Li + s) % 7]).join(' ')), opts = shuffle([ans, ...wrong]);
    return { L, kind: 'choice', cols: 2, prompt: clef === 'bass' ? ['Bass staff: name the three notes, from the bottom.', '낮은음자리표 오선: 아래에서부터 세 음의 이름은?'] : ['Name the three notes, from the bottom.', '아래에서부터 세 음의 이름은?'], opts: opts.map(x => ({ id: x, label: x })), ans, ok: (v) => v === ans,
      fig: (c) => ({ staff: chqStaff([{ notes: nt, side: c.res ? nm : null }], { clef }) }),
      yes: [ans + ': skip a letter, skip a letter.', ans + ': 한 글자 건너, 한 글자 건너.'], no: ['Read the bottom note, then skip a letter twice: ' + ans + '.', '맨 아래 음을 읽고 한 글자씩 두 번 건너요. ' + ivqJ(ans, '이에요', '예요') + '.'] }; },
};

// ── blocked and broken, and the fingers
const chqHandKb = (hand, upto = 3) => { const F = hand === 'R' ? ['1', '3', '5'] : ['5', '3', '1'], T = [0, 4, 7];
  return chqKb(T.slice(0, upto), { ks: [0, 12], words: F.slice(0, upto) }); };
CHQ_SPEC['ch-hands'] = {
  title: ['Playing a triad', '3화음 치기'], allLine: ['A triad can be played blocked, all three notes together, or broken, one note after the other.', '3화음은 세 음을 함께 칠 수도 있고, 한 음씩 펼쳐서 칠 수도 있어요.'],
  fig: () => ({ top: <div style={{ display: 'flex', gap: 10, justifyContent: 'center', flexWrap: 'wrap' }}>
    {[false, true].map(br => <div key={String(br)} style={{ flex: '1 1 150px', maxWidth: 240, textAlign: 'center' }}>{chqStaff([{ notes: chqTriD(28), broken: br }], { width: 170, mw: 240 })}{ivqCap(br ? t('Broken', '펼쳐서') : t('Blocked', '함께'), KQ.COD)}{ivqPlayBtn(t('▶ Listen', '▶ 들어 보기'), () => chqPlay([0, 4, 7], br ? 'arp' : 'block'))}</div>)}</div> }),
  steps: [
    { title: ['Blocked', '함께'], line: ['All three notes at the same time, written one above the other.', '세 음을 동시에 쳐요. 악보에는 위아래로 겹쳐 써요.'], fig: () => ({ staff: chqStaff([{ notes: chqTriD(28) }]), mid: <div style={{ textAlign: 'center', margin: '4px 0 6px' }}>{ivqPlayBtn(t('▶ Listen', '▶ 들어 보기'), () => chqPlay([0, 4, 7], 'block'))}</div>, kb: chqKb([0, 4, 7], { ks: [0, 12] }) }) },
    { title: ['Broken', '펼쳐서'], line: ['One note after the other, from the root up, written side by side.', '근음부터 한 음씩 차례로 쳐요. 악보에는 나란히 써요.'], fig: () => ({ staff: chqStaff([{ notes: chqTriD(28), broken: true }]), mid: <div style={{ textAlign: 'center', margin: '4px 0 6px' }}>{ivqPlayBtn(t('▶ Listen', '▶ 들어 보기'), () => chqPlay([0, 4, 7], 'arp'))}</div>, kb: chqKb([0, 4, 7], { ks: [0, 12] }) }) },
    { title: ['Right hand: 1 3 5', '오른손: 1 3 5'], line: ['In the right hand, the thumb plays the root, finger 3 the 3rd and finger 5 the 5th.', '오른손은 엄지(1번)가 근음, 3번 손가락이 3음, 5번 손가락이 5음을 쳐요.'], fig: (c) => ({ kb: chqHandKb('R', Math.min(c.tk + 1, 3)) }) },
    { title: ['Left hand: 5 3 1', '왼손: 5 3 1'], line: ['The left hand turns it round: finger 5 on the root, 3 on the 3rd, the thumb on the 5th.', '왼손은 반대예요. 5번 손가락이 근음, 3번이 3음, 엄지(1번)가 5음이에요.'], fig: (c) => ({ kb: chqHandKb('L', Math.min(c.tk + 1, 3)) }) },
  ],
  make: (n, prev) => { const kind = n % 3, r = kqPick([0, 5, 7]), T = chqWhiteTri(r), L = ivqL(r);
    if (kind === 0) { const br = Math.random() < 0.5, ans = br ? 'br' : 'bl';
      return { kind: 'choice', cols: 2, prompt: ['Listen: blocked or broken?', '들어 보세요. 함께일까요, 펼쳐서일까요?'], opts: [{ id: 'bl', label: () => t('Blocked', '함께') }, { id: 'br', label: () => t('Broken', '펼쳐서') }], ans, ok: (v) => v === ans, play: () => chqPlay(T, br ? 'arp' : 'block'),
        fig: (c) => ({ staff: c.res ? chqStaff([{ notes: chqNotes(L, chqQOfWhite(r)), broken: br }]) : null, kb: chqKb(T, { ks: [r, r + 12], words: c.res ? undefined : null, marks: c.res ? {} : { [T[0]]: null, [T[1]]: null, [T[2]]: null } }) }),
        yes: [br ? 'Broken: one note after the other.' : 'Blocked: all three together.', br ? '펼쳐서예요. 한 음씩 차례로.' : '함께예요. 세 음을 동시에.'], no: [br ? 'The notes came one after the other: broken. Press ♪ Again.' : 'All three sounded at once: blocked. Press ♪ Again.', br ? '음이 하나씩 차례로 났어요. 펼쳐서예요. ♪ 다시를 눌러 보세요.' : '세 음이 한꺼번에 울렸어요. 함께예요. ♪ 다시를 눌러 보세요.'] }; }
    if (kind === 1) { const br = Math.random() < 0.5, ans = br ? 'br' : 'bl';
      return { kind: 'choice', cols: 2, prompt: ['Blocked or broken?', '함께일까요, 펼쳐서일까요?'], opts: [{ id: 'bl', label: () => t('Blocked', '함께') }, { id: 'br', label: () => t('Broken', '펼쳐서') }], ans, ok: (v) => v === ans, onPick: () => chqPlay(T, br ? 'arp' : 'block'),
        fig: () => ({ staff: chqStaff([{ notes: chqNotes(L, chqQOfWhite(r)), broken: br }]) }),
        yes: [br ? 'Side by side: broken.' : 'One above the other: blocked.', br ? '나란히 있어요. 펼쳐서예요.' : '위아래로 겹쳐 있어요. 함께예요.'], no: [br ? 'The notes stand side by side: broken.' : 'The notes are stacked: blocked.', br ? '음표가 나란히 서 있어요. 펼쳐서예요.' : '음표가 위아래로 겹쳐 있어요. 함께예요.'] }; }
    const hand = Math.random() < 0.5 ? 'R' : 'L', part = kqRnd(3), fing = (hand === 'R' ? ['1', '3', '5'] : ['5', '3', '1'])[part], hw = hand === 'R' ? ['right', '오른손'] : ['left', '왼손'];
    return { kind: 'choice', cols: 3, prompt: ['Playing a triad with the ' + hw[0] + ' hand, which finger plays the ' + CHQ_PART[part][0] + '?', hw[1] + '으로 3화음을 칠 때 ' + CHQ_PART[part][1] + '은 몇 번 손가락일까요?'], opts: ['1', '3', '5'].map(x => ({ id: x, label: x })), ans: fing, ok: (v) => v === fing,
      fig: (c) => ({ kb: c.res ? chqHandKb(hand) : chqKb(T.map(k => k - r), { ks: [0, 12], words: CHQ_PART.map((p, j) => j === part ? kqT(p) : null) }) }),
      yes: [hw[0][0].toUpperCase() + hw[0].slice(1) + ' hand: ' + (hand === 'R' ? '1 3 5' : '5 3 1') + ', from the root up.', hw[1] + ': 근음부터 ' + (hand === 'R' ? '1 3 5' : '5 3 1') + '번이에요.'], no: ['The ' + hw[0] + ' hand plays ' + (hand === 'R' ? '1 3 5' : '5 3 1') + ' from the root up: the ' + CHQ_PART[part][0] + ' gets finger ' + fing + '.', hw[1] + '은 근음부터 ' + (hand === 'R' ? '1 3 5' : '5 3 1') + '번이에요. ' + CHQ_PART[part][1] + '은 ' + fing + '번 손가락이에요.'] }; },
};

// ══ 2. Kinds of chords: count the keys between (her method: 'how many keys sit between', not hop by hop) ══
const CHQ_BCOL = [KQ.COD, KQ.BL, KQ.NV];
// a chord with a bracket over the keys between each pair of notes and the count on it; upto = how many brackets so far
const chqBetween = (keys, o = {}) => { const m = {}, spans = [], n = o.upto == null ? 99 : o.upto;
  keys.forEach((k, j) => { m[k] = j === 1 ? 'pickB' : 'pick'; if (j && j <= n) { for (let x = keys[j - 1] + 1; x < k; x++) m[x] = 'pass'; spans.push([keys[j - 1] + 1, k - 1, String(k - keys[j - 1] - 1), CHQ_BCOL[(j - 1) % 3]]); } });
  return ivqKb({ ks: o.ks || [keys[0], Math.max(keys[0] + 12, keys[keys.length - 1])], marks: m, spans }); };
const chqSpell = (rootName, semis) => { const L0 = 'CDEFGAB'.indexOf(rootName[0]), acc = /[♯#]/.test(rootName.slice(1)) ? 1 : /[♭b]/.test(rootName.slice(1)) ? -1 : 0, pc0 = (KQ_PC[rootName[0]] + acc + 12) % 12;
  return semis.map((x, j) => { const l = 'CDEFGAB'[(L0 + 2 * j) % 7], want = (pc0 + x) % 12, a = ((want - KQ_PC[l] + 18) % 12) - 6; return l + (a === 1 ? '♯' : a === -1 ? '♭' : a === 2 ? '𝄪' : a === -2 ? '𝄫' : ''); }); };
const CHQ_KIND = { major: { s: [0, 4, 7], w: ['major triad', '장3화음'], b: '3 + 2' }, minor: { s: [0, 3, 7], w: ['minor triad', '단3화음'], b: '2 + 3' }, dim: { s: [0, 3, 6], w: ['diminished triad', '감3화음'], b: '2 + 2' }, aug: { s: [0, 4, 8], w: ['augmented triad', '증3화음'], b: '3 + 3' } };
const chqK = (rn, r, q) => { const K = CHQ_KIND[q]; return { keys: K.s.map(x => r + x), names: chqSpell(rn, K.s), w: K.w, b: K.b, q }; };
const chqKcap = (rn, r, q, big) => { const c = chqK(rn, r, q); return ivqCap(kqT([prettyNote(rn) + ' ' + c.w[0] + ': ' + c.names.join(' ') + ', ' + c.b, prettyNote(rn) + ' ' + c.w[1] + ': ' + c.names.join(' ') + ', ' + c.b]), q === 'minor' ? KQ.BL : q === 'major' ? KQ.COD : KQ.NV, big); };
const chqPlayBtn = (keys) => <div style={{ textAlign: 'center', margin: '0 0 6px' }}>{ivqPlayBtn(t('▶ Listen', '▶ 들어 보기'), () => chqPlay(keys))}</div>;
const CHQ_MM = [['C', 0, 'major'], ['D', 2, 'major'], ['E', 4, 'major'], ['F', 5, 'major'], ['G', 7, 'major'], ['A', 9, 'major'], ['B♭', 10, 'major'], ['E♭', 3, 'major'], ['C', 0, 'minor'], ['D', 2, 'minor'], ['E', 4, 'minor'], ['F', 5, 'minor'], ['G', 7, 'minor'], ['A', 9, 'minor'], ['B', 11, 'minor']];
CHQ_SPEC['ch-mm'] = {
  title: ['Major or minor', '장3화음? 단3화음?'], allLine: ['Count the keys between the notes. Major: 3 between, then 2. Minor: 2 between, then 3. Only the 3rd moves.', '음과 음 사이의 건반을 세어요. 장3화음은 3개 그다음 2개, 단3화음은 2개 그다음 3개예요. 3음만 움직여요.'],
  fig: () => ({ top: <>{ivqKbEl(chqBetween(chqK('C', 0, 'major').keys))}{chqKcap('C', 0, 'major')}</>, kb: chqBetween(chqK('C', 0, 'minor').keys), below: chqKcap('C', 0, 'minor') }),
  steps: [
    { title: ['Major: 3 and 2', '장3화음: 3과 2'], line: ['C to E: 3 keys between. E to G: 2 keys between. That is a major triad.', 'C와 E 사이에 건반 3개, E와 G 사이에 2개. 장3화음이에요.'], fig: (c) => ({ kb: chqBetween(chqK('C', 0, 'major').keys, { upto: Math.min(1 + Math.floor(c.tk / 2), 2) }), mid: chqPlayBtn([0, 4, 7]) }) },
    { title: ['Minor: 2 and 3', '단3화음: 2와 3'], line: ['Bring the 3rd down one key, E to E♭: now 2 between, then 3. That is a minor triad. The root and the 5th stay.', '3음을 건반 하나 내려 E를 E♭으로 바꿔요. 이제 2개, 그다음 3개. 단3화음이에요. 근음과 5음은 그대로예요.'], fig: (c) => ({ kb: chqBetween(chqK('C', 0, 'minor').keys, { upto: Math.min(1 + Math.floor(c.tk / 2), 2) }), mid: chqPlayBtn([0, 3, 7]) }) },
    { title: ['On the white keys', '흰건반에서'], line: ['With white keys only, the triads on C, F and G are major and those on D, E and A are minor. B D F has 2 and 2: that is the next lesson.', '흰건반만 쓰면 C, F, G 위의 3화음은 장3화음, D, E, A 위는 단3화음이에요. B D F는 2와 2예요. 다음 레슨에서 배워요.'],
      fig: (c) => { const r = CHQ_W[Math.floor(c.tk / 2) % 7], T = chqWhiteTri(r), q = chqQOfWhite(r), nm = T.map(ivqL).join(' ');
        return { kb: chqBetween(T, { ks: [0, 19] }), below: ivqCap(kqT(q === 'dim' ? [nm + ': 2 + 2, not major or minor', nm + ': 2 + 2, 장도 단도 아니에요'] : [nm + ': ' + CHQ_KIND[q].b + ', ' + CHQ_KIND[q].w[0], nm + ': ' + CHQ_KIND[q].b + ', ' + CHQ_KIND[q].w[1]]), q === 'major' ? KQ.COD : q === 'minor' ? KQ.BL : KQ.NV, true) }; } },
  ],
  make: (n, prev) => { const kind = [0, 1, 0, 2][n % 4];
    if (kind === 0) { let e, g = 0; do { e = kqPick(CHQ_MM); } while (prev && prev.e === e && g++ < 8); const [rn, r, q] = e, C = chqK(rn, r, q), nm = C.names.join(' ');
      return { e, kind: 'choice', cols: 2, prompt: ['Major or minor? Count the keys between.', '장3화음일까요, 단3화음일까요? 사이 건반을 세어 보세요.'], opts: ['major', 'minor'].map(x => ({ id: x, label: () => kqT(CHQ_KIND[x].w) })), ans: q, ok: (v) => v === q, play: () => chqPlay(C.keys),
        fig: (c) => ({ kb: c.res ? chqBetween(C.keys, { ks: [r, r + 12] }) : chqKb(C.keys, { ks: [r, r + 12], words: null }) }),
        yes: [nm + ': ' + C.b + ', ' + C.w[0] + '.', nm + ': ' + C.b + ', ' + ivqJ(C.w[1], '이에요', '예요') + '.'], no: [nm + ' has ' + C.b + ' keys between: ' + C.w[0] + '. Major is 3 + 2, minor 2 + 3.', nm + ': 사이 건반 ' + C.b + ', ' + ivqJ(C.w[1], '이에요', '예요') + '. 장은 3 + 2, 단은 2 + 3이에요.'] }; }
    if (kind === 1) { const toMin = Math.random() < 0.55, r = toMin ? kqPick([0, 5, 7]) : kqPick([2, 4, 9]), q0 = toMin ? 'major' : 'minor', q1 = toMin ? 'minor' : 'major', L = ivqL(r), C0 = chqK(L, r, q0), C1 = chqK(L, r, q1), tgt = C1.keys[1];
      return { kind: 'key', retry: true, prompt: toMin ? ['This is ' + L + ' major. Make it minor: tap the new 3rd.', '이건 ' + L + ' 장3화음이에요. 단3화음으로 바꿔요. 새 3음을 눌러 보세요.'] : ['This is ' + L + ' minor. Make it major: tap the new 3rd.', '이건 ' + L + ' 단3화음이에요. 장3화음으로 바꿔요. 새 3음을 눌러 보세요.'], play: () => chqPlay(C0.keys, 'block'),
        fig: (c) => ({ kb: c.res === 'ok' ? chqBetween(C1.keys, { ks: [r, r + 12] }) : chqKb(C0.keys, { ks: [r, r + 12] }) }), ok: (k) => k === tgt, onPick: (k, ok) => { if (ok) setTimeout(() => chqPlay(C1.keys, 'block'), 300); },
        yes: [toMin ? 'The 3rd one key down: 2 + 3, minor.' : 'The 3rd one key up: 3 + 2, major.', toMin ? '3음을 건반 하나 내렸어요. 2 + 3, 단3화음이에요.' : '3음을 건반 하나 올렸어요. 3 + 2, 장3화음이에요.'],
        no: (k) => k === C0.keys[1] ? ['That is the 3rd it has now. Move it one key ' + (toMin ? 'down, to the left.' : 'up, to the right.'), '그건 지금의 3음이에요. 건반 하나 ' + (toMin ? '아래, 왼쪽으로 옮겨요.' : '위, 오른쪽으로 옮겨요.')] : ['Only the 3rd moves, by one key ' + (toMin ? 'down: the key just left of it.' : 'up: the key just right of it.'), '3음만 건반 하나 ' + (toMin ? '내려요. 바로 왼쪽 건반이에요.' : '올려요. 바로 오른쪽 건반이에요.')] }; }
    const q = Math.random() < 0.5 ? 'major' : 'minor', low = Math.random() < 0.5, ans = String(low ? (q === 'major' ? 3 : 2) : (q === 'major' ? 2 : 3)), C = chqK('C', 0, q);
    return { kind: 'choice', cols: 4, prompt: low ? ['In a ' + C.w[0] + ', how many keys sit between the root and the 3rd?', C.w[1] + '에서 근음과 3음 사이에 건반이 몇 개일까요?'] : ['In a ' + C.w[0] + ', how many keys sit between the 3rd and the 5th?', C.w[1] + '에서 3음과 5음 사이에 건반이 몇 개일까요?'], opts: ['1', '2', '3', '4'].map(x => ({ id: x, label: x })), ans, ok: (v) => v === ans,
      fig: (c) => ({ kb: c.res ? chqBetween(C.keys) : chqKb(C.keys, { ks: [0, 12] }) }),
      yes: [q === 'major' ? 'Major: 3, then 2.' : 'Minor: 2, then 3.', q === 'major' ? '장3화음: 3개, 그다음 2개.' : '단3화음: 2개, 그다음 3개.'], no: [q === 'major' ? 'Major is 3 then 2: ' + ans + ' here.' : 'Minor is 2 then 3: ' + ans + ' here.', q === 'major' ? '장3화음은 3개 그다음 2개예요. 여기는 ' + ans + '개예요.' : '단3화음은 2개 그다음 3개예요. 여기는 ' + ans + '개예요.'] }; },
};

// ── diminished and augmented
const CHQ_ALL4 = [['C', 0, 'major'], ['F', 5, 'major'], ['G', 7, 'major'], ['D', 2, 'minor'], ['A', 9, 'minor'], ['E', 4, 'minor'], ['B', 11, 'dim'], ['E', 4, 'dim'], ['D', 2, 'dim'], ['A', 9, 'dim'], ['C', 0, 'aug'], ['F', 5, 'aug'], ['G', 7, 'aug'], ['D', 2, 'aug']];
CHQ_SPEC['ch-da'] = {
  title: ['Diminished and augmented', '감3화음과 증3화음'], allLine: ['Two more kinds. Diminished: 2 keys between, then 2. Augmented: 3 between, then 3.', '두 가지가 더 있어요. 감3화음은 사이 건반 2개 그다음 2개, 증3화음은 3개 그다음 3개예요.'],
  fig: () => ({ top: <>{ivqKbEl(chqBetween(chqK('B', 11, 'dim').keys, { ks: [7, 19] }))}{chqKcap('B', 11, 'dim')}</>, kb: chqBetween(chqK('C', 0, 'aug').keys), below: chqKcap('C', 0, 'aug') }),
  steps: [
    { title: ['Diminished: 2 and 2', '감3화음: 2와 2'], line: ['B D F, on the white keys: 2 keys between, then 2 again. Both 3rds are minor, so the 5th is one key closer.', 'B D F, 흰건반이에요. 사이에 건반 2개, 그리고 또 2개. 3도가 둘 다 단3도라서 5음이 건반 하나만큼 가까워요.'], fig: () => ({ kb: chqBetween(chqK('B', 11, 'dim').keys, { ks: [7, 19] }), mid: chqPlayBtn([11, 14, 17]) }) },
    { title: ['From minor to diminished', '단3화음에서 감3화음으로'], line: ['Take C minor, C E♭ G, and bring the 5th down one key: C E♭ G♭ is C diminished.', 'C 단3화음 C E♭ G에서 5음을 건반 하나 내리면 C E♭ G♭, C 감3화음이에요.'], fig: (c) => ({ kb: chqBetween(chqK('C', 0, c.tk % 4 < 2 ? 'minor' : 'dim').keys), below: chqKcap('C', 0, c.tk % 4 < 2 ? 'minor' : 'dim', true), mid: chqPlayBtn([0, 3, 6]) }) },
    { title: ['Augmented: 3 and 3', '증3화음: 3과 3'], line: ['Take C major, C E G, and raise the 5th one key: C E G♯. 3 keys between, then 3 again.', 'C 장3화음 C E G에서 5음을 건반 하나 올리면 C E G♯. 사이에 3개, 그리고 또 3개예요.'], fig: (c) => ({ kb: chqBetween(chqK('C', 0, c.tk % 4 < 2 ? 'major' : 'aug').keys), below: chqKcap('C', 0, c.tk % 4 < 2 ? 'major' : 'aug', true), mid: chqPlayBtn([0, 4, 8]) }) },
    { title: ['All four', '네 가지 모두'], line: ['Major 3 + 2, minor 2 + 3, diminished 2 + 2, augmented 3 + 3.', '장 3 + 2, 단 2 + 3, 감 2 + 2, 증 3 + 3.'], fig: (c) => { const q = ['major', 'minor', 'dim', 'aug'][Math.floor(c.tk / 2) % 4]; return { kb: chqBetween(chqK('C', 0, q).keys), below: chqKcap('C', 0, q, true) }; } },
  ],
  make: (n, prev) => { const kind = [0, 1, 0, 2][n % 4];
    if (kind === 0) { let e, g = 0; do { e = kqPick(CHQ_ALL4); } while (prev && prev.e === e && g++ < 8); const [rn, r, q] = e, C = chqK(rn, r, q), nm = C.names.join(' ');
      return { e, kind: 'choice', cols: 2, prompt: ['Which kind of triad? Count the keys between.', '어떤 3화음일까요? 사이 건반을 세어 보세요.'], opts: ['major', 'minor', 'dim', 'aug'].map(x => ({ id: x, label: () => kqT(CHQ_KIND[x].w) })), ans: q, ok: (v) => v === q, play: () => chqPlay(C.keys),
        fig: (c) => ({ kb: c.res ? chqBetween(C.keys, { ks: [r, r + 12] }) : chqKb(C.keys, { ks: [r, r + 12], words: null }) }),
        yes: [nm + ': ' + C.b + ', ' + C.w[0] + '.', nm + ': ' + C.b + ', ' + ivqJ(C.w[1], '이에요', '예요') + '.'], no: [nm + ' has ' + C.b + ' keys between: ' + C.w[0] + '.', nm + ': 사이 건반 ' + C.b + ', ' + ivqJ(C.w[1], '이에요', '예요') + '.'] }; }
    if (kind === 1) { const toDim = Math.random() < 0.5, [L, r] = kqPick([['C', 0], ['D', 2], ['F', 5], ['G', 7]]), q0 = toDim ? 'minor' : 'major', q1 = toDim ? 'dim' : 'aug', C0 = chqK(L, r, q0), C1 = chqK(L, r, q1), tgt = C1.keys[2];
      return { kind: 'key', retry: true, prompt: toDim ? ['This is ' + L + ' minor. Make it diminished: tap the new 5th.', '이건 ' + L + ' 단3화음이에요. 감3화음으로 바꿔요. 새 5음을 눌러 보세요.'] : ['This is ' + L + ' major. Make it augmented: tap the new 5th.', '이건 ' + L + ' 장3화음이에요. 증3화음으로 바꿔요. 새 5음을 눌러 보세요.'], play: () => chqPlay(C0.keys, 'block'),
        fig: (c) => ({ kb: c.res === 'ok' ? chqBetween(C1.keys, { ks: [r, r + 12] }) : chqKb(C0.keys, { ks: [r, r + 12] }) }), ok: (k) => k === tgt, onPick: (k, ok) => { if (ok) setTimeout(() => chqPlay(C1.keys, 'block'), 300); },
        yes: [toDim ? 'The 5th one key down: 2 + 2, diminished.' : 'The 5th one key up: 3 + 3, augmented.', toDim ? '5음을 건반 하나 내렸어요. 2 + 2, 감3화음이에요.' : '5음을 건반 하나 올렸어요. 3 + 3, 증3화음이에요.'],
        no: (k) => k === C0.keys[2] ? ['That is the 5th it has now. Move it one key ' + (toDim ? 'down.' : 'up.'), '그건 지금의 5음이에요. 건반 하나 ' + (toDim ? '내려요.' : '올려요.')] : ['Only the 5th moves, one key ' + (toDim ? 'down: just left of it.' : 'up: just right of it.'), '5음만 건반 하나 ' + (toDim ? '내려요. 바로 왼쪽이에요.' : '올려요. 바로 오른쪽이에요.')] }; }
    const q = kqPick(['dim', 'aug']), ans = q === 'dim' ? '2 + 2' : '3 + 3';
    return { kind: 'choice', cols: 2, prompt: ['How many keys sit between the notes of ' + (q === 'aug' ? 'an ' : 'a ') + CHQ_KIND[q].w[0] + '?', CHQ_KIND[q].w[1] + '의 음 사이에는 건반이 몇 개씩 있을까요?'], opts: ['3 + 2', '2 + 3', '2 + 2', '3 + 3'].map(x => ({ id: x, label: x })), ans, ok: (v) => v === ans,
      fig: (c) => ({ kb: c.res ? chqBetween(chqK('C', 0, q).keys) : ivqKb({ ks: [0, 12], marks: { 0: 'pick' } }) }),
      yes: [CHQ_KIND[q].w[0][0].toUpperCase() + CHQ_KIND[q].w[0].slice(1) + ': ' + ans + '.', CHQ_KIND[q].w[1] + ': ' + ans + '.'], no: ['Major 3 + 2, minor 2 + 3, diminished 2 + 2, augmented 3 + 3.', '장 3 + 2, 단 2 + 3, 감 2 + 2, 증 3 + 3이에요.'] }; },
};

// ── seventh chords: one more 3rd on top
const CHQ_7W = { maj7: [['major 7th', '장7화음'], 'maj7', '3, 2, 3'], dom7: [['dominant 7th', '딸림7화음'], '7', '3, 2, 2'], m7: [['minor 7th', '단7화음'], 'm7', '2, 3, 2'], hd: [['half-diminished 7th', '반감7화음'], 'm7♭5', '2, 2, 3'], dim7: [['diminished 7th', '감7화음'], '°7', '2, 2, 2'] };
const CHQ_7 = [['C', 'maj7', [0, 4, 7, 11]], ['F', 'maj7', [5, 9, 12, 16]], ['G', 'maj7', [7, 11, 14, 18]], ['G', 'dom7', [7, 11, 14, 17]], ['C', 'dom7', [0, 4, 7, 10]], ['D', 'dom7', [2, 6, 9, 12]], ['D', 'm7', [2, 5, 9, 12]], ['A', 'm7', [9, 12, 16, 19]], ['E', 'm7', [4, 7, 11, 14]],
  ['B', 'hd', [11, 14, 17, 21]], ['E', 'hd', [4, 7, 10, 14]], ['B', 'dim7', [11, 14, 17, 20]], ['E', 'dim7', [4, 7, 10, 13]]];
const chq7 = (e) => { const [rn, q, keys] = e; return { rn, q, keys, names: chqSpell(rn, keys.map(k => k - keys[0])), w: CHQ_7W[q][0], sym: prettyNote(rn) + CHQ_7W[q][1], b: CHQ_7W[q][2] }; };
const CHQ_PART4 = [['root', '근음'], ['3rd', '3음'], ['5th', '5음'], ['7th', '7음']];
const chq7step = (e, title, line) => ({ title, line, fig: (c) => { const C = chq7(e); return { kb: chqBetween(C.keys, { upto: Math.min(1 + Math.floor(c.tk / 2), 3), ks: [C.keys[0], Math.max(C.keys[0] + 12, C.keys[3])] }), mid: chqPlayBtn(C.keys), below: ivqCap(C.sym + ': ' + C.names.join(' '), KQ.COD, true) }; } });
CHQ_SPEC['ch-7th'] = {
  title: ['Seventh chords', '7화음'], allLine: ['Stack one more 3rd on a triad and you get a seventh chord: four notes, the root, 3rd, 5th and 7th.', '3화음 위에 3도를 하나 더 쌓으면 7화음이에요. 근음, 3음, 5음, 7음, 음이 네 개예요.'],
  fig: () => ({ kb: chqKb([0, 4, 7, 11], { ks: [0, 12], words: CHQ_PART4.map(kqT) }), mid: chqPlayBtn([0, 4, 7, 11]), below: ivqCap('Cmaj7: C E G B', KQ.COD, true) }),
  steps: [
    { title: ['A 7th on top', '위에 7음'], line: ['C E G, then skip one more white key: B. C E G B is a seventh chord on C.', 'C E G에서 흰건반을 하나 더 건너면 B. C E G B가 C 위의 7화음이에요.'], fig: () => ({ kb: chqKb([0, 4, 7, 11], { ks: [0, 12], words: CHQ_PART4.map(kqT), marks: { 9: 'pass' } }), mid: chqPlayBtn([0, 4, 7, 11]) }) },
    chq7step(CHQ_7[0], ['Major 7th: 3, 2, 3', '장7화음: 3, 2, 3'], ['C E G B: 3, 2, then 3 keys between. A major triad with a major 7th on top: Cmaj7.', 'C E G B: 사이 건반 3, 2, 3. 장3화음 위에 장7도: Cmaj7이에요.']),
    chq7step(CHQ_7[3], ['Dominant 7th: 3, 2, 2', '딸림7화음: 3, 2, 2'], ['G B D F: a major triad with a minor 7th on top: G7. It is the chord on the 5th note of C major.', 'G B D F: 장3화음 위에 단7도, G7이에요. C장조 5번 음 위의 화음이에요.']),
    chq7step(CHQ_7[6], ['Minor 7th: 2, 3, 2', '단7화음: 2, 3, 2'], ['D F A C: a minor triad with a minor 7th on top: Dm7.', 'D F A C: 단3화음 위에 단7도, Dm7이에요.']),
    chq7step(CHQ_7[9], ['Half-diminished: 2, 2, 3', '반감7화음: 2, 2, 3'], ['B D F A: a diminished triad with a minor 7th on top: Bm7♭5.', 'B D F A: 감3화음 위에 단7도, Bm7♭5예요.']),
    chq7step(CHQ_7[11], ['Diminished 7th: 2, 2, 2', '감7화음: 2, 2, 2'], ['B D F A♭: 2 keys between every time: B°7.', 'B D F A♭: 사이 건반이 매번 2개, B°7이에요.']),
  ],
  make: (n, prev) => { const kind = [0, 1, 0, 2][n % 4];
    if (kind === 0) { let e, g = 0; do { e = kqPick(CHQ_7); } while (prev && prev.e === e && g++ < 8); const C = chq7(e), nm = C.names.join(' ');
      return { e, kind: 'choice', cols: 2, prompt: ['Which seventh chord? Count the keys between.', '어떤 7화음일까요? 사이 건반을 세어 보세요.'], opts: Object.keys(CHQ_7W).map(x => ({ id: x, label: () => kqT(CHQ_7W[x][0]) })), ans: C.q, ok: (v) => v === C.q, play: () => chqPlay(C.keys),
        fig: (c) => ({ kb: c.res ? chqBetween(C.keys, { ks: [C.keys[0], Math.max(C.keys[0] + 12, C.keys[3])] }) : chqKb(C.keys, { ks: [C.keys[0], Math.max(C.keys[0] + 12, C.keys[3])], words: null }) }),
        yes: [C.sym + ': ' + nm + ', ' + C.b + ', ' + C.w[0] + '.', C.sym + ': ' + nm + ', ' + C.b + ', ' + C.w[1] + '이에요.'], no: [nm + ' has ' + C.b + ' keys between: ' + C.w[0] + ', ' + C.sym + '.', nm + ': 사이 건반 ' + C.b + ', ' + C.w[1] + ', ' + ivqJ(C.sym, '이에요', '예요') + '.'] }; }
    if (kind === 1) { const dom = Math.random() < 0.5, [L, r] = kqPick([['C', 0], ['F', 5], ['G', 7]]), T = [r, r + 4, r + 7], tgt = r + (dom ? 10 : 11), sym = L + (dom ? '7' : 'maj7');
      return { kind: 'key', retry: true, prompt: ['Add the 7th to ' + L + ' major and make it ' + sym + '.', L + ' 장3화음에 7음을 더해 ' + sym + '로 만들어요.'], play: () => chqPlay(T, 'block'),
        fig: (c) => ({ kb: c.res === 'ok' ? chqBetween([...T, tgt], { ks: [r, r + 12] }) : chqKb(T, { ks: [r, r + 12] }) }), ok: (k) => k === tgt, onPick: (k, ok) => { if (ok) setTimeout(() => chqPlay([...T, tgt], 'block'), 300); },
        yes: [sym + ': ' + (dom ? '2' : '3') + ' keys between the 5th and the 7th.', sym + ': 5음과 7음 사이에 건반 ' + (dom ? '2' : '3') + '개예요.'],
        no: (k) => [k <= T[2] ? 'The 7th goes above the 5th, ' + ivqL(T[2]) + '.' : 'From the 5th, ' + ivqL(T[2]) + ', leave ' + (dom ? '2' : '3') + ' keys between: ' + (dom ? 'a dominant 7th has 3, 2, 2.' : 'a major 7th has 3, 2, 3.'), k <= T[2] ? '7음은 5음 ' + ivqL(T[2]) + '보다 위에 있어요.' : '5음 ' + ivqL(T[2]) + '에서 사이에 건반 ' + (dom ? '2' : '3') + '개를 두어요. ' + (dom ? '딸림7화음은 3, 2, 2예요.' : '장7화음은 3, 2, 3이에요.')] }; }
    const e = kqPick(CHQ_7.filter(x => ['C', 'D', 'E', 'G', 'A', 'B', 'F'].includes(x[0]) && x[2].every(k => ivqWhite(k)))), C = chq7(e), lo = C.keys[0];
    return { e, kind: 'multi', retry: true, targets: C.keys, prompt: ['Tap the four notes of ' + C.sym + ': ' + C.names.join(' ') + '.', C.sym + '의 네 음을 눌러 보세요: ' + C.names.join(' ') + '.'], prog: (a, b) => ['Found ' + a + ' of ' + b + '. Keep going.', b + '개 중 ' + a + '개를 찾았어요. 계속해요.'],
      fig: () => ({ kb: ivqKb({ ks: [lo, Math.max(lo + 12, C.keys[3])] }) }), yes: [C.sym + ': ' + C.b + ' keys between, ' + C.w[0] + '.', C.sym + ': 사이 건반 ' + C.b + ', ' + C.w[1] + '이에요.'],
      no: (k) => [(ivqWhite(k) ? 'That is ' + ivqL(k) + '. ' : 'Only white keys here. ') + C.sym + ' is ' + C.names.join(' ') + '.', (ivqWhite(k) ? '그건 ' + kqYe(ivqL(k)) + '. ' : '여기서는 흰건반만 써요. ') + ivqJ(C.sym, '은', '는') + ' ' + ivqJ(C.names.join(' '), '이에요', '예요') + '.'] }; },
};

// ── hear major and minor
const chqEarFig = (c, roots) => { const on = c.last && typeof c.last === 'object' && c.last.ch ? c.last.ch : null;
  return { mid: <div style={{ display: 'flex', gap: 8, justifyContent: 'center', flexWrap: 'wrap', margin: '0 0 8px' }}>{roots.flatMap(([rn, r]) => ['major', 'minor'].map(q => { const id = rn + q, on1 = on && on.id === id;
      return <button key={id} className={'chip' + (on1 ? ' active' : '')} aria-pressed={!!on1} style={{ ...KF_BTN, padding: '0 14px', fontSize: 14 }} onClick={() => { c.setLast({ ch: { id, r, q, rn } }); chqPlay(chqK(rn, r, q).keys); }}>▶ {prettyNote(rn)} {kqT(CHQ_KIND[q].w)}</button>; }))}</div>,
    kb: on ? chqBetween(chqK(on.rn, on.r, on.q).keys, { ks: [on.r, on.r + 12] }) : ivqKb({ ks: [roots[0][1], roots[0][1] + 12], marks: { [roots[0][1]]: 'pick' } }) }; };
CHQ_SPEC['ch-ear'] = {
  title: ['Hear major and minor', '장3화음과 단3화음 듣기'], allLine: ['Play the same root as a major and a minor triad and listen: one note after the other, then together. Only the 3rd is different.', '같은 근음으로 장3화음과 단3화음을 들어 보세요. 한 음씩 친 다음 함께 쳐요. 다른 음은 3음 하나뿐이에요.'],
  fig: (c) => chqEarFig(c, [['C', 0]]),
  steps: [
    { title: ['C major and C minor', 'C 장3화음과 C 단3화음'], line: ['Listen to both, more than once. C E G, then C E♭ G.', '둘 다 여러 번 들어 보세요. C E G, 그다음 C E♭ G.'], fig: (c) => chqEarFig(c, [['C', 0]]) },
    { title: ['Other roots', '다른 근음'], line: ['Try G and F: G B D and G B♭ D, F A C and F A♭ C.', 'G와 F로도 해 보세요. G B D와 G B♭ D, F A C와 F A♭ C.'], fig: (c) => chqEarFig(c, [['G', 7], ['F', 5]]) },
  ],
  make: (n, prev) => { const [rn, r] = kqPick([['C', 0], ['D', 2], ['F', 5], ['G', 7], ['A', 9]]), q = Math.random() < 0.5 ? 'major' : 'minor', C = chqK(rn, r, q), nm = C.names.join(' ');
    return { kind: 'choice', cols: 2, prompt: ['Listen: major or minor?', '들어 보세요. 장3화음일까요, 단3화음일까요?'], opts: ['major', 'minor'].map(x => ({ id: x, label: () => kqT(CHQ_KIND[x].w) })), ans: q, ok: (v) => v === q, play: () => chqPlay(C.keys),
      fig: (c) => ({ kb: c.res ? chqBetween(C.keys, { ks: [r, r + 12] }) : ivqKb({ ks: [r, r + 12], marks: { [r]: 'pick' } }) }),
      yes: ['Yes: ' + nm + ', a ' + C.w[0] + '.', '맞아요. ' + nm + ', ' + ivqJ(C.w[1], '이에요', '예요') + '.'], no: ['It was ' + nm + ', a ' + C.w[0] + '. Press ♪ Again and listen to the middle note.', nm + ', ' + ivqJ(C.w[1], '이었어요', '였어요') + '. ♪ 다시를 눌러 가운데 음을 들어 보세요.'] }; },
};

// ══ 3. Chords in a key ══
const CHQ_KEYS = ['C', 'G', 'D', 'F'];
const chqDeg = (key, d, seventh) => { const K = IVQ_KEYS[key], o = (i) => K.k + IVQ_SCALE[i % 7] + (i >= 7 ? 12 : 0), idx = seventh ? [d - 1, d + 1, d + 3, d + 5] : [d - 1, d + 1, d + 3]; return { keys: idx.map(o), names: idx.map(i => K.names[i % 7]) }; };
const chqScaleBase = (key) => { const K = IVQ_KEYS[key], m = {}; IVQ_SCALE.forEach(s => { m[K.k + s] = 'pass'; }); return m; };
const CHQ_ROMW = { 1: ['I', 'I · 으뜸화음'], 4: ['IV', 'IV · 버금딸림화음'], 5: ['V', 'V · 딸림화음'], 7: ['V7', 'V7 · 딸림7화음'] };
const chqDegOf = (key, d) => d === 7 ? chqDeg(key, 5, true) : chqDeg(key, d);
const chqDegKb = (key, d, o = {}) => { const D = chqDegOf(key, d), K = IVQ_KEYS[key]; return chqKb(D.keys, { ks: [K.k, K.k + 17], base: o.scale ? chqScaleBase(key) : {}, words: o.words === undefined ? [CHQ_ROMW[d] ? CHQ_ROMW[d][0] : String(d), null, null, null] : o.words }); };
CHQ_SPEC['ch-tonic'] = {
  title: ['The tonic triad', '으뜸화음'], allLine: ['The triad on the key note of a scale is its tonic triad, chord I: the scale’s 1st, 3rd and 5th notes.', '음계의 으뜸음 위의 3화음이 으뜸화음, I이에요. 음계의 1번, 3번, 5번 음이에요.'],
  fig: (c) => { const key = CHQ_KEYS[Math.floor(c.tk / 3) % 4], D = chqDeg(key, 1); return { kb: chqDegKb(key, 1, { scale: true, words: ['1', '3', '5'] }), below: ivqCap(kqT([key + ' major: ' + D.names.join(' '), key + '장조: ' + D.names.join(' ')]), KQ.COD, true) }; },
  steps: [
    { title: ['C major: C E G', 'C장조: C E G'], line: ['In C major, the 1st, 3rd and 5th notes are C, E and G.', 'C장조에서 1번, 3번, 5번 음은 C, E, G예요.'], fig: () => ({ kb: chqDegKb('C', 1, { scale: true, words: ['1', '3', '5'] }), mid: chqPlayBtn(chqDeg('C', 1).keys) }) },
    { title: ['G major: G B D', 'G장조: G B D'], line: ['In G major: G, B and D.', 'G장조에서는 G, B, D예요.'], fig: () => ({ kb: chqDegKb('G', 1, { scale: true, words: ['1', '3', '5'] }), mid: chqPlayBtn(chqDeg('G', 1).keys) }) },
    { title: ['D and F major', 'D장조와 F장조'], line: ['D major: D F♯ A. F major: F A C. In a major key the tonic triad is always a major triad.', 'D장조: D F♯ A. F장조: F A C. 장조의 으뜸화음은 언제나 장3화음이에요.'], fig: () => ({ top: <>{ivqKbEl(chqDegKb('D', 1, { scale: true, words: ['1', '3', '5'] }))}{ivqCap(kqT(['D major: D F♯ A', 'D장조: D F♯ A']), KQ.COD)}</>, kb: chqDegKb('F', 1, { scale: true, words: ['1', '3', '5'] }), below: ivqCap(kqT(['F major: F A C', 'F장조: F A C']), KQ.COD) }) },
  ],
  make: (n, prev) => { const kind = n % 3; let key, g = 0; do { key = kqPick(CHQ_KEYS); } while (prev && prev.key === key && g++ < 8); const D = chqDeg(key, 1), K = IVQ_KEYS[key];
    if (kind === 0) return { key, kind: 'multi', retry: true, targets: D.keys, prompt: ['Tap the tonic triad of ' + key + ' major: the 1st, 3rd and 5th notes. The scale is marked.', key + '장조의 으뜸화음을 눌러 보세요. 1번, 3번, 5번 음이에요. 음계가 표시돼 있어요.'], prog: (a, b) => ['Found ' + a + ' of ' + b + '. Keep going.', b + '개 중 ' + a + '개를 찾았어요. 계속해요.'],
      fig: () => ({ kb: ivqKb({ ks: [K.k, K.k + 14], marks: chqScaleBase(key) }) }), yes: [key + ' major’s tonic triad: ' + D.names.join(' ') + '.', key + '장조의 으뜸화음: ' + D.names.join(' ') + '.'],
      no: (k) => ['Count the marked scale from ' + key + ' as 1: notes 1, 3 and 5 are ' + D.names.join(' ') + '.', key + '를 1로 표시된 음계를 세어 보세요. 1번, 3번, 5번 음은 ' + ivqJ(D.names.join(' '), '이에요', '예요') + '.'] };
    if (kind === 1) return { key, kind: 'choice', cols: 4, prompt: ['This is the tonic triad of a major key. Which key?', '이건 어느 장조의 으뜸화음일까요?'], opts: CHQ_KEYS.map(x => ({ id: x, label: () => t(x + ' major', x + '장조') })), ans: key, ok: (v) => v === key, play: () => chqPlay(D.keys, 'block'),
      fig: (c) => ({ kb: chqKb(D.keys, { ks: [K.k, K.k + 14], words: c.res ? ['1', '3', '5'] : null, plain: !c.res }) }),
      yes: [D.names.join(' ') + ': the tonic triad of ' + key + ' major.', D.names.join(' ') + ': ' + key + '장조의 으뜸화음이에요.'], no: ['The root names the key: ' + D.names.join(' ') + ' is the tonic triad of ' + key + ' major.', '근음이 조 이름이에요. ' + ivqJ(D.names.join(' '), '은', '는') + ' ' + key + '장조의 으뜸화음이에요.'] };
    const ans = D.names.join(' '), L0 = 'CDEFGAB'.indexOf(key), w1 = [0, 2, 4].map(s => 'CDEFGAB'[(L0 + s) % 7]).join(' '), w2 = [0, 1, 2].map(j => K.names[j]).join(' '), w3 = [4, 6, 8].map(j => K.names[j % 7]).join(' ');
    const opts = shuffle([...new Set([ans, w1, w2, w3])]); while (opts.length < 4) opts.push([3, 5, 7].map(j => K.names[j % 7]).join(' '));
    return { key, kind: 'choice', cols: 2, prompt: ['In ' + key + ' major, the tonic triad is…', key + '장조의 으뜸화음은…'], opts: opts.slice(0, 4).map(x => ({ id: x, label: x })), ans, ok: (v) => v === ans,
      fig: (c) => ({ kb: c.res ? chqDegKb(key, 1, { scale: true, words: ['1', '3', '5'] }) : ivqKb({ ks: [K.k, K.k + 14], marks: chqScaleBase(key) }) }),
      yes: [ans + ': notes 1, 3 and 5 of the scale.', ans + ': 음계의 1번, 3번, 5번 음이에요.'], no: ['Notes 1, 3 and 5 of ' + key + ' major: ' + ans + '.', key + '장조의 1번, 3번, 5번 음: ' + ivqJ(ans, '이에요', '예요') + '.'] }; },
};

// ── I, IV and V7
const chqPlayRowBtn = (key, ds) => <div style={{ textAlign: 'center', margin: '0 0 6px' }}>{ivqPlayBtn('▶ ' + ds.map(d => CHQ_ROMW[d][0]).join(' '), () => ds.forEach((x, i) => setTimeout(() => chqPlay(chqDegOf(key, x).keys, 'block'), i * 900)))}</div>;
CHQ_SPEC['ch-145'] = {
  title: ['I, IV and V7', 'I, IV, V7'], allLine: ['The chords on the 1st, 4th and 5th notes of a major scale are I, IV and V. Put a 7th on V and you get V7, which leads strongly back to I. Tap one to hear it.', '장음계의 1번, 4번, 5번 음 위의 화음이 I, IV, V예요. V에 7음을 더하면 V7, I로 강하게 돌아가요. 하나를 눌러 들어 보세요.'],
  fig: (c) => { const d = c.last && typeof c.last === 'object' && c.last.deg ? c.last.deg : 1, D = chqDegOf('C', d);
    return { mid: <div style={{ display: 'grid', gridTemplateColumns: 'repeat(4, minmax(0, 1fr))', gap: 6, maxWidth: 340, margin: '0 auto 8px' }}>{[1, 4, 5, 7].map(x => <button key={x} className={'chip' + (x === d ? ' active' : '')} aria-pressed={x === d} style={{ minHeight: 44, justifyContent: 'center', fontWeight: 900, fontSize: 18 }} onClick={() => { c.setLast({ deg: x }); chqPlay(chqDegOf('C', x).keys, 'block'); }}>{CHQ_ROMW[x][0]}</button>)}</div>,
      kb: chqDegKb('C', d, { scale: true }), below: ivqCap(kqT([CHQ_ROMW[d][0] + ' in C major: ' + D.names.join(' '), 'C장조의 ' + CHQ_ROMW[d][1] + ': ' + D.names.join(' ')]), KQ.COD, true) }; },
  steps: [
    { title: ['I: the tonic', 'I: 으뜸화음'], line: ['Chord I is the tonic triad, on the 1st note: C E G.', 'I은 1번 음 위의 으뜸화음이에요. C E G.'], fig: () => ({ kb: chqDegKb('C', 1, { scale: true }), mid: chqPlayBtn(chqDeg('C', 1).keys) }) },
    { title: ['IV: on the 4th note', 'IV: 4번 음 위'], line: ['Chord IV starts on the 4th note, F: F A C.', 'IV는 4번 음 F에서 시작해요. F A C, 버금딸림화음이에요.'], fig: () => ({ kb: chqDegKb('C', 4, { scale: true }), mid: chqPlayBtn(chqDeg('C', 4).keys) }) },
    { title: ['V: on the 5th note', 'V: 5번 음 위'], line: ['Chord V starts on the 5th note, G: G B D.', 'V는 5번 음 G에서 시작해요. G B D, 딸림화음이에요.'], fig: () => ({ kb: chqDegKb('C', 5, { scale: true }), mid: chqPlayBtn(chqDeg('C', 5).keys) }) },
    { title: ['V7: one more note', 'V7: 음 하나 더'], line: ['Skip one more scale note above G B D: F. G B D F is V7. Play V7 then I and hear it settle.', 'G B D 위로 음계 음을 하나 더 건너 F. G B D F가 V7이에요. V7 다음에 I을 치면 편안히 자리 잡아요.'], fig: () => ({ kb: chqDegKb('C', 7, { scale: true }), mid: chqPlayRowBtn('C', [7, 1]) }) },
    { title: ['I IV V7 I', 'I IV V7 I'], line: ['Play them in turn and come back to I. In a major key I, IV and V are major triads, and V7 is a dominant 7th.', '차례로 치고 다시 I로 돌아와요. 장조에서 I, IV, V는 장3화음이고, V7은 딸림7화음이에요.'],
      fig: (c) => { const d = [1, 4, 7, 1][Math.floor(c.tk / 2) % 4]; return { kb: chqDegKb('C', d, { scale: true }), mid: chqPlayRowBtn('C', [1, 4, 7, 1]) }; } },
  ],
  make: (n, prev) => { const kind = [0, 1, 0, 2][n % 4]; let key, d, g = 0; do { key = kqPick(CHQ_KEYS); d = kqPick([1, 4, 5, 7]); } while (prev && prev.id === key + d && g++ < 8); const D = chqDegOf(key, d), K = IVQ_KEYS[key], id = key + d, nd = d === 7 ? 5 : d;
    if (kind === 0) return { id, kind: 'choice', cols: 4, prompt: ['In ' + key + ' major, which chord is marked?', key + '장조에서 표시된 화음은 어느 것일까요?'], opts: [1, 4, 5, 7].map(x => ({ id: String(x), label: CHQ_ROMW[x][0] })), ans: String(d), ok: (v) => v === String(d), play: () => chqPlay(D.keys, 'block'),
      fig: (c) => ({ kb: chqDegKb(key, d, { scale: true, words: c.res ? undefined : null }) }),
      yes: [D.names.join(' ') + ' starts on note ' + nd + ' of ' + key + ' major' + (d === 7 ? ', with a 7th on top: V7.' : ': chord ' + CHQ_ROMW[d][0] + '.'), ivqJ(D.names.join(' '), '은', '는') + ' ' + key + '장조의 ' + nd + '번 음에서 시작해요' + (d === 7 ? '. 7음이 더해져서 V7이에요.' : '. ' + ivqJ(CHQ_ROMW[d][1], '이에요', '예요') + '.')],
      no: [d === 1 ? 'It starts on the key note itself, ' + key + ': chord I.' : 'Count up the scale from ' + key + ' as 1 to the lowest marked note, ' + D.names[0] + ': note ' + nd + '. ' + (d === 7 ? 'Four notes, so it is V7.' : d === 5 ? 'Three notes, so it is V.' : 'So it is IV.'), d === 1 ? '으뜸음 ' + key + '에서 시작해요. I이에요.' : key + '를 1로 맨 아래 표시 음 ' + D.names[0] + '까지 세면 ' + nd + '번 음이에요. ' + (d === 7 ? '음이 넷이라 V7이에요.' : d === 5 ? '음이 셋이라 V예요.' : '그래서 IV예요.')] };
    if (kind === 1) return { id, kind: 'multi', retry: true, targets: D.keys, prompt: ['Tap chord ' + CHQ_ROMW[d][0] + ' in ' + key + ' major. The scale is marked.', key + '장조의 ' + ivqJ(CHQ_ROMW[d][0], '을', '를') + ' 눌러 보세요. 음계가 표시돼 있어요.'], prog: (a, b) => ['Found ' + a + ' of ' + b + '. Keep going.', b + '개 중 ' + a + '개를 찾았어요. 계속해요.'],
      fig: () => ({ kb: ivqKb({ ks: [K.k, K.k + 17], marks: chqScaleBase(key) }) }), yes: [CHQ_ROMW[d][0] + ' in ' + key + ' major: ' + D.names.join(' ') + '.', key + '장조의 ' + CHQ_ROMW[d][1] + ': ' + D.names.join(' ') + '.'],
      no: () => ['Start on note ' + nd + ' of the scale, ' + D.names[0] + ', then skip a scale note each time: ' + D.names.join(' ') + '.', '음계의 ' + nd + '번 음 ' + D.names[0] + '에서 시작해서 음계 음을 하나씩 건너요. ' + ivqJ(D.names.join(' '), '이에요', '예요') + '.'] };
    const ans = D.names.join(' '), others = [1, 4, 5, 7].filter(x => x !== d).map(x => chqDegOf(key, x).names.join(' ')), opts = shuffle([ans, ...shuffle(others).slice(0, 3)]);
    return { id, kind: 'choice', cols: 2, prompt: ['In ' + key + ' major, chord ' + CHQ_ROMW[d][0] + ' is…', key + '장조의 ' + ivqJ(CHQ_ROMW[d][0], '은', '는') + '…'], opts: opts.map(x => ({ id: x, label: x })), ans, ok: (v) => v === ans,
      fig: (c) => ({ kb: c.res ? chqDegKb(key, d, { scale: true }) : ivqKb({ ks: [K.k, K.k + 17], marks: chqScaleBase(key) }) }),
      yes: [ans + (d === 7 ? ': V with its 7th.' : ': the triad on note ' + d + '.'), ans + (d === 7 ? ': V에 7음을 더한 화음이에요.' : ': ' + d + '번 음 위의 3화음이에요.')], no: [CHQ_ROMW[d][0] + ' starts on note ' + nd + ', ' + D.names[0] + ': ' + ans + '.', ivqJ(CHQ_ROMW[d][0], '은', '는') + ' ' + nd + '번 음 ' + D.names[0] + '에서 시작해요. ' + ivqJ(ans, '이에요', '예요') + '.'] }; },
};

// ── inversions, triads and seventh chords
const CHQ_INV = [['root position', '기본 위치'], ['1st inversion', '제1전위'], ['2nd inversion', '제2전위'], ['3rd inversion', '제3전위']];
const chqInvKeysN = (keys, inv) => keys.slice(inv).concat(keys.slice(0, inv).map(k => k + 12));
const chqInvKbN = (keys, inv, names) => { const K = chqInvKeysN(keys, inv), m = {}, nm = {}, ncol = {}, r = keys[0];
  K.forEach((k, j) => { const ro = keys.indexOf(k) >= 0 ? keys.indexOf(k) : keys.indexOf(k - 12); m[k] = j === 0 ? 'pickB' : 'pick'; nm[k] = names ? names[(j + inv) % keys.length] : kqT(CHQ_PART4[ro]); ncol[k] = [KQ.COD, KQ.BL, KQ.NV, KQ.COD][ro]; });
  return ivqKb({ ks: [inv === 3 ? K[0] : Math.min(r, K[0]), Math.min(Math.max(K[K.length - 1], r + 12), 24)], marks: m, names: nm, ncol }); };   // 3rd inversion: start at the 7th, so the keys stay big
const CHQ_INVSET = [['C', [0, 4, 7], 'C major'], ['F', [5, 9, 12], 'F major'], ['G', [7, 11, 14], 'G major'], ['D', [2, 5, 9], 'D minor'], ['A', [9, 12, 16], 'A minor'], ['C', [0, 4, 7, 10], 'C7'], ['F', [5, 9, 12, 15], 'F7'], ['D', [2, 5, 9, 12], 'Dm7']];
CHQ_SPEC['ch-inv'] = {
  title: ['Inversions', '전위'], allLine: ['Keep the same notes but put a different one at the bottom. C E G, E G C and G C E are all a C major triad.', '같은 음에서 맨 아래 음만 바꿔요. C E G, E G C, G C E는 모두 C 장3화음이에요.'],
  fig: (c) => { const inv = Math.floor(c.tk / 3) % 3; return { kb: chqInvKbN([0, 4, 7], inv), below: ivqCap(kqT([['C E G', 'E G C', 'G C E'][inv] + ': ' + CHQ_INV[inv][0], ['C E G', 'E G C', 'G C E'][inv] + ': ' + CHQ_INV[inv][1]]), KQ.COD, true), staffAlt: chqStaff([{ notes: chqTriD(28), lab: t('root pos.', '기본 위치') }, { notes: [IVX_N(30), IVX_N(32), IVX_N(35)], lab: t('1st inv.', '제1전위') }, { notes: [IVX_N(32), IVX_N(35), IVX_N(37)], lab: t('2nd inv.', '제2전위') }], { width: 260, mw: 360 }) }; },
  steps: [
    { title: ['Root position', '기본 위치'], line: ['The root is at the bottom: C E G.', '근음이 맨 아래예요. C E G.'], fig: () => ({ kb: chqInvKbN([0, 4, 7], 0), mid: chqPlayBtn([0, 4, 7]) }) },
    { title: ['1st inversion', '제1전위'], line: ['Move the C up an octave: E G C. Now the 3rd is at the bottom.', 'C를 한 옥타브 위로 올려요. E G C. 이제 3음이 맨 아래예요.'], fig: () => ({ kb: chqInvKbN([0, 4, 7], 1), mid: chqPlayBtn([4, 7, 12]) }) },
    { title: ['2nd inversion', '제2전위'], line: ['Move the E up too: G C E. Now the 5th is at the bottom.', 'E도 위로 올려요. G C E. 이제 5음이 맨 아래예요.'], fig: () => ({ kb: chqInvKbN([0, 4, 7], 2), mid: chqPlayBtn([7, 12, 16]) }) },
    { title: ['3rd inversion', '제3전위'], line: ['A seventh chord has four notes, so it has one more: the 7th at the bottom. C7 as B♭ C E G.', '7화음은 음이 넷이라서 하나 더 있어요. 7음이 맨 아래, C7을 B♭ C E G로.'], fig: () => ({ kb: chqInvKbN([0, 4, 7, 10], 3), mid: chqPlayBtn([10, 12, 16, 19]) }) },
  ],
  make: (n, prev) => { let e, inv, g = 0; do { e = kqPick(CHQ_INVSET); inv = kqRnd(e[1].length); } while (prev && prev.id === e[2] + inv && g++ < 8);
    const [rn, keys, nmEn] = e, names = chqSpell(rn, keys.map(k => k - keys[0])), K = chqInvKeysN(keys, inv), order = names.slice(inv).concat(names.slice(0, inv)), four = keys.length === 4, id = nmEn + inv;
    const bare = ivqKb({ ks: [Math.min(keys[0], K[0]), Math.min(Math.max(K[K.length - 1], keys[0] + 12), 24)], marks: Object.fromEntries(K.map((k, j) => [k, j === 0 ? 'pickB' : 'pick'])), names: Object.fromEntries(K.map((k, j) => [k, order[j]])) });
    const nmKo = nmEn.replace(' major', ' 장3화음').replace(' minor', ' 단3화음');
    if (n % 2 === 0) return { id, kind: 'choice', cols: 2, prompt: ['Look at the bottom note. Which position is ' + nmEn + ' in?', '맨 아래 음을 보세요. ' + ivqJ(nmKo, '은', '는') + ' 어떤 자리일까요?'], opts: CHQ_INV.slice(0, four ? 4 : 3).map((w, j) => ({ id: String(j), label: () => kqT(w) })), ans: String(inv), ok: (v) => v === String(inv), play: () => chqPlay(K, 'block'),
      fig: (c) => ({ kb: c.res ? chqInvKbN(keys, inv) : bare }),
      yes: [order.join(' ') + ': the ' + CHQ_PART4[inv][0] + ' is at the bottom, ' + CHQ_INV[inv][0] + '.', order.join(' ') + ': ' + CHQ_PART4[inv][1] + '이 맨 아래, ' + CHQ_INV[inv][1] + '예요.'], no: ['The bottom note is ' + order[0] + ', the ' + CHQ_PART4[inv][0] + ' of ' + nmEn + ': ' + CHQ_INV[inv][0] + '.', '맨 아래 음 ' + ivqJ(order[0], '은', '는') + ' ' + nmKo + '의 ' + CHQ_PART4[inv][1] + '이에요. ' + CHQ_INV[inv][1] + '예요.'] };
    const opts = shuffle(names.slice());
    return { id, kind: 'choice', cols: four ? 4 : 3, prompt: ['Which note is the root? Stack the notes in skips.', '근음은 어느 음일까요? 음을 하나씩 건너 쌓아 보세요.'], opts: opts.map(x => ({ id: x, label: x })), ans: names[0], ok: (v) => v === names[0], play: () => chqPlay(K, 'block'),
      fig: (c) => ({ kb: c.res ? chqInvKbN(keys, inv) : bare }),
      yes: ['Stacked in skips it is ' + names.join(' ') + ': ' + nmEn + '.', '건너 쌓으면 ' + names.join(' ') + ', ' + ivqJ(nmKo, '이에요', '예요') + '.'], no: ['Stack the same notes in skips: ' + names.join(' ') + '. The root is ' + names[0] + '.', '같은 음을 하나씩 건너 쌓으면 ' + names.join(' ') + '. 근음은 ' + kqYe(names[0]) + '.'] }; },
};

const chqRow = (id, en, ko, bEn, bKo) => [id, en, ko, bEn, bKo, () => <KqEngine spec={CHQ_SPEC[id]}/>];
const CHQ_ROWS = [
  chqRow('ch-stack', 'Root, 3rd, 5th', '근음, 3음, 5음', 'Skip a key, skip a key: a triad on any white key.', '하나 건너, 하나 건너: 어느 흰건반 위에서나 3화음.'),
  chqRow('ch-staff', 'Triads on the staff', '오선 위의 3화음', 'All on lines or all in spaces; the root at the bottom.', '모두 줄 위에, 또는 모두 칸 안에. 근음은 맨 아래.'),
  chqRow('ch-hands', 'Playing a triad', '3화음 치기', 'Blocked or broken; fingers 1 3 5 and 5 3 1.', '함께 또는 펼쳐서. 손가락 1 3 5와 5 3 1.'),
  chqRow('ch-mm', 'Major or minor', '장3화음? 단3화음?', 'Keys between: 3 + 2 or 2 + 3.', '사이 건반 3 + 2 또는 2 + 3.'),
  chqRow('ch-da', 'Diminished and augmented', '감3화음과 증3화음', 'Keys between: 2 + 2 or 3 + 3.', '사이 건반 2 + 2 또는 3 + 3.'),
  chqRow('ch-7th', 'Seventh chords', '7화음', 'One more 3rd on top: five kinds.', '3도를 하나 더: 다섯 가지.'),
  chqRow('ch-ear', 'Hear major and minor', '장3화음과 단3화음 듣기', 'The same root, one note different.', '같은 근음, 다른 음 하나.'),
  chqRow('ch-tonic', 'The tonic triad', '으뜸화음', 'Notes 1, 3 and 5 of the scale: chord I.', '음계의 1번, 3번, 5번 음: I.'),
  chqRow('ch-145', 'I, IV and V7', 'I, IV, V7', 'The chords on notes 1, 4 and 5, and V7.', '1번, 4번, 5번 음 위의 화음과 V7.'),
  chqRow('ch-inv', 'Inversions', '전위', 'A different note at the bottom; 7th chords too.', '맨 아래 음만 바꿔요. 7화음도.'),
];
CHQ_ROWS.forEach(([id, en, ko, benEn, bko, Comp]) => {
  TOOLS.push({ id, ch: 'concept', title: en, blurb: benEn, hidden: true, get kicker() { return TOOL_AREAS.find(a => a.id === 'pitch').name + ' · ' + homeCatById('p-chords').name; }, C: Comp });
  TOOL_KO[id] = [ko, bko];
  const tl = TOOLS[TOOLS.length - 1], k = TOOL_KO[id], ti = tl.title, bl = tl.blurb; tl.titleEn = ti; tl.blurbEn = bl;
  Object.defineProperty(tl, 'title', { get: () => (LANG === 'ko' ? k[0] : ti), enumerable: true, configurable: true });
  Object.defineProperty(tl, 'blurb', { get: () => (LANG === 'ko' ? k[1] : bl), enumerable: true, configurable: true });
  TOOL_CONCEPT[id] = 'p-chords';
});
