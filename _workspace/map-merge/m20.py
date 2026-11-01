p='drills.src.html'; s=open(p).read()
if 'm20' in s: print('already'); raise SystemExit
# 1. quoins: white again
old="const f = sp.hall ? '#fff' : TH_Q_TINT[sp.wp] || '#fff';"
assert s.count(old)==1
s=s.replace(old,"const f = '#fff';   // m20: her 'the coloured bricks back to navy or white'")
# 2. one floor open
old="    const rh = lay.clean ? lay.h : (cmp ? 45 + (fs.wp === 'drape' ? 7 : 0) : RH) + (lay.ml - 1) * 14, fh = LH + rh * (RS ? RS.length : Math.ceil(n / c));"
assert s.count(old)==1
s=s.replace(old,"    const shut = !o.print && view.openK != null && k !== view.openK;   // m20: one floor open (hers: 'the Library shows everything; here just the floor I am on')\n    const rh = lay.clean ? lay.h : (cmp ? 45 + (fs.wp === 'drape' ? 7 : 0) : RH) + (lay.ml - 1) * 14, fh = shut ? LH + (cmp ? 4 : 6) : LH + rh * (RS ? RS.length : Math.ceil(n / c));")
old="    const nr = RS ? RS.length : Math.ceil(n / c);   // Phase 442: the first rooms on the lowest row, counted from the bottom left -- you climb the house\n    st.ids.forEach((id, j) => {"
assert s.count(old)==1
s=s.replace(old,"""    const nr = RS ? RS.length : Math.ceil(n / c);   // Phase 442: the first rooms on the lowest row, counted from the bottom left -- you climb the house
    if (shut) {   // a closed floor: its plaque, how many rooms are done, and a tap opens it
      const dn = st.st.filter(v => v === 'done').length;
      body += stT(L1 - 8, yy + (cmp ? 15.2 : 18.4), dn + '/' + n + '  ▸', { size: cmp ? 10 : 11.5, weight: 800, font: TH_SANS, fill: dn === n ? ST.G : '#6d6f9c', anchor: 'end' });
      out.btns.push({ num: -100 + k, html: '<g data-floor="' + k + '" role="button" tabindex="0" aria-label="' + penEsc(name + ': ' + dn + ' of ' + n).replace(/"/g, '&quot;') + '" style="cursor:pointer"><rect x="' + L0 + '" y="' + pFix(yy) + '" width="' + (L1 - L0) + '" height="' + (fh - 1) + '" fill="transparent" stroke="none"/></g>' });
    } else
    st.ids.forEach((id, j) => {""")
# HouseMap state
old="  const [opening, setOpening] = useState(false), [peek, setPeek] = useState(null);   // Build BN"
assert s.count(old)==1
s=s.replace(old,"  const [openK, setOpenK] = useState(null);   // m20: the floor open by hand (null: your floor)\n"+old)
old="  const view = { stages, here, nums, focus: topic, star, review: placeReview(),"
assert s.count(old)==1
s=s.replace(old,"  const hereK = Math.max(0, stages.findIndex(x => x.ids.includes(here))), effK = openK == null ? hereK : openK;\n  const view = { stages, here, nums, openK: effK, focus: topic, star, review: placeReview(),")
old="  const house = useMemo(() => townhouseSvg(view, { wide }), [sig, UI_TEACHER, LANG]);"
assert s.count(old)==1
s=s.replace(old,"  const house = useMemo(() => townhouseSvg(view, { wide }), [sig, UI_TEACHER, LANG, effK]);")
old="    if (e.target.closest && e.target.closest('[data-door]')) { enter(); return; }"
assert s.count(old)==1
s=s.replace(old,old+"\n    const fl = e.target.closest && e.target.closest('[data-floor]'); if (fl) { setPeek(null); setOpenK(Number(fl.getAttribute('data-floor'))); return; }   // m20")
old="    if (g.getAttribute('data-door') != null) { e.preventDefault(); enter(); }"
assert s.count(old)==1
s=s.replace(old,old+"\n    else if (g.getAttribute('data-floor') != null) { e.preventDefault(); setOpenK(Number(g.getAttribute('data-floor'))); }")
open(p,'w').write(s); print('ok')
