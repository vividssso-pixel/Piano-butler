# Dashboard D3 (2026-11-01, her 'yes, one iPad, go'): names first, and lesson mode (start, teach with the materials, end, save).
import sys
p=sys.argv[1]; h=open(p,encoding='utf-8').read()
def rep(o,n,c=1):
    global h
    k=h.count(o)
    if k!=c: raise SystemExit("count %d != %d for %r"%(k,c,o[:90]))
    h=h.replace(o,n)
# 1. the log keeps what was shown
rep('''    makeupDate: extra.makeupDate || "",
  };
};''','''    makeupDate: extra.makeupDate || "",
    shown: Array.isArray(extra.shown) ? extra.shown : [],   // Dashboard D3: what the lesson showed (lesson mode)
  };
};''')
rep('''    ...(f.makeupDate ? { makeupDate: f.makeupDate }  : {}),
  }) || null,''','''    ...(f.makeupDate ? { makeupDate: f.makeupDate }  : {}),
    ...(Array.isArray(f.shown) && f.shown.length ? { shown: f.shown.slice(0, 30) } : {}),
  }) || null,''')
rep('''      const row = logToRow(f, editLog.studentId, userId);''','''      const row = logToRow({ ...f, shown: f.shown || editLog.shown }, editLog.studentId, userId);''')

# 2. lesson mode helpers, the names row, the banner and the end sheet (before StudentDetail's PartHead)
rep('// Dashboard D2: the simple student page -- a small heading inside a card','''// ─── Dashboard D3: lesson mode ──────────────────────────────────────────────────────────────────────────────
// One iPad at the lesson table: "Start lesson" on a student's page saves {studentId, name, startedAt, shown: []} under
// pb_lesson_v1 and opens the materials (drills.html, teacher view). The drills note every room and tool opened while it is
// there (same key, same browser) and show a coral bar with "End lesson", which comes back here with ?endlesson=1.
// The end sheet offers what was shown (and last week's unfinished homework) as ticks; Save writes the lesson log.
const LESSON_KEY = "pb_lesson_v1";
const lessonGet = () => { try { const x = JSON.parse(localStorage.getItem(LESSON_KEY) || "null"); return x && x.studentId != null ? x : null; } catch (e) { return null; } };
const lessonSet = (x) => { try { if (x) localStorage.setItem(LESSON_KEY, JSON.stringify(x)); else localStorage.removeItem(LESSON_KEY); } catch (e) {} };
const lessonItemLine = (it) => it.kind === "room" ? it.label + " [chapter:" + it.id + "]" : it.kind === "tool" ? it.label + " [tool:" + it.id + "]" : it.label;
function NameChips({ students, logs, onPick, current }) {
  const dn = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"][new Date().getDay()], today = todayStr();
  const todays = [];
  students.filter(s => !s.paused).forEach(s => {
    const fortOk = s.lessonsPerWeek !== "fortnightly" || isFortnightWeek(s.startDate);
    if (s.lessonDay === dn && fortOk) todays.push({ s, t: s.lessonTime || "09:00", tag: fmtTime(s.lessonTime || "09:00") });
    if (s.lessonsPerWeek === 2 && s.lessonDay2 === dn) todays.push({ s, t: s.lessonTime2 || "09:00", tag: fmtTime(s.lessonTime2 || "09:00") });
  });
  logs.filter(l => l.type === "absent" && l.makeupDate === today).forEach(l => { const s = students.find(x => x.id === l.studentId); if (s) todays.push({ s, t: "99", tag: "makeup" }); });
  todays.sort((a, b) => a.t.localeCompare(b.t));
  const ids = new Set(todays.map(x => x.s.id));
  const rest = students.filter(s => !ids.has(s.id)).sort((a, b) => a.name.localeCompare(b.name));
  if (!students.length) return null;
  const chip = (s, tag, k) => (
    <button key={k} onClick={() => onPick(s)} data-testid="name-chip" className="no-print"
      style={{border:"1.5px solid " + (current === s.id ? "#26296b" : tag ? "#26296b" : "#e3dfd2"), background: current === s.id ? "#26296b" : "#fff", color: current === s.id ? "#fff" : "#26296b",
        borderRadius:999, padding:"7px 13px", fontSize:13.5, fontWeight:800, cursor:"pointer", opacity: s.paused ? 0.5 : 1}}>
      {firstNameOf(s.name)}{tag ? <span style={{fontWeight:600, opacity:0.7, marginLeft:5, fontSize:12}}>{tag}</span> : null}</button>);
  const lab = (t) => <p style={{fontSize:11,fontWeight:800,letterSpacing:"0.07em",textTransform:"uppercase",color:"#e4572e",margin:"0 0 6px"}}>{t}</p>;
  return (
    <div className="no-print mb-5" data-testid="name-chips">
      {todays.length > 0 && <>{lab("Today")}<div style={{display:"flex",gap:6,flexWrap:"wrap",marginBottom:10}}>{todays.map((x, i) => chip(x.s, x.tag, "t" + i))}</div></>}
      {rest.length > 0 && <>{lab(todays.length ? "Everyone else" : "Students")}<div style={{display:"flex",gap:6,flexWrap:"wrap"}}>{rest.map(s => chip(s, null, s.id))}</div></>}
    </div>
  );
}
function LessonBanner({ lesson, onEnd, onOpen }) {
  return (
    <div className="no-print mb-5 px-4 py-3 rounded-2xl flex items-center gap-3 flex-wrap" data-testid="lesson-banner" style={{background:"#e4572e",color:"#fff"}}>
      <span style={{fontWeight:800,fontSize:14}}>Lesson with {lesson.name} · {(lesson.shown || []).length} shown</span>
      <span className="flex-1"/>
      <a href="drills.html?teacher=1" className="text-xs font-bold px-3 py-1.5 rounded-xl" style={{background:"rgba(255,255,255,0.18)",color:"#fff",textDecoration:"none"}} onClick={onOpen}>Open materials</a>
      <button onClick={onEnd} className="text-xs font-bold px-3 py-1.5 rounded-xl" style={{background:"#fff",color:"#e4572e"}} data-testid="lesson-end">End lesson</button>
    </div>
  );
}
function EndLessonSheet({ lesson, student, logs, act, onSave, onAbsent, onBack, onDiscard }) {
  const shown = []; const seen = new Set();
  (lesson.shown || []).forEach(it => { const k = it.kind + ":" + it.id; if (!seen.has(k)) { seen.add(k); shown.push(it); } });
  const studentLogs = logs.filter(l => l.studentId === student.id);
  const last = latestHomeworkLog(studentLogs);
  const notYet = act && act.hw ? act.hw.notYet : [];
  const again = last ? hwLines(last.homework).filter(ln => notYet.includes(ln.text)) : [];
  const items = shown.map(it => ({ key: "s:" + it.kind + ":" + it.id, line: lessonItemLine(it), label: it.label, sub: it.kind === "room" ? "room" : it.kind === "tool" ? "tool" : "page", def: it.kind === "room" }))
    .concat(again.map(ln => ({ key: "a:" + ln.key, line: ln.key, label: ln.text + " (again)", sub: "from last time", def: true })));
  const [on, setOn] = useState(() => new Set(items.filter(x => x.def).map(x => x.key)));
  const seenKeys = React.useRef(new Set(items.map(x => x.key)));
  useEffect(() => { const fresh = items.filter(x => !seenKeys.current.has(x.key)); if (!fresh.length) return; fresh.forEach(x => seenKeys.current.add(x.key)); setOn(prev => { const n = new Set(prev); fresh.filter(x => x.def).forEach(x => n.add(x.key)); return n; }); }, [items.map(x => x.key).join("|")]);   // last week's items arrive with the roster
  const [notes, setNotes] = useState("");
  const [busy, setBusy] = useState(false);
  const toggle = (k) => setOn(prev => { const n = new Set(prev); if (n.has(k)) n.delete(k); else n.add(k); return n; });
  const save = async () => { setBusy(true); await onSave({ homework: items.filter(x => on.has(x.key)).map(x => x.line).join("\\n"), notes: notes.trim(), shown: shown.map(it => it.label) }); setBusy(false); };
  return (
    <div className="fixed inset-0 z-50 flex items-end sm:items-center justify-center no-print" style={{background:"rgba(38,41,107,0.38)"}} data-testid="end-lesson">
      <div className="w-full sm:max-w-md" style={{background:"#fff",borderRadius:"22px 22px 0 0",padding:"16px 18px 20px",maxHeight:"92vh",overflowY:"auto"}}>
        <p style={{fontSize:11,fontWeight:800,letterSpacing:"0.07em",textTransform:"uppercase",color:"#e4572e",margin:0}}>Lesson with {firstNameOf(student.name)} · {fmtShort(todayStr())}</p>
        <p className="text-xs mt-1 mb-2" style={{color:"#7a7ca6"}}>{items.length ? "Shown today · tick what to give as homework" : "Nothing was opened in the materials. Write a note, or go back to the materials."}</p>
        {items.map(x => (
          <label key={x.key} className="flex items-center gap-3" data-testid="end-item" style={{padding:"9px 0",borderTop:"1px solid #ece6d6",cursor:"pointer",fontSize:14,color:"#26296b"}}>
            <input type="checkbox" checked={on.has(x.key)} onChange={() => toggle(x.key)} style={{width:18,height:18}}/>
            <span style={{flex:1}}>{x.label}</span><span style={{fontSize:11,color:"#7a7ca6"}}>{x.sub}</span>
          </label>))}
        <textarea className="input" rows={2} placeholder="Notes (optional)" value={notes} onChange={e => setNotes(e.target.value)} style={{width:"100%",marginTop:10,fontSize:14}} data-testid="end-notes"/>
        <div className="flex gap-2 mt-3">
          <button className="btn-primary text-sm py-2.5 px-4" style={{flex:2}} disabled={busy} onClick={save} data-testid="end-save">{busy ? "Saving…" : "Save lesson"}</button>
          <button className="btn-ghost text-sm py-2.5 px-4" style={{flex:1}} onClick={onAbsent}>Absent</button>
        </div>
        <div className="flex justify-between mt-3 text-xs">
          <a href="drills.html?teacher=1" onClick={onBack} style={{color:"#62649a",textDecoration:"underline"}}>Back to the materials</a>
          <button onClick={onDiscard} style={{color:"#c0431f",textDecoration:"underline"}} data-testid="end-discard">Discard this lesson</button>
        </div>
      </div>
    </div>
  );
}
// Dashboard D2: the simple student page -- a small heading inside a card''')

# 3. the student page: Start lesson
rep('function StudentDetail({ student, logs, onLog, onEditLog, onDeleteLog, onMarkAttended, onBack, onEdit, onPause, onResume, onDelete, act }) {',
    'function StudentDetail({ student, logs, onLog, onEditLog, onDeleteLog, onMarkAttended, onBack, onEdit, onPause, onResume, onDelete, act, onStartLesson, lessonOn }) {')
rep('''          <button onClick={()=>onLog(student)} className="btn-primary text-sm py-2.5 px-4" style={{flex:1}} data-testid="detail-log">+ Log lesson</button>''',
    '''          {onStartLesson ? <button onClick={()=>onStartLesson(student)} className="text-sm font-bold py-2.5 px-4 rounded-xl" style={{flex:1,background:"#e4572e",color:"#fff"}} data-testid="start-lesson">{lessonOn ? "▶ Continue lesson" : "▶ Start lesson"}</button>
            : <button onClick={()=>onLog(student)} className="btn-primary text-sm py-2.5 px-4" style={{flex:1}} data-testid="detail-log">+ Log lesson</button>}''')
rep('''            : linkRow === null ? <button onClick={openSettings} className="btn-ghost text-sm py-2.5 px-4" style={{flex:1}} data-testid="link-strip-make">Make a link</button> : null}
        </div>''','''            : linkRow === null ? <button onClick={openSettings} className="btn-ghost text-sm py-2.5 px-4" style={{flex:1}} data-testid="link-strip-make">Make a link</button> : null}
        </div>
        {onStartLesson && <div className="no-print text-center mt-2"><button onClick={()=>onLog(student)} className="text-xs underline" style={{color:"#7a7ca6"}} data-testid="detail-log">+ Log a lesson without the materials</button></div>}''')

# 4. App: state, start, end, save
rep('''  const roster = useRosterActivity(students, logs, tab);''','''  const roster = useRosterActivity(students, logs, tab);
  const [lesson, setLesson] = useState(() => lessonGet());   // Dashboard D3
  const [endOpen, setEndOpen] = useState(() => { try { return new URLSearchParams(location.search).get("endlesson") === "1"; } catch (e) { return false; } });
  useEffect(() => { const f = () => setLesson(lessonGet()); window.addEventListener("focus", f); window.addEventListener("pageshow", f); return () => { window.removeEventListener("focus", f); window.removeEventListener("pageshow", f); }; }, []);
  const clearEndParam = () => { try { const u = new URL(location.href); u.searchParams.delete("endlesson"); history.replaceState(null, "", u.pathname + (u.search ? u.search : "") + u.hash); } catch (e) {} };''')
rep('''  const selectStudent = (s) => { setSelected(s); setView("detail"); };''','''  const selectStudent = (s) => { setSelected(s); setView("detail"); };
  // Dashboard D3: lesson mode
  const startLesson = (s) => {
    const cur = lessonGet();
    if (cur && String(cur.studentId) !== String(s.id) && !confirm("A lesson with " + cur.name + " is still open. Start a new one with " + firstNameOf(s.name) + "? (The open one is discarded.)")) return;
    if (!cur || String(cur.studentId) !== String(s.id)) lessonSet({ studentId: s.id, name: firstNameOf(s.name), startedAt: Date.now(), shown: [] });
    window.location.href = "drills.html?teacher=1";
  };
  const saveLesson = async (s, f) => {
    const row = logToRow({ date: todayStr(), notes: f.notes, homework: f.homework, shown: f.shown, type: "regular" }, s.id, userId);
    const { data, error } = await _supabase.from("lesson_logs").insert(row).select().single();
    if (error) { alert("Could not save the lesson: " + error.message); return; }
    setLogs(p => [rowToLog(data), ...p]);
    lessonSet(null); setLesson(null); setEndOpen(false); clearEndParam();
  };''')
rep('''      <main className="max-w-6xl mx-auto px-4 py-7">''','''      <main className="max-w-6xl mx-auto px-4 py-7">
        {/* Dashboard D3: the open lesson, and the names */}
        {lesson && !endOpen && <LessonBanner lesson={lesson} onEnd={() => setEndOpen(true)}/>}
        {lesson && endOpen && (() => { const s = students.find(x => String(x.id) === String(lesson.studentId)); return s ? (
          <EndLessonSheet lesson={lesson} student={s} logs={logs} act={roster[s.id]}
            onSave={(f) => saveLesson(s, f)}
            onAbsent={() => { lessonSet(null); setLesson(null); setEndOpen(false); clearEndParam(); setAbsenceTarget(s); }}
            onBack={() => {}}
            onDiscard={() => { if (!confirm("Discard this lesson? Nothing is saved.")) return; lessonSet(null); setLesson(null); setEndOpen(false); clearEndParam(); }}/>
        ) : null; })()}
        {(tab==="today" || (tab==="students" && view==="list")) && <NameChips students={students} logs={logs} current={null} onPick={(s) => { setSelected(s); setView("detail"); setTab("students"); }}/>}''')
rep('''              onDelete={deleteStudent}
              act={roster[liveStudent.id]}''','''              onDelete={deleteStudent}
              act={roster[liveStudent.id]}
              onStartLesson={startLesson}
              lessonOn={!!(lesson && String(lesson.studentId) === String(liveStudent.id))}''')
# the open lesson, shown in Last lesson and history: "Shown"
rep('''            {(last.repertoire || last.technical) && <p className="text-xs mt-2" style={{color:"#62649a"}}>''','''            {last.shown && last.shown.length > 0 && <p className="text-xs mt-2" style={{color:"#62649a"}} data-testid="last-shown"><b style={{letterSpacing:"0.05em",textTransform:"uppercase",fontSize:10.5}}>Shown</b><br/>{last.shown.join(" · ")}</p>}
            {(last.repertoire || last.technical) && <p className="text-xs mt-2" style={{color:"#62649a"}}>''')
open(p,'w',encoding='utf-8').write(h); print('d3 ok')
