p='teacher-dashboard.html'; s=open(p).read()
def rep(o,n,c=1):
    global s
    assert s.count(o)==c,(s.count(o),o[:80]); s=s.replace(o,n)
# parse / write: a finished mark (her 2 Nov: start and finish buttons)
rep('''const parsePiece = (line) => { const x = String(line || "").trim(); let m = /^\\[s([1-6])(?:\\s*♩\\s*(\\d{2,3}))?\\]\\s*(.+)$/u.exec(x); if (m) return { s: Math.min(5, +m[1]), b: m[2] || "", t: m[3] }; m = /^([🔴🟡🟢])\\s*(.+)$/u.exec(x); if (m) return { s: PIECE_STAGE_OLD[m[1]], b: "", t: m[2] }; return { s: 0, b: "", t: x }; };''',
'''const parsePiece = (line) => { const x = String(line || "").trim(); let m = /^\\[s([1-6])(?:\\s*♩\\s*(\\d{2,3}))?(\\s*✓)?\\]\\s*(.+)$/u.exec(x); if (m) return { s: Math.min(5, +m[1]), b: m[2] || "", f: !!m[3], t: m[4] }; m = /^([🔴🟡🟢])\\s*(.+)$/u.exec(x); if (m) return { s: PIECE_STAGE_OLD[m[1]], b: "", f: false, t: m[2] }; return { s: 0, b: "", f: false, t: x }; };
const STAGE_SHORT = ["Right hand", "Left hand", "Together", "Speed", "Fluent"];
// m47b (her 2 Nov: 'buttons for the stages, as simple as possible', 'start and finish'): one row of stage buttons under each piece, and Finish
function StageBar({ it, onPatch }) {
  const n = +it.r || 0, done = !!it.f;
  return (
    <div data-stagebar style={{ display: "flex", alignItems: "center", gap: 4, flexWrap: "wrap", marginTop: 5 }}>
      {STAGE_SHORT.map((nm, j) => { const on = j + 1 <= n, cur = j + 1 === n;
        return <button key={j} type="button" data-stage-pick={j + 1} aria-pressed={cur} onClick={() => onPatch({ r: cur ? (j ? String(j) : "") : String(j + 1) })}
          style={{ fontSize: 11, fontWeight: 800, padding: "4px 9px", borderRadius: 99, cursor: "pointer", border: "1.5px solid " + (on ? "#2e8a6e" : "#e1dccd"), background: cur ? "#2e8a6e" : on ? "#e8f3ee" : "white", color: cur ? "white" : on ? "#2e8a6e" : "#9a9cc0" }}>{nm}</button>; })}
      {n >= 4 && <input aria-label="Metronome speed" value={it.b || ""} onChange={e => onPatch({ b: e.target.value.replace(/\\D/g, "").slice(0, 3) })} placeholder="♩=" inputMode="numeric" style={{ width: 46, border: "1px solid #e9e2d2", borderRadius: 8, padding: "4px", fontSize: 12, textAlign: "center", color: "#26296b" }}/>}
      <button type="button" data-finish aria-pressed={done} onClick={() => onPatch({ f: !done, r: !done && n < 5 ? "5" : it.r })}
        style={{ marginLeft: "auto", fontSize: 11, fontWeight: 800, padding: "4px 10px", borderRadius: 99, cursor: "pointer", border: "1.5px solid #e4572e", background: done ? "#e4572e" : "white", color: done ? "white" : "#e4572e" }}>{done ? "✓ Finished" : "Finish"}</button>
    </div>
  );
}''')
# the chip from m47 goes; the bar sits under the piece's name
rep('''          {rating && (() => { const n = +it.r || 0, [bd, bg2, fg] = stageCol(n);''', '''          {false && (() => { const n = +it.r || 0, [bd, bg2, fg] = stageCol(n);''')
rep('''              innerRef={el => { refs.current[i] = el; }} bg={bg} accent={color}/>''', '''              innerRef={el => { refs.current[i] = el; }} bg={bg} accent={color}/>
            {rating && <StageBar it={it} onPatch={p => patch(i, p)}/>}''')
rep('''    if (rating) { const pp = parsePiece(l); return { t: pp.t, r: pp.s ? String(pp.s) : "", b: pp.b }; }   // m47''',
    '''    if (rating) { const pp = parsePiece(l); return { t: pp.t, r: pp.s ? String(pp.s) : "", b: pp.b, f: pp.f }; }   // m47''')
rep('''r: it.r, b: it.b, k: it.k })).filter(it => it.t).map(it => (rating && +it.r ? "[s" + (+it.r) + (it.b ? " ♩" + it.b : "") + "] " : "")''',
    '''r: it.r, b: it.b, f: it.f, k: it.k })).filter(it => it.t).map(it => (rating && (+it.r || it.f) ? "[s" + (+it.r || 5) + (it.b ? " ♩" + it.b : "") + (it.f ? " ✓" : "") + "] " : "")''')
# a new log starts with last lesson's pieces that are not finished
rep('''const [lists, setLists] = useState(() => { const src = existingLog ?? blank; return { rep: parseItems(src.repertoire, true),''',
    '''const [lists, setLists] = useState(() => { const src = existingLog ?? blank; const carry = existingLog ? src.repertoire : String((lastLog && lastLog.repertoire) || "").split("\\n").filter(x => x.trim() && !parsePiece(x).f).join("\\n");   /* m47b: last lesson's pieces carry on until finished */
    return { rep: parseItems(carry, true),''')
rep('rating addLabel="Add piece"', 'rating addLabel="Start a new piece"')
rep("Tap the stage to move a piece on: right hand, left hand, hands together, up to speed, fluent (‹ goes back). The speed box is optional. The student sees the stage too.",
    "Last lesson's pieces are already here. Tap the stage each piece is at; Finish when it is done (it moves to the pieces learned and stops coming back). The speed box is optional.")
# statement: learned = finished; growing leaves finished pieces out
rep("if (pp.s) pieces.get(pp.t).push({ s: pp.s, b: pp.b, d: l.date }); }));", "if (pp.s && !pp.f) pieces.get(pp.t).push({ s: pp.s, b: pp.b, d: l.date }); }));")
rep(".filter(([, , top]) => top.s < 5).slice(-6);", ".filter(([name]) => !finishedSet.has(name)).slice(-6);")
rep("const learned = new Map(); sorted.forEach(l => String(l.repertoire || \"\").split(\"\\n\").forEach(line => { const pp = parsePiece(line); if (pp.t && pp.s >= 5) learned.set(pp.t, pp.s); }));",
    "const learned = new Map(); sorted.forEach(l => String(l.repertoire || \"\").split(\"\\n\").forEach(line => { const pp = parsePiece(line); if (pp.t && pp.f) learned.set(pp.t, pp.s); }));")
rep("  const pieces = new Map();   // m47: name -> [{ s, b, d }] in this period", "  const finishedSet = new Set(); sorted.forEach(l => String(l.repertoire || \"\").split(\"\\n\").forEach(line => { const pp = parsePiece(line); if (pp.t && pp.f) finishedSet.add(pp.t); }));\n  const pieces = new Map();   // m47: name -> [{ s, b, d }] in this period")
open(p,'w').write(s)
p='drills.src.html'; s=open(p).read()
rep("const m = /^\\[s([1-6])(?:\\s*♩\\s*(\\d{2,3}))?\\]\\s*(.+)$/u.exec(v);\n    return m ? { t: m[3].slice(0, 120), s: Math.min(5, +m[1]), b: m[2] || '' } : { t: v.slice(0, 120), s: 0, b: '' }; })",
    "const m = /^\\[s([1-6])(?:\\s*♩\\s*(\\d{2,3}))?(\\s*✓)?\\]\\s*(.+)$/u.exec(v);\n    return m ? { t: m[4].slice(0, 120), s: m[3] ? 5 : Math.min(5, +m[1]), b: m[2] || '', f: !!m[3] } : { t: v.slice(0, 120), s: 0, b: '' }; })")
rep("{t('Now: ', '지금: ') + t(PIECE_STAGES[p.s - 1][0], PIECE_STAGES[p.s - 1][1]).toLowerCase()",
    "{p.f ? t('Finished ✓ Well done!', '완성 ✓ 잘했어요!') : t('Now: ', '지금: ') + t(PIECE_STAGES[p.s - 1][0], PIECE_STAGES[p.s - 1][1]).toLowerCase()")
rep("(p.s < 5 ? t(' · next: ', ' · 다음: ') + t(PIECE_STAGES[p.s][0], PIECE_STAGES[p.s][1]).toLowerCase() : ' ✓')}</span>}",
    "(p.f ? '' : p.s < 5 ? t(' · next: ', ' · 다음: ') + t(PIECE_STAGES[p.s][0], PIECE_STAGES[p.s][1]).toLowerCase() : ' ✓')}</span>}")
open(p,'w').write(s); print('ok')
