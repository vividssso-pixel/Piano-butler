// ─── Pitch gaps (her call 2026-10-24: every old Pitch topic moves onto the Home): writing a key signature, transposing,
// the pentatonic scale. Same engine as Keys and staff. Music facts and Korean terms flagged for her review (CLAUDE.md row 642).

// ── Write a key signature: each sign in its order, on its own line or space
const PG_KEYS = { G: ['#', 1], D: ['#', 2], A: ['#', 3], E: ['#', 4], B: ['#', 5], F: ['b', 1], Bb: ['b', 2], Eb: ['b', 3], Ab: ['b', 4], Db: ['b', 5] };
const pgSigns = (key, clef) => { const [s, n] = PG_KEYS[key]; return SKG_ORDER[s].slice(0, n).map(l => [s, skgSignD(s, l, clef), l]); };
const pgSignName = ([s, , l]) => l + (s === '#' ? '♯' : '♭');
const pgKeyName = (key) => [prettyNote(key) + ' major', prettyNote(key) + '장조'];
const pgWhere = (d, clef) => { const off = d - (clef === 'bass' ? 18 : 30);
  if (off < 0) return ['below the staff', '오선 아래']; if (off > 8) return off === 9 ? ['in the space just above the staff', '오선 바로 위 칸'] : ['above the staff', '오선 위'];
  return off % 2 === 0 ? ['on line ' + (off / 2 + 1), (off / 2 + 1) + '번 줄'] : ['in space ' + ((off + 1) / 2), ((off + 1) / 2) + '번 칸']; };
// the staff with a key signature (signs in order after the clef); with onPick, tap rows from lo to hi; pickd: the tapped place, drawn in the next slot
function PgSigSvg({ clef, signs, cols, onPick, lo, hi, pickd, ok, next }) {
  const c = CLEFS[clef], W = 176, yOf = (d) => dY(d), ink = clefInkYs(clef, yOf, clef), sx = (i) => 52 + i * 13;
  const ds = signs.map(x => x[1]).concat(pickd != null ? [pickd] : []), top = Math.max(c.high, ...ds) + 1, bot = Math.min(c.low, ...ds) - 1;
  const y0 = Math.min(yOf(top) - 16, ink[0] - 2), y1 = Math.max(yOf(bot) + 12, ink[1] + 2), rows = []; if (onPick) for (let d = lo; d <= hi; d++) rows.push(d);
  return <svg viewBox={`0 ${y0} ${W} ${y1 - y0}`} style={{ width: '100%', maxWidth: 360, display: 'block', margin: '0 auto', touchAction: 'manipulation', userSelect: 'none' }}>
    {c.lines.map(l => <line key={l} x1="4" x2={W - 4} y1={yOf(l)} y2={yOf(l)} stroke={KQ.NV} strokeOpacity="0.6" strokeWidth="1.1"/>)}
    <ClefGlyph clef={clef} st={clef} yOf={yOf} ink={KQ.NV}/>
    {signs.map(([s, d], i) => <g key={'s' + i} style={{ animation: 'fadeUp 0.25s both' }}>{tnAcc(s, sx(i), yOf(d), (cols && cols[i]) || KQ.NV)}</g>)}
    {onPick && rows.map(d => <circle key={'g' + d} cx={sx(signs.length)} cy={yOf(d)} r="1.2" fill={KQ.CO} opacity="0.6" style={{ pointerEvents: 'none' }}/>)}
    {pickd != null && next && <g>{tnAcc(next, sx(signs.length), yOf(pickd), ok ? '#2e8a6e' : '#c8361b')}</g>}
    {rows.map(d => <rect key={'r' + d} x="40" y={yOf(d) - 2.5} width={W - 44} height="5" fill="transparent" style={{ cursor: 'pointer' }} onClick={() => onPick(d)}/>)}
  </svg>;
}
const pgSigFig = (key, clef, upto, hl) => { const S = pgSigns(key, clef).slice(0, upto == null ? 9 : upto); return { staff: <PgSigSvg clef={clef} signs={S} cols={S.map((_, i) => i === hl ? KQ.CO : KQ.NV)}/>, below: ivqCap(S.map(pgSignName).join(' '), KQ.COD) }; };
const PG_SH7 = ['F', 'C', 'G', 'D', 'A', 'E', 'B'].map(l => ['#', skgSignD('#', l, 'treble'), l]), PG_FL7 = ['B', 'E', 'A', 'D', 'G', 'C', 'F'].map(l => ['b', skgSignD('b', l, 'treble'), l]);
const pgSevenFig = (S, c) => { const n = Math.min(c.tk + 1, 7), sh = S.slice(0, n); return { staff: <PgSigSvg clef="treble" signs={sh} cols={sh.map((_, i) => i === n - 1 ? KQ.CO : KQ.NV)}/>, below: ivqCap(kqT([pgSignName(S[n - 1]) + ' ' + pgWhere(S[n - 1][1], 'treble')[0], pgSignName(S[n - 1]) + ': ' + pgWhere(S[n - 1][1], 'treble')[1]]), KQ.COD) }; };
const PG_SPEC = {};
PG_SPEC['kf-write'] = {
  title: ['Write a key signature', '조표 쓰기'], allLine: ['The sharps or flats of a key signature go straight after the clef, in their order, each on its own line or space.', '조표의 샵이나 플랫은 음자리표 바로 뒤에, 정해진 순서대로, 저마다 정해진 줄이나 칸에 써요.'],
  fig: () => ({ top: <>{pgSigFig('A', 'treble').staff}{ivqCap(kqT(['A major: F♯ C♯ G♯', 'A장조: F♯ C♯ G♯']), KQ.COD)}</>, staff: pgSigFig('Eb', 'treble').staff, below: ivqCap(kqT(['E♭ major: B♭ E♭ A♭', 'E♭장조: B♭ E♭ A♭']), KQ.COD) }),
  steps: [
    { title: ['Sharps, in order', '샵, 순서대로'], line: ['F♯ C♯ G♯ D♯ A♯ E♯ B♯. F♯ sits on the top line, C♯ in space 3, G♯ just above the staff, then down and up again.', 'F♯ C♯ G♯ D♯ A♯ E♯ B♯. F♯은 맨 윗줄, C♯은 3번 칸, G♯은 오선 바로 위 칸, 그다음 내려갔다 올라갔다 해요.'], fig: (c) => pgSevenFig(PG_SH7, c) },
    { title: ['Flats, in order', '플랫, 순서대로'], line: ['B♭ E♭ A♭ D♭ G♭ C♭ F♭. B♭ sits on line 3, E♭ in space 4, A♭ in space 2, then up and down again.', 'B♭ E♭ A♭ D♭ G♭ C♭ F♭. B♭은 3번 줄, E♭은 4번 칸, A♭은 2번 칸, 그다음 올라갔다 내려갔다 해요.'], fig: (c) => pgSevenFig(PG_FL7, c) },
    { title: ['In the bass clef', '낮은음자리표에서'], line: ['The same shape, each sign two places lower on the staff. D major: F♯ on line 4, C♯ in space 2.', '모양은 같고, 오선에서 두 자리씩 낮게 써요. D장조: F♯은 4번 줄, C♯은 2번 칸.'], fig: () => pgSigFig('D', 'bass') },
  ],
  make: (n, prev) => { const clef = n % 3 === 2 ? 'bass' : 'treble'; let key, i, g = 0; do { key = kqPick(Object.keys(PG_KEYS)); i = kqRnd(PG_KEYS[key][1]); } while (prev && prev.id === key + i && g++ < 8);
    const S = pgSigns(key, clef), sg = S[i], want = sg[1], nm = pgSignName(sg), K = pgKeyName(key), w = kqClefW(clef), lo = clef === 'bass' ? 16 : 28, hi = clef === 'bass' ? 27 : 40, have = S.slice(0, i).map(pgSignName), wh = pgWhere(want, clef);
    return { id: key + i, kind: 'tap', retry: true, prompt: [K[0] + ' has ' + S.length + (sg[0] === '#' ? ' sharp' : ' flat') + (S.length > 1 ? 's' : '') + (have.length ? '. ' + have.join(' ') + ' ' + (have.length > 1 ? 'are' : 'is') + ' written.' : '.') + ' Tap where ' + nm + ' goes (' + w[0] + ' clef).', K[1] + '에는 ' + (sg[0] === '#' ? '샵' : '플랫') + '이 ' + S.length + '개 있어요.' + (have.length ? ' ' + have.join(' ') + '까지 썼어요.' : '') + ' ' + nm + '이 들어갈 자리를 눌러요. (' + w[1] + '표)'],
      ok: (v) => v === want, onPick: (v, ok) => { if (ok) playKey(dMidiKey(want), 0.4); },
      fig: (c) => ({ staff: <PgSigSvg clef={clef} signs={S.slice(0, i)} onPick={c.res === 'ok' ? null : c.pick} lo={lo} hi={hi} pickd={c.pickd} ok={c.res === 'ok'} next={sg[0]}/> }),
      yes: [nm + ', ' + wh[0] + '.', nm + ', ' + wh[1] + '이에요.'],
      no: (v) => kqLetter(v) === sg[2] ? ['The right letter, but ' + nm + ' goes ' + wh[0] + ' in a key signature.', '글자는 맞지만, 조표에서 ' + nm + '은 ' + wh[1] + '에 써요.'] : ['That place is ' + kqLetter(v) + '. ' + nm + ' goes ' + wh[0] + '.', '그 자리는 ' + kqLetter(v) + '예요. ' + nm + '은 ' + wh[1] + '에 써요.'] }; },
};

// ── Transposing: the same scale numbers in another key
const PG_TUNE = [1, 2, 3, 2, 1];
const pgTune = (key, deg = PG_TUNE) => { const K = IVQ_KEYS[key]; return { keys: deg.map(d => K.k + IVQ_SCALE[d - 1]), names: deg.map(d => K.names[d - 1]) }; };
const pgTunePlay = (keys) => keys.forEach((k, i) => setTimeout(() => playKey(k, 0.4), i * 420));
const pgTuneKb = (key, o = {}) => { const T = pgTune(key), K = IVQ_KEYS[key], m = {}, names = {}, ncol = {}; T.keys.forEach((k, j) => { m[k] = 'pick'; names[k] = String(PG_TUNE[j]); ncol[k] = KQ.COD; });
  return ivqKb({ ks: [K.k, K.k + 12], marks: { ...chqScaleBase(key), ...m }, names, ncol }); };
const pgTuneCap = (key) => ivqCap(kqT([key + ' major: ' + pgTune(key).names.join(' '), key + '장조: ' + pgTune(key).names.join(' ')]), KQ.COD);
const pgTuneBtn = (key) => <div style={{ textAlign: 'center', margin: '0 0 6px' }}>{ivqPlayBtn(t('▶ Play in ' + key, '▶ ' + key + '장조로 치기'), () => pgTunePlay(pgTune(key).keys))}</div>;
PG_SPEC['kf-trans'] = {
  title: ['Transposing', '이조'], allLine: ['Transposing moves a whole tune into another key. Every note keeps its number in the scale, so the tune stays the same, only higher or lower.', '이조는 곡 전체를 다른 조로 옮기는 거예요. 음마다 음계의 번호는 그대로라서, 같은 곡이 더 높거나 낮게 들려요.'],
  fig: () => ({ top: <>{pgTuneBtn('C')}{ivqKbEl(pgTuneKb('C'))}{pgTuneCap('C')}</>, mid: pgTuneBtn('G'), kb: pgTuneKb('G'), below: pgTuneCap('G') }),
  steps: [
    { title: ['The tune in C', 'C장조의 곡'], line: ['C D E D C: scale notes 1 2 3 2 1 of C major.', 'C D E D C: C장음계의 1 2 3 2 1번 음이에요.'], fig: () => ({ mid: pgTuneBtn('C'), kb: pgTuneKb('C'), below: pgTuneCap('C') }) },
    { title: ['The same numbers in G', 'G장조에서 같은 번호로'], line: ['Play 1 2 3 2 1 of G major: G A B A G. That is the tune transposed to G.', 'G장음계의 1 2 3 2 1번 음을 쳐요. G A B A G. 이게 G장조로 이조한 곡이에요.'], fig: () => ({ mid: pgTuneBtn('G'), kb: pgTuneKb('G'), below: pgTuneCap('G') }) },
    { title: ['The key signature comes too', '조표도 함께'], line: ['In D major the 3 is F♯, because D major has F♯ in its key signature: D E F♯ E D.', 'D장조에서 3번 음은 F♯이에요. D장조의 조표에 F♯이 있으니까요. D E F♯ E D.'], fig: () => ({ mid: pgTuneBtn('D'), kb: pgTuneKb('D'), below: pgTuneCap('D') }) },
  ],
  make: (n, prev) => { const kind = n % 3; let key, g = 0; do { key = kqPick(['G', 'D', 'F']); } while (prev && prev.key === key && g++ < 8); const K = IVQ_KEYS[key];
    if (kind === 0) { const ans = pgTune(key).names.join(' '), opts = shuffle([...new Set([ans, ...['G', 'D', 'F', 'C'].filter(x => x !== key).map(x => pgTune(x).names.join(' ')), pgTune(key).names.map(x => x.replace('♯', '').replace('♭', '')).join(' ')])]).slice(0, 4);
      if (!opts.includes(ans)) opts[0] = ans;
      return { key, kind: 'choice', cols: 1, prompt: ['C D E D C is in C major. Transposed to ' + key + ' major it is…', 'C D E D C는 C장조예요. ' + key + '장조로 이조하면…'], opts: shuffle(opts).map(x => ({ id: x, label: x })), ans, ok: (v) => v === ans, onPick: () => pgTunePlay(pgTune(key).keys),
        fig: (c) => ({ kb: c.res ? pgTuneKb(key) : ivqKb({ ks: [K.k, K.k + 12], marks: chqScaleBase(key) }) }), yes: ['1 2 3 2 1 of ' + key + ' major: ' + ans + '.', key + '장조의 1 2 3 2 1번 음: ' + ans + '.'],
        no: ['Keep the numbers, 1 2 3 2 1, and use the ' + key + ' major scale: ' + ans + '.', '번호 1 2 3 2 1은 그대로, ' + key + '장음계로 쳐요. ' + ivqJ(ans, '이에요', '예요') + '.'] }; }
    if (kind === 1) { const d = kqPick([3, 4, 5]), cN = IVQ_KEYS.C.names[d - 1], tk = K.k + IVQ_SCALE[d - 1], tn = K.names[d - 1];
      return { key, kind: 'key', retry: true, prompt: ['A tune in C major starts on ' + cN + ', note ' + d + '. Transposed to ' + key + ' major, which key does it start on?', 'C장조의 곡이 ' + d + '번 음 ' + cN + '에서 시작해요. ' + key + '장조로 이조하면 어느 건반에서 시작할까요?'], fig: () => ({ kb: ivqKb({ ks: [K.k, K.k + 12], marks: chqScaleBase(key) }) }), ok: (k) => k === tk, onPick: (k, ok) => { if (ok) playKey(tk, 0.5); },
        yes: ['Note ' + d + ' of ' + key + ' major: ' + tn + '.', key + '장조의 ' + d + '번 음: ' + ivqJ(tn, '이에요', '예요') + '.'], no: ['Keep the number: note ' + d + '. Count up the ' + key + ' major scale from ' + key + ' as 1.', '번호는 그대로 ' + d + '번 음이에요. ' + key + '를 1로 ' + key + '장음계를 세어 보세요.'] }; }
    const T = [1, 3, 5], ans = T.map(d => K.names[d - 1]).join(' '), wrong = [T.map(d => 'CDEFGAB'[('CDEFGAB'.indexOf(key) + d - 1) % 7]).join(' '), [2, 4, 6].map(d => K.names[d - 1]).join(' '), [1, 3, 6].map(d => K.names[d - 1]).join(' ')];
    const opts = [...new Set([ans, ...wrong])]; while (opts.length < 4) opts.push([1, 4, 6].map(d => K.names[d - 1]).join(' '));
    return { key, kind: 'choice', cols: 2, prompt: ['C E G in C major, transposed to ' + key + ' major, is…', 'C장조의 C E G를 ' + key + '장조로 이조하면…'], opts: shuffle(opts.slice(0, 4)).map(x => ({ id: x, label: x })), ans, ok: (v) => v === ans,
      fig: (c) => ({ kb: c.res ? chqKb(T.map(d => K.k + IVQ_SCALE[d - 1]), { ks: [K.k, K.k + 12], base: chqScaleBase(key), words: ['1', '3', '5'] }) : ivqKb({ ks: [K.k, K.k + 12], marks: chqScaleBase(key) }) }),
      yes: ['Notes 1, 3 and 5 of ' + key + ' major: ' + ans + '.', key + '장조의 1, 3, 5번 음: ' + ans + '.'], no: ['C E G are notes 1, 3 and 5. In ' + key + ' major they are ' + ans + (ans.includes('♯') || ans.includes('♭') ? ': the key signature comes too.' : '.'), 'C E G는 1, 3, 5번 음이에요. ' + key + '장조에서는 ' + ivqJ(ans, '이에요', '예요') + '.' + (ans.includes('♯') || ans.includes('♭') ? ' 조표도 함께 와요.' : '')] }; },
};

// ── The pentatonic scale: a major scale without notes 4 and 7
const pgPenta = (key) => { const K = IVQ_KEYS[key], d = [1, 2, 3, 5, 6]; return { keys: d.map(x => K.k + IVQ_SCALE[x - 1]), names: d.map(x => K.names[x - 1]), out: [4, 7].map(x => K.k + IVQ_SCALE[x - 1]), outN: [4, 7].map(x => K.names[x - 1]) }; };
const pgPentaKb = (key, o = {}) => { const P = pgPenta(key), K = IVQ_KEYS[key], m = {}, names = {}, ncol = {};
  P.keys.forEach((k, j) => { m[k] = 'pick'; names[k] = String([1, 2, 3, 5, 6][j]); ncol[k] = KQ.COD; }); if (o.out) P.out.forEach((k, j) => { names[k] = String([4, 7][j]); ncol[k] = '#9a9cc2'; });
  return ivqKb({ ks: [K.k, K.k + 12], marks: m, names, ncol }); };
const pgPentaCap = (key) => ivqCap(kqT([key + ' major pentatonic: ' + pgPenta(key).names.join(' '), key + '장조 5음 음계: ' + pgPenta(key).names.join(' ')]), KQ.COD);
const PG_BLACK = [1, 3, 6, 8, 10];
PG_SPEC['sc-penta'] = {
  title: ['The pentatonic scale', '5음 음계'], allLine: ['Five notes: take a major scale and leave out notes 4 and 7. C major pentatonic is C D E G A.', '음이 다섯 개인 음계예요. 장음계에서 4번 음과 7번 음을 빼요. C장조 5음 음계는 C D E G A예요.'],
  fig: () => ({ mid: chqPlayBtn(pgPenta('C').keys), kb: pgPentaKb('C', { out: true }), below: pgPentaCap('C') }),
  steps: [
    { title: ['Leave out 4 and 7', '4번과 7번을 빼요'], line: ['C major without F and B: C D E G A. No two notes are a half step apart.', 'C장음계에서 F와 B를 빼면 C D E G A예요. 반음으로 붙은 음이 하나도 없어요.'], fig: () => ({ kb: pgPentaKb('C', { out: true }), mid: chqPlayBtn(pgPenta('C').keys) }) },
    { title: ['The black keys', '검은건반'], line: ['The five black keys make a pentatonic scale on their own: G♭ A♭ B♭ D♭ E♭.', '검은건반 다섯 개만으로도 5음 음계가 돼요. G♭ A♭ B♭ D♭ E♭.'], fig: () => ({ kb: ivqKb({ ks: [0, 12], marks: Object.fromEntries(PG_BLACK.map(k => [k, 'pick'])) }), mid: chqPlayBtn([6, 8, 10, 13, 15]) }) },
    { title: ['The minor pentatonic', '단조 5음 음계'], line: ['Start the same five notes on A: A C D E G. That is A minor pentatonic.', '같은 다섯 음을 A에서 시작해요. A C D E G. A단조 5음 음계예요.'], fig: () => ({ kb: ivqKb({ ks: [9, 21], marks: { 9: 'pick', 12: 'pick', 14: 'pick', 16: 'pick', 19: 'pick' }, names: { 9: 'A' }, ncol: { 9: KQ.COD } }), mid: chqPlayBtn([9, 12, 14, 16, 19]) }) },
  ],
  make: (n, prev) => { const kind = n % 3; let key, g = 0; do { key = kqPick(['C', 'G', 'F', 'D']); } while (prev && prev.key === key && g++ < 8); const P = pgPenta(key), K = IVQ_KEYS[key];
    if (kind === 0) return { key, kind: 'multi', retry: true, targets: P.keys, prompt: ['Tap the five notes of ' + key + ' major pentatonic. The major scale is marked.', key + '장조 5음 음계의 다섯 음을 눌러 보세요. 장음계가 표시돼 있어요.'], prog: (a, b) => ['Found ' + a + ' of ' + b + '. Keep going.', b + '개 중 ' + a + '개를 찾았어요. 계속해요.'],
      fig: () => ({ kb: ivqKb({ ks: [K.k, K.k + 12], marks: chqScaleBase(key) }) }), yes: [key + ' major pentatonic: ' + P.names.join(' ') + '.', key + '장조 5음 음계: ' + P.names.join(' ') + '.'],
      no: () => ['Leave out notes 4 and 7, ' + P.outN.join(' and ') + '. Tap the other five.', '4번 음 ' + ivqJ(P.outN[0], '과', '와') + ' 7번 음 ' + ivqJ(P.outN[1], '은', '는') + ' 빼요. 나머지 다섯 개를 눌러요.'] };
    if (kind === 1) { const ans = P.outN.join(', '), opts = shuffle([...new Set([ans, [3, 7].map(x => K.names[x - 1]).join(', '), [4, 6].map(x => K.names[x - 1]).join(', '), [2, 5].map(x => K.names[x - 1]).join(', ')])]);
      return { key, kind: 'choice', cols: 2, prompt: ['Which two notes of ' + key + ' major are left out of its pentatonic scale?', key + '장음계에서 5음 음계를 만들 때 빼는 두 음은?'], opts: opts.map(x => ({ id: x, label: x })), ans, ok: (v) => v === ans,
        fig: (c) => ({ kb: c.res ? pgPentaKb(key, { out: true }) : ivqKb({ ks: [K.k, K.k + 12], marks: chqScaleBase(key) }) }), yes: ['Notes 4 and 7: ' + ans + '.', '4번 음과 7번 음: ' + ans + '.'], no: ['Always notes 4 and 7. In ' + key + ' major they are ' + ans + '.', '언제나 4번 음과 7번 음을 빼요. ' + key + '장조에서는 ' + ivqJ(ans, '이에요', '예요') + '.'] }; }
    const ans = P.names.join(' '), all = ['C', 'G', 'F', 'D'].map(x => pgPenta(x).names.join(' ')), w1 = [1, 2, 3, 4, 5].map(x => K.names[x - 1]).join(' '), opts = shuffle([...new Set([ans, w1, ...shuffle(all.filter(x => x !== ans)).slice(0, 2)])]).slice(0, 4);
    if (!opts.includes(ans)) opts[0] = ans;
    return { key, kind: 'choice', cols: 1, prompt: [key + ' major pentatonic is…', key + '장조 5음 음계는…'], opts: shuffle(opts).map(x => ({ id: x, label: x })), ans, ok: (v) => v === ans, onPick: () => chqPlay(P.keys, 'broken'),
      fig: (c) => ({ kb: c.res ? pgPentaKb(key, { out: true }) : ivqKb({ ks: [K.k, K.k + 12], marks: chqScaleBase(key) }) }), yes: [ans + ': notes 1 2 3 5 6.', ans + ': 1 2 3 5 6번 음이에요.'], no: ['Notes 1 2 3 5 6 of ' + key + ' major: ' + ans + '.', key + '장음계의 1 2 3 5 6번 음: ' + ivqJ(ans, '이에요', '예요') + '.'] }; },
};

const PG_ROWS = [
  ['p-keysig', ['Key signatures', '조표'], 'kf-write', 'Write a key signature', '조표 쓰기', 'Each sign in its order, on its own line or space.', '정해진 순서대로, 정해진 줄이나 칸에.'],
  ['p-keysig', ['Key signatures', '조표'], 'kf-trans', 'Transposing', '이조', 'The same scale numbers in another key.', '다른 조에서 같은 음계 번호로.'],
  ['p-scale', ['Scales', '스케일'], 'sc-penta', 'The pentatonic scale', '5음 음계', 'A major scale without notes 4 and 7.', '장음계에서 4번과 7번 음을 빼요.'],
];
PG_ROWS.forEach(([concept, cn, id, en, ko, benEn, bko]) => {
  TOOLS.push({ id, ch: 'concept', title: en, blurb: benEn, hidden: true, get kicker() { return TOOL_AREAS.find(a => a.id === 'pitch').name + ' · ' + kqT(cn); }, C: () => <KqEngine spec={PG_SPEC[id]}/> });
  TOOL_KO[id] = [ko, bko];
  const tl = TOOLS[TOOLS.length - 1], k = TOOL_KO[id], ti = tl.title, bl = tl.blurb; tl.titleEn = ti; tl.blurbEn = bl;
  Object.defineProperty(tl, 'title', { get: () => (LANG === 'ko' ? k[0] : ti), enumerable: true, configurable: true });
  Object.defineProperty(tl, 'blurb', { get: () => (LANG === 'ko' ? k[1] : bl), enumerable: true, configurable: true });
  TOOL_CONCEPT[id] = concept;
});
