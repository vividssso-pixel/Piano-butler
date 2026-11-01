# Lesson mode, the drills side (2026-11-01, her 'yes, one iPad, go'). The dashboard's "Start lesson" saves pb_lesson_v1;
# while it is there, the teacher view notes every room (chapter) and tool opened and shows a coral bar with "End lesson".
import sys
p = sys.argv[1]; h = open(p, encoding='utf-8').read()
def rep(o, n, c=1):
    global h
    k = h.count(o)
    if k != c: raise SystemExit("count %d != %d for %r" % (k, c, o[:100]))
    h = h.replace(o, n)
rep("function mapSave(x) {", r'''// ── Lesson mode (with the teacher dashboard, same browser): {studentId, name, startedAt, shown: [{kind, id, label, at}]}
const TLESSON_KEY = 'pb_lesson_v1';
function tLessonGet() { try { const x = JSON.parse(localStorage.getItem(TLESSON_KEY) || 'null'); return x && x.studentId != null ? x : null; } catch (e) { return null; } }
function tLessonNote(kind, id, label) {
  const x = tLessonGet(); if (!x || !id) return x;
  x.shown = Array.isArray(x.shown) ? x.shown : [];
  if (!x.shown.some(it => it.kind === kind && it.id === id)) { x.shown.push({ kind, id, label: String(label || id).slice(0, 80), at: Date.now() }); try { localStorage.setItem(TLESSON_KEY, JSON.stringify(x)); } catch (e) {} }
  return x;
}
function TLessonBar({ lesson }) {
  const n = (lesson.shown || []).length;
  return <div data-testid="lesson-bar" style={{position:'sticky',top:0,zIndex:40,background:'#e4572e',color:'#fff',padding:'9px 16px',display:'flex',alignItems:'center',justifyContent:'space-between',gap:10,fontWeight:800,fontSize:13.5}}>
    <span>{t('Lesson with ', '레슨: ')}{lesson.name} · {n} {t(n === 1 ? 'shown' : 'shown', '개 보여 줌')}</span>
    <a href="teacher-dashboard.html?endlesson=1" data-testid="lesson-bar-end" style={{background:'#fff',color:'#e4572e',borderRadius:10,padding:'5px 11px',textDecoration:'none',fontSize:13}}>{t('End lesson', '레슨 끝내기')}</a>
  </div>;
}
function mapSave(x) {''')
rep("  const [findOpen, setFindOpen] = useState(false);", "  const [findOpen, setFindOpen] = useState(false);\n  const [lesson, setLesson] = useState(() => tLessonGet());   // lesson mode")
rep("      {term && <DictCard id={term} onClose={() => setTerm(null)}/>}", "      {term && <DictCard id={term} onClose={() => setTerm(null)}/>}\n      {T && lesson && <TLessonBar lesson={lesson}/>}")
rep("  function update(patch) { setSt(prev => ({ ...prev, ...patch })); }",
    "  function update(patch) { setSt(prev => ({ ...prev, ...patch })); }\n  // lesson mode: note each room and tool the teacher opens while a lesson is open\n  useEffect(() => { if (!T || st.lock || !tLessonGet()) return; let x = null;\n    if (st.drill) { const d = DRILLS.find(z => z.id === st.drill); x = tLessonNote('room', st.drill, d && d.label); }\n    if (st.tool) { const tl = TOOLS.find(z => z.id === st.tool); x = tLessonNote('tool', st.tool, tl && tl.title); }\n    if (x) setLesson({ ...x }); }, [st.drill, st.tool, T, st.lock]);")
open(p, 'w', encoding='utf-8').write(h); print('m3 ok')
