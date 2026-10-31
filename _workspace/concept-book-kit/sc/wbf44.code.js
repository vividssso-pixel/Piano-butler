// ── Build EF (her 31 Oct 23:05 and 23:22: the Workbooks, fun first, the Beginner floor; only the parts better changed,
// each swapped for a game that practises the same thing, never a part added). Chapter 7, page 4: the hidden note. Colour
// every note that lasts 3 beats and a big dotted minim appears (its hollow head, its stem, its dot); the child circles
// its name and writes its beats, so the picture checks the colouring. The other cells hold minims (the one to mix up, so
// the most of them), crotchets and semibreves.
const NV_HIDE = ['......X....', '......X....', '......X....', '...XXXX....', '..X...X.X..', '..XXXX.....'];
const NV_HIDE_CELLS = (() => {
  const R = bkRand(bkHash('nv-wb-hide')), others = [...Array(21).fill('h'), ...Array(16).fill('q'), ...Array(15).fill('w')];
  for (let i = others.length - 1; i > 0; i--) { const j = Math.floor(R() * (i + 1)); [others[i], others[j]] = [others[j], others[i]]; }
  let o = 0;
  return NV_HIDE.join('').split('').map(c => (c === 'X' ? 'hd' : others[o++]));
})();
function NvHidden({ cell = 36, solved = false }) {
  const C = NV_HIDE[0].length, R = NV_HIDE.length;
  return <div style={{display:'grid',gridTemplateColumns:'24px auto auto',justifyContent:'center',alignItems:'center',gap:'0 26px',padding:'2px 0'}}>
    <span style={{alignSelf:'start'}}>{nvNum(9)}</span>
    <svg data-nv-hidden viewBox={'0 0 ' + C * cell + ' ' + R * cell} style={{width:C * cell,maxWidth:'100%',display:'block'}}>
      {NV_HIDE_CELLS.map((k, i) => { const x = (i % C) * cell, y = Math.floor(i / C) * cell;
        return <g key={i} data-k={k}>
          <rect x={x + 0.5} y={y + 0.5} width={cell - 1} height={cell - 1} fill={solved && k === 'hd' ? BK.coral : '#fff'} fillOpacity={solved && k === 'hd' ? 0.45 : 1} stroke={BK.line} strokeWidth="1"/>
          <svg x={x + 2} y={y + 2} width={cell - 4} height={cell - 4} viewBox="14 16 52 56" dangerouslySetInnerHTML={{ __html: nvGlyphRaw(k) }}/>
        </g>; })}
    </svg>
    <div style={{display:'grid',gap:10,justifyItems:'start',minWidth:0}}>
      <span style={{fontSize:12.5,fontWeight:900,color:BK.ink}}>The note that appears:</span>
      <div style={{display:'grid',gap:6}}>{['minim', 'dotted minim', 'semibreve'].map(w => <span key={w}>{nvChoose([w])}</span>)}</div>
      <span style={{display:'inline-flex',alignItems:'center',gap:6,fontSize:12.5,fontWeight:800,color:BK.ink}}>It lasts {bkBox(36, 30)} beats</span>
    </div>
  </div>;
}

// Chapter 5, Hand positions. Page 6's PLAY 'Make your own echo' was free and needed someone at home (Book rules 3 and 4):
// now the finger code, four rows of finger numbers (each hand, each position) whose letters spell a word, so the word
// checks the letters. Page 7's PLAY 'Write your own tune' was free: now the same tune, higher, the room's two tunes
// (MT_SONGS) in C position and in G position. Page 5's 'Draw the mirror' asked for two hands traced in a box 3 cm tall and
// pushed the page over: now the mirror's missing numbers. Pages 3 and 4's PLAY pictures are drawn big enough to fill.
const HP_CODE = [['R', 'C', [3, 5, 5]], ['R', 'G', [3, 2, 1]], ['L', 'C', [2, 3, 4]], ['L', 'G', [1, 4, 1]]];   // EGG BAG FED DAD
const hpLetter = (pos, h, f) => (pos === 'C' ? 'CDEFG' : 'GABCD')[h === 'R' ? f - 1 : 5 - f];
const hpRing = (x, size = 30) => <span style={{width:size,height:size,borderRadius:size / 2,border:'2px solid ' + BK.ink,display:'inline-flex',alignItems:'center',justifyContent:'center',fontSize:size * 0.52,fontWeight:900,color:BK.ink,background:'#fff'}}>{x}</span>;
function HpCodeCell({ row, n, ex }) {
  const [h, pos, fs] = row;
  return <ExCell n={n} ex={ex}><div style={{display:'grid',justifyItems:'center',gap:10,padding:'22px 4px 14px'}}>
    <div style={{fontSize:12.5,fontWeight:900,color:BK.muted}}>{hpwHand(h)}, {pos} position</div>
    <div style={{display:'flex',gap:20}}>{fs.map((f, i) => <div key={i} style={{display:'grid',justifyItems:'center',gap:8}}>{hpRing(f, 40)}{nvBox(ex, hpLetter(pos, h, f), 44, 42)}</div>)}</div>
  </div></ExCell>;
}
function HpSameTune({ ex0 = true }) {
  return <div style={{display:'grid',gap:12}}>{MT_SONGS.map(([name, , seq], r) => <div key={name} style={{border:'1px solid rgba(38,41,107,0.16)',borderRadius:10,padding:'8px 10px',display:'grid',gap:6}}>
    <span style={{fontFamily:LB_SERIF,fontSize:14,fontWeight:800,color:BK.ink}}>{name}</span>
    <div style={{display:'grid',gridTemplateColumns:'86px repeat(' + seq.length + ', 36px)',gap:'6px 6px',alignItems:'center',justifyItems:'center',justifyContent:'start'}}>
      <span style={{justifySelf:'start',fontSize:11,fontWeight:900,color:BK.muted}}>Fingers</span>{seq.map((f, i) => <span key={i}>{hpRing(f, 28)}</span>)}
      {['C', 'G'].map(pos => <React.Fragment key={pos}><span style={{justifySelf:'start',fontSize:11.5,fontWeight:900,color:BK.ink}}>{pos} position</span>{seq.map((f, i) => <span key={i}>{nvBox(ex0 && r === 0 && i === 0, hpLetter(pos, 'R', f), 32, 30)}</span>)}</React.Fragment>)}
    </div></div>)}</div>;
}
function HpMirrorFill() {
  const side = (label, s) => <div style={{display:'grid',justifyItems:'center',gap:6}}>{hpwCircles(s, false, 34)}<span style={{fontSize:11.5,fontWeight:900,color:BK.muted}}>{label}</span></div>;
  return <div style={{display:'flex',justifyContent:'center',alignItems:'flex-start',gap:22,padding:'6px 0'}}>
    {side('Left hand', '5 ?4 3 ?2 1')}<span style={{width:0,alignSelf:'stretch',borderLeft:'2px dashed ' + BK.coral}}/>{side('Right hand', '1 ?2 ?3 4 ?5')}
  </div>;
}
function HpLadder() {
  const L = ['D', '', 'B', '', 'G'], x0 = 70, x1 = 230, y0 = 20, G = 58;
  return <svg viewBox="0 0 300 300" style={{width:330,maxWidth:'100%',display:'block',margin:'0 auto'}}>
    <line x1={x0} x2={x0} y1="6" y2="296" stroke={BK.ink} strokeWidth="5" strokeLinecap="round"/><line x1={x1} x2={x1} y1="6" y2="296" stroke={BK.ink} strokeWidth="5" strokeLinecap="round"/>
    {L.map((l, i) => { const y = y0 + i * G + 20; return <g key={i}>
      <line x1={x0} x2={x1} y1={y} y2={y} stroke={BK.ink} strokeWidth="4" strokeLinecap="round"/>
      <rect x="124" y={y - 24} width="52" height="48" rx="8" fill="#fff" stroke={l ? BK.ink : BK.coral} strokeWidth="2"/>
      {l && <text x="150" y={y + 10} textAnchor="middle" fontFamily={LB_SERIF} fontSize="27" fontWeight="800" fill={BK.ink}>{l}</text>}
    </g>; })}
  </svg>;
}

// Chapter 8, Dynamics, page 3: YOUR TURN numbered the signs a second time and circled the louder of two. Now the voice
// ladder (the everyday voices of the old dynamics opener, VolumeLadder): four voices, each written as loud as it is, the
// child writes its sign, pp, p, mf or f. Same skill, tied to sounds the child knows.
const SDY_VOICES = [['classroom talk', 'mf', 19, 800], ['a whisper', 'pp', 13, 600], ['playground shout!', 'f', 23, 900], ['library voice', 'p', 15, 700]];
function SdyVoices() {
  return <BkGrid cols={4} gap="8px 10px">{SDY_VOICES.map(([w, sgn, fs, fw], i) => <BkCell key={i} n={i + 2}><div style={{display:'grid',justifyItems:'center',alignContent:'space-between',gap:10,padding:'18px 4px 8px',minHeight:118}}>
    <span style={{fontSize:fs,fontWeight:fw,fontStyle:sgn === 'pp' ? 'italic' : 'normal',color:sgn === 'pp' ? BK.muted : BK.ink,textAlign:'center',lineHeight:1.1,minHeight:52,display:'flex',alignItems:'center'}}>{sgn === 'f' ? w.toUpperCase() : w}</span>
    {sdyBox(48, 44)}</div></BkCell>)}</BkGrid>;
}

// Chapter 10, Steps & Skips, page 3: PLAY drew a single second note four times. Now the secret word: start on the red
// note, follow the moves, draw each next note and write every letter; the letters spell a word, so the word checks the
// notes. Two words in C position, so the right hand plays them with the thumb on middle C: EGG (a skip up, the same),
// FED (a step down, a step down).
const SSK_WORDS = [[30, [2, 0]], [31, [-1, -1]]];   // E G G, F E D
function SskWordPath({ start, moves, n }) {
  const X0 = 66, G = 60, W = X0 + moves.length * G + 34, xs = [X0, ...moves.map((_, i) => X0 + (i + 1) * G)];
  return <ExCell n={n}><div style={{padding:'12px 6px 8px'}}>
    <SfRow clef="treble" notes={[{ d: start, x: X0, color: BK.coral }]} width={W} minSpan={[29, 36]} items={moves.map((m, i) => ({ x: xs[i + 1], label: m === 0 ? 'same' : SF_MOVE[m] }))}/>
    <div style={{position:'relative',height:40,marginTop:6}}>{xs.map((x, i) => <span key={i} style={{position:'absolute',left:(x / W * 100) + '%',transform:'translateX(-50%)',top:0}}>{bkBox(38, 36)}</span>)}</div>
  </div></ExCell>;
}

// Chapter 12, Time Signatures, page 3: YOUR TURN wrote four more time signatures, as TRY IT does. Now spot the wrong
// bar: each tune has one bar with a beat too many; the child counts every bar against the top number and crosses it out.
const TS_WRONG = [{ top: 3, bars: [['h', 'q'], ['q', 'q', 'q'], ['h', 'h'], ['hd']], wrong: 3 }, { top: 4, bars: [['q', 'q', 'h'], ['w', 'q'], ['h', 'q', 'q'], ['w']], wrong: 2 }];

// Chapter 13, Tones & Semitones, page 3: PLAY asked 'half or whole?' of four more pairs. Now the step trail: from the
// star, seven moves (whole up, half up, ..., half down); the child writes each move's number on the key it lands on, and
// the seventh lands on the flag, so the flag checks the trail. C D E♭ F G A♭ B♭, then down to A.
const TN_TRAIL = { start: 'w0', moves: [[2, 1], [1, 1], [2, 1], [2, 1], [1, 1], [2, 1], [1, -1]] };
const tnTrailKeys = () => { const out = []; let k = TN_TRAIL.start; TN_TRAIL.moves.forEach(([n, d]) => { k = tnStep(k, n * d); out.push(k); }); return out; };
function TnTrail() {
  const w = 50, h = 80, T = 27, bw = w * 0.6, bh = h * 0.6, W = 8 * w + 4, L = (i) => TN_WL[i % 7], hasB = (i) => 'CDFGA'.includes(L(i)) && i < 7;
  const cx = (k) => k[0] === 'w' ? 2 + (+k.slice(1) + 0.5) * w : 2 + (+k.slice(1) + 1) * w, end = tnTrailKeys().slice(-1)[0];
  return <div style={{display:'grid',gridTemplateColumns:'auto 1fr',gap:22,alignItems:'center',padding:'0 6px'}}>
    <svg viewBox={'0 0 ' + W + ' ' + (T + h + 4)} style={{width:380,maxWidth:'100%',display:'block'}}>
      {Array.from({ length: 8 }, (_, i) => <g key={i}><rect x={2 + i * w} y={T} width={w} height={h} rx="3" fill="#fff" stroke={BK.ink} strokeWidth="1.3"/>
        {('w' + i) !== TN_TRAIL.start && <circle cx={2 + (i + 0.5) * w} cy={T + h - 15} r="10" fill="none" stroke={BK.ink} strokeWidth="0.9" strokeOpacity="0.45"/>}</g>)}
      {Array.from({ length: 8 }, (_, i) => hasB(i) && <g key={'b' + i}><rect x={2 + (i + 1) * w - bw / 2} y={T} width={bw} height={bh} rx="2" fill={BK.ink}/><circle cx={2 + (i + 1) * w} cy={T + bh - 12} r="9" fill="#fff"/></g>)}
      <text x={cx(TN_TRAIL.start)} y={T + h - 9} textAnchor="middle" fontSize="22" fill={BK.coral}>★</text>
      <text x={cx(TN_TRAIL.start)} y={T - 9} textAnchor="middle" fontSize="11" fontWeight="900" fill={BK.coral}>start</text>
      <g transform={'translate(' + cx(end) + ' ' + (T - 4) + ')'}><line x1="0" y1="0" x2="0" y2="-24" stroke={BK.ink} strokeWidth="1.8"/><path d="M0 -24 L15 -19 L0 -14 Z" fill={BK.coral}/></g>
    </svg>
    <div style={{display:'grid',gridTemplateRows:'repeat(4, auto)',gridAutoFlow:'column',gap:'6px 18px',justifyContent:'start'}}>{TN_TRAIL.moves.map(([n, d], i) => <span key={i} style={{display:'inline-flex',alignItems:'center',gap:6,fontSize:12.5,fontWeight:800,color:BK.ink,whiteSpace:'nowrap'}}>
      <span style={{fontFamily:LB_SERIF,fontStyle:'italic',fontWeight:700,fontSize:14}}>{i + 1}</span>{(n === 2 ? 'whole' : 'half') + (d > 0 ? ' up' : ' down')}</span>)}</div>
  </div>;
}
