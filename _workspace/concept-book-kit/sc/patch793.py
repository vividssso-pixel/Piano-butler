#!/usr/bin/env python3
"""Build DQ (on t792 -> t793; board call 33-1, her 21:41 'go with your recommendation'): Knowing Your Pieces, Grade 8 and Diplomas,
the fourth Grade 8 room. The general knowledge of the Certificate of Performance and the diplomas (Piano syllabus 2026, Section II;
research33-grade8.md): the significance of titles and every marking; the composer's influences, impact and output; the period and
its performance conventions; the structure with its keys, language and climax; the piano of the time and what it did to the
repertoire; all as the ground for the candidate's own interpretive choices. Five steps (the arc, the title, the conventions, the
piano, viva cards) and the five checks; a drill with four levels; the Workbook's diploma sheet per piece and a paper check; the
teacher copy; four Home lessons and one 'Make your own' (the viva cards). The room reuses the app's own data: the map of the Grade 7
room, the eras' conventions and the piano's timeline from the piano's story. The chapter code is pieces8.code.js next to this file.
"""
import sys, os
src, dst = sys.argv[1], sys.argv[2]
here = os.path.dirname(os.path.abspath(__file__))
s = open(src, encoding='utf-8').read()
def R(old, new, n=1):
    global s
    c = s.count(old); assert c == n, (c, n, old[:120]); s = s.replace(old, new)

# the room in every registry (after the Grade 7 pieces room, or after the Grade 8 arpeggios room)
R("""const PIECES_78_DRILL = { id: 'pieces-78', label: 'Knowing Your Pieces, Grades 7 and 8' };   // Build BW""",
  """const PIECES_78_DRILL = { id: 'pieces-78', label: 'Knowing Your Pieces, Grades 7 and 8' };   // Build BW
const PIECES_8_DRILL = { id: 'pieces-8', label: 'Knowing Your Pieces, Grade 8 and Diplomas' };   // Build DQ""")
R("""  { id: 'pieces-78', label: 'Knowing Your Pieces, Grades 7 and 8', concept: PIECES_78_DRILL, track: 'start' },   // Build BW""",
  """  { id: 'pieces-78', label: 'Knowing Your Pieces, Grades 7 and 8', concept: PIECES_78_DRILL, track: 'start' },   // Build BW
  { id: 'pieces-8', label: 'Knowing Your Pieces, Grade 8 and Diplomas', concept: PIECES_8_DRILL, track: 'start' },   // Build DQ""")
R("""'pieces-78': '내 곡 알기, Grade 7과 8'""", """'pieces-78': '내 곡 알기, Grade 7과 8', 'pieces-8': '내 곡 알기, Grade 8과 디플로마'""")
R("""'pieces-78': 'c-map'""", """'pieces-78': 'c-map', 'pieces-8': 'c-map'""")
R("""  'pieces-78': 'general knowledge grade 7 grade 8 piece form structure analysis map sections key changes tonal organisation atonal pentatonic whole tone movement larger work period style genres composer works influences',""",
  """  'pieces-78': 'general knowledge grade 7 grade 8 piece form structure analysis map sections key changes tonal organisation atonal pentatonic whole tone movement larger work period style genres composer works influences',
  'pieces-8': 'general knowledge grade 8 certificate of performance diploma amusa lmusa viva title terms climax keys harmonic language performance conventions period style piano history fortepiano harpsichord composer influences output interpretive choices',""")
R("""'pieces-78': ['form', 'composers']""", """'pieces-78': ['form', 'composers'], 'pieces-8': ['pieces-78', 'piano-story']""")
R("""'pieces-78': ['My pieces', '내 곡']""", """'pieces-78': ['My pieces', '내 곡'], 'pieces-8': ['My pieces 8', '내 곡 8']""")
R("""'listen-8': [1, 2, 4], 'scales-8': [1, 2, 3, 4, 5], 'arps-8': [1, 2, 3, 4],""", """'listen-8': [1, 2, 4], 'scales-8': [1, 2, 3, 4, 5], 'arps-8': [1, 2, 3, 4], 'pieces-8': [1, 2, 3, 4],""")
R("""  { ids: ['listen-8', 'scales-8', 'arps-8'], en: ['Grade 8', 'Your ears, scales, and arpeggios and chord walks: the top floor.'], ko: ['Grade 8', '귀, 스케일, 아르페지오와 화음 진행: 맨 위층.'] },""",
  """  { ids: ['listen-8', 'scales-8', 'arps-8', 'pieces-8'], en: ['Grade 8', 'Your ears, scales, arpeggios and chord walks, and knowing your pieces to diploma depth: the top floor.'], ko: ['Grade 8', '귀, 스케일, 아르페지오와 화음 진행, 그리고 디플로마 깊이로 내 곡 알기: 맨 위층.'] },""")
# the chapter
CH = open(os.path.join(here, 'pieces8.code.js'), encoding='utf-8').read()
R("""WORKBOOKS['pieces-78'] = P78Workbook;""", """WORKBOOKS['pieces-78'] = P78Workbook;""" + CH)
# the Home: four lessons after the book's pages, and the viva cards as a 'Make your own'
HOME = r'''
// ══ Build DQ: Knowing Your Pieces, Grade 8 and Diplomas on the Home (Pieces, Melody and form) ══
LBH_FN['pieces-8'] = (s) => p8LbPages(s);
const p8HomeAdd = (id, i, en, ko, benEn, bko, make) => lbhAdd(id, 'c-map', 'piece', en, ko, benEn, bko, lbhSpec('pieces-8', i, { make }));
const p8Q = (kind) => (n, prev) => { const L = P8_LEVELS.find(x => x.kind === kind), q = genP8Question(L, prev);
  const lab = (c) => (kind === 'title' ? t(p8Title(c)[1], p8Title(c)[2]) : kind === 'arc' ? q.secs[c][0] : kind === 'conv' ? p8Era(c).short : p8PianoName(c));
  const prompt = kind === 'title' ? ['Which title promises this?', '이것을 약속하는 제목은?'] : kind === 'arc' ? ['Where is the climax?', '클라이맥스는 어디일까요?'] : kind === 'conv' ? ['Which period plays like this?', '어느 시대의 연주일까요?'] : ['Which piano is this?', '어떤 피아노일까요?'];
  const card = (txt) => <div style={{textAlign:'center',margin:'6px auto',maxWidth:420,padding:'12px 12px',borderRadius:10,border:'1.5px solid ' + BK.ink,background:'#fff',fontSize:15,fontWeight:800,color:BK.ink,lineHeight:1.4}}>{txt}</div>;
  const fig = () => ({ mid: kind === 'title' ? card(t(p8Title(q.id)[3], p8Title(q.id)[4])) : kind === 'arc' ? <PaArc secs={q.secs} ten={q.ten} quiz mark={-1} sel={-1} w={420} h={110}/> : kind === 'conv' ? card(p8Era(q.id).traits[q.ti]) : card(t(P8_PIANOS[q.k][1], P8_PIANOS[q.k][2])) });
  return { kind: 'choice', cols: kind === 'arc' ? q.choices.length : 2, key: q.key, prompt, opts: q.choices.map(c => ({ id: c, label: () => lab(c) })), ans: q.answer, ok: (v) => v === q.answer, fig,
    yes: ['Yes: ' + lab(q.answer) + '.', '맞아요: ' + lab(q.answer) + '.'], no: ['It is ' + lab(q.answer) + '.', '정답은 ' + lab(q.answer) + '.'] }; };
p8HomeAdd('p8-arc', 1, 'The arc of my piece', '내 곡의 곡선', 'Tension up, the climax, the way home: where is the top?', '긴장이 오르고, 클라이맥스, 집으로: 꼭대기는 어디?', p8Q('arc'));
p8HomeAdd('p8-title', 2, 'What the title promises', '제목이 약속하는 것', 'Nocturne, scherzo, barcarolle, ballade: what does each one promise?', '녹턴, 스케르초, 뱃노래, 발라드: 무엇을 약속할까?', p8Q('title'));
p8HomeAdd('p8-conv', 3, 'How they played it then', '그때는 어떻게 쳤을까', 'Ornaments, pedal, rubato, touch: which period plays like this?', '꾸밈음, 페달, 루바토, 터치: 어느 시대의 연주?', p8Q('conv'));
p8HomeAdd('p8-piano', 4, 'The piano of the time', '그 시대의 피아노', 'Harpsichord, fortepiano, iron frame, 88 keys: which piano was it written for?', '하프시코드, 포르테피아노, 철 프레임, 88건반: 어떤 피아노를 위해 썼을까?', p8Q('piano'));
'''
R("""p78HomeAdd('p78-genre', 4, 'Other music of its time', '그 시대의 다른 음악', 'Which period does each genre belong to?', '갈래마다 어느 시대의 것일까?', p78Q('genre'));
""", """p78HomeAdd('p78-genre', 4, 'Other music of its time', '그 시대의 다른 음악', 'Which period does each genre belong to?', '갈래마다 어느 시대의 것일까?', p78Q('genre'));
""" + HOME)
R("""    { id: 'c-pieces', en: 'Knowing your pieces, Grades 7 and 8', ko: '내 곡 알기, Grade 7과 8', lessons: ['p78-form', 'p78-tonal', 'p78-mvt', 'p78-genre', 'mk-map'], check: 'pieces-78' },   // Build BW""",
  """    { id: 'c-pieces', en: 'Knowing your pieces, Grades 7 and 8', ko: '내 곡 알기, Grade 7과 8', lessons: ['p78-form', 'p78-tonal', 'p78-mvt', 'p78-genre', 'mk-map'], check: 'pieces-78' },   // Build BW
    { id: 'c-pieces8', en: 'Knowing your pieces, Grade 8 and diplomas', ko: '내 곡 알기, Grade 8과 디플로마', lessons: ['p8-arc', 'p8-title', 'p8-conv', 'p8-piano', 'mk-viva'], check: 'pieces-8' },   // Build DQ""")
R("""  set('8', 'a8-walk a8-arp a8-inv a8-dim mk-fourkeys');   // Build BZ: Arpeggios and Progressions, Grade 8""",
  """  set('8', 'a8-walk a8-arp a8-inv a8-dim mk-fourkeys');   // Build BZ: Arpeggios and Progressions, Grade 8
  set('8', 'p8-arc p8-title p8-conv p8-piano mk-viva');   // Build DQ: Knowing Your Pieces, Grade 8 and Diplomas""")
# the 'Make your own': the viva cards
R("""  { id: 'mk-map', ch: 'pieces-78', title: 'The map of my piece',""", """  { id: 'mk-viva', ch: 'pieces-8', title: 'Viva cards', blurb: 'The examiner\\'s eleven questions on any piece, answered aloud and ticked off.', C: () => <VivaCards/> },   // Build DQ
  { id: 'mk-map', ch: 'pieces-78', title: 'The map of my piece',""")
R("""  'mk-map': ['내 곡의 지도', '내가 치는 곡의 부분, 마디, 조를 지도로 그려요.'],""", """  'mk-viva': ['비바 카드', '어떤 곡이든 시험관의 질문 열한 장에 소리 내어 답하고 표시해요.'],
  'mk-map': ['내 곡의 지도', '내가 치는 곡의 부분, 마디, 조를 지도로 그려요.'],""")
R("""'mk-map': ['melody', 3, 3, 'write show'],""", """'mk-map': ['melody', 3, 3, 'write show'], 'mk-viva': ['composers', 3, 3, 'show'],""")
R("""'mk-map': 'c-map',""", """'mk-map': 'c-map', 'mk-viva': 'c-map',""")
R("""  'mk-map': () => (\n""", """  'mk-viva': () => (
    <svg width="34" height="34" viewBox="0 0 24 24"><rect width="24" height="24" rx="6" fill="#3b4fa8"/><rect x="8" y="4" width="11" height="14" rx="1.5" fill="#fefbf3"/><rect x="5" y="7" width="11" height="14" rx="1.5" fill="#fefbf3" stroke="#3b4fa8" strokeWidth="0.8"/><text x="10.5" y="18" textAnchor="middle" fontSize="9" fontWeight="900" fill="#e9a83a" fontFamily="Georgia, serif">?</text></svg>
  ),
  'mk-map': () => (\n""")
R("""const LESSON_BOOKS = { 'arps-8': Arps8LessonBook,""", """const LESSON_BOOKS = { 'pieces-8': Pieces8LessonBook, 'arps-8': Arps8LessonBook,""")
R("""const LB_PAGE_FNS = { 'arps-8': a8LbPages,""", """const LB_PAGE_FNS = { 'pieces-8': p8LbPages, 'arps-8': a8LbPages,""")
R("""const HOUSE_ICONS = {""", """const HOUSE_ICONS = {"pieces-8": "<rect x=\\"4\\" y=\\"10\\" width=\\"40\\" height=\\"24\\" rx=\\"2\\"/><path d=\\"M8 30 L15 26 L22 14 L29 22 L39 28\\" fill=\\"none\\"/><circle cx=\\"22\\" cy=\\"14\\" r=\\"3.2\\" fill=\\"#e4572e\\" stroke=\\"none\\"/>",""")
open(dst, 'w', encoding='utf-8').write(s)
print('ok', len(s))
