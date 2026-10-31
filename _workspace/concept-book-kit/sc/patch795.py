"""Build DS, her 09:37 and 09:42 (on t794 -> t795): the crackle. Every composer tune was rendered offline as playEvents plays it:
thick chords in the loud ones went past full scale (Stravinsky style 2.06, Liszt style 1.61, Beethoven 5 1.33, Bartok 1.23,
Rachmaninoff 1.14), and the speaker clips them: heard as a crackle on each loud chord, in Safari and Chrome alike. Every sound
now goes to the speakers through one limiter per audio context (pbOut), so nothing passes full scale; a quiet note keeps its level."""
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def R(old, new, n=1):
    global s
    c = s.count(old); assert c == n, (c, n, old[:120]); s = s.replace(old, new)

# the limiter: one per context (the live one and any offline render); a gentle knee from about half scale, then a gain back
# down so a quiet note comes out as loud as before (the compressor adds its own make-up gain)
R("""let _noiseBuf = null;
function noiseBuf(ctx) {""", """// Build DS (her 09:37): one way out to the speakers for every sound, through a limiter, so a thick loud chord never goes
// past full scale (that clipping was the crackle)
const _pbOuts = new WeakMap();
function pbOut(ctx) {
  let o = _pbOuts.get(ctx); if (o) return o;
  try {
    const lim = ctx.createDynamicsCompressor(), g = ctx.createGain();
    lim.threshold.value = PB_LIM.th; lim.knee.value = PB_LIM.knee; lim.ratio.value = 20; lim.attack.value = 0.002; lim.release.value = 0.2;
    g.gain.value = PB_LIM.back; lim.connect(g); g.connect(ctx.destination); o = lim;
  } catch (e) { o = ctx.destination; }
  _pbOuts.set(ctx, o); return o;
}
const PB_LIM = { th: -9, knee: 6, back: 0.86 };
let _noiseBuf = null;
function noiseBuf(ctx) {""")
R('.connect(ctx.destination)', '.connect(pbOut(ctx))', 14)   # 13 sounds and, just written above, the limiter's own way out
R('g.connect(pbOut(ctx)); o = lim;', 'g.connect(ctx.destination); o = lim;')
assert s.count('ctx.destination') == 2, s.count('ctx.destination')   # only the limiter's own way out, and its fallback

# (2) her 09:38: the stems hang off their heads. Build DK made the filled head fit its space (5.8 x 4.1, tilted 20 degrees: its
# outer edge is 5.63 from its centre) but the stems stayed where the old head's edge was (6.4, and 5.3 in nvbNote), starting
# 1.5 below or above the centre, so the stem's centre line missed the head and it hung from one corner. A stem's outer edge now
# meets the head's outer edge (centre at 5.63 - 0.95 = 4.68) and the stem starts at the head's centre, inside the head.
R("""function nvbHead(x, y, kind, col, k) {""", """const NV_SX = 4.68;   // Build DS: a 1.9 stem's centre, from the head's centre, so its outer edge meets the head's (5.63 for the filled head, 5.6 for the minim's outline)
function nvbHead(x, y, kind, col, k) {""")
R("""const k = o.k || 1, col = o.col || PEN_N, sx = x + 5.3 * k, top = y - 34 * k;   // Build DK: the stem at the smaller head's edge""",
  """const k = o.k || 1, col = o.col || PEN_N, sx = x + NV_SX * k, top = y - 34 * k;   // Build DS: the stem's outer edge on the head's edge""")
R("""  if (kind !== 'w') s += '<line x1="' + nvbF(sx) + '" y1="' + nvbF(y - 1.5 * k) + '" x2="' + nvbF(sx) + '" y2="' + nvbF(top) + '" stroke="' + col + '" stroke-width="' + nvbF(1.9 * k) + '" stroke-linecap="round"/>';""",
  """  if (kind !== 'w') s += '<line x1="' + nvbF(sx) + '" y1="' + nvbF(y) + '" x2="' + nvbF(sx) + '" y2="' + nvbF(top) + '" stroke="' + col + '" stroke-width="' + nvbF(1.9 * k) + '" stroke-linecap="round"/>';""")
R("""  [x1, x2].forEach(x => { s += '<line x1="' + nvbF(x + 5.3 * k) + '" y1="' + nvbF(y - 1.5 * k) + '" x2="' + nvbF(x + 5.3 * k) + '" y2="' + nvbF(top) + '" stroke="' + col + '" stroke-width="' + nvbF(1.9 * k) + '"/>'; });
  s += '<path d="M' + nvbF(x1 + 4.4 * k) + ' ' + nvbF(top - 0.2 * k) + ' L' + nvbF(x2 + 6.2 * k) + ' ' + nvbF(top - 0.2 * k) + ' L' + nvbF(x2 + 6.2 * k) + ' ' + nvbF(top + 5.2 * k) + ' L' + nvbF(x1 + 4.4 * k) + ' ' + nvbF(top + 5.2 * k) + ' Z" fill="' + col + '"/>';""",
  """  [x1, x2].forEach(x => { s += '<line x1="' + nvbF(x + NV_SX * k) + '" y1="' + nvbF(y) + '" x2="' + nvbF(x + NV_SX * k) + '" y2="' + nvbF(top) + '" stroke="' + col + '" stroke-width="' + nvbF(1.9 * k) + '"/>'; });
  s += '<path d="M' + nvbF(x1 + (NV_SX - 0.95) * k) + ' ' + nvbF(top - 0.2 * k) + ' L' + nvbF(x2 + (NV_SX + 0.95) * k) + ' ' + nvbF(top - 0.2 * k) + ' L' + nvbF(x2 + (NV_SX + 0.95) * k) + ' ' + nvbF(top + 5.2 * k) + ' L' + nvbF(x1 + (NV_SX - 0.95) * k) + ' ' + nvbF(top + 5.2 * k) + ' Z" fill="' + col + '"/>';""")
# sskRaw (the scales rooms, the Scale finder, the Workbooks' tunes): the single stem and the beamed pair
R("""  const stem = (nx, y, up, c) => '<line x1="' + pFix(up ? nx + 6.4 : nx - 6.4) + '" x2="' + pFix(up ? nx + 6.4 : nx - 6.4) + '" y1="' + pFix(up ? y - 1.5 : y + 1.5) + '" y2="' + pFix(up ? y - 34 : y + 34) + '" stroke="' + c + '" stroke-width="1.9" stroke-linecap="round"/>';""",
  """  const stem = (nx, y, up, c) => '<line x1="' + pFix(up ? nx + NV_SX : nx - NV_SX) + '" x2="' + pFix(up ? nx + NV_SX : nx - NV_SX) + '" y1="' + pFix(y) + '" y2="' + pFix(up ? y - 34 : y + 34) + '" stroke="' + c + '" stroke-width="1.9" stroke-linecap="round"/>';   // Build DS: flush with the head""")
R("""        out.push(ledgers(xx, d), nvbHead(xx, y, 'q', c, 1), '<line x1="' + pFix(up ? xx + 6.4 : xx - 6.4) + '" x2="' + pFix(up ? xx + 6.4 : xx - 6.4) + '" y1="' + pFix(up ? y - 1.5 : y + 1.5) + '" y2="' + pFix(by) + '" stroke="' + c + '" stroke-width="1.9"/>');""",
  """        out.push(ledgers(xx, d), nvbHead(xx, y, 'q', c, 1), '<line x1="' + pFix(up ? xx + NV_SX : xx - NV_SX) + '" x2="' + pFix(up ? xx + NV_SX : xx - NV_SX) + '" y1="' + pFix(y) + '" y2="' + pFix(by) + '" stroke="' + c + '" stroke-width="1.9"/>');""")
R("""      const xa = (up ? nx + 6.4 : nx - 6.4) - 0.9, xb = (up ? x2 + 6.4 : x2 - 6.4) + 0.9;""",
  """      const xa = (up ? nx + NV_SX : nx - NV_SX) - 0.95, xb = (up ? x2 + NV_SX : x2 - NV_SX) + 0.95;""")
# srhGroup (beamed quavers and semiquavers in the rhythm rooms' pictures)
R("""  xs.forEach((x, i) => { s += nvbHead(x, y, 'q', cols[i], 1) + '<line x1="' + pFix(x + 6.4) + '" y1="' + pFix(y - 1.5) + '" x2="' + pFix(x + 6.4) + '" y2="' + pFix(top) + '" stroke="' + cols[i] + '" stroke-width="1.9"/>'; });
  const x1 = xs[0] + 5.5, x2 = xs[xs.length - 1] + 7.3;""",
  """  xs.forEach((x, i) => { s += nvbHead(x, y, 'q', cols[i], 1) + '<line x1="' + pFix(x + NV_SX) + '" y1="' + pFix(y) + '" x2="' + pFix(x + NV_SX) + '" y2="' + pFix(top) + '" stroke="' + cols[i] + '" stroke-width="1.9"/>'; });
  const x1 = xs[0] + NV_SX - 0.95, x2 = xs[xs.length - 1] + NV_SX + 0.95;   // Build DS: the beam ends where the stems' edges are""")
# (3) the other staffs drawn by hand, each with its own head: the stem's outer edge on the head's outer edge, from the head's
# centre. For a head rx x ry tilted 20 degrees the outer edge is sqrt(rx^2 cos^2 20 + ry^2 sin^2 20) from the centre:
# 5.9 x 4.3 -> 5.74; 4.6 x 3.3 with a 2.2 outline -> 5.56; 4.7 x 3.4 -> 4.57; 4.6 x 3.4 at 22 degrees -> 4.45. Minus half the stem.
# K4Melody (Keys, Grades 4 and 5: 'A melody'): 1.6 stems
R("""        <line x1={up ? x + 6 : x - 6} x2={up ? x + 6 : x - 6} y1={y} y2={y + (up ? -30 : 30)} stroke={col} strokeWidth="1.6"/>""",
  """        <line x1={up ? x + 4.94 : x - 4.94} x2={up ? x + 4.94 : x - 4.94} y1={y} y2={y + (up ? -30 : 30)} stroke={col} strokeWidth="1.6"/>""")
# MwStaff (the melody-writing rooms): 1.7 stems, the filled head 5.9 x 4.3, the minim 4.6 x 3.3 in a 2.2 outline
R("""      if (s.k === 'q' || s.k === 'h' || s.k === 'hd') els.push(<line key={'s' + i} x1={up ? x + 6 : x - 6} x2={up ? x + 6 : x - 6} y1={y + (up ? -1 : 1)} y2={y + (up ? -32 : 32)} stroke={c} strokeWidth="1.7"/>);""",
  """      if (s.k === 'q' || s.k === 'h' || s.k === 'hd') { const sd = s.k === 'q' ? 4.89 : 4.71; els.push(<line key={'s' + i} x1={up ? x + sd : x - sd} x2={up ? x + sd : x - sd} y1={y} y2={y + (up ? -32 : 32)} stroke={c} strokeWidth="1.7"/>); }""")
R("""sx1 = up ? x + 6 : x - 6, sx2 = up ? x2 + 6 : x2 - 6;
        els.push(<line key={'s' + i} x1={sx1} x2={sx1} y1={y + (up ? -1 : 1)} y2={by} stroke={c} strokeWidth="1.7"/>, <line key={'s' + j} x1={sx2} x2={sx2} y1={y2 + (up ? -1 : 1)} y2={by} stroke={colOf(j)} strokeWidth="1.7"/>,""",
  """sx1 = up ? x + 4.89 : x - 4.89, sx2 = up ? x2 + 4.89 : x2 - 4.89;
        els.push(<line key={'s' + i} x1={sx1} x2={sx1} y1={y} y2={by} stroke={c} strokeWidth="1.7"/>, <line key={'s' + j} x1={sx2} x2={sx2} y1={y2} y2={by} stroke={colOf(j)} strokeWidth="1.7"/>,""")
# StmMiniPage (Tempo's Workbook): 4.7 x 3.4 heads, 1.3 stems
R("""<line x1={x + 5.4} x2={x + 5.4} y1={nY(noteD[i])} y2={nY(noteD[i]) - 28} stroke={ink} strokeWidth="1.3"/>""",
  """<line x1={x + 3.92} x2={x + 3.92} y1={nY(noteD[i])} y2={nY(noteD[i]) - 28} stroke={ink} strokeWidth="1.3"/>""")
# MlxMapSvg (the map of a tune): heads 0.59 x 0.43 of a space, 1.3 stems
R("""<line x1={x + sp * 0.56} x2={x + sp * 0.56} y1={y - 1} y2={y - 3.4 * sp} stroke={zc} strokeWidth="1.3"/>""",
  """<line x1={x + sp * 0.5736 - 0.65} x2={x + sp * 0.5736 - 0.65} y1={y} y2={y - 3.4 * sp} stroke={zc} strokeWidth="1.3"/>""")
# StmMark (Tempo's crotchet = 60): the head 4.6 x 3.4 at 22 degrees, centred at x0 + 4.6k, y - 3.2k; a 1.4k stem
R("""    <line x1={x0 + 8.8 * k} x2={x0 + 8.8 * k} y1={y - 4 * k} y2={y - 19 * k} stroke={c} strokeWidth={1.4 * k}/>""",
  """    <line x1={x0 + 8.35 * k} x2={x0 + 8.35 * k} y1={y - 3.2 * k} y2={y - 19 * k} stroke={c} strokeWidth={1.4 * k}/>""")
# the older note-reading pads (5.9 x 4.3 heads, 1.4 stems)
R("""<line x1={x + 6.5} x2={x + 6.5} y1={dY(d)} y2={dY(d) - 32} stroke={color} strokeWidth="1.4"/>""", """<line x1={x + 5.04} x2={x + 5.04} y1={dY(d)} y2={dY(d) - 32} stroke={color} strokeWidth="1.4"/>""")
R("""<line x1={x - 6.5} x2={x - 6.5} y1={dY(d)} y2={dY(d) + 32} stroke={color} strokeWidth="1.4"/>""", """<line x1={x - 5.04} x2={x - 5.04} y1={dY(d)} y2={dY(d) + 32} stroke={color} strokeWidth="1.4"/>""")
R("""x1={xs[i] - 6.5} x2={xs[i] - 6.5}""", """x1={xs[i] - 5.04} x2={xs[i] - 5.04}""", 2)
# (4) the small pictures beside the checks and the steps: the same rule at their own sizes
# the rhythm rooms' pictures: 5.5 x 4 heads (edge 5.35), 1.8 stems -> 4.45 from the centre, from the centre
R("""<line x1="' + (19 + i * 16) + '" x2="' + (19 + i * 16) + '" y1="33" y2="8" stroke="#26296b" stroke-width="1.8"/>""", """<line x1="' + (18.45 + i * 16) + '" x2="' + (18.45 + i * 16) + '" y1="34" y2="8" stroke="#26296b" stroke-width="1.8"/>""")
R("""<line x1="27" x2="27" y1="33" y2="8" stroke="#26296b" stroke-width="1.8"/><line x1="59" x2="59" y1="33" y2="8" stroke="#26296b" stroke-width="1.8"/>""", """<line x1="26.45" x2="26.45" y1="34" y2="8" stroke="#26296b" stroke-width="1.8"/><line x1="58.45" x2="58.45" y1="34" y2="8" stroke="#26296b" stroke-width="1.8"/>""")
R("""<line x1="' + (25 + i * 18) + '" x2="' + (25 + i * 18) + '" y1="33" y2="12" stroke="#26296b" stroke-width="1.8"/>""", """<line x1="' + (24.45 + i * 18) + '" x2="' + (24.45 + i * 18) + '" y1="34" y2="12" stroke="#26296b" stroke-width="1.8"/>""")
R("""<line x1="19" x2="19" y1="33" y2="10" stroke="#26296b" stroke-width="1.8"/><path d="M19 10 Q26 16 24 24" fill="none" stroke="#26296b" stroke-width="2"/>""", """<line x1="18.45" x2="18.45" y1="34" y2="10" stroke="#26296b" stroke-width="1.8"/><path d="M18.45 10 Q25.5 16 23.5 24" fill="none" stroke="#26296b" stroke-width="2"/>""")
# Dynamics' pictures: 4.7 x 3.4 heads (edge 4.57), 1.4 stems -> 3.87
R("""<line x1="' + (x + 5) + '" x2="' + (x + 5) + '" y1="' + (y - 1) + '" y2="' + (y - 24) + '" stroke="' + PEN_N + '" stroke-width="1.4"/>'""", """<line x1="' + (x + 3.87) + '" x2="' + (x + 3.87) + '" y1="' + y + '" y2="' + (y - 24) + '" stroke="' + PEN_N + '" stroke-width="1.4"/>'""")
# 6/8's dotted crotchet: 6 x 4.4 at 22 degrees (edge 5.80), 1.8 stem -> 4.9
R("""<ellipse cx="18" cy="30" rx="6" ry="4.4" fill="#26296b" transform="rotate(-22 18 30)"/><line x1="23.6" x2="23.6" y1="29" y2="8" stroke="#26296b" stroke-width="1.8"/>""", """<ellipse cx="18" cy="30" rx="6" ry="4.4" fill="#26296b" transform="rotate(-22 18 30)"/><line x1="22.9" x2="22.9" y1="30" y2="8" stroke="#26296b" stroke-width="1.8"/>""")
# Composers' 'mine' picture: 4.2 x 3, no tilt, 1.5 stem -> 3.45
R("""<ellipse cx="62" cy="28" rx="4.2" ry="3" fill="' + PEN_C + '"/><line x1="66" x2="66" y1="28" y2="10" stroke="' + PEN_C + '" stroke-width="1.5"/>""", """<ellipse cx="62" cy="28" rx="4.2" ry="3" fill="' + PEN_C + '"/><line x1="65.45" x2="65.45" y1="28" y2="10" stroke="' + PEN_C + '" stroke-width="1.5"/>""")
# the reading pad's quaver pairs: a 1.7 rect stem on a 4.7 x 3.4 head -> its right edge on the head's edge (4.57)
R("""<rect x={x + 4.1} y="5" width="1.7" height="24" fill="#26296b"/>""", """<rect x={x + 2.87} y="5" width="1.7" height="24" fill="#26296b"/>""")
open(dst, 'w', encoding='utf-8').write(s)
print('ok limiter, stems', len(s))
