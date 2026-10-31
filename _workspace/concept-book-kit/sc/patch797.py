"""Build DU, her 11:07 (on t796 -> t797): 'the string shaking was better; weren't the pedals there too?' The Piano's Story's
'Key, hammer, damper' pad (step 3) gets back what the older 'Inside the piano' had: the string shakes while it sounds (a red
wobble that fades as the sound dies) and the pedals sit under it, tappable: the right pedal lifts every damper and keeps the
string singing after you let go; the left pedal (una corda) moves the hammers onto fewer strings, softer (on today's grand two
of the three, as the diploma room says); the middle pedal points to the next page."""
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def R(old, new, n=1):
    global s
    c = s.count(old); assert c == n, (c, n, old[:120]); s = s.replace(old, new)

# the drawing: a shaking string while it sounds (vib: one id per strike; the static red line stays for the printed pages)
R("""function SpsAction({ down = false, ham, show = 'words', hl, letters = 'ABCD', size = 13, pedal = false, ring = false, arrow = true }) {""",
  """function SpsAction({ down = false, ham, show = 'words', hl, letters = 'ABCD', size = 13, pedal = false, ring = false, arrow = true, vib = 0 }) {""")
R("""    <line x1="30" x2="300" y1="62" y2="62" stroke={hl === 'string' ? PEN_C : PEN_N} strokeWidth={hl === 'string' ? 3 : 2}/>
    {ring && <path d="M40 62 Q120 55 165 62 T290 62" fill="none" stroke={PEN_C} strokeWidth="1.4" opacity="0.8"/>}""",
  """    <line x1="30" x2="300" y1="62" y2="62" stroke={hl === 'string' ? PEN_C : PEN_N} strokeWidth={hl === 'string' ? 3 : 2} opacity={vib ? 0.25 : 1}/>
    {ring && !vib && <path d="M40 62 Q120 55 165 62 T290 62" fill="none" stroke={PEN_C} strokeWidth="1.4" opacity="0.8"/>}
    {vib ? <g key={vib} className="sps-fade"><path className="sps-wob" d="M30 62 Q165 50 300 62" fill="none" stroke={PEN_C} strokeWidth="2.2"/></g> : null}""")

# the pad: the key, the shaking string, and the three pedals under it
i = s.index('function SpsActionPad() {'); j = s.index('// a fixed shuffle for one quiz', i)
s = s[:i] + r'''function SpsActionPad() {
  const [down, setDown] = useState(false), [ham, setHam] = useState('rest'), [vib, setVib] = useState(0), [sus, setSus] = useState(false), [una, setUna] = useState(false), [mid, setMid] = useState(false), { quiz, setQuiz, score, answer } = useSpsQuiz();
  const note = useRef(null), downRef = useRef(false), susRef = useRef(false), T = useRef([]);
  susRef.current = sus;
  const damp = () => { if (note.current) { note.current.damp(); note.current = null; } setVib(0); };
  const stopMe = useRef(() => { T.current.forEach(clearTimeout); T.current = []; if (note.current) { note.current.damp(); note.current = null; } downRef.current = false; setVib(0); setDown(false); setHam('rest'); }).current;
  useEffect(() => () => { T.current.forEach(clearTimeout); if (note.current) note.current.damp(); spsRelease(stopMe); }, []);
  function press() { if (downRef.current || quiz) return; spsTake(stopMe); T.current.forEach(clearTimeout); T.current = []; if (note.current) note.current.damp();
    downRef.current = true; setDown(true); setHam('strike'); setMid(false); const id = Date.now(); setVib(id);
    T.current.push(setTimeout(() => setHam(h => (h === 'strike' ? 'held' : h)), 110));
    T.current.push(setTimeout(() => setVib(v => (v === id ? 0 : v)), 4500));
    const ctx = getAudio(); if (ctx) note.current = actionNote(ctx, una); }
  function release() { if (!downRef.current) return; downRef.current = false; setDown(false); setHam('rest'); if (!susRef.current) { damp(); spsRelease(stopMe); } }
  function tapPedal(p) { if (quiz) return; if (p === 'middle') { setMid(true); return; } setMid(false);
    if (p === 'soft') { setUna(u => !u); return; }
    const nx = !sus; setSus(nx); if (!nx && !downRef.current) damp(); }
  function ask() { release(); setSus(false); setUna(false); damp(); let p; do { p = pick(SPS_PARTS); } while (quiz && quiz.p === p); setQuiz({ p, ans: null }); }
  const st = (p) => !quiz || quiz.ans == null ? '' : p === quiz.p ? ' good' : p === quiz.ans ? ' bad' : '';
  const status = mid ? t('The middle pedal is on the next page.', '가운데 페달은 다음 쪽에 있어요.')
    : down ? (sus ? t('Key down, right pedal down: the damper is up and the string sings.', '건반도 페달도 누름: 댐퍼가 올라가 있고 현이 노래해요.') : t('Key down: the hammer hit the string and fell back; the damper is up, so the string shakes and sings.', '건반을 누르면: 해머가 현을 치고 떨어져요. 댐퍼가 들려 있어서 현이 떨며 울려요.'))
    : vib ? t('You let go, but the right pedal holds every damper up: the string keeps singing and slowly fades.', '손을 뗐지만 오른쪽 페달이 댐퍼를 모두 들고 있어요: 현이 계속 울리다가 천천히 사라져요.')
    : sus ? t('Right pedal down: every damper is lifted. Now hold the key.', '오른쪽 페달을 밟으면 댐퍼가 모두 들려요. 이제 건반을 눌러 봐요.')
    : t('Hold the key, then let go. Watch the string, the hammer and the damper.', '건반을 꾹 눌렀다가 떼 봐요. 현, 해머, 댐퍼를 잘 봐요.');
  return (
    <div className="try-box" style={actBox} data-sps="action">
      <style>{'@keyframes spsWob{0%,100%{transform:scaleY(1)}50%{transform:scaleY(-1)}}@keyframes spsFade{from{opacity:1}to{opacity:0}}.sps-wob{transform-box:fill-box;transform-origin:center;animation:spsWob 0.09s linear infinite}.sps-fade{animation:spsFade 4.4s linear forwards}@media (prefers-reduced-motion: reduce){.sps-wob{animation:none}}'}</style>
      <div style={actTitle}>{t('Key, hammer, damper', '건반, 해머, 댐퍼')}</div>
      <div style={actNote}>{quiz ? t('What is the red part called?', '빨간 부분의 이름은?') : t('Hold the key down: the hammer strikes the string and comes back, the damper moves off, and the string shakes as it sings. Let go: the damper stops it. Then try the pedals.', '건반을 꾹 누르고 있어 봐요: 해머가 현을 치고 되돌아오고, 댐퍼가 떨어지고, 현이 떨며 울려요. 손을 떼 봐요: 댐퍼가 현을 멈춰요. 그다음 페달도 밟아 봐요.')}</div>
      <div style={{maxWidth:460,margin:'0 auto',touchAction:'none',userSelect:'none'}} onPointerDown={(e) => { if (quiz) return; e.preventDefault(); press(); }} onPointerUp={release} onPointerLeave={release} onPointerCancel={release}>
        <SpsAction down={!quiz && down} pedal={!quiz && sus} ham={quiz ? 'rest' : ham} vib={quiz ? 0 : vib} show={quiz ? 'none' : 'words'} hl={quiz ? quiz.p : undefined} size={20}/>
      </div>
      {!quiz && <div style={{textAlign:'center',marginTop:4}}><button className="primary-btn" data-sps-hold style={{width:'auto',padding:'10px 20px',fontSize:15,touchAction:'none',minHeight:44}} onPointerDown={(e) => { e.preventDefault(); press(); }} onPointerUp={release} onPointerLeave={release} onPointerCancel={release}
        onKeyDown={(e) => { if ((e.key === ' ' || e.key === 'Enter') && !e.repeat) { e.preventDefault(); press(); } }} onKeyUp={(e) => { if (e.key === ' ' || e.key === 'Enter') release(); }}>{t('Hold the key', '건반 누르고 있기')}</button></div>}
      {!quiz && <div style={{display:'flex',gap:10,alignItems:'center',justifyContent:'center',flexWrap:'wrap',margin:'10px auto 0',maxWidth:460}}>
        <div style={{flex:'1 1 240px',maxWidth:300,minWidth:0}} data-sps-pedals><SpsPedals down={[...(una ? ['soft'] : []), ...(sus ? ['sustain'] : [])]} onTap={tapPedal} short size={15}/></div>
        <svg viewBox="0 0 76 70" style={{width:76,flex:'0 0 auto'}} role="img" aria-label={una ? t('Seen from above: the hammer has moved and strikes two of the note’s three strings.', '위에서 보면: 해머가 옮겨 가서 한 음의 현 세 줄 중 두 줄을 쳐요.') : t('Seen from above: the hammer strikes all three of the note’s strings.', '위에서 보면: 해머가 한 음의 현 세 줄을 모두 쳐요.')}>
          <rect x="1" y="1" width="74" height="68" rx="8" fill="#fff" stroke={PEN_N} strokeOpacity="0.25"/>
          {[24, 38, 52].map(x => <line key={x} x1={x} x2={x} y1="8" y2="46" stroke={PEN_N} strokeWidth="1.6"/>)}
          <rect x={una ? 33 : 17} y="20" width={una ? 26 : 42} height="12" rx="3" fill={PEN_C} opacity="0.85" style={{transition:'all .2s'}}/>
          <text x="38" y="62" fontSize="10" fontWeight="800" fill={BK.muted} textAnchor="middle">{una ? t('2 strings', '현 2줄') : t('3 strings', '현 3줄')}</text>
        </svg>
      </div>}
      {!quiz && <div style={{fontSize:14,color:BK.ink,lineHeight:1.5,margin:'8px auto 0',maxWidth:460,minHeight:42,textAlign:'center',fontWeight:700}} data-sps-status>{status}</div>}
      {!quiz && una && <div style={{fontSize:13,color:BK.muted,lineHeight:1.45,margin:'2px auto 0',maxWidth:460,textAlign:'center'}}>{t('Left pedal (una corda): the hammers move over and strike fewer strings, softer. On today’s grand, two of the three treble strings.', '왼쪽 페달(우나 코르다): 해머가 옆으로 옮겨 더 적은 줄을 쳐요, 더 여리게. 오늘의 그랜드에서는 고음 세 줄 중 두 줄.')}</div>}
      {quiz && <div style={{display:'grid',gridTemplateColumns:'repeat(2,minmax(0,1fr))',gap:6,marginTop:6}}>{shuffleOnce(quiz, SPS_PARTS).map(p => spsChoice(st(p), SPS_PART_W[p](), () => answer(p, p === quiz.p), p))}</div>}
      {quiz && quiz.ans != null && spsNote(quiz.ans === quiz.p, <>{spsCap(t('the ' + SPS_PART_W[quiz.p](), SPS_PART_W[quiz.p]()))}.{spsScore(score)}</>)}
      {spsQuizBtns(quiz, ask, () => setQuiz(null))}
    </div>
  );
}
''' + s[j:]

# (2) her 11:09: the instruments redrawn in the books' look (the grand three-quarter with its keys showing, as the house design
# asks; the side view that hid the keys was rejected there). Same props and boxes as before.
LIB = '// Build DU (her 11:09 \'redraw the pianos and instruments, classy, in the design\'): the keyboard instruments in the books\' look --\n// navy line on white, a diagonal hatch for the wood\'s dark faces, turned legs, mouldings as double hairlines, coral only for\n// what the page is about (the strings, a candle flame, a pedal). Each returns SVG markup in its own box.\nconst PB_INST = (() => { const N = PEN_N, C = PEN_C;\nlet _hid = 0;\nconst hatch = (id, gap = 3.2) => \'<pattern id="\' + id + \'" width="\' + gap + \'" height="\' + gap + \'" patternUnits="userSpaceOnUse" patternTransform="rotate(40)"><rect width="\' + gap + \'" height="\' + gap + \'" fill="#fff"/><line x1="0" y1="0" x2="0" y2="\' + gap + \'" stroke="\' + N + \'" stroke-width="0.7"/></pattern>\';\nconst L = (d, w = 1.6, o = \'\') => \'<path d="\' + d + \'" fill="none" stroke="\' + N + \'" stroke-width="\' + w + \'" stroke-linecap="round" stroke-linejoin="round"\' + o + \'/>\';\nconst F = (d, fill = \'#fff\', w = 1.6) => \'<path d="\' + d + \'" fill="\' + fill + \'" stroke="\' + N + \'" stroke-width="\' + w + \'" stroke-linejoin="round"/>\';\n// a turned leg from (x, y0) to (x, y1): a collar, a bulb, a taper, a small foot\nconst leg = (x, y0, y1, w = 5) => { const h = y1 - y0, b = y0 + h * 0.28;\n  return F(\'M\' + (x - w / 2) + \' \' + y0 + \' H\' + (x + w / 2) + \' V\' + (y0 + 3) + \' H\' + (x - w / 2) + \' Z\') +\n    F(\'M\' + (x - w / 2 + 0.4) + \' \' + (y0 + 3) + \' C\' + (x - w * 0.95) + \' \' + (b - 3) + \' \' + (x - w * 0.95) + \' \' + (b + 4) + \' \' + (x - w / 2 + 0.6) + \' \' + (b + 7) +\n      \' L\' + (x - w / 2 + 1.2) + \' \' + (y1 - 3) + \' H\' + (x + w / 2 - 1.2) + \' L\' + (x + w / 2 - 0.6) + \' \' + (b + 7) +\n      \' C\' + (x + w * 0.95) + \' \' + (b + 4) + \' \' + (x + w * 0.95) + \' \' + (b - 3) + \' \' + (x + w / 2 - 0.4) + \' \' + (y0 + 3) + \' Z\', \'#fff\', 1.4) +\n    F(\'M\' + (x - w / 2 - 0.6) + \' \' + (y1 - 3) + \' H\' + (x + w / 2 + 0.6) + \' V\' + y1 + \' H\' + (x - w / 2 - 0.6) + \' Z\', N, 1); };\n// a strip of keys seen from the front: white keys as lines, black keys in the 2-3 pattern\nconst keys = (x, y, w, h, n) => { const kw = w / n; let s = F(\'M\' + x + \' \' + y + \' H\' + (x + w) + \' V\' + (y + h) + \' H\' + x + \' Z\', \'#fff\', 1.3);\n  for (let i = 1; i < n; i++) s += \'<line x1="\' + (x + i * kw) + \'" x2="\' + (x + i * kw) + \'" y1="\' + y + \'" y2="\' + (y + h) + \'" stroke="\' + N + \'" stroke-width="0.6"/>\';\n  for (let i = 0; i < n - 1; i++) if ([0, 1, 3, 4, 5].includes(i % 7)) s += \'<rect x="\' + (x + (i + 1) * kw - kw * 0.32) + \'" y="\' + y + \'" width="\' + (kw * 0.64) + \'" height="\' + (h * 0.58) + \'" fill="\' + N + \'"/>\';\n  return s; };\n\n// ── a grand piano, three-quarter from the keyboard side: the lid up on its stick, the keys showing, three turned legs, the\n// lyre with its pedals; cut: the strings inside, in coral ──\nfunction grandSvg({ cut = false, lidUp = true } = {}) {\n  const id = \'pbinst\' + (++_hid);\n  let s = \'<defs>\' + hatch(id) + \'</defs>\';\n  // the lid, hinged on the spine (from the front corner back to the tail), propped open on its stick\n  if (lidUp) s += F(\'M16 70 L128 38 C150 30 186 14 196 8 C204 4 200 -2 190 0 C160 6 130 20 104 30 Z\', \'url(#\' + id + \')\', 1.6) + F(\'M30 64 L120 38 C140 30 170 16 182 9 C162 14 132 26 108 34 Z\', \'#fff\', 0.8);\n  // the rim\'s side under the bentside, hatched\n  s += F(\'M16 70 L16 82 L112 82 C150 82 168 60 198 58 L198 46 C168 48 150 70 112 70 Z\', \'url(#\' + id + \')\', 1.6);\n  // the top: the spine running back to the tail, the bentside curving round to the keyboard\n  s += F(\'M16 70 L128 38 C150 34 192 36 198 42 C200 44 199 46 198 46 C168 48 150 70 112 70 Z\', \'#fff\', 1.6);\n  if (cut) for (let i = 0; i < 8; i++) s += \'<line x1="\' + (30 + i * 11) + \'" y1="\' + (67 - i * 0.6) + \'" x2="\' + (132 + i * 8) + \'" y2="\' + (40 + i * 0.9) + \'" stroke="\' + C + \'" stroke-width="1.3"/>\';\n  if (lidUp) s += L(\'M160 58 L150 22\', 1.6);\n  // the music desk, the keys between their cheeks\n  s += F(\'M44 62 L96 62 L94 54 L46 54 Z\', \'#fff\', 1.2) + L(\'M50 58 H90\', 0.6);\n  s += F(\'M12 66 H20 V80 H12 Z\', \'#fff\', 1.4) + F(\'M108 66 H116 V80 H108 Z\', \'#fff\', 1.4) + keys(20, 68, 88, 11, 20) + F(\'M12 80 H116 V83 H12 Z\', \'url(#\' + id + \')\', 1.1);\n  // the legs, the lyre and its pedals\n  s += leg(20, 83, 114, 6) + leg(108, 83, 114, 6) + leg(190, 58, 104, 5);\n  s += F(\'M58 83 H72 V86 H58 Z\', \'#fff\', 1.1) + L(\'M60 86 C56 92 60 98 61 104 M70 86 C74 92 70 98 69 104 M63 86 V104 M67 86 V104\', 1.1) + F(\'M56 104 H74 V107 H56 Z\', N, 1) + L(\'M60 107 V111 M65 107 V111 M70 107 V111\', 1.8);\n  return s;\n}\n// ── a parlour upright from the front: a moulded top, panels in double hairlines, candle sconces (coral flames), the keys, the\n// consoles, the toe blocks, three pedals; cut: the strings standing up inside, in coral ──\nfunction uprightSvg({ cut = false } = {}) {\n  const id = \'pbinst\' + (++_hid);\n  let s = \'<defs>\' + hatch(id) + \'</defs>\';\n  s += F(\'M6 6 H164 V12 H6 Z\', \'#fff\', 1.6) + F(\'M2 2 H168 V6 H2 Z\', \'url(#\' + id + \')\', 1.4);\n  s += F(\'M10 12 H160 V66 H10 Z\', \'#fff\', 1.6);\n  if (cut) { s += F(\'M20 18 H150 V58 H20 Z\', \'#fff\', 1); for (let i = 0; i < 15; i++) s += \'<line x1="\' + (26 + i * 8.4) + \'" x2="\' + (28 + i * 8.2) + \'" y1="\' + (20 + (i < 5 ? 0 : 3)) + \'" y2="56" stroke="\' + C + \'" stroke-width="\' + (i < 5 ? 1.8 : 1.1) + \'"/>\'; }\n  else { s += F(\'M20 18 H150 V58 H20 Z\', \'#fff\', 1) + F(\'M24 22 H146 V54 H24 Z\', \'#fff\', 0.7) + F(\'M56 34 H114 V46 H56 Z\', \'#fff\', 1.1) + L(\'M60 38 H110 M60 42 H104\', 0.6); }\n  // candle sconces on the front, one each side\n  [16, 154].forEach(x => { s += L(\'M\' + x + \' 40 C\' + (x + (x < 85 ? -6 : 6)) + \' 40 \' + (x + (x < 85 ? -6 : 6)) + \' 34 \' + (x + (x < 85 ? -6 : 6)) + \' 30\', 1.2) + F(\'M\' + (x + (x < 85 ? -8 : 4)) + \' 30 H\' + (x + (x < 85 ? -4 : 8)) + \' V24 H\' + (x + (x < 85 ? -8 : 4)) + \' Z\', \'#fff\', 1) +\n    \'<path d="M\' + (x + (x < 85 ? -6 : 6)) + \' 23 C\' + (x + (x < 85 ? -8 : 4)) + \' 20 \' + (x + (x < 85 ? -6 : 6)) + \' 16 \' + (x + (x < 85 ? -6 : 6)) + \' 15 C\' + (x + (x < 85 ? -4 : 8)) + \' 18 \' + (x + (x < 85 ? -4 : 8)) + \' 21 \' + (x + (x < 85 ? -6 : 6)) + \' 23 Z" fill="\' + C + \'"/>\'; });\n  // the key bed, the keys, the consoles (scrolls) under the cheeks\n  s += F(\'M4 66 H166 V70 H4 Z\', \'#fff\', 1.4) + keys(14, 70, 142, 11, 24) + F(\'M4 70 H14 V81 H4 Z\', \'#fff\', 1.4) + F(\'M156 70 H166 V81 H156 Z\', \'#fff\', 1.4) + F(\'M4 81 H166 V84 H4 Z\', \'url(#\' + id + \')\', 1.2);\n  s += L(\'M9 84 C4 92 14 96 10 104\', 1.6) + L(\'M161 84 C166 92 156 96 160 104\', 1.6);\n  // the lower panel, the plinth and toe blocks, the pedals\n  s += F(\'M12 84 H158 V112 H12 Z\', \'#fff\', 1.6) + F(\'M30 88 H140 V106 H30 Z\', \'#fff\', 0.8) + F(\'M34 91 H136 V103 H34 Z\', \'#fff\', 0.6);\n  s += F(\'M8 112 H162 V118 H8 Z\', \'url(#\' + id + \')\', 1.4) + F(\'M2 104 H16 V118 H2 Z\', \'#fff\', 1.4) + F(\'M154 104 H168 V118 H154 Z\', \'#fff\', 1.4);\n  [74, 85, 96].forEach(x => { s += F(\'M\' + (x - 3) + \' 110 H\' + (x + 3) + \' L\' + (x + 4) + \' 115 H\' + (x - 4) + \' Z\', N, 1); });\n  return s;\n}\n// ── a harpsichord, three-quarter: long and slender, the lid up with a painted border, two stepped keyboards (one: a single\n// keyboard, as Cristofori\'s piano was built), a stand on turned legs with a stretcher, no pedals ──\nfunction harpsichordSvg({ one = false } = {}) {\n  const id = \'pbinst\' + (++_hid);\n  let s = \'<defs>\' + hatch(id) + \'</defs>\';\n  s += F(\'M18 72 L140 42 C162 36 192 18 204 12 C210 8 206 4 198 6 C168 14 136 28 100 36 Z\', \'url(#\' + id + \')\', 1.6) + F(\'M34 66 L132 42 C152 36 176 24 190 15 C168 22 136 32 104 40 Z\', \'#fff\', 0.8) + L(\'M42 64 L130 44\', 0.6, \' stroke-dasharray="2 2"\');\n  s += F(\'M18 72 L18 82 L112 82 C150 82 176 62 206 56 L206 48 C176 52 150 72 112 72 Z\', \'url(#\' + id + \')\', 1.6);\n  s += F(\'M18 72 L140 42 C162 38 200 40 206 46 L206 48 C176 52 150 72 112 72 Z\', \'#fff\', 1.6);\n  s += L(\'M150 62 L156 26\', 1.5);\n  const manual = (x, y, w) => keys(x, y, w, 6, 16);\n  s += F(\'M14 66 H20 V80 H14 Z\', \'#fff\', 1.4) + F(\'M104 66 H110 V80 H104 Z\', \'#fff\', 1.4);\n  s += one ? manual(20, 70, 84) : manual(22, 66, 80) + manual(20, 73, 84);\n  s += F(\'M14 82 H114 V86 H14 Z\', \'#fff\', 1.4) + leg(20, 86, 114, 5) + leg(108, 86, 114, 5) + leg(198, 56, 104, 4.5) + L(\'M20 104 H108 L196 96\', 1.3);\n  return s;\n}\n// ── a clavichord on its stand: a box seen from the front and a little above, the lid up behind with a painted border, the\n// keys set into the front, four turned legs, a stretcher ──\nfunction clavichordSvg() {\n  const id = \'pbinst\' + (++_hid);\n  let s = \'<defs>\' + hatch(id) + \'</defs>\';\n  s += F(\'M24 46 L36 10 H184 L172 46 Z\', \'url(#\' + id + \')\', 1.6) + F(\'M32 44 L41 15 H179 L170 44 Z\', \'#fff\', 0.8);\n  s += F(\'M16 46 H184 L190 52 H10 Z\', \'#fff\', 1.6) + F(\'M10 52 H190 V72 H10 Z\', \'url(#\' + id + \')\', 1.6);\n  s += F(\'M40 54 H128 V70 H40 Z\', \'#fff\', 1.2) + keys(42, 56, 84, 12, 16);\n  s += F(\'M14 72 H186 V77 H14 Z\', \'#fff\', 1.4) + leg(22, 77, 112, 5) + leg(178, 77, 112, 5) + leg(60, 77, 106, 4) + leg(140, 77, 106, 4) + L(\'M22 100 H178\', 1.4);\n  return s;\n}\n// ── the front of a piano of any year, for the pedals\' story: the keys between their cheeks, the key bed, two turned legs;\n// hand: hand stops on the cheeks (coral knobs); knee: knee levers under the keys (coral); ped: pedals on a lyre ──\nfunction frontSvg({ hand = 0, knee = 0, ped = 0 } = {}) {\n  const id = \'pbinst\' + (++_hid);\n  let s = \'<defs>\' + hatch(id) + \'</defs>\';\n  s += F(\'M14 18 H286 V24 H14 Z\', \'url(#\' + id + \')\', 1.4) + F(\'M14 24 H26 V46 H14 Z\', \'#fff\', 1.4) + F(\'M274 24 H286 V46 H274 Z\', \'#fff\', 1.4) + keys(26, 26, 248, 20, 35);\n  s += F(\'M14 46 H286 V56 H14 Z\', \'url(#\' + id + \')\', 1.4) + L(\'M18 50 H282\', 0.6);\n  s += leg(34, 56, 128, 9) + leg(266, 56, 128, 9);\n  if (hand >= 1) s += \'<circle cx="9" cy="35" r="4.5" fill="\' + C + \'"/>\' + L(\'M13.5 35 H14\', 2);\n  if (hand >= 2) s += \'<circle cx="291" cy="35" r="4.5" fill="\' + C + \'"/>\' + L(\'M286 35 H286.5\', 2);\n  if (knee >= 1) s += \'<rect x="124" y="58" width="13" height="28" rx="5" fill="\' + C + \'" stroke="\' + N + \'" stroke-width="1.2"/>\';\n  if (knee >= 2) s += \'<rect x="163" y="58" width="13" height="28" rx="5" fill="\' + C + \'" stroke="\' + N + \'" stroke-width="1.2"/>\';\n  if (ped) { s += F(\'M136 56 H164 V60 H136 Z\', \'#fff\', 1.1) + L(\'M139 60 C132 76 138 96 140 112 M161 60 C168 76 162 96 160 112 M146 60 V112 M154 60 V112\', 1.2) + F(\'M126 112 H174 V117 H126 Z\', \'#fff\', 1.3);\n    const xs = ped === 2 ? [138, 162] : [132, 150, 168]; xs.forEach(x => { s += \'<path d="M\' + (x - 5) + \' 117 L\' + (x - 8) + \' 128 Q\' + x + \' 132 \' + (x + 8) + \' 128 L\' + (x + 5) + \' 117 Z" fill="\' + C + \'" stroke="\' + N + \'" stroke-width="1.2"/>\'; }); }\n  return s;\n}\nreturn { grand: grandSvg, upright: uprightSvg, harpsichord: harpsichordSvg, clavichord: clavichordSvg, front: frontSvg };\n})();\n'
i = s.index('function SpsGrand('); j = s.index('// ── how each sounds its string, close up', i)
s = s[:i] + LIB + """function SpsGrand({ x = 0, y = 0, s = 1, cut, lidUp = true }) {
  return <g transform={'translate(' + x + ' ' + y + ') scale(' + s + ')'} dangerouslySetInnerHTML={{ __html: PB_INST.grand({ cut: !!cut, lidUp }) }}/>;
}
function SpsUpright({ x = 0, y = 0, s = 1, cut }) {
  return <g transform={'translate(' + x + ' ' + y + ') scale(' + s + ')'} dangerouslySetInnerHTML={{ __html: PB_INST.upright({ cut: !!cut }) }}/>;
}
function SpsHarpsichord({ x = 0, y = 0, s = 1, one }) {
  return <g transform={'translate(' + x + ' ' + y + ') scale(' + s + ')'} dangerouslySetInnerHTML={{ __html: PB_INST.harpsichord({ one: !!one }) }}/>;
}
function SpsClavichord({ x = 0, y = 0, s = 1 }) {
  return <g transform={'translate(' + x + ' ' + y + ') scale(' + s + ')'} dangerouslySetInnerHTML={{ __html: PB_INST.clavichord() }}/>;
}
""" + s[j:]
# the diploma room's piano fronts (hand stops, knee levers, pedals) in the same look
i = s.index('function Ps8Front('); j = s.index('// the markings: [id, the marking', i)
s = s[:i] + """function Ps8Front({ ctl = {}, w = 300 }) {
  return <svg viewBox="0 -2 300 138" style={{width:'100%',maxWidth:w,display:'block',margin:'0 auto'}} role="img" aria-label={t('The front of a piano: ', '피아노의 앞모습: ') + [ctl.hand ? t(ctl.hand + ' hand stop(s) beside the keys', '건반 옆 손잡이 ' + ctl.hand + '개') : '', ctl.knee ? t(ctl.knee + ' knee lever(s) under the keys', '건반 아래 무릎 레버 ' + ctl.knee + '개') : '', ctl.ped ? t(ctl.ped + ' pedal(s)', '페달 ' + ctl.ped + '개') : ''].filter(Boolean).join(', ')}><g dangerouslySetInnerHTML={{ __html: PB_INST.front(ctl) }}/></svg>;
}
""" + s[j:]
# (3) the pedals' drawing in the same look: a hatched key bed, a classical lyre (two curving arms and three rods), a hatched
# pedal box; the pedals and their taps as before
R("""    <rect x="30" y="2" width="280" height="12" rx="2" {...SPS_SWF} strokeWidth="1.6"/>
    <path d="M120 14 L124 74 Q126 86 140 88 L200 88 Q214 86 216 74 L220 14" {...SPS_SWF} strokeWidth="2"/>
    <path d="M148 14 L148 80 M170 14 L170 80 M192 14 L192 80" {...SPS_SW} strokeWidth="1.3"/>
    <rect x="40" y="88" width="260" height="14" rx="4" {...SPS_SWF}/>""",
  """    <g dangerouslySetInnerHTML={{ __html: '<defs><pattern id="pbinstped" width="3.2" height="3.2" patternUnits="userSpaceOnUse" patternTransform="rotate(40)"><rect width="3.2" height="3.2" fill="#fff"/><line x1="0" y1="0" x2="0" y2="3.2" stroke="' + PEN_N + '" stroke-width="0.7"/></pattern></defs>' }}/>
    <rect x="30" y="2" width="280" height="12" rx="1.5" fill="url(#pbinstped)" stroke={PEN_N} strokeWidth="1.6"/>
    <rect x="132" y="14" width="76" height="6" fill="#fff" stroke={PEN_N} strokeWidth="1.3"/>
    <path d="M138 20 C116 40 132 66 142 88 M202 20 C224 40 208 66 198 88" fill="none" stroke={PEN_N} strokeWidth="2" strokeLinecap="round"/>
    <path d="M156 20 L156 88 M170 20 L170 88 M184 20 L184 88" {...SPS_SW} strokeWidth="1.2"/>
    <rect x="40" y="88" width="260" height="14" rx="2" fill="url(#pbinstped)" stroke={PEN_N} strokeWidth="1.6"/>""")
# (4) her 11:18: the Scale finder inside the chapter too. In every scales room, under the opener and above the steps, a closed
# panel 'Scale finder' that opens the finder right there (the 'More to play with' card at the end stays)
R("""      {DICT_BRING[id] && <DictChips ch={id}/>}
      <div style={{display:'flex',flexWrap:'wrap',gap:5,margin:'4px 0 2px'}}>""", """      {DICT_BRING[id] && <DictChips ch={id}/>}
      <LessonFinder id={id}/>
      <div style={{display:'flex',flexWrap:'wrap',gap:5,margin:'4px 0 2px'}}>""")
R("""function LessonMore({ id }) {""", """// Build DU (her 11:18): the Scale finder inside every scales room, closed until tapped
const LESSON_SF_ROOMS = ['scales', 'scale-play', 'minor-scales', 'scales-23', 'scales-3', 'scales-4', 'scales-5', 'scales-6', 'scales-7', 'scales-8', 'arps-6', 'arps-7', 'arps-8'];
function LessonFinder({ id }) {
  const [open, setOpen] = useState(false);
  if (!LESSON_SF_ROOMS.includes(id)) return null;
  return <div data-lesson-finder style={{margin:'4px 0 10px',border:'1.5px solid rgba(38,41,107,0.18)',borderRadius:12,background:'#fff'}}>
    <button type="button" onClick={() => setOpen(o => !o)} aria-expanded={open} style={{display:'flex',alignItems:'center',gap:10,width:'100%',minHeight:48,padding:'8px 12px',background:'none',border:'none',cursor:'pointer',fontFamily:'inherit',textAlign:'left',color:'var(--navy)'}}>
      <span style={{flex:'0 0 auto',fontSize:10.5,fontWeight:900,color:'#e4572e',letterSpacing:'0.08em'}}>{t('TOOL', '도구')}</span>
      <span style={{flex:1,minWidth:0}}><span style={{display:'block',fontSize:16,fontWeight:900}}>{t('Scale finder', '스케일 찾기')}</span><span style={{display:'block',fontSize:12.5,fontWeight:700,color:'var(--muted)',lineHeight:1.35}}>{t('Any key: its notes, both hands’ fingers, its key signature', '어떤 조든: 음, 양손 손가락 번호, 조표')}</span></span>
      <span aria-hidden="true" style={{flex:'0 0 auto',color:'#e4572e',fontSize:22,fontWeight:900,transform:open ? 'rotate(90deg)' : 'none',transition:'transform 0.2s'}}>›</span></button>
    {open && <div style={{borderTop:'1px solid rgba(38,41,107,0.14)',padding:'6px 2px 4px',minWidth:0,animation:'fadeUp 0.25s both'}}><ScaleFinderDial/></div>}
  </div>;
}
function LessonMore({ id }) {""")
open(dst, 'w', encoding='utf-8').write(s)
print('ok action pad, instruments, finder', len(s))
