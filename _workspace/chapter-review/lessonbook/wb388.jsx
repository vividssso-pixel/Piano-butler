function fsWorkbook() {
  // Phase 388: the chapter 2 Workbook follows the Lesson Book page by page (Keyboard Patterns & Note Names)
  const k = (s) => 'fs-wb388-' + s;
  const pair = () => { let a, b; do { a = Math.floor(Math.random() * 10); b = Math.floor(Math.random() * 10); } while (Math.abs(a - b) < 2); return [a, b]; };
  const whites = (n, len, avoid) => { const out = []; let g = 0; while (out.length < n && g++ < 200) { const w = Math.floor(Math.random() * len); if (w !== avoid && out[out.length - 1] !== w) out.push(w); } return out; };
  const s3 = withSeed(k('s3'), () => [1, ...whites(5, 7, -1)]);        // whose house: the first one is the worked example (D: small)
  const s4 = withSeed(k('s4'), () => [4, ...whites(5, 10, 4)]);        // name it: the first one is the worked example (G)
  const chk = withSeed(k('chk'), () => ({ wh: shuffle([0, 4, 2, 6]), ln: shuffle([1, 5, 3, 8]), hl: Array.from({ length: 4 }, pair), sg: shuffle([3, 4, 5, 3]), lg: shuffle([true, false, true, false]) }));
  return { s3, s4, chk };
}
const fsLetter = (i) => 'CDEFGAB'[i % 7];
const fsHouse = (i) => (i % 7) < 3 ? 'S' : 'B';
const FS_TINT = (n, start = 'C') => { const s0 = 'CDEFGAB'.indexOf(start), o = {}; for (let i = 0; i < n; i++) o[i] = ((s0 + i) % 7) < 3 ? '#fbe9e2' : '#e9eaf4'; return o; };
function fsConcepts() {
  return [
    { id: 'hs', name: 'Small & big houses', step: '1', page: '2' },
    { id: 'hl', name: 'High & low', step: '1', page: '2' },
    { id: 'wk', name: 'White keys of each house', step: '2', page: '3' },
    { id: 'ln', name: 'The seven letter names', step: '3', page: '4' },
    { id: 'mc', name: 'Middle C', step: '4', page: '5', chk: false },
    { id: 'sg', name: 'Hot Cross Buns', step: '5', page: '6' },
    { id: 'lg', name: 'Legato', step: '5', page: '6' },
    { id: 'ck', name: 'My five checks', step: '6', page: '7', chk: false },
  ];
}
function FirstStepsWorkbook({ startNo = 1 }) {
  const W = useMemo(() => fsWorkbook(), [LANG]);
  const C = fsConcepts();
  const pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={startNo + pages.length} chId="first-steps">{content}</WbPage>);
  const box = (l) => <div key={l} style={{border:'1.5px solid ' + BK.line,borderRadius:10,display:'flex',alignItems:'flex-end',padding:'6px 10px',fontSize:11.5,color:BK.muted}}>{l}</div>;

  // 1 (faces the Lesson Book opener): the map
  P(<>
    <div style={{display:'flex',alignItems:'baseline',gap:12,margin:'2px 0 2px'}}>
      <span style={{fontSize:12,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>{'CHAPTER ' + bkChapterNo('first-steps')}</span>
      <span style={{fontFamily:"'Playfair Display', Georgia, serif",fontSize:24,fontWeight:900,color:BK.ink}}>{bkChapterName('first-steps')}</span>
    </div>
    <div style={{fontSize:12.5,color:BK.muted,margin:'0 0 10px',lineHeight:1.45}}>Each workbook page faces its Lesson Book page: read the left page, then do the right one.</div>
    <WbMap id="first-steps" concepts={C} steps={6} checkPage={startNo + 6} tasks={[
      'Find every small and big house, from the bottom to the top.',
      'Play the white keys under each roof: 3, then 4.',
      'Find every C and F, then any letter someone calls out.',
      'Hot Cross Buns with 2 3 4, smooth as a relay baton.',
    ]}/>
  </>);

  // 2 (faces "Small house, big house")
  P(<>
    <WbTop step={1}/>
    <Part kind="together" title="Draw the roofs" how="Draw a roof over every group of black keys -- a small roof over 2, a big roof over 3. The first one is done.">
      <KeysCell ex><div style={{position:'relative'}}><PaperKeys start="C" whites={14} w={40} h={120} roofs/><svg viewBox="0 0 564 150" style={{position:'absolute',inset:0,width:'100%'}}><path d="M26 24 L62 6 L98 24" fill="none" stroke={BK.coral} strokeWidth="2.6" strokeLinejoin="round"/></svg></div></KeysCell>
    </Part>
    <Part kind="home" title="Count the roofs" how="Colour the small roofs' black keys one colour and the big roofs' black keys another. Then count them.">
      <PaperKeys start="C" whites={21} w={30} h={100}/>
      <div style={{display:'flex',gap:28,justifyContent:'center',marginTop:8,fontSize:13,color:BK.ink,alignItems:'center'}}>
        <span>Small houses: {bkBox(36, 28)}</span><span>Big houses: {bkBox(36, 28)}</span>
      </div>
    </Part>
    <Part kind="play" title="Bear or bird?" how="Low sounds live at the bear's end, high sounds at the bird's end. Draw a line from each sound to the bear or the bird, then make each sound on the piano!">
      <div style={{display:'grid',gridTemplateColumns:'90px 1fr 90px',gap:10,alignItems:'center',flex:1}}>
        <div style={{display:'grid',justifyItems:'center',gap:2,fontSize:12,fontWeight:800,color:BK.ink}}>{bearIcon(66)}low</div>
        <div style={{display:'grid',gridTemplateColumns:'repeat(3,1fr)',gap:'10px 20px'}}>{['elephant', 'mouse', 'thunder', 'bell', 'drum', 'whistle'].map(k => <div key={k} style={{border:'1px solid #ece6d8',borderRadius:8,display:'grid',justifyItems:'center',padding:'4px 4px 2px',fontSize:11,color:BK.muted}}><SoundIcon kind={k} size={48}/>{k}</div>)}</div>
        <div style={{display:'grid',justifyItems:'center',gap:2,fontSize:12,fontWeight:800,color:BK.coral}}>{birdIcon(66)}high</div>
      </div>
    </Part>
    <Faces/>
  </>);

  // 3 (faces "The white keys of each house")
  P(<>
    <WbTop step={2}/>
    <Part kind="together" title="Who lives under each roof?" how="Colour the 3 white keys under every small roof one colour and the 4 under every big roof another. The first house is done.">
      <KeysCell ex><PaperKeys start="C" whites={14} w={40} h={120} roofs fills={{ 0: '#fbe9e2', 1: '#fbe9e2', 2: '#fbe9e2' }}/></KeysCell>
    </Part>
    <Part kind="home" title="Whose house?" how="Is the dotted white key under a small roof or a big roof? Write S or B.">
      <BkGrid cols={3} gap="8px 12px">{W.s3.map((w, i) => <ExCell key={i} n={i + 1} ex={i === 0}><div style={{display:'flex',alignItems:'center',gap:10,padding:'14px 4px 4px'}}>
        <div style={{flex:1}}><PaperKeys start="C" whites={7} w={22} h={64} roofs dots={[w]}/></div>{nvBox(i === 0, fsHouse(w), 34, 28)}
      </div></ExCell>)}</BkGrid>
    </Part>
    <Part kind="play" title="Who lives here?" how="Draw a family of 3 under the small roof and a family of 4 under the big one -- one for each white key. Give them names!">
      <div style={{display:'grid',gridTemplateColumns:'1fr 1.33fr',gap:14,flex:1,minHeight:150}}>
        {[['Small house: 3 live here', 2], ['Big house: 4 live here', 3]].map(([l, n]) => <div key={l} style={{border:'1.5px solid ' + BK.line,borderRadius:10,display:'flex',flexDirection:'column',justifyContent:'space-between',padding:'6px 10px',fontSize:11.5,color:BK.muted}}>
          <svg viewBox="0 0 120 30" style={{width:n === 2 ? 70 : 96}}><path d={n === 2 ? 'M4 26 L34 6 L64 26' : 'M4 26 L50 4 L96 26'} fill="none" stroke={BK.ink} strokeWidth="2.4"/>{Array.from({ length: n }, (_, k) => <rect key={k} x={(n === 2 ? 20 : 26) + k * 15} y="14" width="9" height="12" fill={BK.ink}/>)}</svg>
          <span>{l}</span></div>)}
      </div>
    </Part>
    <Faces/>
  </>);

  // 4 (faces "The seven letter names")
  P(<>
    <WbTop step={3}/>
    <Part kind="together" title="Write the names on the doors" how="C is the small house's left door, F is the big house's. Write the other five letters. The first one is done.">
      <KeysCell ex><PaperKeys start="C" whites={7} w={68} h={150} labels={{ 0: 'C', 1: 'D', 3: 'F' }} ex={{ 1: true }} boxes={[2, 4, 5, 6]} fills={FS_TINT(7)}/></KeysCell>
      <div style={{fontSize:11.5,color:BK.muted,marginTop:4}}>Example: D sits inside the small house, between its two black keys.</div>
    </Part>
    <Part kind="home" title="Name the dotted key" how="Find the two left doors first (C and F), then walk to the dot. Write its letter.">
      <BkGrid cols={3} gap="8px 12px">{W.s4.map((w, i) => <ExCell key={i} n={i + 1} ex={i === 0}><div style={{display:'flex',alignItems:'center',gap:10,padding:'14px 4px 4px'}}>
        <div style={{flex:1}}><PaperKeys start="C" whites={10} w={17} h={56} dots={[w]}/></div>{nvBox(i === 0, fsLetter(w), 34, 28)}
      </div></ExCell>)}</BkGrid>
    </Part>
    <Part kind="play" title="Spell a word on the keys" how="Music only uses A B C D E F G -- but they make words! Find each word on the piano and play it letter by letter. Then make up your own.">
      <div style={{display:'flex',flexWrap:'wrap',gap:'8px 12px',alignItems:'center'}}>
        {['BAG', 'CAFE', 'FACE', 'BEAD', 'CAGE', 'BADGE'].map(w => <span key={w} style={{display:'inline-flex',alignItems:'center',gap:6,border:'1px solid #ece6d8',borderRadius:8,padding:'5px 10px',fontFamily:"'Playfair Display', Georgia, serif",fontSize:18,fontWeight:900,color:BK.ink,letterSpacing:'0.12em'}}>{w}<span style={{width:14,height:14,border:'1.5px solid ' + BK.ink,borderRadius:4}}/></span>)}
      </div>
      <div style={{display:'flex',alignItems:'center',gap:8,marginTop:12,fontSize:13,color:BK.ink}}>My word: {Array.from({ length: 6 }, (_, i) => <span key={i}>{bkBox(32, 32)}</span>)}</div>
    </Part>
    <Faces/>
  </>);

  // 5 (faces "The whole piano & middle C")
  P(<>
    <WbTop step={4}/>
    <Part kind="together" title="Count the houses on a real piano" how="A real piano has 88 keys. Count the small houses together, from left to right, ticking each one.">
      <div style={{border:'1px solid #ece6d8',borderRadius:8,padding:'6px 8px 8px',fontSize:10.5,fontWeight:800,color:BK.muted}}>
        <div style={{margin:'0 0 2px'}}>Bottom half -- the low keys, the bear's end</div><KeyScene start="A" whites={26} w={24} h={72} houses={false} bear/>
        <div style={{margin:'6px 0 2px'}}>Top half -- the high keys, the bird's end (carry on counting here)</div><KeyScene start="F" whites={26} w={24} h={72} houses={false} bird/>
      </div>
      <div style={{display:'flex',gap:28,justifyContent:'center',marginTop:8,fontSize:13,color:BK.ink,alignItems:'center'}}><span>Small houses: {bkHand('7', 36, 28)}</span></div>
    </Part>
    <Part kind="home" title="Your turn on the big piano" how="Use the keyboard above.">
      <div style={{display:'grid',gap:6,fontSize:13,color:BK.ink}}>
        <div style={{display:'flex',alignItems:'center',gap:10}}>1 · Count the big houses: {bkBox(36, 28)}</div>
        <div>2 · Draw a little kennel over the lonely black key at the very bottom.</div>
        <div>3 · Draw a star on <b>middle C</b> -- the white key just left of the 4th small house.</div>
      </div>
    </Part>
    <Part kind="play" title="Low Land and High Land" how="Middle C is the door between them. Draw who lives in Low Land (left of the door) and who lives in High Land (right of it). Then play their voices!">
      <div style={{display:'grid',gridTemplateColumns:'1fr 46px 1fr',gap:10,flex:1,minHeight:140,alignItems:'stretch'}}>
        {box('Low Land')}
        <div style={{display:'grid',justifyItems:'center',alignContent:'center',gap:4,fontSize:10,fontWeight:900,color:BK.coral,textAlign:'center'}}><svg viewBox="0 0 30 46" style={{width:30}}><rect x="3" y="2" width="24" height="42" rx="3" fill="#fff" stroke={BK.coral} strokeWidth="2"/><circle cx="21" cy="24" r="2" fill={BK.coral}/></svg>middle C</div>
        {box('High Land')}
      </div>
    </Part>
    <Faces/>
  </>);

  // 6 (faces "Play on the patterns")
  P(<>
    <WbTop step={5}/>
    <Part kind="together" title="Fingers on the roofs" how="Right hand on the big roof: 2 on the first black key, 3 in the middle, 4 on the highest. Write the finger number on each black key.">
      <KeysCell ex><div style={{display:'grid',gridTemplateColumns:'1fr 120px',gap:16,alignItems:'center'}}>
        <div style={{position:'relative'}}><KeyScene start="C" whites={7} w={60} h={118} houses blackNums={{ 3: '2' }}/><div style={{position:'absolute',left:(5 * 60 + 2) / (7 * 60 + 4) * 100 + '%',top:72,transform:'translateX(-50%)'}}>{bkBox(26, 26)}</div><div style={{position:'absolute',left:(6 * 60 + 2) / (7 * 60 + 4) * 100 + '%',top:72,transform:'translateX(-50%)'}}>{bkBox(26, 26)}</div></div>
        <PbArt name="keys-hand-R" h={112}/>
      </div></KeysCell>
    </Part>
    <Part kind="home" title="Hot Cross Buns" how="The song in finger numbers. Fill in the missing numbers, then tick each tune you play this week.">
      <SongRow gaps={FS_SONG_GAPS} ex/>
      <div style={{marginTop:8}}><PhLog rows={['Hot Cross Buns', 'Mary Had a Little Lamb', 'Old MacDonald', 'Rain Rain Go Away', 'Echo game with someone at home']} label={190}/></div>
    </Part>
    <Part kind="play" title="The relay baton: legato" how="Hold the key until the next one plays -- the moment it sounds, let the old one go. Draw a smooth snake joining the honey pots without lifting your pencil!">
      <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:16,marginBottom:4}}>
        <div style={{border:'1px solid #ece6d8',background:BK.soft,borderRadius:8,padding:'4px 10px'}}><Footsteps smooth/><div style={{fontSize:11.5,fontWeight:800,color:BK.ink,textAlign:'center'}}>Legato: one foot is always on the ground.</div></div>
        <div style={{border:'1px solid #ece6d8',borderRadius:8,padding:'4px 10px'}}><Footsteps smooth={false}/><div style={{fontSize:11.5,fontWeight:800,color:BK.muted,textAlign:'center'}}>Not legato: a gap between every step.</div></div>
      </div>
      <svg viewBox="0 0 640 112" style={{width:'100%',display:'block'}}>
        {[[40, 80], [150, 40], [260, 76], [370, 30], [480, 72], [590, 38]].map(([x, y], i) => <g key={i}><path d={`M${x - 18} ${y - 14} Q${x - 22} ${y + 22} ${x} ${y + 22} Q${x + 22} ${y + 22} ${x + 18} ${y - 14} Z`} fill="#fff" stroke={BK.ink} strokeWidth="1.6"/><rect x={x - 20} y={y - 19} width="40" height="6" rx="2" fill={BK.ink}/><text x={x} y={y + 9} textAnchor="middle" fontSize="13" fontWeight="900" fill={BK.coral}>{i + 1}</text></g>)}
        <text x="20" y="108" fontSize="10.5" fontWeight="800" fill={BK.coral}>start here</text>
      </svg>
    </Part>
    <Faces/>
  </>);

  // 7 (faces "My five checks"): the chapter check-up
  const cnt = { hs: 4, hl: 4, wk: 4, ln: 4, sg: 4, lg: 4 };
  P(<>
    <CheckHead total={24}/>
    {bkSec('A', 'Write S under each small house and B under each big house.')}
    <div style={{border:'1px solid #ece6d8',borderRadius:8,padding:'4px 10px'}}><PaperKeys start="C" whites={14} w={34} h={74} boxes={[1, 4, 8, 11]}/></div>
    {bkSec('B', 'Put a star on the higher dot -- the one nearer the bird.')}
    <BkGrid cols={4} gap="5px 10px">{W.chk.hl.map((p, i) => <BkCell key={i} n={5 + i}><div style={{padding:'12px 6px 6px'}}><PaperKeys start="C" whites={10} w={22} h={56} dots={p}/></div></BkCell>)}</BkGrid>
    {bkSec('C', 'Whose house is the dotted white key? Write S (small) or B (big).')}
    <BkGrid cols={4} gap="5px 10px">{W.chk.wh.map((w, i) => <BkCell key={i} n={9 + i}><div style={{display:'flex',alignItems:'center',gap:8,padding:'12px 4px 4px'}}><div style={{flex:1}}><PaperKeys start="C" whites={7} w={16} h={50} roofs dots={[w]}/></div>{bkBox(28, 24)}</div></BkCell>)}</BkGrid>
    {bkSec('D', 'Name the dotted key. Write its letter.')}
    <BkGrid cols={4} gap="5px 10px">{W.chk.ln.map((w, i) => <BkCell key={i} n={13 + i}><div style={{display:'flex',alignItems:'center',gap:8,padding:'12px 4px 4px'}}><div style={{flex:1}}><PaperKeys start="C" whites={10} w={12} h={46} dots={[w]}/></div>{bkBox(28, 24)}</div></BkCell>)}</BkGrid>
    {bkSec('E', 'Hot Cross Buns: which finger plays the dotted key?')}
    <BkGrid cols={4} gap="5px 10px">{W.chk.sg.map((f, i) => <BkCell key={i} n={17 + i}><div style={{display:'flex',alignItems:'center',gap:8,padding:'12px 4px 4px'}}><div style={{flex:1}}><PaperKeys start="C" whites={7} w={20} h={54} blackDots={[f]}/></div>{bkBox(28, 24)}</div></BkCell>)}</BkGrid>
    {bkSec('F', 'Legato means... Tick the right word in each pair.')}
    <BkGrid cols={4} gap="5px 10px">{W.chk.lg.map((first, i) => <BkCell key={i} n={21 + i}><div style={{display:'grid',gap:3,padding:'12px 6px 4px'}}>{[first, !first].map((sm, j) => <div key={j} style={{display:'grid',gridTemplateColumns:'1fr 20px',alignItems:'center',gap:4,fontSize:12.5,fontWeight:800,color:BK.ink}}><span>{FS_LEGATO_WORDS[i][sm ? 0 : 1]}</span><span style={{width:15,height:15,border:'1.5px solid ' + BK.ink,borderRadius:4}}/></div>)}</div></BkCell>)}</BkGrid>
    <CheckTable concepts={C} cnt={cnt}/>
  </>);
  return <>{pages}</>;
}

function FirstStepsTeacher() {
  const W = useMemo(() => fsWorkbook(), [LANG]);
  const pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={pages.length + 1} chId="first-steps" teacher>{content}</WbPage>);
  const finger = { 3: 2, 4: 3, 5: 4 };
  const hi = (p) => fsLetter(Math.max(p[0], p[1])) + ' (the right-hand dot)';
  P(<>
    <div style={{fontFamily:"'Playfair Display', Georgia, serif",fontSize:28,fontWeight:900,color:BK.ink,margin:'2px 0 2px'}}>Teacher copy · {bkChapterName('first-steps')}</div>
    <div style={{fontSize:12.5,color:BK.muted,margin:'0 0 12px',lineHeight:1.5}}>Each workbook page faces its Lesson Book page. Pattern first, names second -- the same order at every age: older beginners take this chapter in one sitting, younger ones live in the patterns for a while before the names stick. Everything happens by ear and by eye on the keyboard; no staff yet (the Queen of G and the King of F wait for the Reading chapter -- here only "the low and high voices meet at middle C"). Loud and soft are not part of this chapter.</div>
    <TcBlock page={2} title="Small house, big house" answers={<>{tcAns('TOGETHER', ['a small roof over every 2, a big roof over every 3 (4 roofs)'])}{tcAns('AT HOME', ['small houses 3, big houses 3'])}{tcAns('PLAY', ['bear (low): elephant, thunder, drum', 'bird (high): mouse, bell, whistle'])}</>}
      watch="Counting the black keys one by one instead of seeing the groups. Taking “higher” as further up the piano lid. The black keys are the roofs: the shape is what matters."
      say="“Look for the shapes, not the keys -- two together, three together.”"/>
    <TcBlock page={3} title="The white keys of each house" answers={<>{tcAns('TOGETHER', ['C D E one colour (twice), F G A B the other (twice)'])}{tcAns('AT HOME', W.s3.map(w => fsHouse(w) + ' (' + fsLetter(w) + ')'))}</>}
      watch="This is the chapter's key idea: the white keys belong to a house -- 3 under the small roof, 4 under the big. A student who sees this grouping finds every note name, and later every scale fingering, from the pattern instead of counting from the bottom."
      say="“Every white key lives under a roof.”"/>
    <TcBlock page={4} title="The seven letter names" answers={<>{tcAns('TOGETHER', ['C D E F G A B'])}{tcAns('AT HOME', W.s4.map(fsLetter))}<div style={{fontSize:12,color:BK.ink}}>PLAY: any word from A to G, played letter by letter.</div></>}
      watch="The most common stumble: crossing into F G A at the three-black-key roof. Anchor C and F at their left doors and walk from there. Also watch for an “H” (there is none -- after G comes A again) and for counting up from A at the bottom."
      say="“C and F are the left doors. Find the door, then walk.”"/>
  </>);
  P(<>
    <TcBlock page={5} title="The whole piano & middle C" answers={<>{tcAns('TOGETHER', ['7 small houses'])}{tcAns('AT HOME', ['7 big houses', 'the kennel over the 2nd key from the bottom (A♯0/B♭0)', 'the star on the 24th white key from the left: middle C'])}</>}
      watch="Losing count on the long keyboard -- tick each house as it is counted so none is counted twice. Check middle C at the piano, not only on paper."
      say="“Count the small houses to 4. Middle C is the door just to its left.”"/>
    <TcBlock page={6} title="Play on the patterns" answers={<>{tcAns('TOGETHER', ['2 3 4 (left to right)'])}{tcAns('AT HOME', [FS_SONG.join(' ')])}<div style={{fontSize:12,color:BK.ink}}>PLAY: one unbroken line through all six pots. Then hear Hot Cross Buns legato.</div></>}
      watch="Fingers 2 3 4 only, in both hands: 1 and 5 wait for C position. Lifting the hand between notes (a gap) or holding both keys down (a blur). Check the chapter 1 habits while it plays: round hand, wrist back to level. Echo game: play 2-3 black keys, the student plays them straight back; grow to 4-5 as it gets easy."
      say="“Like a relay baton: hold on until the next note sounds, then let the old one go. No gap between the two sounds.”"/>
    <TcBlock page={7} title="Check-up" goBack={fsConcepts()} answers={<>{tcAns('A', ['S B S B'])}{tcAns('B', W.chk.hl.map(hi))}{tcAns('C', W.chk.wh.map(w => fsHouse(w) + ' (' + fsLetter(w) + ')'))}{tcAns('D', W.chk.ln.map(fsLetter))}{tcAns('E', W.chk.sg.map(f => String(finger[f])))}{tcAns('F', W.chk.lg.map(first => first ? 'top' : 'bottom'))}
      <div style={{fontSize:12,color:BK.ink,marginTop:6,lineHeight:1.5}}>Chapter 1's five checks still come first, every time at the piano. This chapter's five checks are shown on the keyboard (find the houses, say 3 and 4, name any white key, find middle C, Hot Cross Buns legato); you only correct. Score each concept on its own (4 marks each, pass 3+).</div></>}/>
  </>);
  return <>{pages}</>;
}
