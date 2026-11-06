#!/usr/bin/env python3
"""Phase 453 (This week): patch teacher-dashboard.html. Usage: patch_dash.py <teacher-dashboard.html>"""
import sys
p = sys.argv[1]
s = open(p, encoding='utf-8').read()

def rep(old, new):
    global s
    n = s.count(old)
    if n != 1:
        sys.exit('anchor found %d times: %r' % (n, old[:80]))
    s = s.replace(old, new)

COMPONENT = r'''// This week (Phase 451): the "For the student" lines of the latest lesson log that has some (the same lesson the student's
// Today page shows), with what is done: a chapter line is done once that chapter was played in the app on or after the
// lesson day (practice_log), any line is done when the student ticked it (homework_ticks, migrations/2026-10-12_phaseC_this-week.sql).
// Without that SQL the student's ticks are simply not shown; the app plays still are. The week ends at the next lesson log.
const HW_MARK_RE = /\s*\[(chapter|tool):([a-z0-9-]{1,40})\]\s*$/;
// the same lines as the student's Today page: list marks removed, at most 12; the key is the line as saved (with its mark)
const hwLines = (text) => String(text || "").split(/\r?\n/).map(x => x.replace(/^\s*(?:[-*•·]|\d+[.)])\s+/, "").trim()).filter(Boolean).slice(0, 12).map(line => {
  const m = HW_MARK_RE.exec(line);
  const label = (m ? line.slice(0, m.index).trim() : line) || (m ? chapterLabel(m[2]) : line);
  return { key: line.slice(0, 220), text: label.slice(0, 200), chapter: m && m[1] === "chapter" ? m[2] : null };
});
const latestHomeworkLog = (logs) => (logs || []).filter(l => l.type !== "absent" && (l.homework || "").trim())
  .sort((a, b) => String(b.date).localeCompare(String(a.date)) || (Number(b.id) || 0) - (Number(a.id) || 0))[0] || null;
function ThisWeekCard({ studentId, logs }) {
  const log = latestHomeworkLog(logs);
  const lessonDay = log ? String(log.date).slice(0, 10) : "";
  const [res, setRes] = useState(null); // null = loading, { ticks: Map|false, plays: [] }
  useEffect(() => {
    let off = false;
    setRes(null);
    if (!lessonDay) return;
    const from = new Date(lessonDay + "T00:00:00");
    Promise.all([
      _supabase.from("homework_ticks").select("item,at").eq("student_id", studentId).eq("lesson_date", lessonDay),
      _supabase.from("practice_log").select("at,drill").eq("student_id", studentId).gte("at", from.toISOString()).order("at", { ascending: true }).limit(1000),
    ]).then(([a, b]) => {
      if (off) return;
      setRes({ ticks: a.error ? false : new Map((a.data || []).map(r => [r.item, r.at])), plays: b.error ? [] : (b.data || []) });
    });
    return () => { off = true; };
  }, [studentId, lessonDay]);

  const lines = log ? hwLines(log.homework) : [];
  const status = (ln) => {
    if (!res) return null;
    if (ln.chapter) { const p = res.plays.find(r => r.drill === ln.chapter); if (p) return { how: "played", at: p.at }; }
    if (res.ticks && res.ticks.has(ln.key)) return { how: "ticked", at: res.ticks.get(ln.key) };
    return null;
  };
  const rows = lines.map(ln => ({ ...ln, st: status(ln) }));
  const nDone = rows.filter(r => r.st).length;
  const wd = (at) => new Date(at).toLocaleDateString("en-AU", { weekday: "short" });
  return (
    <section className="no-print mb-6" data-testid="this-week">
      <SecHead title="This week" right={log && res && lines.length ? <span className="text-xs px-2 py-0.5 rounded-full font-semibold" style={nDone === lines.length ? navyPill : coralPill} data-testid="this-week-count">{nDone} of {lines.length} done</span> : null}/>
      <div className="card p-5">
        {!log && <p className="text-sm text-slate-500">No homework yet. Write it under Log lesson › “For the student”; it shows here and on the student’s Today page.</p>}
        {log && (
          <>
            <p className="text-xs text-slate-500 mb-3">From the lesson on {fmtDay(new Date(lessonDay + "T12:00:00"))} · until the next lesson log</p>
            {rows.map((r, i) => (
              <div key={i} className="flex items-start justify-between gap-3" data-testid="this-week-row" style={{padding:"9px 0",borderTop: i ? "1px dashed #e3dfd2" : "none"}}>
                <span className="text-sm" style={{color: r.st ? "#7a7ca6" : "#26296b", fontWeight: 600, overflowWrap: "anywhere", minWidth: 0}}>{r.text}{r.chapter ? <span className="text-slate-400"> ↗</span> : null}</span>
                <span className="text-xs whitespace-nowrap" style={{color: r.st ? "#26296b" : "#a0a2c4", fontWeight: r.st ? 800 : 500}}>
                  {!res ? "…" : r.st ? (r.st.how === "played" ? "✓ played " : "✓ ticked ") + wd(r.st.at) : "not yet"}
                </span>
              </div>
            ))}
            {res && res.ticks === false && <p className="text-[11px] text-slate-400 mt-3">The student’s own ticks show here once migrations/2026-10-12_phaseC_this-week.sql has been run in Supabase. Chapters played in the app show already.</p>}
          </>
        )}
      </div>
    </section>
  );
}

function StudentLinkPanel({ student, logs }) {'''

rep("function StudentLinkPanel({ student }) {", COMPONENT)
rep("""      {row && <PracticeStrip studentId={student.id}/>}
      {row && <DrillProgress studentId={student.id}/>}""", """      {row && <ThisWeekCard studentId={student.id} logs={logs}/>}
      {row && <PracticeStrip studentId={student.id}/>}
      {row && <DrillProgress studentId={student.id}/>}""")
rep("      <StudentLinkPanel student={student}/>", "      <StudentLinkPanel student={student} logs={studentLogs}/>")

open(p, 'w', encoding='utf-8').write(s)
print('patched', p)
