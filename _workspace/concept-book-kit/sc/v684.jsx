
// ─── Build V (her 2026-10-25 23:10: 'the animation where the King and the Queen are taken home -- put it here'): the staff
// chapter's clef pictures (the clef = its chess piece) come alive on screen. The piece leaves its place beside the '=', steps onto
// its line and goes home: the Queen along the second line and round the curl into its centre, on G; the King along the fourth line,
// between his two guards (the dots), into the clef, on F. The line lights, its note sounds, its letter shows. Print keeps the still.
function SfClefHome({ clef }) {
  const queen = clef === 'treble', line = queen ? 32 : 24, L = queen ? 'G' : 'F';
  const piece = useMemo(() => { const s = penSvg(queen ? sfQueen(26, 31, 1.2) : sfKing(26, 31, 1.2), { vb: [0, 0, 52, 58] }); return s.slice(s.indexOf('>') + 1, s.lastIndexOf('</svg>')); }, [queen]);
  const [u, setU] = useState(-1), raf = useRef(null), snd = useRef(null);
  useEffect(() => () => { cancelAnimationFrame(raf.current); clearTimeout(snd.current); }, []);
  const reduce = (() => { try { return window.matchMedia('(prefers-reduced-motion: reduce)').matches; } catch (e) { return false; } })();
  const go = () => { cancelAnimationFrame(raf.current); clearTimeout(snd.current);
    const dur = reduce ? 1 : 4400, t0 = performance.now(), step = (now) => { const v = Math.min(1, (now - t0) / dur); setU(v); if (v < 1) raf.current = requestAnimationFrame(step); };
    raf.current = requestAnimationFrame(step); snd.current = setTimeout(() => playKey(dMidiKey(line), 0.9), dur * 0.8); };
  const ease = (x) => (x < 0.5 ? 2 * x * x : 1 - Math.pow(-2 * x + 2, 2) / 2), seg = (a, b) => Math.max(0, Math.min(1, (u - a) / (b - a)));
  const W = 250, X1 = 150, ly = dY(line), HOME = queen ? { x: 21, y: 89.6 } : { x: 21, y: 129.5 }, START = { x: 214, y: ly - 4, k: 0.92 }, ENTRY = { x: X1 - 6, y: ly, k: 0.42 };
  let p = START, phase = 'rest';
  if (u >= 0) {
    const a = ease(seg(0, 0.15));
    p = { x: START.x + (ENTRY.x - START.x) * a, y: START.y + (ENTRY.y - START.y) * a, k: START.k + (ENTRY.k - START.k) * a }; phase = 'step';
    if (u >= 0.15) {
      if (queen) {
        if (u < 0.45) { const b = ease(seg(0.15, 0.45)); p = { x: ENTRY.x + (HOME.x + 15 - ENTRY.x) * b, y: ly, k: 0.42 }; phase = 'line'; }
        else { const c = ease(seg(0.45, 0.8)), r = 15 * (1 - c), ang = c * 4 * Math.PI; p = { x: HOME.x + r * Math.cos(ang), y: HOME.y + r * Math.sin(ang), k: 0.42 - 0.12 * c }; phase = 'curl'; }
      } else { const b = ease(seg(0.15, 0.8)); p = { x: ENTRY.x + (HOME.x - ENTRY.x) * b, y: HOME.y, k: 0.42 - 0.1 * b }; phase = p.x < 46 ? 'guards' : 'line'; }
    }
    if (u >= 0.8) phase = 'home';
  }
  const home = phase === 'home', eqOp = u < 0 ? 1 : 1 - seg(0, 0.1);
  const cap = { rest: '', step: t('Off to the staff…', '오선으로 가요…'), line: queen ? t('Along the second line…', '둘째 줄을 따라가요…') : t('Walking along the fourth line…', '넷째 줄을 따라 걸어가요…'),
    curl: t('Following the swirl…', '소용돌이를 따라가요…'), guards: t('Past the two guards…', '두 경비병을 지나서…'),
    home: queen ? t('Home: the Queen sits on G, the second line.', '집에 왔어요: 여왕은 둘째 줄, G에 앉아요.') : t('Home: the King sits on F, the fourth line, between his guards.', '집에 왔어요: 왕은 경비병 사이, 넷째 줄 F에 앉아요.') }[phase];
  return <div>
    <div style={{maxWidth:380,margin:'0 auto'}}>
      <SfStaff clef={clef} width={W} span={[4, X1]} pad={[18, 18]} label={queen ? t('The treble clef and the Queen: tap the button to take her home to her line, G', '높은음자리표와 여왕: 버튼을 누르면 여왕을 자기 줄 G로 데려다줘요') : t('The bass clef and the King: tap the button to take him home to his line, F', '낮은음자리표와 왕: 버튼을 누르면 왕을 자기 줄 F로 데려다줘요')}
        extra={(yOf, layer, txt) => layer === 'under'
          ? <line x1="4" x2={X1} y1={yOf(line)} y2={yOf(line)} stroke={BK.coral} strokeOpacity={home ? 0.9 : 0.55} strokeWidth={home ? 4.2 : 3.4} style={{transition:'stroke-opacity .3s, stroke-width .3s'}}/>
          : <g>
            <text x={X1 - 14} y={yOf(line) + 4.5} fontSize="14" fontWeight="900" fill={BK.coral} textAnchor="middle" style={txt} opacity={u < 0 || home ? 1 : 0.25}>{L}</text>
            <text x="178" y={yOf(line) + 2} fontSize="30" fontWeight="900" fill={BK.ink} textAnchor="middle" dominantBaseline="middle" opacity={eqOp}>=</text>
            {!queen && phase === 'guards' && [125, 134].map(y => <circle key={y} cx="34.2" cy={y} r="3.4" fill="none" stroke={BK.coral} strokeWidth="0.9"/>)}
            {u >= 0.74 && <circle cx={HOME.x} cy={HOME.y} r="10.5" fill="#fbe3da" fillOpacity="0.92" stroke={BK.coral} strokeWidth="1" opacity={seg(0.74, 0.84)}/>}
            <g transform={`translate(${(p.x - 26 * p.k).toFixed(2)} ${(p.y - 31 * p.k).toFixed(2)}) scale(${p.k.toFixed(3)})`} dangerouslySetInnerHTML={{__html: piece}}/>
          </g>}/>
    </div>
    <div style={{textAlign:'center',fontSize:13.5,fontWeight:700,color:home ? BK.coral : '#6d6f9c',minHeight:20,marginTop:2}}>{cap}</div>
    <div style={{textAlign:'center',marginTop:4}}>
      <button className="ghost-btn" style={{fontSize:14,padding:'8px 16px',minHeight:44}} onClick={go}>{queen ? t('Take the Queen home', '여왕을 집으로 데려다줘요') : t('Take the King home', '왕을 집으로 데려다줘요')}</button>
    </div>
  </div>;
}
// ─── Build V (her 23:15: 'I can't tell which room is rhythm and which is pitch; a selector that shows just the rhythm rooms'):
// the house's topic chips. All shows the house as it is; a topic keeps its rooms clear and pales the rest, on every floor.
const thArea = (id) => { if (id === 'listen-sing') return 'aural'; const c = catOfChapter(id); return c ? c.area : CHAPTER_CAT[id] === 'about' ? 'beside' : null; };
const HOUSE_TOPIC_KEY = 'pb_house_topic_v1';
function HouseTopics({ value, onChange }) {
  const ids = pathIds(), have = new Set(ids.map(thArea));
  const opts = [[null, t('All', '전체')]].concat(TOOL_AREAS.filter(a => have.has(a.id)).map(a => [a.id, a.name]), have.has('aural') ? [['aural', t('Aural', '청음')]] : []);
  return <div role="group" aria-label={t('Show the rooms of one topic', '한 주제의 방만 보기')} style={{display:'flex',gap:6,flexWrap:'wrap',justifyContent:'center',margin:'6px auto 10px',maxWidth:560}}>
    {opts.map(([id, nm]) => { const on = value === id, n = id ? ids.filter(x => thArea(x) === id).length : ids.length;
      return <button key={id || 'all'} className={'chip' + (on ? ' active' : '')} aria-pressed={on} style={{minHeight:40,padding:'6px 12px',fontSize:13.5}} onClick={() => onChange(id)}>{nm} <span style={{opacity:0.6,fontWeight:700,marginLeft:2}}>{n}</span></button>; })}
  </div>;
}
