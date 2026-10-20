import sys
a, b = sys.argv[1], sys.argv[2]
s = open(a, encoding='utf-8').read()
def rep(x, y, n=1):
    global s
    assert s.count(x) == n, (s.count(x), x[:90])
    s = s.replace(x, y)
rep("  fof:    { white: '#dfe9f8', black: '#3b4fa8', stroke: '#3b4fa8' },\n", "  fof:    { white: '#dfe9f8', black: '#3b4fa8', stroke: '#3b4fa8' },\n  seg3:   { white: '#93d0f5', black: '#4a63c9', stroke: '#4a63c9', text: '#26296b' },   // the Scale finder: a 1-2-3 reach (the old finder's blue)\n  seg4:   { white: '#98e6ab', black: '#3fa860', stroke: '#3fa860', text: '#26296b' },   // a 1-2-3-4 reach (the old finder's green)\n")
rep("top = 0, vx = null, clean = false }) {", "top = 0, vx = null, clean = false, nameCol = null }) {")
rep("fill={m ? (m.text || m.stroke) : '#26296b'} style={{pointerEvents:'none',animation:'fadeUp 0.3s both'}}>{names[k.i]}", "fill={(nameCol && nameCol[k.i]) || (m ? (m.text || m.stroke) : '#26296b')} style={{pointerEvents:'none',animation:'fadeUp 0.3s both'}}>{names[k.i]}")
rep("fill={m && m.blackText ? m.blackText : '#fff'} style={{pointerEvents:'none',animation:'fadeUp 0.3s both'}}>{names[k.i]}", "fill={(nameCol && nameCol[k.i]) ? (marks[k.i] === 'pass' ? nameCol[k.i] : '#fff') : m && m.blackText ? m.blackText : '#fff'} style={{pointerEvents:'none',animation:'fadeUp 0.3s both'}}>{names[k.i]}")
rep("ncol, nums, ring, mw, oct, clean }) {", "ncol, nums, ring, mw, oct, clean, inKey }) {")
rep("<TapKeyboard octaves={oct || 2} extraC clean={clean} labels={arcs.length ? 'white' : 'all'} marks={marks} onTap={onTap} top={46} vx={[x0, x1]}", "<TapKeyboard octaves={oct || 2} extraC clean={clean} names={inKey ? names : null} nameCol={inKey ? ncol : null} labels={arcs.length ? 'white' : 'all'} marks={marks} onTap={onTap} top={inKey ? 0 : 46} vx={[x0, x1]}")
rep("{Object.entries(names || {}).map(([k, txt]) => { const col = (ncol && ncol[k]) || '#c0431f';", "{Object.entries(inKey ? {} : (names || {})).map(([k, txt]) => { const col = (ncol && ncol[k]) || '#c0431f';")
rep("mk[KK[q]] = g.kind === 3 ? 'target' : g.kind === 4 ? 'fof' : 'pass'; nc[KK[q]] = g.kind === 3 ? SC_G3 : g.kind === 4 ? SC_G4 : '#26296b';", "mk[KK[q]] = g.kind === 3 ? 'seg3' : g.kind === 4 ? 'seg4' : 'pass'; nc[KK[q]] = '#e4572e';")
rep("<ScKeys nums clean ks={KK}", "<ScKeys inKey clean ks={KK}")
rep("background: '#fbe3da', border: '1.5px solid #e4572e' }}/>{t('1-2-3', '1-2-3')}", "background: SEGMENT_COLORS.three.fill, border: '1.5px solid ' + SEGMENT_COLORS.three.stroke }}/>{t('1-2-3', '1-2-3')}")
rep("background: '#dfe9f8', border: '1.5px solid #3b4fa8' }}/>{t('1-2-3-4', '1-2-3-4')}", "background: SEGMENT_COLORS.four.fill, border: '1.5px solid ' + SEGMENT_COLORS.four.stroke }}/>{t('1-2-3-4', '1-2-3-4')}")
open(b, 'w', encoding='utf-8').write(s); print('ok')
