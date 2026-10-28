import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)

# Build CH (call 25, batch 6; her 09:56: fun first): the Beginner and Grades 2-3 rooms still without a thing to make.
#   Posture and hands: Fix the pianist (a side-view pianist set up all wrong; move the stool, sit, footstool, hand shape;
#     "Ready to play?" names the first fault in the room's own words; fewer tries, more stars)
#   Note values: Ways to make four beats (notes and rests that fill a 4/4 bar; each new way is caught and counted)
#   Ear Training, Grade 2: The tune on top (a chain of the Grade 2 two-note chords; the listener hums the top line)
#   Ear Training, Grade 3: Ear duel (two players set each other Grade 3 questions; first to five)
#   Scales further: My melodic minor tune (A, E or D minor; the 6th and 7th rise going up and fall back coming down)
#   Intervals and chords further: Fill the choir (one note each for S, A, T and B; every chord note, in order; root position
#     or first inversion)
#   Rhythm further: Split the beat (two bars of 4/4, each beat split one of seven ways; then listen and tap it)

CODE = r'''
// ══ Build CH: batch 6, the Beginner and Grades 2–3 rooms' things to make (call 25; her 09:56: fun first) ══
// ── Posture and hands: Fix the pianist. Side view: piano on the right, the stool moves, the pianist sits on it. The
// faults are named in the room's own words (POSTURE_SIT, POSTURE_HAND, the Lesson Book's sitting steps). ──
const PF_HAND = ['good', 'flat', 'low', 'high'];
const pfGeom = (st) => {
  const SY = [125, 111, 97][st.h], SX = [134, 114, 96][st.d], front = st.s === 0;
  const hip = { x: SX + (front ? 38 : 13), y: SY - 4 }, ang = (front ? 8 : -14) * Math.PI / 180;
  const sh = { x: hip.x + 52 * Math.sin(ang), y: hip.y - 52 * Math.cos(ang) }, head = { x: sh.x + 19 * Math.sin(ang), y: sh.y - 19 * Math.cos(ang) };
  const HS = { good: [[206, 89], [213, 85], [219, 95]], flat: [[204, 93], [212, 93], [222, 95]], low: [[203, 101], [211, 96], [218, 95]], high: [[207, 79], [212, 84], [218, 95]] }[PF_HAND[st.hand]];
  const a = 36, b = 34, W = { x: HS[0][0], y: HS[0][1] }, dx = W.x - sh.x, dy = W.y - sh.y, D = Math.hypot(dx, dy), dir = Math.atan2(dy, dx);
  let el, reach = true, sx = 0, sy = 0;
  if (D >= a + b - 0.5) { reach = false; const L = a + b - 1; el = { x: sh.x + a * Math.cos(dir), y: sh.y + a * Math.sin(dir) }; sx = sh.x + L * Math.cos(dir) - W.x; sy = sh.y + L * Math.sin(dir) - W.y; }
  else { const al = Math.acos((a * a + D * D - b * b) / (2 * a * D)), e1 = { x: sh.x + a * Math.cos(dir + al), y: sh.y + a * Math.sin(dir + al) }, e2 = { x: sh.x + a * Math.cos(dir - al), y: sh.y + a * Math.sin(dir - al) }; el = e1.y > e2.y ? e1 : e2; }
  const hand = HS.map(([x, y]) => ({ x: x + sx, y: y + sy }));
  const ground = 185 - (st.f ? 16 : 0), knee = { x: hip.x + 40, y: hip.y + 2 }, low = knee.y + 64, dangle = low < ground - 1;
  return { SX, SY, hip, sh, head, el, hand, reach, knee, foot: { x: knee.x + 4, y: dangle ? low : ground }, dangle };
};
const pfProblems = (st) => { const out = [], P = (id) => POSTURE_SIT.find(x => x.id === id).why;
  if (st.h !== 1) out.push(P(st.h === 0 ? 'low' : 'high'));
  if (st.d !== 1) out.push(P(st.d === 0 ? 'close' : 'far'));
  if (st.s !== 0) out.push(['Leaning back, like on a sofa. Sit on the front half of the stool, tall.', '소파처럼 뒤로 기댔어요. 의자 앞쪽 절반에 곧게 앉아요.']);
  if (pfGeom(st).dangle) out.push(['Feet dangling? A footstool or a sturdy box fixes it.', '발이 대롱대롱하면 발판이나 튼튼한 상자를 놓아요.']);
  if (st.hand !== 0) out.push(POSTURE_HAND.find(x => x.id === PF_HAND[st.hand]).why);
  return out; };
const pfFresh = () => { let x, g = 0; do { x = { h: kqRnd(3), d: kqRnd(3), s: kqRnd(2), f: kqRnd(2), hand: kqRnd(4) }; } while (pfProblems(x).length < 3 && g++ < 60); return x; };
const PF_TUNE = [0, 2, 4, 5, 7, 5, 4, 2, 0];
function PianistFix() {
  const T = useSpTimers();
  const [st, setSt] = useState(pfFresh), [tries, setTries] = useState(0), [say, setSay] = useState(null), [done, setDone] = useState(null), [sing, setSing] = useState(-1);
  const [best, setBest] = useState(() => { try { return Number(localStorage.getItem('pb_mk_pianist')) || 0; } catch (e) { return 0; } });
  const g = pfGeom(st), ink = BK.ink, cor = BK.coral, P = (p) => p.x.toFixed(1) + ' ' + p.y.toFixed(1);
  const ch = (k, v) => { if (done) return; T.clear(); setSay(null); setSt(x => ({ ...x, [k]: v })); };
  const ready = () => { if (done) return; const pr = pfProblems(st), n = tries + 1; setTries(n);
    if (pr.length) { setSay(pr[0]); return; }
    const stars = n === 1 ? 3 : n === 2 ? 2 : 1; setDone({ n, stars }); setSay(null);
    if (stars > best) { setBest(stars); try { localStorage.setItem('pb_mk_pianist', String(stars)); } catch (e) {} }
    const r = spPlay(PF_TUNE.map((k, j) => ({ at: j * 0.5, keys: [k], len: j === PF_TUNE.length - 1 ? 1.4 : 0.45, vol: 0.14 })), 66); if (!r) return;
    PF_TUNE.forEach((k, j) => T.at(r.ms(j * 0.5), () => setSing(j))); T.at(r.ms(PF_TUNE.length * 0.5 + 1.2), () => setSing(-1)); };
  const again = () => { T.clear(); setSt(pfFresh()); setTries(0); setSay(null); setDone(null); setSing(-1); };
  const smile = !!done, hd = g.head, H = g.hand;
  const stepBtn = (lab, fn, dis) => <button className="ghost-btn" style={{...spBtn, minWidth:0, padding:'6px 10px'}} disabled={dis || !!done} onClick={fn}>{lab}</button>;
  return (
    <div className="try-box" style={actBox} data-mk="pianist">
      <div style={actTitle}>{t('Fix the pianist', '피아니스트 고치기')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>이 피아니스트, 엉망이에요! 의자를 옮기고, 바르게 앉히고, 손 모양을 고쳐요. 완벽하다 싶으면 <b>칠 준비 됐나요?</b>를 눌러요. 덜 물어볼수록 별이 많아요.</> : <>This pianist is all wrong! Move the stool, sit them properly, fix the hand. When you think it is perfect, press <b>Ready to play?</b> Fewer tries, more stars.</>}</div>
      <svg viewBox="0 0 300 192" style={{width:'100%',maxWidth:440,display:'block',margin:'0 auto'}} data-pf={JSON.stringify(st)}>
        <line x1="6" x2="294" y1="185" y2="185" stroke={ink} strokeWidth="2"/>
        <rect x="232" y="26" width="60" height="159" rx="3" fill="#fff" stroke={ink} strokeWidth="2"/>
        <line x1="232" x2="292" y1="50" y2="50" stroke={ink} strokeWidth="1.2"/>
        <rect x="238" y="58" width="48" height="26" rx="2" fill="none" stroke={ink} strokeWidth="1.2" opacity="0.6"/>
        <rect x="196" y="95" width="40" height="11" fill="#fff" stroke={ink} strokeWidth="2"/>
        <rect x="222" y="90" width="12" height="5" fill={ink}/>
        <rect x={g.SX} y={g.SY} width="50" height="7" rx="2" fill="#fff" stroke={ink} strokeWidth="2"/>
        <line x1={g.SX + 6} x2={g.SX + 6} y1={g.SY + 7} y2="185" stroke={ink} strokeWidth="2.5"/>
        <line x1={g.SX + 44} x2={g.SX + 44} y1={g.SY + 7} y2="185" stroke={ink} strokeWidth="2.5"/>
        {st.f === 1 && <rect x={g.foot.x - 16} y="169" width="36" height="16" rx="2" fill="#fbe3da" stroke={ink} strokeWidth="2"/>}
        <g stroke={ink} strokeLinecap="round" strokeLinejoin="round" fill="none">
          <path d={'M' + P(g.hip) + ' L' + P(g.knee) + ' L' + P(g.foot) + (g.dangle ? ' l9 4' : ' l12 0')} strokeWidth="5"/>
          <line x1={g.hip.x} y1={g.hip.y} x2={g.sh.x} y2={g.sh.y} strokeWidth="8"/>
          <path d={'M' + P(g.sh) + ' L' + P(g.el) + ' L' + P(H[0])} strokeWidth="4.5"/>
        </g>
        <path d={'M' + P(H[0]) + ' L' + P(H[1]) + ' L' + P(H[2])} stroke={cor} strokeWidth="4" strokeLinecap="round" strokeLinejoin="round" fill="none"/>
        <circle cx={hd.x} cy={hd.y} r="11" fill="#fff" stroke={ink} strokeWidth="2.5"/>
        <circle cx={hd.x + 5} cy={hd.y - 2} r="1.6" fill={ink}/>
        <path d={smile ? 'M' + (hd.x + 2) + ' ' + (hd.y + 4) + ' q4 4 8 -1' : say ? 'M' + (hd.x + 2) + ' ' + (hd.y + 6) + ' q4 -3 8 0' : 'M' + (hd.x + 3) + ' ' + (hd.y + 5) + ' l6 0'} stroke={ink} strokeWidth="1.8" fill="none" strokeLinecap="round"/>
        {sing >= 0 && [0, 1].map(j => <text key={j} x={hd.x + 16 + j * 14} y={hd.y - 14 - ((sing + j) % 3) * 5} fontFamily={MUSIC_FONT} fontSize="15" fill={cor}>♪</text>)}
      </svg>
      <div style={{display:'flex',flexWrap:'wrap',gap:6,justifyContent:'center',margin:'6px 0 2px'}}>
        <span style={{alignSelf:'center',fontSize:12,fontWeight:900,color:BK.muted}}>{t('Stool', '의자')}</span>
        {stepBtn(t('▼ Lower', '▼ 낮게'), () => ch('h', st.h - 1), st.h === 0)}{stepBtn(t('▲ Higher', '▲ 높게'), () => ch('h', st.h + 1), st.h === 2)}
        {stepBtn(t('← Further', '← 멀리'), () => ch('d', st.d + 1), st.d === 2)}{stepBtn(t('Closer →', '가까이 →'), () => ch('d', st.d - 1), st.d === 0)}
      </div>
      {spChips([[0, t('Front half', '앞쪽 절반')], [1, t('At the back', '뒤쪽')]], st.s, (v) => ch('s', v))}
      <div style={{display:'flex',flexWrap:'wrap',gap:6,justifyContent:'center',margin:'2px 0'}}>
        {stepBtn(st.f ? t('Footstool: on', '발판: 있음') : t('Footstool: off', '발판: 없음'), () => ch('f', 1 - st.f))}
        {stepBtn(t('↻ Hand shape', '↻ 손 모양'), () => ch('hand', (st.hand + 1) % PF_HAND.length))}
      </div>
      {spMsg(say ? t(say[0], say[1]) : done ? t('Ready! Fixed in ' + done.n + (done.n === 1 ? ' try. ' : ' tries. ') + '★★★'.slice(0, done.stars), '준비 완료! ' + done.n + '번 만에 고쳤어요. ' + '★★★'.slice(0, done.stars)) : t('Fix it, then ask.', '고친 다음 물어봐요.'), say ? cor : done ? BK.green : undefined)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        {!done && <button className="primary-btn" style={spBtn} onClick={ready}>{t('Ready to play?', '칠 준비 됐나요?')}</button>}
        <button className="ghost-btn" style={spBtn} onClick={again}>{t('↻ A new pianist', '↻ 새 피아니스트')}</button>
      </div>
      {best > 0 && <div style={{textAlign:'center',fontSize:12,fontWeight:800,color:BK.muted,marginTop:6}}>{t('Best: ', '최고: ') + '★★★'.slice(0, best)}</div>}
    </div>
  );
}

// ── Note values: Ways to make four beats. Each new way is caught; the minim rest starts on beat 1 or 3, as in the room's bars ──
const BW_PARTS = ['q', 'p', 'h', 'hd', 'w', 'r', 'hr', 'wr'];
const bwUsed = (row) => row.reduce((a, k) => a + NV_ROOM[k].b, 0);
const bwFits = (row, k) => { const u = bwUsed(row); return u + NV_ROOM[k].b <= 4 && !(k === 'hr' && u % 2); };
let BW_TOTAL = 0;
const bwTotal = () => { if (BW_TOTAL) return BW_TOTAL; let n = 0; const go = (row) => { if (bwUsed(row) === 4) { n++; return; } BW_PARTS.forEach(k => { if (bwFits(row, k)) go(row.concat([k])); }); }; go([]); BW_TOTAL = n; return n; };
const bwBeats = (b) => t(b === 1 ? '1 beat' : b + ' beats', b + '박');
const BW_MILES = [5, 15, 30];
function BeatWays() {
  const [row, setRow] = useState([]), [res, setRes] = useState(null), [all, setAll] = useState(false);
  const [found, setFound] = useState(() => { try { return JSON.parse(localStorage.getItem('pb_mk_ways')) || []; } catch (e) { return []; } });
  const total = bwTotal(), used = bwUsed(row), full = used === 4, base = full ? [] : row;
  const hear = (r) => { stopClicks(); rqRun(r.map(x => [x, NV_ROOM[x].b])); };
  const add = (k) => { if (!bwFits(base, k)) return; const r = base.concat([k]); setRow(r); setRes(null);
    if (bwUsed(r) === 4) { const key = r.join('.'), at = found.indexOf(key);
      if (at < 0) { const n = found.concat([key]); setFound(n); try { localStorage.setItem('pb_mk_ways', JSON.stringify(n)); } catch (e) {} setRes({ isNew: true, n: n.length }); } else setRes({ isNew: false, n: at + 1 });
      hear(r); } };
  const shown = all ? found : found.slice(-8);
  return (
    <div className="try-box" style={actBox} data-mk="ways">
      <div style={actTitle}>{t('Ways to make four beats', '4박을 만드는 방법')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>음표와 쉼표로 <b>딱 4박</b>을 채워요. 새로운 방법을 찾을 때마다 내 모음집에 들어가요. 모두 몇 가지일까요?</> : <>Fill exactly <b>four beats</b> with notes and rests. Every new way you find goes into your collection. How many are there?</>}</div>
      <div style={{textAlign:'center',fontFamily:LB_SERIF,fontSize:22,fontWeight:900,color:BK.ink,fontVariantNumeric:'lining-nums'}}>{found.length} <span style={{fontSize:14,color:BK.muted}}>/ {total} {t('found', '찾음')}</span></div>
      <div style={{display:'flex',gap:'4px 12px',justifyContent:'center',flexWrap:'wrap',margin:'0 0 6px'}}>{BW_MILES.map(m => <span key={m} style={{fontSize:12.5,fontWeight:800,color:found.length >= m ? BK.coral : BK.muted}}>{found.length >= m ? '★' : '☆'} {t(m + ' ways', m + '가지')}</span>)}</div>
      <div style={{display:'grid',gridTemplateColumns:'repeat(4,minmax(0,1fr))',gap:4,maxWidth:360,margin:'4px auto 8px'}}>
        {row.map((k, j) => <div key={j} style={{gridColumn:'span ' + NV_ROOM[k].b,border:'2px solid ' + (full && res ? (res.isNew ? BK.green : BK.coral) : BK.ink),borderRadius:10,background:'#fff',display:'flex',flexDirection:'column',alignItems:'center',padding:'2px 0 4px',minWidth:0}}><NvGlyph kind={k} size={40}/><span style={{fontSize:10.5,fontWeight:800,color:BK.muted}}>{bwBeats(NV_ROOM[k].b)}</span></div>)}
        {Array.from({ length: 4 - used }).map((_, j) => <div key={'e' + j} style={{border:'2px dashed ' + BK.line,borderRadius:10,minHeight:66}}/>)}
      </div>
      <div style={{display:'grid',gridTemplateColumns:'repeat(4,minmax(0,1fr))',gap:6,maxWidth:400,margin:'0 auto'}}>{BW_PARTS.map(k => { const ok = bwFits(base, k);
        return <button key={k} className="choice-btn" disabled={!ok} onClick={() => add(k)} style={{padding:'2px 0 4px',opacity:ok ? 1 : 0.3,display:'flex',flexDirection:'column',alignItems:'center',minWidth:0}}><NvGlyph kind={k} size={32}/><span style={{fontSize:10.5,fontWeight:800}}>{bwBeats(NV_ROOM[k].b)}</span></button>; })}</div>
      {spMsg(res ? (res.isNew ? t('New! Way number ' + res.n + '.', '새로운 방법! ' + res.n + '번째예요.') : t('You found that one already: way number ' + res.n + '.', '이미 찾은 방법이에요: ' + res.n + '번째.'))
        : used === 1 ? t((4 - used) + ' beats to go. The minim rest starts on beat 1 or beat 3.', '앞으로 3박. 2분쉼표는 1박이나 3박에서 시작해요.') : used ? t((4 - used) + (4 - used === 1 ? ' beat to go.' : ' beats to go.'), '앞으로 ' + (4 - used) + '박.') : t('Tap notes and rests to fill the bar.', '음표와 쉼표를 눌러 마디를 채워요.'), res ? (res.isNew ? BK.green : BK.coral) : undefined)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:6}}>
        {row.length > 0 && !full && <button className="ghost-btn" style={spBtn} onClick={() => { setRow(row.slice(0, -1)); setRes(null); }}>{t('⌫ Back', '⌫ 지우기')}</button>}
        {full && <button className="ghost-btn" style={spBtn} onClick={() => hear(row)}>{t('▶ Hear it again', '▶ 다시 듣기')}</button>}
      </div>
      {found.length > 0 && <div style={{marginTop:10}}>
        <div style={{fontSize:12,fontWeight:900,color:BK.muted,textAlign:'center',marginBottom:4}}>{t('My collection: tap one to hear it', '내 모음집: 눌러서 들어요')}</div>
        <div style={{display:'flex',flexWrap:'wrap',gap:6,justifyContent:'center'}}>{shown.map((key) => { const n = found.indexOf(key) + 1;
          return <button key={key} className="ghost-btn" onClick={() => hear(key.split('.'))} style={{display:'inline-flex',alignItems:'center',gap:0,padding:'0 6px 0 4px',minHeight:34}}><span style={{fontSize:10,fontWeight:900,color:BK.muted,marginRight:2}}>{n}</span>{key.split('.').map((k, j) => <NvGlyph key={j} kind={k} size={24}/>)}</button>; })}</div>
        {found.length > 8 && <div style={{textAlign:'center',marginTop:6}}><button className="ghost-btn" style={spBtn} onClick={() => setAll(!all)}>{all ? t('Show the newest', '최근 것만') : t('Show all ' + found.length, found.length + '개 모두 보기')}</button></div>}
      </div>}
    </div>
  );
}

// ── Ear Training, Grade 2: The tune on top. A chain of the Grade 2 two-note chords (a major 3rd or a perfect 5th) ──
const HT_STARS = [['third', 'Use a 3rd', '3도 쓰기'], ['fifth', 'Use a 5th', '5도 쓰기'], ['hum', 'Someone hummed the top tune', '누군가 위 선율을 흥얼거렸어요']];
function HiddenTune() {
  const T = useSpTimers();
  const [ch, setCh] = useState([3, 1, 2, 3]), [on, setOn] = useState(-1), [part, setPart] = useState(null), [heard, setHeard] = useState(false);
  const [stars, setStars] = useState(() => { try { return JSON.parse(localStorage.getItem('pb_mk_hidden')) || {}; } catch (e) { return {}; } });
  const give = (ks) => { const n = { ...stars }; ks.forEach(k => { n[k] = 1; }); setStars(n); try { localStorage.setItem('pb_mk_hidden', JSON.stringify(n)); } catch (e) {} };
  const kind = (i) => (L2_G2[i][1] - L2_G2[i][0] === 4 ? 3 : 5);
  const play = (p) => { T.clear(); const ev = ch.map((i, j) => { const pr = L2_G2[i]; return { at: j * 1.25, keys: p === 'top' ? [pr[1]] : p === 'bot' ? [pr[0]] : pr, len: 1.1, vol: 0.13 }; });
    const r = spPlay(ev, 60); if (!r) return; ev.forEach((e, j) => T.at(r.ms(e.at), () => setOn(j))); T.at(r.ms(ch.length * 1.25 + 0.3), () => setOn(-1)); setPart(p);
    if (p === 'both') { setHeard(true); const ks = []; if (ch.some(i => kind(i) === 3)) ks.push('third'); if (ch.some(i => kind(i) === 5)) ks.push('fifth'); if (ks.length) give(ks); } };
  const add = (i) => { if (ch.length >= 6) return; T.clear(); setOn(-1); setCh(ch.concat([i])); playKey(L2_G2[i][0], 0.5); playKey(L2_G2[i][1], 0.5); setPart(null); setHeard(false); };
  const circ = (L, lit, col) => <span style={{width:30,height:30,borderRadius:15,display:'inline-flex',alignItems:'center',justifyContent:'center',fontWeight:900,fontSize:14,border:'2px solid ' + col,background:lit ? col : '#fff',color:lit ? '#fff' : col}}>{L}</span>;
  return (
    <div className="try-box" style={actBox} data-mk="hidden">
      <div style={actTitle}>{t('The tune on top', '위에 숨은 선율')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>Grade 2 시험의 두 음(장3도나 완전5도)을 이어 붙여요. 함께 울리면 <b>위쪽 음들이 선율</b>이 돼요. 들려주고 위 선율을 흥얼거려 보게 해요. 그다음 위 선율만 들어서 확인!</> : <>Chain together the Grade 2 two-note chords (a major 3rd or a perfect 5th). Played together, <b>the top notes make a tune</b>. Play it to someone: can they hum the top tune? Then check with the top alone.</>}</div>
      <div style={{display:'flex',gap:'4px 12px',justifyContent:'center',flexWrap:'wrap',margin:'0 0 6px'}}>{HT_STARS.map(([id, en, ko]) => <span key={id} style={{fontSize:12.5,fontWeight:800,color:stars[id] ? BK.coral : BK.muted}}>{stars[id] ? '★' : '☆'} {t(en, ko)}</span>)}</div>
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',minHeight:96,margin:'4px 0'}}>{ch.map((i, j) => { const [a, b] = L2_G2[i], cur = j === on;
        return <div key={j} style={{display:'flex',flexDirection:'column',alignItems:'center',gap:3,padding:'4px 3px',borderRadius:10,background:cur ? '#fbe3da' : 'transparent'}}>
          {circ(lwLet(b), cur && part !== 'bot', part === 'bot' ? BK.line : BK.coral)}{circ(lwLet(a), cur && part !== 'top', part === 'top' ? BK.line : BK.ink)}
          <span style={{fontSize:10,fontWeight:900,color:BK.muted}}>{kind(i) === 3 ? t('3rd', '3도') : t('5th', '5도')}</span></div>; })}</div>
      <div style={{display:'grid',gridTemplateColumns:'repeat(7,minmax(0,1fr))',gap:4,maxWidth:420,margin:'0 auto'}}>{L2_G2.map(([a, b], i) => <button key={i} className="choice-btn" disabled={ch.length >= 6} onClick={() => add(i)} style={{padding:'4px 0',display:'flex',flexDirection:'column',alignItems:'center',lineHeight:1.15,minWidth:0}}>
        <span style={{fontWeight:900,fontSize:14,color:BK.coral}}>{lwLet(b)}</span><span style={{fontWeight:900,fontSize:14}}>{lwLet(a)}</span><span style={{fontSize:9.5,fontWeight:800,color:BK.muted}}>{kind(i) === 3 ? t('3rd', '3도') : t('5th', '5도')}</span></button>)}</div>
      {spMsg(part === 'top' ? t('The top alone: ' + ch.map(i => lwLet(L2_G2[i][1])).join(' ') + '. Was that what they hummed?', '위 음만: ' + ch.map(i => lwLet(L2_G2[i][1])).join(' ') + '. 흥얼거린 선율과 같았나요?')
        : part === 'bot' ? t('The bottom alone: ' + ch.map(i => lwLet(L2_G2[i][0])).join(' ') + '.', '아래 음만: ' + ch.map(i => lwLet(L2_G2[i][0])).join(' ') + '.')
        : heard ? t('Now hum the top notes, one by one.', '이제 위 음을 하나씩 흥얼거려요.') : t('Up to six pairs. Tap ▶ to hear them together.', '여섯 쌍까지. ▶를 눌러 함께 들어요.'))}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        <button className="primary-btn" style={spBtn} disabled={!ch.length} onClick={() => play('both')}>{t('▶ Together', '▶ 함께')}</button>
        <button className="ghost-btn" style={spBtn} disabled={!ch.length} onClick={() => play('top')}>{t('♪ Top alone', '♪ 위 음만')}</button>
        <button className="ghost-btn" style={spBtn} disabled={!ch.length} onClick={() => play('bot')}>{t('♪ Bottom alone', '♪ 아래 음만')}</button>
        {ch.length > 0 && <button className="ghost-btn" style={spBtn} onClick={() => { T.clear(); setOn(-1); setCh(ch.slice(0, -1)); setPart(null); setHeard(false); }}>{t('⌫ Back', '⌫ 지우기')}</button>}
      </div>
      {heard && !stars.hum && <div style={{textAlign:'center',marginTop:8}}><button className="ghost-btn" style={spBtn} onClick={() => give(['hum'])}>{t('✓ They hummed it!', '✓ 흥얼거렸어요!')}</button></div>}
    </div>
  );
}

// ── Ear Training, Grade 3: Ear duel. Two players take turns: one sets a Grade 3 question, the other answers. Right: a point
// to the one who answered; wrong: a point to the one who set it. First to five. ──
const DU_TYPES = [['deg', 'From the keynote', '으뜸음에서'], ['metre', 'Two or three?', '두 박? 세 박?'], ['pair', 'Two notes at once', '두 음 함께']];
const DU_WIN = 5;
function EarDuel() {
  const [score, setScore] = useState([0, 0]), [setter, setSetter] = useState(0), [type, setType] = useState('deg'), [q, setQ] = useState(null), [phase, setPhase] = useState('set'), [got, setGot] = useState(null), [pair, setPair] = useState([]), [run, setRun] = useState([0, 0]);
  const gs = 1 - setter, win = score[0] >= DU_WIN ? 0 : score[1] >= DU_WIN ? 1 : -1, PN = (i) => t('Player ' + (i + 1), '플레이어 ' + (i + 1));
  const play = (x) => { stopClicks(); if (x.type === 'deg') l2PlayDeg(x.k, L2_DEG.find(y => y[0] === x.answer)[1]); else if (x.type === 'metre') rqRunS(L2_CLAP[x.i], { bpm: L2_CLAP_BPM }); else l2PlayDyad(x.p[0], x.p[1]); };
  const make = (answer, extra) => { setQ({ type, answer, ...extra }); setPhase('ready'); };
  const setMetre = (m) => { const is = L2_CLAP.map((x, j) => j).filter(j => srhTop(L2_CLAP[j]) === m); make(m, { i: pick(is) }); };
  const tapSet = (k) => { if (!L2_WHITE.includes(k)) return;   /* silent: the one answering may still hear */ const p = pair.length >= 2 ? [k] : pair.concat([k]); if (p.length === 2 && p[0] === p[1]) return; setPair(p.slice().sort((a, b) => a - b)); };
  const answer = (c) => { if (phase !== 'answer') return; stopClicks(); const ok = c === q.answer; setGot({ c, ok }); setPhase('shown');
    const sc = score.slice(); sc[ok ? gs : setter]++; setScore(sc); const r = run.slice(); r[gs] = ok ? r[gs] + 1 : 0; setRun(r); };
  const next = () => { stopClicks(); setSetter(gs); setQ(null); setGot(null); setPair([]); setPhase('set'); };
  const fresh = () => { stopClicks(); setScore([0, 0]); setRun([0, 0]); setSetter(0); setQ(null); setGot(null); setPair([]); setPhase('set'); };
  const ansLab = (x, v) => (x.type === 'deg' ? l2DegName(v) : x.type === 'metre' ? (v === 2 ? t('two', '두 박') : t('three', '세 박')) : lwLet(v));
  const grid = (n) => ({display:'grid',gridTemplateColumns:'repeat(' + n + ',minmax(0,1fr))',gap:8,maxWidth:420,margin:'6px auto 0'});
  const big = {padding:'12px 4px',fontSize:16,fontWeight:900};
  const cls = (c) => 'choice-btn' + (phase !== 'shown' ? '' : c === q.answer ? ' good' : got && got.c === c ? ' bad' : '');
  const board = (i) => <div key={i} style={{flex:1,minWidth:0,border:'2px solid ' + (win === i ? BK.coral : BK.ink),borderRadius:12,padding:'6px 4px',textAlign:'center',background:win === i ? '#fbe3da' : '#fff'}}>
    <div style={{fontSize:12.5,fontWeight:900,color:BK.ink}}>{PN(i)}</div>
    <div style={{display:'flex',gap:4,justifyContent:'center',margin:'4px 0'}}>{Array.from({ length: DU_WIN }).map((_, j) => <span key={j} style={{width:11,height:11,borderRadius:6,background:j < score[i] ? BK.coral : 'transparent',border:'1.5px solid ' + (j < score[i] ? BK.coral : BK.line)}}/>)}</div>
    <div style={{fontSize:10.5,fontWeight:800,color:BK.muted}}>{win >= 0 ? (win === i ? t('WINS!', '승리!') : '') : i === setter ? t('sets the question', '문제를 내요') : t('answers', '답해요')}{run[i] >= 2 && win < 0 ? ' · ' + t(run[i] + ' in a row!', run[i] + '연속!') : ''}</div></div>;
  return (
    <div className="try-box" style={actBox} data-mk="duel">
      <div style={actTitle}>{t('Ear duel', '귀 대결')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>두 사람이 번갈아 Grade 3 청음 문제를 내요. 맞히면 답한 사람이 1점, 틀리면 낸 사람이 1점. <b>먼저 5점</b>이면 승리!</> : <>Two players take turns setting each other Grade 3 ear questions. Right: a point to the one who answered. Wrong: a point to the one who set it. <b>First to five</b> wins!</>}</div>
      <div style={{display:'flex',gap:8,margin:'2px 0 8px'}}>{board(0)}{board(1)}</div>
      {win >= 0 ? <div style={{textAlign:'center'}}><span style={{display:'inline-block',transform:'rotate(-6deg)',border:'3px solid ' + BK.coral,color:BK.coral,borderRadius:8,padding:'4px 16px',fontFamily:LB_SERIF,fontSize:24,fontWeight:900}}>{t(PN(win) + ' wins!', PN(win) + ' 승리!')}</span>
        <div style={{marginTop:10}}><button className="primary-btn" style={spBtn} onClick={fresh}>{t('▶ A new match', '▶ 새 대결')}</button></div></div>
      : phase === 'set' ? <>
        <div style={{textAlign:'center',fontSize:15,fontWeight:900,color:BK.ink,margin:'0 0 4px'}}>{t(PN(setter) + ' sets a question. ' + PN(gs) + ', look away!', PN(setter) + '이(가) 문제를 내요. ' + PN(gs) + ', 보지 마요!')}</div>
        {spChips(DU_TYPES.map(([id, en, ko]) => [id, t(en, ko)]), type, (x) => { setType(x); setPair([]); })}
        {type === 'deg' && <div style={grid(4)}>{[2, 3, 4, 5].map(n => <button key={n} className="choice-btn" style={big} onClick={() => make(n, { k: pick(L2_KEYS) })}>{l2DegName(n)}</button>)}</div>}
        {type === 'metre' && <div style={grid(2)}>{[2, 3].map(m => <button key={m} className="choice-btn" style={big} onClick={() => setMetre(m)}>{m === 2 ? t('Two beats', '두 박') : t('Three beats', '세 박')}</button>)}</div>}
        {type === 'pair' && <><SpKb lo={0} hi={12} W={34} H={86} lit={Object.fromEntries(pair.map(k => [k, 'cor']))} names={Object.fromEntries(pair.map(k => [k, lwLet(k)]))} onTap={tapSet} label={t('Pick two white keys', '흰건반 두 개 고르기')}/>
          {pair.length === 2 && <div style={grid(2)}>{[[1, t('Ask: the higher', '높은 음 물어보기')], [0, t('Ask: the lower', '낮은 음 물어보기')]].map(([hi, lab]) => <button key={hi} className="choice-btn" style={{...big, fontSize:14}} onClick={() => make(hi ? pair[1] : pair[0], { p: pair, ask: hi ? 'hi' : 'lo' })}>{lab}</button>)}</div>}</>}
        {spMsg(type === 'pair' && pair.length < 2 ? t('Pick two white keys (no sound, so no peeking by ear).', '흰건반 두 개를 골라요 (소리가 안 나요, 귀로 엿듣기 금지).') : type === 'deg' ? t('Pick a note: the app plays the keynote of a major key, then that note.', '음을 골라요: 앱이 장조의 으뜸음, 그다음 그 음을 들려줘요.') : type === 'metre' ? t('Pick two or three: the app plays a passage in that time.', '두 박이나 세 박을 골라요: 앱이 그 박자의 리듬을 들려줘요.') : t('The app plays your two notes together; the answer is the one you ask for.', '앱이 두 음을 함께 들려줘요. 정답은 물어본 음이에요.'))}
      </> : <>
        {phase === 'ready' && <div style={{textAlign:'center'}}><div style={{fontSize:15,fontWeight:900,color:BK.ink,marginBottom:8}}>{t('Question set! Over to ' + PN(gs) + '.', '문제 완성! 이제 ' + PN(gs) + ' 차례.')}</div>
          <button className="primary-btn" style={spBtn} onClick={() => { play(q); setPhase('answer'); }}>{t('▶ Play the question', '▶ 문제 듣기')}</button></div>}
        {(phase === 'answer' || phase === 'shown') && <>
          <div style={{textAlign:'center',fontSize:15,fontWeight:900,color:BK.ink}}>{q.type === 'deg' ? t('The keynote, then a note: the 2nd, 3rd, 4th or 5th?', '으뜸음, 그다음 음: 2도, 3도, 4도, 5도?') : q.type === 'metre' ? t('Two or three beats in a bar?', '한 마디에 두 박? 세 박?') : q.ask === 'hi' ? t('Hum the higher note, then find it.', '높은 음을 흥얼거리고, 찾아요.') : t('Hum the lower note, then find it.', '낮은 음을 흥얼거리고, 찾아요.')}</div>
          {q.type === 'deg' && <div style={grid(4)}>{[2, 3, 4, 5].map(n => <button key={n} className={cls(n)} style={big} onClick={() => answer(n)}>{l2DegName(n)}</button>)}</div>}
          {q.type === 'metre' && <div style={grid(2)}>{[2, 3].map(m => <button key={m} className={cls(m)} style={big} onClick={() => answer(m)}>{m === 2 ? t('Two', '두 박') : t('Three', '세 박')}</button>)}</div>}
          {q.type === 'pair' && <SpKb lo={0} hi={12} W={34} H={86} lit={phase === 'shown' ? { [q.p[0]]: q.answer === q.p[0] ? 'good' : 'pale', [q.p[1]]: q.answer === q.p[1] ? 'good' : 'pale', ...(got.ok ? {} : { [got.c]: 'bad' }) } : {}} names={phase === 'shown' ? { [q.p[0]]: lwLet(q.p[0]), [q.p[1]]: lwLet(q.p[1]) } : { 0: 'C' }} onTap={(k) => { playKey(k, 0.45); answer(k); }} label={t('Find the note you hummed', '흥얼거린 음 찾기')}/>}
          {phase === 'answer' && <div style={{textAlign:'center',marginTop:8}}><button className="ghost-btn" style={spBtn} onClick={() => play(q)}>{t('♪ Again', '♪ 다시')}</button></div>}
          {phase === 'shown' && <>{spMsg(got.ok ? t('Right! A point to ' + PN(gs) + '.', '정답! ' + PN(gs) + ' 1점.') : t('Not this time: it was ' + ansLab(q, q.answer) + (q.type === 'deg' ? ' of ' + lwLet(q.k) + ' major' : '') + '. A point to ' + PN(setter) + '.', '아쉬워요: ' + (q.type === 'deg' ? lwLet(q.k) + '장조의 ' : '') + ansLab(q, q.answer) + '였어요. ' + PN(setter) + ' 1점.'), got.ok ? BK.green : BK.coral)}
            <div style={{textAlign:'center',marginTop:8}}><button className="primary-btn" style={spBtn} onClick={next}>{t('Next round: swap!', '다음 판: 바꿔요!')}</button></div></>}
        </>}
      </>}
    </div>
  );
}

// ── Scales further: My melodic minor tune. Going up, the 6th and 7th rise; coming down, they are natural again (the room's
// step 3). A 6th or 7th takes the direction of the next different note (or, at the end, the way the tune came in). ──
const MM_KEYS = { A: { s: -3, nat: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'A'], up: ['F♯', 'G♯'], en: 'A minor', ko: 'A단조' }, E: { s: 4, nat: ['E', 'F♯', 'G', 'A', 'B', 'C', 'D', 'E'], up: ['C♯', 'D♯'], en: 'E minor', ko: 'E단조' }, D: { s: 2, nat: ['D', 'E', 'F', 'G', 'A', 'B♭', 'C', 'D'], up: ['B♮', 'C♯'], en: 'D minor', ko: 'D단조' } };
const MM_NAT = [0, 2, 3, 5, 7, 8, 10, 12];
const mmUp = (tune, j) => { const g = tune[j]; if (g !== 6 && g !== 7) return false; for (let x = j + 1; x < tune.length; x++) if (tune[x] !== g) return tune[x] > g; for (let x = j - 1; x >= 0; x--) if (tune[x] !== g) return tune[x] < g; return false; };
const MM_STARS = [['up', 'Up through the 6th and 7th to the top', '6도, 7도를 지나 꼭대기로'], ['down', 'From the top down through the 7th and 6th', '꼭대기에서 7도, 6도를 지나 아래로'], ['both', 'Both in one tune', '한 선율에 둘 다']];
function MelMinorTune() {
  const T = useSpTimers();
  const [k, setK] = useState('A'), [tune, setTune] = useState([1, 3, 5, 6, 7, 8, 7, 6, 5]), [on, setOn] = useState(-1);
  const [stars, setStars] = useState(() => { try { return JSON.parse(localStorage.getItem('pb_mk_melmin')) || {}; } catch (e) { return {}; } });
  const K = MM_KEYS[k], semi = (j) => K.s + MM_NAT[tune[j] - 1] + (mmUp(tune, j) ? 1 : 0), name = (j) => (mmUp(tune, j) ? K.up[tune[j] - 6] : K.nat[tune[j] - 1]);
  const has = (seq) => tune.some((_, j) => seq.every((g, x) => tune[j + x] === g));
  const play = () => { T.clear(); if (!tune.length) return; const ev = tune.map((_, j) => ({ at: j * 0.55, keys: [semi(j)], len: j === tune.length - 1 ? 1.4 : 0.5, vol: 0.14 })), r = spPlay(ev, 60); if (!r) return;
    ev.forEach((e, j) => T.at(r.ms(e.at), () => setOn(j))); T.at(r.ms(tune.length * 0.55 + 1.2), () => setOn(-1));
    const u = has([6, 7, 8]), d = has([8, 7, 6]), n = { ...stars }; if (u) n.up = 1; if (d) n.down = 1; if (u && d) n.both = 1;
    if (Object.keys(n).length !== Object.keys(stars).length) { setStars(n); try { localStorage.setItem('pb_mk_melmin', JSON.stringify(n)); } catch (e) {} } };
  const add = (g) => { if (tune.length >= 16) return; T.clear(); setOn(-1); const nt = tune.concat([g]); setTune(nt); playKey(K.s + MM_NAT[g - 1] + (mmUp(nt, nt.length - 1) ? 1 : 0), 0.4); };
  const raised = tune.some((_, j) => mmUp(tune, j)), fell = tune.some((g, j) => (g === 6 || g === 7) && !mmUp(tune, j));
  const lit = {}; MM_NAT.forEach(x => { lit[K.s + x] = 'pale'; }); if (on >= 0) lit[semi(on)] = 'cor';
  return (
    <div className="try-box" style={actBox} data-mk="melmin">
      <div style={actTitle}>{t('My melodic minor tune', '나의 가락 단음계 선율')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>단조로 선율을 써요. <b>올라갈 때</b> 6도와 7도가 반음 올라가고, <b>내려올 때</b>는 원래대로. 6도와 7도는 다음 음이 어느 쪽으로 가는지 보고 스스로 바뀌어요!</> : <>Write a tune in a minor key. <b>Going up</b>, the 6th and 7th rise a semitone; <b>coming down</b>, they go back. The 6th and 7th watch where the next note goes and change by themselves!</>}</div>
      <div style={{display:'flex',gap:'4px 12px',justifyContent:'center',flexWrap:'wrap',margin:'0 0 6px'}}>{MM_STARS.map(([id, en, ko]) => <span key={id} style={{fontSize:12.5,fontWeight:800,color:stars[id] ? BK.coral : BK.muted}}>{stars[id] ? '★' : '☆'} {t(en, ko)}</span>)}</div>
      {spChips(Object.keys(MM_KEYS).map(x => [x, t(MM_KEYS[x].en, MM_KEYS[x].ko)]), k, (x) => { T.clear(); setOn(-1); setK(x); })}
      <div style={{display:'flex',gap:4,justifyContent:'center',flexWrap:'wrap',margin:'6px 0',minHeight:52}}>{tune.map((g, j) => { const up = mmUp(tune, j), cur = j === on;
        return <div key={j} style={{display:'flex',flexDirection:'column',alignItems:'center',gap:1}}>
          <span style={{fontSize:10,fontWeight:900,color:BK.coral,height:12}}>{up ? '↑' : ''}</span>
          <span style={{minWidth:30,height:30,padding:'0 3px',boxSizing:'border-box',borderRadius:15,display:'inline-flex',alignItems:'center',justifyContent:'center',fontWeight:900,fontSize:13,border:'2px solid ' + (up ? BK.coral : BK.ink),background:cur ? (up ? BK.coral : BK.ink) : up ? '#fbe3da' : '#fff',color:cur ? '#fff' : up ? BK.coral : BK.ink}}>{name(j)}</span>
          <span style={{fontSize:9.5,fontWeight:800,color:BK.muted}}>{g}</span></div>; })}</div>
      <SpKb lo={K.s} hi={K.s + 12} W={26} H={70} lit={lit} names={on >= 0 ? { [semi(on)]: name(on) } : { [K.s]: K.nat[0] }} onTap={() => {}} label={t(K.en, K.ko)}/>
      <div style={{display:'grid',gridTemplateColumns:'repeat(8,minmax(0,1fr))',gap:4,maxWidth:420,margin:'8px auto 0'}}>{[1, 2, 3, 4, 5, 6, 7, 8].map(g => <button key={g} className="choice-btn" disabled={tune.length >= 16} onClick={() => add(g)} style={{padding:'8px 0',fontSize:16,fontWeight:900,minWidth:0,color:g === 6 || g === 7 ? BK.coral : undefined}}>{g}</button>)}</div>
      {spMsg(raised && fell ? t('Going up: ' + K.up.join(' and ') + '. Coming down: ' + K.nat[5] + ' and ' + K.nat[6] + ' again.', '올라갈 때: ' + K.up.join(', ') + '. 내려올 때: 다시 ' + K.nat[5] + ', ' + K.nat[6] + '.')
        : raised ? t('Going up, the 6th and 7th rise: ' + K.up.join(' and ') + '.', '올라갈 때 6도와 7도가 올라가요: ' + K.up.join(', ') + '.') : fell ? t('Coming down, the 6th and 7th are natural: ' + K.nat[5] + ' and ' + K.nat[6] + '.', '내려올 때 6도와 7도는 원래대로: ' + K.nat[5] + ', ' + K.nat[6] + '.')
        : t('Tap the scale numbers: 1 is the keynote, 8 the keynote at the top.', '음계 번호를 눌러요: 1은 으뜸음, 8은 꼭대기의 으뜸음.'))}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        <button className="primary-btn" style={spBtn} disabled={!tune.length} onClick={play}>{t('▶ Play my tune', '▶ 나의 선율 듣기')}</button>
        {tune.length > 0 && <button className="ghost-btn" style={spBtn} onClick={() => { T.clear(); setOn(-1); setTune(tune.slice(0, -1)); }}>{t('⌫ Back', '⌫ 지우기')}</button>}
        <button className="ghost-btn" style={spBtn} onClick={() => { T.clear(); setOn(-1); setTune([1, 2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 1]); }}>{t('Try: up and down the scale', '해 보기: 음계 위아래')}</button>
      </div>
    </div>
  );
}

// ── Intervals and chords further: Fill the choir. One note each for soprano, alto, tenor and bass, in their ranges (H3_RANGE):
// every note of the chord, the voices in order. The bass decides root position or first inversion (the room's step 3). ──
const CC_KEYS = ['C', 'G', 'F'], CC_V = ['S', 'A', 'T', 'B'], CC_DEG = [[1, 0], [4, 3], [5, 4]];   // [degree, H3_DEGN index]
const ccRange = (v) => H3_RANGE[v].map(x => h3N(x).d);
const ccRootL = (k, deg) => (H3_L.indexOf(H3_TRI[k].tr[0]) + deg - 1) % 7;
const ccNote = (k, d) => ({ d, acc: H3_TRI[k].acc[H3_L[((d % 7) + 7) % 7]] || 0 });
const ccRole = (k, deg, d) => { const x = ((((d % 7) + 7) % 7) - ccRootL(k, deg) + 7) % 7; return x === 0 ? 'root' : x === 2 ? 'third' : x === 4 ? 'fifth' : null; };
const ccStart = (k, deg) => { const r = ccRootL(k, deg), at = (o) => o * 7 + r; return { S: at(5) <= ccRange('S')[1] ? at(5) : at(4), A: at(4), T: at(3), B: at(2) >= ccRange('B')[0] ? at(2) : at(3) }; };
const CC_ROLE = { root: ['root', '근음'], third: ['3rd', '3음'], fifth: ['5th', '5음'] };
const CC_STARS = [['root', 'Root position', '기본 위치'], ['first', 'First inversion', '제1전위'], ['all', 'I, IV and V all sung', 'I, IV, V 모두 노래하기']];
const ccRom = (deg) => ({ 1: 'I', 4: 'IV', 5: 'V' }[deg]);
function ChoirChord() {
  const T = useSpTimers();
  const [k, setK] = useState('C'), [deg, setDeg] = useState(1), [vs, setVs] = useState(() => ccStart('C', 1)), [hi, setHi] = useState(null);
  const [stars, setStars] = useState(() => { try { return JSON.parse(localStorage.getItem('pb_mk_choir')) || {}; } catch (e) { return {}; } });
  const choose = (kk, dg) => { T.clear(); setHi(null); setK(kk); setDeg(dg); setVs(ccStart(kk, dg)); };
  const move = (v, by) => { const [lo, top] = ccRange(v), d = vs[v] + by; if (d < lo || d > top) return; T.clear(); const n = { ...vs, [v]: d }; setVs(n); setHi({ i: 0, v }); playKey(h3Semi(ccNote(k, d)), 0.5); };
  const rootL = ccRootL(k, deg), tones = [0, 2, 4].map(x => H3_L[(rootL + x) % 7]), roles = CC_V.map(v => ccRole(k, deg, vs[v]));
  const wrongV = CC_V.filter((v, j) => !roles[j]), order = CC_V.findIndex((v, j) => j < 3 && vs[v] < vs[CC_V[j + 1]]), missing = ['root', 'third', 'fifth'].filter(r => !roles.includes(r));
  const ok = !wrongV.length && order < 0 && !missing.length, bass = roles[3];
  const tn = (r) => h3Let(ccNote(k, rootL + { root: 0, third: 2, fifth: 4 }[r]));
  const sing = () => { T.clear(); const ns = CC_V.map(v => h3Semi(ccNote(k, vs[v]))), ev = [3, 2, 1, 0].map((j, x) => ({ at: x * 0.7, keys: [ns[j]], len: 0.6, vol: 0.12 })).concat([{ at: 3, keys: ns, len: 2.2, vol: 0.1 }]);
    const r = spPlay(ev, 60); if (!r) return; [3, 2, 1, 0].forEach((j, x) => T.at(r.ms(x * 0.7), () => setHi({ i: 0, v: CC_V[j] }))); T.at(r.ms(3), () => setHi(null));
    if (ok && (bass === 'root' || bass === 'third')) { const n = { ...stars, [bass === 'root' ? 'root' : 'first']: 1, ['d' + deg]: 1 }; if (n.d1 && n.d4 && n.d5) n.all = 1; setStars(n); try { localStorage.setItem('pb_mk_choir', JSON.stringify(n)); } catch (e) {} } };
  const msg = wrongV.length ? t('The ' + H3_VOICE[wrongV[0]][0] + ' sings ' + h3Let(ccNote(k, vs[wrongV[0]])) + ': not in the chord (' + tones.join(' ') + ').', H3_VOICE[wrongV[0]][1] + '는 ' + h3Let(ccNote(k, vs[wrongV[0]])) + ': 화음의 음이 아니에요 (' + tones.join(' ') + ').')
    : order >= 0 ? t('The ' + H3_VOICE[CC_V[order + 1]][0] + ' is above the ' + H3_VOICE[CC_V[order]][0] + ': from the top, soprano, alto, tenor, bass.', H3_VOICE[CC_V[order + 1]][1] + '가 ' + H3_VOICE[CC_V[order]][1] + '보다 높아요: 위에서부터 소프라노, 알토, 테너, 베이스.')
    : missing.length ? t('Nobody sings the ' + missing.map(r => CC_ROLE[r][0] + ' (' + tn(r) + ')').join(' or the ') + ' yet.', '아직 아무도 ' + missing.map(r => CC_ROLE[r][1] + '(' + tn(r) + ')').join(', ') + '을 부르지 않아요.')
    : bass === 'root' ? t('A full chord in root position: the root in the bass.', '기본 위치의 완전한 화음: 베이스에 근음.') : bass === 'third' ? t('A full chord in first inversion: the 3rd in the bass.', '제1전위의 완전한 화음: 베이스에 3음.')
    : t('A full chord, but with the 5th in the bass: that one is for later. Give the bass the root or the 3rd.', '완전한 화음이지만 베이스에 5음: 그건 나중에 배워요. 베이스에 근음이나 3음을 줘요.');
  return (
    <div className="try-box" style={actBox} data-mk="choir">
      <div style={actTitle}>{t('Fill the choir', '합창단 채우기')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>합창단 네 사람이 모두 같은 음을 부르고 있어요. ▲▼로 한 사람씩 음을 바꿔 <b>화음의 세 음이 모두</b> 들리게 해요. 위에서부터 소프라노, 알토, 테너, 베이스 순서로!</> : <>All four singers are on the same note. Move them one by one with ▲▼ until <b>all three notes of the chord</b> are sung. From the top: soprano, alto, tenor, bass!</>}</div>
      <div style={{display:'flex',gap:'4px 12px',justifyContent:'center',flexWrap:'wrap',margin:'0 0 6px'}}>{CC_STARS.map(([id, en, ko]) => <span key={id} style={{fontSize:12.5,fontWeight:800,color:stars[id] ? BK.coral : BK.muted}}>{stars[id] ? '★' : '☆'} {t(en, ko)}</span>)}</div>
      {spChips(CC_KEYS.map(x => [x, t(H3_TRI[x].en, H3_TRI[x].ko)]), k, (x) => choose(x, deg))}
      {spChips(CC_DEG.map(([dg, ni]) => [dg, ccRom(dg) + ' · ' + h3DegName(ni)]), deg, (x) => choose(k, x))}
      <div style={{maxWidth:240,margin:'0 auto'}}><SatbStaff chords={[{ S: ccNote(k, vs.S), A: ccNote(k, vs.A), T: ccNote(k, vs.T), B: ccNote(k, vs.B) }]} ks={H3_CAD[k].ks} labels={[ccRom(deg)]} width={200} hi={hi}/></div>
      <div style={{display:'flex',flexDirection:'column',gap:4,alignItems:'center',margin:'4px 0'}}>{CC_V.map((v, j) => { const r = roles[j], [lo, top] = ccRange(v);
        return <div key={v} style={{display:'flex',alignItems:'center',gap:6}}>
          <span style={{width:72,textAlign:'right',fontWeight:900,fontSize:13,color:BK.ink}}>{h3Voice(v)}</span>
          <button className="ghost-btn" style={{minWidth:40,minHeight:36,padding:0}} disabled={vs[v] <= lo} onClick={() => move(v, -1)}>▼</button>
          <span style={{width:40,textAlign:'center',fontWeight:900,fontSize:18,color:r ? BK.ink : BK.coral}}>{h3Let(ccNote(k, vs[v]))}</span>
          <button className="ghost-btn" style={{minWidth:40,minHeight:36,padding:0}} disabled={vs[v] >= top} onClick={() => move(v, 1)}>▲</button>
          <span style={{width:52,fontSize:11.5,fontWeight:900,color:r ? BK.green : BK.coral}}>{r ? t(CC_ROLE[r][0], CC_ROLE[r][1]) : '✗'}</span></div>; })}</div>
      {spMsg(msg, ok && (bass === 'root' || bass === 'third') ? BK.green : ok ? undefined : BK.coral)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        <button className="primary-btn" style={spBtn} onClick={sing}>{t('▶ Sing!', '▶ 노래해요!')}</button>
        <button className="ghost-btn" style={spBtn} onClick={() => choose(k, deg)}>{t('↻ Start again', '↻ 처음부터')}</button>
      </div>
    </div>
  );
}

// ── Rhythm further: Split the beat. Two bars of 4/4; each beat splits one of seven ways (the room's semiquavers, the dotted
// quaver and semiquaver, the triplet). Counted 1 e + a, and 1 trip let for the triplet. ──
const BS_KINDS = [['q', '1', 'crotchet', '4분음표'], ['p', '1 +', 'two quavers', '8분음표 둘'], ['s4', '1 e + a', 'four semiquavers', '16분음표 넷'], ['es', '1 + a', 'quaver, two semiquavers', '8분음표, 16분음표 둘'], ['se', '1 e +', 'two semiquavers, quaver', '16분음표 둘, 8분음표'], ['ds', '1 a', 'dotted quaver, semiquaver', '점8분음표, 16분음표'], ['t3', '1 trip let', 'triplet', '셋잇단음표']];
const bsCount = (p) => { const f = p - Math.floor(p + 1e-6); return Math.abs(f - 1 / 3) < 0.02 ? 'trip' : Math.abs(f - 2 / 3) < 0.02 ? 'let' : srhCount(p); };
const BS_STARS = [['trip', 'Use a triplet', '셋잇단음표 쓰기'], ['dot', 'Use the dotted one', '점 리듬 쓰기'], ['all', 'All seven in two bars', '두 마디에 일곱 가지 모두']];
function BeatSplit() {
  const [c, setC] = useState(['q', 'p', 's4', 'q', 'ds', 'ds', 't3', 'q']), [bpm, setBpm] = useState(66);
  const [stars, setStars] = useState(() => { try { return JSON.parse(localStorage.getItem('pb_mk_split')) || {}; } catch (e) { return {}; } });
  const items = [['ts', 4]].concat(c.slice(0, 4).map(k => [k]), [['|']], c.slice(4).map(k => [k]), [['||']]);
  const flip = (j) => { const n = c.slice(); n[j] = BS_KINDS[(BS_KINDS.findIndex(x => x[0] === n[j]) + 1) % BS_KINDS.length][0]; setC(n);
    const s2 = { ...stars }; if (n.includes('t3')) s2.trip = 1; if (n.includes('ds')) s2.dot = 1; if (BS_KINDS.every(x => n.includes(x[0]))) s2.all = 1;
    if (Object.keys(s2).length !== Object.keys(stars).length) { setStars(s2); try { localStorage.setItem('pb_mk_split', JSON.stringify(s2)); } catch (e) {} } };
  const cell = (j) => { const K = BS_KINDS.find(x => x[0] === c[j]);
    return <button key={j} className="choice-btn" onClick={() => flip(j)} style={{flex:1,minWidth:0,padding:'6px 1px',display:'flex',flexDirection:'column',alignItems:'center',gap:2,lineHeight:1.15}}>
      <span style={{fontSize:13,fontWeight:900,color:BK.coral,whiteSpace:'nowrap'}}>{K[1].replace('1', String(j % 4 + 1))}</span><span style={{fontSize:9.5,fontWeight:800,color:BK.muted}}>{t(K[2], K[3])}</span></button>; };
  return (
    <div className="try-box" style={actBox} data-mk="split">
      <div style={actTitle}>{t('Split the beat', '박 쪼개기')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>4/4 두 마디. 박을 누를 때마다 <b>쪼개는 방법</b>이 바뀌어요: 하나 그대로, 둘, 넷, 길게 짧게, 셋잇단까지 일곱 가지. 듣고, 쳐 보고, 빠르게도!</> : <>Two bars of 4/4. Tap a beat to <b>split it a new way</b>: whole, in two, in four, long-short, in three… seven ways. Listen, tap it back, then speed up!</>}</div>
      <div style={{display:'flex',gap:'4px 12px',justifyContent:'center',flexWrap:'wrap',margin:'0 0 6px'}}>{BS_STARS.map(([id, en, ko]) => <span key={id} style={{fontSize:12.5,fontWeight:800,color:stars[id] ? BK.coral : BK.muted}}>{stars[id] ? '★' : '☆'} {t(en, ko)}</span>)}</div>
      <RqStaff key={c.join() + bpm} items={items} bpm={bpm} so={{ countFn: bsCount }}/>
      {[0, 1].map(b => <div key={b} style={{display:'flex',gap:4,margin:'4px 0'}}>{[0, 1, 2, 3].map(x => cell(b * 4 + x))}</div>)}
      {spChips([[56, t('Slow', '느리게')], [66, t('Moderate', '보통')], [80, t('Fast', '빠르게')]], bpm, setBpm)}
    </div>
  );
}
'''
rep("// ══ Build BH: Blues jam ══", CODE + "\n// ══ Build BH: Blues jam ══")
rep("""  { id: 'mk-exam', ch: 'listen-sing',""", """  { id: 'mk-pianist', ch: 'posture-hands', title: 'Fix the pianist', blurb: 'A pianist set up all wrong: fix the stool, the sitting and the hand. Fewer tries, more stars.', C: () => <PianistFix/> },   // Build CH
  { id: 'mk-ways', ch: 'note-values', title: 'Ways to make four beats', blurb: 'Notes and rests that add up to four beats: how many different ways can you find?', C: () => <BeatWays/> },
  { id: 'mk-hidden', ch: 'listen-23', title: 'The tune on top', blurb: 'A chain of two-note chords hides a tune on top: can someone hum it?', C: () => <HiddenTune/> },
  { id: 'mk-duel', ch: 'listen-3', title: 'Ear duel', blurb: 'Two players take turns setting each other Grade 3 ear questions. First to five wins.', C: () => <EarDuel/> },
  { id: 'mk-melmin', ch: 'scales-23', title: 'My melodic minor tune', blurb: 'A tune in a minor key: going up, the 6th and 7th rise; coming down, they go back.', C: () => <MelMinorTune/> },
  { id: 'mk-choir', ch: 'harmony-23', title: 'Fill the choir', blurb: 'Soprano, alto, tenor and bass, one note each: every note of the chord, in order.', C: () => <ChoirChord/> },
  { id: 'mk-split', ch: 'rhythm-23', title: 'Split the beat', blurb: 'Two bars of 4/4, each beat split one of seven ways, from semiquavers to triplets. Then tap it.', C: () => <BeatSplit/> },
  { id: 'mk-exam', ch: 'listen-sing',""")
rep("""  'mk-exam': ['시험관 되기',""", """  'mk-pianist': ['피아니스트 고치기', '엉망으로 앉은 피아니스트: 의자, 앉는 자리, 손 모양을 고쳐요. 덜 물어볼수록 별이 많아요.'],
  'mk-ways': ['4박을 만드는 방법', '음표와 쉼표로 딱 4박: 서로 다른 방법을 몇 가지나 찾을 수 있을까요?'],
  'mk-hidden': ['위에 숨은 선율', '두 음 화음을 이어 붙이면 위에 선율이 숨어 있어요: 누가 흥얼거릴 수 있을까요?'],
  'mk-duel': ['귀 대결', '두 사람이 번갈아 Grade 3 청음 문제를 내요. 먼저 5점이면 승리.'],
  'mk-melmin': ['나의 가락 단음계 선율', '단조 선율: 올라갈 때 6도와 7도가 올라가고, 내려올 때 원래대로.'],
  'mk-choir': ['합창단 채우기', '소프라노, 알토, 테너, 베이스에 한 음씩: 화음의 모든 음을, 순서대로.'],
  'mk-split': ['박 쪼개기', '4/4 두 마디, 박마다 일곱 가지로 쪼개요. 16분음표부터 셋잇단음표까지. 그리고 쳐 봐요.'],
  'mk-exam': ['시험관 되기',""")
rep("""'mk-e8': ['rpulse', 1, 1, 'game ear'],""", """'mk-e8': ['rpulse', 1, 1, 'game ear'], 'mk-pianist': ['body', 0, 1, 'game'], 'mk-ways': ['rnotes', 0, 1, 'game ear'], 'mk-hidden': ['steps', 1, 2, 'game ear'], 'mk-duel': ['steps', 1, 2, 'game ear'], 'mk-melmin': ['scales', 1, 2, 'game ear'], 'mk-choir': ['chords', 1, 2, 'game ear'], 'mk-split': ['rrhythm', 1, 2, 'game ear'],""")
rep("""'mk-e8': 'r-beat',""", """'mk-e8': 'r-beat', 'mk-pianist': 'k-posture', 'mk-ways': 'r-beat', 'mk-hidden': 'aural', 'mk-duel': 'aural', 'mk-melmin': 'k-play', 'mk-choir': 'p-chords', 'mk-split': 'r-beat',""")
rep("""  'mk-exam': () => (\n""", """  'mk-pianist': () => (
    <svg width="34" height="34" viewBox="0 0 24 24"><rect width="24" height="24" rx="6" fill="#3b4fa8"/><rect x="16" y="5" width="5" height="15" rx="1" fill="#fefbf3"/><rect x="14" y="11" width="3" height="2" fill="#fefbf3"/><circle cx="9" cy="6" r="2.2" fill="#fefbf3"/><path d="M9 8.5 L9.6 14 M9.4 10.5 L13.5 11.5" stroke="#fefbf3" strokeWidth="1.6" strokeLinecap="round"/><rect x="5" y="14" width="7" height="1.6" rx="0.6" fill="#e9a83a"/><path d="M6 15.6 V20 M11 15.6 V20" stroke="#e9a83a" strokeWidth="1.2"/></svg>
  ),
  'mk-ways': () => (
    <svg width="34" height="34" viewBox="0 0 24 24"><rect width="24" height="24" rx="6" fill="#2e8a6e"/>{[0, 1, 2, 3].map(i => <rect key={i} x={3.5 + i * 4.5} y="15" width="3.6" height="4" rx="1" fill={i < 3 ? '#fefbf3' : 'none'} stroke="#fefbf3" strokeWidth="0.9"/>)}<ellipse cx="7" cy="10" rx="2" ry="1.4" fill="#e9a83a"/><path d="M8.8 10 V4" stroke="#e9a83a" strokeWidth="1.1"/><ellipse cx="15" cy="10" rx="2" ry="1.4" fill="none" stroke="#e9a83a" strokeWidth="1.1"/><path d="M16.8 10 V4" stroke="#e9a83a" strokeWidth="1.1"/></svg>
  ),
  'mk-hidden': () => (
    <svg width="34" height="34" viewBox="0 0 24 24"><rect width="24" height="24" rx="6" fill="#7a4f96"/>{[[5, 9, 15], [9, 7, 15], [13, 6, 13], [17, 8, 15]].map(([x, a, b]) => <g key={x}><circle cx={x} cy={a} r="1.8" fill="#e9a83a"/><circle cx={x} cy={b} r="1.8" fill="#fefbf3"/></g>)}</svg>
  ),
  'mk-duel': () => (
    <svg width="34" height="34" viewBox="0 0 24 24"><rect width="24" height="24" rx="6" fill="#e4572e"/><text x="12" y="15.5" textAnchor="middle" fontFamily="Georgia, serif" fontSize="9" fontWeight="900" fill="#fefbf3">VS</text><circle cx="4.5" cy="12" r="1.6" fill="#e9a83a"/><circle cx="19.5" cy="12" r="1.6" fill="#e9a83a"/></svg>
  ),
  'mk-melmin': () => (
    <svg width="34" height="34" viewBox="0 0 24 24"><rect width="24" height="24" rx="6" fill="#3b4fa8"/>{[0, 1, 2, 3, 4].map(i => <rect key={i} x={3 + i * 3.6} y={17 - i * 2.6} width="3" height="2" rx="0.6" fill={i === 2 || i === 3 ? '#e9a83a' : '#fefbf3'}/>)}<path d="M20 9 V4 M18 6 L20 4 L22 6" stroke="#e9a83a" strokeWidth="1.3" fill="none"/></svg>
  ),
  'mk-choir': () => (
    <svg width="34" height="34" viewBox="0 0 24 24"><rect width="24" height="24" rx="6" fill="#2e8a6e"/>{[5, 8, 11, 14].map((y, i) => <line key={i} x1="3" x2="21" y1={y} y2={y} stroke="#fefbf3" strokeWidth="0.6" opacity="0.6"/>)}{[6.5, 9.5, 15.5, 18.5].map((y, i) => <ellipse key={i} cx="12" cy={y} rx="2.4" ry="1.6" fill={i === 3 ? '#e9a83a' : '#fefbf3'}/>)}{[17, 20].map((y, i) => <line key={'b' + i} x1="3" x2="21" y1={y} y2={y} stroke="#fefbf3" strokeWidth="0.6" opacity="0.6"/>)}</svg>
  ),
  'mk-split': () => (
    <svg width="34" height="34" viewBox="0 0 24 24"><rect width="24" height="24" rx="6" fill="#e4572e"/><rect x="3" y="4" width="18" height="3.2" rx="1.2" fill="#fefbf3"/><rect x="3" y="10" width="8.6" height="3.2" rx="1.2" fill="#fefbf3"/><rect x="12.4" y="10" width="8.6" height="3.2" rx="1.2" fill="#fefbf3"/>{[0, 1, 2, 3].map(i => <rect key={i} x={3 + i * 4.6} y="16" width="3.8" height="3.2" rx="1.2" fill="#e9a83a"/>)}</svg>
  ),
  'mk-exam': () => (\n""")
rep("""  'k-posture': { lessons: ['kp-sit', 'kp-arm', 'kp-hand', 'kp-fingers', 'kp-walks', 'kp-check'], check: 'posture-hands' },""", """  'k-posture': { lessons: ['kp-sit', 'kp-arm', 'kp-hand', 'kp-fingers', 'kp-walks', 'kp-check', 'mk-pianist'], check: 'posture-hands' },""")
rep("""lessons: ['rn-q', 'rn-h', 'rn-long', 'rn-p', 'rn-rest'], check: 'note-values' },""", """lessons: ['rn-q', 'rn-h', 'rn-long', 'rn-p', 'rn-rest', 'mk-ways'], check: 'note-values' },""")
rep("""lessons: ['l2-dyad', 'l2-clap2', 'l2-sing'], check: 'listen-23' },""", """lessons: ['l2-dyad', 'l2-clap2', 'l2-sing', 'mk-hidden'], check: 'listen-23' },""")
rep("""lessons: ['l2-any', 'l2-deg', 'lw-metre', 'l2-clap', 'l3-sing'], check: 'listen-3' },""", """lessons: ['l2-any', 'l2-deg', 'lw-metre', 'l2-clap', 'l3-sing', 'mk-duel'], check: 'listen-3' },""")
rep("""lessons: ['scf-thumb', 'scf-meet', 'scf-mel', 'scf-mirror', 'scf-chrom'], check: 'scales-23' },""", """lessons: ['scf-thumb', 'scf-meet', 'scf-mel', 'scf-mirror', 'scf-chrom', 'mk-melmin'], check: 'scales-23' },""")
rep("""lessons: ['h3-iv', 'h3-deg', 'h3-inv', 'h3-satb', 'h3-cad'], check: 'harmony-23' },""", """lessons: ['h3-iv', 'h3-deg', 'h3-inv', 'h3-satb', 'h3-cad', 'mk-choir'], check: 'harmony-23' },""")
rep("""lessons: ['r2-semi', 'r2-dot', 'r2-trip', 'r2-minim', 'r2-98'], check: 'rhythm-23' },""", """lessons: ['r2-semi', 'r2-dot', 'r2-trip', 'r2-minim', 'r2-98', 'mk-split'], check: 'rhythm-23' },""")
rep("""  set('P1', 'mk-exam mk-keytune mk-remix'); set('1', 'mk-hang mk-e8');   // Build CG""", """  set('P1', 'mk-exam mk-keytune mk-remix'); set('1', 'mk-hang mk-e8');   // Build CG
  set('G', 'mk-pianist mk-ways'); set('23', 'mk-hidden mk-duel mk-melmin mk-choir mk-split');   // Build CH""")
rep("""  'note-values': ['nv-walk', 'nv-hold', 'nv-long', 'nv-run', 'nv-rests', 'count-aloud', 'note-value-tree', 'note-rest-match', 'split-it'],""", """  'note-values': ['nv-walk', 'nv-hold', 'nv-long', 'nv-run', 'nv-rests', 'count-aloud', 'note-value-tree', 'note-rest-match', 'split-it', 'mk-ways'],""")
rep("""  'posture-hands': ['sit-check', 'arm-moves', 'arm-alignment', 'hand-shape', 'finger-friends', 'finger-numbers', 'posture-check'],""", """  'posture-hands': ['sit-check', 'arm-moves', 'arm-alignment', 'hand-shape', 'finger-friends', 'finger-numbers', 'posture-check', 'mk-pianist'],""")

open(dst, 'w', encoding='utf-8').write(s)
print('ok')
