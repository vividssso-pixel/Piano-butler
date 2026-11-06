#!/usr/bin/env python3
# Phase 476, the teacher dashboard: the student's keys (her 2026-10-17 02:05 '1.2.3. 다동의해', decision 2: the teacher sets
# "this student's keys"; default the exam keys; all twelve possible). Log lesson › For the student gets the twelve major
# keys (circle-of-fifths order, two rows of six). Saved as one line [keys:C,G,D] at the start of the homework (so the
# 1500-character cap trims homework text, never the line); cleared after being set: [keys:-] (the drills go back to the
# chapter's keys). A lesson with no homework and unchanged keys stores no line (so the student's Today keeps last week's
# list, as before). The line is not a homework item: the editor and This week leave it out; the history shows 'Keys: ...'.
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    if s.count(a) != n: raise SystemExit('found %d: %s' % (s.count(a), a[:90]))
    s = s.replace(a, b)

# 1. the keys: helpers and the picker, before the drills' links
rep("""// Chapters and practice activities of the drills that the teacher can attach to "For the student" (the student's Today page""",
"""// The student's keys (Phase 476): chapters 16 and 19 (Scales, Key Signatures) open and close with a map of all twelve keys;
// the student's keys are marked there and drill level 10 asks about them. Saved as a line [keys:C,G,D] in "For the student"
// (the drills store it and leave it out of the Today list); [keys:-]: none (back to the chapter's keys), carried with each
// homework after a clear. The names are the drills' own (G♭ for F♯; a typed F#, c or B♭ is read as the drills read it).
const KEYS_FIFTHS = ["C", "G", "D", "A", "E", "B", "Gb", "Db", "Ab", "Eb", "Bb", "F"];
const KEY_LABEL = { Gb: "G♭", Db: "D♭", Ab: "A♭", Eb: "E♭", Bb: "B♭" };
const KEY_ALIAS = { "C#": "Db", "D#": "Eb", "F#": "Gb", "G#": "Ab", "A#": "Bb", Cb: "B", Fb: "E", "E#": "F", "B#": "C" };
const keyId = (k) => { const x = String(k || "").trim().replace(/♯/g, "#").replace(/♭/g, "b"), n = x ? x[0].toUpperCase() + x.slice(1) : ""; return KEYS_FIFTHS.includes(n) ? n : KEY_ALIAS[n] || null; };
const HW_KEYS_RE = /^\\s*\\[keys:([^\\]]{0,80})\\]\\s*$/;
const hwPlain = (x) => String(x).replace(/^\\s*(?:[-*•·]|\\d+[.)])\\s+/, "").trim();   // a homework line without its list mark
// -> null (no keys line), [] ([keys:-]) or the keys, in circle-of-fifths order
const keysOf = (text) => { const ln = String(text || "").split(/\\r?\\n/).map(hwPlain).find(x => HW_KEYS_RE.test(x)); if (!ln) return null; const k = HW_KEYS_RE.exec(ln)[1].split(/[\\s,]+/).map(keyId); return KEYS_FIFTHS.filter(x => k.includes(x)); };
const latestKeys = (logs) => { for (const l of [...(logs || [])].sort((a, b) => String(b.date).localeCompare(String(a.date)) || (Number(b.id) || 0) - (Number(a.id) || 0))) { const k = keysOf(l.homework); if (k) return k; } return null; };   // null: never set
const keysLineShow = (text) => String(text || "").replace(/^\\s*(?:(?:[-*•·]|\\d+[.)])\\s+)?\\[keys:([^\\]]{0,80})\\]\\s*$/m, (m) => { const ks = keysOf(m) || []; return ks.length ? "Keys: " + ks.map(x => KEY_LABEL[x] || x).join(" ") : "Keys: the chapters' own"; });
function KeysField({ keys, onChange }) {
  const on = new Set(keys);
  const chip = (active) => ({ minHeight: 44, padding: "4px 6px", borderRadius: 99, border: "1.5px solid " + (active ? "#26296b" : "#d9d3c4"), background: active ? "#26296b" : "#fff", color: active ? "#fff" : "#26296b", fontWeight: 800, fontSize: 13, cursor: "pointer" });
  return (
    <div data-testid="keys-field">
      <div className="flex items-center justify-between gap-2" style={{ marginBottom: 6 }}>
        <span className="field-label" style={{ color: "#26296b", marginBottom: 0 }}>Keys (scales and key signatures)</span>
        <span style={{ display: "flex", gap: 6 }}>
          <button type="button" data-keys="all" onClick={() => onChange(KEYS_FIFTHS.slice())} className="btn-ghost text-xs py-1 px-3">All 12</button>
          <button type="button" data-keys="none" onClick={() => onChange([])} className="btn-ghost text-xs py-1 px-3">Clear</button>
        </span>
      </div>
      <div style={{ display: "grid", gridTemplateColumns: "repeat(6, minmax(0, 1fr))", gap: 6 }}>
        {KEYS_FIFTHS.map(k => (
          <button type="button" key={k} data-key={k} aria-pressed={on.has(k)} onClick={() => onChange(KEYS_FIFTHS.filter(x => x === k ? !on.has(x) : on.has(x)))} style={chip(on.has(k))}>
            {KEY_LABEL[k] || k}
          </button>
        ))}
      </div>
      <p style={{ margin: "6px 0 0", fontSize: 11, color: "#7a7ca6", lineHeight: 1.5 }}>On the student's twelve-key maps (chapters 16 and 19) and drill level 10. None picked: each chapter's own keys. G♭ is played on the same keys as F♯; key signatures use G♭ (six flats).</p>
    </div>
  );
}

// Chapters and practice activities of the drills that the teacher can attach to "For the student" (the student's Today page""")

# 2. the editor's list leaves the keys line out
rep("""  const lines = String(text || "").split(/\\r?\\n/).map(x => x.trim()).filter(Boolean);
  if (!lines.length) return [{ t: "", r: "" }];""", """  const lines = String(text || "").split(/\\r?\\n/).map(x => x.trim()).filter(x => x && !(withLinks && HW_KEYS_RE.test(hwPlain(x))));
  if (!lines.length) return [{ t: "", r: "" }];""")

# 3. the modal: the keys (from this log, else the student's latest); the line first; only when it says something
rep("function LogModal({ student, existingLog, currentMonth, lastLog, onSave, onClose }) {", "function LogModal({ student, existingLog, currentMonth, lastLog, keysNow, onSave, onClose }) {")
rep("""  const save = () => onSave({ ...f, repertoire: joinItems(lists.rep, true), technical: joinItems(lists.tech), srAural: joinItems(lists.sr), gk: joinItems(lists.gk), homework: joinItems(lists.hw) });""",
"""  const own = keysOf(existingLog?.homework);   // this log's own keys line (null: none)
  const [keys, setKeys] = useState(() => own != null ? own : (keysNow || []));
  // the keys line: with homework, or when it changes the keys, or when this log had one; [keys:-] when keys set before are cleared
  const keysLine = (hw) => { const now = keysNow || [], changed = keys.join() !== now.join();
    if (keys.length) return (hw || changed || own != null) ? "[keys:" + keys.join(",") + "]" : "";
    return (now.length || own != null || (hw && keysNow != null)) ? "[keys:-]" : ""; };   // once cleared, the clear goes on with each homework
  const save = () => { const hw = joinItems(lists.hw); onSave({ ...f, repertoire: joinItems(lists.rep, true), technical: joinItems(lists.tech), srAural: joinItems(lists.sr), gk: joinItems(lists.gk), homework: [keysLine(hw), hw].filter(Boolean).join("\\n") }); };""")
rep("""            hint="This week's homework. Shows on the student's Today page when they have a student link. A chapter or activity gets an Open button. Your notes below stay private."
/>
""", """            hint="This week's homework. Shows on the student's Today page when they have a student link. A chapter or activity gets an Open button. Your notes below stay private."
/>
          <KeysField keys={keys} onChange={setKeys}/>
""")
rep("""  const lastHint = !existingLog ? ((lastLog?.homework || "").trim() || (lastLog?.notes || "").trim()) : "";""",
    """  const lastHint = !existingLog ? (keysLineShow(lastLog?.homework || "").replace(/\\s*\\[(?:chapter|tool):[a-z0-9-]+\\]/g, " ↗").trim() || (lastLog?.notes || "").trim()) : "";""")
rep("""          lastLog={!editLog ? logs.filter(l=>l.studentId===logging.id).sort((a,b)=>b.date.localeCompare(a.date))[0] : null}
""", """          lastLog={!editLog ? logs.filter(l=>l.studentId===logging.id).sort((a,b)=>b.date.localeCompare(a.date))[0] : null}
          keysNow={latestKeys(logs.filter(l=>l.studentId===logging.id))}
""")

# 4. This week: the keys line is not a line to tick (the week's log is chosen as before: the server does the same)
rep("""const hwLines = (text) => String(text || "").split(/\\r?\\n/).map(x => x.replace(/^\\s*(?:[-*•·]|\\d+[.)])\\s+/, "").trim()).filter(Boolean).slice(0, 12).map(line => {""",
    """const hwLines = (text) => String(text || "").split(/\\r?\\n/).map(x => x.replace(/^\\s*(?:[-*•·]|\\d+[.)])\\s+/, "").trim()).filter(x => x && !HW_KEYS_RE.test(x)).slice(0, 12).map(line => {""")

# 5. the log history: the keys line in words
rep("""{s.key === "homework" ? String(log[s.key]).replace(/\\s*\\[(?:chapter|tool):[a-z0-9-]+\\]/g, " ↗") : log[s.""",
    """{s.key === "homework" ? keysLineShow(String(log[s.key])).replace(/\\s*\\[(?:chapter|tool):[a-z0-9-]+\\]/g, " ↗") : log[s.""")
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
