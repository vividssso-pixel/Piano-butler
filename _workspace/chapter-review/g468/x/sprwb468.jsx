// ─── Phase 468: chapter 12's Workbook (pages 2 to 6 face Lesson Book pages 2 to 6: low, middle and high; big is low;
// the families; low to high; the piano's range; page 7 the check-up on paper) and its Teacher copy. English, like every
// Workbook. Every task set (rule 3) and done alone (rule 4: nothing needs an adult); a word to write is words to circle
// (rule 5); no PLAY task copies its Lesson Book picture. Notes are named by letter only (octave numbers are not taught).
// the 88 keys, small, one key filled (and an arrow over it) or a range shaded
const sprStripSm = (o = {}) => <svg viewBox="0 -14 264 50" style={{width:'100%',display:'block'}}><SprKeys88 x0={2} y0={0} kw={5} h={32} cLabel={false} key1={o.key1} range={o.range} rangeCol="#f3a27c" sw={0.5}/></svg>;
// part of the keyboard, bare, its keys big enough to draw on (lo and hi white keys); middle C named under its key
function SprKeysPart({ lo, hi, x0 = 0, y0 = 0, kw = 16, h = 62, midC = true }) {
  const whites = sprWhites.filter(m => m >= lo && m <= hi), xw = (m) => x0 + whites.indexOf(m) * kw, bw = kw * 0.6;
  const blacks = []; for (let m = lo + 1; m < hi; m++) if (!sprIsWhite(m)) blacks.push(m);
  return <g>
    {whites.map(m => <rect key={m} x={xw(m)} y={y0} width={kw} height={h} fill="#fff" stroke={PEN_N} strokeWidth="0.9"/>)}
    {blacks.map(m => <rect key={m} x={xw(m - 1) + kw - bw / 2} y={y0} width={bw} height={h * 0.6} fill={PEN_N}/>)}
    {midC && whites.includes(60) && <g><path d={'M' + (xw(60) + kw / 2) + ' ' + (y0 + h + 3) + ' l-4 6 l8 0 Z'} fill={PEN_C}/><text x={whites[0] === 60 ? xw(60) : xw(60) + kw / 2} y={y0 + h + 21} textAnchor={whites[0] === 60 ? 'start' : 'middle'} fontSize="12" fontWeight="900" fill={PEN_C}>middle C</text></g>}
  </g>;
}
const sprPairPic = (pid, bigLeft, ring) => { const P = SPR_PAIRS.find(p => p.id === pid);
  return <svg viewBox="0 0 320 180" style={{width:'100%',display:'block'}}>{['left', 'right'].map(side => { const cx = side === 'left' ? 90 : 230, big = (side === 'left') === bigLeft;
    return <g key={side}>{ring && !big && <ellipse cx={cx} cy={92} rx="72" ry="84" fill="none" stroke={PEN_C} strokeWidth="3"/>}{(big ? P.big : P.small)(cx, 92)}</g>; })}</svg>; };
const sprIconSm = (id, size = 64) => <svg viewBox="0 0 60 60" style={{width:size,height:size,display:'block',margin:'0 auto'}}><SprInst id={id}/></svg>;
const sprTick = () => <span style={{display:'inline-block',width:20,height:20,border:'1.5px solid rgba(38,41,107,0.55)',borderRadius:3,background:'#fff',flex:'0 0 auto'}}/>;
const sprTickW = (w, key) => <span key={key || w} style={{display:'flex',alignItems:'center',gap:8}}>{sprTick()}{w}</span>;
const sprBoxN = (txt, coral) => <span style={{display:'inline-flex',alignItems:'center',justifyContent:'center',width:36,height:34,border:'1.5px solid ' + (coral ? BK.coral : 'rgba(38,41,107,0.55)'),borderRadius:3,background:'#fff',color:BK.coral,fontFamily:LB_SERIF,fontStyle:'italic',fontWeight:800,fontSize:18}}>{txt}</span>;
const sprEn = (n) => SPR_RNAME[n] ? SPR_RNAME[n][0] : n;
const SPR_HOW_EN = { strings: 'bow or pluck its strings', woodwind: 'blow across a hole or through a reed', brass: 'buzz your lips into it', percussion: 'hit, shake or scrape it' };
const sprZoneOf = (m) => Object.keys(SPR_ZONE).find(z => SPR_ZONE[z].includes(m));
const sprLower = (pr) => SPR_RANGE(pr[0]).lo < SPR_RANGE(pr[1]).lo ? pr[0] : pr[1];
const sprOrderNums = (list) => list.map(n => 1 + SPR_VFAM.map(v => v.n).indexOf(n));
// the four family words in two rows, far enough apart to circle one (the worked example's ringed in coral)
const sprFamWords = (on, fs = 12.5) => <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',rowGap:12,columnGap:4,marginTop:'auto',paddingTop:6,fontSize:fs,fontWeight:800,color:BK.ink,textAlign:'center'}}>{SPR_FAMS.map(f => <span key={f} style={{justifySelf:'center',border:'1.5px solid ' + (on === f ? BK.coral : 'transparent'),borderRadius:12,color:on === f ? BK.coral : BK.ink,padding:'1px 5px'}}>{f}</span>)}</div>;
// a hand laid flat (fingers up), its palm's bottom left at (x, y), k its scale
const sprHand = (x, y, k = 1) => <g transform={'translate(' + x + ' ' + y + ') scale(' + k + ')'}>
  {[0, 1, 2, 3].map(i => <rect key={i} x={1 + i * 6.6} y={-38 + [4, 0, 1, 5][i]} width="5.8" height="22" rx="2.9" {...SPR_SWF}/>)}
  <rect x="-6" y="-21" width="7" height="16" rx="3.5" transform="rotate(-30 -2.5 -5)" {...SPR_SWF}/>
  <rect x="0" y="-22" width="28" height="22" rx="7" {...SPR_SWF}/></g>;
const sprBuzz = (x, y) => <g fill="none" stroke={PEN_C} strokeWidth="1.8" strokeLinecap="round"><path d={'M' + x + ' ' + (y - 8) + ' q4 8 0 16'}/><path d={'M' + (x + 6) + ' ' + (y - 12) + ' q6 12 0 24'}/></g>;
// a ruler held on a table, `out` of it over the edge, twanged
const sprRuler = (x, out, label) => <g>
  <rect x={x} y="62" width="72" height="7" {...SPR_SWF}/><line x1={x + 8} x2={x + 8} y1="69" y2="110" {...SPR_SW}/><line x1={x + 64} x2={x + 64} y1="69" y2="110" {...SPR_SW}/>
  <line x1={x + 72} x2={x + 72 + out} y1="59" y2={59 - out * 0.3} stroke={PEN_N} strokeOpacity="0.3" strokeWidth="2.4" strokeLinecap="round"/><line x1={x + 72} x2={x + 72 + out} y1="59" y2={59 + out * 0.3} stroke={PEN_N} strokeOpacity="0.3" strokeWidth="2.4" strokeLinecap="round"/>
  <rect x={x + 72 - (84 - out)} y="56" width="84" height="6" fill="#fff" stroke={PEN_N} strokeWidth="1.5"/>
  <path d={'M' + (x + 76 + out) + ' ' + (52 - out * 0.3) + ' q5 7 0 14 M' + (x + 76 + out) + ' ' + (52 + out * 0.3) + ' q5 7 0 14'} fill="none" stroke={PEN_C} strokeWidth="1.6" strokeLinecap="round"/>
  <path d={'M' + (x + 36) + ' 34 L' + (x + 36) + ' 50 M' + (x + 31) + ' 45 L' + (x + 36) + ' 51 L' + (x + 41) + ' 45'} fill="none" stroke={PEN_C} strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
  <text x={x + 50} y="22" textAnchor="middle" fontSize="13" fontWeight="900" fill={PEN_N}>{label}</text></g>;

const SPR_WB = {
  zones: [38, 62, 89, 33],
  higher: [['treble', 30, 34], ['bass', 22, 19], ['treble', 36, 31], ['bass', 20, 24]],
  tunes: [['treble', 35, 'from the next C up'], ['treble', 28, 'from middle C'], ['bass', 21, 'from the next C down']],
  pairs: [['bar', true], ['bell', false], ['fiddle', true], ['brass', false]],
  bars: [70, 40, 92, 55],
  words: [['A short string sounds', 'high'], ['A big drum sounds', 'low'], ['Slow vibrations sound', 'low'], ['A small bell sounds', 'high']],
  fams: ['flute', 'trombone', 'harp', 'xylophone'],
  hows: ['brass', 'percussion', 'woodwind', 'strings'],
  copy: [['violin', 'a violin', 'E\u00a0D\u00a0C\u00a0D\u00a0E, starting on the E above middle C, smooth and singing'], ['clarinet', 'a clarinet', 'C\u00a0E\u00a0G\u00a0E\u00a0C from middle C, smooth'], ['tuba', 'a tuba', 'C\u00a0D\u00a0E\u00a0D\u00a0C from the second C below middle C, slow'], ['triangle', 'a triangle', 'the highest C, once, softly; let it ring']],
  vfam: ['Viola', 'Double bass', 'Violin', 'Cello'],
  lowerV: [['Soprano', 'Bass'], ['Tenor', 'Alto'], ['Violin', 'Viola'], ['Double bass', 'Cello']],
  find: [['The violin family', ['double bass: the first E from the left', 'cello: the second C', 'viola: the third C', 'violin: the G below middle C']], ['Voices', ['bass voice: the second E from the left', 'tenor: the third C', 'alto: the F below middle C', 'soprano: middle C']]],
  bars6: [['Double bass', ['double bass', 'piccolo']], ['Piccolo', ['cello', 'piccolo']], ['Violin', ['violin', 'double bass']], ['Cello', ['flute', 'cello']]],
  yesno: [['The piano can play lower than a double bass.', 'yes'], ['The piano has 88 keys.', 'yes'], ['The piano’s lowest key is a C.', 'no'], ['The piano can play as high as a piccolo.', 'yes']],
  gBelow: ['violin', 'flute', 'cello', 'piccolo'],
};
const SPR_CHK = {
  zones: [86, 35, 60, 41],
  pairs: [['bell', false], ['string', true], ['brass', true], ['drum', false]],
  fams: ['clarinet', 'triangle', 'cello', 'trumpet'],
  vfam: ['Cello', 'Violin', 'Double bass', 'Viola'],
  lower: [['Piccolo', 'Double bass'], ['Viola', 'Violin'], ['Bass', 'Alto'], ['Flute', 'Cello']],
  staff: [[27, 'bass', 'middle'], [17, 'bass', 'low'], [40, 'treble', 'high']],
  slow: ['Fast vibrations sound', 'high'],
};

function SprWorkbook({ startNo = 1 }) {
  const W = SPR_WB, pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={startNo + 1 + pages.length} chId="pitch-range">{content}</WbPage>);
  const zoneWords = ['low', 'middle', 'high'];

  // 2 (faces "Low, middle and high")
  P(<>
    <WbTop step={1}/>
    <Part kind="together" title="Low, middle or high?" how="The orange key: circle low, middle or high. The first one is done.">
      <BkGrid cols={2} gap="8px 14px">{W.zones.map((m, i) => <ExCell key={i} n={i + 1} ex={i === 0}>{sdyCol(<>{sprStripSm({ key1: m })}{sdyCircle(zoneWords, i === 0 ? sprZoneOf(m) : null)}</>, '12px 6px 4px')}</ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="Circle the higher note" how="In each box, circle the higher of the two notes.">
      <BkGrid cols={4} gap="8px 10px">{W.higher.map(([clef, a, b], i) => <BkCell key={i} n={i + 5}><div style={{padding:'10px 2px 4px'}}><SdyPaper mm={3.6} clef={clef} items={[['w', 4, a], ['w', 4, b], ['sp', 6]]} o={{ D: 14, x0: clef === 'bass' ? 52 : 44 }}/></div></BkCell>)}</BkGrid>
    </Part>
    <Part kind="play" title="Play it, then tick it" how="Right hand: play the same tune from the next C up, from middle C and from the next C down. Tick each one you play.">
      {sskRowN(9, <div style={{display:'grid',gridTemplateColumns:'190px 1fr',alignItems:'center',gap:'34px 16px',width:'100%'}}>{W.tunes.map(([clef, d, w]) => <React.Fragment key={w}>
        <span style={{fontSize:14.5,fontWeight:800,color:BK.ink,display:'flex',alignItems:'center',gap:8}}>{sprTick()}{w}</span>
        <div style={{justifySelf:'start',width:'100%',maxWidth:420}}><SdyPaper mm={5.2} clef={clef} items={[['ts', 4], ...sdyQ([d, d + 2, d + 4, d + 2]), ['|'], ['w', 4, d], ['||']]} o={{ D: 30 }}/></div></React.Fragment>)}</div>)}
    </Part>
    <Faces/>
  </>);

  // 3 (faces "Big is low, small is high")
  P(<>
    <WbTop step={2}/>
    <Part kind="together" title="Which sounds higher?" how="In each box, circle the one that sounds higher. The first one is done.">
      <BkGrid cols={2} gap="8px 14px">{W.pairs.map(([pid, bigLeft], i) => <ExCell key={i} n={i + 1} ex={i === 0}><div style={{padding:'8px 0 2px',maxWidth:290,margin:'0 auto'}}>{sprPairPic(pid, bigLeft, i === 0)}</div></ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="Number the bars, circle the words" how="These are xylophone bars. Number them from the lowest sound (1) to the highest (4). Then circle high or low.">
      <div style={{display:'grid',gridTemplateColumns:'1fr 1.4fr',gap:14,alignItems:'center'}}>
        {sskRowN(5, <div style={{display:'flex',justifyContent:'center',alignItems:'flex-end',gap:16}}>{W.bars.map((h, i) => <div key={i} style={{display:'flex',flexDirection:'column',alignItems:'center',gap:6}}><div style={{width:24,height:h,background:PEN_N,borderRadius:4}}/>{sprBoxN()}</div>)}</div>)}
        <div style={{display:'grid',gap:8}}>{W.words.map(([s], i) => <div key={i} style={{display:'flex',alignItems:'center',gap:10,fontSize:14,fontWeight:800,color:BK.ink}}>{sskNum(i + 6)}<span style={{flex:1}}>{s}</span>{sdyCircle(['high', 'low'], null, false, 18)}</div>)}</div>
      </div>
    </Part>
    <Part kind="play" title="Try it, then circle it" how="Tap a big pot, then a small cup, with a spoon. Then play the lowest A and the highest C, and hold each key down.">
      <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:18,fontSize:14.5,fontWeight:800,color:BK.ink,alignItems:'end'}}>
        {sskRowN(10, <div style={{display:'flex',flexDirection:'column',alignItems:'center',gap:8}}><svg viewBox="0 0 220 110" style={{width:'100%',maxWidth:250}}><path d="M14 40 L104 40 L96 100 L22 100 Z" {...SPR_SWF}/><path d="M4 46 L14 46 M104 46 L114 46" {...SPR_SW}/><path d="M150 66 L190 66 L186 100 L154 100 Z" {...SPR_SWF}/><path d="M190 74 q 14 4 0 16" {...SPR_SW}/><path d="M124 30 L150 56" stroke={PEN_C} strokeWidth="3" strokeLinecap="round"/><ellipse cx="121" cy="27" rx="6" ry="4" fill={PEN_C}/>
          <text x="59" y="28" textAnchor="middle" fontSize="13" fontWeight="900" fill={PEN_N}>pot</text><text x="170" y="56" textAnchor="middle" fontSize="13" fontWeight="900" fill={PEN_N}>cup</text></svg>
          <span style={{textAlign:'center'}}>The higher sound came from</span>{sdyCircle(['the pot', 'the cup'], null, false, 26)}</div>)}
        {sskRowN(11, <div style={{display:'flex',flexDirection:'column',alignItems:'center',gap:8}}><svg viewBox="0 -30 264 84" style={{width:'100%',maxWidth:300}}><SprKeys88 x0={2} y0={0} kw={5} h={32} middleC={false} marks={{ 21: "cor", 108: "cor" }}/>
          <text x="2" y="-10" fontSize="11" fontWeight="900" fill={PEN_C}>lowest A</text><text x="262" y="-10" textAnchor="end" fontSize="11" fontWeight="900" fill={PEN_C}>highest C</text></svg>
          <span style={{textAlign:'center'}}>The one that rang longer</span>{sdyCircle(['the lowest A', 'the highest C'], null, false, 16)}</div>)}
      </div>
    </Part>
    <Faces/>
  </>);

  // 4 (faces "The instrument families")
  P(<>
    <WbTop step={3}/>
    <Part kind="together" title="Which family?" how="Circle each instrument's family. The first one is done.">
      <BkGrid cols={4} gap="8px 10px">{W.fams.map((id, i) => { const it = SPR_INST.find(x => x.id === id); return <ExCell key={i} n={i + 1} ex={i === 0}>{sdyCol(<>{sprIconSm(id, 76)}<div style={{textAlign:'center',fontSize:13,fontWeight:900,color:BK.ink}}>{it.en}</div>{sprFamWords(i === 0 ? it.fam : null)}</>, '12px 2px 6px')}</ExCell>; })}</BkGrid>
    </Part>
    <Part kind="home" title="How does it make its sound?" how="Draw a line from each family to how it makes its sound.">
      <div style={{display:'grid',gridTemplateColumns:'1fr 1.5fr',gap:'12px 80px',maxWidth:560,margin:'0 auto',fontSize:15,fontWeight:800,color:BK.ink}}>
        {SPR_FAMS.map((f, i) => <React.Fragment key={f}><div style={{display:'flex',alignItems:'center',justifyContent:'space-between',gap:8}}>{sskNum(i + 5)}<span style={{flex:1}}>{f}</span><span style={{width:8,height:8,borderRadius:4,background:PEN_N}}/></div>
          <div style={{display:'flex',alignItems:'center',gap:8}}><span style={{width:8,height:8,borderRadius:4,background:PEN_N,flex:'0 0 auto'}}/><span>{SPR_HOW_EN[W.hows[i]]}</span></div></React.Fragment>)}
      </div>
    </Part>
    <Part kind="play" title="Play like them" how="Play each one on the piano. Tick each one you play.">
      <div style={{display:'grid',gap:18,maxWidth:600,margin:'0 auto',width:'100%'}}>{W.copy.map(([id, who, how], i) => <div key={id} style={{display:'grid',gridTemplateColumns:'24px 90px 1fr 24px',alignItems:'center',gap:14,fontSize:15.5,color:BK.ink}}>{sskNum(i + 9)}{sprIconSm(id, 84)}<span><b>Like {who}:</b> {how}</span>{sprTick()}</div>)}</div>
    </Part>
    <Faces/>
  </>);

  // 5 (faces "Low to high")
  P(<>
    <WbTop step={4}/>
    <Part kind="together" title="Low to high" how="Number the violin family from the lowest (1) to the highest (4). The double bass is done.">
      {sskRowN(1, <div style={{display:'flex',justifyContent:'center',alignItems:'flex-end',gap:26}}>{W.vfam.map(n => { const v = SPR_VFAM.find(x => x.n === n), h = v.h * 1.0;
        return <div key={n} style={{display:'flex',flexDirection:'column',alignItems:'center',gap:4}}><svg viewBox={'0 0 84 ' + (h + 4)} style={{width:84,height:h + 4}}><SprFiddle cx={42} base={h + 2} h={h} peg={v.peg} bass={v.bass}/></svg><span style={{fontSize:12.5,fontWeight:800,color:BK.ink}}>{sprEn(n)}</span>{sprBoxN(n === 'Double bass' ? '1' : null, n === 'Double bass')}</div>; })}</div>)}
    </Part>
    <Part kind="home" title="Which can go lower?" how="In each box, circle the one that can go lower.">
      <BkGrid cols={4} gap="8px 10px">{W.lowerV.map((pr, i) => <BkCell key={i} n={i + 2}><div style={{padding:'16px 2px 6px',display:'flex',flexDirection:'column',alignItems:'center',gap:12,fontSize:14.5,fontWeight:800,color:BK.ink}}>{pr.map(n => <span key={n}>{sprEn(n)}</span>)}</div></BkCell>)}</BkGrid>
    </Part>
    <Part kind="play" title="Find them, then play them" how="On each keyboard, draw a dot on each one's lowest note. Then play them from left to right. Tick each one.">
      {W.find.map(([head, list], k) => <React.Fragment key={head}>{sskRowN(6 + k, <div style={{display:'flex',flexDirection:'column',gap:8,width:'100%',marginTop:k ? 14 : 0}}><div style={{fontSize:14.5,fontWeight:900,color:BK.coral}}>{head}</div><svg viewBox="0 0 500 94" style={{width:'100%',display:'block'}}><SprKeysPart lo={21} hi={72} x0={2} y0={2} kw={16} h={64}/></svg>
        <div style={{display:'grid',gridTemplateColumns:'1.25fr 1fr',gap:'10px 20px',fontSize:14.5,fontWeight:800,color:BK.ink,maxWidth:600,margin:'0 auto'}}>{list.map(w => sprTickW(w))}</div></div>)}</React.Fragment>)}
    </Part>
    <Faces/>
  </>);

  // 6 (faces "The piano's range")
  P(<>
    <WbTop step={5}/>
    <Part kind="together" title="Whose range is it?" how="The orange keys are one instrument's range. Circle the instrument. The first one is done.">
      <BkGrid cols={2} gap="8px 14px">{W.bars6.map(([n, opts], i) => { const r = SPR_RANGE(n); return <ExCell key={i} n={i + 1} ex={i === 0}>{sdyCol(<>{sprStripSm({ range: [r.lo, r.hi] })}{sdyCircle(opts, i === 0 ? sprEn(n) : null)}</>, '12px 6px 4px')}</ExCell>; })}</BkGrid>
    </Part>
    <Part kind="home" title="Yes or no?" how="Circle yes or no.">
      <div style={{display:'grid',gap:6,maxWidth:560}}>{W.yesno.map(([s], i) => <div key={i} style={{display:'grid',gridTemplateColumns:'24px 1fr 120px',alignItems:'center',gap:8,fontSize:14.5,fontWeight:800,color:BK.ink}}>{sskNum(i + 5)}<span>{s}</span><span style={{display:'flex',justifyContent:'space-between',padding:'0 8px'}}><span style={{padding:'0 7px'}}>yes</span><span style={{padding:'0 7px'}}>no</span></span></div>)}</div>
    </Part>
    <Part kind="play" title="Colour them, then play them" how="Play every C on an 88-key piano, from the lowest to the highest. Colour each C on the picture as you play it, then count them.">
      {sskRowN(9, <div style={{display:'flex',flexDirection:'column',alignItems:'stretch',gap:6,width:'100%'}}><svg viewBox="0 0 500 158" style={{width:'100%',display:'block'}}><SprKeysPart lo={21} hi={59} x0={2} y0={2} kw={16.8} h={52} midC={false}/><text x={398} y={24} fontSize="12" fontWeight="800" fill={BK.muted}>continued</text><text x={398} y={40} fontSize="12" fontWeight="800" fill={BK.muted}>below ↓</text><SprKeysPart lo={60} hi={108} x0={2} y0={72} kw={16.8} h={52}/></svg>
        <div style={{display:'flex',alignItems:'center',justifyContent:'center',gap:8,fontSize:15,fontWeight:800,color:BK.ink}}>Cs on the piano: {sprBoxN()}</div></div>)}
      {sskRowN(10, <div style={{display:'flex',flexDirection:'column',alignItems:'center',gap:6,marginTop:12,fontSize:15,fontWeight:800,color:BK.ink}}><span>Play the G below middle C. Circle each one that can play it.</span>
        <div style={{display:'flex',gap:30,alignItems:'flex-end'}}>{W.gBelow.map(id => <div key={id} style={{display:'flex',flexDirection:'column',alignItems:'center'}}>{sprIconSm(id === 'piccolo' ? 'flute' : id, id === 'piccolo' ? 56 : 82)}<span>{id}</span></div>)}</div></div>)}
    </Part>
    <Faces/>
  </>);

  // 7. the check-up on paper
  P(<SprPaperCheck/>);
  return <>{pages}</>;
}
function SprPaperCheck() {
  const C = SPR_CHK;
  return <div className="lb-paper" style={{display:'flex',flexDirection:'column',gap:4,flex:'1 0 auto'}}>
    <LbPaperHead/>
    {bkSec('A', 'The orange key: circle low, middle or high.')}
    <BkGrid cols={2} gap="6px 10px">{C.zones.map((m, i) => <BkCell key={i} n={i + 1}>{sdyCol(<><div style={{maxWidth:270,width:'100%',margin:'0 auto'}}>{sprStripSm({ key1: m })}</div>{sdyCircle(['low', 'middle', 'high'], null, true)}</>, '6px 6px 2px')}</BkCell>)}</BkGrid>
    {bkSec('B', 'Circle the one that sounds higher.')}
    <BkGrid cols={4} gap="6px 8px">{C.pairs.map(([pid, bigLeft], i) => <BkCell key={i} n={i + 5}><div style={{padding:'0',margin:'0 -4px'}}>{sprPairPic(pid, bigLeft)}</div></BkCell>)}</BkGrid>
    {bkSec('C', 'Circle each instrument’s family.')}
    <BkGrid cols={4} gap="6px 8px">{C.fams.map((id, i) => <BkCell key={i} n={i + 9}>{sdyCol(<>{sprIconSm(id, 46)}<div style={{textAlign:'center',fontSize:12.5,fontWeight:900,color:BK.ink}}>{SPR_INST.find(x => x.id === id).en}</div>{sprFamWords(null, 12)}</>, '8px 2px 4px')}</BkCell>)}</BkGrid>
    <div style={{display:'grid',gridTemplateColumns:'1.25fr 1fr',gap:10}}>
      <div style={{display:'flex',flexDirection:'column'}}>{bkSec('D', 'Number them, lowest (1) to highest (4).')}
        <BkCell n={13}><div style={{padding:'6px 2px 4px',display:'flex',justifyContent:'center',alignItems:'flex-end',gap:14}}>{C.vfam.map(n => { const v = SPR_VFAM.find(x => x.n === n), h = v.h * 0.42;
          return <div key={n} style={{display:'flex',flexDirection:'column',alignItems:'center',gap:3}}><svg viewBox={'0 0 44 ' + (h + 4)} style={{width:44,height:h + 4}}><SprFiddle cx={22} base={h + 2} h={h} peg={v.peg} bass={v.bass}/></svg><span style={{fontSize:11,fontWeight:800,color:BK.ink}}>{sprEn(n)}</span>{sprBoxN()}</div>; })}</div></BkCell></div>
      <div style={{display:'flex',flexDirection:'column'}}>{bkSec('E', 'Circle the one that can go lower.')}
        <BkGrid cols={2} gap="6px 8px">{C.lower.map((pr, i) => <BkCell key={i} n={i + 14}><div style={{padding:'8px 2px 2px',display:'flex',flexDirection:'column',alignItems:'center',gap:6,fontSize:13,fontWeight:800,color:BK.ink}}>{pr.map(n => <span key={n}>{sprEn(n)}</span>)}</div></BkCell>)}</BkGrid></div>
    </div>
    {bkSec('F', 'Circle low, middle or high for each note. Then circle the right word.')}
    <BkGrid cols={4} gap="6px 8px">{C.staff.map(([d, clef], i) => <BkCell key={i} n={i + 18}>{sdyCol(<><div style={{padding:'0 6px'}}><SdyPaper mm={3} clef={clef} items={[['w', 4, d], ['sp', 3]]} o={{ D: 14, x0: clef === 'bass' ? 52 : 44 }}/></div>{sdyCircle(['low', 'middle', 'high'], null, true, 8)}</>, '8px 2px 2px')}</BkCell>)}
      <BkCell n={21}>{sdyCol(<><div style={{flex:1,display:'flex',alignItems:'center',justifyContent:'center',textAlign:'center',fontSize:14,fontWeight:800,color:BK.ink,padding:'0 6px'}}>{C.slow[0]}</div>{sdyCircle(['high', 'low'], null, false, 22)}</>, '12px 2px 6px')}</BkCell></BkGrid>
  </div>;
}

const sprLesson = (txt) => <div style={{fontSize:12,color:BK.ink,lineHeight:1.5,marginBottom:4}}><b style={{color:BK.coral}}>In the lesson</b>{'  '}{txt}</div>;
function SprTeacher() {
  const W = SPR_WB, C = SPR_CHK, pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={pages.length + 1} chId="pitch-range" teacher>{content}</WbPage>);
  const hi = ([, a, b]) => a > b ? 'the first (' + dName(a) + ')' : 'the second (' + dName(b) + ')';
  const small = ([, bigLeft]) => bigLeft ? 'the right one (smaller)' : 'the left one (smaller)';
  const barNums = (hs) => hs.map(h => 1 + hs.slice().sort((a, b) => b - a).indexOf(h)).join(' ');
  const famOf = (id) => SPR_INST.find(x => x.id === id).fam;
  const marks = { A: C.zones.length, B: C.pairs.length, C: C.fams.length, D: 1, E: C.lower.length, F: C.staff.length + 1 };
  const total = Object.values(marks).reduce((a, b) => a + b, 0);
  const canG = (id) => id === 'violin' || id === 'cello';
  P(<>
    <div style={{fontFamily:"'Playfair Display', Georgia, serif",fontSize:28,fontWeight:900,color:BK.ink,margin:'2px 0 2px'}}>Teacher copy · {bkChapterName('pitch-range')}</div>
    <div style={{fontSize:12.5,color:BK.muted,margin:'0 0 8px',lineHeight:1.5}}>Low on the left, high on the right (chapter {bkChapterNo('first-steps')}). Low: the bottom of the bass staff and below; high: the top of the treble staff and above; middle: middle C and the keys near it, from the G below to the F above. Every task and drill question keeps to clear cases (low up to G2, middle G3 to F4, high from G5): the keys between are left out on purpose. Big and long things vibrate slowly and sound low; hertz counts vibrations per second. The four families and how each makes its sound. The violin family (in one family, the bigger, the lower); the voices, soprano to bass; range; the piano's 88 keys, A0 to C8. Drill: levels 1 and 2 after page 3, 3 and 4 after page 4, 5 after page 6, 6 and 7 by ear; 8 (each A doubles in hertz) and 9 (which instrument can play a key) are extras.</div>
    <div style={{fontSize:12.5,color:BK.ink,margin:'0 0 12px',lineHeight:1.5,border:'0.8px solid ' + BK.hair,padding:'7px 10px'}}><b style={{color:BK.coral}}>Lesson time: the sea, the ground and the sky.</b> The child shuts their eyes; play one note anywhere. They point down (low), straight ahead (middle) or up (high), then find a key near it.</div>
    <TcBlock page={2} title="Low, middle and high" answers={<>{sprLesson('Play one note low, middle or high; the child says which, then plays a note in the same place. Swap.')}{tcAns('TRY IT', W.zones.map(sprZoneOf))}{tcAns('YOUR TURN', W.higher.map(hi), 5)}{tcAns('PLAY', ['C E G E C from C5, from middle C and from C3 (bass staff)'], 9)}</>}
      watch="Left and right mixed up. Thinking low means soft and high means loud. Reading higher on the page but playing further left. A tune moved to a new C starting on the wrong letter."
      say="“Left: low. Right: high. Middle C: the middle.”"/>
    <TcBlock page={3} title="Big is low, small is high" answers={<>{sprLesson('Open the lid together: play the lowest and the highest key and watch the strings. Long, thick strings move slowly; short, thin ones fast.')}{tcAns('TRY IT', W.pairs.map(small))}{tcAns('YOUR TURN', [barNums(W.bars), ...W.words.map(w => w[1])], 5)}{tcAns('PLAY', ['the cup', 'the lowest A'], 10)}</>}
      watch="Big read as loud. Long bars counted from the short end. Vibrations heard as loudness, not pitch. The lowest A rings longer: long, heavy strings vibrate longer."
      say="“Big and long: low. Small and short: high.”"/>
    <TcBlock page={4} title="The instrument families" answers={<>{sprLesson('Name an instrument; the child names its family and mimes how it is played: bow, blow, buzz, hit.')}{tcAns('TRY IT', W.fams.map(famOf))}{tcAns('YOUR TURN', SPR_FAMS.map(f => f + ': ' + SPR_HOW_EN[f]), 5)}{tcAns('PLAY', W.copy.map(c => c[1]), 9)}</>}
      watch="The flute put in brass because it is metal: it is woodwind. The harp put in percussion. The piano called only percussion: its strings are hit by hammers."
      say="“Strings: bow or pluck. Woodwind: blow. Brass: buzz. Percussion: hit.”"/>
  </>);
  P(<>
    <TcBlock page={5} title="Low to high" answers={<>{sprLesson('Play the four lowest notes (E1, C2, C3, G3) and match each to its instrument. Sing one note low like a bass, then high like a soprano.')}{tcAns('TRY IT', [sprOrderNums(W.vfam).join(' ')], 1)}{tcAns('YOUR TURN', W.lowerV.map(sprLower).map(sprEn), 2)}{tcAns('PLAY', ['dots on E1, C2, C3, G3', 'dots on E2, C3, F3, C4 (middle C)'], 6)}</>}
      watch="“Bass” means three things: the bass staff, the bass voice and the double bass. The rule holds in one family only: a flute is longer than a violin, yet its lowest note (middle C) is higher than the violin's (G). The viola mixed up with the violin: it is a little bigger, so a little lower. Alto taken as the lowest voice: bass is."
      say="“In one family: the bigger, the lower.”"/>
    <TcBlock page={6} title="The piano’s range" answers={<>{sprLesson('Point to a key; the child names an instrument that can play it. Middle C: almost all of them.')}{tcAns('TRY IT', W.bars6.map(([n]) => sprEn(n)))}{tcAns('YOUR TURN', W.yesno.map(y => y[1]), 5)}{tcAns('PLAY', ['8 Cs (C1 to C8)', W.gBelow.filter(canG).join(' and ') + ' (the flute starts on middle C, the piccolo higher still)'], 9)}</>}
      watch="Counting the Cs by guesswork: each C is the white key just left of a group of two black keys. Missing the top C, the last key. Thinking the piano starts on C: it starts on A."
      say="“88 keys: lower than a double bass, as high as a piccolo.”"/>
    <TcBlock page={7} title="The check-up on paper (the Workbook's last page)" answers={<>
      {tcAns('A', C.zones.map(sprZoneOf))}
      {tcAns('B', C.pairs.map(small), 5)}
      {tcAns('C', C.fams.map(famOf), 9)}
      {tcAns('D', [sprOrderNums(C.vfam).join(' ')], 13)}
      {tcAns('E', C.lower.map(sprLower).map(sprEn), 14)}
      {tcAns('F', [...C.staff.map(s => s[2]), C.slow[1]], 18)}
      <div style={{fontSize:12,color:BK.ink,marginTop:6,lineHeight:1.5}}>One mark for each answer; D is one mark if all four numbers are right: A {marks.A}, B {marks.B}, C {marks.C}, D {marks.D}, E {marks.E}, F {marks.F}; {total} in all. A section with any wrong answer is not passed yet: go back to its page below. Also listen to the student (My five checks, Lesson Book page 7).</div>
    </>}
      goBack={[{ id: 'a', step: 1, page: 2 }, { id: 'b', step: 2, page: 3 }, { id: 'c', step: 3, page: 4 }, { id: 'd', step: 4, page: 5 }, { id: 'e', step: '4⁠–⁠5', page: '5⁠–⁠6' }, { id: 'f', step: '1⁠–⁠2', page: '2⁠–⁠3' }]}/>
    <div style={{border:'0.8px solid ' + BK.hair,padding:'7px 12px',fontSize:12,color:BK.ink,lineHeight:1.5}}><b style={{color:BK.coral}}>My five checks (Lesson Book page 7): what to ask.</b> 1. Page 2: a low, a middle and a high C; then point to the bass staff and the treble staff. 2. Page 3: why a cello sounds lower than a violin. 3. Page 4: the four families, with an instrument and how it is played for each. 4. Page 5: the violin family from low to high. 5. Page 6: where a double bass, a violin and a piccolo play on the keys. Got it! means right without help.</div>
  </>);
  return <>{pages}</>;
}
WORKBOOKS['pitch-range'] = SprWorkbook;
TEACHER_COPIES['pitch-range'] = SprTeacher;
