p='teacher-dashboard.html'; s=open(p).read()
assert 'ScalesField' not in s
def rep(o,n,c=1):
    global s
    assert s.count(o)==c,(s.count(o),o[:80]); s=s.replace(o,n)
rep("function KeysField({ keys, onChange }) {", r'''// m49 (her 2 Nov): scales like the pieces. Add a scale (major and its relative minor side by side), then tap its stage.
// Stored in lesson_logs.technical as "[s3 ♩80] G major"; the twelve-key maps take their keys from the scales added.
const SC_MIN = ["A", "E", "B", "F♯", "C♯", "G♯", "E♭", "B♭", "F", "C", "G", "D"];
const scMaj = (k) => (KEY_LABEL[k] || k);
const scOrder = (t) => { const m = /^(.+?) (major|minor)$/.exec(t); if (!m) return 99; const i = m[2] === "major" ? KEYS_FIFTHS.map(scMaj).indexOf(m[1]) : SC_MIN.indexOf(m[1]); return i < 0 ? 99 : i * 2 + (m[2] === "minor" ? 1 : 0); };
const scKeys = (items) => KEYS_FIFTHS.filter((k, i) => items.some(it => it.t === scMaj(k) + " major" || it.t === SC_MIN[i] + " minor"));
function ScalesField({ items, onChange }) {
  const [pick, setPick] = useState(false);
  const rows = items.filter(it => it.t && it.t.trim());
  const has = (t) => rows.some(it => it.t === t);
  const toggle = (t) => { const next = has(t) ? rows.filter(it => it.t !== t) : [...rows, { t, r: "", b: "" }]; next.sort((a, b) => scOrder(a.t) - scOrder(b.t)); onChange(next.length ? next : [{ t: "", r: "" }]); };
  const patch = (i, pt) => onChange(rows.map((it, j) => j === i ? { ...it, ...pt } : it));
  const half = (t, label, top) => { const on = has(t); return <button type="button" data-scale={t} aria-pressed={on} onClick={() => toggle(t)}
    style={{ display: "block", width: "100%", border: "none", borderTop: top ? "none" : "1px solid #e9e2d2", padding: "7px 2px", background: on ? "#26296b" : "white", color: on ? "white" : top ? "#26296b" : "#62649a", fontWeight: top ? 800 : 700, fontSize: top ? 13 : 12, cursor: "pointer" }}>{label}</button>; };
  return (
    <div data-testid="scales-field">
      <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between", gap: 8, marginBottom: 4 }}>
        <span className="field-label" style={{ color: "#26296b", marginBottom: 0 }}>Scales</span>
        <button type="button" onClick={() => setPick(x => !x)} aria-expanded={pick} style={{ fontSize: 10, fontWeight: 700, padding: "3px 10px", borderRadius: 99, cursor: "pointer", border: "1px solid " + (pick ? "#26296b" : "#e9e2d2"), background: pick ? "#ecebf5" : "white", color: pick ? "#26296b" : "#62649a" }}>{pick ? "Done" : "+ Add a scale"}</button>
      </div>
      <p className="text-xs text-slate-400 mb-2">Each major sits over its relative minor. Tap to add or remove, then tap the stage like a piece. These keys also go on the student's twelve-key maps.</p>
      {pick && <div data-testid="scale-pick" style={{ display: "grid", gridTemplateColumns: "repeat(6, minmax(0, 1fr))", gap: 6, marginBottom: 10 }}>
        {KEYS_FIFTHS.map((k, i) => <div key={k} style={{ border: "1.5px solid #d9d3c4", borderRadius: 12, overflow: "hidden" }}>{half(scMaj(k) + " major", scMaj(k), true)}{half(SC_MIN[i] + " minor", SC_MIN[i] + "m", false)}</div>)}
      </div>}
      {rows.map((it, i) => (
        <div key={it.t} data-scale-row={it.t} style={{ display: "flex", alignItems: "flex-start", gap: 8, marginBottom: 8 }}>
          <div style={{ flex: 1, minWidth: 0 }}>
            <div style={{ fontSize: 14, fontWeight: 700, color: "#26296b", background: "#ecebf5", borderRadius: 10, padding: "8px 12px" }}>{it.t}</div>
            <StageBar it={it} onPatch={pt => patch(i, pt)}/>
          </div>
          <button type="button" onClick={() => toggle(it.t)} aria-label={"Remove " + it.t} style={{ flex: "0 0 22px", marginTop: 8, border: "none", background: "transparent", color: "#9b9cbd", fontSize: 18, cursor: "pointer", padding: 0 }}>×</button>
        </div>
      ))}
    </div>
  );
}
function KeysField({ keys, onChange }) {''')
rep('''    return { rep: parseItems(carry, true), tech: parseItems(src.technical),''',
    '''    const carrySc = existingLog ? src.technical : String((lastLog && lastLog.technical) || "").split("\\n").filter(x => x.trim() && !parsePiece(x).f).join("\\n");   /* m49: scales carry on too */
    return { rep: parseItems(carry, true), sc: parseItems(carrySc, true).filter(it => it.t), tech: parseItems(src.technical),''')
rep('''  const keysLine = (hw) => { const now = keysNow || [], changed = keys.join() !== now.join();
    if (keys.length) return (hw || changed || own != null) ? "[keys:" + keys.join(",") + "]" : "";''',
    '''  const keysLine = (hw, kk) => { const now = keysNow || [], changed = kk.join() !== now.join();   /* m49: kk, the keys of the scales added */
    if (kk.length) return (hw || changed || own != null) ? "[keys:" + kk.join(",") + "]" : "";''')
rep('''technical: joinItems(lists.tech), srAural: joinItems(lists.sr), gk: joinItems(lists.gk), homework: [keysLine(hw), hw].filter(Boolean).join("\\n") }); };''',
    '''technical: joinItems(lists.sc, true), srAural: joinItems(lists.sr), gk: joinItems(lists.gk), homework: [keysLine(hw, lists.sc.some(it => it.t) ? scKeys(lists.sc) : keys), hw].filter(Boolean).join("\\n") }); };''')
i=s.index('          {legacy.tech && <ListField testid="list-tech"'); j=s.index('\n', i)
s=s[:i]+'          <ScalesField items={lists.sc} onChange={setList("sc")}/>   {/* m49: scales like the pieces (was the old Technical work list) */}'+s[j:]
rep('          <KeysField keys={keys} onChange={setKeys}/>\n', '')
open(p,'w').write(s); print('ok')
