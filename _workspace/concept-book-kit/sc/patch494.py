#!/usr/bin/env python3
# Phase 494: note names on the scale keyboard (her 2026-10-19 03:26: 'put the note names on the scale keyboard').
# ScaleKeyboard gets an opt-in `names` (one per lit key, the scale's own spelling); the Scale finder steps and Free play pass it.
#   python3 patch494.py in.src.html out.src.html
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    if s.count(a) != n: raise SystemExit('found %d (want %d): %s' % (s.count(a), n, a[:110]))
    s = s.replace(a, b)

rep("function ScaleKeyboard({ rootPc, offsets, fingers, hand, plain }) {", "function ScaleKeyboard({ rootPc, offsets, fingers, hand, plain, names }) {")
rep("  offsets.forEach((off, idx) => { fingerAt[off] = plain ? null : fingers[idx]; lit[off] = true; });",
    "  const nameAt = {};\n  offsets.forEach((off, idx) => { fingerAt[off] = plain ? null : fingers[idx]; lit[off] = true; if (names && names[idx]) nameAt[off] = names[idx]; });")
# white key: name above the finger number
rep("""          {played && (
            <text x={k.whiteIndex*whiteW+whiteW/2} y={whiteH-14} textAnchor="middle" fontSize="14" fontWeight="800" fill="var(--brass)">
              {played}
            </text>
          )}""", """          {nameAt[k.i] && <text x={k.whiteIndex*whiteW+whiteW/2} y={whiteH-36} textAnchor="middle" fontSize="13" fontWeight="900" fill="#26296b">{prettyAny(nameAt[k.i])}</text>}
          {played && (
            <text x={k.whiteIndex*whiteW+whiteW/2} y={whiteH-14} textAnchor="middle" fontSize="14" fontWeight="800" fill="var(--brass)">
              {played}
            </text>
          )}""")
# black key: name above the finger number
rep("""          {played && (
            <text x={(k.precedingWhiteIndex+1)*whiteW} y={blackH-15} textAnchor="middle" fontSize="13" fontWeight="900" fill="#fff">
              {played}
            </text>
          )}""", """          {nameAt[k.i] && <text x={(k.precedingWhiteIndex+1)*whiteW} y={blackH-33} textAnchor="middle" fontSize="11" fontWeight="900" fill="#fffefa">{prettyAny(nameAt[k.i])}</text>}
          {played && (
            <text x={(k.precedingWhiteIndex+1)*whiteW} y={blackH-15} textAnchor="middle" fontSize="13" fontWeight="900" fill="#fff">
              {played}
            </text>
          )}""")
# steps: pass the spelled scale (8 notes, the tonic again on top)
rep("  const nm = prettyNote(k);\n  return (<>\n    <div style={{textAlign:'center',fontFamily:\"'Playfair Display', Georgia, serif\",fontSize:22",
    "  const nm = prettyNote(k);\n  const sp = spellFor(k, 'major'), nmz = sp.concat([sp[0]]);\n  return (<>\n    <div style={{textAlign:'center',fontFamily:\"'Playfair Display', Georgia, serif\",fontSize:22")
rep('<ScaleKeyboard rootPc={info.rootPc} offsets={e.offsets} fingers={e.RH} hand="RH"/></div>}', '<ScaleKeyboard rootPc={info.rootPc} offsets={e.offsets} fingers={e.RH} hand="RH" names={nmz}/></div>}')
rep('<ScaleKeyboard rootPc={info.rootPc} offsets={e.offsets} fingers={e.LH} hand="LH"/></div>}', '<ScaleKeyboard rootPc={info.rootPc} offsets={e.offsets} fingers={e.LH} hand="LH" names={nmz}/></div>}')
# Free play: its own spelled notes (the same row it already prints)
rep('<ScaleKeyboard rootPc={info.rootPc} offsets={offs} fingers={fing(\'RH\')} hand="RH" plain={clash}/>', '<ScaleKeyboard rootPc={info.rootPc} offsets={offs} fingers={fing(\'RH\')} hand="RH" plain={clash} names={names.concat([names[0]])}/>')
rep('<ScaleKeyboard rootPc={info.rootPc} offsets={offs} fingers={fing(\'LH\')} hand="LH" plain={clash}/>', '<ScaleKeyboard rootPc={info.rootPc} offsets={offs} fingers={fing(\'LH\')} hand="LH" plain={clash} names={names.concat([names[0]])}/>')
open(dst, 'w', encoding='utf-8').write(s)
print('patched 494', len(s))
