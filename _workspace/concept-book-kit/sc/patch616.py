import sys
a, b = sys.argv[1], sys.argv[2]
s = open(a, encoding='utf-8').read()
def rep(x, y, n=1):
    global s
    assert s.count(x) == n, (s.count(x), x[:90])
    s = s.replace(x, y)
# TapKeyboard: finger numbers well below the black keys, a ring round every thumb (1)
rep("vx = null, clean = false, nameCol = null }) {", "vx = null, clean = false, nameCol = null, numIn = false }) {   // numIn: numbers low in the key, a ring round each 1")
rep("y={labels ? whiteH - (solfaOn() ? 48 : 38) : whiteH - (sf ? 26 : 12)} textAnchor=\"middle\" fontSize={labels ? 19 : 15}", "y={numIn ? 104 : labels ? whiteH - (solfaOn() ? 48 : 38) : whiteH - (sf ? 26 : 12)} textAnchor=\"middle\" fontSize={numIn ? 17 : labels ? 19 : 15}")
rep("            {labels && (\n              <text x={k.x + whiteW / 2} y={whiteH - 12} textAnchor=\"middle\" fontSize=\"13\" fontWeight=\"800\"", "            {numIn && names && names[k.i] === '1' && <circle cx={k.x + whiteW / 2} cy={98} r={12} fill=\"none\" stroke=\"#e4572e\" strokeWidth=\"2\" style={{pointerEvents:'none'}}/>}\n            {labels && (\n              <text x={k.x + whiteW / 2} y={numIn ? whiteH - 6 : whiteH - 12} textAnchor=\"middle\" fontSize={numIn ? 12 : 13} fontWeight=\"800\"")
rep("            {names && names[k.i] && (\n              <text x={k.x + blackW / 2} y={labels === 'all' ? 22", "            {numIn && names && names[k.i] === '1' && <circle cx={k.x + blackW / 2} cy={16} r={11} fill=\"none\" stroke=\"#fff\" strokeWidth=\"2\" style={{pointerEvents:'none'}}/>}\n            {names && names[k.i] && (\n              <text x={k.x + blackW / 2} y={labels === 'all' ? 22")
rep("nameCol={inKey ? ncol : null} labels=", "nameCol={inKey ? ncol : null} numIn={!!inKey} labels=")
# the staff: finger numbers over the notes, a ring only round each 1
rep("const fing = (fy, j, v) => '<circle cx=\"' + pFix(notes[j].x) + '\" cy=\"' + pFix(fy) + '\" r=\"' + R + '\" fill=\"#fff\" stroke=\"' + cor + '\" stroke-width=\"1.5\"/>' + (v === ''", "const fing = (fy, j, v) => (o.ring1 && String(v) !== '1' ? '' : '<circle cx=\"' + pFix(notes[j].x) + '\" cy=\"' + pFix(fy) + '\" r=\"' + R + '\" fill=\"#fff\" stroke=\"' + cor + '\" stroke-width=\"1.5\"/>') + (v === ''")
# the finder: fingers for the staff (one octave)
rep("    const mkS = (d0) => { const it = sfdScaleItems(key, d0); return { items: it, coral: [], alt: skgOf(it, key, n => n.byKey) }; };\n    staff = { k: key, R: mkS(SC_D0[key]), L: mkS(sfdLD0(key)) };", "    const mkS = (d0, h) => { const it = sfdScaleItems(key, d0); return { items: it, coral: [], alt: skgOf(it, key, n => n.byKey), fingers: info.octaves[1][h] }; };\n    staff = { k: key, R: mkS(SC_D0[key], 'RH'), L: mkS(sfdLD0(key), 'LH') };")
rep("    const mkM = (d0) => { const mi = sfdMinItems(key, form, d0); return mi && { items: mi.items, coral: mi.coral, alt:", "    const mkM = (d0, h) => { const mi = sfdMinItems(key, form, d0); return mi && { fingers: clash ? undefined : MINOR_SCALES[key].octaves[1][h], items: mi.items, coral: mi.coral, alt:")
rep("const mR = mkM(null), mL = mkM(sfdLD0(key));", "const mR = mkM(null, 'RH'), mL = mkM(sfdLD0(key), 'LH');")
rep("signHl: staff[h].coral, underAlt: staff[h].alt, ksCol: '#2e8a6e',", "signHl: staff[h].coral, underAlt: staff[h].alt, ksCol: '#2e8a6e', fingers: staff[h].fingers, ring1: true,")
open(b, 'w', encoding='utf-8').write(s); print('ok')
