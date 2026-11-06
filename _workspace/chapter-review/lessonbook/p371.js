// ── Phase 371: the app's chapter 1 follows the Lesson Book (words, order, pictures) ──
// 1. The step texts say what the book says.
repIn('ExplPostureHands1', `{tip(t('Sitting', '앉는 법'), t('Sit on the front half of the stool, feet flat, facing middle C. Stool height: forearm level with the keys. Distance: elbows just in front of the body, open a little to the side.', '의자 앞쪽 절반에 앉고, 발은 바닥에 평평하게, 가운데 도(C)를 마주보게 앉아요. 의자 높이: 팔뚝이 건반과 수평이 되도록. 거리: 팔꿈치가 몸 바로 앞에, 옆으로 살짝 벌어지게.'))}`,
  `{tip(t('Sitting', '앉는 법'), t('Sit on the front half of the stool, feet flat, facing middle C, leaning a little toward the piano. Stool height: forearm level with the keys. Distance: elbows just in front of you and away from your body, about a fist from your sides.', '의자 앞쪽 절반에 앉고, 발은 바닥에 평평하게, 가운데 도(C)를 마주보며 피아노 쪽으로 살짝 기울여 앉아요. 의자 높이: 팔뚝이 건반과 수평이 되도록. 거리: 팔꿈치는 몸 바로 앞에, 몸에서 떨어지게 -- 옆구리에서 주먹 하나만큼.'))}`, '371 expl 1');
repIn('ExplPostureHands2', `{tip(t('The arm carries the hand', '팔이 손을 데려가요'), t('Fingers play the keys, but the arm takes the hand where it needs to go -- the hand keeps its shape all the way. Do these a few minutes at the start of every practice.', '손가락이 건반을 누르지만, 손을 필요한 곳으로 데려가는 건 팔이에요 -- 손 모양은 계속 그대로 유지돼요. 연습을 시작할 때마다 몇 분씩 이 동작들을 해보세요.'))}`,
  `{tip(t('The arm carries the hand', '팔이 손을 데려가요'), t('Your fingertips stay connected to the piano, but the whole arm does the work: from above, it leads the hand and the fingers, with the elbows free and away from your body. Even while a finger presses a key, the whole arm stays free. Do the six moves in order, from the big parts of the body to the small, a few minutes at the start of every practice.', '손끝은 늘 피아노와 이어져 있지만, 일은 팔 전체가 해요: 위에서 손과 손가락을 이끌고, 팔꿈치는 몸에서 떨어져 자유로워요. 손가락이 건반을 누르는 동안에도 팔 전체는 자유로워요. 여섯 가지 동작을 큰 몸 부분부터 작은 부분 순서로, 연습을 시작할 때마다 몇 분씩 해요.'))}`, '371 expl 2');
repIn('ExplPostureHands3', `{tip(t('A round hand', '둥근 손'), t('Let your arms hang, then lift your hands as if holding a small ball. Knuckles up like a bridge, wrist level with the forearm, play on the fingertip pads, the thumb on its side.', '팔을 편하게 늘어뜨렸다가, 작은 공을 쥐듯이 손을 들어올려요. 손가락 마디는 다리처럼 위로, 손목은 팔뚝과 수평으로, 손가락 끝 살로 연주하고, 엄지손가락은 옆면으로.'))}`,
  `{tip(t('A round hand', '둥근 손'), t('Let your arms hang, then lift your hands as if holding a small ball. Knuckles up like a bridge, and play on the fingertips. The wrist stays free: with the fingertip on the key, the hand can sway up and down and side to side, as if a roller sat under your forearm. Keep an eye on the knuckles and the tips.', '팔을 편하게 늘어뜨렸다가, 작은 공을 쥐듯이 손을 들어올려요. 손가락 마디는 다리처럼 위로, 손끝으로 쳐요. 손목은 자유롭게: 손끝을 건반에 댄 채로, 팔 아래 롤러가 있는 것처럼 손이 위아래, 좌우로 흔들려요. 마디와 손끝이 무너지지 않는지 살펴봐요.'))}
        <div style={{display:'flex',alignItems:'center',justifyContent:'center',gap:12,flexWrap:'wrap',margin:'2px 0 8px'}}>
          <PbArt name="hand-thumb" h={118}/>
          <div style={{fontSize:13.5,lineHeight:1.45,maxWidth:230}}><b>{t('The thumb', '엄지')}</b>: {t('it bends in and plays on the side of its tip, like a tipped boat.', '안으로 꺾여서 손끝 옆면으로 쳐요. 옆으로 누운 배처럼.')}</div>
        </div>`, '371 expl 3');
repIn('ExplPostureHands3', `  const tip = (title, body) => <Rule title={title}>{body}</Rule>;`, `  const tip = (title, body) => <Rule title={title}>{body}</Rule>;`, '371 expl 3 check');

// 2. The six warm-ups in the book's order and words: rag doll, elbow wings, arm glide, arm drop, knuckle bridge, wrist balloon
{
  const i = s.indexOf('const ARM_EXERCISES = ['), j = s.indexOf('\n];', i) + 3;
  if (i < 0 || j < 3) throw new Error('371 ARM_EXERCISES');
  const old = s.slice(i, j);
  const bridgeStart = old.indexOf("  { id: 'bridge'"), bridgeEnd = old.indexOf("  { id: 'glide'");
  let bridge = old.slice(bridgeStart, bridgeEnd).trimEnd().replace(/,$/, '');
  const b1 = "'All five fingertips resting ON the keys (C D E F G) -- they never leave the key surface.'";
  if (bridge.split(b1).length !== 2) throw new Error('371 bridge text');
  bridge = bridge.replace(b1, "'Check the bridge: your knuckles are a bridge a little car can drive over. All five fingertips rest ON the keys (C D E F G).'")
    .replace('"다섯 손끝을 모두 건반(C D E F G) \\"위에\\" 올려 둬요 -- 건반 표면에서 떨어지지 않아요."', '"다리를 확인해요: 손가락 마디는 작은 자동차가 지나갈 수 있는 다리예요. 다섯 손끝을 모두 건반(C D E F G) 위에 올려 둬요."');
  if (bridge.indexOf('다리를 확인해요') < 0) throw new Error('371 bridge ko');
  s = s.slice(0, i) + `const ARM_EXERCISES = [ // Phase 371: the Lesson Book's order -- from the big parts of the body to the small
  { id: 'ragdoll', title: 'Rag doll', ko: '헝겊 인형', C: ExRagDoll, ms: 4200, reps: 3,
    how: ['Flop forward and let both arms hang heavy.', 'Shake them loose from the shoulders.', 'Float the hands up and set them gently on the keys.'],
    howKo: ['앞으로 축 늘어지며 두 팔을 무겁게 늘어뜨려요.', '어깨부터 털어서 힘을 빼요.', '손을 둥실 올려서 건반 위에 살포시 내려놓아요.'],
    watch: 'Shoulders stay down when the arms come up.', watchKo: '팔이 올라올 때도 어깨는 내려가 있어요.' },
  { id: 'wings', title: 'Elbow wings', ko: '팔꿈치 날개', C: ExWings, ms: 3000, reps: 5,
    how: ['Hands resting on the keys.', 'Check the elbows are free, not stuck to your body: let them float out like wings, then back.', 'Stop in the middle -- about a fist from your body.'],
    howKo: ['손은 건반 위에 올려 둬요.', '팔꿈치가 몸에 붙지 않고 자유로운지 확인해요: 날개처럼 옆으로 띄웠다가 돌아와요.', '가운데에서 멈춰요 -- 몸에서 주먹 하나만큼.'],
    watch: 'The hands stay still on the keys while the elbows move.', watchKo: '팔꿈치가 움직이는 동안 손은 건반 위에 가만히 있어요.' },
  { id: 'glide', title: 'Arm glide', ko: '팔 미끄럼', C: ExGlide, ms: 5200, reps: 3,
    how: ['Put the hand shape on middle C.', 'Now the whole arm: skate along the keys to the next C, and the next. The fingers ride, they don’t walk.', 'Come back down. The elbow moves first and opens out.'],
    howKo: ['손 모양을 가운데 도에 올려요.', '이제 팔 전체로: 건반 위를 미끄러지듯 다음 C로, 또 그다음 C로. 손가락은 타고 갈 뿐, 걸어가지 않아요.', '다시 내려와요. 팔꿈치가 먼저 움직이며 바깥으로 열려요.'],
    watch: 'The hand looks exactly the same at every C.', watchKo: '어느 C에서나 손 모양이 똑같아요.' },
  { id: 'drop', title: 'Arm drop', ko: '팔 떨어뜨리기', C: ExDrop, ms: 2400, reps: 5,
    how: ['Hand in the good shape, finger 3 ready.', 'Lift the whole arm (the hand keeps its shape).', 'Let it drop into the key: firm tip, soft wrist, a round sound.'],
    howKo: ['좋은 손 모양으로, 3번 손가락 준비.', '팔 전체를 들어 올려요(손 모양은 그대로).', '건반 속으로 떨어뜨려요: 단단한 손끝, 부드러운 손목, 둥근 소리.'],
    watch: 'A full, round sound -- no knocking. Notice the tip joint.', watchKo: '꽉 찬 둥근 소리 -- 두드리지 않아요. 손끝 관절을 살펴봐요.' },
${bridge},
  { id: 'balloon', title: 'Wrist balloon', ko: '손목 풍선', C: ExBalloon, ms: 3200, reps: 5,
    how: ['Play a key with a round hand.', 'As the key goes down, a balloon lifts the wrist straight back up to level.', 'The fingertip stays on the key the whole time.'],
    howKo: ['둥근 손으로 건반 하나를 쳐요.', '건반이 내려가는 순간, 풍선이 손목을 같은 높이로 다시 끌어올려요.', '손끝은 내내 건반 위에 있어요.'],
    watch: 'The wrist never sinks below the keys.', watchKo: '손목은 절대 건반 아래로 처지지 않아요.' },
];` + s.slice(j);
}
repIn('ArmExercises', `const [open, setOpen] = useState('glide');`, `const [open, setOpen] = useState('ragdoll');`, '371 first exercise');
repIn('ArmExercises', `<div style={actNote}>{LANG === 'ko' ? <>손은 모양을 지키고, <b>팔</b>이 손을 움직여요. 짧은 운동 여섯 가지 -- 그림을 보고 따라 한 뒤, 할 때마다 +1을 눌러요.</> : <>The hand holds its shape; the <b>arm</b> moves it. Six short exercises -- watch the picture, do it, then tap +1 for each time.</>}</div>`,
  `<div style={actNote}>{LANG === 'ko' ? <>손은 모양을 지키고, <b>팔</b>이 손을 움직여요. 여섯 가지 동작을 <b>이 순서대로</b>, 큰 몸 부분부터 작은 부분으로 -- 앞 동작이 다음 동작을 준비해요. 그림을 보고 따라 한 뒤, 할 때마다 +1을 눌러요.</> : <>The hand holds its shape; the <b>arm</b> moves it. Six moves <b>in this order</b>, from the big parts of the body to the small: each one gets the arm ready for the next. Watch the picture, do it, then tap +1 for each time.</>}</div>`, '371 arm note');
repIn('ArmExercises', `<div style={{background:'#fff',borderRadius:10,padding:'6px 4px'}}><Anim u={u}/></div>`,
  `<div style={{display:'flex',justifyContent:'center',background:'#fff',borderRadius:10,padding:'8px 4px 4px'}}><PbArt name={ex.id === 'drop' ? 'dive' : ex.id} h={136} style={{maxWidth:'100%'}}/></div>
      <div style={{fontSize:11.5,fontWeight:800,color:'var(--muted)',margin:'6px 0 2px'}}>{t('Watch it move', '움직임 보기')}</div>
      <div style={{background:'#fff',borderRadius:10,padding:'6px 4px'}}><Anim u={u}/></div>`, '371 book picture');
rep(`get fix() { return t('Play slowly on the tip, press the key down and hold -- the tip joint stays firm like a little pillar.', '손끝으로 천천히, 건반을 끝까지 누르고 기다려요 -- 손끝 관절은 작은 기둥처럼 단단하게.'); }`,
  `get fix() { return t('Notice the tip joint: play slowly on the tip, press the key down and hold, and feel it stay firm like a little pillar.', '손끝 관절을 살펴봐요: 손끝으로 천천히, 건반을 끝까지 누르고 기다리며, 작은 기둥처럼 단단한지 느껴 봐요.'); }`, '371 nail fix');
rep(`'arm-moves': ['팔 전체로 움직이기', '횟수를 세어 주는 준비 운동 여섯 가지.'],`, `'arm-moves': ['팔 전체로 움직이기', '큰 몸 부분부터 작은 부분까지, 순서대로 하는 준비 운동 여섯 가지.'],`, '371 tool ko');
rep(`blurb: 'Six warm-up exercises with a rep counter.'`, `blurb: 'Six warm-ups in order, from the big parts of the body to the small.'`, '371 tool en');

// 3. Play: finger walks (the book's page 6) as a new lesson step; the Posture check keeps its tick (storeAs)
rep('function PostureHandsLearn({ onStart }) {', read('fw371.jsx') + '\nfunction PostureHandsLearn({ onStart }) {', '371 finger walks code');
repIn('PostureHandsLearn', `      <Step title={t('Posture check', '자세 점검')}>
        <PostureChecklist/>
      </Step>`, `      <Step title={t('Play: finger walks', '연주: 손가락 걷기')} storeAs={7}>
        <FingerWalks/>
      </Step>
      <Step title={t('Posture check', '자세 점검')} storeAs={6}>
        <PostureChecklist/>
      </Step>`, '371 steps');
repIn('PostureWorkbook', `<WbMap id="posture-hands" concepts={C} steps={7}`, `<WbMap id="posture-hands" concepts={C} steps={8}`, '371 workbook map');

// 4. The posture check opens with the book's five checks (same ids, so saved marks and history stay)
{
  const i = s.indexOf('const POSTURE_LIST = ['), j = s.indexOf('\n];', i) + 3;
  if (i < 0 || j < 3) throw new Error('371 POSTURE_LIST');
  s = s.slice(0, i) + `const POSTURE_LIST = [ // Phase 371: the Lesson Book's five checks first
  { g: 'My five checks', items: [
    ['front', 'Front half of the stool', 'sit-check', 'Sit forward so the feet can take some weight'],
    ['feet', 'Feet flat (or on a footstool), leaning a little toward the piano', 'sit-check', 'A footstool or books under the feet; lean a little forward'],
    ['back', 'Sit tall, like a puppet on a string', 'arm-moves', 'Rag doll: hang, shake, then sit tall and float up'],
    ['forearm', 'Forearm level with the keys, elbows away from your body', 'sit-check', 'Set up the stool: stool height, then Elbow wings'],
    ['tips', 'Round hand, play on the tips', 'hand-shape', 'The hand shape: find the tip'],
  ] },
  { g: 'Sitting', items: [
    ['stool', 'Stool height: forearm level with the keys', 'sit-check', 'Set up the stool: raise or lower until the forearm is level'],
    ['dist', 'Distance: elbows just in front of the body', 'sit-check', 'Set up the stool: move it until the elbows are just in front'],
    ['shoulders', 'Shoulders down and loose', 'arm-moves', 'Rag doll -- the shoulders stay down as the arms come up'],
  ] },
  { g: 'Arms', items: [
    ['elbows', 'Elbows free -- a fist’s width from the body, never stuck to it', 'arm-moves', 'Elbow wings (and the Front view in Set up the stool)'],
    ['wrist', 'Wrist back up to level after each key -- it never sinks', 'arm-moves', 'Wrist balloon'],
  ] },
  { g: 'Hands', items: [
    ['knuckles', 'Knuckles up -- a bridge', 'arm-moves', 'Knuckle bridge: press into the key and hold'],
    ['curve', 'Fingers curved (holding a ball)', 'hand-shape', 'The hand shape: compare “Flat fingers” with the good shape'],
    ['nail', 'Notice the tip joint: try not to let it cave in', 'arm-moves', 'Arm drop onto a firm fingertip'],
    ['thumb', 'Thumb bends in and plays on the side of its tip', 'hand-shape', 'The thumb: on its side, like a tipped boat'],
  ] },
  { g: 'Moving', items: [
    ['carry', 'The arm carries the hand along the keys', 'arm-moves', 'Arm glide'],
    ['keep', 'The hand keeps its shape while moving', 'arm-moves', 'Arm glide -- the hand looks the same at every C'],
    ['loose', 'The whole arm stays free, even while a finger presses', 'arm-moves', 'Rag doll, then Arm drop'],
  ] },
];` + s.slice(j);
}
rep(`const POSTURE_G_KO = { Sitting: '앉기', Arms: '팔', Hands: '손', Moving: '움직임' };`, `const POSTURE_G_KO = { 'My five checks': '나의 다섯 가지 확인', Sitting: '앉기', Arms: '팔', Hands: '손', Moving: '움직임' };`, '371 group ko');
for (const [id, oldKo, newKo] of [
  ['front', "front: ['의자 앞쪽 절반에 앉기', '앞으로 당겨 앉아서 발이 몸무게를 조금 받치게 해요'],", "front: ['의자 앞쪽 절반에 앉기', '앞으로 당겨 앉아서 발이 몸무게를 조금 받치게 해요'],"],
  ['feet', "feet: ['발은 평평하게 (또는 발판 위에)', '발밑에 발판이나 책을 두어요'],", "feet: ['발은 평평하게 (또는 발판 위에), 피아노 쪽으로 살짝 기울여요', '발밑에 발판이나 책을 두고, 살짝 앞으로 기울여요'],"],
  ['back', "back: ['허리는 곧게, 살짝 앞으로', '헝겊 인형: 늘어뜨리고, 털고, 곧게 앉아 둥실 올려요'],", "back: ['줄에 매달린 인형처럼 곧게 앉기', '헝겊 인형: 늘어뜨리고, 털고, 곧게 앉아 둥실 올려요'],"],
  ['forearm', "forearm: ['아래팔은 수평, 위아래로 기울지 않게', '의자 맞추기: 의자 높이'],", "forearm: ['팔뚝은 건반과 수평, 팔꿈치는 몸에서 띄워요', '의자 맞추기: 의자 높이, 그다음 팔꿈치 날개'],"],
  ['tips', "tips: ['손끝 살로 치기', '손 모양: 손끝을 찾아요'],", "tips: ['둥근 손으로 손끝으로 치기', '손 모양: 손끝을 찾아요'],"],
  ['elbows', "elbows: ['팔꿈치는 열고 -- 몸에서 주먹 하나', '팔꿈치 날개 (그리고 의자 맞추기의 \"앞에서\" 보기)'],", "elbows: ['팔꿈치는 자유롭게 -- 몸에서 주먹 하나, 몸에 붙이지 않기', '팔꿈치 날개 (그리고 의자 맞추기의 \"앞에서\" 보기)'],"],
  ['wrist', "wrist: ['손목은 아래팔과 수평 (처지지도, 솟지도 않게)', '손목 풍선'],", "wrist: ['건반을 칠 때마다 손목은 같은 높이로 다시 -- 처지지 않게', '손목 풍선'],"],
  ['nail', "nail: ['손끝 관절은 단단하게, 꺾이지 않게', '단단한 손끝으로 팔 떨어뜨리기'],", "nail: ['손끝 관절을 살펴봐요: 무너지지 않게', '단단한 손끝으로 팔 떨어뜨리기'],"],
  ['thumb', "thumb: ['엄지는 옆면 모서리로', '엄지는 옆으로, 손톱 모서리 근처로'],", "thumb: ['엄지는 안으로 꺾여서 손끝 옆면으로', '엄지: 옆으로 누운 배처럼'],"],
  ['loose', "loose: ['긴장 없이 -- 팔이 자유롭게 흔들릴 수 있게', '헝겊 인형, 그다음 팔 떨어뜨리기'],", "loose: ['손가락이 누르는 동안에도 팔 전체는 자유롭게', '헝겊 인형, 그다음 팔 떨어뜨리기'],"],
]) rep('  ' + oldKo, '  ' + newKo, '371 ko ' + id);

// 5. The moving pictures of chapter 1 (stool, front arms, hand from the side, warm-up animations, arm weight) in the
//    book's two inks: paper and navy instead of skin tones and periwinkle (same shapes, same motion).
{
  const i = s.indexOf("const POS_SKIN = '#f8e6dc', POS_SKIN_EDGE = '#d9a27a'");
  const a = s.indexOf('function ArmAlignment()'), j = s.indexOf('\nfunction ', a + 10);
  if (i < 0 || a < 0 || j < 0 || a < i) throw new Error('371 recolour range');
  let mid = s.slice(i, j);
  const counts = {};
  for (const [from, to] of [["const POS_SKIN = '#f8e6dc', POS_SKIN_EDGE = '#d9a27a'", "const POS_SKIN = '#fffdf7', POS_SKIN_EDGE = '#26296b'"], ['#7e86c0', '#26296b'], ['#5d6f86', '#26296b'], ['#6b5a4a', '#26296b']]) {
    counts[from] = mid.split(from).length - 1; mid = mid.split(from).join(to);
  }
  if (counts['#7e86c0'] !== 10 || counts['#5d6f86'] !== 2 || counts['#6b5a4a'] !== 1) throw new Error('371 recolour counts ' + JSON.stringify(counts));
  s = s.slice(0, i) + mid + s.slice(j);
}
