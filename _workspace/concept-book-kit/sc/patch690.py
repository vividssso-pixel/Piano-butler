import sys, os
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
here = os.path.dirname(os.path.abspath(__file__))
SP = open(os.path.join(here, 'spx.jsx'), encoding='utf-8').read()
SPH = open(os.path.join(here, 'sph.jsx'), encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)

# Build AB (the syllabus check, 26 Oct; the build order sent to her): Playing Scales, the technique room after Scales on the
# Prelim - Grade 1 floor. The Scales room says which fingers; this one plays them: smooth turns, one note a beat, A and E minor
# (natural, harmonic), contrary motion as mirror twins, two octaves hands together (Grade 1). Fingerings and speeds checked
# against the technical work book pages. On the Home its five lessons open the Technique door's 'Playing scales and chords'.
rep("""const LISTEN_DRILL = { id: 'listen-sing', label: 'Listen and Sing', noPrint: true };""",
    """const LISTEN_DRILL = { id: 'listen-sing', label: 'Listen and Sing', noPrint: true };
const SCALE_PLAY_DRILL = { id: 'scale-play', label: 'Playing Scales' };   // Build AB: its lessons and questions with its Lesson Book (spLbPages)""")
rep("""  { id: 'scales', label: 'Scales', concept: SCALES_DRILL, track: 'pitch' },""",
    """  { id: 'scales', label: 'Scales', concept: SCALES_DRILL, track: 'pitch' },
  { id: 'scale-play', label: 'Playing Scales', concept: SCALE_PLAY_DRILL, track: 'start' },   // Build AB""")
rep("""'scales': '스케일', 'accidentals'""", """'scales': '스케일', 'scale-play': '스케일 치기', 'accidentals'""")
rep("""'scales': ['Scales', '스케일'],""", """'scales': ['Scales', '스케일'], 'scale-play': ['Playing scales', '스케일 치기'],""")
rep("""const HOUSE_ICONS = {"listen-sing": """, """const HOUSE_ICONS = {"scale-play": "<path d=\\"M4 31 H12 V25 H20 V19 H28 V13 H36 V7 H44\\"/><path d=\\"M9 21 Q15 33 25 19\\" stroke=\\"#e4572e\\"/><path d=\\"M20 19.5 L25 19 L25.5 24\\" stroke=\\"#e4572e\\"/>", "listen-sing": """)
rep("""  'scales': 'scale major minor fingering octave degree mode',""",
    """  'scales': 'scale major minor fingering octave degree mode',
  'scale-play': 'playing scales technique thumb under 3 over turn smooth bumpy beat metronome minor natural harmonic contrary motion mirror twins two octaves hands together',""")
rep("""scales: ['tones'], """, """scales: ['tones'], 'scale-play': ['scales'], """)
rep("""'scales': 'p-scales', """, """'scales': 'p-scales', 'scale-play': 'k-play', """)
rep("""  { ids: ['tempo', 'rhythm', 'ledger-lines', 'scales', 'accidentals', 'piano-story'], en: ['Prelim – Grade 1', 'Speed, quavers and dots, ledger lines, scales, accidentals, and the piano’s own story.'], ko: ['Prelim – Grade 1', '빠르기, 8분음표와 점, 덧줄, 스케일, 임시표, 그리고 피아노 이야기.'] },""",
    """  { ids: ['tempo', 'rhythm', 'ledger-lines', 'scales', 'scale-play', 'accidentals', 'piano-story'], en: ['Prelim – Grade 1', 'Speed, quavers and dots, ledger lines, scales and how to play them, accidentals, and the piano’s own story.'], ko: ['Prelim – Grade 1', '빠르기, 8분음표와 점, 덧줄, 스케일과 스케일 치기, 임시표, 그리고 피아노 이야기.'] },   // Build AB: Playing Scales""")
rep("""
// ─── Chapter 2: Keyboard Patterns (Phase 387""", SP + """
// ─── Chapter 2: Keyboard Patterns (Phase 387""")
rep("""'listen-sing': ListenSingLessonBook,""", """'listen-sing': ListenSingLessonBook, 'scale-play': ScalePlayLessonBook,""")
rep("""'listen-sing': lsLbPages,""", """'listen-sing': lsLbPages, 'scale-play': spLbPages,""")
# the Home: the Technique door's 'Playing scales and chords' opens with the room's five lessons; the fingerings in every key after
rep("""  'k-play': { lessons: ['sc-wr', 'sc-wl', 'sc-br', 'sc-bl', 'sc-both', 'ch-hands'] },""",
    """  'k-play': { lessons: [], groups: [   // Build AB
    { id: 'kpl-scales', en: 'Playing scales', ko: '스케일 치기', lessons: ['sp-turn', 'sp-beat', 'sp-minor', 'sp-mirror', 'sp-two'], check: 'scale-play' },
    { id: 'kpl-keys', en: 'Fingerings in every key, and chords', ko: '모든 조의 운지와 화음', lessons: ['sc-wr', 'sc-wl', 'sc-br', 'sc-bl', 'sc-both', 'ch-hands'] },
  ] },""")
rep("""  set('G', 'ls-beat ls-echo ls-updown ls-find ls-sing');   // Build X""", """  set('G', 'ls-beat ls-echo ls-updown ls-find ls-sing');   // Build X
  set('P1', 'sp-turn sp-beat sp-minor sp-mirror sp-two');   // Build AB""")
rep("""lbhAdd('rb-finger', 'r-beat', 'rhythm', 'The beat in your fingers',""", SPH + """
lbhAdd('rb-finger', 'r-beat', 'rhythm', 'The beat in your fingers',""")

open(dst, 'w', encoding='utf-8').write(s)
print('ok')
