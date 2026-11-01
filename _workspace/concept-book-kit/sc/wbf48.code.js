// Build EJ (her 1 Nov 23:32 "keep going"): the Grade 3 Workbooks, fun first -- only the parts better changed, none added.
// Rhythm, Grade 3's three PLAYs were questions ("how many beats in a bar of 3/2?", "S or C?"), the same as its check-up on
// paper; now they play the thing with Grade 2's words, one beat a word, one note a syllable. Writing a Melody (the writing
// is the page), Scales, Grade 3 (its check-up only) and Chords and Cadences, Grade 3 (written PLAYs beside played weeks)
// stay as they are.

// The beat and its parts: the bottom number gives the beat (2 a minim, 4 a crotchet, 8 a quaver), except 6/8 and 9/8, whose
// beat is a dotted crotchet in three quavers -- the room's own simple and compound.
const R3_PARTS = { 2: { 1: 'a minim', 2: 'two crotchets', 4: 'four quavers' }, 4: { 1: 'a crotchet', 2: 'two quavers', 3: 'a triplet', 4: 'four semiquavers' }, 8: { 1: 'a quaver', 2: 'two semiquavers' }, c: { 1: 'a dotted crotchet', 2: 'a duplet', 3: 'three quavers' } };
const r3Compound = (ts) => ts[1] === 8 && ts[0] % 3 === 0 && ts[0] > 3;
const r3Note = (ts, w, dotted) => dotted && r2wSyl(w) === 2 ? 'a dotted quaver and a semiquaver' : R3_PARTS[r3Compound(ts) ? 'c' : ts[1]][r2wSyl(w)];
const r3Ans = (lines) => lines.map(l => { const out = []; l.words.forEach((w, k) => { if (k && k % l.bar === 0) out.push('|'); out.push(r3Note(l.ts, w, l.dotted)); }); return (l.dotted ? 'dotted: ' : l.even ? 'even: ' : '') + out.join(', ').replace(/, \|, /g, ' | '); });

// Page 2 (dotted rhythms): the same words drawn even, then dotted -- long, short, counted 1 a.
const R3W_DOT = [{ ts: [4, 4], words: ['ap-ple', 'ap-ple', 'ap-ple', 'pie'], bar: 4, even: true }, { ts: [4, 4], words: ['ap-ple', 'ap-ple', 'ap-ple', 'pie'], bar: 4, dotted: true }];
// Page 3 (the minim beat): in 2/2 and 3/2 a beat is a minim, so pie is a minim and wa-ter-mel-on four quavers.
const R3W_MIN = [{ ts: [2, 2], words: ['pie', 'ap-ple', 'wa-ter-mel-on', 'pie'], bar: 2 }, { ts: [3, 2], words: ['ap-ple', 'wa-ter-mel-on', 'pie'], bar: 3 }];
const R3WordLines = ({ lines, n0 }) => <div style={{display:'grid',gap:10,padding:'2px 0'}}>{lines.map((l, i) => <div key={i} style={{display:'grid',gridTemplateColumns:'64px minmax(0,1fr)',alignItems:'center'}}>
  <span style={{fontSize:11,fontWeight:900,letterSpacing:'0.08em',color:l.dotted ? BK.coral : BK.muted,textAlign:'right',paddingTop:18}}>{l.dotted ? 'DOTTED' : l.even ? 'EVEN' : ''}</span><R2WordLine line={l} n={n0 + i}/></div>)}{ivxTicks(['said and clapped', 'played on one note'])}</div>;

// Page 4 (3/8 and 9/8): say one bar of each time signature in words, one word a beat -- ap-ple for a beat that splits in
// two (simple), pine-ap-ple for one that splits in three (compound) -- then S or C. The words are the answer, so the
// number of words shows the beats in the bar.
const R3_SC = [[9, 8], [6, 8], [3, 8], [3, 4]];   // the left column wider: 9/8 takes three pine-ap-ples
const r3ScWords = (ts) => { const c = r3Compound(ts), n = c ? ts[0] / 3 : ts[0]; return Array(n).fill(c ? 'pine-ap-ple' : 'ap-ple'); };
const R3SayBars = ({ n0 }) => <div style={{display:'grid',gap:10}}>
  <div style={{display:'grid',gridTemplateColumns:'minmax(0,1.4fr) minmax(0,1fr)',gap:'8px 12px'}}>{R3_SC.map((ts, i) => <BkCell key={i} n={n0 + i}><div style={{display:'grid',gridTemplateColumns:'30px minmax(0,1fr) auto',alignItems:'end',gap:8,padding:'14px 8px 8px'}} data-r3sc={ts.join('/')}>
    <span style={{alignSelf:'center'}}><R4TsSig top={ts[0]} bot={ts[1]} size={23}/></span><div style={{borderBottom:'1.3px solid ' + BK.line,height:34}}/>
    <span style={{display:'grid',justifyItems:'center',gap:2,fontSize:10.5,fontWeight:800,color:BK.muted}}>S or C{bkBox(36, 32)}</span></div></BkCell>)}</div>
  {ivxTicks(['said and clapped, leaning on each word'])}</div>;
