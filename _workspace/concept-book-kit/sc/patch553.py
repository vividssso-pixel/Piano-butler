import sys
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:90],s.count(a)); s=s.replace(a,b)
# TapKeyboard can carry an overlay drawn on the keys
rep("trail = null, trailLabels = null }) {", "trail = null, trailLabels = null, overlay = null }) {")
rep("height\n    </svg>\n  );\n}\n\nconst NOTE_NAME_LEVELS", "height\n    </svg>\n  );\n}\n\nconst NOTE_NAME_LEVELS", 0) if False else None
i=s.index("const NOTE_NAME_LEVELS = [")
j=s.rindex("    </svg>\n  );\n}\n", 0, i)
s=s[:j]+"      {overlay}\n"+s[j:]
# the arrows start at the letter on the key and end on the next key
a=s.index("// one octave C to C with the B below and the C above, so every key has a neighbour on both sides; arcs [from, to, animate?] drawn over it")
b=s.index("function AcStep({ kind }) {")
new=r"""// one octave C to C with the B below and the C above, so every key has a neighbour on both sides.
// arcs [from, to, animate?] are arrows drawn ON the keys: from the letter of a white key (or the middle of a black key) to the next key
function AcKeys({ marks, onTap, arcs, nonce }) {
  const kx = (i) => i === -1 ? 18 : keyCenterX(i) + 36;
  const white = (i) => PC_INFO[((i % 12) + 12) % 12].white;
  const pt = (i) => [kx(i), white(i) ? 99 : 58];
  const arrows = arcs.map(([a, b, anim], j) => {
    const [x1, y1] = pt(a), [x2, y2] = pt(b), dx = x2 - x1, dy = y2 - y1, L = Math.hypot(dx, dy), ux = dx / L, uy = dy / L;
    const s0 = anim ? 7 : 4, s1 = anim ? 5 : 3, hd = anim ? 10 : 4.5, w = anim ? 3.4 : 1.5;
    const sx = x1 + ux * s0, sy = y1 + uy * s0, ex = x2 - ux * s1, ey = y2 - uy * s1, ang = 0.55;
    const hx = (sg) => ex - hd * (ux * Math.cos(ang) - sg * uy * Math.sin(ang)), hy = (sg) => ey - hd * (uy * Math.cos(ang) + sg * ux * Math.sin(ang));
    const line = 'M' + sx + ',' + sy + ' L' + ex + ',' + ey, head = 'M' + hx(1) + ',' + hy(1) + ' L' + ex + ',' + ey + ' L' + hx(-1) + ',' + hy(-1);
    const dash = anim ? { strokeDasharray: '120', strokeDashoffset: '120', animation: 'drawArc 0.45s ease-out forwards' } : {};
    const headAnim = anim ? { animation: 'fadeUp 0.3s both 0.3s' } : {};
    return <g key={j + ':' + a + ':' + b + ':' + nonce} fill="none" strokeLinecap="round" strokeLinejoin="round" style={{pointerEvents:'none'}}>
      <path d={line} stroke="#fff" strokeWidth={w + 3} style={dash}/><path d={head} stroke="#fff" strokeWidth={w + 3} style={headAnim}/>
      <path d={line} stroke="#26296b" strokeWidth={w} style={dash}/><path d={head} stroke="#26296b" strokeWidth={w} style={headAnim}/>
    </g>; });
  return (<div style={{maxWidth:330,margin:'0 auto'}}>
    <TapKeyboard octaves={1} extraB extraC labels="white" marks={marks} onTap={onTap} overlay={<g aria-hidden="true">{arrows}</g>}/>
  </div>);
}
"""
s=s[:a]+new+s[b:]
# the whole picture: a zigzag over the keys (letter, black key, next letter ...)
rep("""    const arcs = []; if (SZ === 1) { for (let k = -1; k <= 11; k++) arcs.push([k, k + 1, false]); } else { for (let k = 0; k <= 10; k += 2) arcs.push([k, k + 2, false]); }""",
    """    const arcs = []; if (SZ === 1) { for (let k = 0; k <= 11; k++) arcs.push([k, k + 1, false]); } else { for (let k = 0; k <= 10; k += 2) arcs.push([k, k + 2, false]); }""")
open(sys.argv[2],'w',encoding='utf-8').write(s);print('ok')
