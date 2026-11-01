# Dashboard D4 (2026-11-01, her 'the phone too, keep them in sync'): the open lesson lives in Supabase (lesson_sessions,
# migrations/2026-11-01_phaseE_lesson-sessions.sql) as well as in this browser, so any device of the teacher sees it.
import sys
p=sys.argv[1]; h=open(p,encoding='utf-8').read()
def rep(o,n,c=1):
    global h
    k=h.count(o)
    if k!=c: raise SystemExit("count %d != %d for %r"%(k,c,o[:90]))
    h=h.replace(o,n)
rep('''const lessonItemLine = (it) =>''','''// the server copy (lesson_sessions, one row per teacher). undefined = no table yet (SQL not run) or offline: the local copy carries on
const lsFromRow = (r) => ({ studentId: r.student_id, name: r.name || "", startedAt: Date.parse(r.started_at) || Date.now(), shown: Array.isArray(r.shown) ? r.shown : [], synced: true });
const lsMerge = (a, b) => { const out = []; const seen = new Set(); [...(a || []), ...(b || [])].forEach(it => { const k = it.kind + ":" + it.id; if (!seen.has(k)) { seen.add(k); out.push(it); } }); return out; };
async function lsFetch() { try { const { data, error } = await _supabase.from("lesson_sessions").select("*").maybeSingle(); return error ? undefined : (data || null); } catch (e) { return undefined; } }
async function lsPut(uid, x) { if (!uid || !x) return false; try { const { error } = await _supabase.from("lesson_sessions").upsert({ user_id: uid, student_id: String(x.studentId), name: (x.name || "").slice(0, 40), started_at: new Date(x.startedAt || Date.now()).toISOString(), shown: (x.shown || []).slice(0, 60), updated_at: new Date().toISOString() }); return !error; } catch (e) { return false; } }
async function lsClear(uid) { if (!uid) return; try { await _supabase.from("lesson_sessions").delete().eq("user_id", uid); } catch (e) {} }
// local and server agree: same student -> both lists of what was shown; another student or none -> the server wins;
// no server row but a local one that was synced before -> the lesson ended on another device
async function lessonSync(uid) {
  const local = lessonGet(), srv = await lsFetch();
  if (srv === undefined) return local;
  if (srv) {
    const s = lsFromRow(srv);
    const merged = local && String(local.studentId) === String(s.studentId) ? { ...s, shown: lsMerge(s.shown, local.shown) } : s;
    lessonSet(merged);
    if (merged.shown.length > s.shown.length) await lsPut(uid, merged);
    return merged;
  }
  if (local && local.synced) { lessonSet(null); return null; }
  if (local) { const ok = await lsPut(uid, local); if (ok) { local.synced = true; lessonSet(local); } }
  return local;
}
const lessonItemLine = (it) =>''')
# App: sync on load, focus, every 30 s
rep('''  useEffect(() => { const f = () => setLesson(lessonGet()); window.addEventListener("focus", f); window.addEventListener("pageshow", f); return () => { window.removeEventListener("focus", f); window.removeEventListener("pageshow", f); }; }, []);''',
'''  useEffect(() => {   // Dashboard D4: the open lesson follows the teacher across devices
    if (!userId) return;
    let off = false;
    const f = () => { lessonSync(userId).then(x => { if (!off) setLesson(x); }); };
    f(); window.addEventListener("focus", f); window.addEventListener("pageshow", f);
    const iv = setInterval(f, 30000);
    return () => { off = true; window.removeEventListener("focus", f); window.removeEventListener("pageshow", f); clearInterval(iv); };
  }, [userId]);''')
rep('''    if (!cur || String(cur.studentId) !== String(s.id)) lessonSet({ studentId: s.id, name: firstNameOf(s.name), startedAt: Date.now(), shown: [] });
    window.location.href = "drills.html?teacher=1";''','''    let x = cur && String(cur.studentId) === String(s.id) ? cur : { studentId: s.id, name: firstNameOf(s.name), startedAt: Date.now(), shown: [] };
    lessonSet(x);
    const go = () => { window.location.href = "drills.html?teacher=1"; };
    lsPut(userId, x).then(ok => { if (ok) { x = { ...x, synced: true }; lessonSet(x); } go(); }, go);''')
rep('''    lessonSet(null); setLesson(null); setEndOpen(false); clearEndParam();
  };''','''    lessonSet(null); setLesson(null); setEndOpen(false); clearEndParam(); lsClear(userId);
  };''')
rep('''            onAbsent={() => { lessonSet(null); setLesson(null); setEndOpen(false); clearEndParam(); setAbsenceTarget(s); }}''',
    '''            onAbsent={() => { lessonSet(null); setLesson(null); setEndOpen(false); clearEndParam(); lsClear(userId); setAbsenceTarget(s); }}''')
rep('''            onDiscard={() => { if (!confirm("Discard this lesson? Nothing is saved.")) return; lessonSet(null); setLesson(null); setEndOpen(false); clearEndParam(); }}/>''',
    '''            onDiscard={() => { if (!confirm("Discard this lesson? Nothing is saved.")) return; lessonSet(null); setLesson(null); setEndOpen(false); clearEndParam(); lsClear(userId); }}/>''')
open(p,'w',encoding='utf-8').write(h); print('d4 ok')
