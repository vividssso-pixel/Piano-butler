# Reference, chords (2026-11-01, her notes on the screenshot): (1) the triads on the staff drawn cleanly (real semibreve heads,
# room between the staff and the numerals); (2) every chord that exists in common use, in families, with compound intervals.
import sys
p = sys.argv[1]; h = open(p, encoding='utf-8').read()
def rep(o, n, c=1):
    global h
    k = h.count(o)
    if k != c: raise SystemExit("count %d != %d for %r" % (k, c, o[:100]))
    h = h.replace(o, n)
# (1) the staff
i = h.index("function RefChordStaff() {"); j = h.index("\n}\n", i) + 3
h = h[:i] + r'''function RefChordStaff() {   // the triad on every degree of C major: semibreves on a clean staff, the numerals well below it
  const base = 70, yOf = (d) => base - (d - 30) * 5, x0 = 66, dx = 46, roman = ['I', 'ii', 'iii', 'IV', 'V', 'vi', 'vii°'];
  const head = (x, y) => '<ellipse cx="' + x + '" cy="' + y + '" rx="7.2" ry="4.9" fill="' + PEN_N + '"/>' +
    '<ellipse cx="' + x + '" cy="' + y + '" rx="3.5" ry="2.3" transform="rotate(-38 ' + x + ' ' + y + ')" fill="#fff"/>';
  const right = x0 + dx * 6 + 22;
  let s = [0, 2, 4, 6, 8].map(p => '<line x1="4" x2="' + right + '" y1="' + (base - p * 5) + '" y2="' + (base - p * 5) + '" stroke="' + PEN_N + '" stroke-opacity="0.55" stroke-width="1.2"/>').join('');
  roman.forEach((r, i) => { const x = x0 + i * dx, root = 28 + i;
    if (root <= 28) s += '<line x1="' + (x - 12) + '" x2="' + (x + 12) + '" y1="' + yOf(28) + '" y2="' + yOf(28) + '" stroke="' + PEN_N + '" stroke-width="1.4"/>';
    [root, root + 2, root + 4].forEach(d => { s += head(x, yOf(d)); });
    s += '<text x="' + x + '" y="' + (base + 38) + '" text-anchor="middle" font-size="16" font-weight="900" font-family="Georgia, serif" fill="' + (i === 0 || i === 3 || i === 4 ? PEN_C : PEN_N) + '">' + r + '</text>'; });
  return <svg viewBox={'0 ' + (base - 56) + ' ' + (right + 6) + ' 102'} style={{width:'100%',maxWidth:440,display:'block',margin:'4px auto 6px'}} role="img" aria-label={t('The triad on every degree of C major, I to vii°', 'C장조 모든 음 위의 3화음, I부터 vii°까지')}>
    <ClefGlyph clef="treble" st="treble" yOf={yOf} ink={PEN_N}/><g dangerouslySetInnerHTML={{ __html: s }}/></svg>;
}
''' + h[j:]
# (2) the chord list, in families; compound intervals (9, 11, 13)
i = h.index("const REF_CHORDS = ["); j = h.index("];\n", i) + 3
h = h[:i] + r'''const REF_CHORDS = [   // [id, name en, name ko, symbol, letter steps, semitones, room, family]; the first eleven are the printed page
  ['maj', 'major', '장3화음', '', [0, 2, 4], [0, 4, 7], 'chords', 'tri'], ['min', 'minor', '단3화음', 'm', [0, 2, 4], [0, 3, 7], 'chords', 'tri'],
  ['dim', 'diminished', '감3화음', '°', [0, 2, 4], [0, 3, 6], 'harmony-5', 'tri'], ['aug', 'augmented', '증3화음', '+', [0, 2, 4], [0, 4, 8], 'listen-8', 'tri'],
  ['dom7', 'dominant 7th', '딸림7화음', '7', [0, 2, 4, 6], [0, 4, 7, 10], 'harmony-6', 'sev'], ['maj7', 'major 7th', '장7화음', 'maj7', [0, 2, 4, 6], [0, 4, 7, 11], 'chords', 'sev'],
  ['min7', 'minor 7th', '단7화음', 'm7', [0, 2, 4, 6], [0, 3, 7, 10], 'chords', 'sev'], ['hdim7', 'half-diminished', '반감7화음', 'm7♭5', [0, 2, 4, 6], [0, 3, 6, 10], 'chords', 'sev'],
  ['dim7', 'diminished 7th', '감7화음', '°7', [0, 2, 4, 6], [0, 3, 6, 9], 'arps-6', 'sev'], ['six', 'major 6th (added 6th)', '부가6화음', '6', [0, 2, 4, 5], [0, 4, 7, 9], null, 'add'],
  ['min6', 'minor 6th', '단 부가6화음', 'm6', [0, 2, 4, 5], [0, 3, 7, 9], null, 'add'],
  // more chords in common use (not taught in a room yet: 'extra')
  ['sus2', 'suspended 2nd', '서스2화음', 'sus2', [0, 1, 4], [0, 2, 7], null, 'sus'], ['sus4', 'suspended 4th', '서스4화음', 'sus4', [0, 3, 4], [0, 5, 7], null, 'sus'],
  ['pow', 'power chord (no 3rd)', '파워 코드(3음 없음)', '5', [0, 4], [0, 7], null, 'sus'], ['7sus4', 'dominant 7th, suspended 4th', '딸림7 서스4', '7sus4', [0, 3, 4, 6], [0, 5, 7, 10], null, 'sus'],
  ['mmaj7', 'minor-major 7th', '단장7화음', 'm(maj7)', [0, 2, 4, 6], [0, 3, 7, 11], null, 'sev'], ['aug7', 'augmented 7th', '증7화음', '+7', [0, 2, 4, 6], [0, 4, 8, 10], null, 'sev'],
  ['augmaj7', 'augmented major 7th', '증장7화음', '+maj7', [0, 2, 4, 6], [0, 4, 8, 11], null, 'sev'], ['7b5', 'dominant 7th, flat 5th', '딸림7 ♭5', '7♭5', [0, 2, 4, 6], [0, 4, 6, 10], null, 'sev'],
  ['add9', 'added 9th', '부가9화음', 'add9', [0, 2, 4, 8], [0, 4, 7, 14], null, 'add'], ['madd9', 'minor, added 9th', '단 부가9화음', 'm(add9)', [0, 2, 4, 8], [0, 3, 7, 14], null, 'add'],
  ['69', '6th and 9th', '6·9화음', '6/9', [0, 2, 4, 5, 8], [0, 4, 7, 9, 14], null, 'add'],
  ['dom9', 'dominant 9th', '딸림9화음', '9', [0, 2, 4, 6, 8], [0, 4, 7, 10, 14], null, 'ext'], ['maj9', 'major 9th', '장9화음', 'maj9', [0, 2, 4, 6, 8], [0, 4, 7, 11, 14], null, 'ext'],
  ['min9', 'minor 9th', '단9화음', 'm9', [0, 2, 4, 6, 8], [0, 3, 7, 10, 14], null, 'ext'], ['7b9', 'dominant 7th, flat 9th', '딸림7 ♭9', '7♭9', [0, 2, 4, 6, 8], [0, 4, 7, 10, 13], null, 'ext'],
  ['7s9', 'dominant 7th, sharp 9th', '딸림7 ♯9', '7♯9', [0, 2, 4, 6, 8], [0, 4, 7, 10, 15], null, 'ext'],
  ['dom11', 'dominant 11th', '딸림11화음', '11', [0, 2, 4, 6, 8, 10], [0, 4, 7, 10, 14, 17], null, 'ext'], ['min11', 'minor 11th', '단11화음', 'm11', [0, 2, 4, 6, 8, 10], [0, 3, 7, 10, 14, 17], null, 'ext'],
  ['7s11', 'dominant 7th, sharp 11th', '딸림7 ♯11', '7♯11', [0, 2, 4, 6, 10], [0, 4, 7, 10, 18], null, 'ext'],
  ['dom13', 'dominant 13th', '딸림13화음', '13', [0, 2, 4, 6, 8, 10, 12], [0, 4, 7, 10, 14, 17, 21], null, 'ext'], ['maj13', 'major 13th', '장13화음', 'maj13', [0, 2, 4, 6, 8, 10, 12], [0, 4, 7, 11, 14, 17, 21], null, 'ext'],
  ['min13', 'minor 13th', '단13화음', 'm13', [0, 2, 4, 6, 8, 10, 12], [0, 3, 7, 10, 14, 17, 21], null, 'ext'],
];
const REF_CHORD_FAM = [['tri', 'Triads', '3화음'], ['sus', 'Suspended and power chords', '서스 화음과 파워 코드'], ['sev', 'Sevenths', '7화음'], ['add', 'Sixths and added notes', '부가6·부가9화음'], ['ext', 'Ninths, elevenths, thirteenths', '9·11·13화음']];
const REF_CHORD_PAPER = 11;   // the printed book keeps its page: the first eleven
''' + h[j:]
rep("const refIvName = (st, se) => { const base = REF_NATPC[st], perf = [0, 3, 4].includes(st), d = se - base;",
    "const refIvName = (st, se) => { const base = REF_NATPC[st % 7] + 12 * Math.floor(st / 7), perf = [0, 3, 4].includes(st % 7), d = se - base;   // compound too: 9, 11, 13")
# the table, in families (the printed book: the first eleven in one table, as before)
i = h.index("    <RefTable k=\"chordtypes\""); j = h.index("    <RefNote>{t('M major, m minor", i)
old = h[i:j]
row_fn = old[old.index("rows={REF_CHORDS.map(") + len("rows={REF_CHORDS.map("): old.rindex(")}/>")]
new = '''    {(() => { const rowOf = ''' + row_fn + ''';
      const head = [t('Chord · symbol', '화음 · 기호'), t('From the root · on ', '근음에서 · ') + r, ''], cols = "minmax(0,1fr) minmax(0,1.1fr) auto";
      if (paper) return <RefTable k="chordtypes" cols={cols} head={head} rows={REF_CHORDS.slice(0, REF_CHORD_PAPER).map(rowOf)}/>;
      return REF_CHORD_FAM.map(([fam, en, ko], fi) => <div key={fam} data-ref-chordfam={fam} style={{marginTop: fi ? 10 : 0}}>
        <div style={{fontSize:11,fontWeight:900,color:BK.muted,letterSpacing:'0.06em',textTransform:'uppercase',margin:'0 2px 4px'}}>{t(en, ko)}</div>
        <RefTable k={'chordtypes-' + fam} cols={cols} head={fi === 0 ? head : null} rows={REF_CHORDS.filter(c => c[7] === fam).map(rowOf)}/></div>); })()}
'''
h = h[:i] + new + h[j:]
rep("    <RefNote>{t('M major, m minor, P perfect, A augmented, d diminished: each counted from the root.', 'M 장, m 단, P 완전, A 증, d 감: 모두 근음에서 센 음정.')}",
    "    <RefNote>{t('M major, m minor, P perfect, A augmented, d diminished: each counted from the root. 9, 11 and 13 are the 2nd, 4th and 6th an octave higher; in an 11th chord the 3rd is often left out, in a 13th the 11th.', 'M 장, m 단, P 완전, A 증, d 감: 모두 근음에서 센 음정. 9·11·13도는 한 옥타브 위의 2·4·6도; 11화음에서는 3음을, 13화음에서는 11음을 흔히 빼요.')}")
open(p, 'w', encoding='utf-8').write(h); print('m7 ok')
