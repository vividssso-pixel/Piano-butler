import re
# ── dashboard ──
p='teacher-dashboard.html'; s=open(p).read()
assert 'PIECE_STAGES' not in s
def rep(old, new, cnt=1):
    global s
    assert s.count(old)==cnt, (s.count(old), old[:90])
    s=s.replace(old,new)
rep('const RATING_NEXT = { "": "🔴", "🔴": "🟡", "🟡": "🟢", "🟢": "" };',
'''// m47 (her 2 Nov): a piece moves through stages instead of red / yellow / green. Stored in the line as "[s3 ♩96] Minuet in G";
// an old line's 🔴 / 🟡 / 🟢 reads as stage 1 / 3 / 5. The drills read the same prefix (pieceItems).
const PIECE_STAGES = ["Right hand", "Left hand", "Hands together", "Up to speed", "Fluent", "Memorised"];
const PIECE_STAGE_OLD = { "🔴": 1, "🟡": 3, "🟢": 5 };
const parsePiece = (line) => { const x = String(line || "").trim(); let m = /^\\[s([1-6])(?:\\s*♩\\s*(\\d{2,3}))?\\]\\s*(.+)$/u.exec(x); if (m) return { s: +m[1], b: m[2] || "", t: m[3] }; m = /^([🔴🟡🟢])\\s*(.+)$/u.exec(x); if (m) return { s: PIECE_STAGE_OLD[m[1]], b: "", t: m[2] }; return { s: 0, b: "", t: x }; };
const stageCol = (n) => n >= 5 ? ["#2e8a6e", "#2e8a6e", "white"] : n >= 3 ? ["#f2b3a3", "#fdece7", "#b9421f"] : n >= 1 ? ["#26296b", "white", "#26296b"] : ["#d9d3c4", "white", "#9a9cc0"];
const RATING_NEXT = { "": "🔴", "🔴": "🟡", "🟡": "🟢", "🟢": "" };''')
rep('''          {rating && (
            <button type="button" onClick={() => patch(i, { r: RATING_NEXT[it.r || ""] })}''',
'''          {rating && (() => { const n = +it.r || 0, [bd, bg2, fg] = stageCol(n);   /* m47: the stage chip; ‹ goes back one */
            return <div style={{ display: "flex", alignItems: "center", gap: 4, marginTop: 5, flex: "0 0 auto" }}>
              {n > 0 && <button type="button" aria-label="One stage back" onClick={() => patch(i, { r: n > 1 ? String(n - 1) : "" })} style={{ border: "none", background: "none", color: "#9a9cc0", fontSize: 15, cursor: "pointer", padding: "0 2px" }}>‹</button>}
              <button type="button" data-stage={n} onClick={() => patch(i, { r: n >= 6 ? "" : String(n + 1) })} title="Tap to move the piece on a stage"
                style={{ fontSize: 11.5, fontWeight: 800, padding: "5px 10px", borderRadius: 99, cursor: "pointer", whiteSpace: "nowrap", border: "1.5px solid " + bd, background: bg2, color: fg }}>{n ? PIECE_STAGES[n - 1] : "Stage"} ›</button>
              {n >= 3 && <input aria-label="Metronome speed" value={it.b || ""} onChange={e => patch(i, { b: e.target.value.replace(/\\D/g, "").slice(0, 3) })} placeholder="♩=" inputMode="numeric"
                style={{ width: 46, border: "1px solid #e9e2d2", borderRadius: 8, padding: "5px 4px", fontSize: 12, textAlign: "center", color: "#26296b" }}/>}
            </div>; })()}
          {false && (
            <button type="button" onClick={() => patch(i, { r: RATING_NEXT[it.r || ""] })}''')
rep('''    const m = rating ? /^([🔴🟡🟢])\\s*(.*)$/u.exec(l) : null;
    if (m) return { t: m[2], r: m[1] };''',
'''    if (rating) { const pp = parsePiece(l); return { t: pp.t, r: pp.s ? String(pp.s) : "", b: pp.b }; }   // m47''')
rep('''const joinItems = (items, rating) => items.map(it => ({ t: it.t.trim() || (it.k ? linkLabel(it.k) : ""), r: it.r, k: it.k })).filter(it => it.t).map(it => (rating && it.r ? it.r + " " : "") + it.t''',
'''const joinItems = (items, rating) => items.map(it => ({ t: it.t.trim() || (it.k ? linkLabel(it.k) : ""), r: it.r, b: it.b, k: it.k })).filter(it => it.t).map(it => (rating && +it.r ? "[s" + (+it.r) + (it.b ? " ♩" + it.b : "") + "] " : "") + it.t''')
rep("The red / yellow / green circle is for you only: tap it to rate, red needs work, yellow progressing, green solid.",
    "Tap the stage to move a piece on: right hand, left hand, hands together, up to speed, fluent, memorised (‹ goes back). The speed box is optional. The student sees the stage too.")
# the statement: stages, not colours; a learned list across all lessons
rep('''  const pieces = new Map();
  L.forEach(l => String(l.repertoire || "").split("\\n").forEach(line => { const m = /^([🔴🟡🟢])\\s*(.+)$/u.exec(line.trim()); const name = (m ? m[2] : line.trim()); if (!name) return; if (!pieces.has(name)) pieces.set(name, []); if (m) pieces.get(name).push(ST_RATE[m[1]]); }));
  const pc = [...pieces.entries()].filter(([, r]) => r.length).slice(-6);''',
'''  const pieces = new Map();   // m47: name -> [{ s, b, d }] in this period
  L.forEach(l => String(l.repertoire || "").split("\\n").forEach(line => { const pp = parsePiece(line); if (!pp.t) return; if (!pieces.has(pp.t)) pieces.set(pp.t, []); if (pp.s) pieces.get(pp.t).push({ s: pp.s, b: pp.b, d: l.date }); }));
  const pc = [...pieces.entries()].filter(([, r]) => r.length).map(([name, r]) => { const top = r.reduce((a, x) => x.s >= a.s ? x : a, r[0]); return [name, r, top]; }).filter(([, , top]) => top.s < 5).slice(-6);
  const learned = new Map(); sorted.forEach(l => String(l.repertoire || "").split("\\n").forEach(line => { const pp = parsePiece(line); if (pp.t && pp.s >= 5) learned.set(pp.t, pp.s); }));''')
rep('''const nowPiece = (() => { for (let i = L.length - 1; i >= 0; i--) { const x = String(L[i].repertoire || "").split("\\n").map(z => z.replace(/^[🔴🟡🟢]\\s*/u, "").trim()).filter(Boolean); if (x.length) return x[0]; } return ""; })();''',
'''const nowPiece = (() => { for (let i = L.length - 1; i >= 0; i--) { const x = String(L[i].repertoire || "").split("\\n").map(z => parsePiece(z).t).filter(Boolean); if (x.length) return x[0]; } return ""; })();''')
rep('''.map(x => { const m = /^([🔴🟡🟢])\\s*(.+)$/u.exec(x); return (m ? dot(ST_RATE[m[1]]) : "") + stEsc(m ? m[2] : x); }).join(" · ");''',
'''.map(x => { const pp = parsePiece(x); return stEsc(pp.t) + (pp.s ? ' <span style="color:#7a7ca6">(' + PIECE_STAGES[pp.s - 1].toLowerCase() + (pp.b ? " ♩=" + pp.b : "") + ')</span>' : ""); }).join(" · ");''')
# the pieces block on page 1: a six-step ladder per piece, then the pieces learned
a = s.index("    + (pc.length ? '<div class=\"lab\">' + stEsc(first) + '’s pieces, growing</div>'")
b = s.index("    + '<div class=\"lab\">When ' + stEsc(first) + ' played</div>", a)
s = s[:a] + '''    + (pc.length ? '<div class="lab">' + stEsc(first) + '’s pieces, growing</div>' + pc.map(([name, r, top]) => { const f0 = r[0];
        return '<div class="pc2"><b>' + stEsc(name) + '</b><small>' + (f0.s !== top.s ? PIECE_STAGES[f0.s - 1] + ' (' + fmt(f0.d, { day: "numeric", month: "short" }) + ') → ' : 'Now: ') + PIECE_STAGES[top.s - 1] + (top.b ? ' at ♩=' + top.b : '') + (f0.s !== top.s ? ' (' + fmt(top.d, { day: "numeric", month: "short" }) + ')' : '') + '</small><div class="lad">'
          + PIECE_STAGES.map((nm, i) => '<span class="' + (i + 1 < top.s ? 'on' : i + 1 === top.s ? 'now' : '') + '"></span>').join('<em></em>') + '</div><div class="ll">' + PIECE_STAGES.map(nm => '<span>' + nm + '</span>').join("") + '</div></div>'; }).join("") : "")
    + (learned.size ? '<div class="lab">Pieces ' + stEsc(first) + ' has learned</div><div class="lrn">' + [...learned.entries()].map(([n, st6]) => '<span>✓ ' + stEsc(n) + (st6 === 6 ? ' · by heart' : '') + '</span>').join("") + '</div>' : "")
''' + s[b:]
rep("+ '.r{background:#fff;border:2px solid #26296b}",
    "+ '.pc2{padding:8px 0;border-bottom:1px solid #eee8da}.pc2 b{font-size:14px}.pc2 small{display:block;font-size:12px;color:#7a7ca6;margin:2px 0 6px}.lad{display:flex;align-items:center}.lad span{flex:none;width:13px;height:13px;border-radius:50%;background:#e6dfcd}.lad span.on{background:#2e8a6e}.lad span.now{background:#f2b3a3;box-shadow:0 0 0 3px #fdece7}.lad em{flex:1;height:2px;background:#e1dccd}.ll{display:flex;justify-content:space-between;font-size:9px;color:#9a9cc0;margin-top:3px}.lrn{display:flex;flex-wrap:wrap;gap:6px}.lrn span{background:#e8f3ee;color:#2e8a6e;border-radius:99px;padding:4px 10px;font-size:12.5px;font-weight:700}'\n    + '.r{background:#fff;border:2px solid #26296b}")
open(p,'w').write(s); print('dashboard ok')

# ── drills: the student's pieces show their stage ──
p='drills.src.html'; s=open(p).read()
assert 'PIECE_STAGES' not in s
rep('''function pieceItems(arr) {
  if (!Array.isArray(arr)) return [];
  return arr.map(x => (typeof x === 'string' ? x : '').replace(/^(?:\\s|🔴|🟡|🟢)+/, '').replace(/^(?:[-*•·]|\\d+[.)])\\s+/, '').trim().slice(0, 120)).filter(Boolean).slice(0, 12);
}''',
'''// m47: the dashboard writes a piece's stage as "[s3 ♩96] Minuet in G" (right hand, left hand, hands together, up to speed, fluent, memorised)
const PIECE_STAGES = [['Right hand', '오른손'], ['Left hand', '왼손'], ['Hands together', '양손'], ['Up to speed', '목표 속도'], ['Fluent', '유창하게'], ['Memorised', '암보']];
function pieceItems(arr) {
  if (!Array.isArray(arr)) return [];
  return arr.map(x => { const v = (typeof x === 'string' ? x : '').replace(/^(?:\\s|🔴|🟡|🟢)+/, '').replace(/^(?:[-*•·]|\\d+[.)])\\s+/, '').trim(); const m = /^\\[s([1-6])(?:\\s*♩\\s*(\\d{2,3}))?\\]\\s*(.+)$/u.exec(v);
    return m ? { t: m[3].slice(0, 120), s: +m[1], b: m[2] || '' } : { t: v.slice(0, 120), s: 0, b: '' }; }).filter(p => p.t).slice(0, 12);
}''')
rep('''              <span style={{ fontSize: 15.5, lineHeight: 1.35, color: 'var(--navy)', fontWeight: 600, minWidth: 0, overflowWrap: 'anywhere' }}>{p}</span>''',
'''              <span style={{ fontSize: 15.5, lineHeight: 1.35, color: 'var(--navy)', fontWeight: 600, minWidth: 0, overflowWrap: 'anywhere', flex: 1 }}>{p.t}
                {p.s > 0 && <span data-testid="piece-stage" style={{ display: 'block', fontSize: 12.5, fontWeight: 500, color: 'var(--muted)', marginTop: 2 }}>{t('Now: ', '지금: ') + t(PIECE_STAGES[p.s - 1][0], PIECE_STAGES[p.s - 1][1]).toLowerCase() + (p.b ? ' · ♩=' + p.b : '') + (p.s < 6 ? t(' · next: ', ' · 다음: ') + t(PIECE_STAGES[p.s][0], PIECE_STAGES[p.s][1]).toLowerCase() : ' ✓')}</span>}
                {p.s > 0 && <span aria-hidden="true" style={{ display: 'flex', alignItems: 'center', marginTop: 6 }}>{PIECE_STAGES.map((x, j) => <React.Fragment key={j}>{j > 0 && <i style={{ flex: 1, height: 2, background: 'var(--navy-line)' }}/>}<i style={{ flex: 'none', width: 12, height: 12, borderRadius: '50%', background: j + 1 < p.s ? '#2e8a6e' : j + 1 === p.s ? '#f2b3a3' : '#e6dfcd', boxShadow: j + 1 === p.s ? '0 0 0 3px #fdece7' : 'none' }}/></React.Fragment>)}</span>}
              </span>''')
open(p,'w').write(s); print('drills ok')
