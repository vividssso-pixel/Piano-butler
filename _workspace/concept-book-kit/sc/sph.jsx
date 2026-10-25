
// ══ Build AB: Playing scales on the Home (the Technique door, 'Playing scales and chords'). Each lesson is the book's page
// (lbhSpec); the questions after it are the page's own: a bump heard, a scale played along, natural or harmonic, mirror twins,
// two octaves ══
LBH_FN['scale-play'] = (s) => spLbPages(s);
const spHomeAdd = (id, i, en, ko, benEn, bko, make) => lbhAdd(id, 'k-play', 'tech', en, ko, benEn, bko, lbhSpec('scale-play', i, { make }));
const spBumpQ = (n) => { const k = n % 2 ? 'G' : 'C', hand = Math.floor(n / 2) % 2 ? 'L' : 'R', b = Math.random() < 0.5, S = spTurnSeq(k, hand), K = spKeys(k, hand, 1), ans = b ? 'bumpy' : 'smooth';
  return { kind: 'choice', cols: 2, prompt: [(hand === 'R' ? 'Right hand, ' : 'Left hand, ') + SP_SC[k].en + '. Listen to the turns: smooth, or bumpy?', (hand === 'R' ? '오른손, ' : '왼손, ') + SP_SC[k].ko + '. 넘기는 곳을 들어 봐요: 매끄럽게? 덜컹?'],
    opts: ['smooth', 'bumpy'].map(id => ({ id, label: SP_WORD[id] })), ans, ok: (v) => v === ans, play: () => spPlay(spTurnEvents(k, hand, b), 72),
    fig: () => ({ mid: <SpKb lo={K[0]} hi={K[7]} W={30} lit={Object.fromEntries(K.map(x => [x, 'pale']))} names={spNameMap(K, spNames(k, 1))} hand={S[0].win}/> }),
    yes: b ? ['Bumpy: the note after each turn came late and loud.', '덜컹: 넘긴 다음 음이 늦고 크게 났어요.'] : ['Smooth: every note even, the turns too.', '매끄럽게: 넘기는 곳까지 모든 음이 고르게.'],
    no: b ? ['Listen again: the note after each turn came late and loud. That is the bump.', '다시 들어 봐요: 넘긴 다음 음이 늦고 컸어요. 그게 덜컹이에요.'] : ['Listen again: every note came on time, even at the turns.', '다시 들어 봐요: 넘기는 곳까지 모든 음이 제때 났어요.'] }; };
const spBeatQ = (n) => { const k = n % 2 ? 'G' : 'C', hand = Math.floor(n / 2) % 2 ? 'L' : 'R', bpm = n < 4 ? 60 : 76;
  return { kind: 'tap', retry: true, prompt: ['Play along: one note on every click, up and back.', '같이 쳐요: 클릭마다 한 음, 올라갔다 내려와요.'], ok: (v) => !!(v && v.ok),
    fig: (c) => ({ mid: <SpBeatPad key={c.qn} fixed={{ k, hand, bpm }} onResult={(r) => c.pick(r)}/> }),
    yes: ['On the beat ✓', '박에 맞았어요 ✓'], no: () => ['Nearly. Tap ▶ Listen first, then play along again.', '거의 다 왔어요. 먼저 ▶ 듣기, 그다음 다시 같이 쳐요.'] }; };
const spNhQ = (n) => { const r = n % 2 ? 'E' : 'A', f = Math.random() < 0.5 ? 'nat' : 'har', k = r + 'm' + (f === 'har' ? 'h' : ''), K = spKeys(k, 'R', 1), ix = spUpDown(8);
  return { kind: 'choice', cols: 2, prompt: [r + ' minor: natural or harmonic? Look at the 7th note, and listen.', r + '단조: 자연일까요, 화성일까요? 7번째 음을 보고, 들어 봐요.'],
    opts: ['nat', 'har'].map(id => ({ id, label: SP_WORD[id] })), ans: f, ok: (v) => v === f, play: () => spPlay(ix.map((j, s) => ({ at: s, keys: [K[j]], len: s === ix.length - 1 ? 2 : 1 })), 84),
    fig: (c) => ({ mid: <SpKb lo={K[0]} hi={K[7]} W={30} lit={Object.fromEntries(K.map((x, j) => [x, c.res && j === 6 ? 'cor' : 'pale']))} names={spNameMap(K, spNames(k, 1))} up={spFingMap(K, spFing(k, 'R', 1))}/> }),
    yes: f === 'har' ? ['Harmonic: the 7th is raised, ' + SP_SC[r + 'mh'].nm[6] + '.', '화성: 7번째 음이 올라갔어요(' + SP_SC[r + 'mh'].nm[6] + ').'] : ['Natural: the 7th is ' + SP_SC[r + 'm'].nm[6] + ', not raised.', '자연: 7번째 음 ' + SP_SC[r + 'm'].nm[6] + ', 올라가지 않았어요.'],
    no: f === 'har' ? ['It is harmonic: look at the 7th, ' + SP_SC[r + 'mh'].nm[6] + ', up a half step.', '화성이에요: 7번째 음 ' + SP_SC[r + 'mh'].nm[6] + ', 반음 올라갔어요.'] : ['It is natural: the 7th, ' + SP_SC[r + 'm'].nm[6] + ', is not raised.', '자연이에요: 7번째 음 ' + SP_SC[r + 'm'].nm[6] + '은 그대로예요.'] }; };
const spMirrorQ = (n, prev) => { const k = n % 3 === 2 ? 'Amh' : 'C', c = spCm(k); let j, g = 0; do { j = 1 + Math.floor(Math.random() * 7); } while (prev && prev.j === j && g++ < 10);
  const f = SP_CM_F[j], ans = spCmLet(c, 'L', j), pool = shuffle(Array.from(new Set(c.nmL.filter(x => x !== ans)))).slice(0, 3), lit0 = {}; c.R.concat(c.L).forEach(x => { lit0[x] = 'pale'; }); lit0[c.R[j]] = 'cor';
  return { j, kind: 'choice', cols: 4, prompt: ['Contrary motion, ' + SP_CM[k].en + '. The right hand plays ' + spCmLet(c, 'R', j) + ' with finger ' + f + '. Which key does the left hand’s finger ' + f + ' play?', '반대 방향, ' + SP_CM[k].ko + '. 오른손 ' + f + '번: ' + spCmLet(c, 'R', j) + '. 왼손 ' + f + '번은 어느 건반일까요?'],
    opts: shuffle([ans].concat(pool)).map(x => ({ id: x, label: x })), ans, ok: (v) => v === ans, play: () => { playKey(c.R[j], 0.6); },
    fig: (cx) => ({ mid: <SpKb lo={c.L[7]} hi={c.R[7]} W={22} H={66} lit={cx.res ? Object.assign({}, lit0, { [c.L[j]]: 'good' }) : lit0} names={cx.res ? Object.assign(spNameMap(c.R, c.nmR), spNameMap(c.L, c.nmL)) : spNameMap(c.R, c.nmR)} up={{ [c.R[j]]: f }} dn={cx.res ? { [c.L[j]]: f } : {}} act={{ [c.R[j]]: true, ['d' + c.L[j]]: true }} k={1.5}/> }),
    yes: ['Mirror twins: ' + ans + ', finger ' + f + ' too.', '거울 쌍둥이: ' + ans + ', 왼손도 ' + f + '번.'], no: ['Count out from the middle: the same number of steps each way. It is ' + ans + '.', '가운데에서부터 세어 봐요: 양쪽으로 같은 걸음 수. 답은 ' + ans + '.'] }; };
const spTwoQ = (n, prev) => { const k = ['G', 'F', 'Em', 'Dmh'][n % 4], hand = Math.random() < 0.5 ? 'R' : 'L', F = spFing(k, hand, 2); let j, g = 0; do { j = Math.floor(Math.random() * 15); } while (prev && prev.j === j && g++ < 10);
  const hide = F.map((_, x) => x === j);
  return { j, kind: 'choice', cols: 5, prompt: [(hand === 'R' ? 'Right hand, ' : 'Left hand, ') + SP_SC[k].en + ', two octaves: which finger plays the coral note?', (hand === 'R' ? '오른손, ' : '왼손, ') + SP_SC[k].ko + ', 두 옥타브: 산호색 음은 몇 번 손가락일까요?'],
    opts: [1, 2, 3, 4, 5].map(x => ({ id: x, label: String(x) })), ans: F[j], ok: (v) => v === F[j], play: () => playKey(spKeys(k, hand, 2)[j], 0.6),
    fig: (c) => ({ mid: <SpStrip k={k} ask={j} hideR={hand === 'R' && !c.res ? hide : null} hideL={hand === 'L' && !c.res ? hide : null}/> }),
    yes: ['Finger ' + F[j] + '.', F[j] + '번 손가락.'], no: ['It is finger ' + F[j] + '. Say the groups out loud as you play.', F[j] + '번이에요. 치면서 묶음을 소리 내어 말해 봐요.'] }; };
spHomeAdd('sp-turn', 1, 'Smooth turns', '매끄럽게 넘기기', 'The thumb gets ready early: no bump.', '엄지는 미리 준비: 덜컹 없이.', spBumpQ);
spHomeAdd('sp-beat', 2, 'On the beat', '박에 맞춰', 'One note on every click, up and back, at 60, then 76.', '클릭마다 한 음, 60에서 76까지.', spBeatQ);
spHomeAdd('sp-minor', 3, 'A and E minor', 'A단조와 E단조', 'Natural, then harmonic: the 7th goes up.', '자연, 그다음 화성: 7번째 음이 올라가요.', spNhQ);
spHomeAdd('sp-mirror', 4, 'Mirror twins', '거울 쌍둥이', 'Contrary motion: the same numbers, both ways.', '반대 방향: 양쪽으로 같은 번호.', spMirrorQ);
spHomeAdd('sp-two', 5, 'Two octaves, hands together', '두 옥타브, 양손 함께', 'Grade 1: two notes a beat; the thumbs meet in the middle.', 'Grade 1: 한 박에 두 음, 엄지는 가운데에서 만나요.', spTwoQ);
