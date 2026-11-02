p='teacher-dashboard.html'; s=open(p).read()
if 'openStatement' in s: print('already'); raise SystemExit
def rep(old, new, cnt=1):
    global s
    assert s.count(old)==cnt, (s.count(old), old[:90])
    s=s.replace(old,new)

JS = r'''
// ── m46 (her 2 Nov): the parents' statement. Nothing to write: it gathers what is already there (lesson logs, the
// student's practice check-ins, homework ticks, rooms finished in the drills) and frames it as what the child learned.
// No scores, no percentages, no streaks: 'this is what they did, they are growing'.
const CAN_DO = {
  "posture-hands": "Sits well at the piano with a rounded hand", "first-steps": "Finds the groups of black keys", "pulse": "Feels and keeps a steady beat",
  "note-names": "Knows the musical alphabet on the keys", "hand-positions": "Plays in C position with both hands", "ear-prep": "Hears high and low, loud and soft",
  "note-values": "Reads how long notes and rests last", "dynamics": "Plays loud and soft, smooth and detached", "staff": "Reads the staff and both clefs",
  "reading-steps": "Reads steps and skips", "whole-staff": "Names every line and space", "time-signatures": "Understands time signatures", "tones": "Knows tones and semitones",
  "listen-sing": "Listens and sings back short tunes", "tempo": "Knows the words for fast and slow", "rhythm": "Claps and reads rhythm patterns",
  "ledger-lines": "Reads notes above and below the staff", "scales": "Knows how a major scale is built", "scale-play": "Plays scales with smooth thumb turns",
  "minor-scales": "Knows the three kinds of minor scale", "signs": "Follows repeats and other music signs",
  "listen-write": "Hears and writes down short rhythms and tunes", "scales-1": "Plays scales over two octaves", "accidentals": "Reads sharps, flats and naturals",
  "key-signatures": "Reads key signatures", "terms": "Knows the musical terms on the page", "six-eight": "Feels and counts 6/8 time", "intervals": "Names the distance between two notes",
  "chords": "Builds and plays chords", "form": "Hears how a piece is built in sections",
  "listen-23": "Hears changes in rhythm and melody", "melody": "Shapes a phrase like a sentence", "scales-23": "Plays scales hands together with ease",
  "harmony-2": "Names intervals in major and minor keys", "rhythm-2": "Reads semiquavers and triplets",
  "listen-3": "Hears cadences and changes of key", "melody-3": "Writes a melody of her own", "scales-3": "Plays melodic minor and chromatic scales",
  "harmony-3": "Knows chords and cadences", "rhythm-3": "Reads dotted rhythms and compound time",
  "listen-4": "Hears and describes what she plays", "scales-4": "Plays scales and arpeggios in more keys", "keys-4": "Knows keys up to five sharps and flats",
  "harmony-4": "Harmonises a melody with chords", "rhythm-4": "Reads syncopation and longer bars", "melody-4": "Sets words to a melody",
  "listen-5": "Hears harmony and modulation", "scales-5": "Plays scales and arpeggios in every key", "keys-5": "Knows every key signature",
  "harmony-5": "Chooses chords for a cadence", "melody-5": "Writes a melody for a poem",
  "listen-6": "Hears and names chords and cadences", "scales-6": "Plays scales in thirds, sixths and more", "arps-6": "Plays arpeggios and chord progressions", "harmony-6": "Uses sevenths and inversions",
  "listen-7": "Listens closely and describes style", "scales-7": "Plays advanced scales fluently", "arps-7": "Plays arpeggios across the keyboard", "pieces-78": "Talks about her pieces and their composers",
  "listen-8": "Listens with a musician's ear", "scales-8": "Plays the full range of scales", "arps-8": "Plays arpeggios in every form", "pieces-8": "Knows her pieces inside out",
  "piano-story": "Knows the story of the piano", "piano-story-8": "Knows how the piano grew up", "pitch-range": "Knows the instruments and their ranges",
  "composers": "Knows composers through time", "styles": "Knows styles and genres of music",
};
const stEsc = (x) => String(x == null ? "" : x).replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" })[c]);
const stYmd = (d) => d.getFullYear() + "-" + String(d.getMonth() + 1).padStart(2, "0") + "-" + String(d.getDate()).padStart(2, "0");
const ST_PAWN = '<path d="M12 4.2a2.9 2.9 0 1 1 0 5.8a2.9 2.9 0 1 1 0-5.8zM9.6 10.8h4.8l1.3 6.2H8.3zM6.8 17.8h10.4v2.6H6.8z"/>';
const ST_QUEEN = '<path d="M3.6 8.6l3.3 7.6h10.2l3.3-7.6-4.7 3.2L12 5.6l-3.7 6.2z"/><path d="M6.4 17.2h11.2v2.8H6.4z"/>';
const ST_RATE = { "🔴": "r", "🟡": "y", "🟢": "g" };
function stBoard(y, m, S, played, lessons, from, to) {
  const first = new Date(y, m, 1), nd = new Date(y, m + 1, 0).getDate(), off = (first.getDay() + 6) % 7, rows = Math.ceil((off + nd) / 7);
  let g = '<svg viewBox="0 0 ' + (7 * S + 4) + ' ' + (rows * S + 22) + '" width="100%">';
  "MTWTFSS".split("").forEach((c, i) => { g += '<text x="' + (2 + i * S + S / 2) + '" y="11" text-anchor="middle" font-size="9" font-weight="800" fill="#9a9cc0">' + c + '</text>'; });
  for (let r = 0; r < rows; r++) for (let c = 0; c < 7; c++) {
    const x = 2 + c * S, yy = 16 + r * S, d = r * 7 + c - off + 1;
    const dk = (r + c) % 2 === 1;   /* her 2 Nov: a navy board */
    g += '<rect x="' + x + '" y="' + yy + '" width="' + S + '" height="' + S + '" fill="' + (dk ? "#26296b" : "#fbf8f1") + '"/>';
    if (d < 1 || d > nd) continue;
    const k = stYmd(new Date(y, m, d));
    g += '<text x="' + (x + 2.5) + '" y="' + (yy + 8.5) + '" font-size="7" fill="' + (dk ? "#8f92c4" : "#9a9cc0") + '">' + d + '</text>';
    if (k < from || k > to) continue;
    const sc = S / 24 * 0.78, tx = x + S / 2 - 12 * sc, ty = yy + S / 2 - 11 * sc;
    if (lessons.has(k)) g += '<g transform="translate(' + tx.toFixed(1) + ' ' + ty.toFixed(1) + ') scale(' + sc.toFixed(3) + ')" fill="#e4572e">' + ST_QUEEN + '</g>';
    else if (played.has(k)) g += '<g transform="translate(' + tx.toFixed(1) + ' ' + ty.toFixed(1) + ') scale(' + sc.toFixed(3) + ')" fill="' + (dk ? "#fbf8f1" : "#26296b") + '">' + ST_PAWN + '</g>';
  }
  return g + '<rect x="1" y="15" width="' + (7 * S + 2) + '" height="' + (rows * S + 2) + '" fill="none" stroke="#26296b" stroke-width="1.6"/></svg>';
}
async function openStatement(student, logs, months, note) {
  const w = window.open("", "_blank");
  if (!w) { alert("Please allow pop-ups to open the statement."); return; }
  w.document.write('<p style="font-family:sans-serif;padding:24px;color:#26296b">Preparing the statement…</p>');
  const end = new Date(), sorted = logs.slice().sort((a, b) => (a.date < b.date ? -1 : 1));
  const start = months ? new Date(end.getFullYear(), end.getMonth() - months, end.getDate() + 1) : (sorted.length ? new Date(sorted[0].date + "T12:00:00") : end);
  const from = stYmd(start), to = stYmd(end), first = String(student.name || "").split(" ")[0] || "Your child";
  const L = sorted.filter(l => l.date >= from && l.date <= to);
  let checks = [], ticks = [], st = {}, plog = [];
  try {
    const [a, b, c, d] = await Promise.all([
      _supabase.from("practice_checkins").select("day,minutes").eq("student_id", student.id).gte("day", from),
      _supabase.from("homework_ticks").select("lesson_date,item").eq("student_id", student.id).gte("lesson_date", from),
      _supabase.from("progress_store").select("store,value").eq("student_id", student.id).in("store", ["lesson_steps", "steps_total"]),
      _supabase.from("practice_log").select("at,drill").eq("student_id", student.id).gte("at", start.toISOString()).limit(5000),
    ]);
    checks = (a && a.data) || []; ticks = (b && b.data) || []; ((c && c.data) || []).forEach(r => { st[r.store] = r.value; }); plog = (d && d.data) || [];
  } catch (e) {}
  // what they can do: every room finished, in the house's order; the ones worked on in this period marked new
  const steps = st.lesson_steps && typeof st.lesson_steps === "object" ? st.lesson_steps : {}, tot = st.steps_total && typeof st.steps_total === "object" ? st.steps_total : {};
  const touched = new Set(plog.map(r => r.drill));
  L.forEach(l => String(l.homework || "").split("\n").forEach(x => { const m = /\[chapter:([a-z0-9-]+)\]/.exec(x); if (m) touched.add(m[1]); }));
  const rooms = DRILL_LINKS.chapters.filter(c => { const dn = Object.values(steps[c.id] || {}).filter(Boolean).length, t = +tot[c.id] || 0; return t > 0 && dn >= t; });
  const fresh = rooms.filter(c => touched.has(c.id)), shown = (fresh.length ? fresh : rooms).slice(-8);
  const more = rooms.length - shown.length;
  // pieces: each piece's ratings, lesson by lesson
  const pieces = new Map();
  L.forEach(l => String(l.repertoire || "").split("\n").forEach(line => { const m = /^([🔴🟡🟢])\s*(.+)$/u.exec(line.trim()); const name = (m ? m[2] : line.trim()); if (!name) return; if (!pieces.has(name)) pieces.set(name, []); if (m) pieces.get(name).push(ST_RATE[m[1]]); }));
  const pc = [...pieces.entries()].filter(([, r]) => r.length).slice(-6);
  // the boards
  const played = new Set(checks.map(c => String(c.day).slice(0, 10))), lessonDays = new Set(L.filter(l => !noLesson(l)).map(l => l.date));
  const monthsList = []; for (let d = new Date(start.getFullYear(), start.getMonth(), 1); d <= end; d = new Date(d.getFullYear(), d.getMonth() + 1, 1)) monthsList.push([d.getFullYear(), d.getMonth()]);
  const per = monthsList.length <= 3 ? 3 : 4, S = per === 3 ? 38 : 30, hasLink = checks.length > 0;
  const boards = monthsList.map(([y, m]) => '<div class="b"><b>' + new Date(y, m, 1).toLocaleDateString("en-GB", { month: "long" }) + (monthsList.length > 4 && m === 0 ? " " + y : "") + '</b>' + stBoard(y, m, S, played, lessonDays, from, to) + '</div>').join("");
  const nowPiece = (() => { for (let i = L.length - 1; i >= 0; i--) { const x = String(L[i].repertoire || "").split("\n").map(z => z.replace(/^[🔴🟡🟢]\s*/u, "").trim()).filter(Boolean); if (x.length) return x[0]; } return ""; })();
  const lastRoom = shown.length ? shown[shown.length - 1].label : "";
  const help = [nowPiece ? "Ask " + first + " to play you " + nowPiece + ", and just listen." : "Ask " + first + " to play you something new, and just listen.",
    "A few short sessions a week help more than one long one.",
    lastRoom ? "Ask " + first + " to teach you something from " + lastRoom + "." : "Ask " + first + " what the lesson was about this week."];
  const dot = (c) => '<i class="d ' + c + '"></i>';
  const fmt = (k, o) => new Date(k + "T12:00:00").toLocaleDateString("en-GB", o);
  const label = months === 3 ? "three months" : months === 6 ? "six months" : months === 12 ? "year" : "lessons so far";
  const tickBy = {}; ticks.forEach(t => { const k = String(t.lesson_date).slice(0, 10); tickBy[k] = (tickBy[k] || 0) + 1; });
  const rowsHtml = L.slice().reverse().map(l => {
    const off = noLesson(l), hw = String(l.homework || "").split("\n").map(x => hwPlain(x).replace(/\s*\[(chapter|tool):[a-z0-9-]+\]$/, "")).filter(x => x && !HW_KEYS_RE.test(x));
    const ps = String(l.repertoire || "").split("\n").map(x => x.trim()).filter(Boolean).map(x => { const m = /^([🔴🟡🟢])\s*(.+)$/u.exec(x); return (m ? dot(ST_RATE[m[1]]) : "") + stEsc(m ? m[2] : x); }).join(" · ");
    const n = tickBy[l.date] || 0;
    return '<div class="lr"><span class="dt">' + (off ? "" : '<svg viewBox="0 0 24 24" width="12" fill="#e4572e">' + ST_QUEEN + '</svg> ') + fmt(l.date, { weekday: "short", day: "numeric", month: "short" }) + '</span><span>'
      + (off ? '<span style="color:#9a9cc0">No lesson' + (l.reason ? " (" + stEsc(l.reason) + ")" : "") + '</span>' : (l.type === "makeup" ? '<small class="mk">Makeup</small> ' : "") + (ps || '<span style="color:#9a9cc0">Lesson</span>') + (hw.length ? '<small>' + stEsc(hw.join(" · ")) + '</small>' : ""))
      + '</span><span class="k">' + (!off && hw.length && n ? Math.min(n, hw.length) + "/" + hw.length : "") + '</span></div>';
  }).join("");
  const css = 'body{margin:0;background:#eee;font-family:Inter,system-ui,-apple-system,sans-serif;color:#26296b}.pg{width:794px;min-height:1080px;background:#fbf8f1;margin:16px auto;padding:44px 52px;box-sizing:border-box}'
    + '.ser{font-family:Georgia,serif}.lab{font-size:10.5px;font-weight:800;letter-spacing:.1em;text-transform:uppercase;color:#e4572e;margin:24px 0 8px}'
    + '.note{margin-top:18px;background:#fff;border-left:4px solid #e4572e;border-radius:8px;padding:12px 16px;font-family:Georgia,serif;font-size:15px;line-height:1.5;font-style:italic}'
    + '.cds{display:grid;grid-template-columns:1fr 1fr;gap:4px 22px}.cd{display:flex;gap:10px;align-items:flex-start;padding:6px 0;border-bottom:1px solid #eee8da}.tk{flex:none;width:20px;height:20px;border-radius:50%;background:#2e8a6e;color:#fff;font-size:12px;font-weight:900;display:flex;align-items:center;justify-content:center}.cd b{font-size:13.5px;display:block}.cd small{font-size:11px;color:#9a9cc0}'
    + '.pc{display:flex;align-items:center;gap:12px;padding:8px 0;border-bottom:1px solid #eee8da}.pc b{width:170px;font-size:13.5px}.sts{flex:1;display:flex;align-items:center}.st{width:15px;height:15px;border-radius:50%;flex:none;box-sizing:border-box}.ln{flex:1;height:3px;background:#e1dccd}'
    + '.r{background:#fff;border:2px solid #26296b}.y{background:#f2b3a3}.g{background:#2e8a6e}.d{display:inline-block;width:9px;height:9px;border-radius:50%;margin-right:3px;box-sizing:border-box}'
    + '.bs{display:grid;grid-template-columns:repeat(' + per + ',1fr);gap:14px}.b b{display:block;font-family:Georgia,serif;font-size:14px;margin-bottom:2px}'
    + '.leg{display:flex;gap:16px;font-size:11.5px;color:#7a7ca6;margin-top:6px;align-items:center}.hp{display:grid;gap:6px;font-size:13px}.hp div{background:#fff;border-radius:8px;padding:8px 12px 8px 26px;position:relative}.hp div:before{content:"";position:absolute;left:12px;top:14px;width:6px;height:6px;border-radius:50%;background:#e4572e}'
    + '.lh,.lr{display:grid;grid-template-columns:130px 1fr 50px;gap:8px}.lh{font-size:10px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:#9a9cc0;border-bottom:1.5px solid #26296b;padding-bottom:5px}.lr{padding:7px 0;border-bottom:1px solid #eee8da;font-size:12.5px;align-items:start}.lr .dt{font-weight:700}.lr small{display:block;color:#7a7ca6;font-size:11.5px;margin-top:1px}.lr small.mk{display:inline;color:#2e8a6e;font-weight:800}.lr .k{text-align:right;font-weight:700;color:#2e8a6e}'
    + '.foot{margin-top:22px;display:flex;justify-content:space-between;font-size:10.5px;color:#9a9cc0;border-top:1px solid #e1dccd;padding-top:8px}.bar{text-align:center;margin:12px}.bar button{font:700 14px Inter,sans-serif;background:#26296b;color:#fff;border:none;border-radius:99px;padding:10px 22px;cursor:pointer}'
    + '@media print{body{background:#fff}.pg{margin:0;width:auto;min-height:0;page-break-after:always;padding:14mm 14mm}.bar{display:none}@page{size:A4;margin:0}}';
  const p1 = '<div class="pg"><div style="display:flex;justify-content:space-between;align-items:center"><div><div class="ser" style="font-size:28px;font-weight:700">' + stEsc(first) + '’s ' + label + '</div><div style="font-size:13px;color:#7a7ca6">' + fmt(from, { day: "numeric", month: "long", year: "numeric" }) + ' – ' + fmt(to, { day: "numeric", month: "long", year: "numeric" }) + ' · Piano Butler</div></div></div>'
    + (note && note.trim() ? '<div class="note">' + stEsc(note.trim()) + '</div>' : "")
    + (rooms.length ? '<div class="lab">What ' + stEsc(first) + ' can do now</div><div class="cds">' + shown.map(c => '<div class="cd"><span class="tk">✓</span><div><b>' + stEsc(CAN_DO[c.id] || c.label) + '</b><small>' + stEsc(c.label) + '</small></div></div>').join("") + '</div>' + (more > 0 ? '<div style="font-size:11.5px;color:#9a9cc0;margin-top:6px">and ' + more + ' more rooms finished before</div>' : "") : "")
    + (pc.length ? '<div class="lab">' + stEsc(first) + '’s pieces, growing</div>' + pc.map(([name, r]) => '<div class="pc"><b>' + stEsc(name) + '</b><div class="sts">' + r.slice(-8).map(c => '<span class="st ' + c + '"></span>').join('<span class="ln"></span>') + '</div></div>').join("")
      + '<div class="leg"><span><span class="st r" style="display:inline-block;width:11px;height:11px;vertical-align:-2px"></span> needs work</span><span><span class="st y" style="display:inline-block;width:11px;height:11px;vertical-align:-2px"></span> progressing</span><span><span class="st g" style="display:inline-block;width:11px;height:11px;vertical-align:-2px"></span> solid</span></div>' : "")
    + '<div class="lab">When ' + stEsc(first) + ' played</div><div class="bs">' + boards + '</div><div class="leg">' + (hasLink ? '<span><svg viewBox="0 0 24 24" width="14" fill="#26296b">' + ST_PAWN + '</svg> played at home</span>' : "") + '<span><svg viewBox="0 0 24 24" width="14" fill="#e4572e">' + ST_QUEEN + '</svg> lesson</span></div>'
    + '<div class="lab">Ways to help at home</div><div class="hp">' + help.map(x => '<div>' + stEsc(x) + '</div>').join("") + '</div>'
    + '<div class="foot"><span>' + lessonDays.size + ' lessons in this period</span><span>Page 1</span></div></div>';
  const p2 = L.length ? '<div class="pg"><div style="display:flex;justify-content:space-between;font-size:12px;color:#7a7ca6"><span class="ser" style="font-size:18px;color:#26296b;font-weight:700">' + stEsc(student.name) + ' · lesson by lesson</span><span>' + fmt(from, { day: "numeric", month: "short" }) + ' – ' + fmt(to, { day: "numeric", month: "short", year: "numeric" }) + '</span></div><div style="height:14px"></div>'
    + '<div class="lh"><span>Lesson</span><span>Pieces · homework</span><span style="text-align:right">Done</span></div>' + rowsHtml
    + '<div class="foot"><span>Done = homework ticked on the student’s page.</span><span>Page 2</span></div></div>' : "";
  w.document.open();
  w.document.write('<!doctype html><html><head><meta charset="utf-8"><title>' + stEsc(first) + ' · Piano Butler statement</title><style>' + css + '</style></head><body><div class="bar"><button onclick="window.print()">Print or save as PDF</button></div>' + p1 + p2 + '</body></html>');
  w.document.close();
}
function StatementButton({ student, logs }) {
  const [m, setM] = useState(3);
  const [note, setNote] = useState("");
  const [busy, setBusy] = useState(false);
  const chip = (v, t) => <button key={t} type="button" onClick={() => setM(v)} style={{ fontSize: 12, fontWeight: 700, padding: "4px 11px", borderRadius: 99, cursor: "pointer", border: "1px solid " + (m === v ? "#26296b" : "#e9e2d2"), background: m === v ? "#26296b" : "white", color: m === v ? "white" : "#62649a" }}>{t}</button>;
  return (
    <div data-testid="statement" style={{ border: "1px solid #e9e2d2", borderRadius: 14, background: "#fffefa", padding: 12, marginBottom: 14 }}>
      <p style={{ fontSize: 11, fontWeight: 800, letterSpacing: "0.08em", textTransform: "uppercase", color: "#e4572e", margin: "0 0 6px" }}>Statement for parents</p>
      <div style={{ display: "flex", gap: 6, flexWrap: "wrap", marginBottom: 8 }}>{chip(3, "3 months")}{chip(6, "6 months")}{chip(12, "1 year")}{chip(0, "All")}</div>
      <input value={note} onChange={e => setNote(e.target.value)} placeholder="A line from you (optional)" className="input text-sm" style={{ marginBottom: 8 }}/>
      <button type="button" data-testid="statement-open" disabled={busy} onClick={async () => { setBusy(true); try { await openStatement(student, logs, m, note); } finally { setBusy(false); } }}
        style={{ width: "100%", background: "#26296b", color: "white", border: "none", borderRadius: 10, padding: "9px", fontWeight: 800, fontSize: 13, cursor: "pointer" }}>{busy ? "Preparing…" : "Open statement"}</button>
      <p style={{ fontSize: 11, color: "#9a9cc0", margin: "6px 0 0" }}>What they learned, their pieces and when they played. Nothing for you to fill in.</p>
    </div>
  );
}
'''
rep("// m45 (her 2 Nov: 'easier to pick')", JS.strip('\n') + "\n// m45 (her 2 Nov: 'easier to pick')")
rep("      {/* ── Progress Passport ── */}", "      <StatementButton student={student} logs={studentLogs}/>   {/* m46 */}\n      {/* ── Progress Passport ── */}")
open(p,'w').write(s); print('ok')
