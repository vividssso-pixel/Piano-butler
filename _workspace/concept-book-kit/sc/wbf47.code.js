// Build EI (her 1 Nov 21:44 "yes" to going on the same way): the Grade 2 Workbooks, fun first -- only the parts better
// changed, none added. Rhythm, Grade 2's two PLAYs were sums and questions ("how many semiquavers in a crotchet?"); now
// they play the thing, with words: one beat a word, one note a syllable. Melody's PLAY loses its "make your own". Scales,
// Grade 2 and Intervals, Grade 2 stay as they are (set tasks; their weekly logs are how scales and intervals are practised).

// One beat a word, one note a syllable: in 2/4 and 4/4 (a crotchet beat) one syllable is a crotchet, two are two quavers,
// three a triplet, four four semiquavers; in 6/8 (a dotted crotchet beat) one is a dotted crotchet, two a duplet, three
// three quavers -- the room's own "three for two, two for three". Words with the weight on the first syllable.
const R2W_SIMPLE = { 1: 'a crotchet', 2: 'two quavers', 3: 'a triplet', 4: 'four semiquavers' };
const R2W_COMPOUND = { 1: 'a dotted crotchet', 2: 'a duplet', 3: 'three quavers' };
const r2wSyl = (w) => w.split('-').length;
const r2wNote = (ts, w) => (ts[1] === 8 ? R2W_COMPOUND : R2W_SIMPLE)[r2wSyl(w)];
// lines: [top, bottom], the words a beat each, the beats in a bar
const R2W_SEMI = [{ ts: [4, 4], words: ['pie', 'wa-ter-mel-on', 'ap-ple', 'pie'], bar: 4 }, { ts: [4, 4], words: ['wa-ter-mel-on', 'ap-ple', 'wa-ter-mel-on', 'pie'], bar: 4 }];
const R2W_TRIP = [{ ts: [2, 4], words: ['pine-ap-ple', 'ap-ple', 'pine-ap-ple', 'pie'], bar: 2 }, { ts: [6, 8], words: ['ap-ple', 'pine-ap-ple', 'ap-ple', 'pie'], bar: 2 }];
function R2WordLine({ line, n }) {
  const bars = []; for (let i = 0; i < line.words.length; i += line.bar) bars.push(line.words.slice(i, i + line.bar).map((w, k) => [w, i + k]));
  return <div style={{display:'flex',alignItems:'flex-end',justifyContent:'center',gap:8}} data-r2w={line.ts.join('/')}>
    <span style={{alignSelf:'center'}}>{nvNum(n)}</span><span style={{alignSelf:'center',width:30,display:'flex',justifyContent:'center'}}><R4TsSig top={line.ts[0]} bot={line.ts[1]} size={24}/></span>
    {bars.map((b, j) => <div key={j} style={{display:'flex',alignItems:'flex-end',padding:'2px 0',borderRight:(j === bars.length - 1 ? '3px' : '1.6px') + ' solid ' + BK.ink}}>
      {b.map(([w, k]) => <div key={k} style={{display:'grid',justifyItems:'center',gap:4,padding:'0 7px'}} data-word={w}><span style={{fontFamily:LB_SERIF,fontStyle:'italic',fontWeight:800,fontSize:15,color:BK.ink,whiteSpace:'nowrap'}}>{w}</span>{bkBox(line.words.length > 4 ? 96 : 112, 52)}</div>)}</div>)}
  </div>;
}
const R2WordLines = ({ lines, n0 }) => <div style={{display:'grid',gap:10,padding:'2px 0'}}>{lines.map((l, i) => <R2WordLine key={i} line={l} n={n0 + i}/>)}{ivxTicks(['said and clapped', 'played on one note'])}</div>;
const r2wAns = (lines) => lines.map(l => { const out = []; l.words.forEach((w, k) => { if (k && k % l.bar === 0) out.push('|'); out.push(r2wNote(l.ts, w)); }); return out.join(', ').replace(/, \|, /g, ' | '); });
