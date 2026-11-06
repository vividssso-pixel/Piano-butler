// ─── Phase 376: one Lesson Book, opened two ways (Sohyun 2026-10-08) ───
// "The online lesson should open exactly like the Lesson Book; only what can move is different." The chapter's
// pages are written once (postureLbPages); printed, they are the A4 Lesson Book; on screen, each page after the
// opener is one step of the online lesson, with the same words and drawings, and LbLive swaps a still picture for
// its moving version. Words are t(English, Korean), so the app keeps its Korean; the books print in English.
const LbScreenCtx = React.createContext(false);
const lbScreen = () => React.useContext(LbScreenCtx);
function LbLive({ still, live }) { return lbScreen() ? live : still; }
function LbOnly({ print, screen, children }) { return (lbScreen() ? screen : print) ? children : null; }
// an "At the piano" tick box: printed, an empty box; on screen, a box the student can tick
function LbTick({ label }) {
  const [on, setOn] = useState(false);
  if (!lbScreen()) return <span style={{flex:'0 0 auto',width:18,height:18,border:'1.6px solid ' + BK.ink,borderRadius:4,marginTop:3}}/>;
  return <button onClick={() => setOn(v => !v)} aria-pressed={on} aria-label={label} style={{flex:'0 0 auto',width:24,height:24,border:'1.8px solid ' + BK.ink,borderRadius:5,marginTop:0,background:on ? BK.ink : '#fff',color:'#fff',fontWeight:900,fontSize:14,lineHeight:1,padding:0,cursor:'pointer'}}>{on ? '✓' : ''}</button>;
}
// a page of the book, on screen (the opener's page is the lesson's head instead)
function LbScreenPage({ page }) {
  const { teacher, children } = page.props;
  return (
    <LbScreenCtx.Provider value={true}>
      <BkChapterCtx.Provider value={page.props.chId}>
        <div className="lb-screen" data-lb-screen={page.props.no} style={{display:'flex',flexDirection:'column',gap:14,margin:'4px 0 6px'}}>
          {children}
          {teacher && <TeacherOnly><div data-lb-teacher style={{display:'flex',gap:10,alignItems:'flex-start',borderTop:'1.3px dashed ' + BK.line,paddingTop:9}}>
            <span style={{flex:'0 0 auto',fontSize:9.5,fontWeight:900,letterSpacing:'0.06em',color:'#fff',background:BK.ink,borderRadius:4,padding:'3px 7px',marginTop:2}}>{t('TEACHER', '선생님')}</span>
            <div style={{flex:1,fontSize:13,color:BK.ink,lineHeight:1.5}}>{teacher}</div>
          </div></TeacherOnly>}
        </div>
      </BkChapterCtx.Provider>
    </LbScreenCtx.Provider>
  );
}
const LB_SCREEN_CSS = ` .lb-screen .lb-pic { min-height: 0 !important; } .lb-screen .pb-art { max-width: 100%; }`;

// the six warm-ups' names and how-tos (the Lesson Book's page 3 and the Toolbox)
function postureWarmCards() {
  return [[t('Rag doll', '헝겊 인형'), t('Flop forward and let both arms hang heavy. Shake them loose, then float the hands up and set them gently on the keys.', '앞으로 털썩 숙여 두 팔을 무겁게 늘어뜨려요. 흔들어 힘을 빼고, 손을 둥실 올려 건반 위에 살포시 내려놓아요.')],
    [t('Elbow wings', '팔꿈치 날개'), t('Check the elbows are free, not stuck to your body: let them float out like wings, then back. Stop in the middle, a fist from your body.', '팔꿈치가 몸에 붙지 않고 자유로운지 확인해요: 날개처럼 둥실 벌렸다가 돌아와요. 몸에서 주먹 하나만큼 떨어진 가운데에서 멈춰요.')],
    [t('Arm glide', '팔 미끄럼'), t('Now the whole arm: skate along the keys. The round hand rides on the arm to the next group of keys. The fingers ride, they don’t walk.', '이제 팔 전체로 건반 위를 스케이트 타듯 지나가요. 둥근 손은 팔을 타고 다음 건반 묶음으로 가요. 손가락은 걷지 않고 타고 가요.')],
    [t('Arm drop', '팔 떨어뜨리기'), t('Lift the whole arm and let it drop into a key on finger 3: firm tip, soft wrist, a round sound.', '팔 전체를 들었다가 3번 손가락으로 건반에 떨어뜨려요: 단단한 손끝, 부드러운 손목, 둥근 소리.')],
    [t('Knuckle bridge', '마디 다리'), t('Check the bridge: your knuckles are a bridge a little car can drive over. Press one key slowly and hold for 3: the bridge stays up.', '다리를 확인해요: 손가락 마디는 작은 자동차가 지나갈 수 있는 다리예요. 건반 하나를 천천히 누르고 셋을 세는 동안 그대로: 다리는 무너지지 않아요.')],
    [t('Wrist balloon', '손목 풍선'), t('Check the wrist never sinks: as the key goes down, a balloon lifts the wrist straight back up to level. The fingertip stays on the key.', '손목이 가라앉지 않는지 확인해요: 건반이 내려가면 풍선이 손목을 바로 같은 높이까지 다시 들어 올려요. 손끝은 건반 위에 그대로 있어요.')]];
}
// ─── Chapter 1: Posture & Hand Shape ───
// scr: true when the pages are shown as the online lesson (decided by the caller: page JSX is built outside the screen context)
function postureLbPages(scr = false) {
  const ch = 'posture-hands';
  const checks5 = [['chk-front', t('Front half of the stool', '의자 앞쪽 절반에 앉기')], ['chk-feet', t('Feet flat, leaning a little toward the piano', '발은 평평하게, 피아노 쪽으로 살짝 기울여요')], ['chk-tall', t('Sit tall, like a puppet on a string', '줄에 매달린 인형처럼 곧게 앉기')], ['chk-forearm', t('Forearm level with the keys, elbows away from your body', '팔뚝은 건반과 수평, 팔꿈치는 몸에서 띄워요')], ['chk-hand', t('Round hand, play on the tips', '둥근 손으로 손끝으로 치기')]];
  return [
    // 1. opener
    <LbPage key="1" no={1} chId={ch} teacher={<>{t('This chapter is the base for every other one. The five checks on page 7 come before every time at the piano, for every student at every level, not only for beginners.', '이 챕터는 다른 모든 챕터의 바탕이에요. 7쪽의 다섯 가지 확인은 초보자만이 아니라 모든 학생이, 피아노 앞에 앉을 때마다 먼저 해요.')}</>} qr={bkLink('drill=' + ch + '&lock=1')}>
      <LbOnly print><div data-ch={ch}>
        <div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>CHAPTER {bkChapterNo(ch)}</div>
        <div style={{fontFamily:LB_SERIF,fontSize:50,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{t('Posture & Hand Shape', '자세와 손 모양')}</div>
      </div></LbOnly>
      <LbPic h={300}><LbFig art="puppet" h={350} cap={t('Sit tall, like a puppet on a string', '줄에 매달린 인형처럼 곧게 앉아요')}/></LbPic>
      <LbSay size={18}>{t('Before the first note: how to sit, and how to hold your hands. Get these right, and every note after them is easier.', '첫 음을 치기 전에: 어떻게 앉고, 손을 어떻게 둘지 배워요. 이걸 잘 잡으면 그다음 모든 음이 쉬워져요.')}</LbSay>
      <div style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:20}}>
        <LbOnly print><div>
          <div style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>In this chapter</div>
          {[['Sit at the piano', 2], ['Let the arm carry the hand', 3], ['A round hand', 4], ['Finger numbers', 5], ['Play: finger walks', 6], ['My five checks', 7]].map(([n, p]) => <div key={p} style={{display:'flex',justifyContent:'space-between',fontSize:14.5,padding:'5px 0',borderBottom:'1px solid #ece6d8'}}><span>{n}</span><span style={{color:BK.muted,fontWeight:700}}>page {p}</span></div>)}
        </div></LbOnly>
        <div>
          <div style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('By the end, you can', '이 챕터를 마치면')}</div>
          {[t('sit at the right height and distance', '알맞은 높이와 거리로 앉을 수 있어요'), t('move your hand with the whole arm', '팔 전체로 손을 움직일 수 있어요'), t('make a round hand and play on the tips', '둥근 손으로, 손끝으로 칠 수 있어요'), t('say every finger number, on both hands', '양손의 손가락 번호를 모두 말할 수 있어요')].map(x => <div key={x} style={{display:'flex',gap:9,alignItems:'flex-start',fontSize:14.5,padding:'5px 0',borderBottom:'1px solid #ece6d8'}}><span style={{flex:'0 0 16px',height:16,border:'1.6px solid ' + BK.ink,borderRadius:4,marginTop:3}}/><span>{x}</span></div>)}
        </div>
      </div>
      <LbOnly print><div style={{fontSize:13,color:BK.muted}}>Goes with: the Workbook page beside each lesson page, and the online lesson (scan the code below).</div></LbOnly>
    </LbPage>,
    // 2. sit
    <LbPage key="2" no={2} chId={ch} kicker={t('Step 1', '1단계')} title={t('Sit at the piano', '피아노 앞에 앉기')}
      teacher={<>{t('Watch for elbows squashed in (too close) or arms reaching out (too far). Feet dangling? A footstool or a sturdy box fixes it. Say: "Sit tall, like a puppet on a string."', '팔꿈치가 몸에 눌리는지(너무 가까움), 팔이 앞으로 멀리 뻗는지(너무 멂) 봐 주세요. 발이 대롱대롱하면 발판이나 튼튼한 상자를 놓아요. 이렇게 말해 주세요: "줄에 매달린 인형처럼 곧게 앉자."')}</>}>
      <LbLive still={<LbPic h={250}><PbArt name="sit" h={310}/></LbPic>} live={<SitCheck/>}/>
      <LbSay>{LANG === 'ko' ? <>맞출 것은 두 가지예요: <b>높이</b>와 <b>거리</b>. 팔뚝은 건반과 수평이고, 팔꿈치는 몸 바로 앞에 있어요.</> : <>Two things to set: <b>how high</b> and <b>how far</b>. Your forearm is level with the keys, and your elbows sit just in front of your body.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <><b>의자 앞쪽 절반</b>에 앉고, 발은 바닥에 평평하게, 피아노 쪽으로 살짝 기울여요.</>,
        <><b>팔뚝이 건반과 수평</b>이 될 때까지 의자를 올리거나 내려요.</>,
        <><b>팔꿈치가 몸 바로 앞에</b> 오도록, 옆구리에서 주먹 하나만큼 떨어지게 의자를 앞뒤로 옮겨요.</>,
      ] : [
        <>Sit on the <b>front half of the stool</b>, feet flat on the floor, leaning a little toward the piano.</>,
        <>Raise or lower the stool until your <b>forearm is level</b> with the keys.</>,
        <>Slide in or out until your <b>elbows are just in front of you</b>, about a fist away from your sides.</>,
      ]}/>
      <LbNot items={[[<PbArt name="not-sofa" h={104}/>, t('Leaning back, like on a sofa', '소파처럼 뒤로 기대기')], [<PbArt name="not-close" h={104}/>, t('So close the elbows squash in', '너무 가까워서 팔꿈치가 눌려요')], [<PbArt name="not-swing" h={104}/>, t('Too high: feet swinging', '너무 높아서 발이 대롱대롱')]]}/>
      <LbRemember>{t('Front half of the stool, feet flat, sit tall, leaning a little forward.', '의자 앞쪽 절반, 발은 평평하게, 곧게 앉아 앞으로 살짝 기울여요.')}</LbRemember>
    </LbPage>,
    // 3. arm -- the six warm-ups as one sequence, in Sohyun's order (2026-10-08): each move checks something the next one needs
    <LbPage key="3" no={3} chId={ch} kicker={t('Step 2', '2단계')} title={t('Let the arm carry the hand', '팔이 손을 데려가요')}
      teacher={<>{t('Do all six in this order: each one checks something the next one needs. After every key, watch the wrist: it comes straight back up to level and never sinks. Say: "Arms heavy, like wet spaghetti. Now rest them on the keys."', '여섯 가지를 이 순서대로 해요: 하나하나가 다음 동작에 필요한 것을 확인해 줘요. 건반을 칠 때마다 손목을 봐 주세요: 바로 같은 높이로 다시 올라오고, 절대 가라앉지 않아요. 이렇게 말해 주세요: "팔이 젖은 스파게티처럼 무거워. 이제 건반 위에 살짝 내려놓자."')}</>}>
      <LbSay>{LANG === 'ko' ? <>손끝은 늘 피아노와 이어져 있지만, 일은 <b>팔 전체</b>가 해요: 위에서 손과 손가락을 이끌어요. 여섯 가지 동작을 <b>이 순서대로</b>, 큰 몸 부분부터 작은 부분까지 해요. 하나하나가 다음 동작을 준비해 줘요.</>
        : <>Your fingertips stay connected to the piano, but the <b>whole arm</b> does the work: from above, it leads the hand and the fingers. Six moves, <b>in this order</b>, from the big parts of the body to the small ones: each one gets the arm ready for the next.</>}</LbSay>
      <LbLive live={<WarmUps376 cards={postureWarmCards()}/>} still={
      <div style={{display:'grid',gridTemplateColumns:scr ? 'repeat(auto-fill, minmax(min(100%, 170px), 1fr))' : 'repeat(3,minmax(0,1fr))',gap:14,flex:'1 1 auto',minHeight:0,alignContent:'center'}}>
        {postureWarmCards().map(([n, how], i) => [WARM_UPS[i].id, n, how]).map(([a, n, how], i) => (
          <div key={a} style={{border:'1px solid #ece6d8',borderRadius:12,padding:'8px 10px 10px',display:'flex',flexDirection:'column',gap:5,minHeight:0}}>
            <div style={{background:BK.soft,borderRadius:8,height:scr ? 150 : 196,display:'flex',alignItems:'center',justifyContent:'center',overflow:'hidden'}}><PbArt name={a} h={scr ? 134 : 176} style={{maxWidth:'100%'}}/></div>
            <div style={{display:'flex',alignItems:'center',gap:7}}>
              <span style={{flex:'0 0 22px',height:22,borderRadius:11,background:BK.ink,color:'#fff',fontWeight:900,fontSize:12.5,display:'flex',alignItems:'center',justifyContent:'center'}}>{i + 1}</span>
              <span style={{fontFamily:LB_SERIF,fontSize:16.5,fontWeight:800,color:BK.ink}}>{n}</span>
            </div>
            <div style={{fontSize:scr ? 13.5 : 12.5,color:BK.ink,lineHeight:1.4}}>{how}</div>
          </div>))}
      </div>}/>
      <LbRemember>{t('The arm leads from above, elbows free. Even while a finger presses a key, the whole arm stays free.', '팔이 위에서 이끌고, 팔꿈치는 자유롭게. 손가락이 건반을 누르는 동안에도 팔 전체는 자유로워요.')}</LbRemember>
    </LbPage>,
    // 4. round hand
    <LbPage key="4" no={4} chId={ch} kicker={t('Step 3', '3단계')} title={t('A round hand', '둥근 손')}
      teacher={<>{t('Watch the tip joint, especially on finger 5: for now, just help the student notice it. Say: "Hold a little bubble in your hand. Don\'t pop it!"', '손끝 관절을, 특히 5번 손가락을 봐 주세요: 지금은 학생이 알아차리도록만 도와요. 이렇게 말해 주세요: "손 안에 작은 비눗방울을 쥐고 있어. 터뜨리지 마!"')}</>}>
      <LbLive still={<LbPic h={200} gap={24}>
        <LbFig art="hand-good" h={168} cap={t('Round, like holding a ball', '공을 쥔 것처럼 둥글게')}/>
        <LbFig art="hand-thumb" h={128} cap={t('The thumb bends in and plays on the side of its tip, like a tipped boat', '엄지는 안으로 꺾여 손끝 옆면으로 쳐요. 옆으로 누운 배처럼')}/>
      </LbPic>} live={<>
        <RoundHand376/>
        <LbPic h={120}><LbFig art="hand-thumb" h={118} cap={t('The thumb bends in and plays on the side of its tip, like a tipped boat', '엄지는 안으로 꺾여 손끝 옆면으로 쳐요. 옆으로 누운 배처럼')}/></LbPic>
      </>}/>
      <LbSay>{LANG === 'ko' ? <>팔을 늘어뜨렸다가, 작은 공을 쥐듯이 손을 들어 올려요. 손이 건반 위로 가도 그 모양 그대로예요. <b>손가락 마디는 다리처럼 위로</b>, <b>손끝</b>으로 쳐요. 손목은 자유롭게: 손끝을 건반에 댄 채로, 팔뚝 아래 <b>롤러</b>가 있는 것처럼 손이 위아래, 좌우로 흔들려요.</>
        : <>Let your arms hang, then lift your hands as if you were holding a small ball. Keep that shape when the hand goes on the keys. <b>Knuckles up</b> like a bridge, and play on the <b>fingertips</b>. The wrist stays free: with the fingertip on the key, the hand can sway up and down and side to side, as if a <b>roller</b> sat under your forearm.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>손을 무릎에 올리고, 상상의 공을 쥐어요.</>,
        <>공 모양을 찌그러뜨리지 않고 건반 위로 옮겨요.</>,
        <>손가락마다 건반 하나씩, 손끝으로 쳐요. 마디는 위로 그대로.</>,
        <>손끝을 건반에 대고: 롤러 위에 있는 것처럼 손목을 위아래로, 그다음 좌우로 흔들어요. 마디와 손끝을 살펴보고, 무너지지 않게 해 봐요.</>,
      ] : [
        <>Hands on your knees. Hold an imaginary ball.</>,
        <>Move the ball shape onto the keys without squashing it.</>,
        <>Play one key with each finger, on the tip. The knuckles stay up.</>,
        <>Fingertip on a key: sway the wrist up and down, then side to side, as if on a roller. Notice the knuckles and the tip, and try not to let them cave in.</>,
      ]}/>
      <LbNot items={[[<PbArt name="hand-flat" h={80}/>, t('Flat fingers', '납작한 손가락')], [<PbArt name="hand-cave" h={80}/>, t('Tip joint caving in', '손끝 관절이 꺾여요')], [<PbArt name="hand-high" h={80}/>, t('Wrist stiff and high', '손목이 굳고 높아요')]]}/>
      <LbRemember>{t('A free wrist, as if on a roller. Keep an eye on the knuckles and fingertips.', '롤러 위에 있는 것처럼 자유로운 손목. 마디와 손끝을 살펴봐요.')}</LbRemember>
    </LbPage>,
    // 5. finger numbers
    <LbPage key="5" no={5} chId={ch} kicker={t('Step 4', '4단계')} title={t('Finger numbers', '손가락 번호')}
      teacher={<>{t('Watch for the left hand numbered from the little finger. Say: "Thumbs are always 1. Your hands are mirror twins."', '왼손을 새끼손가락부터 세는지 봐 주세요. 이렇게 말해 주세요: "엄지는 언제나 1번. 두 손은 거울 쌍둥이야."')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=3')}>
      <LbLive still={<LbPic h={220} gap={40}><PbArt name="hand-L" h={210}/><PbArt name="hand-R" h={210}/></LbPic>} live={<FingerNumbers376/>}/>
      <LbSay>{LANG === 'ko' ? <>손가락마다 번호가 있어요. <b>엄지부터 1번에서 5번까지</b>예요. 양손이 똑같아요: 두 엄지는 1번, 두 새끼손가락은 5번이에요.</>
        : <>Every finger has a number, <b>1 to 5, starting from the thumb</b>. It's the same on both hands: both thumbs are 1, and both little fingers are 5.</>}</LbSay>
      <div style={{display:'flex',flexWrap:'wrap',gap:8}}>
        {FINGER_NAMES.map((n, i) => (i + 1) + ' ' + t(n.en, n.ko)).map(x => <span key={x} style={{border:'1.6px solid ' + BK.ink,borderRadius:999,padding:'4px 13px',fontSize:14,fontWeight:800}}>{x}</span>)}
      </div>
      <div style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 250px',gap:18,alignItems:'center'}}>
        <LbPiano title={t('The mirror game', '거울 게임')} steps={LANG === 'ko' ? [
          <>두 손을 들어요. 손가락을 하나씩 꼼지락거리며 번호를 말해요.</>,
          <>선생님이 "오른손 3번!" 하고 부르면 그 손가락을 꼼지락거려요. 열 번 해 봐요.</>,
          <>바꿔요: 내가 손가락을 부르고, 선생님이 꼼지락거려요.</>,
        ] : [
          <>Hold both hands up. Wiggle each finger as you say its number.</>,
          <>Your teacher calls "Right hand, 3!" and you wiggle it. Try ten calls.</>,
          <>Swap: you call the finger, and your teacher wiggles it.</>,
        ]}/>
        <div style={{background:BK.soft,borderRadius:12,padding:'6px 4px',display:'flex',justifyContent:'center'}}><PbArt name="mirror" h={170}/></div>
      </div>
      <LbRemember>{t('Fingers are numbered 1 to 5 from the thumb, on both hands.', '양손 모두, 엄지부터 1번에서 5번까지.')}</LbRemember>
    </LbPage>,
    // 6. finger walks
    <LbPage key="6" no={6} chId={ch} kicker={t('Play', '연주')} title={t('Finger walks', '손가락 걷기')}
      teacher={<>{t('Right hand first, then left hand, then together if it is easy. Move on to the next tune only when the hand stays round. Any five white keys near the middle will do; your teacher shows where to put the hand, and the letter names come in chapter 3.', '오른손 먼저, 그다음 왼손, 쉬우면 양손 함께 해요. 손이 둥글게 유지될 때만 다음 곡으로 넘어가요. 가운데 근처 흰 건반 다섯 개면 어디든 괜찮아요. 손 놓을 자리는 선생님이 보여 주고, 음이름은 챕터 3에서 배워요.')}</>}>
      <LbSay>{LANG === 'ko' ? <>앉은 자세, 둥근 손으로 쳐 봐요. <b>작게 시작해요:</b> 한 음, 그다음 두 음, 세 음, 네 음, 다섯 음. 건반에서 건반으로 손이 작은 <b>무지개</b>를 그려요: 꽉 쥐지 않고 편하게, 손 전체가 도와줘요. <b>동그라미 하나가 일정한 박 하나</b>예요.</>
        : <>Now put it together: sit well, make a round hand, and play. <b>Start small:</b> one note, then two, three, four, and all five. From key to key, the hand draws a little <b>rainbow</b>: relaxed, never squeezed tight, the whole hand helping. <b>One circle is one steady beat.</b></>}</LbSay>
      <LbLive still={<>
        <LbPic h={164} gap={48} pad="6px 18px">
          <LbFig art="keys-hand-L" h={152}/>
          <LbFig art="keys-hand-R" h={152}/>
        </LbPic>
        {FW_TUNES.map(x => <LbTune key={x.icon} icon={x.icon} name={t(x.en, x.ko)} how={t(x.howEn, x.howKo)} seq={x.seq}/>)}
        <div style={{fontSize:13,color:BK.muted}}>{t('An empty dashed circle means: hold the note for one more beat.', '빈 점선 동그라미는 그 음을 한 박 더 누르고 있으라는 뜻이에요.')}</div>
      </>} live={<FingerWalks bare/>}/>
      <LbRemember>{t('A little rainbow from key to key. Relaxed: the whole hand helps.', '건반에서 건반으로 작은 무지개. 편하게, 손 전체가 도와줘요.')}</LbRemember>
    </LbPage>,
    // 7. five checks
    <LbPage key="7" no={7} chId={ch} kicker={t('Step 5', '5단계')} title={t('My five checks', '나의 다섯 가지 확인')}
      teacher={<>{t('At the start of each lesson, the student says the five checks out loud while doing them; you only correct. When all five are easy, do the Chapter check-up in the Workbook.', '레슨을 시작할 때마다 학생이 다섯 가지를 소리 내어 말하며 직접 해요. 선생님은 고쳐 주기만 해요. 다섯 가지가 다 쉬워지면 워크북의 챕터 점검을 해요.')}</>}>
      <LbSay>{t('Before you play, every time. Give yourself a star for each check in each lesson.', '칠 때마다, 치기 전에 먼저. 레슨마다 확인 하나에 별 하나씩 칠해요.')}</LbSay>
      <LbLive still={
      <div style={{display:'flex',flexDirection:'column',gap:9,flex:'1 1 auto'}}>
        <div style={{display:'grid',gridTemplateColumns:scr ? '64px 1fr repeat(6, 26px)' : '150px 1fr repeat(6, 34px)',gap:scr ? 4 : 8,alignItems:'end',fontSize:11,fontWeight:800,color:BK.muted,textAlign:'center'}}><span/><span style={{textAlign:'right',paddingRight:6}}>{t('Lesson', '레슨')}</span>{[1, 2, 3, 4, 5, 6].map(n => <span key={n}>{n}</span>)}</div>
        {checks5.map(([a, txt], i) => (
          <div key={i} style={{display:'grid',gridTemplateColumns:scr ? '64px 1fr repeat(6, 26px)' : '150px 1fr repeat(6, 34px)',gap:scr ? 4 : 8,alignItems:'center',border:'1px solid #ece6d8',borderRadius:12,padding:scr ? '4px 6px' : '4px 8px',flex:'1 1 auto'}}>
            <div style={{display:'flex',justifyContent:'center'}}><PbArt name={a} h={scr ? (a === 'chk-hand' ? 40 : 52) : a === 'chk-hand' ? 86 : 108}/></div>
            <div style={{fontSize:scr ? 13 : 15.5,fontWeight:800,color:BK.ink}}>{txt}</div>
            {[1, 2, 3, 4, 5, 6].map(n => <span key={n} style={{width:scr ? 24 : 30,height:scr ? 24 : 30,border:'1.5px solid ' + BK.line,borderRadius:8,justifySelf:'center',display:'flex',alignItems:'center',justifyContent:'center'}}><BkStarG size={14} fill="#ece6d8"/></span>)}
          </div>))}
      </div>} live={<FiveChecks376 rows={checks5}/>}/>
      <LbOnly screen><div style={{fontSize:13,color:BK.muted}}>{t('More checks, with a history: ', '더 많은 확인과 기록: ')}<a href="?tool=posture-check" style={{color:BK.coral,fontWeight:800}}>{t('the full posture check (17 points)', '전체 자세 점검 (17가지)')}</a></div></LbOnly>
      <LbRemember>{t('Check your posture before every practice.', '연습할 때마다 먼저 자세를 확인해요.')}</LbRemember>
    </LbPage>,
  ];
}
function PostureLessonBook() { return <>{postureLbPages(false)}</>; }
// the online lesson: the book's pages 2-7 as its six steps; each keeps the tick it had in the old 8-step lesson
const POSTURE_STORE = [0, 1, 3, 5, 7, 6];
function PostureHandsLearn({ onStart }) {
  const pages = postureLbPages(true);
  const opener = pages[0];
  return (
    <Lesson id="posture-hands" title={t('Posture and hand shape', '자세와 손 모양')} onStart={onStart} noArt
      head={<LbScreenCtx.Provider value={true}><BkChapterCtx.Provider value="posture-hands"><div className="lb-screen lb-open" style={{display:'flex',flexDirection:'column',gap:12,margin:'0 0 8px'}}>{opener.props.children}</div></BkChapterCtx.Provider></LbScreenCtx.Provider>}>
      {pages.slice(1).map((pg, i) => (
        <Step key={i} storeAs={POSTURE_STORE[i]} title={pg.props.kicker === t('Play', '연주') ? t('Play: ', '연주: ') + pg.props.title.charAt(0).toLowerCase() + pg.props.title.slice(1) : pg.props.title}>
          <LbScreenPage page={pg}/>
        </Step>
      ))}
    </Lesson>
  );
}
