import sys
a, b, V = sys.argv[1], sys.argv[2], sys.argv[3]
s = open(a, encoding='utf-8').read()
def rep(x, y, n=1):
    global s
    assert s.count(x) == n, (s.count(x), x[:90])
    s = s.replace(x, y)
SPEC = {
 'A': ("'#f6ac93', black: '#c0431f', stroke: '#c0431f', text: '#26296b'", "'#a3baf0', black: '#3b4fa8', stroke: '#3b4fa8', text: '#26296b'", ("'#26296b'", "'#26296b'", "'#26296b'")),
 'B': ("'#fad0c2', black: '#e4572e', stroke: '#e4572e', text: '#26296b'", "'#cddcf7', black: '#3b4fa8', stroke: '#3b4fa8', text: '#26296b'", ("'#c0431f'", "'#3b4fa8'", "'#26296b'")),
 'C': ("'#e4572e', black: '#a83315', stroke: '#a83315', text: '#fff'", "'#3b4fa8', black: '#26296b', stroke: '#26296b', text: '#fff'", ("'#fff'", "'#fff'", "'#c0431f'")),
}[V]
rep("  seg3:   { white: '#93d0f5', black: '#4a63c9', stroke: '#4a63c9', text: '#26296b' },", "  seg3:   { white: " + SPEC[0] + " },")
rep("  seg4:   { white: '#98e6ab', black: '#3fa860', stroke: '#3fa860', text: '#26296b' },", "  seg4:   { white: " + SPEC[1] + " },")
rep("nc[KK[q]] = '#e4572e'; } });", "nc[KK[q]] = g.kind === 3 ? " + SPEC[2][0] + " : g.kind === 4 ? " + SPEC[2][1] + " : " + SPEC[2][2] + "; } });")
rep("background: SEGMENT_COLORS.three.fill, border: '1.5px solid ' + SEGMENT_COLORS.three.stroke", "background: MARK_STYLE.seg3.white, border: '1.5px solid ' + MARK_STYLE.seg3.stroke")
rep("background: SEGMENT_COLORS.four.fill, border: '1.5px solid ' + SEGMENT_COLORS.four.stroke", "background: MARK_STYLE.seg4.white, border: '1.5px solid ' + MARK_STYLE.seg4.stroke")
rep("r={12} fill=\"none\" stroke=\"#e4572e\" strokeWidth=\"2\"", "r={12} fill=\"none\" stroke={(nameCol && nameCol[k.i]) || '#e4572e'} strokeWidth=\"2\"")
open(b, 'w', encoding='utf-8').write(s)
