import sys
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:90],s.count(a)); s=s.replace(a,b)
# straight arrows along the keys instead of arcs: the move reads as a direction (right = up, left = down)
rep("""      {arcs.map(([a, b, anim], j) => { const x1 = kx(a), x2 = kx(b), sp = Math.abs(x2 - x1), cy = 26 - Math.min(28, sp * 0.8 + 6);
        return <path key={j + ':' + a + ':' + b + ':' + nonce} d={'M' + x1 + ',26 Q' + (x1 + x2) / 2 + ',' + cy + ' ' + x2 + ',26'} fill="none" stroke="#e4572e" strokeWidth={anim ? 3 : 1.8} strokeLinecap="round"
          strokeDasharray={anim ? '120' : undefined} strokeDashoffset={anim ? '120' : undefined} style={anim ? {animation:'drawArc 0.45s ease-out forwards'} : undefined}/>; })}""",
"""      {arcs.map(([a, b, anim], j) => { const x1 = kx(a), x2 = kx(b), dir = x2 > x1 ? 1 : -1, hd = anim ? 8 : 5, y = 17, xs = x1 + dir * (anim ? 3 : 1.5), xe = x2 - dir * (anim ? 1 : 0.5);
        return <g key={j + ':' + a + ':' + b + ':' + nonce} fill="none" stroke="#e4572e" strokeWidth={anim ? 3.4 : 1.8} strokeLinecap="round" strokeLinejoin="round">
          <path d={'M' + xs + ',' + y + ' L' + xe + ',' + y} strokeDasharray={anim ? '120' : undefined} strokeDashoffset={anim ? '120' : undefined} style={anim ? {animation:'drawArc 0.45s ease-out forwards'} : undefined}/>
          <path d={'M' + (xe - dir * hd) + ',' + (y - hd * 0.75) + ' L' + xe + ',' + y + ' L' + (xe - dir * hd) + ',' + (y + hd * 0.75)} style={anim ? {animation:'fadeUp 0.3s both 0.3s'} : undefined}/>
        </g>; })}""")
open(sys.argv[2],'w',encoding='utf-8').write(s);print('ok')
