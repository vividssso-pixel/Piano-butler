"""Build EC, call 41 (her 14:32 'a space that takes in the whole, like a book's reference pages: it becomes the map',
14:36 'all at once'): the Reference. One table per topic (notes and rests, time signatures, keys and key signatures,
scales, intervals, chords and cadences, signs and terms), Beginner to Grade 8, each row a door into the room that teaches
it. On the Home's Quick line in place of the Scales map (which lives inside it now, under Scales) and on paper
(?book=reference, five A4 pages, on the Books tab). Code in sc/ref41.code.js."""
import sys, os
src, dst = sys.argv[1], sys.argv[2]
here = os.path.dirname(os.path.abspath(__file__))
s = open(src, encoding='utf-8').read()
def R(old, new, n=1):
    global s
    c = s.count(old); assert c == n, (c, n, old[:120]); s = s.replace(old, new)
CODE = open(os.path.join(here, 'ref41.code.js'), encoding='utf-8').read()
R("""function ToolView({ id, locked, onBack, onChapter, backLabel = '← Home', backAlways }) {""", CODE + """
function ToolView({ id, locked, onBack, onChapter, backLabel = '← Home', backAlways }) {""")
R("""  { id: 'scales-map', ch: 'scales',""", """  { id: 'reference', ch: 'concept', title: 'Reference', blurb: 'The whole of the theory on a few tables, Beginner to Grade 8; each row a door into its room.', C: (p) => <ReferenceView onChapter={p && p.onChapter}/> },   // Build EC (call 41)
  { id: 'scales-map', ch: 'scales',""")
R("""  'scales-map': ['스케일 지도',""", """  'reference': ['한눈에 보기', 'Beginner부터 Grade 8까지의 이론을 표 몇 장에. 줄마다 그걸 배우는 방으로 가는 문.'],
  'scales-map': ['스케일 지도',""")
R("""  'scales-map': () => (""", """  'reference': () => (
    <svg width="34" height="34" viewBox="0 0 24 24"><rect width="24" height="24" rx="6" fill="#26296b"/>{[6, 10.5, 15].map((y, i) => <g key={y}><rect x="4" y={y} width="4.5" height="2.6" rx="1" fill={i === 0 ? "#e4572e" : "#fefbf3"}/><rect x="10" y={y} width="10" height="2.6" rx="1" fill="#fefbf3"/></g>)}</svg>
  ),
  'scales-map': () => (""")
R("""'scales-map': ['scales', 0, 3, 'show home'],""", """'scales-map': ['scales', 0, 3, 'show home'], 'reference': ['scales', 0, 3, 'show home'],""")
R("""{[['scale-finder', t('Scale finder', '스케일 찾기')], ['scales-map', t('Scales map', '스케일 지도')], ['metronome', t('Metronome', '메트로놈')]]""",
  """{[['scale-finder', t('Scale finder', '스케일 찾기')], ['reference', t('Reference', '한눈에 보기')], ['metronome', t('Metronome', '메트로놈')]]""")
# on paper
R("""  const fixed = kind === 'check' || kind === 'checkkey' ||""", """  const fixed = kind === 'reference' || kind === 'check' || kind === 'checkkey' ||""")
R("""        ? kind === 'check' ? <CkpPaperBook fk={(CKP && CKP.key) || '0a'}/> :""", """        ? kind === 'reference' ? <RefBook/> : kind === 'check' ? <CkpPaperBook fk={(CKP && CKP.key) || '0a'}/> :""")
R("""  if (printParams && (printParams.get('book') === 'lesson' ||""", """  if (printParams && (printParams.get('book') === 'reference' || printParams.get('book') === 'lesson' ||""")
R("""          {wholeBtn('teacher', 'all', t('All Teacher copies', '교사용 전체'))}""", """          {wholeBtn('teacher', 'all', t('All Teacher copies', '교사용 전체'))}
          <a href={'?book=reference' + (LANG === 'ko' ? '&lang=ko' : '&lang=en')} target="_blank" rel="noopener" data-ref-book style={{fontSize:12.5,fontWeight:800,color:KIND.lesson.col,border:'1.5px solid ' + KIND.lesson.col,borderRadius:10,padding:'6px 12px',textDecoration:'none',background:'#fff'}}>{t('Reference', '한눈에 보기')}</a>""")
open(dst, 'w', encoding='utf-8').write(s)
print('ok reference', len(s))
