import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:100])
    s = s.replace(old, new)
# Build CU, part 3: the strips took room from the pictures, and on some pages the drawing ran past its frame (it already
# did on three pages before: Dynamics pages 3 and 5, The Staff page 3). A printed picture box now fits its drawing: when
# the drawing is taller than the room the page leaves, it is scaled down to fit (never below 60%), measured again once the
# fonts are in. Pages whose drawing fits are untouched. The strips are a little more compact.
rep("""function LbPic({ children, h, gap = 18, pad = '14px 16px' }) {
  const scr = lbScreen();""", """function LbPic({ children, h, gap = 18, pad = '14px 16px' }) {
  const scr = lbScreen(), boxRef = React.useRef(null);
  React.useLayoutEffect(() => {   // Build CU: fit the drawing inside its frame (print only)
    if (scr) return; const el = boxRef.current; if (!el) return;
    const fit = () => {
      const kids = [...el.children].filter(c => getComputedStyle(c).position !== 'absolute'); if (!kids.length) return;
      kids.forEach(c => { if (!('mw0' in c.dataset)) { c.dataset.mw0 = c.style.maxWidth || ''; c.dataset.ml0 = c.style.marginLeft || ''; c.dataset.mr0 = c.style.marginRight || ''; } c.style.maxWidth = c.dataset.mw0; c.style.marginLeft = c.dataset.ml0; c.style.marginRight = c.dataset.mr0; c.style.zoom = ''; });
      const cs = getComputedStyle(el), inner = el.clientHeight - parseFloat(cs.paddingTop) - parseFloat(cs.paddingBottom);
      // the drawn extent, drawings that spill past their own box included (screen px, so divide by the page's own zoom)
      const measure = () => { const r0 = el.getBoundingClientRect(), sc = r0.height && el.offsetHeight ? r0.height / el.offsetHeight : 1; let t0 = Infinity, b0 = -Infinity;
        kids.forEach(k => { [k, ...k.querySelectorAll('*')].forEach(nd => { const r = nd.getBoundingClientRect(); if (r.width > 0 || r.height > 0) { t0 = Math.min(t0, r.top); b0 = Math.max(b0, r.bottom); } }); });
        return { need: (b0 - t0) / sc, sc }; };
      let m = measure(); if (!(inner > 20 && m.need > inner + 2)) return;
      const f = Math.max(0.6, (inner - 4) / m.need);
      kids.forEach(c => { const w = c.getBoundingClientRect().width / m.sc; c.style.maxWidth = (w * f).toFixed(1) + 'px'; c.style.marginLeft = 'auto'; c.style.marginRight = 'auto'; });   // a drawing that fills the width shrinks with it
      m = measure(); if (m.need > inner + 2) { const g = Math.max(0.6, (inner - 4) / m.need); kids.forEach(c => { c.style.zoom = g.toFixed(3); }); }   // anything else: zoom
    };
    fit(); const tm = setTimeout(fit, 500); try { document.fonts.ready.then(fit); } catch (e) {}
    return () => clearTimeout(tm);
  });""")
rep("""  return <div className="lb-pic" style={{position:'relative',background:'#fff',border:'0.8px solid ' + BK.ink2,""", """  return <div ref={boxRef} className="lb-pic" style={{position:'relative',background:'#fff',border:'0.8px solid ' + BK.ink2,""")
# compact strips
rep("""  return <div className="lb-challenge" data-kind={kind} style={{display:'flex',alignItems:'center',gap:'6px 12px',flexWrap:'wrap',borderTop:'0.8px solid ' + BK.ink,borderBottom:'0.8px solid ' + BK.ink,padding:'5px 2px'}}>""",
    """  return <div className="lb-challenge" data-kind={kind} style={{display:'flex',alignItems:'center',gap:'4px 12px',flexWrap:'wrap',borderTop:'0.8px solid ' + BK.ink,borderBottom:'0.8px solid ' + BK.ink,padding:'4px 2px'}}>""")
rep("""    <span style={{flex:'1 1 230px',fontSize:14,lineHeight:1.42,color:BK.ink,minWidth:0}}>{children}</span>""",
    """    <span style={{flex:'1 1 230px',fontSize:13.5,lineHeight:1.38,color:BK.ink,minWidth:0}}>{children}</span>""")
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
