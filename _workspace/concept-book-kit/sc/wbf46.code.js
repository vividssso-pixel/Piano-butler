// Build EH (her 1 Nov 19:44: "make it the best you think, build Grade 1, I'll check"): the Grade 1 Workbooks, fun first --
// only the parts better changed, each swapped for one that practises the same thing, none added. Swapped: the parts that
// needed someone else at home (a listening week, "your teacher plays six"), the free ones ("write your own", "make up your
// own B", "make your own term"), and the fifth "write what it means" in a row. Accidentals and Key Signatures stay as they are.

// Chapter 26, 6/8 Time, page 5: YOUR TURN was a week of someone at home clapping. Now words: said over and over, one
// quaver a syllable, the first syllable loud -- a two-syllable word is loud every second quaver (3/4), a three-syllable
// word every third (6/8), the room's own two groupings. Four words go in each bar, so the count checks the sorting.
const E8_WORDS = { 34: ['apple', 'tiger', 'pizza', 'monkey'], 68: ['butterfly', 'elephant', 'dinosaur', 'octopus'] };
const E8_BANK = ['tiger', 'butterfly', 'pizza', 'elephant', 'dinosaur', 'monkey', 'octopus'];   // apple is the example
function E8Words() {
  const house = (ts, row, list, ex) => <div style={{border:'1px solid ' + BK.hair,borderRadius:6,padding:'4px 14px 8px',display:'grid',gap:2,minWidth:0}} data-e8house={ts}>
    <div style={{display:'flex',alignItems:'center',gap:10}}><span style={{fontFamily:LB_SERIF,fontSize:26,fontWeight:900,color:BK.ink,flex:'0 0 auto'}}>{ts}</span><div style={{flex:'1 1 auto',minWidth:0}}>{e8wRow(e8wSee(row), { mw: 170 })}</div></div>
    <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:'0 14px'}}>{[0, 1, 2, 3].map(k => <div key={k} style={{height:29,borderBottom:'1.3px solid ' + BK.line,display:'flex',alignItems:'flex-end',justifyContent:'center',paddingBottom:2,fontFamily:LB_SERIF,fontStyle:'italic',fontWeight:800,fontSize:17,color:BK.coral}}>{ex && k === 0 ? list[0] : ''}</div>)}</div>
  </div>;
  return <div style={{display:'grid',gap:8}}>
    <div style={{display:'flex',flexWrap:'wrap',justifyContent:'center',gap:'6px 8px'}}>{E8_BANK.map(w => <span key={w} style={{border:'1.3px solid ' + BK.ink,borderRadius:16,padding:'1px 11px',fontFamily:LB_SERIF,fontWeight:800,fontSize:15.5,color:BK.ink}}>{w}</span>)}</div>
    <div style={{display:'grid',gridTemplateColumns:'minmax(0,1fr) minmax(0,1fr)',gap:14}}>{house('3/4', 't34', E8_WORDS[34], true)}{house('6/8', 'big', E8_WORDS[68], false)}</div>
  </div>;
}

// Chapter 26, 6/8 Time, page 6: PLAY was "write your own". Now the other way round from TRY IT on the same page: the
// counts where a note starts are circled; draw the notes. Each group of three counts is three quavers (all three
// circled), a dotted crotchet (the first only) or a crotchet and a quaver (the first and third): the room's own three.
// One line of two bars, the room's long-short row: a crotchet and a quaver, three quavers, a crotchet and a quaver, a
// dotted crotchet -- all three kinds.
const E8_CODE = ['ls2'];
const e8cGroups = (row) => { const g = [[], [], [], []]; srhSounds(E8[row]).forEach(x => { const k = Math.floor(x.b / 1.5 + 1e-6); g[k].push(Math.round((x.b - k * 1.5) / 0.5)); }); return g; };
const E8C_NAME = { '0,1,2': 'three quavers', '0': 'a dotted crotchet', '0,2': 'a crotchet and a quaver' };
function E8Code({ row, n }) {
  const G = e8cGroups(row), cell = (k) => <div key={k} style={{display:'grid',justifyItems:'center',gap:6,padding:'0 10px'}} data-e8code={G[k].join('')}>
    <div style={{display:'flex',gap:4}}>{[0, 1, 2].map(j => { const on = G[k].includes(j); return <span key={j} style={{width:28,height:28,borderRadius:14,border:'2px solid ' + (on ? BK.coral : 'transparent'),display:'inline-flex',alignItems:'center',justifyContent:'center',fontSize:16,fontWeight:900,color:on ? BK.ink : BK.muted}}>{(k % 2) * 3 + j + 1}</span>; })}</div>
    {bkBox(112, 66)}</div>;
  return <div style={{display:'flex',alignItems:'center',justifyContent:'center',gap:8}}>
    {nvNum(n)}<span style={{fontFamily:LB_SERIF,fontSize:24,fontWeight:900,color:BK.ink,lineHeight:0.9,textAlign:'center',width:26}}>6<br/>8</span>
    {[0, 1].map(b => <div key={b} style={{display:'flex',alignItems:'flex-end',padding:'4px 0',borderRight:(b === 1 ? '3px' : '1.6px') + ' solid ' + BK.ink}}>{cell(2 * b)}{cell(2 * b + 1)}</div>)}
  </div>;
}

// Chapter 25, Musical Terms, page 5: YOUR TURN was the fifth "write what each word means" in five pages. Now a crossword:
// each clue is a meaning (the room's own words), each answer the term, from the word bank. The crossings check the
// spelling (leggiero's two g, espressivo's two s); the two 9-letter downs and the two 8-letter acrosses need the meaning.
const TMX_XW = [['cantabile', 0, 4, 'D'], ['sostenuto', 0, 9, 'D'], ['maestoso', 3, 0, 'A'], ['leggiero', 6, 0, 'A'], ['espressivo', 8, 0, 'A']];
const xwCells = (xw) => { const m = {}; xw.forEach(([w, r, c, d]) => w.split('').forEach((ch, i) => { const k = (d === 'A' ? r : r + i) + ',' + (d === 'A' ? c + i : c); m[k] = m[k] && m[k] !== ch ? '!' : ch; })); return m; };
const xwNums = (xw) => { const st = xw.slice().sort((a, b) => a[1] - b[1] || a[2] - b[2]), out = {}; let n = 0, last = ''; st.forEach(([w, r, c]) => { if (r + ',' + c !== last) { n++; last = r + ',' + c; } out[w] = n; }); return out; };
function TmxXword() {
  const cells = xwCells(TMX_XW), nums = xwNums(TMX_XW), S = 30, keys = Object.keys(cells).map(k => k.split(',').map(Number));
  const R = Math.max(...keys.map(k => k[0])) + 1, C = Math.max(...keys.map(k => k[1])) + 1, at = {};
  TMX_XW.forEach(([w, r, c]) => { at[r + ',' + c] = nums[w]; });
  const clues = (d) => <div style={{display:'grid',gap:5}}><div style={{fontSize:11,fontWeight:900,letterSpacing:'0.12em',color:BK.coral}}>{d === 'A' ? 'ACROSS' : 'DOWN'}</div>
    {TMX_XW.filter(x => x[3] === d).sort((a, b) => nums[a[0]] - nums[b[0]]).map(([w]) => <div key={w} style={{display:'flex',gap:8,alignItems:'baseline',fontSize:14.5,fontWeight:800,color:BK.ink}}><span style={{fontFamily:LB_SERIF,fontStyle:'italic',width:14,flex:'0 0 auto'}}>{nums[w]}</span><span>“{tmxOf(w).en}”</span></div>)}</div>;
  return <div style={{display:'grid',gridTemplateColumns:'auto minmax(0,1fr)',gap:26,alignItems:'center',justifyContent:'center',padding:'4px 6px'}}>
    <svg viewBox={'0 0 ' + (C * S + 2) + ' ' + (R * S + 2)} style={{width:C * S + 2,maxWidth:'100%',display:'block'}} data-xw={keys.length}>
      {keys.map(([r, c]) => <g key={r + ',' + c}><rect x={1 + c * S} y={1 + r * S} width={S} height={S} fill="#fff" stroke={BK.ink} strokeWidth="1.3"/>
        {at[r + ',' + c] && <text x={3.5 + c * S} y={10.5 + r * S} fontSize="8.5" fontWeight="800" fill={BK.ink} style={{fontFamily:'Inter, sans-serif'}}>{at[r + ',' + c]}</text>}</g>)}
    </svg>
    <div style={{display:'grid',gap:16,minWidth:0}}>
      <div style={{display:'flex',flexWrap:'wrap',gap:'4px 12px'}}>{TMX_XW.map(x => x[0]).sort().map(w => <span key={w}>{tmxWord(w, 16)}</span>)}</div>
      {clues('A')}{clues('D')}
    </div>
  </div>;
}

// Chapter 25, Musical Terms, page 6: YOUR TURN was six meanings to name and then "make your own". Now the tiles: six
// little words, six terms, every tile used once -- a tile left over means one is in the wrong place. Four pairs are the
// room's own (più mosso, meno mosso, con moto, poco a poco cresc.); two are made the way the room makes them: sempre +
// legato like its sempre staccato ("short all the way"), molto + rit. like its molto cresc. ("getting much louder"), the
// molto rit. its own Teacher copy plays in the lesson.
const TMX_BUILD = ['più mosso', 'meno mosso', 'con moto', 'poco a poco cresc.', { w: 'sempre legato', a: 'sempre', b: 'legato', en: 'smoothly all the way' }, { w: 'molto rit.', a: 'molto', b: 'rit.', en: 'getting much slower' }];
const tmxBuildOf = (x) => typeof x === 'string' ? tmxOf(x) : x;
const TMX_TILES = [['molto', 'con', 'più', 'sempre', 'poco a poco', 'meno'], ['mosso', 'rit.', 'cresc.', 'moto', 'legato', 'mosso']];
function TmxBuild() {
  const tile = (w, k) => <span key={k} style={{border:'1.4px solid ' + BK.ink,borderRadius:6,padding:'3px 10px',background:'#fff'}} data-tile={w}>{tmxWord(w, 17)}</span>;
  return <div style={{display:'grid',gap:10}}>
    <div style={{display:'grid',gap:6,justifyItems:'center',padding:'4px 0'}}>{TMX_TILES.map((row, r) => <div key={r} style={{display:'flex',flexWrap:'wrap',justifyContent:'center',gap:8}}>{row.map((w, k) => tile(w, r + '-' + k))}</div>)}</div>
    <BkGrid cols={3} gap="8px 10px">{TMX_BUILD.map((x, i) => <BkCell key={i} n={i + 5}>{sdyCol(<>{tmxQuote('“' + tmxBuildOf(x).en + '”', 14)}<div style={{display:'flex',alignItems:'center',justifyContent:'center',gap:6,margin:'auto 0 6px',paddingTop:12}}>{bkBox(92, 36)}<span style={{fontWeight:900,color:BK.muted}}>+</span>{bkBox(74, 36)}</div></>, '6px 4px 6px')}</BkCell>)}</BkGrid>
  </div>;
}

// Chapter 27, Intervals, page 4: YOUR TURN drew the note above, as page 3 had. Now each note above gives a letter, and the
// four letters spell a word, so a wrong count shows itself. The same mix as before (a 6th, an octave, a 7th, a 6th;
// three treble, one bass): C, A, G, E.
const IVX_WORD = [[30, 'treble', 6], [19, 'bass', 8], [33, 'treble', 7], [32, 'treble', 6]];
const ivxWordOf = () => IVX_WORD.map(([d, , n]) => dName(d + n - 1)).join('');
function IvxWord() {
  return <div>
    <BkGrid cols={2} gap="8px 14px">{IVX_WORD.map(([d, clef, n], i) => <BkCell key={i} n={i + 5}>{sdyCol(<>{ivxAboveTitle(d, n)}<div style={{display:'grid',gridTemplateColumns:'minmax(0,1fr) auto',alignItems:'center',gap:8}}>{ivxWriteStaff(d, clef)}<span style={{display:'grid',justifyItems:'center',gap:2,fontSize:10.5,fontWeight:800,color:BK.muted,paddingRight:6}}>its letter{wbLetterBox('', { w: 36, h: 38 })}</span></div></>, '4px 4px 4px')}</BkCell>)}</BkGrid>
  </div>;
}

// Chapter 27, Intervals, page 5: PLAY was "your teacher plays six intervals". Now the four the child has just made harmonic,
// played both ways at home.
const IvxBothWays = () => <div style={{display:'grid',gridTemplateColumns:'repeat(4,minmax(0,1fr))',gap:10,width:'100%'}}>{IVX_WB.turn5.map((_, i) => <div key={i} style={{border:'1.2px solid ' + BK.line,borderRadius:8,padding:'8px 6px 10px',display:'grid',justifyItems:'center',gap:8}}><span style={{fontFamily:LB_SERIF,fontStyle:'italic',fontSize:16,fontWeight:800,color:BK.muted}}>{i + 5}</span>{wbTick('melodic')}{wbTick('harmonic')}</div>)}</div>;

// Chapter 28, Chords, page 3: PLAY was "your teacher plays six triads". Now the six the child has just made minor, played
// major then minor at home. (PLAY is 11: YOUR TURN is 5 to 10.)
const ChxMajMin = () => <div style={{display:'grid',gridTemplateColumns:'repeat(3,minmax(0,1fr))',gap:'10px 12px',width:'100%'}}>{CHX_WB.turn3.map((r, i) => <div key={i} style={{display:'flex',alignItems:'center',justifyContent:'center',gap:12,border:'1.2px solid ' + BK.line,borderRadius:8,padding:'10px 4px',flexWrap:'wrap'}}><span style={{fontFamily:LB_SERIF,fontSize:17,fontWeight:900,color:BK.ink}}>{prettyNote(r)}</span>{wbTick('major')}{wbTick('then minor')}</div>)}</div>;
