import sys
a, b = sys.argv[1], sys.argv[2]
s = open(a, encoding='utf-8').read()
def rep(x, y, n=1):
    global s
    assert s.count(x) == n, (s.count(x), x[:90])
    s = s.replace(x, y)
# pastel version (variant B) for the finder keyboards
rep("seg3:   { white: '#f6ac93', black: '#c0431f', stroke: '#c0431f', text: '#26296b' }", "seg3:   { white: '#fad0c2', black: '#e4572e', stroke: '#e4572e', text: '#26296b' }")
rep("seg4:   { white: '#a3baf0', black: '#3b4fa8', stroke: '#3b4fa8', text: '#26296b' }", "seg4:   { white: '#cddcf7', black: '#3b4fa8', stroke: '#3b4fa8', text: '#26296b' }")
rep("nc[KK[q]] = g.kind === 3 ? '#26296b' : g.kind === 4 ? '#26296b' : '#26296b'; } });", "nc[KK[q]] = g.kind === 3 ? '#c0431f' : g.kind === 4 ? '#3b4fa8' : '#26296b'; } });")
# staff finger numbers take the group colour
rep("const fing = (fy, j, v) => (o.ring1 && String(v) !== '1' ? '' : '<circle cx=\"' + pFix(notes[j].x) + '\" cy=\"' + pFix(fy) + '\" r=\"' + R + '\" fill=\"#fff\" stroke=\"' + cor + '\" stroke-width=\"1.5\"/>')",
    "const fing = (fy, j, v) => { const cor = (o.fingerCols && o.fingerCols[j]) || cor0; return (o.ring1 && String(v) !== '1' ? '' : '<circle cx=\"' + pFix(notes[j].x) + '\" cy=\"' + pFix(fy) + '\" r=\"' + R + '\" fill=\"#fff\" stroke=\"' + cor + '\" stroke-width=\"1.5\"/>')")
rep("font-weight=\"900\" fill=\"' + cor + '\">' + v + '</text>');\n  if (o.fingers) {", "font-weight=\"900\" fill=\"' + cor + '\">' + v + '</text>'); };\n  if (o.fingers) {")
rep("  const R = o.fingerR || 9;\n  const fing =", "  const R = o.fingerR || 9, cor0 = cor;\n  const fing =")
rep("ring1: true, ring: an >= 0 && oct === 1", "ring1: true, fingerCols: sfdCols(h === 'R' ? 'RH' : 'LH'), ring: an >= 0 && oct === 1")
rep("  const FORMS = ['natural', 'harmonic', 'melodic'];\n  const FNAME", "  const sfdCols = (hand) => { const e1 = info.octaves[1] && info.octaves[1][hand]; if (!e1) return []; const cs = []; scRuns(mode === 'major' ? key : 'm' + key, hand, e1).forEach(g => { for (let q = g.from; q < g.from + g.len; q++) cs[q] = g.kind === 3 ? '#c0431f' : g.kind === 4 ? '#3b4fa8' : '#26296b'; }); return cs; };\n  const FORMS = ['natural', 'harmonic', 'melodic'];\n  const FNAME")
open(b, 'w', encoding='utf-8').write(s)
