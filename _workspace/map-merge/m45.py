import re
p='teacher-dashboard.html'; s=open(p).read()
if 'DRILL_LEVELS' in s: print('already'); raise SystemExit
lv=open('_workspace/map-merge/levels.js').read()
def rep(old, new, cnt=1):
    global s
    assert s.count(old)==cnt, (s.count(old), old[:90])
    s=s.replace(old,new)

# 1. every room of the drills, by level and in the house's order (generated from the drills' PATH_STAGES, 2 Nov 2026)
a = s.index("const DRILL_LINKS = {\n  chapters: [")
b = s.index("  tools: [", a)
s = s[:a] + ("// m45: [short, level name, [[id, room number, room name], ...]] in the house's order. Regenerate from the drills when rooms change.\n"
  "const DRILL_LEVELS = [\n" + lv + "\n];\n"
  "const DRILL_LINKS = {\n  chapters: DRILL_LEVELS.flatMap(([, , rows]) => rows.map(([id, no, label]) => ({ id, no, label }))),\n") + s[b:]

# 2. the picker: Chapters / Practice activities, a search, the level chips, one room per row
a = s.index("      {pick && links && (\n        <div data-testid=\"link-picker\"")
b = s.index("      {items.map((it, i) => (", a)
s = s[:a] + "      {pick && links && <LinkPicker links={links} items={items} max={max} onAdd={addLink} onClose={() => setPick(false)}/>}\n" + s[b:]
rep("// A numbered list of short items (rows are { t: text, r: rating }).",
r'''// m45 (her 2 Nov: 'easier to pick'): Chapters by level in the house's order, with a search; activities on their own tab.
const PICK_LV_KEY = "pb_dash_pick_lv";
function LinkPicker({ links, items, max, onAdd, onClose }) {
  const [tab, setTab] = useState("chapter");
  const [q, setQ] = useState("");
  const [lv, setLv] = useState(() => { try { return localStorage.getItem(PICK_LV_KEY) || "0"; } catch (e) { return "0"; } });
  const pickLv = (x) => { setLv(x); try { localStorage.setItem(PICK_LV_KEY, x); } catch (e) {} };
  const full = items.length >= max && !(items.length === 1 && !items[0].t.trim() && !items[0].k);
  const has = (k) => items.some(it => it.k === k);
  const qq = q.trim().toLowerCase();
  const row = (kind, id, label, no) => { const k = kind + ":" + id, on = has(k);
    return <div key={k} className="flex items-center gap-2" style={{ padding: "7px 4px", borderTop: "1px solid #f0ebdf", fontSize: 13 }}>
      {no != null && <span style={{ width: 24, flex: "0 0 24px", color: "#9a9cc0", fontSize: 11.5, fontWeight: 700 }}>{no}</span>}
      <span style={{ flex: 1, minWidth: 0, color: "#26296b" }}>{label}</span>
      <button type="button" data-pick={k} disabled={on || full} onClick={() => onAdd(kind, id, label)}
        style={{ flex: "0 0 auto", fontSize: 11.5, fontWeight: 800, padding: "3px 10px", borderRadius: 99, cursor: on || full ? "default" : "pointer", border: "1px solid " + (on ? "#2e8a6e" : "#e4572e"), background: on ? "#2e8a6e" : "white", color: on ? "white" : "#e4572e", opacity: full && !on ? 0.4 : 1 }}>{on ? "✓ Added" : "+ Add"}</button>
    </div>; };
  const L = DRILL_LEVELS.find(x => x[0] === lv) || DRILL_LEVELS[0];
  const found = qq ? DRILL_LEVELS.flatMap(([, name, rows]) => rows.filter(r => (r[2] + " " + r[0] + " " + name).toLowerCase().includes(qq)).map(r => [...r, name])) : null;
  const tabBtn = (k, t) => <button type="button" onClick={() => setTab(k)} style={{ flex: 1, padding: "6px", borderRadius: 10, border: "none", fontWeight: 800, fontSize: 12.5, cursor: "pointer", background: tab === k ? "#26296b" : "#f4f1ea", color: tab === k ? "white" : "#62649a" }}>{t}</button>;
  return (
    <div data-testid="link-picker" className="mb-2 p-3 rounded-xl" style={{ border: "1px solid #e9e2d2", background: "#fffefa" }}>
      <div className="flex gap-2 mb-2">{tabBtn("chapter", "Chapters")}{tabBtn("tool", "Practice activities")}
        <button type="button" onClick={onClose} aria-label="Close" style={{ border: "none", background: "none", color: "#7a7ca6", fontSize: 14, cursor: "pointer", padding: "0 4px" }}>✕</button></div>
      {tab === "chapter" ? <>
        <input data-testid="pick-search" value={q} onChange={e => setQ(e.target.value)} placeholder="Search a chapter (e.g. scales, cadence, 6/8)" className="input text-sm" style={{ marginBottom: 8 }}/>
        {!found && <>
          <div className="flex gap-1 flex-wrap mb-1">{DRILL_LEVELS.map(([k]) => <button key={k} type="button" data-pick-lv={k} onClick={() => pickLv(k)}
            style={{ minWidth: 32, fontSize: 12, fontWeight: 700, padding: "4px 9px", borderRadius: 99, cursor: "pointer", border: "1px solid " + (k === L[0] ? "#2e8a6e" : "#e9e2d2"), background: k === L[0] ? "#2e8a6e" : "white", color: k === L[0] ? "white" : "#62649a" }}>{k}</button>)}</div>
          <p style={{ fontSize: 11, color: "#7a7ca6", margin: "4px 0 2px" }}>{L[1]} · {L[2].length} rooms</p>
        </>}
        <div style={{ maxHeight: 300, overflowY: "auto" }}>
          {found ? (found.length ? found.map(([id, no, label, name]) => row("chapter", id, label + " · " + name, no)) : <p style={{ fontSize: 12, color: "#9a9cc0", padding: "6px 4px" }}>No chapter matches.</p>)
            : L[2].map(([id, no, label]) => row("chapter", id, label, no))}
        </div>
      </> : <div style={{ maxHeight: 300, overflowY: "auto" }}>{links.tools.map(c => row("tool", c.id, c.label, null))}</div>}
    </div>
  );
}
// A numbered list of short items (rows are { t: text, r: rating }).''')
# keep the picker open after adding, so several rooms can be picked in a row
rep("onChange([...base, { t: text, r: \"\", k: kind + \":\" + id }]); setPick(false); setFocus({ i: base.length, k: Date.now() });",
    "onChange([...base, { t: text, r: \"\", k: kind + \":\" + id }]);   // m45: the picker stays open for the next one")
open(p,'w').write(s); print('ok')
