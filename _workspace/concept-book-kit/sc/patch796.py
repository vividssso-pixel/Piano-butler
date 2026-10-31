"""Build DT, board call 33-2 and her 09:37 ('information, and other devices to understand it'), on t795 -> t796:
The Piano's Story, Grade 8 and Diplomas, a room in the attic beside The Piano's Story. The diplomas' fifth area of general
knowledge, "the construction and development of the instrument ... implications ... upon the repertoire", in five steps, each
with a thing to touch: Vienna and London (two actions to press, a sketch of each sound), the keyboard that grows (an 88-key
strip and six compasses; 'could it play this note?'), hand, knee, foot (a slider through the pedals' years; the markings read
then and today), iron, felt and the singing tone (build the modern piano; a key to repeat with one escapement or two), and
their piano, my choices (the composer's piano and four questions said aloud). Facts and sources: sc/research33-2-piano.md."""
import sys, os
here = os.path.dirname(os.path.abspath(__file__))
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def R(old, new, n=1):
    global s
    c = s.count(old); assert c == n, (c, n, old[:120]); s = s.replace(old, new)

NAME_EN, NAME_KO = 'The Piano’s Story, Grade 8 and Diplomas', '피아노 이야기, Grade 8과 디플로마'
# the room in every registry
R("""const PIECES_8_DRILL = { id: 'pieces-8', label: 'Knowing Your Pieces, Grade 8 and Diplomas' };   // Build DQ""",
  """const PIECES_8_DRILL = { id: 'pieces-8', label: 'Knowing Your Pieces, Grade 8 and Diplomas' };   // Build DQ
const PIANO_STORY_8_DRILL = { id: 'piano-story-8', label: '""" + NAME_EN + """' };   // Build DT""")
R("""  { id: 'piano-story', label: 'The Piano’s Story', concept: PIANO_STORY_DRILL, track: 'reading' },""",
  """  { id: 'piano-story', label: 'The Piano’s Story', concept: PIANO_STORY_DRILL, track: 'reading' },
  { id: 'piano-story-8', label: '""" + NAME_EN + """', concept: PIANO_STORY_8_DRILL, track: 'reading' },   // Build DT""")
R("""'piano-story': '피아노 이야기', """, """'piano-story': '피아노 이야기', 'piano-story-8': '""" + NAME_KO + """', """)
R("""  'piano-story': 'about', 'composers': 'about', 'styles': 'about',""", """  'piano-story': 'about', 'piano-story-8': 'about', 'composers': 'about', 'styles': 'about',""")
R("""'piano-story': 'General knowledge', """, """'piano-story': 'General knowledge', 'piano-story-8': 'G8–Diplomas', """)
R("""  'piano-story': 'history piano era composer hammer damper string key action inside pedal una corda sustain sostenuto grand upright',""",
  """  'piano-story': 'history piano era composer hammer damper string key action inside pedal una corda sustain sostenuto grand upright',
  'piano-story-8': 'piano history diploma amusa lmusa construction development fortepiano viennese action english action stein walter backers broadwood erard graf pleyel compass keyboard range 61 keys 88 keys knee lever hand stop moderator pedal una corda tre corde senza sordino sostenuto double escapement iron frame felt hammers crossed strings interpretive choices',""")
R("""'pieces-8': ['pieces-78', 'piano-story']""", """'pieces-8': ['pieces-78', 'piano-story'], 'piano-story-8': ['piano-story']""")
R("""'piano-story': ['The piano', '피아노'], """, """'piano-story': ['The piano', '피아노'], 'piano-story-8': ['The piano 8', '피아노 8'], """)
R("""'piano-story': [1, 2, 3, 4, 5, 6, 7, 8], """, """'piano-story': [1, 2, 3, 4, 5, 6, 7, 8], 'piano-story-8': [1, 2, 3, 4], """)
R("""  { ids: ['piano-story', 'pitch-range', 'composers', 'styles'], stories: true, garret: true, th: { wp: 'drape', fl: 'boards', lamp: 'candelabrum' }, en: ['Stories of music', 'Rooms to visit any time: the piano’s own story, the instruments, composers through time, and styles.'], ko: ['음악 이야기', '언제든 들어가는 방: 피아노 이야기, 악기, 시대별 작곡가, 스타일.'] },""",
  """  { ids: ['piano-story', 'piano-story-8', 'pitch-range', 'composers', 'styles'], stories: true, garret: true, th: { wp: 'drape', fl: 'boards', lamp: 'candelabrum' }, en: ['Stories of music', 'Rooms to visit any time: the piano’s own story (and again at diploma depth), the instruments, composers through time, and styles.'], ko: ['음악 이야기', '언제든 들어가는 방: 피아노 이야기(디플로마 깊이로 한 번 더), 악기, 시대별 작곡가, 스타일.'] },   // Build DT: the piano's story at diploma depth""")
# the chapter
CH = open(os.path.join(here, 'ps8.code.js'), encoding='utf-8').read()
R("""WORKBOOKS['piano-story'] = SpsWorkbook;""", """WORKBOOKS['piano-story'] = SpsWorkbook;""" + CH)
# the Home: five lessons, in Stories of music and on the Grade 8 shelf
HOME = r'''
// ══ Build DT: The Piano's Story, Grade 8 and Diplomas on the Home (Stories of music) ══
LBH_FN['piano-story-8'] = (s) => ps8LbPages(s);
const ps8HomeAdd = (id, i, en, ko, benEn, bko, make) => lbhAdd(id, 'about', 'beside', en, ko, benEn, bko, lbhSpec('piano-story-8', i, { make }));
const ps8Q = (kind) => (n, prev) => { const L = PS8_LEVELS.find(x => x.kind === kind), q = genPs8Question(L, prev), lab = (c) => ps8Label(kind, c);
  const prompt = kind === 'act' ? ['Vienna or London?', '빈일까요, 런던일까요?'] : kind === 'comp' ? ['A ' + ps8NoteName(q.m) + ': which is the first keyboard here that has it?', ps8NoteName(q.m) + ': 이 음이 있는 가장 이른 건반은?'] : kind === 'mark' ? ['What does it ask for?', '무엇을 하라는 걸까요?'] : ['Which invention gave this?', '어떤 발명이 이것을 주었을까요?'];
  const card = (txt, o = {}) => <div style={{textAlign:'center',margin:'6px auto',maxWidth:420,padding:'12px 12px',borderRadius:10,border:'1.5px solid ' + BK.ink,background:'#fff',fontSize:o.fs || 15,fontWeight:800,fontStyle:o.it ? 'italic' : undefined,fontFamily:o.serif ? LB_SERIF : undefined,color:BK.ink,lineHeight:1.4}}>{txt}</div>;
  const fig = () => ({ mid: kind === 'act' ? card(t(PS8_CLUES[q.ci][1], PS8_CLUES[q.ci][2])) : kind === 'comp' ? <Ps8Ladder sel={null} mark={q.m} rows={false}/> : kind === 'mark' ? card(ps8Mark(q.id)[1], { fs: 24, it: true, serif: true }) : card(t(ps8Inv(q.id)[4][0], ps8Inv(q.id)[4][1])) });
  return { kind: 'choice', cols: kind === 'mark' ? 1 : 2, key: q.key, prompt, opts: q.choices.map(c => ({ id: c, label: () => lab(c) })), ans: q.answer, ok: (v) => v === q.answer, fig,
    yes: ['Yes: ' + lab(q.answer) + '.', '맞아요: ' + lab(q.answer) + '.'], no: ['It is: ' + lab(q.answer) + '.', '정답은: ' + lab(q.answer) + '.'] }; };
ps8HomeAdd('ps8-act', 1, 'Vienna and London', '빈과 런던', 'Two ways to throw a hammer: press both actions and hear the difference.', '해머를 던지는 두 가지 방법: 두 액션을 눌러 보고 차이를 들어요.', ps8Q('act'));
ps8HomeAdd('ps8-comp', 2, 'The keyboard grows', '자라나는 건반', '61, 68, 73, 78, 85, 88 keys: could your composer’s piano play that note?', '61, 68, 73, 78, 85, 88건반: 내 작곡가의 피아노는 그 음을 칠 수 있었을까?', ps8Q('comp'));
ps8HomeAdd('ps8-ped', 3, 'Hand, knee, foot', '손, 무릎, 발', 'From hand stops and knee levers to three pedals; read senza sordino and una corda.', '손잡이와 무릎 레버에서 페달 세 개까지; 센차 소르디노와 우나 코르다 읽기.', ps8Q('mark'));
ps8HomeAdd('ps8-modern', 4, 'Iron, felt and the singing tone', '철, 펠트, 노래하는 소리', 'Build the modern piano invention by invention, and repeat a note with one escapement or two.', '발명을 하나씩 더해 현대 피아노를 만들고, 이스케이프먼트 하나와 둘로 같은 음을 반복해요.', ps8Q('inv'));
ps8HomeAdd('ps8-mine', 5, 'Their piano, my choices', '그들의 피아노, 나의 선택', 'Which piano was your piece written for, and so how do you play it today?', '내 곡은 어떤 피아노를 위해 쓰였고, 그래서 오늘 어떻게 칠까?');
'''
R("""p8HomeAdd('p8-piano', 4, 'The piano of the time', '그 시대의 피아노', 'Harpsichord, fortepiano, iron frame, 88 keys: which piano was it written for?', '하프시코드, 포르테피아노, 철 프레임, 88건반: 어떤 피아노를 위해 썼을까?', p8Q('piano'));
""", """p8HomeAdd('p8-piano', 4, 'The piano of the time', '그 시대의 피아노', 'Harpsichord, fortepiano, iron frame, 88 keys: which piano was it written for?', '하프시코드, 포르테피아노, 철 프레임, 88건반: 어떤 피아노를 위해 썼을까?', p8Q('piano'));
""" + HOME)
R("""    { id: 'ab-piano', en: 'The piano’s story', ko: '피아노 이야기', lessons: CHAPTER_TOOL_ORDER['piano-story'].slice(), check: 'piano-story' },
    { id: 'ab-inst',""", """    { id: 'ab-piano', en: 'The piano’s story', ko: '피아노 이야기', lessons: CHAPTER_TOOL_ORDER['piano-story'].slice(), check: 'piano-story' },
    { id: 'ab-piano8', en: 'The piano’s story, Grade 8 and diplomas', ko: '피아노 이야기, Grade 8과 디플로마', lessons: ['ps8-act', 'ps8-comp', 'ps8-ped', 'ps8-modern', 'ps8-mine'], check: 'piano-story-8' },   // Build DT
    { id: 'ab-inst',""")
R("""  set('8', 'p8-arc p8-title p8-conv p8-piano mk-viva');   // Build DQ: Knowing Your Pieces, Grade 8 and Diplomas""",
  """  set('8', 'p8-arc p8-title p8-conv p8-piano mk-viva');   // Build DQ: Knowing Your Pieces, Grade 8 and Diplomas
  set('8', 'ps8-act ps8-comp ps8-ped ps8-modern ps8-mine');   // Build DT: The Piano's Story, Grade 8 and Diplomas""")
R("""const LESSON_BOOKS = { 'pieces-8': Pieces8LessonBook,""", """const LESSON_BOOKS = { 'piano-story-8': PianoStory8LessonBook, 'pieces-8': Pieces8LessonBook,""")
R("""const LB_PAGE_FNS = { 'pieces-8': p8LbPages,""", """const LB_PAGE_FNS = { 'piano-story-8': ps8LbPages, 'pieces-8': p8LbPages,""")
R("""const HOUSE_ICONS = {""", """const HOUSE_ICONS = {"piano-story-8": "<path d=\\"M6 14 L30 14 C38 14 42 18 42 22 L42 24 L6 24 Z\\" fill=\\"#26296b\\"/><path d=\\"M9 24 V32 M39 24 V32 M6 14 L26 4\\"/><text x=\\"34\\" y=\\"11\\" font-size=\\"11\\" font-weight=\\"900\\" fill=\\"#e4572e\\" stroke=\\"none\\" font-family=\\"Inter, sans-serif\\">8</text>",""")
open(dst, 'w', encoding='utf-8').write(s)
print('ok room', len(s))
