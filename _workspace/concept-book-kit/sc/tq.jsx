// ─── Technique on the Home (her order 2026-10-24: Pitch gaps, Rhythm, then Technique). Same lesson engine; the pictures
// and words are the Lesson Book's own (posture-hands: puppet on a string, wet spaghetti, holding a ball, a tipped boat,
// mirror twins), its six warm-ups (ARM_EXERCISES) and its five checks. Positions sit where the Reading steps and the
// five-finger tool already put them (SSK_POS, FF_ROOTS). Scale fingering stays in Pitch > Scales (her answer 07:22):
// 'Playing scales and chords' on the Home links to those lessons instead of copying them.
const tqArt = (name, h = 150, lit) => <div style={{ display: 'flex', justifyContent: 'center', margin: '4px 0 6px' }}><PbArt name={name} h={h} lit={lit} style={{ maxWidth: '100%' }}/></div>;
const tqRow = (items, h = 90) => <div style={{ display: 'grid', gridTemplateColumns: 'repeat(' + items.length + ', minmax(0, 1fr))', gap: 6, alignItems: 'end', margin: '4px 0 6px' }}>{items.map(([name, cap], i) => <div key={i} style={{ textAlign: 'center', minWidth: 0 }}><PbArt name={name} h={h} style={{ maxWidth: '100%' }}/><div style={{ fontSize: 12.5, fontWeight: 800, color: KQ.NV, marginTop: 2, lineHeight: 1.25, wordBreak: 'keep-all', textWrap: 'balance' }}>{kqT(cap)}</div></div>)}</div>;
// pictures down the screen, each with its words beside it
const tqList = (items, h) => <div style={{ display: 'flex', flexDirection: 'column', gap: 10, maxWidth: 380, margin: '4px auto 6px' }}>{items.map(([name, cap], i) => <div key={i} style={{ display: 'flex', alignItems: 'center', gap: 12 }}><span style={{ flex: '0 0 46%', display: 'flex', justifyContent: 'center' }}><PbArt name={name} h={h} style={{ maxWidth: '100%' }}/></span><span style={{ flex: 1, minWidth: 0, fontSize: 14.5, fontWeight: 800, color: KQ.NV, lineHeight: 1.3, wordBreak: 'keep-all' }}>{kqT(cap)}</span></div>)}</div>;
// the five finger numbers in the hand's own order (left 5 4 3 2 1, right 1 2 3 4 5), one lit
const tqFingers = (h, lit) => <div style={{ display: 'flex', justifyContent: 'center', gap: 6, margin: '0 0 6px' }}>{(h === 'L' ? [5, 4, 3, 2, 1] : [1, 2, 3, 4, 5]).map(f => { const on = String(f) === String(lit);
  return <span key={f} style={{ width: 32, height: 32, borderRadius: 16, border: '1.6px solid ' + (on ? KQ.CO : KQ.NV), background: on ? KQ.CO : '#fff', color: on ? '#fff' : KQ.NV, display: 'flex', alignItems: 'center', justifyContent: 'center', fontWeight: 900, fontSize: 16 }}>{f}</span>; })}</div>;
// the Korean words of the Lesson Book: 마디 (the posture drill's list says 너클)
const tqKo = (x) => x.replace(/너클이/g, '마디가').replace(/너클을/g, '마디를').replace(/너클/g, '마디');
const tqArtOf = (id) => id === 'drop' ? 'dive' : id;
// one warm-up: the movement, then the rest of its steps and what to watch for (its first step is the screen's line)
function TqEx({ id }) {
  const ex = ARM_EXERCISES.find(x => x.id === id), u = useLoop(ex.ms || 3000, !!ex.C), A = ex.C, how = LANG === 'ko' ? ex.howKo : ex.how;
  return <div style={{ margin: '0 0 6px' }}>
    {A ? <div style={{ maxWidth: 360, margin: '0 auto' }}><A u={u}/></div> : tqArt(tqArtOf(id), 120)}
    <ol start={2} style={{ margin: '8px auto 4px', paddingLeft: 22, fontSize: 14, lineHeight: 1.5, maxWidth: 420, color: KQ.NV }}>{how.slice(1).map((h, i) => <li key={i}>{h}</li>)}</ol>
    <div style={{ fontSize: 13.5, maxWidth: 420, margin: '0 auto', color: KQ.NV, lineHeight: 1.45 }}><b style={{ color: KQ.COD }}>{t('Watch for: ', '살펴볼 점: ')}</b>{t(ex.watch, ex.watchKo)}</div>
  </div>;
}
const TQ_SPEC = {};
// a picture to judge, the answers from the posture drill's own list (an odd count: the first, 'just right', across the whole row)
const tqPickQ = (list, art, prompt, prev, h) => { let item, g = 0; do { item = kqPick(list); } while (prev && prev.key === item.id && g++ < 10);
  const ko = tqKo(item.ko), wk = tqKo(item.why[1]), say = [item.en + '. ' + item.why[0], wk.startsWith(ko) ? wk : ko + '. ' + wk];
  return { key: item.id, kind: 'choice', cols: 2, prompt, opts: list.map((x, i) => ({ id: x.id, span: i === 0 && list.length % 2 === 1, label: () => t(x.en, tqKo(x.ko)) })), ans: item.id, ok: (v) => v === item.id,
    fig: () => ({ mid: tqArt(art + item.id, h) }), yes: say, no: say }; };

// ══ 1. Posture and hands ══
TQ_SPEC['kp-sit'] = {
  title: ['Sit at the piano', '피아노 앞에 앉기'], allLine: ['Front half of the stool, feet flat, sit tall, leaning a little forward.', '의자 앞쪽 절반, 발은 평평하게, 곧게 앉아 앞으로 살짝 기울여요.'],
  fig: () => ({ mid: tqArt('sit', 190) }),
  steps: [
    { title: ['Front half of the stool', '의자 앞쪽 절반에 앉기'], line: ['Sit forward, so the feet can take some weight.', '앞쪽에 앉아요. 발이 몸무게를 조금 받쳐 줄 수 있게요.'], fig: () => ({ mid: tqArt('chk-front', 140) }) },
    { title: ['Feet flat', '발은 평평하게'], line: ['Feet flat, leaning a little toward the piano. Feet dangling? A footstool or a sturdy box fixes it.', '발은 평평하게, 피아노 쪽으로 살짝 기울여요. 발이 대롱대롱하면 발판이나 튼튼한 상자를 놓아요.'], fig: () => ({ mid: tqArt('chk-feet', 140) }) },
    { title: ['Sit tall', '곧게 앉기'], line: ['Sit tall, like a puppet on a string.', '줄에 매달린 인형처럼 곧게 앉아요.'], fig: () => ({ mid: tqArt('puppet', 180) }) },
    { title: ['Forearm level', '팔뚝은 수평'], line: ['Stool height: the forearm level with the keys. Distance: elbows just in front of the body, away from your sides.', '의자 높이: 팔뚝이 건반과 수평이 되도록. 거리: 팔꿈치는 몸 바로 앞에, 옆구리에서 떨어지게.'], fig: () => ({ mid: tqArt('chk-forearm', 140) }) },
    { title: ['Not like this', '이렇게는 아니에요'], line: ['Three ways it goes wrong. Spot them on yourself.', '이렇게 되기 쉬워요. 내 모습에서 찾아봐요.'], fig: () => ({ mid: tqList([['not-sofa', ['Leaning back, like on a sofa', '소파처럼 뒤로 기대기']], ['not-close', ['So close the elbows squash in', '너무 가까워서 팔꿈치가 눌려요']], ['not-swing', ['Too high: feet swinging', '너무 높아서 발이 대롱대롱']]], 100) }) },
  ],
  make: (n, prev) => tqPickQ(POSTURE_SIT, 'q-sit-', ['Is this stool set up right?', '이 의자 자리가 알맞나요?'], prev, 210),
};
// yes or no about the arm (the Workbook's statements); the picture is the warm-up that checks it
const TQ_ARM = [
  ['The arm leads from above.', '팔이 위에서 이끌어요.', true, 'dive', ['The hand keeps its shape; the arm moves it.', '손은 모양을 지키고, 팔이 손을 움직여요.']],
  ['My elbows stay stuck to my body.', '팔꿈치가 몸에 꼭 붙어 있어요.', false, 'wings', ['The elbows stay free, about a fist from your body: Elbow wings.', '팔꿈치는 몸에서 주먹 하나만큼 떨어져 자유로워요. 팔꿈치 날개처럼요.']],
  ['Even while a finger presses a key, the whole arm stays free.', '손가락이 건반을 누를 때도 팔 전체는 자유로워요.', true, 'bridge', ['The arm’s weight sinks through the knuckle into the fingertip: Knuckle bridge.', '팔의 무게가 마디를 지나 손끝으로 가라앉아요. 마디 다리처럼요.']],
  ['After a key goes down, my wrist sinks below the keys.', '건반을 누르고 나면 손목이 건반 아래로 처져요.', false, 'balloon', ['The wrist never sinks: a balloon lifts it back up to level.', '손목은 가라앉지 않아요. 풍선이 같은 높이로 다시 들어 올려요.']],
  ['Rag doll comes first: big parts of the body before small ones.', '헝겊 인형이 먼저예요. 큰 몸 부분부터 작은 부분으로.', true, 'ragdoll', ['The six warm-ups go from the big parts of the body to the small: each one gets the arm ready for the next.', '준비 운동 여섯 가지는 큰 몸 부분부터 작은 부분으로 가요. 앞 동작이 다음 동작을 준비해요.']],
  ['I squeeze hard to play loud.', '세게 치려고 손을 꽉 쥐어요.', false, 'dive', ['No squeezing: let the arm’s weight drop into the key, as in Arm drop.', '꽉 쥐지 않아요. 팔 떨어뜨리기처럼 팔의 무게를 건반 속으로 떨어뜨려요.']],
];
TQ_SPEC['kp-arm'] = {
  title: ['Let the arm carry the hand', '팔이 손을 데려가요'], allLine: ['The arm leads from above, elbows free. Arms heavy, like wet spaghetti. Six warm-ups in this order, from the big parts of the body to the small.', '팔이 위에서 이끌고, 팔꿈치는 자유롭게. 팔은 젖은 스파게티처럼 무겁게. 준비 운동 여섯 가지를 이 순서대로, 큰 몸 부분부터 작은 부분으로.'],
  fig: () => ({ mid: <>{tqRow(ARM_EXERCISES.slice(0, 3).map((x, i) => [tqArtOf(x.id), [(i + 1) + '. ' + x.title, (i + 1) + '. ' + x.ko]]), 76)}{tqRow(ARM_EXERCISES.slice(3).map((x, i) => [tqArtOf(x.id), [(i + 4) + '. ' + x.title, (i + 4) + '. ' + x.ko]]), 76)}</> }),
  steps: ARM_EXERCISES.map((x, i) => ({ title: [(i + 1) + '. ' + x.title, (i + 1) + '. ' + x.ko], line: [x.how[0], x.howKo[0]], fig: () => ({ mid: <TqEx id={x.id}/> }) })),
  make: (n, prev) => { let i, g = 0; do { i = kqRnd(TQ_ARM.length); } while (prev && prev.i === i && g++ < 8); const [en, ko, ok, art, fix] = TQ_ARM[i], ans = ok ? 'y' : 'n';
    return { i, kind: 'choice', cols: 2, prompt: ['“' + en + '” Is that how it should be?', '“' + ko + '” 이렇게 하는 게 맞을까요?'], opts: [{ id: 'y', label: () => t('Yes', '네') }, { id: 'n', label: () => t('No', '아니요') }], ans, ok: (v) => v === ans, fig: () => ({ mid: tqArt(art, 120) }),
      yes: ok ? ['Yes. ' + fix[0], '맞아요. ' + fix[1]] : ['Right, not like that. ' + fix[0], '맞아요, 그렇게 하지 않아요. ' + fix[1]], no: ok ? ['It is how it should be. ' + fix[0], '그렇게 하는 게 맞아요. ' + fix[1]] : ['Not like that. ' + fix[0], '그렇게 하지 않아요. ' + fix[1]] }; },
};
TQ_SPEC['kp-hand'] = {
  title: ['A round hand', '둥근 손'], allLine: ['Round, like holding a ball. The knuckles make a bridge, the wrist is level, and each finger plays on its tip.', '공을 쥔 것처럼 둥글게. 마디는 다리처럼 서고, 손목은 수평, 손가락은 손끝으로 쳐요.'],
  fig: () => ({ mid: tqArt('hand-good', 150) }),
  steps: [
    { title: ['Round, like holding a ball', '공을 쥔 것처럼 둥글게'], line: ['Hold a small ball, then keep that round shape on the keys. Play on the tips.', '작은 공을 쥔 듯한 둥근 모양을 건반에 그대로 올려요. 손끝으로 쳐요.'], fig: () => ({ mid: tqArt('hand-good', 150) }) },
    { title: ['The knuckle bridge', '마디 다리'], line: ['Your knuckles are a bridge a little car can drive over. Press one key slowly and hold for 3: the bridge stays up.', '손가락 마디는 작은 자동차가 지나가는 다리예요. 건반 하나를 천천히 누르고 셋을 세요. 다리는 그대로예요.'], fig: () => ({ mid: tqArt('bridge', 140) }) },
    { title: ['The thumb: a tipped boat', '엄지: 옆으로 누운 배'], line: ['The thumb bends in and plays on the side of its tip, like a tipped boat.', '엄지는 안으로 꺾여 손끝 옆면으로 쳐요. 옆으로 누운 배처럼.'], fig: () => ({ mid: tqArt('hand-thumb', 140) }) },
    { title: ['Faults to notice', '알아차릴 모양'], line: ['A free wrist, as if on a roller. Watch the knuckles and fingertips.', '롤러 위처럼 자유로운 손목. 마디와 손끝을 살펴봐요.'], fig: () => ({ mid: tqList([['hand-flat', ['Flat fingers', '납작한 손가락']], ['hand-cave', ['Tip joint caving in', '손끝 관절이 꺾여요']], ['hand-high', ['Wrist stiff and high', '손목이 굳고 높아요']]], 72) }) },
  ],
  make: (n, prev) => tqPickQ(POSTURE_HAND, 'q-hand-', ['What is wrong with this hand shape? Or is it just right?', '이 손 모양은 무엇이 문제일까요? 아니면 딱 좋은가요?'], prev, 140),
};
const TQ_CHECKS = [['chk-front', ['Front half of the stool', '의자 앞쪽 절반에 앉기']], ['chk-feet', ['Feet flat, leaning a little toward the piano', '발은 평평하게, 피아노 쪽으로 살짝 기울여요']], ['chk-tall', ['Sit tall, like a puppet on a string', '줄에 매달린 인형처럼 곧게 앉기']], ['chk-forearm', ['Forearm level with the keys, elbows away from your body', '팔뚝은 건반과 수평, 팔꿈치는 몸에서 띄워요']], ['chk-hand', ['Round hand, play on the tips', '둥근 손으로 손끝으로 치기']]];
TQ_SPEC['kp-check'] = {
  title: ['My five checks', '나의 다섯 가지 확인'], allLine: ['Every time, before you play, do the five checks and say them out loud.', '칠 때마다, 치기 전에 다섯 가지를 확인하며 소리 내어 말해요.'],
  fig: () => ({ mid: <div style={{ display: 'flex', flexDirection: 'column', gap: 6, maxWidth: 420, margin: '0 auto 6px' }}>{TQ_CHECKS.map(([a, w], i) => <div key={a} style={{ display: 'flex', alignItems: 'center', gap: 10 }}><span style={{ flex: '0 0 64px', display: 'flex', justifyContent: 'center' }}><PbArt name={a} h={a === 'chk-hand' ? 36 : 50}/></span><span style={{ fontSize: 14.5, fontWeight: 800, color: KQ.NV, minWidth: 0 }}>{(i + 1) + '. ' + kqT(w)}</span></div>)}</div> }),
  steps: TQ_CHECKS.map(([a, w], i) => ({ title: ['Check ' + (i + 1), (i + 1) + '번 확인'], line: w, fig: () => ({ mid: tqArt(a, a === 'chk-hand' ? 90 : 140) }) })),
  make: (n, prev) => { let i, g = 0; do { i = kqRnd(5); } while (prev && prev.i === i && g++ < 8); const [a, w] = TQ_CHECKS[i];
    return { i, kind: 'choice', cols: 1, prompt: ['Which check does this picture show?', '이 그림은 어떤 확인일까요?'], opts: TQ_CHECKS.map(([x, ww], j) => ({ id: x, label: () => (j + 1) + '. ' + kqT(ww) })), ans: a, ok: (v) => v === a, fig: () => ({ mid: tqArt(a, a === 'chk-hand' ? 76 : 120) }),
      yes: ['Check ' + (i + 1) + ': ' + w[0] + '.', (i + 1) + '번 확인: ' + w[1] + '.'], no: ['This is check ' + (i + 1) + ': ' + w[0] + '.', '이건 ' + (i + 1) + '번 확인이에요. ' + w[1] + '.'] }; },
};

// ══ 2. Finger numbers and positions ══
TQ_SPEC['kp-fingers'] = {
  title: ['Finger numbers', '손가락 번호'], allLine: ['Fingers are numbered 1 to 5 from the thumb, on both hands. Thumbs are always 1: your hands are mirror twins.', '양손 모두, 엄지부터 1번에서 5번까지. 엄지는 언제나 1번. 두 손은 거울 쌍둥이예요.'],
  fig: () => ({ mid: tqArt('mirror', 160) }),
  steps: [
    { title: ['Right hand', '오른손'], line: ['Count from the thumb: 1 2 3 4 5.', '엄지부터 세요: 1 2 3 4 5.'], fig: (c) => { const f = 1 + Math.floor(c.tk / 2) % 5; return { mid: <>{tqArt('q-fingers-R', 170, String(f))}{tqFingers('R', f)}</> }; } },
    { title: ['Left hand', '왼손'], line: ['The thumb is 1 here too, not the little finger.', '여기서도 새끼손가락이 아니라 엄지가 1번이에요.'], fig: (c) => { const f = 1 + Math.floor(c.tk / 2) % 5; return { mid: <>{tqArt('q-fingers-L', 170, String(f))}{tqFingers('L', f)}</> }; } },
    { title: ['Mirror twins', '거울 쌍둥이'], line: ['Palm to palm: 1 meets 1, 5 meets 5.', '손바닥을 마주 대 보세요. 1은 1과, 5는 5와 만나요.'], fig: () => ({ mid: tqArt('mirror', 160) }) },
  ],
  make: (n, prev) => { const R = n % 2 === 0; let f, g = 0; do { f = 1 + kqRnd(5); } while (prev && prev.f === f && g++ < 8);
    return { f, kind: 'choice', cols: 5, prompt: [R ? 'Right hand: which finger is coloured?' : 'Left hand: which finger is coloured?', R ? '오른손: 색칠된 손가락은 몇 번일까요?' : '왼손: 색칠된 손가락은 몇 번일까요?'], opts: ['1', '2', '3', '4', '5'].map(x => ({ id: x, label: x })), ans: String(f), ok: (v) => v === String(f),
      fig: (c) => ({ mid: <>{tqArt(c.res ? (R ? 'q-fingers-R' : 'q-fingers-L') : (R ? 'q-fingers-R-plain' : 'q-fingers-L-plain'), 170, String(f))}{c.res && tqFingers(R ? 'R' : 'L', f)}</> }), yes: ['Finger ' + f + '.', f + '번 손가락이에요.'], no: ['Count from the thumb, 1: this is finger ' + f + '.', '엄지 1번부터 세어 보세요. ' + f + '번 손가락이에요.'] }; },
};
// the five notes of a position: the first five notes of the major scale (tone, tone, semitone, tone), one finger each.
// Right hand: thumb on the key note, from middle C up. Left hand: little finger on the key note, below middle C
// (G, A♭, A, B♭ and B an octave lower), as in the Reading steps and the five-finger tool. s = semitones from middle C.
const TQ_LET = ['C', 'D', 'E', 'F', 'G', 'A', 'B'], TQ_WPC = [0, 2, 4, 5, 7, 9, 11], TQ_5 = [0, 2, 4, 5, 7];
const TQ_FF = [['C', 0, 0], ['D♭', 1, 1], ['D', 2, 1], ['E♭', 3, 2], ['E', 4, 2], ['F', 5, 3], ['F♯', 6, 3], ['G', 7, 4], ['A♭', 8, 5], ['A', 9, 5], ['B♭', 10, 6], ['B', 11, 6]];
const tqHand = (key, hand) => { const [, pc, L] = TQ_FF.find(x => x[0] === key), root = hand === 'R' ? pc : pc - (L < 4 ? 12 : 24);
  return TQ_5.map((s, j) => { const l = (L + j) % 7; let d = (((pc + s - TQ_WPC[l]) % 12) + 12) % 12; if (d > 6) d -= 12;
    return { s: root + s, name: TQ_LET[l] + (d === 1 ? '♯' : d === -1 ? '♭' : ''), f: hand === 'R' ? j + 1 : 5 - j, h: hand }; }); };
const tqNames = (key) => tqHand(key, 'R').map(x => x.name);
// one hand's keyboard: o.hl = 'R3' lights a finger, o.bare hides the numbers, o.mark = { semitone: style }, o.mc keeps middle C in view
const tqPosKb = (key, hand, o = {}) => { const all = tqHand(key, hand), ss = all.map(x => x.s).concat(o.mc ? [0] : []);
  const lo = Math.min(...ss), hi = Math.max(...ss), base = Math.floor((lo - 3) / 12) * 12, m = {}, names = {}, ncol = {};
  all.forEach(x => { const k = x.s - base, on = o.hl === x.h + x.f; m[k] = on ? 'pick' : 'pass'; if (!o.bare) { names[k] = String(x.f); ncol[k] = on ? KQ.COD : KQ.NV; } });
  Object.entries(o.mark || {}).forEach(([s, st]) => { m[+s - base] = st; });
  const mc = !!o.mc && !all.some(x => x.s === 0); if (mc) { names[-base] = 'C'; ncol[-base] = KQ.CO; }   // middle C: a coral C over it, its key left plain
  return { oct: Math.ceil((hi - base + 4) / 12), ks: [lo - base - 2, hi - base + 2], base, plain: false, marks: m, names, ncol, cap: mc && !o.noCap }; };
const tqPosCap = (key, hands = 'LR') => ivqCap(kqT(hands === 'LR' ? ['Both hands: ' + tqNames(key).join(' '), '양손: ' + tqNames(key).join(' ')]
  : hands === 'R' ? ['Right hand 1 2 3 4 5: ' + tqNames(key).join(' '), '오른손 1 2 3 4 5: ' + tqNames(key).join(' ')] : ['Left hand 5 4 3 2 1: ' + tqNames(key).join(' '), '왼손 5 4 3 2 1: ' + tqNames(key).join(' ')]), KQ.NV);
const tqHandW = (R) => R ? ['right hand', '오른손'] : ['left hand', '왼손'];
// both hands: the right hand's keyboard over the left hand's (as the treble staff sits over the bass), middle C in each
const tqBoth = (key) => <div style={{ display: 'flex', flexDirection: 'column', gap: 2 }}>{['R', 'L'].map(h => { const kb = tqPosKb(key, h, { mc: true, noCap: h === 'R' });
  return <div key={h}><div style={{ textAlign: 'center', fontSize: 14, fontWeight: 900, color: KQ.NV, margin: '4px 0 0' }}>{h === 'R' ? t('Right hand', '오른손') : t('Left hand', '왼손')}</div>{kqKb(kb, (k) => playKey(k + kb.base, 0.6))}</div>; })}</div>;
// which finger plays this key? / tap the key this finger plays
const tqFingerQ = (key, R, f, title, mc) => { const H = tqHand(key, R ? 'R' : 'L'), x = H.find(y => y.f === f), hw = tqHandW(R), kb0 = tqPosKb(key, R ? 'R' : 'L', { mc }), first = H[0];
  const why = R ? ['The right thumb, 1, is on ' + first.name + '; one key per finger up from there: ' + x.name + ' is ' + f + '.', '오른손 엄지 1번이 ' + first.name + ', 손가락 하나에 건반 하나씩 올라가요. ' + ivqJ(x.name, '은', '는') + ' ' + f + '번이에요.']
    : ['The left little finger, 5, is on ' + first.name + ' and the thumb, 1, on ' + H[4].name + ': ' + x.name + ' is ' + f + '.', '왼손 새끼손가락 5번이 ' + first.name + ', 엄지 1번이 ' + H[4].name + '. ' + ivqJ(x.name, '은', '는') + ' ' + f + '번이에요.'];
  return {
    choice: { id: key + R + f, f, kind: 'choice', cols: 5, prompt: [title[0] + ', ' + hw[0] + ': which finger plays ' + x.name + '?', title[1] + ', ' + hw[1] + ': ' + ivqJ(x.name, '은', '는') + ' 몇 번 손가락이 칠까요?'], opts: ['1', '2', '3', '4', '5'].map(v => ({ id: v, label: v })), ans: String(f), ok: (v) => v === String(f),
      fig: (c) => ({ kb: c.res ? tqPosKb(key, R ? 'R' : 'L', { mc, hl: (R ? 'R' : 'L') + f }) : tqPosKb(key, R ? 'R' : 'L', { mc, bare: true, mark: { [x.s]: 'pick' } }) }), play: () => playKey(x.s, 0.6), yes: ['Finger ' + f + ' plays ' + x.name + '.', f + '번 손가락이 ' + ivqJ(x.name, '을', '를') + ' 쳐요.'], no: why },
    key: { id: key + R + f, f, kind: 'key', retry: true, prompt: [title[0] + ', ' + hw[0] + ': tap the key finger ' + f + ' plays.', title[1] + ', ' + hw[1] + ': ' + f + '번 손가락이 치는 건반을 눌러 보세요.'], fig: () => ({ kb: tqPosKb(key, R ? 'R' : 'L', { mc, bare: true }) }), ok: (k) => k + kb0.base === x.s,
      yes: ['Finger ' + f + ': ' + x.name + '.', f + '번 손가락: ' + ivqJ(x.name, '이에요', '예요') + '.'], no: () => why },
  }; };
const tqPosLesson = (key, o) => ({
  title: o.title, allLine: o.allLine, fig: () => ({ mid: tqBoth(key), below: tqPosCap(key) }),
  steps: [
    { title: ['Right hand', '오른손'], line: o.right, fig: (c) => ({ kb: tqPosKb(key, 'R', { mc: true, hl: 'R' + (1 + Math.floor(c.tk / 2) % 5) }), below: tqPosCap(key, 'R') }) },
    { title: ['Left hand', '왼손'], line: o.left, fig: (c) => ({ kb: tqPosKb(key, 'L', { mc: true, hl: 'L' + (5 - Math.floor(c.tk / 2) % 5) }), below: tqPosCap(key, 'L') }) },
    { title: ['Both hands', '양손'], line: o.both, fig: () => ({ mid: tqBoth(key), below: tqPosCap(key) }) },
  ],
  make: (n, prev) => { const R = n % 2 === 0; let f, g = 0; do { f = 1 + kqRnd(5); } while (prev && prev.id === key + R + f && g++ < 8); const Q = tqFingerQ(key, R, f, o.title, true); return Math.floor(n / 2) % 2 === 0 ? Q.choice : Q.key; },
});
TQ_SPEC['kp-cpos'] = tqPosLesson('C', { title: ['C position', 'C 자리'], allLine: ['One finger on each key, C to G, in both hands.', '양손 모두, C부터 G까지 건반 하나에 손가락 하나.'],
  right: ['Thumb 1 on middle C, then D 2, E 3, F 4, G 5.', '엄지 1번이 가운데 도, 그다음 D 2, E 3, F 4, G 5.'], left: ['Little finger 5 on the C below middle C, then D 4, E 3, F 2, thumb 1 on G.', '새끼손가락 5번이 가운데 도 아래의 C, 그다음 D 4, E 3, F 2, 엄지 1번이 G.'],
  both: ['The two thumbs point at each other: left 1 on G, right 1 on middle C.', '두 엄지가 서로를 향해요. 왼손 1번은 G, 오른손 1번은 가운데 도.'] });
TQ_SPEC['kp-gpos'] = tqPosLesson('G', { title: ['G position', 'G 자리'], allLine: ['The same shape, moved to G: G A B C D, one finger on each key.', '같은 모양을 G로 옮겨요. G A B C D, 건반 하나에 손가락 하나.'],
  right: ['Thumb 1 on the G above middle C, then A 2, B 3, C 4, D 5.', '엄지 1번이 가운데 도 위의 G, 그다음 A 2, B 3, C 4, D 5.'], left: ['Little finger 5 on a low G, then A 4, B 3, C 2, thumb 1 on D.', '새끼손가락 5번이 낮은 G, 그다음 A 4, B 3, C 2, 엄지 1번이 D.'],
  both: ['The left hand sits low, well below middle C; the right hand just above it.', '왼손은 가운데 도보다 한참 아래, 오른손은 가운데 도 바로 위에 있어요.'] });
const TQ_FIVE_STEPS = [['D', 3, ['D E F♯ G A: the whole step from E is F♯, under finger 3.', 'D E F♯ G A: E에서 온음 올라가면 F♯, 3번 손가락이에요.']],
  ['F', 4, ['F G A B♭ C: the half step from A is B♭, under finger 4.', 'F G A B♭ C: A에서 반음 올라가면 B♭, 4번 손가락이에요.']],
  ['E♭', 1, ['E♭ F G A♭ B♭: the thumb starts on a black key. The same shape.', 'E♭ F G A♭ B♭: 엄지가 검은건반에서 시작해요. 모양은 같아요.']]];
TQ_SPEC['kp-five'] = {
  title: ['Five-finger positions in every key', '모든 조의 다섯 손가락 자리'], allLine: ['A five-finger position is the first five notes of the major scale, one finger on each: tone, tone, semitone, tone. The same shape in all 12 keys.', '다섯 손가락 자리는 장음계의 처음 다섯 음이에요. 손가락 하나에 음 하나: 온음, 온음, 반음, 온음. 12개 조 모두 같은 모양이에요.'],
  fig: (c) => { const key = ['C', 'G', 'D', 'A', 'E', 'F', 'B♭', 'E♭'][Math.floor(c.tk / 3) % 8]; return { kb: tqPosKb(key, 'R'), below: ivqCap(kqT([key + ' position: ' + tqNames(key).join(' '), key + ' 자리: ' + tqNames(key).join(' ')]), KQ.COD) }; },
  steps: [
    { title: ['The shape: T T S T', '모양: 온 온 반 온'], line: ['C D E F G: tone, tone, semitone, tone. Fingers 3 and 4 are the close pair.', 'C D E F G: 온음, 온음, 반음, 온음. 3번과 4번 손가락 사이가 가까운 짝이에요.'], fig: () => ({ kb: tqPosKb('C', 'R', { hl: 'R3', mark: { 5: 'pick' } }), below: tqPosCap('C', 'R') }) },
    ...TQ_FIVE_STEPS.map(([key, f, line]) => ({ title: [key + ' position', key + ' 자리'], line, fig: () => ({ kb: tqPosKb(key, 'R', { hl: 'R' + f }), below: tqPosCap(key, 'R') }) })),
  ],
  make: (n, prev) => { let key, g = 0; do { key = kqPick(TQ_FF.slice(1))[0]; } while (prev && prev.key === key && g++ < 8);
    if (n % 2 === 0) { const H = tqHand(key, 'R'), kb = tqPosKb(key, 'R', { bare: true }), r = H[0].s - kb.base, blank = { ...kb, marks: { [r]: 'pick' }, names: { [r]: '1' }, ncol: { [r]: KQ.COD } };
      return { key, kind: 'multi', retry: true, targets: H.slice(1).map(x => x.s - kb.base), prompt: ['Right hand, ' + key + ' position: the thumb is on ' + key + '. Tap the keys for fingers 2 to 5.', '오른손 ' + key + ' 자리: 엄지는 ' + key + ' 위에 있어요. 2번부터 5번 손가락의 건반을 눌러 보세요.'], prog: (a, b) => ['Found ' + a + ' of ' + b + '. Keep going.', b + '개 중 ' + a + '개를 찾았어요. 계속해요.'],
        fig: () => ({ kb: blank }), yes: [key + ' position: ' + tqNames(key).join(' ') + '.', key + ' 자리: ' + tqNames(key).join(' ') + '.'],
        no: () => ['Not that one. From ' + key + ': tone, tone, semitone, tone.', '그 건반은 아니에요. ' + key + '에서 온음, 온음, 반음, 온음.'] }; }
    const R = Math.floor(n / 2) % 2 === 0; let f, h = 0; do { f = 2 + kqRnd(4); } while (!/[♯♭]/.test(tqHand(key, R ? 'R' : 'L').find(x => x.f === f).name) && h++ < 6);
    return { ...tqFingerQ(key, R, f, [key + ' position', key + ' 자리']).choice, key }; },
};

// ══ Registration ══
const TQ_ROWS = [
  ['k-posture', 'kp-sit', 'Sit at the piano', '피아노 앞에 앉기', 'Front half, feet flat, sit tall.', '앞쪽 절반, 발은 평평하게, 곧게.'],
  ['k-posture', 'kp-arm', 'Let the arm carry the hand', '팔이 손을 데려가요', 'Six warm-ups, big to small.', '준비 운동 여섯 가지, 큰 것부터 작은 것까지.'],
  ['k-posture', 'kp-hand', 'A round hand', '둥근 손', 'Like holding a ball; the thumb a tipped boat.', '공을 쥔 것처럼, 엄지는 누운 배처럼.'],
  ['k-posture', 'kp-check', 'My five checks', '나의 다섯 가지 확인', 'Every time, before you play.', '칠 때마다, 치기 전에.'],
  ['k-positions', 'kp-fingers', 'Finger numbers', '손가락 번호', 'Thumbs are always 1: mirror twins.', '엄지는 언제나 1번: 거울 쌍둥이.'],
  ['k-positions', 'kp-cpos', 'C position', 'C 자리', 'C to G, one finger on each key.', 'C부터 G까지, 건반 하나에 손가락 하나.'],
  ['k-positions', 'kp-gpos', 'G position', 'G 자리', 'G to D, the same shape.', 'G부터 D까지, 같은 모양.'],
  ['k-positions', 'kp-five', 'Five-finger positions in every key', '모든 조의 다섯 손가락 자리', 'Tone, tone, semitone, tone.', '온음, 온음, 반음, 온음.'],
];
TQ_ROWS.forEach(([concept, id, en, ko, benEn, bko]) => {
  TOOLS.push({ id, ch: 'concept', title: en, blurb: benEn, hidden: true, get kicker() { return TOOL_AREAS.find(a => a.id === 'tech').name + ' · ' + homeCatById(concept).name; }, C: () => <KqEngine spec={TQ_SPEC[id]}/> });
  TOOL_KO[id] = [ko, bko];
  const tl = TOOLS[TOOLS.length - 1], k = TOOL_KO[id], ti = tl.title, bl = tl.blurb; tl.titleEn = ti; tl.blurbEn = bl;
  Object.defineProperty(tl, 'title', { get: () => (LANG === 'ko' ? k[0] : ti), enumerable: true, configurable: true });
  Object.defineProperty(tl, 'blurb', { get: () => (LANG === 'ko' ? k[1] : bl), enumerable: true, configurable: true });
  TOOL_CONCEPT[id] = concept;
});
