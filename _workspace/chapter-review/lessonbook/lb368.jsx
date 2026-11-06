// ─── Phase 368: the Lesson Book, written as a book (Sohyun 2026-10-08) ───────────────────────────────
// Sohyun: the Lesson Book did not work as a lesson book -- it was the app's lesson printed on paper. Now the
// Lesson Book is the spine: every chapter gets its own hand-made pages, one idea per page (a big picture, two or
// three lines, AT THE PIANO steps, a REMEMBER line, a small TEACHER strip at the foot). The Workbook, the app and
// the public guide page follow it. Short exercises and tiny tunes by finger number, no full pieces (her repertoire
// is chosen per student). Chapters without their own pages yet still print the app lesson (LessonBookChapter).
// ?draft=1 marks, in yellow, the lines that wait for one of Sohyun's answers (B1..B8 in the review pack).
const LB_DRAFT = (() => { try { return new URLSearchParams(location.search).get('draft') === '1'; } catch (e) { return false; } })();
const LB_SERIF = "'Playfair Display', Georgia, serif";
function LbAsk({ q, children }) {
  if (!LB_DRAFT) return children;
  return <span data-lb-ask={q} style={{background:'#fff1a8',boxShadow:'0 0 0 2px #fff1a8',borderRadius:2}}><sup style={{fontSize:8,fontWeight:900,color:'#8a6d00',marginRight:2}}>{q}</sup>{children}</span>;
}
// One fixed A4 page of the Lesson Book.
function LbPage({ no, chId, kicker, title, teacher, qr, children }) {
  return (
    <section className="bk-page lb-page" data-lb-page={no}>
      <div className="lb-head" style={{display:'flex',justifyContent:'space-between',alignItems:'baseline',fontSize:10.5,color:BK.muted,fontWeight:700,borderBottom:'1.2px solid ' + BK.ink,paddingBottom:4,marginBottom:14}}>
        <span><b style={{color:BK.ink}}>Piano Butler</b> · Lesson Book</span>
        <span>Chapter {bkChapterNo(chId)} · {bkChapterName(chId)}</span>
      </div>
      {title && <div style={{margin:'0 0 12px'}}>
        {kicker && <div style={{fontSize:12.5,fontWeight:800,color:BK.coral,marginBottom:3}}>{kicker}</div>}
        <div style={{fontFamily:LB_SERIF,fontSize:36,fontWeight:900,color:BK.ink,lineHeight:1.05}}>{title}</div>
      </div>}
      <div className="bk-body" style={{flex:1,minHeight:0,overflow:'hidden',display:'flex',flexDirection:'column',gap:14}}><BkChapterCtx.Provider value={chId}>{children}</BkChapterCtx.Provider></div>
      {teacher && <div data-lb-teacher style={{display:'flex',gap:12,alignItems:'center',borderTop:'1.3px dashed ' + BK.line,marginTop:12,paddingTop:9}}>
        <span style={{flex:'0 0 auto',fontSize:9.5,fontWeight:900,letterSpacing:'0.06em',color:'#fff',background:BK.ink,borderRadius:4,padding:'3px 7px'}}>TEACHER</span>
        <div style={{flex:1,fontSize:11.8,color:BK.ink,lineHeight:1.45}}>{teacher}</div>
        {qr && <div style={{flex:'0 0 auto',display:'flex',alignItems:'center',gap:6}}><span style={{fontSize:9,color:BK.muted,textAlign:'right',lineHeight:1.2,width:48}}>Try it in the app</span><QR url={qr} size={46}/></div>}
      </div>}
      <div className="lb-no" style={{textAlign:'center',fontSize:10.5,color:BK.muted,fontWeight:700,paddingTop:6}}>{no}</div>
    </section>
  );
}
// the picture box takes whatever height the page has left, so every page ends level (it shrinks back to h when printed inside page margins)
function LbPic({ children, h, gap = 18, pad = '14px 16px' }) {
  return <div className="lb-pic" style={{background:BK.soft,borderRadius:16,padding:pad,display:'flex',alignItems:'center',justifyContent:'center',gap,minHeight:h,flex:'1 1 auto',flexWrap:'wrap'}}>{children}</div>;
}
function LbSay({ children, size = 16.5 }) {
  return <p style={{fontSize:size,lineHeight:1.5,color:BK.ink,margin:0}}>{children}</p>;
}
function LbKeysIcon({ size = 22 }) {
  return <svg viewBox="0 0 24 16" width={size} height={size * 16 / 24} aria-hidden="true"><rect x="1" y="1" width="22" height="14" rx="2" fill="#fff" stroke={BK.ink} strokeWidth="1.4"/>{[6.5, 12, 17.5].map(x => <line key={x} x1={x} x2={x} y1="1" y2="15" stroke={BK.ink} strokeWidth="1"/>)}{[5, 10.5, 16].map(x => <rect key={x} x={x} y="1" width="3" height="8" fill={BK.ink}/>)}</svg>;
}
function LbPiano({ steps, title = 'At the piano' }) {
  return (
    <div>
      <div style={{display:'flex',alignItems:'center',gap:8,marginBottom:7}}><LbKeysIcon/><span style={{fontFamily:LB_SERIF,fontSize:21,fontWeight:800,color:BK.ink}}>{title}</span></div>
      <div style={{display:'flex',flexDirection:'column',gap:7}}>
        {steps.map((s, i) => (
          <div key={i} style={{display:'flex',alignItems:'flex-start',gap:10,fontSize:15,lineHeight:1.45,color:BK.ink}}>
            <span style={{flex:'0 0 24px',height:24,borderRadius:12,background:BK.ink,color:'#fff',fontWeight:900,fontSize:13,display:'flex',alignItems:'center',justifyContent:'center'}}>{i + 1}</span>
            <span style={{flex:1,paddingTop:1}}>{s}</span>
            <span style={{flex:'0 0 auto',width:18,height:18,border:'1.6px solid ' + BK.ink,borderRadius:4,marginTop:3}}/>
          </div>
        ))}
      </div>
    </div>
  );
}
function LbRemember({ children }) {
  return (
    <div style={{display:'flex',alignItems:'center',gap:12,borderTop:'1.6px solid ' + BK.coral,borderBottom:'1.6px solid ' + BK.coral,padding:'4px 2px'}}>
      <PbArt name="rabbit-head" h={40}/>
      <span style={{fontSize:10.5,fontWeight:900,letterSpacing:'0.08em',color:BK.coral}}>REMEMBER</span>
      <span style={{fontSize:16.5,fontWeight:800,color:BK.ink}}>{children}</span>
    </div>
  );
}
// small "not like this" pictures under the big good one
function LbNot({ items }) {
  return (
    <div>
      <div style={{fontSize:12.5,fontWeight:800,color:BK.coral,marginBottom:5}}>Not like this</div>
      <div style={{display:'grid',gridTemplateColumns:'repeat(' + items.length + ',1fr)',gap:10}}>
        {items.map(([pic, cap], i) => <div key={i} style={{border:'1px solid #ece6d8',borderRadius:10,padding:'6px 6px 7px',display:'flex',flexDirection:'column',alignItems:'center',gap:3}}>
          {pic}<div style={{fontSize:11.5,fontWeight:700,color:BK.ink,textAlign:'center',lineHeight:1.25}}><span style={{color:BK.coral,fontWeight:900}}>✗</span> {cap}</div></div>)}
      </div>
    </div>
  );
}
// a tiny tune by finger numbers: one circle = one steady beat, a long oval = hold for one more beat
function LbTune({ name, how, seq, icon }) {
  return (
    <div style={{border:'1.6px dashed ' + BK.coral,borderRadius:14,padding:'8px 14px 10px',display:'flex',alignItems:'center',gap:14}}>
      {icon && <PbArt name={icon} h={66}/>}
      <div style={{flex:1,minWidth:0}}>
        <div style={{display:'flex',alignItems:'baseline',gap:10,flexWrap:'wrap'}}>
          <span style={{fontFamily:LB_SERIF,fontSize:19,fontWeight:800,color:BK.ink}}>{name}</span>
          <span style={{fontSize:12.5,color:BK.muted}}>{how}</span>
        </div>
        <div style={{display:'flex',flexWrap:'wrap',alignItems:'center',gap:6,marginTop:7}}>
          {seq.map((x, i) => x === '|' ? <span key={i} style={{width:1.6,height:28,background:BK.ink,opacity:0.5,margin:'0 4px'}}/>
            : x === '-' ? <span key={i} style={{width:28,height:28,borderRadius:14,border:'1.6px dashed ' + BK.line}}/>
            : <span key={i} style={{width:28,height:28,borderRadius:14,background:'#fff',border:'2px solid ' + BK.ink,display:'inline-flex',alignItems:'center',justifyContent:'center',fontSize:14.5,fontWeight:900,color:BK.ink}}>{x}</span>)}
        </div>
      </div>
    </div>
  );
}
// a captioned picture inside a page's picture box
function LbFig({ art, h, cap }) {
  return <div style={{display:'grid',justifyItems:'center',gap:5,width:'min-content'}}><PbArt name={art} h={h}/>{cap && <b style={{fontSize:13,color:BK.ink,textAlign:'center',lineHeight:1.3}}>{cap}</b>}</div>;
}

// ─── Chapter 1: Posture & Hand Shape (drawings: art369.jsx, pen and ink: the rabbit butler, a sister and a brother) ───
function PostureLessonBook() {
  const ch = 'posture-hands';
  const pages = [
    // 1. opener
    <LbPage key="1" no={1} chId={ch} teacher={<>This chapter is the base for every other one. The five checks on page 7 come before every time at the piano, for every student at every level, not only for beginners.</>} qr={bkLink('drill=' + ch + '&lock=1')}>
      <div data-ch={ch}>
        <div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>CHAPTER {bkChapterNo(ch)}</div>
        <div style={{fontFamily:LB_SERIF,fontSize:50,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>Posture &amp; Hand Shape</div>
      </div>
      <LbPic h={300}><LbFig art="puppet" h={350} cap="Sit tall, like a puppet on a string"/></LbPic>
      <LbSay size={18}>Before the first note: how to sit, and how to hold your hands. Get these right, and every note after them is easier.</LbSay>
      <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:20}}>
        <div>
          <div style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>In this chapter</div>
          {[['Sit at the piano', 2], ['Let the arm carry the hand', 3], ['A round hand', 4], ['Finger numbers', 5], ['Play: finger walks', 6], ['My five checks', 7]].map(([n, p]) => <div key={p} style={{display:'flex',justifyContent:'space-between',fontSize:14.5,padding:'5px 0',borderBottom:'1px solid #ece6d8'}}><span>{n}</span><span style={{color:BK.muted,fontWeight:700}}>page {p}</span></div>)}
        </div>
        <div>
          <div style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>By the end, you can</div>
          {['sit at the right height and distance', 'move your hand with the whole arm', 'make a round hand and play on the tips', 'say every finger number, on both hands'].map(x => <div key={x} style={{display:'flex',gap:9,alignItems:'flex-start',fontSize:14.5,padding:'5px 0',borderBottom:'1px solid #ece6d8'}}><span style={{flex:'0 0 16px',height:16,border:'1.6px solid ' + BK.ink,borderRadius:4,marginTop:3}}/><span>{x}</span></div>)}
        </div>
      </div>
      <div style={{fontSize:13,color:BK.muted}}>Goes with: the Workbook page beside each lesson page, and the online lesson (scan the code below).</div>
    </LbPage>,
    // 2. sit
    <LbPage key="2" no={2} chId={ch} kicker="Step 1" title="Sit at the piano"
      teacher={<>Watch for elbows squashed in (too close) or arms reaching out (too far). Feet dangling? A footstool or a sturdy box fixes it. Say: "Sit tall, like a puppet on a string."</>}>
      <LbPic h={250}><PbArt name="sit" h={310}/></LbPic>
      <LbSay>Two things to set: <b>how high</b> and <b>how far</b>. Your forearm is level with the keys, and your elbows sit just in front of your body.</LbSay>
      <LbPiano steps={[
        <>Sit on the <b>front half of the stool</b>, feet flat on the floor, leaning a little toward the piano.</>,
        <>Raise or lower the stool until your <b>forearm is level</b> with the keys.</>,
        <>Slide in or out until your <b>elbows are just in front of you</b>, about a fist away from your sides.</>,
      ]}/>
      <LbNot items={[[<PbArt name="not-sofa" h={104}/>, 'Leaning back, like on a sofa'], [<PbArt name="not-close" h={104}/>, 'So close the elbows squash in'], [<PbArt name="not-swing" h={104}/>, 'Too high: feet swinging']]}/>
      <LbRemember>Front half of the stool, feet flat, sit tall, leaning a little forward.</LbRemember>
    </LbPage>,
    // 3. arm -- the six warm-ups as one sequence, in Sohyun's order (2026-10-08): each move checks something the next one needs
    <LbPage key="3" no={3} chId={ch} kicker="Step 2" title="Let the arm carry the hand"
      teacher={<>Do all six in this order: each one checks something the next one needs. After every key, watch the wrist: it comes straight back up to level and never sinks. Say: "Arms heavy, like wet spaghetti. Now rest them on the keys."</>}>
      <LbSay>Your fingertips stay connected to the piano, but the <b>whole arm</b> does the work: from above, it leads the hand and the fingers. Six moves, <b>in this order</b>, from the big parts of the body to the small ones: each one gets the arm ready for the next.</LbSay>
      <div style={{display:'grid',gridTemplateColumns:'repeat(3,minmax(0,1fr))',gap:14,flex:'1 1 auto',minHeight:0,alignContent:'center'}}>
        {[['ragdoll', 'Rag doll', 'Flop forward and let both arms hang heavy. Shake them loose, then float the hands up and set them gently on the keys.'],
          ['wings', 'Elbow wings', 'Check the elbows are free, not stuck to your body: let them float out like wings, then back. Stop in the middle, a fist from your body.'],
          ['glide', 'Arm glide', 'Now the whole arm: skate along the keys. The round hand rides on the arm to the next group of keys. The fingers ride, they don\u2019t walk.'],
          ['dive', 'Arm drop', 'Lift the whole arm and let it drop into a key on finger 3: firm tip, soft wrist, a round sound.'],
          ['bridge', 'Knuckle bridge', 'Check the bridge: your knuckles are a bridge a little car can drive over. Press one key slowly and hold for 3: the bridge stays up.'],
          ['balloon', 'Wrist balloon', 'Check the wrist never sinks: as the key goes down, a balloon lifts the wrist straight back up to level. The fingertip stays on the key.']].map(([a, n, how], i) => (
          <div key={n} style={{border:'1px solid #ece6d8',borderRadius:12,padding:'8px 10px 10px',display:'flex',flexDirection:'column',gap:5,minHeight:0}}>
            <div style={{background:BK.soft,borderRadius:8,height:196,display:'flex',alignItems:'center',justifyContent:'center',overflow:'hidden'}}><PbArt name={a} h={176} style={{maxWidth:'100%'}}/></div>
            <div style={{display:'flex',alignItems:'center',gap:7}}>
              <span style={{flex:'0 0 22px',height:22,borderRadius:11,background:BK.ink,color:'#fff',fontWeight:900,fontSize:12.5,display:'flex',alignItems:'center',justifyContent:'center'}}>{i + 1}</span>
              <span style={{fontFamily:LB_SERIF,fontSize:16.5,fontWeight:800,color:BK.ink}}>{n}</span>
            </div>
            <div style={{fontSize:12.5,color:BK.ink,lineHeight:1.4}}>{how}</div>
          </div>))}
      </div>
      <LbRemember>The arm leads from above, elbows free. Even while a finger presses a key, the whole arm stays free.</LbRemember>
    </LbPage>,
    // 4. round hand
    <LbPage key="4" no={4} chId={ch} kicker="Step 3" title="A round hand"
      teacher={<>Watch the tip joint, especially on finger 5: for now, just help the student notice it. Say: "Hold a little bubble in your hand. Don't pop it!"</>}>
      <LbPic h={200} gap={24}>
        <LbFig art="hand-good" h={168} cap="Round, like holding a ball"/>
        <LbFig art="hand-thumb" h={128} cap="The thumb bends in and plays on the side of its tip, like a tipped boat"/>
      </LbPic>
      <LbSay>Let your arms hang, then lift your hands as if you were holding a small ball. Keep that shape when the hand goes on the keys. <b>Knuckles up</b> like a bridge, and play on the <b>fingertips</b>. The wrist stays free: with the fingertip on the key, the hand can sway up and down and side to side, as if a <b>roller</b> sat under your forearm.</LbSay>
      <LbPiano steps={[
        <>Hands on your knees. Hold an imaginary ball.</>,
        <>Move the ball shape onto the keys without squashing it.</>,
        <>Play one key with each finger, on the tip. The knuckles stay up.</>,
        <>Fingertip on a key: sway the wrist up and down, then side to side, as if on a roller. Notice the knuckles and the tip, and try not to let them cave in.</>,
      ]}/>
      <LbNot items={[[<PbArt name="hand-flat" h={80}/>, 'Flat fingers'], [<PbArt name="hand-cave" h={80}/>, 'Tip joint caving in'], [<PbArt name="hand-high" h={80}/>, 'Wrist stiff and high']]}/>
      <LbRemember>A free wrist, as if on a roller. Keep an eye on the knuckles and fingertips.</LbRemember>
    </LbPage>,
    // 5. finger numbers
    <LbPage key="5" no={5} chId={ch} kicker="Step 4" title="Finger numbers"
      teacher={<>Watch for the left hand numbered from the little finger. Say: "Thumbs are always 1. Your hands are mirror twins."</>} qr={bkLink('drill=' + ch + '&tab=drill&level=3')}>
      <LbPic h={220} gap={40}><PbArt name="hand-L" h={210}/><PbArt name="hand-R" h={210}/></LbPic>
      <LbSay>Every finger has a number, <b>1 to 5, starting from the thumb</b>. It's the same on both hands: both thumbs are 1, and both little fingers are 5.</LbSay>
      <div style={{display:'flex',flexWrap:'wrap',gap:8}}>
        {['1 Captain Thumb', '2 Pointer', '3 Tall Middle', '4 Shy Ring', '5 Baby Pinky'].map(x => <span key={x} style={{border:'1.6px solid ' + BK.ink,borderRadius:999,padding:'4px 13px',fontSize:14,fontWeight:800}}>{x}</span>)}
      </div>
      <div style={{display:'grid',gridTemplateColumns:'1fr 250px',gap:18,alignItems:'center'}}>
        <LbPiano title="The mirror game" steps={[
          <>Hold both hands up. Wiggle each finger as you say its number.</>,
          <>Your teacher calls "Right hand, 3!" and you wiggle it. Try ten calls.</>,
          <>Swap: you call the finger, and your teacher wiggles it.</>,
        ]}/>
        <div style={{background:BK.soft,borderRadius:12,padding:'6px 4px',display:'flex',justifyContent:'center'}}><PbArt name="mirror" h={170}/></div>
      </div>
      <LbRemember>Fingers are numbered 1 to 5 from the thumb, on both hands.</LbRemember>
    </LbPage>,
    // 6. finger walks
    <LbPage key="6" no={6} chId={ch} kicker="Play" title="Finger walks"
      teacher={<>Right hand first, then left hand, then together if it is easy. Move on to the next tune only when the hand stays round. Any five white keys near the middle will do; your teacher shows where to put the hand, and the letter names come in chapter 3.</>}>
      <LbSay>Now put it together: sit well, make a round hand, and play. <b>Start small:</b> one note, then two, three, four, and all five. From key to key, the hand draws a little <b>rainbow</b>: relaxed, never squeezed tight, the whole hand helping. <b>One circle is one steady beat.</b></LbSay>
      <LbPic h={164} gap={48} pad="6px 18px">
        <LbFig art="keys-hand-L" h={152}/>
        <LbFig art="keys-hand-R" h={152}/>
      </LbPic>
      <LbTune icon="tune-hop" name="Hop on 3" how="one note: an arm drop on every 3" seq={['3', '-', '3', '-', '|', '3', '3', '3', '-']}/>
      <LbTune icon="tune-neighbours" name="Neighbours" how="two notes, next door, taking turns" seq={['2', '3', '2', '3', '|', '3', '2', '3', '-']}/>
      <LbTune icon="tune-hill3" name="Up and back" how="three notes: up, then back down" seq={['1', '2', '3', '-', '|', '3', '2', '1', '-']}/>
      <LbTune icon="tune-hill4" name="Little hill" how="four notes: up the hill and down" seq={['1', '2', '3', '4', '|', '3', '2', '1', '-']}/>
      <LbTune icon="tune-stairs" name="Stairs and slide" how="all five: up the stairs, then down the slide" seq={['1', '2', '3', '4', '5', '-', '|', '5', '4', '3', '2', '1', '-']}/>
      <div style={{fontSize:13,color:BK.muted}}>An empty dashed circle means: hold the note for one more beat.</div>
      <LbRemember>A little rainbow from key to key. Relaxed: the whole hand helps.</LbRemember>
    </LbPage>,
    // 7. five checks
    <LbPage key="7" no={7} chId={ch} kicker="Step 5" title="My five checks"
      teacher={<>At the start of each lesson, the student says the five checks out loud while doing them; you only correct. When all five are easy, do the Chapter check-up in the Workbook.</>}>
      <LbSay>Before you play, every time. Give yourself a star for each check in each lesson.</LbSay>
      <div style={{display:'flex',flexDirection:'column',gap:9,flex:'1 1 auto'}}>
        <div style={{display:'grid',gridTemplateColumns:'150px 1fr repeat(6, 34px)',gap:8,alignItems:'end',fontSize:11,fontWeight:800,color:BK.muted,textAlign:'center'}}><span/><span style={{textAlign:'right',paddingRight:6}}>Lesson</span>{[1, 2, 3, 4, 5, 6].map(n => <span key={n}>{n}</span>)}</div>
        {[['chk-front', 'Front half of the stool'], ['chk-feet', 'Feet flat, leaning a little toward the piano'], ['chk-tall', 'Sit tall, like a puppet on a string'], ['chk-forearm', 'Forearm level with the keys, elbows away from your body'], ['chk-hand', 'Round hand, play on the tips']].map(([a, txt], i) => (
          <div key={i} style={{display:'grid',gridTemplateColumns:'150px 1fr repeat(6, 34px)',gap:8,alignItems:'center',border:'1px solid #ece6d8',borderRadius:12,padding:'4px 8px',flex:'1 1 auto'}}>
            <div style={{display:'flex',justifyContent:'center'}}><PbArt name={a} h={a === 'chk-hand' ? 86 : 108}/></div>
            <div style={{fontSize:15.5,fontWeight:800,color:BK.ink}}>{txt}</div>
            {[1, 2, 3, 4, 5, 6].map(n => <span key={n} style={{width:30,height:30,border:'1.5px solid ' + BK.line,borderRadius:8,justifySelf:'center',display:'flex',alignItems:'center',justifyContent:'center'}}><BkStarG size={14} fill="#ece6d8"/></span>)}
          </div>))}
      </div>
      <LbRemember>Check your posture before every practice.</LbRemember>
    </LbPage>,
  ];
  return <>{pages}</>;
}
const LESSON_BOOKS = { 'posture-hands': PostureLessonBook };
// Printed alone, a chapter's pages use the Workbook's fixed A4 frame (BookRoot's fixed css). Printed with chapters
// that are still the app lesson (?ch=all), they sit inside that book's page margins: 264 mm tall, no padding.
const LB_CSS = PB_KID_CSS + ` .lb-page button { display: none !important; }
  .lb-page .bk-body > *:not(.lb-pic) { flex-shrink: 0 }
  .lb-ex > * { width: 100%; } .lb-ex svg { width: 100% !important; height: 146px !important; max-width: none !important; }`;
const LB_FLOW_CSS = LB_CSS + ` .bk-lesson .lb-page, .lb-page { width: 178mm; height: 263mm; margin: 0 auto; padding: 0; display: flex; flex-direction: column; break-after: page; overflow: hidden; }
  .bk-lesson + .bk-lesson .bk-chapter, .lb-page + .bk-lesson .bk-chapter { break-before: page; }
  .lb-page .lb-pic { min-height: 0 !important; }
  .lb-page .lb-head, .lb-page .lb-no { display: none !important; }`;
