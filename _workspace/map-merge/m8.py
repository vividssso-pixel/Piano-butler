# Lesson mode: pick the student inside the drills (2026-11-01, her 'a tab to choose the student here; the dashboard is for
# editing and the small things; in a lesson, tap the name and go'). The teacher view shows a "Lesson" row: the students
# (today's first), read with the teacher's own login; a tap starts the lesson (local + lesson_sessions). The login is
# refreshed here when it has run out, so the drills keep working without reopening the dashboard.
import sys
p = sys.argv[1]; h = open(p, encoding='utf-8').read()
def rep(o, n, c=1):
    global h
    k = h.count(o)
    if k != c: raise SystemExit("count %d != %d for %r" % (k, c, o[:100]))
    h = h.replace(o, n)
# a session that refreshes itself
rep("async function tLessonServer(method, body) {\n  const ss = tTeacherSession(); if (!ss) return undefined;",
    r'''async function tTeacherSessionFresh() {   // refresh an expired login with its refresh token, the way supabase-js does
  const ok = tTeacherSession(); if (ok) return ok;
  try { for (let i = 0; i < localStorage.length; i++) { const k = localStorage.key(i); if (!/^sb-.*-auth-token$/.test(k)) continue;
    const s = JSON.parse(localStorage.getItem(k) || 'null'); if (!s || !s.refresh_token) continue;
    const r = await fetch(PB_SUPABASE_URL + '/auth/v1/token?grant_type=refresh_token', { method: 'POST', headers: { apikey: PB_SUPABASE_ANON, 'Content-Type': 'application/json' }, body: JSON.stringify({ refresh_token: s.refresh_token }) });
    if (!r.ok) return null; const n = await r.json(); if (!n || !n.access_token) return null;
    const exp = n.expires_at || Math.floor(Date.now() / 1000) + (n.expires_in || 3600);
    localStorage.setItem(k, JSON.stringify({ ...s, ...n, expires_at: exp }));
    return { token: n.access_token, uid: (n.user && n.user.id) || (s.user && s.user.id) }; } } catch (e) {}
  return null;
}
async function tTeacherGet(path) {   // a read with the teacher's login -> array | undefined
  const ss = await tTeacherSessionFresh(); if (!ss) return undefined;
  try { const r = await fetch(PB_SUPABASE_URL + '/rest/v1/' + path, { headers: { apikey: PB_SUPABASE_ANON, Authorization: 'Bearer ' + ss.token } }); if (!r.ok) return undefined; return await r.json(); } catch (e) { return undefined; }
}
const T_DAYS = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
function tFirst(n) { return String(n || '').trim().split(/\s+/)[0].slice(0, 40); }
function tLessonStart(s) {   // s: { id, name }
  const cur = tLessonGet();
  if (cur && String(cur.studentId) === String(s.id)) return cur;
  const x = { studentId: s.id, name: tFirst(s.name), startedAt: Date.now(), shown: [] };
  try { localStorage.setItem(TLESSON_KEY, JSON.stringify(x)); } catch (e) {}
  tLessonPush(x);
  return x;
}
function TLessonPick({ onStart }) {
  const [open, setOpen] = useState(false);
  const [list, setList] = useState(null);   // null = not loaded, false = no login, [] = students
  useEffect(() => { if (!open || list) return; tTeacherGet('students?select=id,name,lesson_day,lesson_time,lesson_day2,lesson_time2,extra&order=name').then(a => setList(Array.isArray(a) ? a : false)); }, [open]);
  const today = T_DAYS[new Date().getDay()];
  const rows = Array.isArray(list) ? list.map(s => { let ex = {}; try { ex = typeof s.extra === 'string' ? JSON.parse(s.extra || '{}') : (s.extra || {}); } catch (e) {} return { ...s, paused: !!ex.paused,
    when: s.lesson_day === today ? (s.lesson_time || '') : s.lesson_day2 === today ? (s.lesson_time2 || '') : null }; }).filter(s => !s.paused) : [];
  const todays = rows.filter(s => s.when != null).sort((a, b) => String(a.when).localeCompare(String(b.when))), rest = rows.filter(s => s.when == null);
  const chip = (s) => <button key={s.id} type="button" className="chip" data-testid="tpick-name" onClick={() => { setOpen(false); onStart(s); }} style={{minHeight:40,padding:'6px 13px',fontSize:14,fontWeight:800}}>{tFirst(s.name)}{s.when ? <span style={{fontWeight:600,opacity:0.7,marginLeft:5,fontSize:12}}>{s.when.slice(0, 5)}</span> : null}</button>;
  const lab = (x) => <div style={{fontSize:11,fontWeight:900,letterSpacing:'0.07em',textTransform:'uppercase',color:'#e4572e',margin:'8px 0 5px'}}>{x}</div>;
  return <div data-testid="tpick" style={{background:'#fffefa',border:'1.5px solid var(--navy-line)',borderRadius:12,padding:'8px 12px',marginBottom:12}}>
    <button type="button" onClick={() => setOpen(o => !o)} data-testid="tpick-open" style={{display:'flex',width:'100%',justifyContent:'space-between',alignItems:'center',border:'none',background:'transparent',cursor:'pointer',font:'inherit',padding:'4px 0',color:'var(--navy)'}}>
      <span style={{fontWeight:900,fontSize:14.5}}>{t('▶ Start a lesson', '▶ 레슨 시작')}</span><span style={{fontSize:12.5,color:'var(--muted)',fontWeight:700}}>{open ? t('close', '닫기') : t('choose a student', '학생 고르기')}</span></button>
    {open && (list === null ? <div style={{fontSize:13,color:'var(--muted)',padding:'6px 0'}}>…</div>
      : list === false ? <div style={{fontSize:13,color:'var(--muted)',padding:'6px 0'}}>{t('Sign in on the dashboard once on this device, then come back.', '이 기기에서 대시보드에 한 번 로그인한 뒤 다시 오세요.')} <a href="teacher-dashboard.html" style={{color:'var(--navy)',fontWeight:800}}>{t('Dashboard', '대시보드')}</a></div>
      : <div>{todays.length > 0 && <>{lab(t('Today', '오늘'))}<div style={{display:'flex',flexWrap:'wrap',gap:6}}>{todays.map(chip)}</div></>}
          {rest.length > 0 && <>{lab(todays.length ? t('Everyone else', '나머지 학생') : t('Students', '학생'))}<div style={{display:'flex',flexWrap:'wrap',gap:6}}>{rest.map(chip)}</div></>}
          {!rows.length && <div style={{fontSize:13,color:'var(--muted)',padding:'6px 0'}}>{t('No students yet. Add them on the dashboard.', '아직 학생이 없어요. 대시보드에서 추가하세요.')}</div>}</div>)}
  </div>;
}
async function tLessonServer(method, body) {
  const ss = await tTeacherSessionFresh(); if (!ss) return undefined;''')
# show the picker in the teacher view when no lesson is open
rep("        <StudentBanner sl={sl}/>", "        <StudentBanner sl={sl}/>\n        {T && !st.lock && !lesson && <TLessonPick onStart={(s) => { const cur = tLessonGet(); if (cur && String(cur.studentId) !== String(s.id) && !window.confirm(t('A lesson with ' + cur.name + ' is still open. Start a new one?', cur.name + '의 레슨이 아직 열려 있어요. 새로 시작할까요?'))) return; setLesson({ ...tLessonStart(s) }); }}/>}")
open(p, 'w', encoding='utf-8').write(h); print('m8 ok')
