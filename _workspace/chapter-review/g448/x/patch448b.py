#!/usr/bin/env python3
# Phase 448, part 2 (the same QA sweep): since Phase 447 set each clef on its own line, a treble clef's tail hangs 1.68 spaces
# under the bottom line, and several staves' boxes stopped short of it, so the bottom of the tail was cut off (by up to a
# third of a space on paper: PaperStaff, SfStaff, BigStaff). A few boxes also cut the top of the curl by a hair (MelodyStaff,
# CurvePair). Each box now makes room for its clef's ink (clefInkYs, from CLEF_GLYPH). Measured on every page and in every
# drill question: no clef is cut off (kit/clefclip448.js).
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    if s.count(a) != n: raise SystemExit('found %d (want %d): %s' % (s.count(a), n, a[:90]))
    s = s.replace(a, b)

# the helper, next to the geometry it reads
rep("""function ClefGlyph({ clef, yOf, st, ink }) {""",
"""// Phase 448: where a clef's ink reaches, top and bottom (0.6 of a unit each side for the faint edge the ink scan trims),
// so a staff's box can make room for it.
function clefInkYs(clef, yOf, st) { const g = CLEF_GLYPH[clef]; return g ? [yOf(g.top, st) - g.topPad - 0.6, yOf(g.bottom, st) + g.bottomPad + 0.6] : []; }
function ClefGlyph({ clef, yOf, st, ink }) {""")

# PaperStaff (Workbook, cut-outs)
rep("""  staves.forEach(st => ys.push(yOf(CLEFS[st].high, st) - 15, yOf(CLEFS[st].low, st) + 13));
  notes.forEach(n => { const st = staffOf(n); ys.push(yOf(n.d, st) - 9, yOf(n.d, st) + 9);""",
"""  staves.forEach(st => ys.push(yOf(CLEFS[st].high, st) - 15, yOf(CLEFS[st].low, st) + 13));
  if (clefOn) staves.forEach(st => ys.push(...clefInkYs(st, yOf, st)));   // Phase 448: the treble clef's tail
  notes.forEach(n => { const st = staffOf(n); ys.push(yOf(n.d, st) - 9, yOf(n.d, st) + 9);""")

# SfStaff (Lesson Books, Workbook)
rep("""  const y0 = Math.min(...ys) - pad[0], y1 = Math.max(...ys) + pad[1];
  const inner = (shapes, vb) =>""",
"""  let y0 = Math.min(...ys) - pad[0], y1 = Math.max(...ys) + pad[1];
  if (!none) staves.forEach(st => { const [a, b] = clefInkYs(st, yOf, st); y0 = Math.min(y0, a); y1 = Math.max(y1, b); });   // Phase 448
  const inner = (shapes, vb) =>""")

# BigStaff (Workbook): the clef is scaled to the staff, so its ink is scaled too
rep("""  const yOf = (d) => top + 4 * gap - (d - base) * (gap / 2);
  return (
    <svg viewBox={`0 0 ${width} ${top + 4 * gap + h1}`} style={{width:'100%',display:'block'}}>""",
"""  const yOf = (d) => top + 4 * gap - (d - base) * (gap / 2);
  const ty = top + 4 * gap - (clef === 'treble' ? 100 : 160) * gap / 10, ink = clefInkYs(clef, dY, clef).map(y => ty + y * gap / 10);   // Phase 448
  const vy0 = Math.min(0, ink[0]), vy1 = Math.max(top + 4 * gap + h1, ink[1]);
  return (
    <svg viewBox={`0 ${vy0} ${width} ${vy1 - vy0}`} style={{width:'100%',display:'block'}}>""")

# MelodyStaff (drills): the top of the curl
rep("""  let y0 = dY(top) - (fingers ? 12 : 4), y1 = dY(bot) + (counts ? 26 : 6) + (names ? 14 : 0);
  let t = 0;""",
"""  let y0 = dY(top) - (fingers ? 12 : 4), y1 = dY(bot) + (counts ? 26 : 6) + (names ? 14 : 0);
  { const [a, b] = clefInkYs(clef, dY, clef); y0 = Math.min(y0, a); y1 = Math.max(y1, b); }   // Phase 448
  let t = 0;""")

# CurvePair (ties and slurs): the top of the curl
rep("""    <svg viewBox={`0 ${dY(40)} ${width} ${dY(26) - dY(40)}`} style={{width:'100%',maxWidth:width * 1.6,display:'block',margin:'0 auto'}}>
      {[30, 32, 34, 36, 38].map(l =>""",
"""    <svg viewBox={`0 ${dY(40) - 6} ${width} ${dY(26) - dY(40) + 6}`} style={{width:'100%',maxWidth:width * 1.6,display:'block',margin:'0 auto'}}>
      {[30, 32, 34, 36, 38].map(l =>""")

# KSStaff and PlaceIt (key signatures): two more units at the bottom
rep("""    <svg viewBox={`0 ${base - (numbers ? 72 : 60)} ${width} ${numbers ? 88 : 76}`}""",
"""    <svg viewBox={`0 ${base - (numbers ? 72 : 60)} ${width} ${numbers ? 90 : 78}`}""")
rep("""      <svg viewBox={`0 ${base - 64} ${W} 80`} style={{width:'100%',maxWidth:W * 1.6,display:'block',margin:'0 auto',touchAction:'manipulation'}}>""",
"""      <svg viewBox={`0 ${base - 64} ${W} 82`} style={{width:'100%',maxWidth:W * 1.6,display:'block',margin:'0 auto',touchAction:'manipulation'}}>""")

# IntervalStaff, ChordStaff, StaffFrame (drills)
rep("""  const ys = [dY(c.high) - 18, dY(c.low) + 16];""",
"""  const ys = [dY(c.high) - 18, dY(c.low) + 16, ...clefInkYs(clef, dY, clef)];   // Phase 448: and the clef""")
rep("""  const y0 = dY(top) - 18, y1 = dY(bot) + 16 + (chords.some(ch => ch.label) ? 30 : 0);""",
"""  const y0 = dY(top) - 18, y1 = Math.max(dY(bot) + 16, clefInkYs(clef, dY, clef)[1] || 0) + (chords.some(ch => ch.label) ? 30 : 0);   // Phase 448: and the clef""")
rep("""  const y0 = yOf(topD) - 16, y1 = yOf(botD) + 16;""",
"""  const y0 = yOf(topD) - 16, y1 = yOf(botD) + 18;   // Phase 448: 18, the treble clef's tail""")

# PaperOttava (8va on paper): the clef's tail
rep("""const y0 = up ? dY(46) : dY(41), y1 = up ? dY(27) : dY(22), col""",
"""const y0 = up ? dY(46) : dY(41), y1 = up ? dY(27) + 3 : dY(22), col""")

# CutStaffSystem (cut-out staff mat)
rep("""  const mt = gap * 1.75, mb = gap * 1.6, x0 = 36;""",
"""  const mt = gap * 1.75, mb = gap * 1.75, x0 = 36;   // Phase 448: mb 1.75 (was 1.6), the treble clef's tail""")

# Three Workbook pages grew by a few pixels with the taller staves: tighten their spacing so each still fits its A4 page.
rep("""  const visit = (label, clef, who) => <div style={{border:'1.2px solid rgba(38,41,107,0.22)',borderRadius:12,padding:'8px 12px 6px'}}>""",
"""  const visit = (label, clef, who) => <div style={{border:'1.2px solid rgba(38,41,107,0.22)',borderRadius:12,padding:'7px 12px 3px'}}>""")
rep("""    <Part kind="home" title="Clara visits" how="Draw the note each time, on its little ladder when it is Clara's C.">
      <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:12}}>""",
"""    <Part kind="home" title="Clara visits" how="Draw the note each time, on its little ladder when it is Clara's C.">
      <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:9}}>""")
rep("""{W.crown.lands.map(([cl, d], i) => <ExCell key={i} n={i + 1} ex={i === 0}><div style={{padding:'12px 4px 3px'}}>""",
"""{W.crown.lands.map(([cl, d], i) => <ExCell key={i} n={i + 1} ex={i === 0}><div style={{padding:'9px 4px 2px'}}>""")
rep("""<BkCell key={i} n={i + 1 + W.crown.lands.length}><div style={{padding:'12px 4px 3px'}}>""",
"""<BkCell key={i} n={i + 1 + W.crown.lands.length}><div style={{padding:'9px 4px 2px'}}>""")

open(dst, 'w', encoding='utf-8').write(s)
print('ok')
