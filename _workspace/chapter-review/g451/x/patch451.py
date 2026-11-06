#!/usr/bin/env python3
# Phase 451 (her 2026-10-12 22:24 '컷아웃 페이지도 오류검사 했어?'): the cut-outs' own QA. Every set, en + ko, every page
# looked at, every fact checked (note cards, rhythm cards, the terms, the tempo race key, the scale and triad sliders, the
# circle of fifths, the chord cake, the chord loop, the song shapes, the composer cards, the element cards, the dice).
# What was wrong:
#  1. Chord loop: the I chord's colour is navy, so its three keys (C E G) looked like black keys on the card.
#  2. Chord loop: 'play the bottom note of each chord with your left hand': the cards show F as C F A and Am as C E A, so the
#     bottom key is C for three of the four chords. The left hand plays the root, the chord's letter.
#  3. Composer cards: the answer list 'oldest first' put Bach before Handel; Handel is the older (both 1685: Handel in
#     February, Bach in March).
#  4. The practice week has 21 stars to fill and 14 star stickers: now 21.
#  5. Element cards: the forte sign's tail was cut off by its box (the icon is shared with the app's Styles chapter).
#  6. Motion cards: 'motion' sat on the name's descenders (Contrary, Parallel).
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(a, b):
    global s
    if s.count(a) != 1: raise SystemExit('found %d: %s' % (s.count(a), a[:90]))
    s = s.replace(a, b)

# 1. the I chord's keys: a light navy, with navy letters, so they never look like black keys
rep("""function CutChordKeys({ letters, col }) {
  return <svg viewBox="0 0 70 22" style={{width:'34mm',display:'block'}}>
    {'CDEFGAB'.split('').map((l, i) => <rect key={l} x={i * 10 + 0.3} y="0.3" width="9.4" height="21.4" fill={letters.includes(l) ? col : '#fff'} stroke={BK.ink} strokeWidth="0.5"/>)}""",
"""function CutChordKeys({ letters, col }) {
  const navy = col === BK.ink || col === '#26296b', fill = navy ? '#a4a9e8' : col;   // Phase 451: navy keys looked like black keys
  return <svg viewBox="0 0 70 22" style={{width:'34mm',display:'block'}}>
    {'CDEFGAB'.split('').map((l, i) => <rect key={l} x={i * 10 + 0.3} y="0.3" width="9.4" height="21.4" fill={letters.includes(l) ? fill : '#fff'} stroke={BK.ink} strokeWidth="0.5"/>)}""")
rep("""fontWeight="900" textAnchor="middle" fill={col === '#e8b93a' ? BK.ink : '#fff'}>{l}</text>)}""",
"""fontWeight="900" textAnchor="middle" fill={col === '#e8b93a' || navy ? BK.ink : '#fff'}>{l}</text>)}""")
# 2. the left hand plays the root
rep("""        <>Lay out <b>I · V · vi · IV</b> (C G Am F) on the loop mat. Play the bottom note of each chord with your left hand, four beats each, round and round.</>,
        'Now play the whole chord with your right hand while your left hand plays the bottom note.',""",
"""        <>Lay out <b>I · V · vi · IV</b> (C G Am F) on the loop mat. Play each chord's <b>root</b>, its letter name (C, G, A, F), with your left hand, four beats each, round and round.</>,
        'Now play the whole chord with your right hand while your left hand plays the root.',""")
# 3. oldest first, to the day where two share a year
rep("""  const order = all.slice().sort((x, y) => x.born - y.born);""",
"""  const tie = { handel: 0, bach: 1, chopin: 0, rschumann: 1 };   // Phase 451: same year: Handel (Feb 1685) before Bach (Mar 1685), Chopin (Mar 1810) before Schumann (Jun 1810)
  const order = all.slice().sort((x, y) => x.born - y.born || (tie[x.id] || 0) - (tie[y.id] || 0));""")
# 4. a sticker for every star (3 rows x 7 days)
rep("""        <CutStrip h={12} pieces={Array.from({ length: 14 }, (_, i) => ({ w: 12.5, col: '#e8b93a', node: <svg viewBox="0 0 12 12" style={{width:'9.5mm',height:'9.5mm',display:'block'}}><polygon points={cutStar(6, 6.3, 5.6, 2.3)} fill="#e8b93a" stroke={BK.ink} strokeWidth="0.5" strokeLinejoin="round"/></svg> }))}/>""",
"""        {[14, 7].map((n, r) => <div key={r} style={{marginTop:r ? '2mm' : 0}}><CutStrip h={12} pieces={Array.from({ length: n }, (_, i) => ({ w: 12.5, col: '#e8b93a', node: <svg viewBox="0 0 12 12" style={{width:'9.5mm',height:'9.5mm',display:'block'}}><polygon points={cutStar(6, 6.3, 5.6, 2.3)} fill="#e8b93a" stroke={BK.ink} strokeWidth="0.5" strokeLinejoin="round"/></svg> }))}/></div>)}""")
# 5. the forte sign's tail inside its box
rep("""<text x="18" y="24" fontSize="22" fontStyle="italic" fontWeight="900" fill={color} style={{ fontFamily: 'Georgia, serif' }}>f</text>""",
"""<text x="18" y="22.4" fontSize="22" fontStyle="italic" fontWeight="900" fill={color} style={{ fontFamily: 'Georgia, serif' }}>f</text>""")
# 6. room between the motion name and 'motion'
rep("""      <div style={{fontSize:9,fontWeight:800,color:BK.muted}}>motion</div>""",
"""      <div style={{fontSize:9,fontWeight:800,color:BK.muted,marginTop:'1.2mm'}}>motion</div>""")
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
