#!/usr/bin/env python3
# Phase 430: the cut-in-corner frame inside the Lesson Book's picture boxes.
# Online (drills.html, the chapter pages) the page is zoomed 1.12 on screens >= 900px, and the frame measured the
# box with getBoundingClientRect (zoomed px) but drew in the box's own px -> 12% too big, spilling out of every box.
# Her 2026-10-12 00:58: remove it online. The printed books keep it, measured zoom-proof (computed width/height).
import sys
src, out = sys.argv[1], sys.argv[2]; s = open(src, encoding='utf-8').read()
def rep(a, b):
    global s
    if s.count(a) != 1: raise SystemExit('%r found %d' % (a[:80], s.count(a)))
    s = s.replace(a, b)
rep("""// a hairline frame with cut-in corners and a finer line inside it, drawn inside a box (it measures the box)
function VicCutFrame({ inset = 9, r = 11, gap = 3 }) {
  const ref = React.useRef(null); const [sz, setSz] = useState(null);
  React.useLayoutEffect(() => { const el = ref.current; if (!el) return; const m = () => { const b = el.getBoundingClientRect(); setSz([b.width, b.height]); };""",
"""// a hairline frame with cut-in corners and a finer line inside it, drawn inside a box (it measures the box in the
// box's own px -- its computed width/height, not getBoundingClientRect, which a zoomed page scales; Phase 430)
function VicCutFrame({ inset = 9, r = 11, gap = 3 }) {
  const ref = React.useRef(null); const [sz, setSz] = useState(null);
  React.useLayoutEffect(() => { const el = ref.current; if (!el) return; const m = () => { const c = getComputedStyle(el), w = parseFloat(c.width), h = parseFloat(c.height); if (w && h) setSz([w, h]); };""")
rep("""// inside page margins); white, with the cut-in-corner frame inside
function LbPic({ children, h, gap = 18, pad = '14px 16px' }) {
  const pp = String(pad).split(' ').map(parseFloat), p = pp.length === 1 ? (pp[0] + 4) + 'px ' + (pp[0] + 8) + 'px' : pp.map((v, i) => (i % 2 ? v + 8 : v + 4) + 'px').join(' ');
  return <div className="lb-pic" style={{position:'relative',background:'#fff',border:'0.8px solid ' + BK.ink2,padding:p,display:'flex',alignItems:'center',justifyContent:'center',gap,minHeight:lbScreen() ? 0 : h,flex:'1 1 auto',flexWrap:'wrap'}}>{children}<VicCutFrame/></div>;""",
"""// inside page margins); white, with the cut-in-corner frame inside -- in the printed books only: online the plain
// box (Sohyun 2026-10-12: the frame sat crooked in every chapter on the web; Phase 430)
function LbPic({ children, h, gap = 18, pad = '14px 16px' }) {
  const scr = lbScreen();
  const pp = String(pad).split(' ').map(parseFloat), p = pp.length === 1 ? (pp[0] + 4) + 'px ' + (pp[0] + 8) + 'px' : pp.map((v, i) => (i % 2 ? v + 8 : v + 4) + 'px').join(' ');
  return <div className="lb-pic" style={{position:'relative',background:'#fff',border:'0.8px solid ' + BK.ink2,padding:p,display:'flex',alignItems:'center',justifyContent:'center',gap,minHeight:scr ? 0 : h,flex:'1 1 auto',flexWrap:'wrap'}}>{children}{!scr && <VicCutFrame/>}</div>;""")
open(out, 'w', encoding='utf-8').write(s); print('patched')
