import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)

# Build CK (call 25, batch 9; her 09:56: fun first): the three Stories rooms' things to make.
#   The piano: Make a surprise! (a quiet tune with one sudden loud chord, as in Haydn's Surprise Symphony (the app's own
#     composer card); on the piano it surprises, on the harpsichord it cannot)
#   Instruments: Who can play my note? (move one note across the 88 keys; the instruments and voices that reach it light up,
#     from the app's range chart)
#   Composers: Who came first? (a chain of the room's composers: born earlier, later, or the same year? or: alive at the
#     same time? a streak to beat)

CODE = r'''
// ══ Build CK: batch 9, the three Stories rooms' things to make (call 25; her 09:56: fun first) ══
// ── The piano: Make a surprise! The harpsichord plucks every note the same; the piano plays as you press (sps-softloud) ──
const SU_STARS = [['piano', 'Surprise someone on the piano', '피아노로 깜짝 놀래기'], ['harp', 'Try it on the harpsichord', '하프시코드로 해 보기'], ['wait', 'Make them wait: the surprise near the end', '기다리게 하기: 끝 가까이에 깜짝']];
function SurpriseTune() {
  const T = useSpTimers();
  const [tune, setTune] = useState([0, 2, 4, 5, 7, 5, 4, 2]), [bang, setBang] = useState(6), [inst, setInst] = useState('piano'), [on, setOn] = useState(-1), [last, setLast] = useState(null);
  const [stars, setStars] = useState(() => { try { return JSON.parse(localStorage.getItem('pb_mk_surprise')) || {}; } catch (e) { return {}; } });
  const play = () => { T.clear(); const bpm = 84, ev = [];
    tune.forEach((s, j) => { if (j === bang) [36, 48, 52, 55, 60 + s, 72].forEach(m => ev.push([j, m, 1.6, 1])); else ev.push([j, 60 + s, 0.9, 0.12]); });
    playEvents(inst, ev, bpm); tune.forEach((_, j) => T.at(100 + j * 60000 / bpm, () => setOn(j))); T.at(100 + (tune.length + 1) * 60000 / bpm, () => setOn(-1)); setLast(inst);
    const n = { ...stars }; if (inst === 'piano') n.piano = 1; else n.harp = 1; if (inst === 'piano' && bang >= tune.length - 2 && tune.length >= 6) n.wait = 1;
    if (Object.keys(n).length !== Object.keys(stars).length) { setStars(n); try { localStorage.setItem('pb_mk_surprise', JSON.stringify(n)); } catch (e) {} } };
  const add = (s) => { if (tune.length >= 10) return; T.clear(); setOn(-1); setTune(tune.concat([s])); playKey(s, 0.4); };
  const back = () => { T.clear(); setOn(-1); const nt = tune.slice(0, -1); setTune(nt); if (bang >= nt.length) setBang(Math.max(0, nt.length - 1)); };
  return (
    <div className="try-box" style={actBox} data-mk="surprise">
      <div style={actTitle}>{t('Make a surprise!', '깜짝 놀래기!')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>조용한 선율 속에 <b>쾅!</b> 하는 큰 화음을 하나 숨겨요. 하이든은 “놀람” 교향곡에서 조용한 선율을 갑자기 엄청 큰 화음으로 끊었어요. 피아노로, 그리고 하프시코드로 들어 봐요. 누가 더 놀래킬까요?</> : <>Hide one huge <b>BANG!</b> chord inside a quiet tune. In his “Surprise” Symphony, Haydn suddenly interrupts a quiet tune with a huge, loud chord. Try yours on the piano, then on the harpsichord. Which one can surprise anyone?</>}</div>
      <div style={{display:'flex',gap:'4px 12px',justifyContent:'center',flexWrap:'wrap',margin:'0 0 6px'}}>{SU_STARS.map(([id, en, ko]) => <span key={id} style={{fontSize:12.5,fontWeight:800,color:stars[id] ? BK.coral : BK.muted}}>{stars[id] ? '★' : '☆'} {t(en, ko)}</span>)}</div>
      <div style={{display:'flex',gap:5,justifyContent:'center',flexWrap:'wrap',margin:'6px 0',minHeight:52,alignItems:'flex-end'}}>{tune.map((s, j) => { const b = j === bang, cur = j === on;
        return <button key={j} onClick={() => { T.clear(); setOn(-1); setBang(j); }} style={{width:b ? 46 : 32,height:b ? 46 : 32,borderRadius:b ? 12 : 16,border:'2px solid ' + (b ? BK.coral : BK.ink),background:cur ? (b ? BK.coral : BK.ink) : b ? '#fbe3da' : '#fff',color:cur ? '#fff' : b ? BK.coral : BK.ink,fontWeight:900,fontSize:b ? 13 : 14,cursor:'pointer',fontFamily:'inherit',padding:0,transform:cur && b ? 'scale(1.25)' : 'none',transition:'transform 0.12s'}}>{b ? t('BANG', '쾅') : 'CDEFG'[[0, 2, 4, 5, 7].indexOf(s)]}</button>; })}</div>
      <div style={{fontSize:11.5,fontWeight:800,color:BK.muted,textAlign:'center'}}>{t('Tap a note to make it the BANG.', '음을 누르면 그 자리가 쾅이 돼요.')}</div>
      <div style={{display:'grid',gridTemplateColumns:'repeat(5,minmax(0,1fr))',gap:6,maxWidth:360,margin:'6px auto 0'}}>{[0, 2, 4, 5, 7].map((s, i) => <button key={s} className="choice-btn" disabled={tune.length >= 10} onClick={() => add(s)} style={{padding:'10px 0',fontSize:17,fontWeight:900,minWidth:0}}>{'CDEFG'[i]}</button>)}</div>
      {spChips([['piano', t('Piano', '피아노')], ['harpsichord', t('Harpsichord', '하프시코드')]], inst, (x) => { T.clear(); setOn(-1); setInst(x); setLast(null); })}
      {spMsg(last === 'piano' ? t('BANG! The piano plays as soft or as loud as you press: piano and forte.', '쾅! 피아노는 누르는 만큼 여리게도 세게도: 피아노와 포르테.') : last === 'harpsichord' ? t('No surprise: the harpsichord plucks every note at the same loudness, however hard you press.', '놀랍지 않아요: 하프시코드는 아무리 세게 눌러도 모든 음을 같은 세기로 뜯어요.') : t('The tune is soft; the BANG is as loud as can be.', '선율은 여리게, 쾅은 있는 힘껏.'), last === 'piano' ? BK.green : last ? BK.coral : undefined)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        <button className="primary-btn" style={spBtn} disabled={!tune.length} onClick={play}>{t('▶ Play it', '▶ 들어 보기')}</button>
        {tune.length > 0 && <button className="ghost-btn" style={spBtn} onClick={back}>{t('⌫ Back', '⌫ 지우기')}</button>}
      </div>
    </div>
  );
}

// ── Instruments: Who can play my note? One note across the piano's 88 keys; the range chart's instruments and voices
// (ALL_RANGES, not the history rows) that reach it light up ──
const WC_LIST = ALL_RANGES.filter(r => !r.hist);
const WC_FAM = RANGES.filter(g => !g.hist).map(g => g.g);
const wcName = (m) => lwLet(((m % 12) + 12) % 12) + (Math.floor(m / 12) - 1);
const wcCan = (m) => WC_LIST.filter(r => m >= r.lo && m <= r.hi);
const WC_STARS = [['only', 'A note only the piano can play', '피아노만 낼 수 있는 음'], ['choir', 'A note all four voices can sing', '네 목소리가 모두 부를 수 있는 음'], ['two', 'A note only two can play', '둘만 낼 수 있는 음']];
function WhoCanPlay() {
  const [m, setM] = useState(60);
  const [stars, setStars] = useState(() => { try { return JSON.parse(localStorage.getItem('pb_mk_who')) || {}; } catch (e) { return {}; } });
  const can = wcCan(m), names = new Set(can.map(r => r.name)), voices = ['Soprano', 'Alto', 'Tenor', 'Bass'].every(v => names.has(v));
  const go = (x) => { const n = Math.max(21, Math.min(108, x)); setM(n); playKey(n - 60, 0.6); const c = wcCan(n), nm2 = new Set(c.map(r => r.name)), s2 = { ...stars };
    if (c.length === 1 && nm2.has('Piano (today, 88 keys)')) s2.only = 1; if (['Soprano', 'Alto', 'Tenor', 'Bass'].every(v => nm2.has(v))) s2.choir = 1; if (c.length === 2) s2.two = 1;
    if (Object.keys(s2).length !== Object.keys(stars).length) { setStars(s2); try { localStorage.setItem('pb_mk_who', JSON.stringify(s2)); } catch (e) {} } };
  const s = m - 60;
  return (
    <div className="try-box" style={actBox} data-mk="who">
      <div style={actTitle}>{t('Who can play my note?', '내 음을 누가 낼 수 있을까?')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>피아노의 88건반 위로 음 하나를 옮겨요. 그 음을 낼 수 있는 악기와 목소리에 불이 켜져요. 아주 낮게, 아주 높게 가 보세요: 누가 남을까요?</> : <>Move one note across the piano's 88 keys. The instruments and voices that can play it light up. Go very low, then very high: who is left?</>}</div>
      <div style={{display:'flex',gap:'4px 12px',justifyContent:'center',flexWrap:'wrap',margin:'0 0 6px'}}>{WC_STARS.map(([id, en, ko]) => <span key={id} style={{fontSize:12.5,fontWeight:800,color:stars[id] ? BK.coral : BK.muted}}>{stars[id] ? '★' : '☆'} {t(en, ko)}</span>)}</div>
      <div style={{textAlign:'center',fontFamily:LB_SERIF,fontSize:30,fontWeight:900,color:BK.ink,fontVariantNumeric:'lining-nums'}}>{wcName(m)}{m === 60 ? <span style={{fontSize:14,color:BK.coral,fontFamily:'inherit'}}> {t('middle C', '가운데 도')}</span> : null}</div>
      <SpKb lo={s - 6} hi={s + 6} W={24} H={64} lit={{ [s]: 'cor' }} names={{ [s]: lwLet(((m % 12) + 12) % 12) }} onTap={(k) => go(k + 60)} label={t('Tap a key, or jump', '건반을 누르거나 뛰어요')}/>
      <div style={{display:'flex',gap:6,justifyContent:'center',flexWrap:'wrap',margin:'6px 0'}}>
        {[[-12, t('◀◀ octave', '◀◀ 옥타브')], [-1, '◀'], [1, '▶'], [12, t('octave ▶▶', '옥타브 ▶▶')]].map(([d, lab]) => <button key={d} className="ghost-btn" style={{...spBtn, minWidth:0, padding:'6px 12px'}} disabled={m + d < 21 || m + d > 108} onClick={() => go(m + d)}>{lab}</button>)}
        <button className="ghost-btn" style={{...spBtn, minWidth:0, padding:'6px 12px'}} onClick={() => go(21)}>{t('Lowest A', '가장 낮은 A')}</button><button className="ghost-btn" style={{...spBtn, minWidth:0, padding:'6px 12px'}} onClick={() => go(108)}>{t('Top C', '가장 높은 C')}</button>
      </div>
      <div style={{textAlign:'center',fontSize:15,fontWeight:900,color:BK.ink,margin:'2px 0 6px'}}>{t(can.length + ' of ' + WC_LIST.length + ' can play it', WC_LIST.length + '개 중 ' + can.length + '개가 낼 수 있어요')}</div>
      <div style={{display:'flex',flexDirection:'column',gap:6}}>{WC_FAM.map(fam => <div key={fam}>
        <div style={{fontSize:11,fontWeight:900,color:BK.muted,letterSpacing:'0.04em',marginBottom:3}}>{rangeName(fam)}</div>
        <div style={{display:'flex',flexWrap:'wrap',gap:4}}>{WC_LIST.filter(r => r.g === fam).map(r => { const ok = names.has(r.name);
          return <span key={r.name} style={{fontSize:12,fontWeight:800,padding:'4px 9px',borderRadius:14,border:'1.5px solid ' + (ok ? BK.ink : BK.line),background:ok ? BK.ink : 'transparent',color:ok ? '#fff' : BK.muted,opacity:ok ? 1 : 0.55}}>{kqRangeName(r.name)}</span>; })}</div></div>)}</div>
      {spMsg(can.length === 1 ? t('Only the piano reaches this one!', '이 음은 피아노만 닿아요!') : voices ? t('All four voices can sing this one.', '네 목소리가 모두 부를 수 있어요.') : can.length === 2 ? t('Only two: ' + can.map(r => kqRangeName(r.name)).join(' and ') + '.', '둘뿐이에요: ' + can.map(r => kqRangeName(r.name)).join(', ') + '.') : t('Keep moving: find the stars.', '계속 옮겨 봐요: 별을 찾아요.'), can.length <= 2 || voices ? BK.green : undefined)}
    </div>
  );
}

// ── Composers: Who came first? A chain of the room's composers (CPX_IDS, years from CMP): born earlier, later, or the
// same year? Or: alive at the same time? (pairs where one died the year the other was born are left out) ──
const WF_POOL = () => CMP.filter(c => CPX_IDS.includes(c.id));
const wfEnd = (c) => c.died || MTL_NOW;
const wfYrs = (c) => c.born + '–' + (c.died ? c.died : t('today', '오늘날'));
const WF_STARS = [['five', '5 in a row', '5연속'], ['ten', '10 in a row', '10연속'], ['trio', 'Find a pair born the same year', '같은 해에 태어난 둘 찾기']];
function WhoFirst() {
  const pool = WF_POOL();
  const nextB = (a, mode) => { let b, g = 0; do { b = pick(pool); } while ((b.id === a.id || (mode === 'alive' && (b.born === a.died || a.born === b.died))) && g++ < 40); return b; };
  const [mode, setMode] = useState('born'), [P, setP] = useState(() => { const a0 = pick(pool); return { a: a0, b: nextB(a0, 'born') }; }), [res, setRes] = useState(null), [run, setRun] = useState(0);
  const a = P.a, B = P.b;
  const [st, setSt] = useState(() => { try { return JSON.parse(localStorage.getItem('pb_mk_first')) || {}; } catch (e) { return {}; } });
  const truth = mode === 'born' ? (B.born < a.born ? 'earlier' : B.born > a.born ? 'later' : 'same') : (a.born <= wfEnd(B) && B.born <= wfEnd(a) ? 'yes' : 'no');
  const save = (n) => { setSt(n); try { localStorage.setItem('pb_mk_first', JSON.stringify(n)); } catch (e) {} };
  const answer = (x) => { if (res) return; const ok = x === truth, r = ok ? run + 1 : 0; setRes({ x, ok }); setRun(r);
    const n = { ...st }; if (r > (n.best || 0)) n.best = r; if (r >= 5) n.five = 1; if (r >= 10) n.ten = 1; if (ok && truth === 'same') n.trio = 1; save(n); };
  const next = () => { setP({ a: B, b: nextB(B, mode) }); setRes(null); };
  const card = (c, show) => <div style={{flex:1,minWidth:0,border:'2px solid ' + BK.ink,borderRadius:12,padding:'8px 6px',textAlign:'center',background:'#fff'}}>
    <div style={{fontFamily:LB_SERIF,fontSize:17,fontWeight:900,color:BK.ink,lineHeight:1.15}}>{t(c.name[0], c.name[1])}</div>
    <div style={{fontSize:14,fontWeight:900,color:show ? BK.coral : BK.muted,marginTop:4,fontVariantNumeric:'lining-nums'}}>{show ? wfYrs(c) : '? – ?'}</div></div>;
  const opts = mode === 'born' ? [['earlier', t('Born earlier', '더 먼저 태어남')], ['same', t('Same year', '같은 해')], ['later', t('Born later', '더 나중에 태어남')]] : [['yes', t('Yes, at the same time', '네, 같은 시대')], ['no', t('No, never', '아니요, 한 번도')]];
  return (
    <div className="try-box" style={actBox} data-mk="first">
      <div style={actTitle}>{t('Who came first?', '누가 먼저일까?')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>왼쪽 작곡가의 연도를 보고, 오른쪽 작곡가를 맞혀요. 맞히면 오른쪽이 왼쪽으로 넘어가고 사슬이 이어져요. 몇 연속까지 갈 수 있을까요?</> : <>Look at the left composer's years, then guess about the right one. Get it right and the right card slides over: the chain goes on. How long a streak can you make?</>}</div>
      <div style={{display:'flex',gap:'4px 12px',justifyContent:'center',flexWrap:'wrap',margin:'0 0 6px'}}>{WF_STARS.map(([id, en, ko]) => <span key={id} style={{fontSize:12.5,fontWeight:800,color:st[id] ? BK.coral : BK.muted}}>{st[id] ? '★' : '☆'} {t(en, ko)}</span>)}</div>
      {spChips([['born', t('Born first?', '누가 먼저 태어났을까?')], ['alive', t('Alive at the same time?', '같은 시대에 살았을까?')]], mode, (x) => { setMode(x); setP({ a, b: nextB(a, x) }); setRes(null); setRun(0); })}
      <div style={{display:'flex',gap:8,alignItems:'stretch',margin:'8px 0'}}>{card(a, true)}<div style={{alignSelf:'center',fontSize:18,fontWeight:900,color:BK.coral}}>?</div>{card(B, !!res)}</div>
      <div style={{textAlign:'center',fontSize:14.5,fontWeight:900,color:BK.ink,marginBottom:6}}>{mode === 'born' ? t(B.sur[0] + ' was born…', B.sur[1] + ': 언제 태어났을까요?') : t('Were ' + a.sur[0] + ' and ' + B.sur[0] + ' ever alive at the same time?', a.sur[1] + ', ' + B.sur[1] + ': 같은 때에 살아 있던 적이 있을까요?')}</div>
      <div style={{display:'grid',gridTemplateColumns:'repeat(' + opts.length + ',minmax(0,1fr))',gap:6}}>{opts.map(([id, lab]) => <button key={id} className={'choice-btn' + (!res ? '' : id === truth ? ' good' : id === res.x ? ' bad' : '')} onClick={() => answer(id)} style={{padding:'10px 4px',fontSize:13.5,fontWeight:900,minWidth:0}}>{lab}</button>)}</div>
      {spMsg(res ? (res.ok ? t('Yes! ' + run + ' in a row.' + (truth === 'same' ? ' Both born in ' + a.born + '!' : ''), '맞아요! ' + run + '연속.' + (truth === 'same' ? ' 둘 다 ' + a.born + '년생!' : '')) : t('Not this time: ' + B.sur[0] + ', ' + wfYrs(B) + '. The streak starts again.', '아쉬워요: ' + B.sur[1] + ', ' + wfYrs(B) + '. 연속이 처음부터.')) : t('Streak: ' + run + (st.best ? ' · best: ' + st.best : ''), '연속: ' + run + (st.best ? ' · 최고: ' + st.best : '')), res ? (res.ok ? BK.green : BK.coral) : undefined)}
      {res && <div style={{textAlign:'center',marginTop:8}}><button className="primary-btn" style={spBtn} onClick={next}>{t('Next →', '다음 →')}</button></div>}
    </div>
  );
}
'''
rep("// ══ Build BH: Blues jam ══", CODE + "\n// ══ Build BH: Blues jam ══")
rep("""  { id: 'mk-triad', ch: 'listen-5',""", """  { id: 'mk-surprise', ch: 'piano-story', title: 'Make a surprise!', blurb: 'A quiet tune with one huge BANG: on the piano it surprises; on the harpsichord it cannot.', C: () => <SurpriseTune/> },   // Build CK
  { id: 'mk-who', ch: 'pitch-range', title: 'Who can play my note?', blurb: 'Move one note across the 88 keys: the instruments and voices that reach it light up.', C: () => <WhoCanPlay/> },
  { id: 'mk-first', ch: 'composers', title: 'Who came first?', blurb: 'A chain of composers: born earlier, later or the same year? Alive at the same time? Build a streak.', C: () => <WhoFirst/> },
  { id: 'mk-triad', ch: 'listen-5',""")
rep("""  'mk-triad': ['3화음 탑',""", """  'mk-surprise': ['깜짝 놀래기!', '조용한 선율에 큰 쾅 하나: 피아노는 놀래키고, 하프시코드는 못 해요.'],
  'mk-who': ['내 음을 누가 낼 수 있을까?', '88건반 위로 음 하나를 옮겨요: 그 음에 닿는 악기와 목소리에 불이 켜져요.'],
  'mk-first': ['누가 먼저일까?', '작곡가 사슬: 먼저, 나중, 같은 해? 같은 시대에 살았을까? 연속 기록을 세워요.'],
  'mk-triad': ['3화음 탑',""")
rep("""'mk-triad': ['chords', 2, 3, 'game ear'],""", """'mk-triad': ['chords', 2, 3, 'game ear'], 'mk-surprise': ['about', 0, 1, 'game ear'], 'mk-who': ['about', 0, 2, 'game ear'], 'mk-first': ['about', 1, 2, 'game'],""")
rep("""'mk-triad': 'aural',""", """'mk-triad': 'aural', 'mk-surprise': 'about', 'mk-who': 'about', 'mk-first': 'about',""")
rep("""  'mk-triad': () => (\n""", """  'mk-surprise': () => (
    <svg width="34" height="34" viewBox="0 0 24 24"><rect width="24" height="24" rx="6" fill="#e4572e"/>{[4, 7, 10].map(x => <circle key={x} cx={x} cy="15" r="1.3" fill="#fefbf3"/>)}<path d="M17 6 L18.2 9.5 L21.5 9 L19 11.5 L21 14.5 L17.6 13.4 L16 16.5 L15.3 13 L12 12.5 L15 10.6 L14 7.4 Z" fill="#e9a83a"/></svg>
  ),
  'mk-who': () => (
    <svg width="34" height="34" viewBox="0 0 24 24"><rect width="24" height="24" rx="6" fill="#2e8a6e"/>{[[4, 9, 16], [7, 6, 19], [10, 11, 14], [13, 4, 12]].map(([y, a, b]) => <line key={y} x1={a} x2={b} y1={y + 3} y2={y + 3} stroke="#fefbf3" strokeWidth="1.8" strokeLinecap="round"/>)}<line x1="12" x2="12" y1="3" y2="21" stroke="#e9a83a" strokeWidth="1.4"/></svg>
  ),
  'mk-first': () => (
    <svg width="34" height="34" viewBox="0 0 24 24"><rect width="24" height="24" rx="6" fill="#7a4f96"/><rect x="3" y="6" width="7.5" height="11" rx="1.5" fill="#fefbf3"/><rect x="13.5" y="6" width="7.5" height="11" rx="1.5" fill="none" stroke="#fefbf3" strokeWidth="1.1"/><text x="17.25" y="14.5" textAnchor="middle" fontFamily="Georgia, serif" fontSize="7" fontWeight="900" fill="#e9a83a">?</text></svg>
  ),
  'mk-triad': () => (\n""")
rep("""  'piano-story': ['sps-sound', 'sps-softloud', 'sps-action', 'sps-pedals', 'sps-keys'],""", """  'piano-story': ['sps-sound', 'sps-softloud', 'sps-action', 'sps-pedals', 'sps-keys', 'mk-surprise'],""")
rep("""  'pitch-range': ['spr-zone', 'spr-big', 'spr-fam', 'spr-ladder', 'spr-tune', 'spr-wind', 'spr-brass', 'spr-range', 'string-lab', 'hz-explorer', 'octave-ladder'],""", """  'pitch-range': ['spr-zone', 'spr-big', 'spr-fam', 'spr-ladder', 'spr-tune', 'spr-wind', 'spr-brass', 'spr-range', 'string-lab', 'hz-explorer', 'octave-ladder', 'mk-who'],""")
rep("""  'composers': ['cpx-map', 'cpx-baroque', 'cpx-dances', 'cpx-classical', 'cpx-romantic', 'cpx-modern', 'cpx-alive', 'cpx-order', 'composer-cards', 'movement-map', 'who-am-i', 'name-that-tune'],""", """  'composers': ['cpx-map', 'cpx-baroque', 'cpx-dances', 'cpx-classical', 'cpx-romantic', 'cpx-modern', 'cpx-alive', 'cpx-order', 'composer-cards', 'movement-map', 'who-am-i', 'name-that-tune', 'mk-first'],""")

open(dst, 'w', encoding='utf-8').write(s)
print('ok')
