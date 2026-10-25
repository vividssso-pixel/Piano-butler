import sys, os
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
here = os.path.dirname(os.path.abspath(__file__))
MS = open(os.path.join(here, 'msx.jsx'), encoding='utf-8').read()
MSH = open(os.path.join(here, 'msh.jsx'), encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)

# Build AC (the board's call 6, settled by the syllabus: a minor scales room on Prelim - Grade 1): Minor Scales, after Key
# Signatures. The Grade 1 theory: a major or a minor third; the minor that shares a key signature (A, E, D, G minor); the harmonic
# minor's raised 7th beside the note; tones, semitones and the tone and a half; a major or a harmonic minor scale by ear. On the
# Home, Pitch -> Scales gets three groups: major scales, minor scales (the room's five lessons and 'Three kinds of minor'), more.
rep("""const SCALE_PLAY_DRILL = { id: 'scale-play', label: 'Playing Scales' };""",
    """const SCALE_PLAY_DRILL = { id: 'scale-play', label: 'Playing Scales' };
const MINOR_SCALES_DRILL = { id: 'minor-scales', label: 'Minor Scales' };   // Build AC: its lessons and questions with its Lesson Book (msLbPages)""")
rep("""  { id: 'key-signatures', label: 'Key Signatures', concept: KEYSIG_DRILL, track: 'pitch' },""",
    """  { id: 'key-signatures', label: 'Key Signatures', concept: KEYSIG_DRILL, track: 'pitch' },
  { id: 'minor-scales', label: 'Minor Scales', concept: MINOR_SCALES_DRILL, track: 'pitch' },   // Build AC""")
rep("""'key-signatures': '조표', """, """'key-signatures': '조표', 'minor-scales': '단음계', """)
rep("""'key-signatures': ['Key signatures', '조표'],""", """'key-signatures': ['Key signatures', '조표'], 'minor-scales': ['Minor scales', '단음계'],""")
rep("""const HOUSE_ICONS = {"scale-play": """, """const HOUSE_ICONS = {"minor-scales": "<path d=\\"M4 31 H11 V26 H18 V21 H25 V16 H32 V11\\"/><path d=\\"M32 11 V4 H39\\" stroke=\\"#e4572e\\"/><path d=\\"M39 4 V2 H44\\"/>", "scale-play": """)
rep("""  'key-signatures': 'key signature sharps flats G major F major D major B flat major order of sharps flats circle of fifths relative minor transpose',""",
    """  'key-signatures': 'key signature sharps flats G major F major D major B flat major order of sharps flats circle of fifths relative minor transpose',
  'minor-scales': 'minor scale minor key harmonic natural relative key signature raised seventh tone and a half major third minor third A minor E minor D minor G minor',""")
rep("""'key-signatures': ['scales', 'accidentals'],""", """'key-signatures': ['scales', 'accidentals'], 'minor-scales': ['key-signatures', 'scale-play'],""")
rep("""'key-signatures': 'p-scales', """, """'key-signatures': 'p-scales', 'minor-scales': 'p-scales', """)
rep("""'p-scales': ['scales', 'key-signatures']""", """'p-scales': ['scales', 'key-signatures', 'minor-scales']""")
rep("""{ ids: ['key-signatures', 'signs', 'intervals', 'chords', 'terms', 'form'], en: ['Prelim – Grade 1', 'Key signatures, signs, intervals and chords, the words for how to play, and how a piece is built.'], ko: ['Prelim – Grade 1', '조표, 기호, 음정과 화음, 음악 용어, 그리고 곡의 짜임.'] }""",
    """{ ids: ['key-signatures', 'minor-scales', 'signs', 'intervals', 'chords', 'terms', 'form'], en: ['Prelim – Grade 1', 'Key signatures and minor scales, signs, intervals and chords, the words for how to play, and how a piece is built.'], ko: ['Prelim – Grade 1', '조표와 단음계, 기호, 음정과 화음, 음악 용어, 그리고 곡의 짜임.'] }""")
rep("""
// ─── Chapter 2: Keyboard Patterns (Phase 387""", MS + """
// ─── Chapter 2: Keyboard Patterns (Phase 387""")
rep("""'scale-play': ScalePlayLessonBook,""", """'scale-play': ScalePlayLessonBook, 'minor-scales': MinorScalesLessonBook,""")
rep("""'scale-play': spLbPages,""", """'scale-play': spLbPages, 'minor-scales': msLbPages,""")
rep("""  'p-scale': {
    lessons: ['sc-shape', 'sc-same', 'sc-deg', 'sc-wr', 'sc-wl', 'sc-br', 'sc-bl', 'sc-all', 'sc-chrom', 'sc-min', 'sc-penta'], check: 'scales', tools: ['scale-finder'], more: [],
    tryLine: ['Turn the circle of fifths to any key', '5도권을 돌려 어느 조든 찾아요'],
    checkLine: ['Questions, level by level', '문제를 단계별로'],
  },""", """  'p-scale': { lessons: [], groups: [   // Build AC: major, minor, more
    { id: 'psc-major', en: 'Major scales', ko: '장음계', lessons: ['sc-shape', 'sc-same', 'sc-deg', 'sc-wr', 'sc-wl', 'sc-br', 'sc-bl', 'sc-all', 'sc-chrom'], check: 'scales' },
    { id: 'psc-minor', en: 'Minor scales', ko: '단음계', lessons: ['ms-third', 'ms-rel', 'ms-har', 'ms-gaps', 'ms-ear', 'sc-min'], check: 'minor-scales' },
    { id: 'psc-more', en: 'More scales', ko: '더 많은 음계', lessons: ['sc-penta'] },
  ], tools: ['scale-finder'], more: [],
    tryLine: ['Turn the circle of fifths to any key', '5도권을 돌려 어느 조든 찾아요'],
  },""")
rep("""  set('P1', 'sp-turn sp-beat sp-minor sp-mirror sp-two');   // Build AB""", """  set('P1', 'sp-turn sp-beat sp-minor sp-mirror sp-two');   // Build AB
  set('P1', 'ms-third ms-rel ms-har ms-gaps ms-ear');   // Build AC""")
rep("""lbhAdd('rb-finger', 'r-beat', 'rhythm', 'The beat in your fingers',""", MSH + """
lbhAdd('rb-finger', 'r-beat', 'rhythm', 'The beat in your fingers',""")

open(dst, 'w', encoding='utf-8').write(s)
print('ok')
