// ─── Phase 483: chapter 27's Workbook (pages 2 to 8: one per lesson step, my styles, the check-up) and the Teacher
// copy. English only. r1: three parts and the piano box on every page; words to circle where the answer is a choice; the
// texture pictures drawn alike (one range, ten beats, no coral) so that only the texture tells them apart. ───
const CSX_WB = {
  tex: [['monophony', 'a'], ['homophony', 'b'], ['polyphony', 'a'], ['monophony', 'c']],
  texName: [['a song sung alone, with no instruments', 'monophony'], ['a round sung by two groups', 'polyphony'], ['a tune with left-hand chords under it', 'homophony'], ['a choir all singing the same tune, with no instruments', 'monophony']],
  join: { left: [['busy lines woven together', 'baroque'], ['a clear tune over light chords', 'classical'], ['long singing tunes and rubato', 'romantic'], ['new scales and strong rhythms', 'modern'], ['short patterns repeated', 'contemporary']],
    right: ['romantic', 'baroque', 'contemporary', 'classical', 'modern'] },
  circle: [['many ornaments, such as trills', 'baroque'], ['music for films and games', 'contemporary'], ['balanced phrases, like question and answer', 'classical'], ['rich chords and pedal', 'romantic'], ['jazz and folk mixed in', 'modern'], ['any sound at all, even silence', 'contemporary']],
  keys: [['C D E G A', [0, 2, 4, 7, 9]], ['the five black keys', [1, 3, 6, 8, 10]], ['G A B D E', [7, 9, 11, 2, 4]]],
  // a major scale without its 4th and 7th: one set in each row
  penta: [['C D E F G', 'F G A C D', 'C D E G'], ['B♭ C D E♭ F', 'B♭ C D F G', 'B♭ D F'], ['D E F A B', 'D F♯ A', 'D E F♯ A B'],
    ['E F♯ G♯ B C♯', 'E F♯ G A B', 'E G♯ B'], ['A B C D E', 'A C E', 'A B C♯ E F♯'], ['E♭ F G A♭ B♭', 'E♭ F G B♭ C', 'E♭ G B♭']],
  tune: 'Write eight notes using only C D E G A, ending on C. Play it.',
  gaps: [4, 5, 8, 9, 10],
  iv: ['I', 'IV', 'V'],
  swing: [true, false, true, false, false, true],
  vc: [['it usually comes first, before the first chorus', 'verse'], ['it often holds the song’s title', 'chorus'], ['the part people sing along to most', 'chorus'], ['it tells the story, line by line', 'verse']],
  // a song made up for this page: verse, chorus, verse, chorus, bridge, chorus (the chorus's words the same each time)
  song: [['I woke up in the morning,', 'the sun was on the keys.', 'V'], ['Play it again, play it again,', 'play it all day long!', 'C'],
    ['I counted beats at lunchtime,', 'my fingers tapped along.', 'V'], ['Play it again, play it again,', 'play it all day long!', 'C'],
    ['Slow down, quiet now,', 'listen to the rain.', 'B'], ['Play it again, play it again,', 'play it all day long!', 'C']],
  words: [[['texture', 'how the lines of music are layered'], ['monophony', 'one line alone'], ['homophony', 'a tune with chords underneath'], ['polyphony', 'two or more tunes at once, each as important as the other']],
    [['style', 'the way music sounds'], ['ornament', 'a quick decoration of a note, such as a trill'], ['minimalism', 'short patterns repeated many times, changing slowly']],
    [['folk music', 'the songs and dances of a people, passed on by ear'], ['pentatonic scale', 'a major scale without its 4th and 7th notes'], ['nationalism', 'using your own country’s folk music in concert music']],
    [['blues', 'music from African American communities of the southern USA, from the late 1800s'], ['12-bar blues', 'three chords over twelve bars'], ['swing', 'pairs of quavers played long-short']],
    [['popular music', 'music made for many listeners'], ['verse', 'the same tune with new words each time'], ['chorus', 'the part that comes back with the same words']]],
};
const CSX_CHK = {
  tex: [['polyphony', 'c'], ['monophony', 'b'], ['homophony', 'a'], ['homophony', 'c']],
  era: [['busy lines woven together', 'baroque'], ['short patterns repeated, in minimalism', 'contemporary'], ['an Alberti bass in the left hand', 'classical'], ['rubato that stretches the time', 'romantic']],
  word: ['homophony', 'pentatonic scale', 'swing', 'chorus'],
  bars: [4, 8, 9],
  sets: [['C D E G A', 'C D E F G', 'C E F G A'], ['C D E F G A B', 'F♯ G♯ A♯ C♯ D♯', 'D E F A B']],
};
const csxChkNo = () => { const C = CSX_CHK, nB = C.tex.length + 1, nC = nB + C.era.length, nD = nC + C.word.length, nE = nD + C.bars.length; return { nB, nC, nD, nE, total: nE + C.sets.length - 1 }; };
// a set of note names is a pentatonic scale here: five notes, the shape of C D E G A (a major scale without its 4th and
// 7th) on some note (r1: not merely five notes without half steps, which C D E F♯ G♯ also is)
const csxIsPenta = (set) => { const pc = { C: 0, D: 2, E: 4, F: 5, G: 7, A: 9, B: 11 }, n = set.split(' ').map(x => (pc[x[0]] + (x.includes('♯') ? 1 : x.includes('♭') ? -1 : 0) + 12) % 12);
  return n.length === 5 && new Set(n).size === 5 && [...Array(12).keys()].some(k => [0, 2, 4, 7, 9].every(x => n.includes((x + k) % 12))); };
const csxEraEn = (id) => CMP_PERIODS[id].name[0].replace(/ \(.*\)$/, '');
// words to circle: room around each for a pencil ring
const csxCircle = (words, fs = 13) => <div style={{display:'flex',justifyContent:'center',gap:'6px 8px',flexWrap:'wrap',fontSize:fs,fontWeight:800,color:BK.ink}}>{words.map(w => <span key={w} style={{padding:'3px 8px',whiteSpace:'nowrap'}}>{w}</span>)}</div>;
const csxLine = (h = 30) => <div style={{borderBottom:'1.3px solid ' + BK.line,height:h,margin:'auto 8px 4px'}}/>;
// join each sound to its period: phrases on the left, periods on the right; the first pair joined
function CsxJoin({ left, right, n0, rowH = 30, rname = csxEraEn, what = ['Sounds', 'Periods'] }) {
  const W = 680, H = left.length * rowH + 4, xl = 330, xr = 450, yl = (i) => 4 + i * rowH + rowH / 2;
  return <svg viewBox={`0 0 ${W} ${H}`} role="img" aria-label={what[0] + ': ' + left.map(x => x[0]).join('; ') + '. ' + what[1] + ': ' + right.map(rname).join('; ') + '.'} style={{width:'100%',height:'auto',display:'block',fontFamily:'Inter, system-ui, sans-serif'}}>
    {left.map(([w], i) => <g key={'l' + i}><text x={0} y={yl(i) + 4.5} fontSize="13" fontWeight="700" fontStyle="italic" fill={i === 0 ? BK.coral : BK.ink} style={{fontFamily:LB_SERIF}}>{n0 + i}</text><text x={xl - 12} y={yl(i) + 4.5} textAnchor="end" fontSize="13.5" fontWeight="700" fill={BK.ink}>{w}</text><circle cx={xl} cy={yl(i)} r="3.6" fill={BK.ink}/></g>)}
    {right.map((id, i) => <g key={'r' + id}><circle cx={xr} cy={yl(i)} r="3.6" fill={BK.ink}/><text x={xr + 12} y={yl(i) + 4.5} fontSize="13.5" fontWeight="900" fill={BK.ink}>{rname(id)}</text></g>)}
    <line x1={xl} y1={yl(0)} x2={xr} y2={yl(right.indexOf(left[0][1]))} stroke={BK.coral} strokeWidth="2"/>
  </svg>;
}
const csxHandW = (txt) => <span style={{fontFamily:"'Caveat', 'Comic Sans MS', cursive",fontSize:20,color:BK.coral,fontWeight:700}}>{txt}</span>;
const csxNo = (n) => <span style={{fontFamily:LB_SERIF,fontStyle:'italic',fontSize:13,fontWeight:700,color:BK.ink}}>{n}</span>;

function CsxWorkbook({ startNo = 1 }) {
  const W = CSX_WB, pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={startNo + 1 + pages.length} chId="styles">{content}</WbPage>);
  const words = (k, n0) => <Part kind="home" title="The words" how="Write the word for each meaning.">
    <BkGrid cols={W.words[k].length} gap="6px 10px">{W.words[k].map(([w, mean], i) => <BkCell key={w} n={n0 + i}>{sdyCol(<><div style={{textAlign:'center',fontSize:12.5,fontWeight:800,color:BK.ink,marginTop:14,lineHeight:1.3,textWrap:'balance'}}>“{mean}”</div>{csxLine(34)}</>, '6px 2px 8px')}</BkCell>)}</BkGrid></Part>;
  const play = (n, ticks, how = 'Play, then tick each.', before = null) => <Part kind="play" title="At the piano" how={how}>{before}{sskRowN(n, ivxTicks(ticks))}</Part>;

  // 2 (faces "Texture")
  P(<>
    <WbTop step={1}/>
    <Part kind="together" title="Which texture?" how="Each block is a note: higher is higher, longer is longer. Circle the texture. The first one is done.">
      <BkGrid cols={2} gap="8px 10px">{W.tex.map(([x, tune], i) => <ExCell key={i} n={i + 1} ex={i === 0}>{sdyCol(<><div style={{maxWidth:300,margin:'0 auto',width:'100%'}}><CsxRoll tex={x} tune={tune} mini even label={'A tune drawn as blocks, in one of the three textures.'}/></div>
        <div style={{display:'flex',justifyContent:'center',gap:6,marginTop:'auto'}}>{CSX_TEX.map(w => <span key={w} style={{fontSize:13,fontWeight:800,color:BK.ink,padding:'2px 8px',border:'1.5px solid ' + (i === 0 && w === x ? BK.coral : 'transparent'),borderRadius:12}}>{w}</span>)}</div></>, '18px 6px 6px')}</ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="Name it" how="Circle the texture.">
      <BkGrid cols={2} gap="6px 10px">{W.texName.map(([d], i) => <BkCell key={i} n={i + 5}>{sdyCol(<><div style={{textAlign:'center',fontSize:13.5,fontWeight:800,color:BK.ink,margin:'6px 0 8px',lineHeight:1.3,textWrap:'balance'}}>“{d}”</div>{csxCircle(CSX_TEX)}</>, '14px 4px 8px')}</BkCell>)}</BkGrid>
    </Part>
    {words(0, 9)}
    {play(13, ['a tune alone', 'with left-hand chords', 'two tunes at once'], 'Play, then tick each. Two tunes: right hand C D E F G up while the left hand plays G F E D C down.')}
    <Faces/>
  </>);
  // 3 (faces "The sound of each period")
  P(<>
    <WbTop step={2}/>
    <Part kind="together" title="Join each sound to its period" how="Join with a line. The first one is done.">
      <div style={{border:'0.8px solid ' + BK.hair,padding:'8px 10px'}}><CsxJoin left={W.join.left} right={W.join.right} n0={1} rowH={34}/></div>
    </Part>
    <Part kind="home" title="Which period?" how="Circle the period that sounds like this.">
      <BkGrid cols={2} gap="6px 10px">{W.circle.map(([d], i) => <BkCell key={i} n={i + 6}>{sdyCol(<><div style={{textAlign:'center',fontSize:13.5,fontWeight:800,color:BK.ink,margin:'4px 0 6px',textWrap:'balance'}}>“{d}”</div>{csxCircle(MTL_ERAS.map(csxEraEn), 12.5)}</>, '14px 4px 6px')}</BkCell>)}</BkGrid>
    </Part>
    {words(1, 12)}
    {play(15, ['a piece: its period', 'one sound that shows it', 'a pattern, repeated'])}
    <Faces/>
  </>);
  // 4 (faces "Folk music")
  P(<>
    <WbTop step={3}/>
    <Part kind="together" title="Colour the five notes" how="Colour each pentatonic scale on its keys. The first one is done.">
      <BkGrid cols={3} gap="8px 10px">{W.keys.map(([nm, pcs], i) => <ExCell key={i} n={i + 1} ex={i === 0}>{sdyCol(<><div style={{textAlign:'center',fontSize:14,fontWeight:900,color:BK.ink,margin:'4px 0 8px'}}>{csxNotes(nm)}</div><div style={{maxWidth:230,margin:'0 auto',width:'100%'}}><CsxKeys on={i === 0 ? pcs : []} letters={false} hollow kh={118} label={'One octave of keys, the black keys open' + (i === 0 ? ', C D E G A filled.' : ', to colour.')}/></div></>, '14px 6px 8px')}</ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="Five notes?" how="Five notes with no half steps between them: a major scale without its 4th and 7th. Circle the pentatonic scale in each.">
      <BkGrid cols={3} gap="6px 10px">{W.penta.map((set, i) => <BkCell key={i} n={i + 4}>{sdyCol(<div style={{display:'flex',flexDirection:'column',alignItems:'center',gap:8,fontSize:15,fontWeight:900,color:BK.ink,margin:'auto 0'}}>{set.map(x => <span key={x} style={{whiteSpace:'nowrap',padding:'2px 8px'}}>{csxNotes(x)}</span>)}</div>, '18px 4px 8px')}</BkCell>)}</BkGrid>
    </Part>
    {words(2, 10)}
    {play(14, ['C D E G A', 'my folk tune', 'a folk song I know'], W.tune + ' Then tick each.',
      <div style={{display:'grid',gridTemplateColumns:'26px repeat(8,minmax(0,1fr))',alignItems:'center',gap:8,margin:'0 0 10px'}}>{csxNo(13)}{Array.from({ length: 8 }, (_, i) => <div key={i} style={{height:50,border:'1.4px solid ' + BK.line,borderRadius:4,display:'flex',alignItems:'center',justifyContent:'center'}}>{i === 7 && csxHandW('C')}</div>)}</div>)}
    <Faces/>
  </>);
  // 5 (faces "Blues and jazz")
  P(<>
    <WbTop step={4}/>
    <Part kind="together" title="Fill in the 12-bar blues" how="Write I, IV or V in each empty bar. Then write the letter name of each chord in C.">
      <div style={{border:'0.8px solid ' + BK.hair,padding:'8px 10px'}}>
        <div style={{maxWidth:520,margin:'0 auto'}}><CsxBlues gaps={W.gaps} nums={W.gaps.map((g, i) => i + 1)} letters={false} ch={52} label={'The 12-bar blues with bars ' + W.gaps.map(i => i + 1).join(', ') + ' empty, numbered 1 to 5.'}/></div>
        <div style={{display:'flex',justifyContent:'center',gap:28,margin:'12px 0 4px'}}>{W.iv.map((r, i) => <div key={r} style={{display:'flex',alignItems:'flex-end',gap:8,fontSize:19,fontWeight:900,color:BK.ink}}>{csxNo(i + 6)}<span>{r} =</span><span style={{width:56,borderBottom:'1.3px solid ' + BK.line,height:28}}/></div>)}</div>
      </div>
    </Part>
    <Part kind="home" title="Straight or swing?" how="Each pair of blocks is two quavers. Circle straight or swing.">
      <BkGrid cols={3} gap="6px 10px">{W.swing.map((sw, i) => <BkCell key={i} n={i + 9}>{sdyCol(<><div style={{maxWidth:200,margin:'8px auto 10px',width:'100%'}}><CsxSwing swing={sw} H={40} label={'Four beats of quavers, even or long-short.'}/></div>{csxCircle(['straight', 'swing'])}</>, '16px 4px 8px')}</BkCell>)}</BkGrid>
    </Part>
    {words(3, 15)}
    {play(18, ['the 12-bar blues in C', 'quavers straight', 'quavers swung'])}
    <Faces/>
  </>);
  // 6 (faces "Pop")
  P(<>
    <WbTop step={5}/>
    <Part kind="together" title="Verse or chorus?" how="Circle one. The first one is done.">
      <BkGrid cols={2} gap="6px 10px">{W.vc.map(([d, a], i) => <ExCell key={i} n={i + 1} ex={i === 0}>{sdyCol(<><div style={{textAlign:'center',fontSize:13.5,fontWeight:800,color:BK.ink,margin:'4px 0 6px',textWrap:'balance'}}>“{d}”</div>
        <div style={{display:'flex',justifyContent:'center',gap:8}}>{['verse', 'chorus'].map(w => <span key={w} style={{fontSize:13,fontWeight:800,color:BK.ink,padding:'2px 8px',border:'1.5px solid ' + (i === 0 && w === a ? BK.coral : 'transparent'),borderRadius:12}}>{w}</span>)}</div></>, '16px 4px 10px')}</ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="A song’s parts" how="Read the words. Write V (verse), C (chorus) or B (bridge) in the box beside each part. The first one is done.">
      <div style={{display:'flex',flexDirection:'column',gap:9,maxWidth:520,margin:'0 auto',width:'100%'}}>{W.song.map(([l1, l2, a], i) => <div key={i} style={{display:'grid',gridTemplateColumns:'26px 50px minmax(0,1fr)',alignItems:'center',gap:12}}>{csxNo(i + 5)}
        <div style={{height:44,border:'1.4px solid ' + (i === 0 ? BK.coral : BK.line),borderRadius:6,display:'flex',alignItems:'center',justifyContent:'center'}}>{i === 0 && csxHandW(a)}</div>
        <div style={{fontFamily:LB_SERIF,fontStyle:'italic',fontSize:14.5,color:BK.ink,lineHeight:1.3}}>{l1}<br/>{l2}</div></div>)}</div>
    </Part>
    {words(4, 11)}
    {play(14, ['C G Am F, again and again', 'a song: its verse', 'its chorus'])}
    <Faces/>
  </>);
  P(<CsxMyStyles/>);
  P(<CsxPaperCheck/>);
  return <>{pages}</>;
}

function CsxMyStyles() {
  const head = ['My piece', 'Texture', 'Period or style', 'One sound I hear'];
  const cols = 'minmax(0,1.3fr) minmax(0,1fr) minmax(0,1fr) minmax(0,1.4fr)';
  return <>
    <WbTop step={7}/>
    <div style={{display:'flex',justifyContent:'space-between',alignItems:'flex-end',gap:12,margin:'0 0 2px'}}>
      <div style={{minWidth:0}}><div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>ANY PIECE</div><div style={{fontSize:12.5,color:BK.muted,textWrap:'pretty'}}>Keep this page all year. Add each new piece you learn.</div></div></div>
    <Part kind="together" title="My pieces’ styles" how="For each piece: its texture, its period or style, and one sound in it that shows it.">
      <div style={{border:'0.8px solid ' + BK.hair}}>
        <div style={{display:'grid',gridTemplateColumns:cols,gap:8,padding:'6px 10px',borderBottom:'1px solid ' + BK.line,fontSize:10.5,fontWeight:900,letterSpacing:'0.07em',textTransform:'uppercase',color:BK.muted}}>{head.map(h => <span key={h}>{h}</span>)}</div>
        {Array.from({ length: 12 }, (_, i) => <div key={i} style={{display:'grid',gridTemplateColumns:cols,gap:8,padding:'0 10px',height:34,borderBottom:'0.8px solid ' + BK.hair}}>{head.map(h => <span key={h} style={{borderRight:h === head[3] ? 'none' : '0.8px dotted ' + BK.hair}}/>)}</div>)}
      </div>
    </Part>
    <Part kind="home" title="Listen at home" how="Find a piece or song of each style. Write its name.">
      <div style={{display:'flex',flexDirection:'column',gap:6}}>{['folk', 'classical', 'jazz or blues', 'pop'].map((g, i) => <div key={g} style={{display:'grid',gridTemplateColumns:'26px 120px minmax(0,1fr)',alignItems:'end',gap:8,fontSize:14,fontWeight:900,color:BK.ink,minHeight:40}}><span style={{fontFamily:LB_SERIF,fontStyle:'italic',fontWeight:700}}>{i + 1}</span><span>{g}</span><span style={{borderBottom:'1.3px solid ' + BK.line,height:28}}/></div>)}</div>
    </Part>
    <Part kind="play" title="At the piano" how="Play each piece on your list. Say its texture, its period or style, and one sound. Tick each.">{sskRowN(5, ivxTicks(['texture', 'period or style', 'one sound']))}</Part>
    <Faces/>
  </>;
}
function CsxPaperCheck() {
  const C = CSX_CHK, { nB, nC, nD, nE } = csxChkNo();
  return <div className="lb-paper" style={{display:'flex',flexDirection:'column',gap:15,flex:'1 0 auto'}}>
    <LbPaperHead/>
    {bkSec('A', 'Which texture? Circle one.')}
    <BkGrid cols={4} gap="6px 10px">{C.tex.map(([x, tune], i) => <BkCell key={i} n={i + 1}>{sdyCol(<><div style={{maxWidth:200,margin:'0 auto',width:'100%'}}><CsxRoll tex={x} tune={tune} mini even W={220} label={'A tune drawn as blocks.'}/></div><div style={{marginTop:'auto',display:'flex',flexDirection:'column',alignItems:'center',gap:6,fontSize:13,fontWeight:800,color:BK.ink}}>{CSX_TEX.map(w => <span key={w} style={{padding:'1px 8px'}}>{w}</span>)}</div></>, '16px 2px 6px')}</BkCell>)}</BkGrid>
    {bkSec('B', 'Which period sounds like this? Circle one.')}
    <BkGrid cols={2} gap="6px 10px">{C.era.map(([d], i) => <BkCell key={i} n={nB + i}>{sdyCol(<><div style={{textAlign:'center',fontSize:13.5,fontWeight:800,color:BK.ink,margin:'4px 0 6px'}}>“{d}”</div>{csxCircle(MTL_ERAS.map(csxEraEn), 12.5)}</>, '12px 4px 6px')}</BkCell>)}</BkGrid>
    {bkSec('C', 'Write the word.')}
    <BkGrid cols={4} gap="6px 10px">{C.word.map((w, i) => <BkCell key={w} n={nC + i}>{sdyCol(<><div style={{textAlign:'center',fontSize:12.5,fontWeight:800,color:BK.ink,marginTop:14,lineHeight:1.3,textWrap:'balance'}}>“{CSX_WORDS.find(x => x[0] === w)[1]}”</div>{csxLine(34)}</>, '6px 2px 8px')}</BkCell>)}</BkGrid>
    {bkSec('D', 'The 12-bar blues: write the chord of each bar (I, IV or V).')}
    <BkGrid cols={3} gap="6px 10px">{C.bars.map((b, i) => <BkCell key={b} n={nD + i}>{sdyCol(<div style={{display:'flex',alignItems:'flex-end',justifyContent:'center',gap:10,fontSize:15,fontWeight:900,color:BK.ink,margin:'auto 0'}}><span>bar {b + 1}</span><span style={{width:70,borderBottom:'1.3px solid ' + BK.line,height:26}}/></div>, '16px 4px 8px')}</BkCell>)}</BkGrid>
    {bkSec('E', 'Circle the pentatonic scale.')}
    <BkGrid cols={2} gap="6px 10px">{C.sets.map((set, i) => <BkCell key={i} n={nE + i}>{sdyCol(<div style={{display:'flex',flexDirection:'column',alignItems:'center',gap:10,fontSize:14,fontWeight:900,color:BK.ink,margin:'auto 0'}}>{set.map(x => <span key={x} style={{whiteSpace:'nowrap',padding:'1px 8px'}}>{csxNotes(x)}</span>)}</div>, '14px 4px 8px')}</BkCell>)}</BkGrid>
  </div>;
}

function CsxTeacher() {
  const W = CSX_WB, C = CSX_CHK, pages = [], { nB, nC, nD, nE, total } = csxChkNo();
  const P = (content) => pages.push(<WbPage key={pages.length} no={pages.length + 1} chId="styles" teacher>{content}</WbPage>);
  const done = (i) => i === 0 ? ' (done)' : '';
  const nb = (x) => String(x).replace(/ /g, ' ');
  const wordAns = (k, n0) => skgTcAns('THE WORDS', W.words[k].map(w => nb(w[0])), n0);
  const ms = bkChapterNo('more-scales');
  P(<>
    <div style={{fontFamily:"'Playfair Display', Georgia, serif",fontSize:28,fontWeight:900,color:BK.ink,margin:'2px 0 2px'}}>Teacher copy · {bkChapterName('styles')}</div>
    <div style={{fontSize:12.5,color:BK.muted,margin:'0 0 8px',lineHeight:1.5}}>{'How music sounds, on chapter ' + bkChapterNo('composers') + '’s timeline: texture, the sound of each period, and four style families (folk, classical, jazz and blues, pop). Chapter ' + bkChapterNo('chords') + ' (triads) and chapter ' + bkChapterNo('form') + ' (repetition, sections) come first' + (ms ? '; chapter ' + ms + ' takes the pentatonic and blues scales further' : '') + '. AMEB: general knowledge (the style of each exam piece).'}</div>
    <TcBlock page={2} title="Texture" answers={<>{sscLesson('A tune alone, then with left-hand chords; a round with the teacher (start at bar 3).')}{skgTcAns('TRY IT', W.tex.map(([x], i) => x + done(i)))}{skgTcAns('YOUR TURN', W.texName.map(([, a]) => a), 5)}{wordAns(0, 9)}</>}
      watch="Homophony called polyphony because there are many notes at once: polyphony needs two tunes, each moving on its own. A held chord under a tune is homophony. A choir on one tune, with no instruments, is still monophony."
      say="“One line, a tune with chords, or tunes together?”"/>
    <TcBlock page={3} title="The sound of each period" answers={<>{sscLesson('A piece, its period, and one sound that shows it; a short pattern repeated and changed slowly (minimalism).')}{skgTcAns('TRY IT', W.join.left.map(([w, id], i) => w + ': ' + csxEraEn(id) + done(i)))}{skgTcAns('YOUR TURN', W.circle.map(([, id]) => csxEraEn(id)), 6)}{wordAns(1, 12)}</>}
      watch="Any old-sounding piece called Baroque. The pedal is the quickest clue to Romantic, but pedal alone can also mean Debussy (Modern): ask what else they hear. An Alberti bass points to Classical; ornaments and two busy hands to Baroque."
      say="“What do you hear first: woven lines, a clear tune, or big feelings?”"/>
    <TcBlock page={4} title="Folk music" answers={<>{sscLesson('C D E G A up and down, then a tune made up on them; a folk song the student knows.')}{skgTcAns('TRY IT', W.keys.map(([nm], i) => nb(nm) + done(i)))}{skgTcAns('YOUR TURN', [...W.penta.map(set => nb(set.find(x => csxIsPenta(x))))], 4)}{wordAns(2, 10)}{skgTcAns('AT THE PIANO', ['any eight of C D E G A, ending on C'], 13)}</>}
      watch="F or B slipped into the tune. A set with no half steps taken for pentatonic: C D E F♯ G♯ has none, but it is not the shape; a major scale without its 4th and 7th is. The black keys are the same shape on F♯."
      say="“A major scale without 4 and 7.”"/>
  </>);
  P(<>
    <TcBlock page={5} title="Blues and jazz" answers={<>{sscLesson('The 12-bar blues in C in the left hand (C, F, G, a chord a bar); quavers straight, then swung.')}{skgTcAns('TRY IT', [...W.gaps.map(i => nb('bar ' + (i + 1) + ': ' + BLUES_12[i])), 'I = C', 'IV = F', 'V = G'])}{skgTcAns('YOUR TURN', W.swing.map(sw => sw ? 'swing' : 'straight'), 9)}{wordAns(3, 15)}</>}
      watch="Swing played as dotted rhythms (too sharp): long-short is two parts of a triplet, then one. Bar 10 played as V: it is IV."
      say="“I I I I · IV IV I I · V IV I I.”"/>
    <TcBlock page={6} title="Pop" answers={<>{sscLesson('C G Am F, four beats each, looped; a song the student knows, pointing at verse and chorus.')}{skgTcAns('TRY IT', W.vc.map(([, a], i) => a + done(i)))}{skgTcAns('YOUR TURN', W.song.map(([, , a], i) => a + done(i)), 5)}{wordAns(4, 11)}</>}
      watch="A chorus taken for a verse because its tune is the same: the words decide. The bridge taken for a verse: it comes once, near the end, with a new tune. Am played as A major (C, not C♯)."
      say="“The verse changes its words; the chorus comes back the same.”"/>
    <TcBlock page={7} title="Any piece: my pieces’ styles (one page, kept all year)" answers={<div style={{fontSize:12,color:BK.ink,lineHeight:1.5}}>Texture, period or style, one sound. Many exam pieces are homophony; Baroque pieces are often two-part polyphony.</div>}/>
    <TcBlock page={8} title="The check-up on paper (the Workbook’s last page)" answers={<>
      {skgTcAns('A', C.tex.map(([x]) => x))}
      {skgTcAns('B', C.era.map(([, id]) => csxEraEn(id)), nB)}
      {skgTcAns('C', C.word.map(nb), nC)}
      {skgTcAns('D', C.bars.map(b => nb('bar ' + (b + 1) + ': ' + BLUES_12[b])), nD)}
      {skgTcAns('E', C.sets.map(set => nb(set.find(x => csxIsPenta(x)))), nE)}
      <div style={{fontSize:12,color:BK.ink,marginTop:6,lineHeight:1.5}}>One mark each, {total} in all. A section with a wrong answer is not passed yet: go back to its pages. Also listen to the student (My five checks, page 7).</div>
    </>}
      goBack={[{ id: 'a', step: '1', page: '2' }, { id: 'b', step: '2', page: '3' }, { id: 'c', step: '1 to 5', page: '2 to 6' }, { id: 'd', step: '4', page: '5' }, { id: 'e', step: '3', page: '4' }]}/>
    <div style={{border:'0.8px solid ' + BK.hair,padding:'6px 12px',fontSize:12,color:BK.ink,lineHeight:1.5}}><b style={{color:BK.coral}}>The drill (after page 6).</b> {['1 which texture (a picture)', '2 listening: which texture', '3 which period sounds like this', '4 which style', '5 the 12-bar blues', '6 listening: straight or swing', '7 which five notes', '8 the words', '9 extra: listening: which style'].map((x, i) => <React.Fragment key={i}>{i ? ' · ' : ''}<span style={{whiteSpace:'nowrap'}}>{x}</span></React.Fragment>)} (2, 6 and 9 on screen only).</div>
    <div style={{border:'0.8px solid ' + BK.hair,padding:'6px 12px',margin:'8px 0 0',fontSize:11.5,color:BK.ink,lineHeight:1.42}}><b style={{color:BK.coral}}>Words and sounds.</b> Polyphony is the texture; counterpoint (chapter {bkChapterNo('composers')}) is the craft. Baroque is often polyphony, but much of it is a tune over a bass; Romantic is mostly homophony. “Classical music” is concert music of any period; the Classical period is 1750 to 1820. Nationalism: Chopin (Poland), Bartók (Hungary), Dvořák (the Czech lands), Grieg (Norway). Period sounds: Bach’s Invention No. 1, Mozart’s K. 545, Liszt’s Liebestraum No. 3 (real openings); Debussy and Hisaishi in their style. The folk tune, boogie, swing pattern and four-chord loop were made for the app.</div>
  </>);
  return <>{pages}</>;
}
WORKBOOKS['styles'] = CsxWorkbook;
TEACHER_COPIES['styles'] = CsxTeacher;
