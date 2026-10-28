import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)

# Build CQ (call 24, her 18:11: mark C, 'a small tag at the end'): Theory of Music content carries a small 'T1'..'T6'.
# On the Home: a navy tag at the end of a lesson's line. In the house: an outlined tag in the room's corner; the room's
# card says 'Theory Grade N'. The grades come from the Syllabus check tabs (Theory of Music Grades 1 to 3), the Grade 4
# check and the rooms built for Theory Grades 4 to 6. A room's tag is the grade most of it teaches; a lesson's tag is its
# own grade (its floor mark from Grade 2 up, otherwise its room's). No tag on practical lessons (fingering, playing,
# listening), on aural and technique rooms, on the things to make, or on what Theory of Music does not ask (modes, the
# alto clef, 8va, the pedal, swing, the fugue). The student's own theory grade and the checkpoint filter wait for the
# dashboard (call 8).
CODE = r"""
// ══ Build CQ: the Theory mark (call 24, mark C) ══
const THEORY_ROOM = { 'note-values': 1, dynamics: 1, staff: 1, 'whole-staff': 1, 'time-signatures': 1, tones: 1,
  tempo: 1, rhythm: 1, 'ledger-lines': 1, scales: 1, 'minor-scales': 2, signs: 2,
  accidentals: 1, 'key-signatures': 1, terms: 1, 'six-eight': 2, intervals: 1, chords: 1, form: 2,
  melody: 2, 'harmony-23': 3, 'rhythm-23': 3, 'keys-4': 4, 'harmony-4': 4, 'rhythm-4': 4, 'keys-5': 5, 'harmony-5': 5, 'harmony-6': 6,
  'piano-story': 0, 'pitch-range': 0, composers: 0, styles: 0 };   // 0: only the lessons marked Grade 4 to 6 (the strings, the dances, the woodwinds, the brass, the genres)
const THEORY_LESSON = { 'term-cards': 2, 'term-match': 2, 'term-mixer': 2, 'term-sort': 2, 'rp-dot': 2, 'rm-68': 2, 'kf-minor': 2, 'rm-sync': 4, 'ac-double': 4,
  'sc-wr': 0, 'sc-wl': 0, 'sc-br': 0, 'sc-bl': 0, 'sc-both': 0, 'sc-chrom': 0, 'ch-hands': 0, 'ch-ear': 0, 'iv-ear': 0, 'ms-ear': 0, 'ac-play': 0,
  'stm-sf': 0, 'stm-metro': 0, 'stm-steady': 0, 'stm-read': 0, 'rp-read': 0, 'e8-read': 0, 'rm-swing': 0, 'fmx-fugue': 0, 'pedal': 0 };
let _thRoomOf = null;
function theoryRoomOf(id) {
  if (!_thRoomOf) { _thRoomOf = {}; Object.values(HOME_LIVE).forEach(v => { (v.lessons || []).forEach(x => { if (v.check && !_thRoomOf[x]) _thRoomOf[x] = v.check; }); (v.groups || []).forEach(g => g.lessons.forEach(x => { if (g.check && !_thRoomOf[x]) _thRoomOf[x] = g.check; })); }); }
  if (_thRoomOf[id]) return _thRoomOf[id];
  const tl = TOOLS.find(x => x.id === id); return tl && THEORY_ROOM[tl.ch] !== undefined ? tl.ch : null;
}
function theoryOf(id) {
  if (!id || /^mk-/.test(id)) return null;
  if (THEORY_LESSON[id] !== undefined) return THEORY_LESSON[id] || null;
  const room = theoryRoomOf(id); if (!room || THEORY_ROOM[room] === undefined) return null;
  const fl = HOME_FLOOR[id], n = { '2': 2, '3': 3, '4': 4, '5': 5, '6': 6 }[fl];
  if (n) return n;
  if (!THEORY_ROOM[room] || !fl || fl === '23' || fl === '7' || fl === '8' || fl === 'home') return null;
  return THEORY_ROOM[room];
}
const theoryName = (n) => t('Theory Grade ' + n, '이론 ' + n + '급');
function TheoryTag({ id }) {
  const n = theoryOf(id); if (!n) return null;
  return <span data-theory={n} title={theoryName(n)} aria-label={theoryName(n)} style={{flex:'none',alignSelf:'center',fontSize:11.5,fontWeight:800,lineHeight:1,color:'#fffefa',background:'var(--navy)',borderRadius:4,padding:'4px 5px 3px',letterSpacing:'0.02em',fontVariantNumeric:'lining-nums'}}>{'T' + n}</span>;
}
"""
rep("""const HOME_FLOOR_NAME = {""", CODE + """const HOME_FLOOR_NAME = {""")
# the Home: the tag at the end of the line
rep("""      <span style={{flex:1,minWidth:0,display:'block'}}><span style={homeTitle}>{title}</span><span style={homeSub}>{fid && <FloorMark id={fid}/>}{line}</span></span>
      <HomeChev on/>""", """      <span style={{flex:1,minWidth:0,display:'block'}}><span style={homeTitle}>{title}</span><span style={homeSub}>{fid && <FloorMark id={fid}/>}{line}</span></span>
      {fid && <TheoryTag id={fid}/>}
      <HomeChev on/>""")
# the house: an outlined tag in the room's lower left corner (the check's star is in the right)
rep("""  const star = view.star && view.star[id];   // Build CN: the chapter check passed""", """  const star = view.star && view.star[id];   // Build CN: the chapter check passed
  const thn = THEORY_ROOM[id];   // Build CQ: the Theory mark
  if (thn) { const tw = cmp ? 17 : 21, th = cmp ? 10 : 12, tx = x + (cmp ? 5 : 8), ty = y + h - 6 - (cmp ? 14 : 17);
    s += '<rect x="' + pFix(tx) + '" y="' + pFix(ty) + '" width="' + tw + '" height="' + th + '" rx="' + (th / 2) + '" fill="#fff" stroke="' + ST.N + '" stroke-width="0.9"/>' + stT(tx + tw / 2, ty + th - (cmp ? 2.4 : 2.8), 'T' + thn, { size: cmp ? 7.2 : 8.6, weight: 800, fill: ST.N, anchor: 'middle' }); }""")
rep("""(star ? t(', check passed', ', 체크 통과') : '');""", """(star ? t(', check passed', ', 체크 통과') : '') + (thn ? ', ' + theoryName(thn) : '');""")
# the room's card: 'Theory Grade N' after the floor
rep("""          <div style={{fontSize:12,fontWeight:800,color:BK.muted,marginTop:2}}>{floor}{steps.length ?""", """          <div style={{fontSize:12,fontWeight:800,color:BK.muted,marginTop:2}}>{floor}{THEORY_ROOM[id] ? ' · ' + theoryName(THEORY_ROOM[id]) : ''}{steps.length ?""")
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
