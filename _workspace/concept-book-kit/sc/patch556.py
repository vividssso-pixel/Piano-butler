import sys
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:90],s.count(a)); s=s.replace(a,b)
rep("trailLabels = null, overlay = null }) {", "trailLabels = null, overlay = null, top = 0 }) {")
rep("const TR = trail && trail.length ? 58 : 0;", "const TR = trail && trail.length ? 58 : top;")
rep("<TapKeyboard octaves={1} extraB extraC labels=\"white\" marks={marks} names={names} onTap={onTap} overlay={<g aria-hidden=\"true\">{arrows}</g>}/>",
    "<TapKeyboard octaves={1} extraB extraC labels=\"white\" marks={marks} onTap={onTap} top={26} overlay={<g aria-hidden=\"true\">{arrows}{Object.entries(names || {}).map(([k, txt]) => <text key={'n' + k + txt} x={kx(+k)} y={-9} textAnchor=\"middle\" fontSize=\"17\" fontWeight=\"900\" fill=\"#c0431f\" style={{animation:'fadeUp 0.3s both'}}>{txt}</text>)}</g>}/>")
rep("{TR > 0 && (() => { const P = trail.map", "{trail && trail.length > 0 && (() => { const P = trail.map")
open(sys.argv[2],'w',encoding='utf-8').write(s);print('ok')
