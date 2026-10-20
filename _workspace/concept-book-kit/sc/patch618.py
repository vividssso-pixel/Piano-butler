import sys
a, b = sys.argv[1], sys.argv[2]
s = open(a, encoding='utf-8').read()
def rep(x, y, n=1):
    global s
    assert s.count(x) == n, (s.count(x), x[:90])
    s = s.replace(x, y)
# state + stop on any change
rep("  const [form, setForm] = useState('harmonic'), [oct, setOct] = useState(1), [stf, setStf] = useState(false), [q, setQ] = useState('');\n  const idx0",
    "  const [form, setForm] = useState('harmonic'), [oct, setOct] = useState(1), [stf, setStf] = useState(false), [q, setQ] = useState('');\n  const [an, setAn] = useState(-1), tmR = useRef([]);\n  const stopA = () => { tmR.current.forEach(clearTimeout); tmR.current = []; setAn(-1); };\n  useEffect(() => { stopA(); }, [key, mode, form, oct]);\n  useEffect(() => () => tmR.current.forEach(clearTimeout), []);\n  const idx0")
# the sequence and the player
rep("  const step = (d) => pick((idx + d + 12) % 12, mode);\n  const body = <>",
"""  const step = (d) => pick((idx + d + 12) % 12, mode);
  // up and down, the same notes for both hands; it stops at every thumb (finger 1) and says whose it is
  const eF = clash ? null : (mode === 'major' ? info.octaves[oct] : fing), KKt = offs.map(o => info.rootPc + o), nT = KKt.length;
  const KD = mode === 'minor' && form === 'melodic' ? minorOffsets('natural', oct).map(o => info.rootPc + o) : KKt;
  const seq = []; for (let j = 0; j < nT; j++) seq.push({ j, k: KKt[j] }); for (let j = nT - 2; j >= 0; j--) seq.push({ j, k: KD[j] });
  const thumbs = (i) => { if (!eF || i === 0 || i === seq.length - 1) return null; const r = eF.RH[seq[i].j] === 1, l = eF.LH[seq[i].j] === 1; return r && l ? 'both' : r ? 'RH' : l ? 'LH' : null; };
  const playA = () => {
    if (an >= 0) { stopA(); return; }
    stopA(); let at = 0;
    seq.forEach((sq, i) => { tmR.current.push(setTimeout(() => { setAn(i); playKey(sq.k, 0.5); }, at)); at += thumbs(i) ? 1700 : 520; });
    tmR.current.push(setTimeout(() => setAn(-1), at + 300));
  };
  const thumbNow = an >= 0 ? thumbs(an) : null;
  const thumbMsg = thumbNow === 'both' ? t('Both thumbs (1).', '양손 엄지(1).') : thumbNow === 'RH' ? t('Right hand: the thumb (1).', '오른손: 엄지(1).') : thumbNow === 'LH' ? t('Left hand: the thumb (1).', '왼손: 엄지(1).') : '';
  const body = <>""")
# the keyboards: the sounding key lit
rep("          const paint = (hand) => { const F = e[hand], mk = {}, nm = {}, nc = {};", "          const paint = (hand) => { const F = e[hand], mk = {}, nm = {}, nc = {}, curK = an >= 0 ? seq[an].k : null;")
rep("F.forEach((f, q) => { nm[KK[q]] = String(f); }); return { mk, nm, nc }; };", "F.forEach((f, q) => { nm[KK[q]] = String(f); }); if (curK != null) { mk[curK] = 'pick'; nc[curK] = '#fff'; } return { mk, nm, nc }; };")
rep("            </div>\n          </div>; })()}\n      {noteDown", "            </div>\n            <div data-sfd-thumb style={{ minHeight: 24, textAlign: 'center', fontWeight: 900, fontSize: 14, color: '#c0431f', marginTop: 6 }}>{thumbMsg}</div>\n          </div>; })()}\n      {noteDown")
# the staff: the sounding note ringed
rep("fingers: staff[h].fingers, ring1: true,", "fingers: staff[h].fingers, ring1: true, ring: an >= 0 && oct === 1 && seq[an].j < 8 ? [seq[an].j] : [],")
# the button
rep("        <button className=\"ghost-btn\" style={scS.back} onClick={() => playScaleNotes(info.rootPc, offs, mode === 'minor' && form === 'melodic' ? minorOffsets('natural', oct) : null)}>{t('♪ Hear it up and down', '♪ 올라갔다 내려오며 듣기')}</button>\n        <button className=\"ghost-btn\" style={scS.prim} data-sfd-rel",
    "        <button className=\"ghost-btn\" style={scS.back} data-sfd-play onClick={playA}>{an >= 0 ? t('■ Stop', '■ 멈추기') : t('▶ Up and down: stops at each thumb', '▶ 올라갔다 내려오기: 엄지에서 멈춰요')}</button>\n        <button className=\"ghost-btn\" style={scS.prim} data-sfd-rel")
rep("{live.tools && live.tools.length > 0 && step(++n, t('Try', '해 보기'), LANG === 'ko' ? live.tryLine[1] : live.tryLine[0], true, () => go({ hs: 'try' }))}", "{live.tools && live.tools.length === 1 && (() => { const tl = TOOLS.find(x => x.id === live.tools[0]); return tl ? step(++n, tl.title, LANG === 'ko' ? live.tryLine[1] : live.tryLine[0], true, () => go({ view: 'tools', tool: tl.id, ret: 'home' })) : null; })()}\n          {live.tools && live.tools.length > 1 && step(++n, t('Try', '해 보기'), LANG === 'ko' ? live.tryLine[1] : live.tryLine[0], true, () => go({ hs: 'try' }))}")
rep("tryLine: ['Scale finder: turn the circle of fifths to any key', '스케일 찾기: 5도권을 돌려 어느 조든 찾아요'],", "tryLine: ['Turn the circle of fifths to any key', '5도권을 돌려 어느 조든 찾아요'],")
open(b, 'w', encoding='utf-8').write(s); print('ok')
