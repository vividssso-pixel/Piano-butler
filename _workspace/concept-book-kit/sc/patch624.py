import sys
a, b = sys.argv[1], sys.argv[2]
s = open(a, encoding='utf-8').read()
def rep(x, y, n=1):
    global s
    assert s.count(x) == n, (s.count(x), x[:90])
    s = s.replace(x, y)
f0 = s.index("function ScaleFinderDial()")
head, body = s[:f0], s[f0:]
s = body
rep("      <g style={{ transform: 'rotate(' + (-rot) + 'deg)', transition: tr }}>\n        <circle r={rr}", "      <g>\n        <circle r={rr}")
d0 = s.index("      <rect x={C - 31}"); d1 = s.index("      <text x={C} y={C - 8}")
s = s[:d0] + """      {SFD_MAJ.map((_, i) => node(i, 'major'))}{SFD_MIN.map((_, i) => node(i, 'minor'))}
      <g data-sfd-rot={-rot} style={{ transform: 'rotate(' + (-rot) + 'deg)', transformOrigin: C + 'px ' + C + 'px', transition: tr, pointerEvents: 'none' }}>
        <rect x={C - 31} y={C - 134 - 24 - 7} width={62} height={134 - 82 + 24 + 21 + 14} rx={31} fill="none" stroke={CO} strokeWidth="2.6"/>
        <path d={'M' + C + ' ' + (C - 62) + ' L' + (C - 8) + ' ' + (C - 36) + ' L' + (C + 8) + ' ' + (C - 36) + ' Z'} fill={CO}/>
      </g>
""" + s[d1:]
# nodes after the capsule so the capsule outline is not under them is fine; remove the old nodes group already replaced
s = s.replace("{SFD_MAJ.map((_, i) => node(i, 'major'))}{SFD_MIN.map((_, i) => node(i, 'minor'))}\n      </g>\n", "", 1) if False else s
# staff ring follows the sounding note on both staves, also in 2 octaves, and glides
rep("ring: an >= 0 && oct === 1 && seq[an].j < 8 ? [seq[an].j] : []", "ringGlide: true, ring: an >= 0 ? [seq[an].j < 8 ? seq[an].j : seq[an].j - 7] : []")
s = head + s
g0 = s.index("function SkgStaff(")
old = "        {(o.ring || []).map(j => mm.notes[j] && <ellipse key={'r' + j} cx={mm.notes[j].x} cy={mm.notes[j].y} rx=\"15\" ry=\"11\" fill=\"none\" stroke={PEN_C} strokeWidth=\"1.8\"/>)}\n"
i = s.index(old, g0)
old2 = old.replace("(o.ring || [])", "(o.ringGlide ? [] : (o.ring || []))")
new = old2 + "        {o.ringGlide && (o.ring || []).length > 0 && mm.notes[o.ring[0]] && <g style={{ transform: 'translate(' + mm.notes[o.ring[0]].x + 'px,' + mm.notes[o.ring[0]].y + 'px)', transition: 'transform 0.25s ease' }}><ellipse rx=\"17\" ry=\"13\" fill=\"rgba(228,87,46,0.16)\" stroke={PEN_C} strokeWidth=\"2.6\"/></g>}\n"
s = s[:i] + new + s[i + len(old):]
open(b, 'w', encoding='utf-8').write(s)
