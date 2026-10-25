import sys, os
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
here = os.path.dirname(os.path.abspath(__file__))
E8 = open(os.path.join(here, 'e8x.jsx'), encoding='utf-8').read()
E8H = open(os.path.join(here, 'e8h.jsx'), encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)

# Build AD (the syllabus check's finding 2: 6/8 is Grade 1): 6/8 Time, a room after Rhythm Patterns on the first Prelim - Grade 1
# floor. Two big beats (1 and 4), the dotted crotchet as one big beat, long-short (crotchet + quaver), 3/4 or 6/8 by beams and by
# ear, then new lines to count, clap and play; the rhythm chapter's rows and scoring (RqStaff). On the Home, Rhythm gets a group.
rep("""const MINOR_SCALES_DRILL = { id: 'minor-scales', label: 'Minor Scales' };""",
    """const MINOR_SCALES_DRILL = { id: 'minor-scales', label: 'Minor Scales' };
const SIX_EIGHT_DRILL = { id: 'six-eight', label: '6/8 Time' };   // Build AD: its lessons and questions with its Lesson Book (e8LbPages)""")
rep("""  { id: 'rhythm', label: 'Rhythm Patterns', concept: RHYTHM_DRILL, track: 'rhythm' },""",
    """  { id: 'rhythm', label: 'Rhythm Patterns', concept: RHYTHM_DRILL, track: 'rhythm' },
  { id: 'six-eight', label: '6/8 Time', concept: SIX_EIGHT_DRILL, track: 'rhythm' },   // Build AD""")
rep("""'rhythm': '리듬 패턴', """, """'rhythm': '리듬 패턴', 'six-eight': '6/8박자', """)
rep("""'rhythm': ['Rhythm', '리듬 꼴'],""", """'rhythm': ['Rhythm', '리듬 꼴'], 'six-eight': ['6/8', '6/8'],""")
rep("""const HOUSE_ICONS = {"minor-scales": """, """const HOUSE_ICONS = {"six-eight": "<path d=\\"M10 28 V8 M19 28 V8 M28 28 V8 M10 8 H28\\"/><circle cx=\\"7\\" cy=\\"29\\" r=\\"3.4\\" fill=\\"#26296b\\" stroke=\\"none\\"/><circle cx=\\"16\\" cy=\\"29\\" r=\\"3.4\\" fill=\\"#26296b\\" stroke=\\"none\\"/><circle cx=\\"25\\" cy=\\"29\\" r=\\"3.4\\" fill=\\"#26296b\\" stroke=\\"none\\"/><path d=\\"M41 28 V8\\" stroke=\\"#e4572e\\"/><circle cx=\\"38\\" cy=\\"29\\" r=\\"3.6\\" fill=\\"#e4572e\\" stroke=\\"none\\"/><circle cx=\\"45.5\\" cy=\\"29\\" r=\\"1.7\\" fill=\\"#e4572e\\" stroke=\\"none\\"/>", "minor-scales": """)
rep("""  'rhythm': 'rhythm clap count beat pattern',""", """  'rhythm': 'rhythm clap count beat pattern',
  'six-eight': '6/8 six eight compound time dotted crotchet big beats quavers in threes 3/4 or 6/8 count clap',""")
rep("""rhythm: ['time-signatures'], """, """rhythm: ['time-signatures'], 'six-eight': ['rhythm'], """)
rep("""'rhythm': 'r-beat',""", """'rhythm': 'r-beat', 'six-eight': 'r-beat',""")
rep("""'r-beat': ['pulse', 'note-values', 'time-signatures', 'rhythm']""", """'r-beat': ['pulse', 'note-values', 'time-signatures', 'rhythm', 'six-eight']""")
rep("""{ ids: ['tempo', 'rhythm', 'ledger-lines', 'scales', 'scale-play', 'accidentals', 'piano-story'], en: ['Prelim – Grade 1', 'Speed, quavers and dots, ledger lines, scales and how to play them, accidentals, and the piano’s own story.'], ko: ['Prelim – Grade 1', '빠르기, 8분음표와 점, 덧줄, 스케일과 스케일 치기, 임시표, 그리고 피아노 이야기.'] }""",
    """{ ids: ['tempo', 'rhythm', 'six-eight', 'ledger-lines', 'scales', 'scale-play', 'accidentals', 'piano-story'], en: ['Prelim – Grade 1', 'Speed, quavers and dots, 6/8, ledger lines, scales and how to play them, accidentals, and the piano’s own story.'], ko: ['Prelim – Grade 1', '빠르기, 8분음표와 점, 6/8박자, 덧줄, 스케일과 스케일 치기, 임시표, 그리고 피아노 이야기.'] }""")
rep("""
// ─── Chapter 2: Keyboard Patterns (Phase 387""", E8 + """
// ─── Chapter 2: Keyboard Patterns (Phase 387""")
rep("""'minor-scales': MinorScalesLessonBook,""", """'minor-scales': MinorScalesLessonBook, 'six-eight': SixEightLessonBook,""")
rep("""'minor-scales': msLbPages,""", """'minor-scales': msLbPages, 'six-eight': e8LbPages,""")
rep("""    { id: 'rb-patterns', en: 'Rhythm patterns', ko: '리듬 패턴', lessons: ['rp-beams', 'rp-alone', 'rp-dot', 'rp-up', 'rp-read'], check: 'rhythm' },""",
    """    { id: 'rb-patterns', en: 'Rhythm patterns', ko: '리듬 패턴', lessons: ['rp-beams', 'rp-alone', 'rp-dot', 'rp-up', 'rp-read'], check: 'rhythm' },
    { id: 'rb-68', en: '6/8 time', ko: '6/8박자', lessons: ['e8-big', 'e8-dot', 'e8-ls', 'e8-34', 'e8-read'], check: 'six-eight' },   // Build AD""")
rep("""  set('P1', 'ms-third ms-rel ms-har ms-gaps ms-ear');   // Build AC""", """  set('P1', 'ms-third ms-rel ms-har ms-gaps ms-ear');   // Build AC
  set('P1', 'e8-big e8-dot e8-ls e8-34 e8-read');   // Build AD""")
rep("""lbhAdd('rb-finger', 'r-beat', 'rhythm', 'The beat in your fingers',""", E8H + """
lbhAdd('rb-finger', 'r-beat', 'rhythm', 'The beat in your fingers',""")

open(dst, 'w', encoding='utf-8').write(s)
print('ok')
