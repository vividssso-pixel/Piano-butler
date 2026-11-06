function PostureWorkbook({ startNo = 1 }) {
  const W = useMemo(() => phWorkbook(), [LANG]);
  const C = phConcepts();
  const pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={startNo + pages.length} chId="posture-hands">{content}</WbPage>);
  const star = (l) => <div key={l} style={{display:'flex',alignItems:'center',gap:8,fontSize:12.5,color:BK.ink}}><BkStar size={18}/>{l}</div>;

  // 1 (faces the Lesson Book opener): the map
  P(<>
    <div style={{display:'flex',alignItems:'baseline',gap:12,margin:'2px 0 2px'}}>
      <span style={{fontSize:12,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>{'CHAPTER ' + bkChapterNo('posture-hands')}</span>
      <span style={{fontFamily:"'Playfair Display', Georgia, serif",fontSize:24,fontWeight:900,color:BK.ink}}>{bkChapterName('posture-hands')}</span>
    </div>
    <div style={{fontSize:12.5,color:BK.muted,margin:'0 0 10px',lineHeight:1.45}}>Each workbook page faces its Lesson Book page: read the left page, then do the right one.</div>
    <WbMap id="posture-hands" concepts={C} steps={8} checkPage={startNo + 6} tasks={[
      'Before you play, every time: front half of the stool, feet flat, sit tall, leaning a little toward the piano.',
      'The six warm-ups in order, from the big parts of the body to the small.',
      'A round hand on your knee, like holding a ball, then onto the keys. The wrist stays free, as if on a roller.',
      'Finger walks: one note, then two, three, four, five. A little rainbow from key to key.',
    ]}/>
  </>);

  // 2 (faces "Sit at the piano")
  P(<>
    <WbTop step={1}/>
    <Part kind="together" title="Is this a good set-up?" how="Look at each picture with your teacher, then try it at the piano. Circle the tick or the cross.">
      <BkGrid cols={4} gap="6px 10px">{[PH_SIT[0], PH_SIT[1], PH_SIT[4], PH_SIT[2]].map(([id, , ok], i) => <PhPic key={id} art={'q-sit-' + id} ok={ok} n={i + 1} ex={i === 0} h={84}/>)}</BkGrid>
    </Part>
    <Part kind="home" title="Set up at home" how="Before you practise, set up and tick each one. Ask someone at home to check, or use a mirror.">
      <PhLog rows={['Front half of the stool', 'Feet flat, leaning a little toward the piano', 'Sit tall, like a puppet on a string', 'Forearm level with the keys', 'Elbows away from your body']} label={230}/>
    </Part>
    <Part kind="play" title="Draw yourself at the piano" how="Draw yourself sitting at the piano. Then colour a star for each thing you drew.">
      <div style={{display:'grid',gridTemplateColumns:'1fr 190px',gap:14,flex:1,minHeight:150}}>
        <div style={{border:'1.5px solid ' + BK.line,borderRadius:10}}/>
        <div style={{display:'grid',gap:6,alignContent:'center'}}>{['sitting tall', 'feet flat', 'leaning a little forward', 'elbows away from the body', 'round hands'].map(star)}</div>
      </div>
    </Part>
    <Faces/>
  </>);

  // 3 (faces "Let the arm carry the hand")
  P(<>
    <WbTop step="2-3"/>
    <Part kind="together" title="Put the warm-ups in order" how="Big parts of the body first, small parts last. Write 1 to 6 under the pictures. The first one is done.">
      <BkGrid cols={3} gap="6px 10px">{[PH_WARMUPS[0], ...W.order].map(([art, name], i) => <ExCell key={art} n={i + 1} ex={i === 0}><div style={{display:'flex',flexDirection:'column',alignItems:'center',gap:4,padding:'12px 2px 2px'}}>
        <div style={{height:92,display:'flex',alignItems:'center'}}><PbArt name={art} h={88} style={{maxWidth:'100%'}}/></div>
        <div style={{display:'flex',alignItems:'center',gap:8,fontSize:12,fontWeight:800,color:BK.ink}}>{name}{nvBox(i === 0, '1', 36, 28)}</div>
      </div></ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="My warm-ups this week" how="Do the six in order before you practise. Tick a box for each one you did.">
      <PhLog rows={PH_WARMUPS.map(([, n], i) => (i + 1) + '  ' + n)} days={7} label={150}/>
    </Part>
    <Part kind="home" title="Yes or no?" how="Circle yes or no.">
      <div style={{display:'grid',gap:4}}>{PH_ARM.slice(0, 4).map(([txt, ok], i) => <TFRow key={i} txt={txt} ok={ok} n={i + 1} pad="13px 8px 4px"/>)}</div>
    </Part>
    <Faces/>
  </>);

  // 4 (faces "A round hand")
  P(<>
    <WbTop step={4}/>
    <Part kind="together" title="Spot the good hand" how="Circle the tick for the good hand shape and the cross for a fault. Then tell your teacher what is wrong.">
      <BkGrid cols={3} gap="6px 10px">{PH_HAND.map(([id, , ok], i) => <PhPic key={id} art={'q-hand-' + id} ok={ok} n={i + 1} ex={i === 0} h={66}/>)}</BkGrid>
    </Part>
    <Part kind="home" title="Roller wrist and thumb" how="Do each one at the piano and tick a box each day.">
      <PhLog rows={['Fingertip on a key: sway the wrist up and down, then side to side', 'Knuckles up, like a bridge', 'The thumb bends in and plays on the side of its tip']} label={300}/>
    </Part>
    <Part kind="play" title="Hold the bubble" how="Hold a small ball (or a mandarin) in a round hand. Draw your hand round it, then colour a star for each.">
      <div style={{display:'grid',gridTemplateColumns:'1fr 200px',gap:14,flex:1,minHeight:150}}>
        <div style={{border:'1.5px solid ' + BK.line,borderRadius:10}}/>
        <div style={{display:'grid',gap:6,alignContent:'center'}}>{['knuckles up', 'round fingers', 'playing on the tips', 'the thumb on its side'].map(star)}</div>
      </div>
    </Part>
    <Faces/>
  </>);

  // 5 (faces "Finger numbers")
  P(<>
    <WbTop step="5-6" mins={10}/>
    <Part kind="together" title="Which finger?" how="Write the number of the coloured finger. Thumbs are 1 on both hands.">
      <BkGrid cols={6} gap="6px 8px">{W.fingers.map(([h, f], i) => <ExCell key={i} n={i + 1} ex={i === 0}><div style={{display:'flex',flexDirection:'column',alignItems:'center',gap:4,padding:'12px 2px 2px'}}>
        <PbArt name={'q-fingers-' + h} lit={f} h={74}/>{nvBox(i === 0, String(f), 34, 28)}
      </div></ExCell>)}</BkGrid>
    </Part>
    <Part kind="play" title="Trace your hands" how="Put each hand flat in its box and draw round it. Write the finger numbers on every finger -- the thumb is 1 on both hands! Then draw a ring on each finger 4." style={{padding:'7px 12px 8px'}}>
      <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:12,flex:1,minHeight:500}}>{['Left hand', 'Right hand'].map(l => <div key={l} style={{border:'1.5px solid ' + BK.line,borderRadius:10,display:'flex',alignItems:'flex-end',justifyContent:'center',fontSize:11.5,fontWeight:800,color:BK.muted,paddingBottom:4}}>{l}</div>)}</div>
      <div style={{display:'flex',flexWrap:'wrap',gap:'6px 18px',marginTop:9,fontSize:12,color:BK.ink,alignItems:'center'}}><b style={{color:BK.muted}}>Check:</b>{['5 fingers on each hand', 'Thumbs are 1', 'A ring round each finger 4', 'Left and right the right way round'].map(x => <span key={x} style={{display:'inline-flex',alignItems:'center',gap:5}}><span style={{width:15,height:15,border:'1.5px solid ' + BK.ink,borderRadius:4}}/>{x}</span>)}</div>
    </Part>
  </>);

  // 6 (faces "Finger walks")
  P(<>
    <WbTop step={7}/>
    <Part kind="together" title="Fill in the missing numbers" how="Write the missing finger numbers in the coral circles, then play the tune. The first one is done.">
      <div style={{display:'grid',gap:8}}>{PH_FILL.map(([name, seq], i) => <div key={name} style={{display:'grid',gridTemplateColumns:'130px 1fr',alignItems:'center',gap:10,border:'1px solid #ece6d8',borderRadius:10,padding:'7px 10px'}}>
        <span style={{fontFamily:"'Playfair Display', Georgia, serif",fontSize:15,fontWeight:800,color:BK.ink}}>{name}</span><PhCircles seq={seq} ex={i === 0}/>
      </div>)}</div>
    </Part>
    <Part kind="home" title="Finger walks this week" how="Play each tune. Tick it when the hand stays round and draws a little rainbow from key to key.">
      <PhLog rows={PH_TUNES.map((n, i) => (i + 1) + '  ' + n)} label={150}/>
    </Part>
    <Part kind="play" title="Make your own finger walk" how="Write a finger number (1 to 5) in each circle. Leave a circle empty to hold the note. Play it to your teacher!">
      <div style={{display:'grid',gap:12,justifyItems:'center'}}>
        <div style={{display:'flex',alignItems:'center',gap:8}}>{[0, 1, 2, 3, 'bar', 4, 5, 6, 7].map((k, i) => k === 'bar' ? <span key={i} style={{width:1.8,height:40,background:BK.ink,opacity:0.5,margin:'0 4px'}}/> : <span key={i} style={{width:40,height:40,borderRadius:20,border:'2px solid ' + BK.ink,background:'#fff'}}/>)}</div>
        <div style={{fontSize:13,color:BK.ink}}>My tune is called <span style={{display:'inline-block',width:220,borderBottom:'1px solid ' + BK.ink}}>&nbsp;</span></div>
      </div>
    </Part>
    <Faces/>
  </>);

  // 7 (faces "My five checks"): the chapter check-up
  const cnt = { st: 4, ar: 4, hs: 4, lr: 4, fn: 4, fw: 4 };
  P(<>
    <CheckHead total={24}/>
    {bkSec('A', 'A good set-up? Circle the tick or the cross.')}
    <BkGrid cols={4} gap="5px 10px">{W.chk.st.map(([id, , ok], i) => <PhPic key={id} art={'q-sit-' + id} ok={ok} n={i + 1} h={66}/>)}</BkGrid>
    {bkSec('B', 'The arm: yes or no?')}
    <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:4}}>{W.chk.ar.map(([txt, ok], i) => <TFRow key={i} txt={txt} ok={ok} n={i + 5} pad="12px 8px 4px"/>)}</div>
    {bkSec('C', 'A good hand shape? Circle the tick or the cross.')}
    <BkGrid cols={4} gap="5px 10px">{W.chk.hs.map(([id, , ok], i) => <PhPic key={id} art={'q-hand-' + id} ok={ok} n={i + 9} h={52}/>)}</BkGrid>
    {bkSec('D', 'Left or right hand? Write L or R.  E  Which finger is coloured?')}
    <BkGrid cols={4} gap="5px 10px">{W.chk.fn.map((f, i) => <BkCell key={i} n={(13 + i) + ' · ' + (17 + i)}><div style={{display:'flex',alignItems:'center',justifyContent:'center',gap:8,padding:'12px 4px 4px'}}>
      <PbArt name={'q-fingers-' + W.chk.lr[i] + '-plain'} lit={f} h={66}/>
      <div style={{display:'grid',gap:6,fontSize:10,fontWeight:900,color:BK.coral}}><span>D {bkBox(30, 24)}</span><span>E {bkBox(30, 24)}</span></div>
    </div></BkCell>)}</BkGrid>
    {bkSec('F', 'Finger walks: write the missing number.')}
    <BkGrid cols={4} gap="5px 10px">{PH_FILL_CHK.map((seq, i) => <BkCell key={i} n={21 + i}><div style={{display:'flex',justifyContent:'center',padding:'13px 2px 3px'}}><PhCircles seq={seq} size={22}/></div></BkCell>)}</BkGrid>
    <CheckTable concepts={C} cnt={cnt}/>
  </>);
  return <>{pages}</>;
}
function PostureTeacher() {
  const W = useMemo(() => phWorkbook(), [LANG]);
  const pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={pages.length + 1} chId="posture-hands" teacher>{content}</WbPage>);
  const yn = (ok) => ok ? '✓ tick' : '✗ cross';
  const fill = (seq) => seq.filter(x => x[0] === '?').map(x => x.slice(1)).join(', ');
  P(<>
    <div style={{fontFamily:"'Playfair Display', Georgia, serif",fontSize:28,fontWeight:900,color:BK.ink,margin:'2px 0 2px'}}>Teacher copy · {bkChapterName('posture-hands')}</div>
    <div style={{fontSize:12.5,color:BK.muted,margin:'0 0 12px',lineHeight:1.5}}>Each workbook page faces its Lesson Book page. Every answer here should also be tried at the piano -- the paper is only the reminder.</div>
    <TcBlock page={2} title="Sit at the piano" answers={<>{tcAns('TOGETHER', [PH_SIT[0], PH_SIT[1], PH_SIT[4], PH_SIT[2]].map(([, name, ok]) => yn(ok) + ' (' + name.toLowerCase() + ')'))}{tcAns('AT HOME', ['a tick for each check they really did'])}</>}
      watch="Elbows squashed in (too close) or arms reaching out (too far). Feet dangling: a footstool or a sturdy box fixes it. The five checks come before every time at the piano, for every student."
      say="“Sit tall, like a puppet on a string, and lean a little toward the piano.”"/>
    <TcBlock page={3} title="The arm leads" answers={<>{tcAns('TOGETHER', [PH_WARMUPS[0], ...W.order].map(([art, name]) => name + ' ' + (PH_WARMUPS.findIndex(x => x[0] === art) + 1)))}{tcAns('YES OR NO', PH_ARM.slice(0, 4).map(([, ok]) => ok ? 'yes' : 'no'))}</>}
      watch="The order goes from the big parts of the body to the small. After every key, watch the wrist: it comes straight back up to level and never sinks. The elbows stay away from the body."
      say="“Arms heavy, like wet spaghetti. Now rest them on the keys.”"/>
    <TcBlock page={4} title="A round hand" answers={<>{tcAns('TOGETHER', PH_HAND.map(([, name, ok]) => yn(ok) + (ok ? '' : ' (' + name.toLowerCase() + ')')))}</>}
      watch="The tip joint, especially on finger 5: for now, just help the student notice it. The wrist stays free, as if on a roller."
      say="“Hold a little bubble in your hand. Don't pop it!”"/>
    <TcBlock page={5} title="Finger numbers" answers={<>{tcAns('TOGETHER', W.fingers.map(([h, f]) => f + ' (' + h + ')'))}<div style={{fontSize:12,color:BK.ink}}>Trace: five fingers on each hand, the thumb numbered 1 on BOTH hands, a ring round each finger 4, left and right the right way round.</div></>}
      watch="Numbering the left hand from the little finger. The thumb is 1 on both hands."
      say="“Thumbs are always 1. Your hands are mirror twins.”"/>
  </>);
  P(<>
    <TcBlock page={6} title="Finger walks" answers={<>{tcAns('MISSING NUMBERS', PH_FILL.map(([name, seq]) => name + ': ' + fill(seq)))}<div style={{fontSize:12,color:BK.ink}}>Own tune: any numbers 1 to 5; check that it is played with a round hand and the empty circles are held.</div></>}
      watch="Right hand first, then left hand. Move on to the next tune only when the hand stays round. Relaxed, never squeezed tight."
      say="“Draw a little rainbow from key to key. Let the whole hand help.”"/>
    <TcBlock page={7} title="Check-up" goBack={phConcepts()} answers={<>{tcAns('A', W.chk.st.map(([, , ok]) => yn(ok)))}{tcAns('B', W.chk.ar.map(([, ok]) => ok ? 'yes' : 'no'))}{tcAns('C', W.chk.hs.map(([, , ok]) => yn(ok)))}{tcAns('D', W.chk.lr)}{tcAns('E', W.chk.fn)}{tcAns('F', PH_FILL_CHK.map(fill))}
      <div style={{fontSize:12,color:BK.ink,marginTop:6,lineHeight:1.5}}>Score each concept on its own (4 marks each, pass 3+). Then check the posture at the piano, not just on paper.</div></>}/>
  </>);
  return <>{pages}</>;
}
