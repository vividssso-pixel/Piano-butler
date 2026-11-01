p='drills.src.html'; s=open(p).read()
if 'm30' in s: print('already'); raise SystemExit
def rep(old, new):
    global s
    assert s.count(old)==1, (s.count(old), old[:90])
    s=s.replace(old,new)

# 1. floor height: a checkpoint row under the open floor
rep("    const rh = lay.clean ? lay.h : (cmp ? 45 + (fs.wp === 'drape' ? 7 : 0) : RH) + (lay.ml - 1) * 14 + (view.subs ? 13 : 0) /* m26: room for the 'what you learn' line on paper */, fh = shut ? LH + (cmp ? 4 : 6) : LH + rh * (RS ? RS.length : Math.ceil(n / c));",
    "    const fck = !o.print && view.chk ? view.chk[k] || [] : [], CR = fck.length && !shut ? (cmp ? 22 : 26) : 0;   // m30: the floor's checkpoint, on the floor itself\n"
    "    const rh = lay.clean ? lay.h : (cmp ? 45 + (fs.wp === 'drape' ? 7 : 0) : RH) + (lay.ml - 1) * 14 + (view.subs ? 13 : 0) /* m26: room for the 'what you learn' line on paper */, fh = shut ? LH + (cmp ? 4 : 6) : LH + rh * (RS ? RS.length : Math.ceil(n / c)) + CR;")

# 2. plaque B on screen: navy (coral on your floor), a gold line inside, cream capitals
rep("    body += stR(px, yy + (cmp ? 2 : 4), pw, cmp ? 18 : 20, 0.9) + stR(px + 2, yy + (cmp ? 4 : 6), pw - 4, cmp ? 14 : 16, 0.4, 'none')\n      + stT((X0 + X1) / 2, yy + (cmp ? 15.2 : 18.4), name, { size: 11.5, weight: 700, font: TH_CAPS, digits: \"'Playfair Display',Georgia,serif\", ls: '0.09em', fill: here ? ST.C : st.st.every(v => v === 'done') ? ST.G : ST.N, anchor: 'middle' });",
    "    if (o.print) body += stR(px, yy + (cmp ? 2 : 4), pw, cmp ? 18 : 20, 0.9) + stR(px + 2, yy + (cmp ? 4 : 6), pw - 4, cmp ? 14 : 16, 0.4, 'none')\n      + stT((X0 + X1) / 2, yy + (cmp ? 15.2 : 18.4), name, { size: 11.5, weight: 700, font: TH_CAPS, digits: \"'Playfair Display',Georgia,serif\", ls: '0.09em', fill: here ? ST.C : st.st.every(v => v === 'done') ? ST.G : ST.N, anchor: 'middle' });\n"
    "    else body += '<rect x=\"' + pFix(px) + '\" y=\"' + pFix(yy + (cmp ? 2 : 4)) + '\" width=\"' + pFix(pw) + '\" height=\"' + (cmp ? 18 : 20) + '\" fill=\"' + (here ? ST.C : ST.N) + '\" stroke=\"' + (here ? ST.C : ST.N) + '\" stroke-width=\"0.9\"/>'   // m30: plaque B (her pick)\n"
    "      + '<rect x=\"' + pFix(px + 2.2) + '\" y=\"' + pFix(yy + (cmp ? 4.2 : 6.2)) + '\" width=\"' + pFix(pw - 4.4) + '\" height=\"' + (cmp ? 13.6 : 15.6) + '\" fill=\"none\" stroke=\"' + (here ? '#fff' : '#c9a24f') + '\" stroke-width=\"0.7\"/>'\n"
    "      + stT((X0 + X1) / 2, yy + (cmp ? 15.2 : 18.4), name, { size: 11.5, weight: 700, font: TH_CAPS, digits: \"'Playfair Display',Georgia,serif\", ls: '0.09em', fill: '#f6ead0', anchor: 'middle' });\n"
    "    fck.forEach((f, j) => {   // m30: a '✓ Check' pill on the left of every floor (Beginner: 1 and 2)\n"
    "      const pwid = fck.length > 1 ? (cmp ? 30 : 34) : (cmp ? 48 : 56), ph = cmp ? 14 : 16, x0 = L0 + 6 + j * (pwid + 4), y0 = yy + (LH - ph) / 2 + (cmp ? 1 : 1), ok = view.chkOk && view.chkOk[f.key];\n"
    "      body += '<rect x=\"' + pFix(x0) + '\" y=\"' + pFix(y0) + '\" width=\"' + pwid + '\" height=\"' + ph + '\" rx=\"' + (ph / 2) + '\" fill=\"' + (ok ? ST.G : '#fff') + '\" stroke=\"' + (ok ? ST.G : ST.N) + '\" stroke-width=\"1\"/>'\n"
    "        + stT(x0 + pwid / 2, y0 + ph * 0.7, '✓ ' + (fck.length > 1 ? String(j + 1) : t('Check', '점검')), { size: cmp ? 8 : 9, weight: 800, font: TH_SANS, fill: ok ? '#fff' : ST.N, anchor: 'middle' });\n"
    "      out.btns.push({ num: 1000 + k * 2 + j, html: '<g data-floorcheck=\"' + f.key + '\" role=\"button\" tabindex=\"0\" aria-label=\"' + penEsc(name + ' checkpoint' + (fck.length > 1 ? ' ' + (j + 1) : '')).replace(/\"/g, '&quot;') + '\" style=\"cursor:pointer\"><rect x=\"' + pFix(x0 - 2) + '\" y=\"' + pFix(y0 - 3) + '\" width=\"' + (pwid + 4) + '\" height=\"' + (ph + 6) + '\" fill=\"transparent\" stroke=\"none\"/></g>' });\n"
    "    });")

# 3. the open floor's checkpoint row, under its rooms
rep("    st.ids.forEach((id, j) => {\n      const [r, cc] = at(j), rw = rwOf(j);\n      body += thRoom(view, state, id, L0 + cc * rw, yy + LH + (nr - 1 - r) * rh, rw, rh, fs, out, o.dimNew, lay, cmp);\n    });",
    "    { st.ids.forEach((id, j) => {\n      const [r, cc] = at(j), rw = rwOf(j);\n      body += thRoom(view, state, id, L0 + cc * rw, yy + LH + (nr - 1 - r) * rh, rw, rh, fs, out, o.dimNew, lay, cmp);\n    });\n"
    "    if (CR) { const ry = yy + LH + nr * rh, cw = (L1 - L0) / fck.length;   // m30: the checkpoint row\n"
    "      body += '<rect x=\"' + L0 + '\" y=\"' + pFix(ry) + '\" width=\"' + (L1 - L0) + '\" height=\"' + CR + '\" fill=\"#fff6f1\" stroke=\"none\"/>' + '<line x1=\"' + L0 + '\" x2=\"' + L1 + '\" y1=\"' + pFix(ry) + '\" y2=\"' + pFix(ry) + '\" stroke=\"' + ST.N + '\" stroke-width=\"0.6\" stroke-dasharray=\"3 2\"/>';\n"
    "      fck.forEach((f, j) => { const x0 = L0 + j * cw, N = f.part ? FLOOR_HALF_N : FLOOR_N, lab = fck.length > 1 ? (f.part === 1 ? t('Checkpoint 1', '점검 1') : t('Checkpoint 2', '점검 2')) : name.charAt(0) + name.slice(1).toLowerCase() + t(' checkpoint', ' 점검');\n"
    "        body += stT(x0 + 9, ry + CR * 0.64, lab + ' · ' + N + t(' questions', '문제'), { size: cmp ? 9.5 : 11, weight: 800, font: TH_SANS, fill: ST.N }) + stT(x0 + cw - 9, ry + CR * 0.64, t('Start ›', '시작 ›'), { size: cmp ? 9.5 : 11, weight: 900, font: TH_SANS, fill: ST.C, anchor: 'end' });\n"
    "        out.btns.push({ num: 2000 + k * 2 + j, html: '<g data-floorcheck=\"' + f.key + '\" role=\"button\" tabindex=\"0\" aria-label=\"' + penEsc(lab).replace(/\"/g, '&quot;') + '\" style=\"cursor:pointer\"><rect x=\"' + pFix(x0) + '\" y=\"' + pFix(ry) + '\" width=\"' + pFix(cw) + '\" height=\"' + CR + '\" fill=\"transparent\" stroke=\"none\"/></g>' }); }); } }")

# 4. HouseMap: the checkpoints in the view; a tap opens the card for that floor
rep("  const view = { stages, here, nums, openK: effK, focus: null, star, review: placeReview(),",
    "  const chkByK = {}, chkOk = {}, chkRec = loadChecks().floors; checkFloors().forEach(f => { (chkByK[f.k] = chkByK[f.k] || []).push(f); const r = chkRec[f.key]; if (r && !r.review.length) chkOk[f.key] = 1; });   // m30\n"
    "  const [chkPick, setChkPick] = useState(null);\n"
    "  const view = { stages, here, nums, openK: effK, chk: chkByK, chkOk, focus: null, star, review: placeReview(),")
rep("  const house = useMemo(() => townhouseSvg(view, { wide }), [sig, UI_TEACHER, LANG, effK]);",
    "  const house = useMemo(() => townhouseSvg(view, { wide }), [sig, UI_TEACHER, LANG, effK, Object.keys(chkOk).join(',')]);")
rep("    const fl = e.target.closest && e.target.closest('[data-floor]'); if (fl) {",
    "    const fc = e.target.closest && e.target.closest('[data-floorcheck]'); if (fc) { setPeek(null); setChkPick(fc.getAttribute('data-floorcheck')); return; }   // m30\n"
    "    const fl = e.target.closest && e.target.closest('[data-floor]'); if (fl) {")
rep("    else if (g.getAttribute('data-floor') != null) {",
    "    else if (g.getAttribute('data-floorcheck') != null) { e.preventDefault(); setChkPick(g.getAttribute('data-floorcheck')); }\n"
    "    else if (g.getAttribute('data-floor') != null) {")
rep("{!compact && <FloorCheckCard here={here} onOpen={onOpen}/>}",
    "{!compact && chkPick && <FloorCheckCard key={chkPick} here={here} onOpen={onOpen} pick={chkPick} onClose={() => setChkPick(null)}/>}")

# 5. the card: opened for one floor, no chips, a close button, scrolled into view
rep("function FloorCheckCard({ here, onOpen }) {\n  const floors = checkFloors(), hereF = Math.max(0, floors.findIndex(f => f.ids.includes(here)));",
    "function FloorCheckCard({ here, onOpen, pick, onClose }) {   // m30: pick, the floor tapped in the house\n  const floors = checkFloors(), hereF = pick ? Math.max(0, floors.findIndex(f => f.key === pick)) : Math.max(0, floors.findIndex(f => f.ids.includes(here)));")
rep("  const box = useRef(null);\n  const f = floors[sel]; if (!f) return null;",
    "  const box = useRef(null);\n  useEffect(() => { if (!pick) return; const id = setTimeout(() => { try { box.current.scrollIntoView({ behavior: 'smooth', block: 'center' }); } catch (e) {} }, 60); return () => clearTimeout(id); }, [pick]);\n  const f = floors[sel]; if (!f) return null;")
rep("    <div style={chkKicker}>{t('Floor checkpoint', '층 중간점검')}</div>\n    <div style={{display:'flex',flexWrap:'wrap',gap:5,margin:'4px 0 8px'}}>{floors.map(chip)}</div>",
    "    <div style={{display:'flex',justifyContent:'space-between',alignItems:'center'}}><div style={chkKicker}>{t('Floor checkpoint', '층 중간점검')}</div>{onClose && mode !== 'run' && <button type=\"button\" data-testid=\"floor-check-close\" onClick={onClose} style={{border:'none',background:'none',font:'inherit',fontSize:13,fontWeight:800,color:'#4a4d86',cursor:'pointer'}}>✕</button>}</div>\n    {!pick && <div style={{display:'flex',flexWrap:'wrap',gap:5,margin:'4px 0 8px'}}>{floors.map(chip)}</div>}")
open(p,'w').write(s); print('ok')
