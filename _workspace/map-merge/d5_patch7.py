# Dashboard D5 (2026-11-01, her 'lessons are missed or off for all kinds of reasons: just make those buttons'):
# "No lesson today" with one-tap reasons. Absent and Sick count as the student's absence; I cancelled, Holiday or break,
# Moved and Other are 'cancelled' (no lesson, not held against the student). Both can owe a makeup.
import sys, re
p=sys.argv[1]; h=open(p,encoding='utf-8').read()
def rep(o,n,c=1):
    global h
    k=h.count(o)
    if k!=c: raise SystemExit("count %d != %d for %r"%(k,c,o[:90]))
    h=h.replace(o,n)
# data
rep('''    type: extra.type || "regular", // "regular" | "absent" | "makeup"''','''    type: extra.type || "regular", // "regular" | "absent" | "makeup" | "cancelled" (Dashboard D5)
    reason: extra.reason || "",''')
rep('''    ...(f.makeupDate ? { makeupDate: f.makeupDate }  : {}),''','''    ...(f.makeupDate ? { makeupDate: f.makeupDate }  : {}),
    ...(f.reason ? { reason: f.reason } : {}),''')
# helpers (before AbsenceModal)
rep('function AbsenceModal({ student, onSave, onClose }) {','''// Dashboard D5: why there was no lesson. [id, label, type]: absent counts against attendance, cancelled does not
const NO_LESSON_REASONS = [["absent", "Absent", "absent"], ["sick", "Sick", "absent"], ["teacher", "I cancelled", "cancelled"], ["holiday", "Holiday or break", "cancelled"], ["moved", "Moved to another day", "cancelled"], ["other", "Other", "cancelled"]];
const noLesson = (l) => !!l && (l.type === "absent" || l.type === "cancelled");
const offLabel = (l) => { const r = NO_LESSON_REASONS.find(x => x[0] === (l && l.reason)); return r ? r[1] : l && l.type === "cancelled" ? "No lesson" : "Absent"; };
function AbsenceModal({ student, onSave, onClose }) {''')
# the modal itself
i=h.index('function AbsenceModal({ student, onSave, onClose }) {'); j=h.index('\n}\n',i)+3
h=h[:i]+'''function AbsenceModal({ student, onSave, onClose }) {
  const [reason, setReason] = useState("absent");
  const [mk, setMk] = useState(false);   // record a makeup lesson instead
  const [date, setDate] = useState(todayStr());
  const [makeupDate, setMakeupDate] = useState("");
  const [notes, setNotes] = useState("");
  const r = NO_LESSON_REASONS.find(x => x[0] === reason) || NO_LESSON_REASONS[0];
  const owes = !mk && reason !== "holiday";
  const handleSave = () => {
    if (mk) onSave({ date, type: "makeup", makeupDate: "", notes, repertoire:"", technical:"", srAural:"", gk:"", mood:"", pieceRating:"" });
    else onSave({ date, type: r[2], reason: r[0], makeupDate: owes ? makeupDate : "", notes, repertoire:"", technical:"", srAural:"", gk:"", mood:"", pieceRating:"" });
  };
  return (
    <div className="fixed inset-0 bg-black/40 flex items-center justify-center z-50 p-4" onClick={onClose} data-testid="no-lesson">
      <div className="bg-white rounded-2xl shadow-2xl w-full max-w-sm fade-in" onClick={e=>e.stopPropagation()}>
        <div className="p-5 border-b border-slate-100">
          <h2 className="text-sm font-bold text-slate-800">{mk ? "Makeup lesson" : "No lesson"}</h2>
          <p className="text-xs text-slate-400 mt-0.5">{student.name}</p>
        </div>
        <div className="p-5 space-y-4">
          {!mk && <div>
            <label className="field-label text-slate-500">Why</label>
            <div style={{display:"grid",gridTemplateColumns:"1fr 1fr",gap:8}}>
              {NO_LESSON_REASONS.map(([id, label, type]) => (
                <button key={id} onClick={()=>setReason(id)} data-testid={"reason-" + id}
                  className="py-2.5 rounded-xl text-sm font-semibold border transition-all"
                  style={reason === id ? (type === "absent" ? {background:"#fbe3da",color:"#c0431f",borderColor:"#f3c3b3"} : {background:"#ecebf5",color:"#26296b",borderColor:"#b8b9d9"}) : {background:"white",color:"#62649a",borderColor:"#e9e2d2"}}>
                  {label}
                </button>))}
            </div>
            <p className="text-[11px] mt-2" style={{color:"#7a7ca6"}}>{r[2] === "absent" ? "Counts as the student’s absence." : "Not counted against the student."}</p>
          </div>}
          <div>
            <label className="field-label text-slate-500">{mk ? "Makeup date" : "Lesson date"}</label>
            <input type="date" value={date} onChange={e=>setDate(e.target.value)} className="input"/>
          </div>
          {owes && (
            <div>
              <label className="field-label text-slate-500">{reason === "moved" ? "Moved to" : "Makeup on (optional)"}</label>
              <input type="date" value={makeupDate} onChange={e=>setMakeupDate(e.target.value)} className="input" data-testid="makeup-date"/>
            </div>
          )}
          <div>
            <label className="field-label text-slate-500">Notes (optional)</label>
            <input value={notes} onChange={e=>setNotes(e.target.value)} placeholder="" className="input"/>
          </div>
          <button onClick={()=>setMk(x=>!x)} className="text-xs underline" style={{color:"#7a7ca6"}}>{mk ? "← No lesson instead" : "Record a makeup lesson instead"}</button>
        </div>
        <div className="p-5 flex gap-3 border-t border-slate-100">
          <button className="btn-ghost flex-1" onClick={onClose}>Cancel</button>
          <button className="btn-primary flex-1" onClick={handleSave} data-testid="no-lesson-save">Save</button>
        </div>
      </div>
    </div>
  );
}
'''+h[j:]
# everywhere a lesson did not happen
h=h.replace('l.type !== "absent"','!noLesson(l)')
h=h.replace('l.type === "absent" && l.makeupDate','noLesson(l) && l.makeupDate')
h=h.replace('l.type!=="absent"','!noLesson(l)')
rep('return !lg ? "pending" : lg.type === "absent" ? "absent" : "logged"; };','return !lg ? "pending" : noLesson(lg) ? "absent" : "logged"; };')
rep('todayLog ? (todayLog.type==="absent" ? "absent" : "logged") : "pending";','todayLog ? (noLesson(todayLog) ? "absent" : "logged") : "pending";')
# attendance: absences are the student's only
rep('''        const absentLogs   = filteredLogs.filter(l => l.type === "absent");''','''        const absentLogs   = filteredLogs.filter(l => l.type === "absent");   // D5: 'cancelled' (teacher, holiday…) is neither a lesson nor an absence''')
# labels
rep('''                  {log.type==="absent" && <span style={{fontSize:"10px",fontWeight:700,padding:"1px 8px",borderRadius:"99px",...coralPill}}>Absent</span>}''',
    '''                  {noLesson(log) && <span style={{fontSize:"10px",fontWeight:700,padding:"1px 8px",borderRadius:"99px",...(log.type === "absent" ? coralPill : navyPill)}}>{offLabel(log)}</span>}''')
rep('''                    <span className="pb-tag hot">Absent</span>''','''                    <span className="pb-tag hot">{offLabel(todayLog)}</span>''')
rep('''<button onClick={()=>onAbsence(s)} className="pb-act quiet pb-absent-btn">Absent</button>''','''<button onClick={()=>onAbsence(s)} className="pb-act quiet pb-absent-btn">No lesson</button>''')
rep('''          <button className="btn-ghost text-sm py-2.5 px-4" style={{flex:1}} onClick={onAbsent}>Absent</button>''','''          <button className="btn-ghost text-sm py-2.5 px-4" style={{flex:1}} onClick={onAbsent}>No lesson</button>''')
rep('''<button onClick={()=>onAbsence(s)} className="pb-slot-btn" style={{background:"transparent",color:"#6d6f9c"}}>Absent</button>''','''<button onClick={()=>onAbsence(s)} className="pb-slot-btn" style={{background:"transparent",color:"#6d6f9c"}}>No lesson</button>''')
rep('''<span className="pb-slot-btn" style={{background:"#fbe3da",color:"#c0431f",cursor:"default"}}>Absent</span>''','''<span className="pb-slot-btn" style={{background:"#fbe3da",color:"#c0431f",cursor:"default"}}>{offLabel(todayLog)}</span>''')
rep('''                  {log.type === "absent" && (
                    <button onClick={()=>onMarkAttended(log)}''','''                  {noLesson(log) && (
                    <button onClick={()=>onMarkAttended(log)}''')
# the today summary
h=h.replace('n("absent") ? [n("absent") + " absent"] : []','n("absent") ? [n("absent") + " no lesson"] : []')
open(p,'w',encoding='utf-8').write(h); print('d5 ok', h.count('noLesson('))
