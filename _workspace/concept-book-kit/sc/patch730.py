# Build BK (2026-10-27): call 25, batch 3. A tune from one interval (Intervals): pick 2nd, 3rd, 4th, 5th or octave and
# build a tune hopping only by it, up or down, on the staff. Add a sharp or a flat (Accidentals): Ode to Joy on the
# staff; tap any note to make it sharp, flat or natural again, and hear the colour change. One tune, four styles
# (Styles): Twinkle with a Baroque, Classical, jazz or pop band under it, or the band alone for the child to play the
# tune on top. Transpose a tune (Key signatures) gains My tune: play up to eight notes on C D E F G, then move it.
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()

def rep(old, new, n=1):
    global s
    c = s.count(old)
    assert c == n, (c, n, old[:90])
    s = s.replace(old, new)

CODE = r'''
// ══ Build BK: call 25, batch 3 ══
// a tune from one interval: white keys counted in letters from middle C (0 = C4); every hop is the same number
const IVT_N = [2, 3, 4, 5, 8];
const ivtSemi = (i) => [0, 2, 4, 5, 7, 9, 11][((i % 7) + 7) % 7] + 12 * Math.floor(i / 7);
const IVT_WORD = { 2: ['a 2nd: a step', '2도: 한 걸음'], 3: ['a 3rd: a skip', '3도: 한 칸 건너뛰기'], 4: ['a 4th', '4도'], 5: ['a 5th', '5도'], 8: ['an octave', '옥타브'] };
function IntervalTune() {
  const [n, setN] = useState(3), [seq, setSeq] = useState([0]), [cur, setCur] = useState(-1), tms = useRef([]);
  useEffect(() => () => tms.current.forEach(clearTimeout), []);
  const move = (dir) => { if (seq.length >= 12) return; const nx = seq[seq.length - 1] + dir * (n - 1); if (nx < -7 || nx > 14) return; playKey(ivtSemi(nx), 0.4); setSeq([...seq, nx]); };
  const notes = seq.map((i, j) => ({ d: 28 + i, dur: j === seq.length - 1 && j ? 2 : 1 }));
  const play = () => { tms.current.forEach(clearTimeout); tms.current = playMelody(notes, 100, setCur) || []; tms.current.push(setTimeout(() => setCur(-1), (0.1 + (notes.reduce((a, x) => a + x.dur, 0) + 0.5) * 0.6) * 1000)); };
  const last = seq[seq.length - 1], canUp = last + (n - 1) <= 14 && seq.length < 12, canDn = last - (n - 1) >= -7 && seq.length < 12;
  return (
    <div className="try-box" style={actBox} data-ivt="pad">
      <div style={actTitle}>{t('A tune from one interval', '음정 하나로 선율 만들기')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>음정을 하나 골라요. 선율이 <b>그 음정으로만</b> 위로, 아래로 움직여요. 2도는 걸음, 3도는 건너뛰기, 옥타브는 같은 이름의 음까지. 들어 보면 음정마다 색깔이 달라요.</> : <>Choose one interval. Your tune moves <b>only by that interval</b>, up or down. A 2nd steps, a 3rd skips, an octave jumps to the same letter. Each interval has its own sound.</>}</div>
      {spChips(IVT_N.map(x => [x, t(x === 8 ? 'Octave' : x + (x === 2 ? 'nd' : x === 3 ? 'rd' : 'th'), x === 8 ? '옥타브' : x + '도')]), n, (x) => setN(x))}
      <div style={{textAlign:'center',fontSize:13.5,fontWeight:900,color:BK.coral,margin:'2px 0'}}>{t('Only ' + IVT_WORD[n][0], IVT_WORD[n][1] + '만')}</div>
      <div style={{background:'#fff',borderRadius:8,margin:'4px 0'}}><MelodyStaff notes={notes} on={cur} names width={340}/></div>
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:6}}>
        <button className="ghost-btn" style={spBtn} disabled={!canDn} onClick={() => move(-1)}>{t('▼ Down a ', '▼ 아래로 ') + (n === 8 ? t('n octave', ' 옥타브') : t(n + (n === 2 ? 'nd' : n === 3 ? 'rd' : 'th'), n + '도'))}</button>
        <button className="ghost-btn" style={spBtn} disabled={!canUp} onClick={() => move(1)}>{t('▲ Up a ', '▲ 위로 ') + (n === 8 ? t('n octave', ' 옥타브') : t(n + (n === 2 ? 'nd' : n === 3 ? 'rd' : 'th'), n + '도'))}</button>
      </div>
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        <button className="ghost-btn" style={spBtn} disabled={seq.length < 2} onClick={play}>{t('▶ Play my tune', '▶ 내 선율 듣기')}</button>
        <button className="ghost-btn" style={spBtn} disabled={seq.length < 2} onClick={() => { tms.current.forEach(clearTimeout); setCur(-1); setSeq([0]); }}>{t('Start again', '처음부터')}</button>
      </div>
    </div>
  );
}

// add a sharp or a flat: Ode to Joy on the staff (C D E F G), each note flipped natural, sharp, flat
const ACP_D = { 0: 28, 2: 29, 4: 30, 5: 31, 7: 32 };
function AccPlay() {
  const [acc, setAcc] = useState(() => DS_TUNE.map(() => 0)), [cur, setCur] = useState(-1), tms = useRef([]);
  useEffect(() => () => tms.current.forEach(clearTimeout), []);
  const notes = DS_TUNE.map(([k, d], i) => ({ d: ACP_D[k], acc: acc[i], dur: d }));
  const flip = (i) => { const nx = acc[i] === 0 ? 1 : acc[i] === 1 ? -1 : 0; const a = acc.slice(); a[i] = nx; setAcc(a); playKey(ivMidi({ d: notes[i].d, acc: nx }) - 60, 0.45); };
  const play = () => { tms.current.forEach(clearTimeout); tms.current = playMelody(notes, 100, setCur) || []; tms.current.push(setTimeout(() => setCur(-1), (0.1 + 16.5 * 0.6) * 1000)); };
  const changed = acc.filter(Boolean).length;
  return (
    <div className="try-box" style={actBox} data-acp="pad">
      <div style={actTitle}>{t('Add a sharp or a flat', '샵이나 플랫 붙이기')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>“환희의 송가” 첫 줄이에요. 아래 음 이름을 누를 때마다 <b>♯ → ♭ → 제자리</b>로 바뀌어요. 임시표 하나가 선율의 색깔을 어떻게 바꾸는지 들어 봐요.</> : <>The first line of Ode to Joy. Tap a note name below to make it <b>♯, then ♭, then natural</b> again. Hear how one accidental changes the colour of the tune.</>}</div>
      <div style={{background:'#fff',borderRadius:8,margin:'4px 0'}}><MelodyStaff notes={notes} on={cur} width={340}/></div>
      <div style={{display:'flex',gap:4,justifyContent:'center',flexWrap:'wrap',margin:'6px 0'}}>{notes.map((x, i) => <button key={i} type="button" onClick={() => flip(i)} style={{minWidth:36,padding:'6px 4px',borderRadius:10,cursor:'pointer',fontSize:14,fontWeight:900,background:cur === i ? BK.coral : x.acc ? '#fbe3da' : '#fff',color:cur === i ? '#fff' : BK.ink,border:'2px solid ' + (cur === i ? BK.coral : BK.ink)}}>{ivName(x)}</button>)}</div>
      <div style={{textAlign:'center',fontSize:14,fontWeight:900,minHeight:20,color:changed ? BK.coral : BK.muted}}>{changed ? t(changed + (changed === 1 ? ' note changed' : ' notes changed'), changed + '개 음이 바뀌었어요') : t('No accidentals yet', '아직 임시표가 없어요')}</div>
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        <button className="ghost-btn" style={spBtn} onClick={play}>{t('▶ Play', '▶ 듣기')}</button>
        <button className="ghost-btn" style={spBtn} onClick={() => setAcc(DS_TUNE.map(([k]) => (k === 4 ? -1 : 0)))}>{t('Every E flat', 'E를 모두 E♭으로')}</button>
        <button className="ghost-btn" style={spBtn} disabled={!changed} onClick={() => setAcc(DS_TUNE.map(() => 0))}>{t('All natural', '모두 제자리')}</button>
      </div>
    </div>
  );
}

// one tune, four styles: Twinkle (TD_TUNE) over a band, a chord every two beats
const SB_CH = ['C', 'C', 'F', 'C', 'F', 'C', 'G', 'C'];
const SB_TRI = { C: [48, 52, 55], F: [53, 57, 60], G: [43, 47, 50] }, SB_7 = { C: [52, 55, 59], F: [57, 60, 64], G: [53, 59, 62] };   // the jazz chords: C E G B, F A C E, G B D F (the root in the bass)
const SB_STY = {
  baroque: { inst: 'harpsichord', name: ['Baroque', '바로크'], say: ['A harpsichord, and a bass that keeps moving.', '하프시코드, 쉬지 않고 움직이는 베이스.'] },
  classical: { inst: 'piano', name: ['Classical', '고전'], say: ['A clear tune over an Alberti bass: low, high, middle, high.', '알베르티 베이스(낮은, 높은, 가운데, 높은 음) 위의 또렷한 선율.'] },
  jazz: { inst: 'piano', name: ['Jazz', '재즈'], say: ['Swing, a walking bass and 7th chords.', '스윙, 걷는 베이스, 7화음.'] },
  pop: { inst: 'piano', name: ['Pop', '팝'], say: ['A steady chord on every beat over the bass.', '베이스 위에 박마다 고른 화음.'] },
};
const SB_BASS = { C: 48, F: 41, G: 43 };   // C3, F2, G2
const sbBand = (sty) => { const ev = [];
  SB_CH.forEach((c, h) => { const b = h * 2, [r, th, fi] = SB_TRI[c], B = SB_BASS[c];
    if (sty === 'classical') [r, fi, th, fi].forEach((m, k) => ev.push([b + k * 0.5, m, 0.48, 0.3]));
    else if (sty === 'baroque') [B, B + 7, B + 12, B + 7].forEach((m, k) => ev.push([b + k * 0.5, m, 0.45, 0.38]));
    else if (sty === 'jazz') { [B, B + 4].forEach((m, k) => ev.push([b + k, m, 0.9, 0.42])); SB_7[c].forEach(m => ev.push([b + 1, m, 0.5, 0.22])); }
    else { ev.push([b, B, 1.8, 0.45]); [0, 1].forEach(k => [r, th, fi].forEach(m => ev.push([b + k, m, 0.85, k ? 0.2 : 0.28]))); } });
  return ev; };
function StyleBand() {
  const [sty, setSty] = useState('classical'), [tune, setTune] = useState(true), [cur, setCur] = useState(-1), [on, setOn] = useState(false), tms = useRef([]);
  const stop = () => { tms.current.forEach(clearTimeout); tms.current = []; stopClicks(); setOn(false); setCur(-1); };
  useEffect(() => () => { tms.current.forEach(clearTimeout); stopClicks(); }, []);
  const play = () => { stop(); const ctx = getAudio(); if (!ctx) return; const S = SB_STY[sty], bpm = sty === 'jazz' ? 108 : 96, spb = 60 / bpm, t0 = ctx.currentTime + 0.12;
    const sw = (b) => (sty === 'jazz' && Math.abs(b % 1 - 0.5) < 1e-6 ? b + 1 / 6 : b);
    sbBand(sty).forEach(([b, m, d, v]) => instNote(S.inst, ctx, t0 + sw(b) * spb, m, d * spb, v));
    let b = 0; TD_TUNE.forEach(([k, d], i) => { if (tune) instNote(S.inst, ctx, t0 + b * spb, 60 + k, d * spb * 0.92, 0.62); const at = b; tms.current.push(setTimeout(() => setCur(i), (0.12 + at * spb) * 1000)); b += d; });
    instNote(S.inst, ctx, t0 + 16 * spb, 48, 2 * spb, 0.4); if (tune) instNote(S.inst, ctx, t0 + 16 * spb, 60, 2 * spb, 0.5);
    tms.current.push(setTimeout(() => { setOn(false); setCur(-1); }, (0.12 + 18 * spb) * 1000)); setOn(true); };
  const tap = (k) => { playKey(k, 0.45); };
  const kl = {}; [0, 2, 4, 5, 7, 9].forEach(k => { kl[k] = 'pale'; }); if (cur >= 0 && !tune) kl[TD_TUNE[cur][0]] = 'cor';
  return (
    <div className="try-box" style={actBox} data-sb="pad">
      <div style={actTitle}>{t('One tune, four styles', '한 선율, 네 스타일')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>“반짝반짝 작은 별”을 네 가지 밴드 위에서 들어요. 그다음 <b>선율 끄기</b>를 누르고, 밴드에 맞춰 내가 선율을 쳐 봐요(켜진 건반이 칠 음을 알려 줘요).</> : <>Hear Twinkle over four different bands. Then switch <b>the tune off</b> and play it yourself with the band (the lit key shows the note to play).</>}</div>
      {spChips(Object.keys(SB_STY).map(x => [x, t(SB_STY[x].name[0], SB_STY[x].name[1])]), sty, (x) => { stop(); setSty(x); })}
      <div style={{textAlign:'center',fontSize:13.5,fontWeight:800,color:BK.muted,margin:'4px 0',minHeight:20}}>{t(SB_STY[sty].say[0], SB_STY[sty].say[1])}</div>
      <div style={{display:'flex',gap:4,justifyContent:'center',flexWrap:'wrap',margin:'6px 0'}}>{TD_TUNE.map(([k, d], i) => <span key={i} style={{width:d * 18 + (d - 1) * 4,height:18,borderRadius:9,background:cur === i ? BK.coral : '#fff',border:'2px solid ' + (cur === i ? BK.coral : BK.ink)}}/>)}</div>
      {!tune && <div style={{margin:'6px 0 4px'}}><SpKb lo={0} hi={9} W={34} H={88} lit={kl} names={{ 0: 'C', 2: 'D', 4: 'E', 5: 'F', 7: 'G', 9: 'A' }} onTap={tap} label={t('Play the tune', '선율 치기')}/></div>}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        {on ? <button className="ghost-btn" style={spBtn} onClick={stop}>{t('■ Stop', '■ 멈추기')}</button> : <button className="ghost-btn" style={spBtn} onClick={play}>{t('▶ Play', '▶ 듣기')}</button>}
        <button className="ghost-btn" style={spBtn} onClick={() => { stop(); setTune(!tune); }}>{tune ? t('Tune off: I play it', '선율 끄기: 내가 쳐요') : t('Tune on', '선율 켜기')}</button>
      </div>
    </div>
  );
}
'''
rep("// ══ Build BH: Blues jam ══", CODE + "\n// ══ Build BH: Blues jam ══")

# Transpose a tune: My tune, played on C D E F G
rep("function Transposer() {\n  const TKEYS = ['C', 'G', 'F', 'D', 'Bb', 'A', 'Eb'];\n  const [tid, setTid] = useState('a');",
    "function Transposer() {\n  const TKEYS = ['C', 'G', 'F', 'D', 'Bb', 'A', 'Eb'];\n  const [tid, setTid] = useState('a'), [mine, setMine] = useState([]);   // Build BK: My tune, up to eight notes on C D E F G")
rep("  const tune = TR_TUNES.find(x => x.id === tid);", "  const tune = tid === 'mine' ? { id: 'mine', degs: mine.length ? mine : [[0, 1]] } : TR_TUNES.find(x => x.id === tid);")

rep("onClick={() => { setTid(tt.id); setShow(false); }}>{tt.title}</button>)}</div>",
    "onClick={() => { setTid(tt.id); setShow(false); }}>{tt.title}</button>)}<button className={'chip' + (tid === 'mine' ? ' active' : '')} style={{padding:'3px 9px',fontSize:13}} onClick={() => { setTid('mine'); setShow(false); }}>{t('My tune', '내 선율')}</button></div>\n"
    "      {tid === 'mine' && <div data-tr=\"mine\" style={{margin:'2px 0 6px'}}><div style={{fontSize:12.5,fontWeight:800,color:BK.muted,textAlign:'center'}}>{t('Play up to eight notes on C D E F G: they become the tune in C.', 'C D E F G로 여덟 음까지 쳐요: C장조 선율이 돼요.')}</div>"
    "<SpKb lo={0} hi={7} W={34} H={80} lit={{ 0: 'pale', 2: 'pale', 4: 'pale', 5: 'pale', 7: 'pale' }} names={{ 0: 'C', 2: 'D', 4: 'E', 5: 'F', 7: 'G' }} onTap={(k) => { const g = { 0: 0, 2: 1, 4: 2, 5: 3, 7: 4 }[k]; if (g == null) return; playKey(k, 0.4); setShow(false); setMine(m => (m.length >= 8 ? m : [...m, [g, 1]])); }} label={t('My tune', '내 선율')}/>"
    "<div style={{textAlign:'center',marginTop:4}}><button className=\"ghost-btn\" disabled={!mine.length} onClick={() => { setMine([]); setShow(false); }}>{t('Clear', '지우기')}</button></div></div>}")
rep("  { id: 'csx-jam', ch: 'styles', title: 'Blues jam',",
    "  { id: 'mk-iv', ch: 'intervals', title: 'A tune from one interval', blurb: 'Pick a 2nd, 3rd, 4th, 5th or octave and hop only by it.', C: () => <IntervalTune/> },   // Build BK\n"
    "  { id: 'mk-acc', ch: 'accidentals', title: 'Add a sharp or a flat', blurb: 'Tap any note of Ode to Joy to sharpen or flatten it, and hear it.', C: () => <AccPlay/> },\n"
    "  { id: 'mk-sty', ch: 'styles', title: 'One tune, four styles', blurb: 'Twinkle over a Baroque, Classical, jazz or pop band; then play it yourself.', C: () => <StyleBand/> },\n"
    "  { id: 'csx-jam', ch: 'styles', title: 'Blues jam',")
rep("  'csx-jam': ['블루스 잼',", "  'mk-iv': ['음정 하나로 선율 만들기', '2도, 3도, 4도, 5도, 옥타브 중 하나를 골라 그 음정으로만 움직여요.'],\n  'mk-acc': ['샵이나 플랫 붙이기', '환희의 송가의 아무 음이나 올리고 내려서 들어 봐요.'],\n  'mk-sty': ['한 선율, 네 스타일', '반짝반짝 작은 별을 바로크, 고전, 재즈, 팝 밴드 위에서. 그다음 내가 쳐요.'],\n  'csx-jam': ['블루스 잼',")
rep("'csx-jam': ['about', 0, 3, 'show ear game'],", "'csx-jam': ['about', 0, 3, 'show ear game'], 'mk-iv': ['intervals', 1, 2, 'game ear'], 'mk-acc': ['clock', 1, 2, 'game ear'], 'mk-sty': ['about', 0, 3, 'show ear game'],")
rep("'csx-jam': 'about'", "'csx-jam': 'about', 'mk-iv': 'p-intervals', 'mk-acc': 'p-clock', 'mk-sty': 'about'")
rep("  'csx-jam': () => (\n",
    "  'mk-iv': () => (\n    <svg width=\"34\" height=\"34\" viewBox=\"0 0 24 24\"><rect width=\"24\" height=\"24\" rx=\"6\" fill=\"#3f9a7e\"/><path d=\"M4 18 L9 13 L14 18 L19 8\" fill=\"none\" stroke=\"#fefbf3\" strokeWidth=\"2\" strokeLinejoin=\"round\"/><circle cx=\"19\" cy=\"8\" r=\"2.2\" fill=\"#e9a83a\"/></svg>\n  ),\n"
    "  'mk-acc': () => (\n    <svg width=\"34\" height=\"34\" viewBox=\"0 0 24 24\"><rect width=\"24\" height=\"24\" rx=\"6\" fill=\"#b85068\"/><text x=\"12\" y=\"17\" textAnchor=\"middle\" fontSize=\"15\" fontWeight=\"900\" fill=\"#fefbf3\">♯</text></svg>\n  ),\n"
    "  'mk-sty': () => (\n    <svg width=\"34\" height=\"34\" viewBox=\"0 0 24 24\"><rect width=\"24\" height=\"24\" rx=\"6\" fill=\"#3b4fa8\"/>{[0, 1, 2, 3].map(i => <rect key={i} x={3 + (i % 2) * 9.5} y={3 + Math.floor(i / 2) * 9.5} width=\"8\" height=\"8\" rx=\"2\" fill={i === 1 ? '#e9a83a' : '#fefbf3'}/>)}</svg>\n  ),\n"
    "  'csx-jam': () => (\n")
rep("'csx-blues', 'csx-jam', 'csx-pop', 'csx-ear'],", "'csx-blues', 'csx-jam', 'csx-pop', 'mk-sty', 'csx-ear'],")
rep("lessons: ['iv-count', 'iv-staff'], check: 'intervals', level: 1 }", "lessons: ['iv-count', 'iv-staff', 'mk-iv'], check: 'intervals', level: 1 }")
rep("lessons: ['ac-natural', 'ac-bar', 'ac-play', 'ac-cmp'], check: 'accidentals' }", "lessons: ['ac-natural', 'ac-bar', 'ac-play', 'ac-cmp', 'mk-acc'], check: 'accidentals' }")

open(dst, 'w', encoding='utf-8').write(s)
print('ok')
