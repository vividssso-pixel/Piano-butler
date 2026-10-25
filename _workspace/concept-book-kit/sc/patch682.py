import sys, os
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
HP = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'hp682.jsx'), encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)

# Build T (her 2026-10-25 answer: option 1 for room 5, 'Hand positions'): chapter 5 on the Beginner floor. Its Lesson Book
# (8 pages: opener, C position, G position, move between them, hands together, taking turns, tunes, my five checks) is also its
# online lesson; its drill has five levels. The Workbook and the teacher's copy come next. The chapter code: hp682.jsx.
rep("""const FORM_DRILL = { id: 'form', label: 'Musical Form' };""",
    """const FORM_DRILL = { id: 'form', label: 'Musical Form' };
const HAND_POS_DRILL = { id: 'hand-positions', label: 'Hand Positions' };   // Build T: its lesson and questions with its Lesson Book (hpLbPages)""")
rep("""  { id: 'note-names', label: 'The Musical Alphabet', concept: NOTE_NAMES_DRILL, track: 'pitch' },""",
    """  { id: 'note-names', label: 'The Musical Alphabet', concept: NOTE_NAMES_DRILL, track: 'pitch' },
  { id: 'hand-positions', label: 'Hand Positions', concept: HAND_POS_DRILL, track: 'start' },   // Build T""")
rep("""  'posture-hands': '자세와 손 모양', 'first-steps': '건반 패턴', 'note-names': '음악 알파벳', 'pulse': '박과 세기',""",
    """  'posture-hands': '자세와 손 모양', 'first-steps': '건반 패턴', 'note-names': '음악 알파벳', 'hand-positions': '손 자리', 'pulse': '박과 세기',""")
rep("""  'posture-hands': ['Posture', '자세'], 'first-steps': ['Patterns', '패턴'], 'note-names': ['Alphabet', '알파벳'],""",
    """  'posture-hands': ['Posture', '자세'], 'first-steps': ['Patterns', '패턴'], 'note-names': ['Alphabet', '알파벳'], 'hand-positions': ['Hand positions', '손 자리'],""")
rep("""const HOUSE_ICONS = {"accidentals": """,
    """const HOUSE_ICONS = {"hand-positions": "<rect x=\\"4\\" y=\\"15\\" width=\\"40\\" height=\\"17\\" rx=\\"1.5\\"/><path d=\\"M12 15 V32 M20 15 V32 M28 15 V32 M36 15 V32\\" stroke-width=\\"1.1\\"/><circle cx=\\"8\\" cy=\\"8\\" r=\\"2.6\\" fill=\\"#26296b\\" stroke=\\"none\\"/><circle cx=\\"16\\" cy=\\"6\\" r=\\"2.6\\" fill=\\"#26296b\\" stroke=\\"none\\"/><circle cx=\\"24\\" cy=\\"5\\" r=\\"2.6\\" fill=\\"#26296b\\" stroke=\\"none\\"/><circle cx=\\"32\\" cy=\\"6\\" r=\\"2.6\\" fill=\\"#26296b\\" stroke=\\"none\\"/><circle cx=\\"40\\" cy=\\"9\\" r=\\"2.6\\" fill=\\"#e4572e\\" stroke=\\"none\\"/>", "accidentals": """)
rep("""  'posture-hands': 'k-posture', 'first-steps': 'p-staff',""", """  'posture-hands': 'k-posture', 'hand-positions': 'k-positions', 'first-steps': 'p-staff',""")
rep("""  'posture-hands': 'posture hand shape beginner sit stool arm weight alignment finger number which finger thumb',""",
    """  'posture-hands': 'posture hand shape beginner sit stool arm weight alignment finger number which finger thumb',
  'hand-positions': 'hand position c position g position five finger thumb middle c both hands together mirror move',""")
# the rooms a chapter is easier after, in the Beginner floor's new order (none may point to a later room)
rep("""'reading-steps': ['whole-staff', 'time-signatures'], dynamics: ['reading-steps'],""", """'reading-steps': ['staff', 'hand-positions'], dynamics: ['reading-steps', 'time-signatures'], 'hand-positions': ['note-names'],""")
# the chapter lists' tag: the floor the chapter is on (the old grade tags predate the floors)
rep("""tag={GRADE_TAGS[id]}""", """tag={stageOfChapter(id) >= 0 ? PATH_STAGES[stageOfChapter(id)].en[0] : GRADE_TAGS[id]}""")
# the Home's positions concept: its questions are the new chapter's
rep("""  'k-positions': { lessons: ['kp-fingers', 'kp-cpos', 'kp-gpos', 'kp-five'], check: 'posture-hands', level: 3 },""",
    """  'k-positions': { lessons: ['kp-fingers', 'kp-cpos', 'kp-gpos', 'kp-five'], check: 'hand-positions' },   // Build T""")
# the chapter itself, after chapter 1
rep("""
// ─── Chapter 2: Keyboard Patterns (Phase 387""", HP + """
// ─── Chapter 2: Keyboard Patterns (Phase 387""")
rep("""const LESSON_BOOKS = { 'posture-hands': PostureLessonBook,""", """const LESSON_BOOKS = { 'posture-hands': PostureLessonBook, 'hand-positions': HandPositionsLessonBook,""")
rep("""const LB_PAGE_FNS = { 'posture-hands': postureLbPages,""", """const LB_PAGE_FNS = { 'posture-hands': postureLbPages, 'hand-positions': hpLbPages,""")

open(dst, 'w', encoding='utf-8').write(s)
print('ok')
