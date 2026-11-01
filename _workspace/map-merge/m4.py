# Lesson mode across devices, the drills side (2026-11-01, her 'the phone too'). With the teacher's own login (the
# dashboard's Supabase session in this browser), the open lesson is read from and written to lesson_sessions, so a lesson
# started on the phone shows its coral bar on the iPad, and what the iPad notes reaches the phone. Without a session, or
# before migrations/2026-11-01_phaseE_lesson-sessions.sql is run, everything stays local as before.
import sys
p = sys.argv[1]; h = open(p, encoding='utf-8').read()
def rep(o, n, c=1):
    global h
    k = h.count(o)
    if k != c: raise SystemExit("count %d != %d for %r" % (k, c, o[:100]))
    h = h.replace(o, n)
rep("function TLessonBar({ lesson }) {", r'''function tTeacherSession() {   // the dashboard's login in this browser (supabase-js keeps it as sb-<project>-auth-token)
  try { for (let i = 0; i < localStorage.length; i++) { const k = localStorage.key(i); if (!/^sb-.*-auth-token$/.test(k)) continue;
    const s = JSON.parse(localStorage.getItem(k) || 'null'); const tk = s && (s.access_token || (s.currentSession && s.currentSession.access_token)); const u = s && (s.user || (s.currentSession && s.currentSession.user));
    const exp = s && (s.expires_at || (s.currentSession && s.currentSession.expires_at));
    if (tk && u && u.id && (!exp || exp * 1000 > Date.now() + 30000)) return { token: tk, uid: u.id }; } } catch (e) {}
  return null;
}
async function tLessonServer(method, body) {
  const ss = tTeacherSession(); if (!ss) return undefined;
  const ctl = typeof AbortController !== 'undefined' ? new AbortController() : null; const tm = setTimeout(() => { try { ctl && ctl.abort(); } catch (e) {} }, 8000);
  try {
    const base = PB_SUPABASE_URL + '/rest/v1/lesson_sessions';
    const hd = { apikey: PB_SUPABASE_ANON, Authorization: 'Bearer ' + ss.token, 'Content-Type': 'application/json' };
    let r;
    if (method === 'get') r = await fetch(base + '?select=*&user_id=eq.' + encodeURIComponent(ss.uid), { headers: hd, signal: ctl ? ctl.signal : undefined });
    else r = await fetch(base + '?on_conflict=user_id', { method: 'POST', headers: { ...hd, Prefer: 'resolution=merge-duplicates,return=minimal' }, body: JSON.stringify({ ...body, user_id: ss.uid }), signal: ctl ? ctl.signal : undefined });
    if (!r.ok) return undefined;
    if (method === 'get') { const a = await r.json(); return Array.isArray(a) && a.length ? a[0] : null; }
    return true;
  } catch (e) { return undefined; } finally { clearTimeout(tm); }
}
function tLessonPush(x) { if (!x) return; tLessonServer('put', { student_id: String(x.studentId), name: String(x.name || '').slice(0, 40), started_at: new Date(x.startedAt || Date.now()).toISOString(), shown: (x.shown || []).slice(0, 60), updated_at: new Date().toISOString() }).then(ok => { if (ok) { const y = tLessonGet(); if (y && String(y.studentId) === String(x.studentId) && !y.synced) { y.synced = true; try { localStorage.setItem(TLESSON_KEY, JSON.stringify(y)); } catch (e) {} } } }); }
async function tLessonPull() {   // same rule as the dashboard: same student -> both lists; else the server wins; synced but gone -> ended elsewhere
  const local = tLessonGet(), srv = await tLessonServer('get');
  if (srv === undefined) return local;
  if (srv) {
    const s = { studentId: srv.student_id, name: srv.name || '', startedAt: Date.parse(srv.started_at) || Date.now(), shown: Array.isArray(srv.shown) ? srv.shown : [], synced: true };
    const seen = new Set(); const both = [...s.shown, ...((local && String(local.studentId) === String(s.studentId) && local.shown) || [])].filter(it => { const k = it.kind + ':' + it.id; if (seen.has(k)) return false; seen.add(k); return true; });
    const m = { ...s, shown: both }; try { localStorage.setItem(TLESSON_KEY, JSON.stringify(m)); } catch (e) {}
    if (both.length > s.shown.length) tLessonPush(m);
    return m;
  }
  if (local && local.synced) { try { localStorage.removeItem(TLESSON_KEY); } catch (e) {} return null; }
  if (local) tLessonPush(local);
  return local;
}
function TLessonBar({ lesson }) {''')
# push after every note
rep("  if (!x.shown.some(it => it.kind === kind && it.id === id)) { x.shown.push({ kind, id, label: String(label || id).slice(0, 80), at: Date.now() }); try { localStorage.setItem(TLESSON_KEY, JSON.stringify(x)); } catch (e) {} }",
    "  if (!x.shown.some(it => it.kind === kind && it.id === id)) { x.shown.push({ kind, id, label: String(label || id).slice(0, 80), at: Date.now() }); try { localStorage.setItem(TLESSON_KEY, JSON.stringify(x)); } catch (e) {} tLessonPush(x); }")
# pull on load and when the page comes back
rep("  const [lesson, setLesson] = useState(() => tLessonGet());   // lesson mode",
    "  const [lesson, setLesson] = useState(() => tLessonGet());   // lesson mode\n  useEffect(() => { if (!teacher) return; let off = false; const f = () => tLessonPull().then(x => { if (!off) setLesson(x ? { ...x } : null); }); f(); window.addEventListener('focus', f); window.addEventListener('pageshow', f); return () => { off = true; window.removeEventListener('focus', f); window.removeEventListener('pageshow', f); }; }, [teacher]);")
open(p, 'w', encoding='utf-8').write(h); print('m4 ok')
