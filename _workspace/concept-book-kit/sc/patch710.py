import sys, re
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)

# Build AQ (Sohyun 26 Oct 22:35: "음악이야기에 스타일, 작곡가, 자잘 악기 관련 다 넣어줘. 여기저기 흩어지지 않게. 중복된 건 더 잘
# 만들어진 걸로 남기든 정리하든 새로 만들든 하자"). Stories of music becomes the one place for the piano, instruments, composers
# and styles:
# - The attic's room (pitch-range: high and low, big is low, the instrument families, the violin family, ranges, with Hz and
#   the octave ladder) moves into the Stories of music storey as 'Instruments', after the piano. The attic goes (it held only
#   this room). This changes the 25 Oct call 'Pitch, Hz & range to the attic', at her word.
# - Scattered pieces come home, the better one kept: the Home's 'Pitch and range' topic (Long and short; How far a piano
#   reaches) gives way to the Instruments steps that do the same with more instruments and a quiz (Big is low, small is
#   high; Ranges on the keys); the 12-bar blues in Chords and the pentatonic scale in Scales give way to the Styles steps
#   (Blues and swing, with the chords and swing; Five notes, with 4 and 7 left out, the black keys and a tune); Straight or
#   swing? (read it and tap it) moves from Rhythm into the Styles room beside Blues and swing; Which style? leaves the
#   Aural room's extras (it is a Styles step); the piano's pedals step leaves the Touch room (the Touch room keeps its own
#   pedalling lesson).
# - The planned 'more-scales' room (pentatonic, blues, whole-tone, modes) is dropped from the Grades 2-3 floor: pentatonic and
#   blues are in Styles, the modes have their own Home topic.

# ── the house ──
rep("""  { ids: ['melody', 'listen-23', 'scales-23', 'harmony-23', 'rhythm-23', 'more-scales'], en:""",
    """  { ids: ['melody', 'listen-23', 'scales-23', 'harmony-23', 'rhythm-23'], en:""")
rep("""  { ids: ['piano-story', 'composers', 'styles'], stories: true, th: { wp: 'drape', fl: 'boards', lamp: 'candelabrum' }, en: ['Stories of music', 'Rooms to visit any time: the piano’s own story, composers through time, and styles.'], ko: ['음악 이야기', '언제든 들어가는 방: 피아노 이야기, 시대별 작곡가,""",
    """  { ids: ['piano-story', 'pitch-range', 'composers', 'styles'], stories: true, th: { wp: 'drape', fl: 'boards', lamp: 'candelabrum' }, en: ['Stories of music', 'Rooms to visit any time: the piano’s own story, the instruments, composers through time, and styles.'], ko: ['음악 이야기', '언제든 들어가는 방: 피아노 이야기, 악기, 시대별 작곡가,""")
m = re.search(r"\n  \{ ids: \['pitch-range'\], attic: true, [^\n]*\n", s)
assert m, 'attic'
s = s[:m.start()] + "\n   // Build AQ: the attic's room moved into Stories of music (as Instruments); the attic is gone\n" + s[m.end():]

# ── the room's name: Instruments ──
rep("""  id: 'pitch-range', label: 'Pitch, Hz & Range', levels: PITCH_LEVELS,""", """  id: 'pitch-range', label: 'Instruments', levels: PITCH_LEVELS,""")
rep("""  { id: 'pitch-range', label: 'Pitch, Hz & Range', concept: PITCH_RANGE_DRILL, track: 'pitch' },""", """  { id: 'pitch-range', label: 'Instruments', concept: PITCH_RANGE_DRILL, track: 'pitch' },   // Build AQ: was 'Pitch, Hz & Range'""")
rep("""'pitch-range': '음높이, 헤르츠와 음역',""", """'pitch-range': '악기',""")
rep("""'pitch-range': ['Pitch', '음높이'],""", """'pitch-range': ['Instruments', '악기'],""")
rep("""  'dynamics': 't-touch', 'tempo': 't-tempo', 'terms': 't-tempo', 'pitch-range': 'p-staff',""", """  'dynamics': 't-touch', 'tempo': 't-tempo', 'terms': 't-tempo', 'pitch-range': 'about',""")
rep("""const CAT_CHAPTER_ORDER = { 'p-staff': ['first-steps', 'note-names', 'staff', 'whole-staff', 'ledger-lines', 'pitch-range'],""",
    """const CAT_CHAPTER_ORDER = { 'p-staff': ['first-steps', 'note-names', 'staff', 'whole-staff', 'ledger-lines'],""")
rep("""about: ['piano-story', 'composers', 'styles'] };""", """about: ['piano-story', 'pitch-range', 'composers', 'styles'] };""")
rep("""when: 'Black-key groups, A to G, the staff and its clefs, landmarks, ledger lines and 8va, high and low and why', color: '#e4572e' },""",
    """when: 'Black-key groups, A to G, the staff and its clefs, landmarks, ledger lines and 8va', color: '#e4572e' },""")
rep("""  'p-staff': ['건반과 오선', '검은건반 무리, A부터 G까지, 오선과 음자리표, 기준 음, 덧줄과 8va, 높고 낮은 소리와 그 까닭'],""",
    """  'p-staff': ['건반과 오선', '검은건반 무리, A부터 G까지, 오선과 음자리표, 기준 음, 덧줄과 8va'],""")
for tid in ['csx-blues', 'csx-penta', 'hz-explorer', 'octave-ladder', 'spr-big', 'spr-zone', 'sps-keys', 'sps-pedals', 'string-lab']:
    m = re.findall(r"'" + re.escape(tid) + r"': '(?:p-chords|p-scales|p-staff|t-touch)'", s)
    assert len(m) == 1, (tid, m)
    s = s.replace(m[0], "'" + tid + "': 'about'")

# ── the Home: one Stories door with four rooms; the scattered twins leave their other rooms ──
rep("""    { id: 'ab-piano', en: 'The piano’s story', ko: '피아노 이야기', lessons: CHAPTER_TOOL_ORDER['piano-story'].slice(), check: 'piano-story' },""",
    """    { id: 'ab-piano', en: 'The piano’s story', ko: '피아노 이야기', lessons: CHAPTER_TOOL_ORDER['piano-story'].slice(), check: 'piano-story' },
    { id: 'ab-inst', en: 'Instruments', ko: '악기', lessons: CHAPTER_TOOL_ORDER['pitch-range'].slice(), check: 'pitch-range' },   // Build AQ: from the attic""")
rep("""    { id: 'ab-styles', en: 'Styles', ko: '스타일', lessons: CHAPTER_TOOL_ORDER.styles.slice(), check: 'styles' },""",
    """    { id: 'ab-styles', en: 'Styles', ko: '스타일', lessons: CHAPTER_TOOL_ORDER.styles.flatMap(x => x === 'csx-blues' ? [x, 'rm-swing'] : [x]), check: 'styles' },   // Build AQ: Straight or swing? from Rhythm, beside Blues and swing""")
rep("""    { id: 'p-range', en: 'Pitch and range', ko: '음높이와 음역', lessons: ['kq-size', 'kq-range'], check: 'pitch-range' },
""", """""")
rep("""    { id: 'ch-more', en: 'More chords', ko: '더 많은 화음', lessons: ['ch-ext', 'ch-blues'] },""",
    """    { id: 'ch-more', en: 'More chords', ko: '더 많은 화음', lessons: ['ch-ext'] },   // Build AQ: the 12-bar blues is a Styles step""")
rep("""    { id: 'psc-more', en: 'More scales', ko: '더 많은 음계', lessons: ['sc-penta'] },
""", """""")
rep("""    { id: 'rb-more', en: 'More rhythm', ko: '더 나아가는 리듬', lessons: ['rm-semi', 'rm-trip', 'rm-68', 'rm-cut', 'rm-sync', 'rm-swing'], check: 'time-signatures', level: 9 },""",
    """    { id: 'rb-more', en: 'More rhythm', ko: '더 나아가는 리듬', lessons: ['rm-semi', 'rm-trip', 'rm-68', 'rm-cut', 'rm-sync'], check: 'time-signatures', level: 9 },   // Build AQ: swing went to Styles""")
rep("""    { id: 't-pedal', en: 'The pedals', ko: '페달', lessons: ['sps-pedals', 'pedal'] },""",
    """    { id: 't-pedal', en: 'The pedals', ko: '페달', lessons: ['pedal'] },   // Build AQ: the piano's pedals are a Stories step""")
rep("""    { id: 'au-more', en: 'More listening', ko: '더 듣기', lessons: ['hear-find', 'echo', 'touch-ear', 'ch-ear', 'iv-mh', 'iv-ear', 'csx-ear'] },""",
    """    { id: 'au-more', en: 'More listening', ko: '더 듣기', lessons: ['hear-find', 'echo', 'touch-ear', 'ch-ear', 'iv-mh', 'iv-ear'] },   // Build AQ: Which style? is a Styles step""")
# Straight or swing? now sits in Styles: its kicker and concept follow
rep("""  TOOL_CONCEPT[id] = 'r-beat';
});

// ─── Technique on the Home""", """  TOOL_CONCEPT[id] = id === 'rm-swing' ? 'about' : 'r-beat';
  if (id === 'rm-swing') Object.defineProperty(tl, 'kicker', { get: () => t('Stories of music · Styles', '음악 이야기 · 스타일'), enumerable: true, configurable: true });   // Build AQ
});

// ─── Technique on the Home""")

# the chapter's own title on its opener and its screen lesson
s2 = s
rep("""        <div style={{fontFamily:LB_SERIF,fontSize:44,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{t('Pitch, Hz & Range', '음높이, 헤르츠와 음역')}</div>""",
    """        <div style={{fontFamily:LB_SERIF,fontSize:44,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{bkChapterName('pitch-range')}</div>""")
rep("""    <Lesson id="pitch-range" title={t('Pitch, Hz & Range', '음높이, 헤르츠와 음역')} onStart={onStart} noArt""",
    """    <Lesson id="pitch-range" title={bkChapterName('pitch-range')} onStart={onStart} noArt""")

open(dst, 'w', encoding='utf-8').write(s)
print('ok')
