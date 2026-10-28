import sys, json
src, dst, house = sys.argv[1], sys.argv[2], sys.argv[3]
s = open(src, encoding='utf-8').read()
H = json.load(open(house, encoding='utf-8'))
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:100])
    s = s.replace(old, new)
floors = [{ 'name': f['name'], 'extra': 1 if f['extra'] else 0, 'rooms': [[r[0], r[1], r[2], r[3], r[4]] for r in f['rooms']] } for f in H['floors']]
data = json.dumps({ 'floors': floors, 'cps': H['cps'] }, ensure_ascii=False, separators=(',', ':'))
CODE = r"""// ─── Build CS (board call 8): where the student starts in the drills, and their chapter checks ───────────────
// The drills send two more kinds of progress through the student's link: 'checks' (each chapter check, floor checkpoint
// and review) and 'place' (the "Where should you start?" round). You set the student's own start here (student_plan); the
// drills take it the next time the student opens their link: the house starts on that floor, theory rooms above the theory
// grade wait, and a floor checkpoint asks theory only up to that grade. "Show the Home" is for adults: children see the
// music map and Practice. All of it needs migrations/2026-10-28_phaseD_checks-and-plan.sql (run once in Supabase).
// DRILLS_HOUSE comes from the drills build (sc/housedata.js): floors, rooms [id, chapter no, name, theory grade, has a check].
const DRILLS_HOUSE = __DATA__;
const dhFloorName = (k) => { const f = DRILLS_HOUSE.floors[k]; return f ? "Floor " + (k + 1) + " · " + f.name : "—"; };
const dhRoom = (id) => { for (const f of DRILLS_HOUSE.floors) { const r = f.rooms.find(x => x[0] === id); if (r) return r; } return null; };
const dhRoomName = (id) => { const r = dhRoom(id); return r ? r[1] + " · " + r[2] : String(id); };
const dhTheoryName = (n) => n >= 7 ? "every theory grade" : "Theory Grade " + n;
const dhDate = (ms) => { try { return new Date(ms).toLocaleDateString("en-AU", { day: "numeric", month: "short" }); } catch (e) { return ""; } };
function DrillStartChecks({ studentId }) {
  const [d, setD] = useState(null);   // null = loading; { checks, place, plan, planOk }
  const [form, setForm] = useState({ piano: "", theory: "", home: false });
  const [busy, setBusy] = useState(false);
  const [msg, setMsg] = useState("");
  useEffect(() => {
    let off = false;
    setD(null); setMsg("");
    Promise.all([
      _supabase.from("progress_store").select("store,value,updated_at").eq("student_id", studentId).in("store", ["checks", "place"]),
      _supabase.from("student_plan").select("plan,updated_at").eq("student_id", studentId).maybeSingle(),
    ]).then(([a, b]) => {
      if (off) return;
      const st = {}; (a.data || []).forEach(r => { st[r.store] = r.value; });
      const plan = !b.error && b.data && isObj(b.data.plan) ? b.data.plan : null;
      setD({ checks: isObj(st.checks) ? st.checks : null, place: isObj(st.place) ? st.place : null, plan, planOk: !b.error });
      setForm({ piano: plan && Number.isInteger(plan.piano) ? String(plan.piano) : "", theory: plan && plan.theory ? String(plan.theory) : "", home: !!(plan && plan.home) });
    });
    return () => { off = true; };
  }, [studentId]);
  if (!d) return null;
  const { checks, place, plan } = d;
  const rooms = checks && isObj(checks.rooms) ? checks.rooms : {}, cpRec = checks && isObj(checks.floors) ? checks.floors : {};
  const now = Date.now();
  const passed = (id) => isObj(rooms[id]) && rooms[id].pass > 0;
  const due = Object.keys(rooms).filter(id => isObj(rooms[id]) && isObj(rooms[id].review) && rooms[id].review.stage < 3 && rooms[id].review.due <= now);
  const floorRows = DRILLS_HOUSE.floors.map((f, k) => {
    if (f.extra) return null;
    const ids = f.rooms.filter(r => r[4]).map(r => r[0]);
    const cps = DRILLS_HOUSE.cps.filter(c => c.k === k).map(c => ({ ...c, rec: isObj(cpRec[c.key]) ? cpRec[c.key] : null }));
    const n = ids.filter(passed).length, review = [...new Set(cps.flatMap(c => c.rec && Array.isArray(c.rec.review) ? c.rec.review : []))];
    if (!n && !cps.some(c => c.rec)) return null;
    return { k, n, of: ids.length, cps, review };
  }).filter(Boolean);
  const nPassed = Object.keys(rooms).filter(passed).length, nCheckable = DRILLS_HOUSE.floors.reduce((a, f) => a + (f.extra ? 0 : f.rooms.filter(r => r[4]).length), 0);
  const effFloor = plan && Number.isInteger(plan.piano) ? plan.piano : place && place.piano >= 0 ? place.piano : null;
  const effTheory = plan && plan.theory ? plan.theory : place && place.theory ? place.theory : null;
  async function save() {
    setBusy(true); setMsg("");
    const p = {}; if (form.piano !== "") p.piano = +form.piano; if (form.theory !== "") p.theory = +form.theory; if (form.home) p.home = true;
    const q = Object.keys(p).length
      ? _supabase.from("student_plan").upsert({ student_id: studentId, plan: p, updated_at: new Date().toISOString() }).select().single()
      : _supabase.from("student_plan").delete().eq("student_id", studentId);
    const { error } = await q;
    setBusy(false);
    if (error) { setMsg("Could not save: " + error.message); return; }
    setD(x => ({ ...x, plan: Object.keys(p).length ? p : null }));
    setMsg("Saved. The drills follow it the next time the student opens their link.");
  }
  const sel = { border: "1px solid #e9e2d2", borderRadius: 10, padding: "7px 10px", fontSize: 13, background: "#fff", color: "#26296b", maxWidth: "100%" };
  const lab = { display: "block", fontSize: 10, fontWeight: 700, letterSpacing: "0.06em", textTransform: "uppercase", color: "#7a7ca6", marginBottom: 4 };
  const th = { textAlign: "left", fontSize: 10, fontWeight: 700, color: "#7a7ca6", textTransform: "uppercase", letterSpacing: "0.05em", padding: "0 10px 6px 0", whiteSpace: "nowrap" };
  const td = { fontSize: 13, color: "#34377b", padding: "8px 10px 8px 0", borderTop: "1px solid #efe9d9", verticalAlign: "top" };
  return (
    <section className="no-print mb-6" data-testid="drill-start">
      <SecHead title="Start and checks" right={nPassed ? <span className="text-xs font-bold" style={{color:"#26296b"}}>{"★ " + nPassed + " of " + nCheckable + " chapters"}</span> : null}/>
      <div className="card p-5">
        <DashBlock title="Where to start" note="the student’s placement and your setting" testid="drill-start-where">
          <p className="text-sm mb-3" style={{color:"#26296b"}} data-testid="drill-place">
            {place ? <>Placement, {dhDate(place.at)}: <b>piano {dhFloorName(place.piano)}</b> · <b>{dhTheoryName(place.theory || 1)}</b></>
                   : <span className="text-slate-500">No placement yet. The student can take it on their music map: “Where should I start?”</span>}
          </p>
          {d.planOk ? (
            <div style={{display:"flex",flexWrap:"wrap",gap:10,alignItems:"flex-end"}}>
              <label style={{minWidth:0}}><span style={lab}>Start floor</span>
                <select style={sel} value={form.piano} onChange={e => setForm(f => ({ ...f, piano: e.target.value }))} data-testid="plan-floor">
                  <option value="">{place ? "Their placement" : "From the bottom"}</option>
                  {DRILLS_HOUSE.floors.map((f, k) => f.extra ? null : <option key={k} value={String(k)}>{dhFloorName(k)}</option>)}
                </select></label>
              <label style={{minWidth:0}}><span style={lab}>Theory grade</span>
                <select style={sel} value={form.theory} onChange={e => setForm(f => ({ ...f, theory: e.target.value }))} data-testid="plan-theory">
                  <option value="">{place ? "Their placement" : "Not set"}</option>
                  {[1,2,3,4,5,6].map(n => <option key={n} value={String(n)}>{"Theory Grade " + n}</option>)}
                  <option value="7">All theory done</option>
                </select></label>
              <label className="text-sm" style={{display:"flex",gap:6,alignItems:"center",color:"#26296b",padding:"0 0 7px"}}>
                <input type="checkbox" checked={form.home} onChange={e => setForm(f => ({ ...f, home: e.target.checked }))} data-testid="plan-home"/> Show the Home (adults)</label>
              <button className="btn-primary text-xs py-2 px-4" disabled={busy} onClick={save} data-testid="plan-save">{busy ? "Saving…" : "Save"}</button>
            </div>
          ) : (
            <p className="text-xs rounded-lg p-2" style={{background:"#faf6ec",border:"1px solid #efe9d9",color:"#62649a"}} data-testid="plan-needs-sql">Setting the start needs one database step: run migrations/2026-10-28_phaseD_checks-and-plan.sql once in Supabase (SQL Editor). Until then the drills use the student’s own placement.</p>
          )}
          {(effFloor != null || effTheory) && <p className="text-xs mt-3" style={{color:"#62649a"}} data-testid="plan-effect">
            The drills now start them on <b style={{color:"#26296b"}}>{effFloor != null ? dhFloorName(effFloor) : "Floor 1 · Beginner"}</b>{effTheory && effTheory < 7 ? <>, with theory up to <b style={{color:"#26296b"}}>{dhTheoryName(effTheory)}</b></> : null}.</p>}
          {msg && <p className="text-xs mt-2" style={{color: /Could not/.test(msg) ? "#c0431f" : "#26296b"}} role="status">{msg}</p>}
        </DashBlock>
        <DashBlock title="Chapter checks" note="★ = passed: 8 or more of 10" testid="drill-checks">
          {!floorRows.length ? <p className="text-sm text-slate-500" data-testid="checks-empty">No checks yet. They appear here when the student does a chapter check or a floor checkpoint through their link.</p> : (
            <div style={{overflowX:"auto"}}>
              <table style={{width:"100%",borderCollapse:"collapse"}}>
                <thead><tr><th style={th}>Floor</th><th style={th}>Chapters passed</th><th style={th}>Checkpoint</th><th style={th}>To review</th></tr></thead>
                <tbody>{floorRows.map(r => (
                  <tr key={r.k} data-floor={r.k}>
                    <td style={{...td,fontWeight:700,whiteSpace:"nowrap"}}>{dhFloorName(r.k)}</td>
                    <td style={td}><span style={{fontWeight:800,color: r.n === r.of ? "#2e8a6e" : "#26296b"}}>{"★ " + r.n}</span><span style={{color:"#7a7ca6"}}>{" of " + r.of}</span></td>
                    <td style={td}>{r.cps.map(c => <div key={c.key} style={{whiteSpace:"nowrap"}}>{c.part ? (c.part === 1 ? "1st half: " : "2nd half: ") : ""}{c.rec ? dhDate(c.rec.at) + " · " + c.rec.right + "/" + c.rec.total : <span style={{color:"#a3a5c2"}}>not yet</span>}</div>)}</td>
                    <td style={td}>{r.review.length ? r.review.map(id => <span key={id} style={{...coralPill,display:"inline-block",fontSize:12,borderRadius:999,padding:"2px 8px",margin:"0 4px 4px 0"}}>{dhRoomName(id)}</span>) : <span style={{color:"#a3a5c2"}}>—</span>}</td>
                  </tr>))}</tbody>
              </table>
            </div>
          )}
          {due.length > 0 && <p className="text-xs mt-3" style={{color:"#26296b"}} data-testid="checks-due"><b style={{color:"#c0431f"}}>Review due:</b> {due.map(dhRoomName).join(", ")}</p>}
        </DashBlock>
      </div>
    </section>
  );
}

""".replace('__DATA__', data)
rep("function StudentLinkPanel({ student, logs }) {", CODE + "function StudentLinkPanel({ student, logs }) {")
rep("""      {row && <DrillProgress studentId={student.id}/>}""", """      {row && <DrillProgress studentId={student.id}/>}
      {row && <DrillStartChecks studentId={student.id}/>}""")
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
