// Phase 397: the chapter 3 Workbook follows the Lesson Book page by page; the opener and the check-up are the Lesson
// Book's first and last pages (one page for both books, Phase 394), so the Workbook holds the step pages 2-7.
function NnSkipNote() { return <span style={{color:BK.muted,fontStyle:'italic'}}>(whisper the letter you jump over)</span>; }
function NoteNamesWorkbook({ startNo = 1, frames = true }) {
  const W = useMemo(() => nnWorkbook(), [LANG]);
  const pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={startNo + 1 + pages.length} chId="note-names">{content}</WbPage>);
  // a resident: who lives there, and a little keyboard to put a dot on its key
  const ResCell = ({ L, n, ex }) => <ExCell n={n} ex={ex}><div style={{padding:'13px 4px 2px'}}>
    <div style={{display:'flex',alignItems:'center',gap:8,marginBottom:3}}>{nnResIcon(L, 42)}<span style={{fontSize:12.5,fontWeight:900,color:BK.ink}}>{NN_RES[L][0]}</span></div>
    <PaperKeys start="C" whites={7} w={20} h={50} dots={ex ? [NN_L7.indexOf(L)] : []} dotR={0.2}/>
  </div></ExCell>;

  // 2 (faces "A to G on the keys")
  const cf = [1, 5, 8, 12];
  P(<>
    <WbTop step={1}/>
    <Part kind="together" title="Find every C and F" how="Write C or F in every box.">
      <ArtLead pic={<KeyScene start="C" whites={7} w={40} h={84} houses doors/>} picW={290} text={<><span style={{color:BK.coral}}>C</span> is the small house's left door. <span style={{color:BK.coral}}>F</span> is the big house's left door.</>}/>
      <KeysCell ex><PaperKeys start="E" whites={15} w={40} h={120} boxes={cf} labels={{ 1: 'F' }} ex={{ 1: true }}/></KeysCell>
    </Part>
    <Part kind="home" title="Name the dotted keys" how="Find the house, then its left door, and walk along from there. Write the letter in the box.">
      <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:12}}>{W.s1.kb.map((kb, i) => <KeysCell key={i} n={i === 0 ? '1-4' : '5-8'}><PaperKeys start={kb.start} whites={10} w={30} h={110} dots={kb.dots} boxes={kb.dots} boxNos={Object.fromEntries([...kb.dots].sort((a, b) => a - b).map((d, j) => [d, 4 * i + j + 1]))}/></KeysCell>)}</div>
    </Part>
    <Part kind="play" title="Lost letters" how="Five letters have floated away from their keys! Draw a line from each balloon down to the key it lives on. Then draw a roof on every house.">
      <KeyScene start="C" whites={14} w={40} h={110} houses={false} lost={['D', 'G', 'B', 'C', 'A']}/>
    </Part>
    <Faces/>
  </>);

  // 3 (faces "The letter wheel")
  P(<>
    <WbTop step={2}/>
    <Part kind="together" title="Fill in the missing letters" how="Say the letters round the wheel out loud, then fill the gaps.">
      <ArtLead pic={<LetterWheel size={118}/>} picW={118} text={<>Music has only 7 letters, A to G, going round like a Ferris wheel. <span style={{color:BK.coral}}>After G, you are back at A.</span></>} style={{padding:'4px 14px'}}/>
      <div style={{display:'grid',gap:8}}>{W.s2.tog.map((r, i) => <LetterRow key={i} n={i + 1} ex={i === 0} cells={rowCells(r, i === 0)}/>)}</div>
    </Part>
    <Part kind="home" title="Fill them in on your own">
      <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:8}}>{W.s2.home.map((r, i) => <LetterRow key={i} n={i + 1} cells={rowCells(r, false)}/>)}</div>
    </Part>
    <Part kind="play" title="Same letter, every octave" how="Colour every C. Then draw a hop from each C to the next C, like the first one. Each hop is one octave: 8 white keys, counting both Cs.">
      <PaperKeys start="C" whites={22} w={26} h={96} fills={{ 0: '#fdeee8' }} arrows={<g>
        <path d={`M15 27 Q106 -3 197 27`} fill="none" stroke={BK.coral} strokeWidth="2.2"/>
        <path d="M190 20 L197.5 27.5 L188.5 27" fill="none" stroke={BK.coral} strokeWidth="2.2" strokeLinecap="round" strokeLinejoin="round"/>
        <text x="106" y="9" textAnchor="middle" fontSize="11" fontWeight="900" fill={BK.coral}>one octave</text>
      </g>}/>
      <div style={{display:'flex',gap:28,justifyContent:'center',marginTop:10,fontSize:13,color:BK.ink,alignItems:'center'}}><span>Cs on this keyboard: {bkBox(36, 28)}</span><span>Octave hops: {bkBox(36, 28)}</span></div>
    </Part>
    <Faces/>
  </>);

  // 4 (faces "Forwards up, backwards down")
  const hk = 15, hstart = W.hunt.start;
  P(<>
    <WbTop step={3}/>
    <Part kind="together" title="One step up, one step down" how="Write the letter one step up (the next letter) or one step down (the letter before).">
      <ArtLead pic={<Staircase size={230}/>} picW={230} text={<>Up a step = one key to the RIGHT = the next letter. <span style={{color:BK.coral}}>Down a step = one key to the LEFT = the letter before.</span></>}/>
      <BkGrid cols={4} gap="10px 12px">{W.s3.tog.map((it, i) => <UpDownCell key={i} it={it} n={i + 1} ex={i === 0}/>)}</BkGrid>
    </Part>
    <Part kind="home" title="Backwards" how="Each row goes backwards, down the piano. Watch out for A -- the letter before A is G.">
      <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:8}}>{W.s3.back.map((r, i) => <LetterRow key={i} n={i + 1} cells={rowCells(r, false)}/>)}</div>
      <div style={{display:'flex',alignItems:'center',gap:8,marginTop:9,fontSize:12.5,color:BK.ink,flexWrap:'wrap'}}><b>In my head, no piano:</b><span>the letters backwards, from a different letter each day. Tick a day:</span>{BK_DAYS.map(d => <span key={d} style={{display:'inline-flex',alignItems:'center',gap:3,fontSize:10.5,color:BK.muted,fontWeight:700}}>{d}<span style={{width:18,height:18,border:'1.5px solid ' + BK.line,borderRadius:4}}/></span>)}</div>
    </Part>
    <Part kind="play" title="Treasure hunt" how="Start on the star (F). One step = the next white key. Follow each clue, write the letter you land on, and start the next clue from there. Clue 1 is done: the arrow shows the hop. Draw a treasure chest on the last key!">
      <PaperKeys start="C" whites={hk} w={42} h={110} stars={[hstart]} arrows={(() => { const m0 = W.hunt.moves[0].m, x0 = (hstart + 0.5) * 42 + 2, x1 = (W.hunt.moves[0].land + 0.5) * 42 + 2, dir = m0 > 0 ? 1 : -1; return <g>
        {Array.from({ length: Math.abs(m0) }, (_, j) => { const a = x0 + j * 42 * dir, b = a + 42 * dir; return <path key={j} d={`M${a} 26 Q${(a + b) / 2} 2 ${b} 26`} fill="none" stroke={BK.coral} strokeWidth="2.2"/>; })}
        <path d={`M${x1 - 5 * dir} 17 L${x1} 27 L${x1 - 6 * dir} 25`} fill="none" stroke={BK.coral} strokeWidth="2.2" strokeLinecap="round" strokeLinejoin="round"/>
        <text x={(x0 + x1) / 2} y={11} textAnchor="middle" fontSize="11" fontWeight="900" fill={BK.coral}>{'clue 1: ' + Math.abs(m0) + (Math.abs(m0) === 1 ? ' step ' : ' steps ') + (m0 > 0 ? 'up' : 'down')}</text>
      </g>; })()}/>
      <div style={{display:'grid',gridTemplateColumns:'repeat(6,1fr)',gap:8,marginTop:10}}>{W.hunt.moves.map((mv, i) => <div key={i} style={{border:(i === 0 ? '1.5px solid ' + BK.coral : '1px solid #ece6d8'),background:i === 0 ? '#fff8f5' : '#fff',borderRadius:8,padding:'6px 4px',textAlign:'center'}}>
        <div style={{fontSize:10,fontWeight:900,color:BK.coral}}>{i === 0 ? 'CLUE 1 · EXAMPLE' : 'CLUE ' + (i + 1)}</div>
        <div style={{fontSize:13.5,fontWeight:800,color:BK.ink,margin:'2px 0 6px'}}>{Math.abs(mv.m) + (Math.abs(mv.m) === 1 ? ' step ' : ' steps ') + (mv.m > 0 ? 'up' : 'down')}</div>
        {i === 0 ? bkHand(nnLet('C', mv.land), 40, 34) : bkBox(40, 34)}
      </div>)}</div>
    </Part>
    <Faces/>
  </>);

  // 5 (faces "Name it at a glance")
  P(<>
    <WbTop step={4}/>
    <Part kind="together" title="Who lives where?" how="Put a dot on the key where each one lives. The first one is done.">
      <BkGrid cols={4} gap="8px 10px">{W.gl.tog.map((L, i) => <ResCell key={L} L={L} n={i + 1} ex={i === 0}/>)}</BkGrid>
    </Part>
    <Part kind="home" title="Name it at a glance" how="First the last three: a dot on their keys. Then write the letter of each dotted key below -- don't count from C, think who lives there.">
      <BkGrid cols={4} gap="8px 10px">{W.gl.home.map((L, i) => <ResCell key={L} L={L} n={i + 4}/>)}</BkGrid>
      <div style={{marginTop:8}}><KeysCell n="7-12"><PaperKeys start="C" whites={14} w={36} h={134} dots={W.gl.kb} boxes={W.gl.kb} boxNos={Object.fromEntries([...W.gl.kb].sort((a, b) => a - b).map((d, j) => [d, j + 7]))}/></KeysCell></div>
    </Part>
    <Part kind="play" title="Draw who lives here" how="Draw them on their keys: the Cat, the Dog in his doghouse and the Elephant in the small house; the Front door, Grandma, her Apple garden and the Back door in the big house.">
      <div style={{maxWidth:560,margin:'0 auto',width:'100%'}}><PaperKeys start="C" whites={7} w={78} h={170} roofs/></div>
    </Part>
    <Faces/>
  </>);

  // 6 (faces "Skip a letter")
  P(<>
    <WbTop step={5}/>
    <Part kind="together" title="Skip a letter" how="Say each row out loud first -- whisper the letter you jump over -- then fill the gaps.">
      <ArtLead pic={<LetterWheel size={110} mode="skip"/>} picW={110} text={<>Skipping: hop over one gondola each time. <span style={{color:BK.coral}}>A (b) C (d) E...</span> <NnSkipNote/></>} style={{padding:'4px 14px'}}/>
      <div style={{display:'grid',gap:8}}>{W.sk.tog.map((r, i) => <LetterRow key={i} n={i + 1} ex={i === 0} cells={rowCells(r, i === 0)}/>)}</div>
    </Part>
    <Part kind="home" title="Your turn" how="Rows 1-2 skip up. Rows 3-4 skip down (C, A, F...).">
      <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:8}}>{[0, 2, 1, 3].map(j => <LetterRow key={j} n={j + 1} cells={rowCells(W.sk.home[j], false)}/>)}</div>
    </Part>
    <Part kind="play" title="Draw the letter star" how="Start on A. Skip a letter each time (A, C, E...) and join them with a ruler as you go. Keep going until you are back on A -- what shape did you make?">
      <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:20,alignItems:'center'}}>
        <LetterRing size={185} star start="A"/>
        <div>
          <div style={{fontSize:12.5,color:BK.ink,marginBottom:8}}>Write the letters you visit:</div>
          <div style={{display:'flex',gap:5,flexWrap:'wrap'}}>{['A', '', '', '', '', '', '', 'A'].map((l, i) => <span key={i} style={{width:30,height:34,borderRadius:6,display:'inline-flex',alignItems:'center',justifyContent:'center',fontSize:17,fontWeight:900,border:'1.5px solid ' + (l ? 'transparent' : BK.line),background:l ? BK.soft : '#fff',color:BK.ink}}>{l}</span>)}</div>
          <div style={{fontSize:12.5,color:BK.ink,marginTop:14}}>My shape is a <span style={{display:'inline-block',width:110,borderBottom:'1px solid ' + BK.ink}}>&nbsp;</span></div>
          <div style={{fontSize:11.5,color:BK.muted,marginTop:10,lineHeight:1.45}}>Musicians use this skip all the time: C E G is a chord!</div>
        </div>
      </div>
    </Part>
    <Faces/>
  </>);

  // 7 (faces "Play by letter names")
  const songSeq = NN_SONG_L.map((x, i) => NN_SONG_GAPS.includes(i) ? '?' + x : x);
  P(<>
    <WbTop step={6}/>
    <Part kind="together" title="Hot Cross Buns in letters" how="Fill in the missing letters, then play it: right hand 2 3 4 on C D E, reading the letters.">
      <div style={{border:'1.5px solid ' + BK.coral,background:'#fff8f5',borderRadius:8,padding:'10px 12px 8px'}}><NnTuneRow seq={songSeq} ex/></div>
    </Part>
    <Part kind="home" title="This week" how="Tick each one you do.">
      <PhLog rows={['Hot Cross Buns, right hand, reading the letters', 'Hot Cross Buns, left hand, one small house lower', 'Letter chain with someone: forwards', 'Letter chain: backwards', 'Spell and play: BAG, CAFE, FACE']} days={7} label={250}/>
    </Part>
    <Part kind="play" title="Music word search" how="These words use only music letters. Find each one -- across or down -- ring it, tick it, and play it on the piano!">
      <div style={{display:'grid',gridTemplateColumns:'auto 1fr',gap:22,alignItems:'center'}}>
        <div style={{display:'grid',gridTemplateColumns:'repeat(9, 31px)',gap:3}}>{W.search.g.flat().map((l, i) => <span key={i} style={{width:31,height:31,display:'inline-flex',alignItems:'center',justifyContent:'center',fontSize:16,fontWeight:800,color:BK.ink,border:'1px solid #ece6d8',borderRadius:5}}>{l}</span>)}</div>
        <div style={{display:'grid',gap:8}}>{NN_WORDS.map(w => <div key={w} style={{display:'flex',alignItems:'center',gap:10,fontSize:16,fontWeight:900,color:BK.ink,letterSpacing:'0.12em'}}><span style={{width:20,height:20,border:'1.5px solid ' + BK.line,borderRadius:5}}/>{w}</div>)}
          <div style={{fontSize:12,color:BK.muted,marginTop:4,lineHeight:1.45}}>Bonus: make up your own music word<br/><span style={{display:'inline-block',width:150,borderBottom:'1px solid ' + BK.ink,marginTop:4}}>&nbsp;</span></div>
        </div>
      </div>
    </Part>
    <Faces/>
  </>);

  // (the check-up is on the Lesson Book's last page, under My five checks -- Phase 394)
  return <>{frames ? lbFramed('note-names', pages, startNo) : pages}</>;
}

function NoteNamesTeacher() {
  const W = useMemo(() => nnWorkbook(), [LANG]);
  const pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={pages.length + 1} chId="note-names" teacher>{content}</WbPage>);
  const rowAns = (rows) => rows.map(r => r.pos.map(p => r.seq[p]).join(' '));
  const hunt = W.hunt.moves.map(m => nnLet('C', m.land));
  const resAns = (L) => L + ' (' + NN_RES[L][0] + ')';
  P(<>
    <div style={{fontFamily:"'Playfair Display', Georgia, serif",fontSize:28,fontWeight:900,color:BK.ink,margin:'2px 0 2px'}}>Teacher copy · {bkChapterName('note-names')}</div>
    <div style={{fontSize:12.5,color:BK.muted,margin:'0 0 12px',lineHeight:1.5}}>Each workbook page faces its Lesson Book page. Chapter 2 gave the keyboard its pattern; this chapter gives every white key its name, A to G, and makes the names fast -- forwards, backwards (on the keys and in the head), at a glance, and a skip at a time. Black keys keep no names yet (sharps and flats come with Tones & Semitones); interval numbers wait for Intervals. TRY IT comes first (its first item is the worked example), then YOUR TURN and PLAY.</div>
    <TcBlock page={2} title="A to G on the keys" answers={<>{tcAns('TRY IT', ['F C F C (left to right)'])}{tcAns('YOUR TURN', [...W.s1.kb[0].dots.map(i => nnLet('C', i)), ...W.s1.kb[1].dots.map(i => nnLet('A', i))])}<div style={{fontSize:12,color:BK.ink}}><b style={{color:BK.muted,fontSize:10.5,letterSpacing:'0.06em'}}>PLAY</b>  Each balloon joins any key with that letter (D: 2nd or 9th white key, G: 5th or 12th, B: 7th or 14th, C: 1st or 8th, A: 6th or 13th); roofs over every 2-group and 3-group</div></>}
      watch="Crossing into F G A at the three-black-key roof -- the most common stumble. Finding C by counting from the bottom of the piano instead of using the houses."
      say="“C and F are the left doors: C of the small house, F of the big one.”"/>
    <TcBlock page={3} title="The letter wheel" answers={<>{tcAns('TRY IT', rowAns(W.s2.tog))}{tcAns('YOUR TURN', rowAns(W.s2.home))}{tcAns('PLAY', ['4 Cs (the 1st, 8th, 15th and 22nd white keys)', '3 octave hops'])}</>}
      watch="Carrying on past G to H. Starting every row from A in their head instead of from the letter given."
      say="“Seven letters, round and round: after G comes A -- like Sunday back to Monday.”"/>
    <TcBlock page={4} title="Forwards up, backwards down" answers={<>{tcAns('TRY IT', W.s3.tog.map(it => it.a))}{tcAns('YOUR TURN', rowAns(W.s3.back))}{tcAns('PLAY', hunt)}</>}
      watch="Backwards is much slower than forwards -- that is normal. Saying it backwards in the head, without the keyboard, matters as much as on the keys: a little every day, away from the piano. Up is to the right, and the sound goes higher."
      say="“Up the piano: forwards. Down the piano: backwards. Before A comes G.”"/>
  </>);
  P(<>
    <TcBlock page={5} title="Name it at a glance" answers={<>{tcAns('TRY IT', W.gl.tog.map(resAns))}{tcAns('YOUR TURN', [...W.gl.home.map(resAns), ...[...W.gl.kb].sort((a, b) => a - b).map(i => nnLet('C', i))])}<div style={{fontSize:12,color:BK.ink}}><b style={{color:BK.muted,fontSize:10.5,letterSpacing:'0.06em'}}>PLAY</b>  C the Cat, D the Dog in his doghouse, E the Elephant; F the Front door, G Grandma, A her Apple garden, B the Back door</div></>}
      watch="Counting up from C to find every key. Ask “Who lives there?” instead. Each one sits in its key's place: the Dog between the two black keys, Grandma and the Apple garden between the three."
      say="“Cat, Dog, Elephant -- Front door, Grandma, Apple garden, Back door.”"/>
    <TcBlock page={6} title="Skip a letter" answers={<>{tcAns('TRY IT', rowAns(W.sk.tog))}{tcAns('YOUR TURN', rowAns(W.sk.home))}{tcAns('PLAY', ['A C E G B D F A -- a 7-point star'])}</>}
      watch="Skips are the hardest part of this chapter for most children. Landing on the very next letter instead of jumping one. Start slowly with the whispered letter, then drop it."
      say="“Whisper the one you jump over: C (d) E (f) G.”"/>
    <TcBlock page={7} title="Play by letter names" answers={<>{tcAns('TRY IT', NN_SONG_GAPS.map(i => NN_SONG_L[i]))}{tcAns('PLAY', W.search.placed.map(p => p.w + ' ' + (p.hz ? 'across' : 'down') + ' from row ' + (p.r + 1) + ' col ' + (p.c + 1)))}</>}
      watch="Reading the finger numbers instead of the letters: have them sing the letter names while they play. Fingers 2 3 4 only; 1 and 5 wait for C position. The legato is still the relay baton."
      say="“Read the letter, see its place, play.”"/>
    <TcBlock page={8} title="My five checks · the check-up on paper" answers={<>{tcAns('A', [...W.chk.nm].sort((a, b) => a - b).map(i => nnLet('G', i)))}{tcAns('B', rowAns(W.chk.ab))}{tcAns('C', W.chk.ud.map(it => it.a))}{tcAns('D', rowAns(W.chk.ch))}{tcAns('E', NN_CHK_SONG.filter(x => x[0] === '?').map(x => x.slice(1)))}
      <div style={{fontSize:12,color:BK.ink,marginTop:6,lineHeight:1.5}}>Chapter 1's five checks still come first at the piano. This chapter's five checks are shown on the keyboard or said out loud (A to G on the keys, forwards and backwards, at a glance, skips, Hot Cross Buns by letters); you only correct. The paper part follows the same order: score each part on its own (A, B, C, D: 4 marks, pass 3+; E: 2 marks). Not passed? Go back to that step's page: A p.2 and p.5 · B p.3 · C p.4 · D p.4 and p.6 · E p.7.</div></>}/>
  </>);
  return <>{pages}</>;
}

