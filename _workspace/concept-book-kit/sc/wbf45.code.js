// Build EG (her 1 Nov 10:39 and 14:37): the Prelim Workbooks, fun first -- only the parts better changed, each swapped
// for a game that practises the same thing, none added.

// Chapter 17, Ledger Lines, page 2: PLAY counted the same ladders YOUR TURN had just drawn. Now the ladder race: a track
// of 14 squares, a note without its ladders on each of the first 13. Write how many ladders each note needs; then from
// square 1 move that many squares each time. The right counts land exactly on the flag (square 14); from any square off
// the path the counts overshoot it, so the flag checks the counting. Notes from the room's own (the sky, the sea and
// between the staves: 1 to 3 ladders). Path 1 3 6 7 9 12, then the flag.
const LL_RACE = [['treble', 42], ['bass', 13], ['treble', 44], ['bass', 15], ['bass', 12], ['treble', 28], ['bass', 14], ['treble', 43], ['treble', 44], ['bass', 29], ['treble', 26], ['bass', 30], ['bass', 12]];
const llRaceRun = (from) => { const out = []; let s = from; while (s < LL_RACE.length) { out.push(s); s += llRungCount(...LL_RACE[s]); } return { path: out, end: s }; };
const llRacePath = () => llRaceRun(0).path;
function LlRaceSq({ i }) {
  const flag = i === LL_RACE.length, sq = LL_RACE[i];
  return <div style={{position:'relative',height:100,border:'1px solid rgba(38,41,107,0.32)',borderRadius:3,background:i % 2 ? 'rgba(38,41,107,0.055)' : '#fff',display:'flex',flexDirection:'column',alignItems:'center',justifyContent:'space-between',padding:'12px 2px 4px',minWidth:0}} data-race={i}>
    <span style={{position:'absolute',top:1,left:5,fontFamily:LB_SERIF,fontStyle:'italic',fontWeight:700,fontSize:13,color:BK.muted}}>{i + 1}</span>
    {i === 0 && <span style={{position:'absolute',top:0,right:4,fontSize:10,fontWeight:900,color:BK.coral,letterSpacing:'0.04em'}}>★ start</span>}
    {flag
      ? <svg viewBox="0 0 40 60" style={{width:40,margin:'auto'}}><line x1="12" y1="6" x2="12" y2="56" stroke={BK.ink} strokeWidth="2.4"/><path d="M12 6 L36 14 L12 22 Z" fill={BK.coral}/><line x1="4" y1="56" x2="22" y2="56" stroke={BK.ink} strokeWidth="2.4"/></svg>
      : <><div style={{width:58,flex:'1 1 auto',display:'flex',alignItems:'center'}}><PaperStaff clef={sq[0]} notes={[{ d: sq[1], rungs: [] }]} width={92} guides={sq[1] > CLEFS[sq[0]].high ? [3, 0] : [0, 3]}/></div>
        <span style={{flex:'0 0 auto',display:'flex'}}>{nvBox(i === 0, String(llRungCount(...sq)), 32, 22)}</span></>}
  </div>;
}
function LlRace() {
  const N = LL_RACE.length + 1, top = Array.from({ length: 7 }, (_, i) => i), low = Array.from({ length: N - 7 }, (_, i) => N - 1 - i);
  return <div style={{display:'grid',gap:4}}>
    <div style={{display:'grid',gridTemplateColumns:'repeat(7, 1fr)',gap:6}}>{top.map(i => <LlRaceSq key={i} i={i}/>)}</div>
    <div style={{display:'grid',gridTemplateColumns:'repeat(7, 1fr)',gap:6}}><span style={{gridColumn:7,textAlign:'center',color:BK.coral,fontSize:13,fontWeight:900,lineHeight:1}}>↓</span></div>
    <div style={{display:'grid',gridTemplateColumns:'repeat(7, 1fr)',gap:6}}>{low.map(i => <LlRaceSq key={i} i={i}/>)}</div>
  </div>;
}

// A plain keyboard for the Workbook games: white keys lo..hi (semitones from middle C = 0), keys in `lit` pale, letters on
// the keys in `names`, and extra marks drawn by `draw(kx, top, H)`.
const kbIsW = (s) => [0, 2, 4, 5, 7, 9, 11].includes(((s % 12) + 12) % 12);
const kbWIdx = (s) => Math.floor(s / 12) * 7 + [0, 0, 1, 1, 2, 3, 3, 4, 4, 5, 5, 6][((s % 12) + 12) % 12];
function WbKb({ lo, hi, w = 30, h = 92, top = 6, below = 6, lit = new Set(), names = {}, draw, width }) {
  const w0 = kbWIdx(lo), nw = kbWIdx(hi) - w0 + 1, bw = w * 0.6, bh = h * 0.6, W = nw * w + 4;
  const kx = (s) => 2 + (kbWIdx(s) - w0 + (kbIsW(s) ? 0.5 : 1)) * w, keys = []; for (let s = lo; s <= hi; s++) keys.push(s);
  return <svg viewBox={'0 0 ' + W + ' ' + (top + h + below)} style={{width:width || W,maxWidth:'100%',display:'block'}}>
    {keys.filter(kbIsW).map(s => <rect key={'w' + s} x={2 + (kbWIdx(s) - w0) * w} y={top} width={w} height={h} rx="2" fill={lit.has(s) ? '#fbe3da' : '#fff'} stroke={BK.ink} strokeWidth="1.2"/>)}
    {keys.filter(s => !kbIsW(s)).map(s => <g key={'b' + s}><rect x={kx(s) - bw / 2} y={top} width={bw} height={bh} rx="1.5" fill={BK.ink}/>{lit.has(s) && <circle cx={kx(s)} cy={top + bh - 8} r="3.2" fill={BK.coral}/>}</g>)}
    {keys.map(s => names[s] == null ? null : <text key={'n' + s} x={kx(s)} y={kbIsW(s) ? top + h - 8 : top + bh - 15} textAnchor="middle" fontSize={kbIsW(s) ? 12 : 8.5} fontWeight="900" fill={kbIsW(s) ? BK.ink : '#fff'} style={{fontFamily:'Inter, sans-serif'}}>{names[s]}</text>)}
    {draw && draw(kx, top, h)}
  </svg>;
}
const wbTick = (label) => <span style={{display:'inline-flex',alignItems:'center',gap:6,fontSize:12,fontWeight:800,color:BK.ink,whiteSpace:'nowrap'}}><span style={{width:15,height:15,border:'1.5px solid ' + BK.ink,borderRadius:3,background:'#fff'}}/>{label}</span>;
const wbLetterBox = (x, opts = {}) => <span style={{width:opts.w || 30,height:opts.h || 30,boxSizing:'border-box',border:'1.5px solid ' + (opts.ex ? BK.coral : opts.given ? BK.ink : BK.line),borderRadius:5,display:'inline-flex',alignItems:'center',justifyContent:'center',fontFamily:LB_SERIF,fontSize:(opts.h || 30) * 0.5,fontWeight:800,fontStyle:opts.ex ? 'italic' : 'normal',color:opts.ex ? BK.coral : BK.ink,background:'#fff'}}>{x}</span>;

// Chapter 19, Playing Scales, page 3: PLAY was sums ("at 76, more or less than 15 seconds?"). Now the four-bar scale: one
// note a beat, up and back, the last note held for two beats (the room's own way) -- 15 notes and the hold fill four bars
// of four beats exactly, so the boxes check the counting. Then play it at 60.
const spFourBar = (k) => { const up = spNames(k, 1); return up.concat(up.slice(0, 7).reverse()).concat(['–']); };
function SpFourBars({ k, n, ex }) {
  const seq = spFourBar(k);
  return <div style={{display:'grid',gridTemplateColumns:'84px auto',alignItems:'end',gap:8,justifyContent:'center'}}>
    <span style={{display:'flex',alignItems:'center',gap:8,fontFamily:LB_SERIF,fontSize:15,fontWeight:800,color:BK.ink,paddingBottom:6}}>{nvNum(n)} {SP_SC[k].en}</span>
    <div style={{display:'flex',alignItems:'flex-end'}}>{[0, 1, 2, 3].map(b => <div key={b} style={{display:'flex',alignItems:'flex-end',padding:'0 5px',borderRight:'1.6px solid ' + BK.ink,borderLeft:b === 0 ? '1.6px solid ' + BK.ink : 'none'}}>
      {[0, 1, 2, 3].map(j => <div key={j} style={{display:'grid',justifyItems:'center',gap:2,margin:'0 2px'}}><span style={{fontSize:9.5,fontWeight:800,color:BK.muted}}>{j + 1}</span>{wbLetterBox(ex && b === 0 && j === 0 ? seq[0] : '', { ex: ex && b === 0 && j === 0, w: 26, h: 36 })}</div>)}</div>)}</div>
  </div>;
}
function SpFourBarPlay() {
  return <div style={{display:'grid',gap:26,justifyItems:'center',padding:'4px 0'}}>
    <SpFourBars k="C" n={5} ex/><SpFourBars k="G" n={6}/>
    <div style={{display:'flex',gap:22,flexWrap:'wrap',justifyContent:'center'}}>{wbTick('C major at 60')}{wbTick('G major at 60')}{wbTick('both at 76')}</div>
  </div>;
}

// Chapter 20, Minor Scales, page 3: PLAY matched the same four pairs YOUR TURN had just written. Now the twins at the
// piano: a major key and its minor twin share a key signature, so the natural minor plays the same keys from another
// home. The keys lit, a navy bracket over the major scale and a red one under the minor; play both, hear the twin.
const MS_TWINS = [['C', 'Am', 0, -3], ['G', 'Em', 7, 4], ['F', 'Dm', 5, 2]];   // [major, its natural minor twin, the major's home, the twin's home]
function MsTwinRow({ tw }) {
  const [M, m, hM, hm] = tw, S = SP_SC[M], lit = new Set(), names = {}, lo = hm, hi = hM + 12;
  for (let s = lo; s <= hi; s++) { const j = S.steps.indexOf(((s - hM) % 12 + 12) % 12); if (j >= 0) { lit.add(s); names[s] = S.nm[j]; } }
  const br = (kx, a, b, y, c, up) => <path d={'M' + (kx(a) - 6) + ' ' + (y + (up ? 6 : -6)) + ' V' + y + ' H' + (kx(b) + 6) + ' V' + (y + (up ? 6 : -6))} fill="none" stroke={c} strokeWidth="2"/>;
  return <div style={{display:'grid',gridTemplateColumns:'118px auto 1fr',alignItems:'center',gap:14}}>
    <div style={{display:'grid',gap:4,fontFamily:LB_SERIF,fontSize:15,fontWeight:800,lineHeight:1.15}}><span style={{color:BK.ink}}>{S.en}</span><span style={{color:BK.coral}}>{SP_SC[m].en.replace('natural ', '')}</span></div>
    <WbKb lo={lo} hi={hi} w={30} h={84} top={22} below={22} lit={lit} names={names} width={310}
      draw={(kx, top, h) => <g>{br(kx, hM, hM + 12, top - 10, BK.ink, true)}{br(kx, hm, hm + 12, top + h + 10, BK.coral, false)}
        <text x={kx(hM)} y={top - 13} textAnchor="middle" fontSize="13" fill={BK.ink}>★</text><text x={kx(hm)} y={top + h + 21} textAnchor="middle" fontSize="13" fill={BK.coral}>★</text></g>}/>
    <div style={{display:'grid',gap:8}}>{wbTick('major, up and down')}{wbTick('minor, up and down')}</div>
  </div>;
}
const MsTwinsPlay = () => <div style={{display:'grid',gap:14,justifyItems:'center',padding:'4px 0'}}>{MS_TWINS.map(tw => <MsTwinRow key={tw[0]} tw={tw}/>)}</div>;

// Chapter 20, Minor Scales, page 5: PLAY asked for the code of steps "from memory" with the answer in the boxes above.
// Now the step trail of chapter 13, with the tone and a half: from the star on E, T S T T S T½ S (the room's harmonic
// minor steps); the seventh step lands on the flag, so the flag checks the trail. Then name the scale: E harmonic minor.
const MS_TRAIL = { m: 'E', home: 4, nm: 'Emh' };
const msTrailMoves = () => SP_HAR.concat([12]).slice(1).map((x, i) => x - SP_HAR[i]);
const msTrailKeys = () => SP_HAR.concat([12]).slice(1).map(x => MS_TRAIL.home + x);
const MS_STEP = { 1: 'S', 2: 'T', 3: 'T½' };
function MsTrail() {
  const lo = MS_TRAIL.home, hi = MS_TRAIL.home + 12, end = hi;
  const slots = (kx, top, h) => { const out = []; for (let s = lo + 1; s <= hi; s++) out.push(<circle key={s} cx={kx(s)} cy={kbIsW(s) ? top + h - 17 : top + h * 0.6 - 13} r={kbIsW(s) ? 12 : 10} fill={kbIsW(s) ? 'none' : '#fff'} stroke={BK.ink} strokeWidth="0.9" strokeOpacity={kbIsW(s) ? 0.45 : 0}/>); return out; };
  return <div style={{display:'grid',gap:18,justifyItems:'center',padding:'0 6px'}}>
    <WbKb lo={lo} hi={hi} w={52} h={104} top={32} below={4} width={470} draw={(kx, top, h) => <g>{slots(kx, top, h)}
      <text x={kx(lo)} y={top + h - 9} textAnchor="middle" fontSize="24" fill={BK.coral}>★</text>
      <text x={kx(lo)} y={top - 10} textAnchor="middle" fontSize="12" fontWeight="900" fill={BK.coral}>start</text>
      <g transform={'translate(' + kx(end) + ' ' + (top - 4) + ')'}><line x1="0" y1="0" x2="0" y2="-26" stroke={BK.ink} strokeWidth="1.8"/><path d="M0 -26 L16 -21 L0 -16 Z" fill={BK.coral}/></g></g>}/>
    <div style={{display:'flex',flexWrap:'wrap',gap:'8px 22px',justifyContent:'center',alignItems:'center'}}>{msTrailMoves().map((n, i) => <span key={i} style={{display:'inline-flex',alignItems:'center',gap:7,fontSize:14,fontWeight:800,color:BK.ink,whiteSpace:'nowrap'}}>
      <span style={{fontFamily:LB_SERIF,fontStyle:'italic',fontWeight:700,fontSize:15}}>{i + 1}</span>{MS_STEP[n]} up</span>)}</div>
    <span style={{display:'inline-flex',alignItems:'center',gap:8,fontSize:14,fontWeight:800,color:BK.ink}}>The scale: {bkBox(50, 32)} harmonic minor</span>
  </div>;
}

// Chapter 20, Minor Scales, page 6: YOUR TURN needed someone at home to play the scales. Now the same tune, darker: the
// tunes of Hand Positions (Hot cross buns, Mary had a little lamb: the steps from MT_SONGS) in a major key; the child
// writes the same steps in its minor twin and plays both -- the minor third makes it darker. Alone, by ear. The tunes use
// no 7th, so this is the natural minor and the harmonic minor alike: the page says minor.
const MS_TUNES = [[0, 'C', 'Am'], [1, 'C', 'Am'], [1, 'G', 'Em'], [0, 'F', 'Dm']];
const msTuneLetters = (k, steps) => steps.map(d => SP_SC[k].nm[d - 1]);
function MsTuneCard({ tu, n, ex }) {
  const [si, M, m] = tu, steps = MT_SONGS[si][2], bx = { w: 28, h: 28 };
  const row = (label, c, cells) => <div style={{display:'grid',gridTemplateColumns:'64px auto',alignItems:'center',gap:6}}><span style={{fontSize:11.5,fontWeight:900,color:c}}>{label}</span><div style={{display:'flex',gap:3}}>{cells}</div></div>;
  return <ExCell n={n} ex={ex}><div style={{display:'grid',gap:4,padding:'16px 4px 2px'}}>
    <span style={{fontFamily:LB_SERIF,fontStyle:'italic',fontSize:14.5,fontWeight:700,color:BK.ink}}>{MT_SONGS[si][0]}</span>
    {row('steps', BK.muted, steps.map((d, j) => <span key={j} style={{width:bx.w,textAlign:'center',fontSize:11,fontWeight:900,color:BK.muted}}>{d}</span>))}
    {row(SP_SC[M].en, BK.ink, msTuneLetters(M, steps).map((x, j) => <span key={j}>{wbLetterBox(x, { ...bx, given: true })}</span>))}
    {row(SP_SC[m].en.replace('natural ', ''), BK.coral, msTuneLetters(m, steps).map((x, j) => <span key={j}>{wbLetterBox(ex ? x : '', { ...bx, ex })}</span>))}
    <div style={{display:'flex',justifyContent:'flex-end',marginTop:2}}>{wbTick('played both')}</div>
  </div></ExCell>;
}
const MsTunes = () => <BkGrid cols={2} gap="8px 10px">{MS_TUNES.map((tu, i) => <MsTuneCard key={i} tu={tu} n={5 + i} ex={i === 0}/>)}</BkGrid>;

