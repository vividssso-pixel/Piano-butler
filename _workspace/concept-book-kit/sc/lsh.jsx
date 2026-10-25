
// ══ Build X: Listen and sing on the Home (the Aural door). Each lesson is the book's page (lbhSpec, as Rhythm and Posture);
// the questions are heard: they play by themselves, and ♪ Again plays them again ══
LBH_FN['listen-sing'] = (s) => lsLbPages(s);
const lsTapQ = (Pad, extra, prompt, yes) => (n) => ({ kind: 'tap', retry: true, prompt, ok: (v) => !!(v && v.ok),
  fig: (c) => ({ mid: <Pad key={c.qn} {...extra(n)} onResult={(r) => c.pick(r)}/> }),
  yes: yes || ['On the beat ✓', '박에 맞았어요 ✓'], no: () => ['Nearly. Listen again, count inside, and try once more.', '거의 다 왔어요. 다시 듣고, 속으로 세면서 한 번 더 해 봐요.'] });
const lsUpDownQ = (n, prev) => { const x = lsPair(prev && prev.x); return { x, kind: 'choice', cols: 3, prompt: ['Listen: does the second note go up, down, or stay the same?', '들어 봐요: 두 번째 음은 위로 갈까요, 아래로 갈까요, 같을까요?'],
  opts: ['up', 'same', 'down'].map(id => ({ id, label: () => <span style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 4 }}>{lsDirIcon(id, 28)}{LS_DIR[id]()}</span> })),
  ans: x.answer, ok: (v) => v === x.answer, play: () => lsSeq([x.a, x.b], 750),
  fig: (c) => ({ mid: <LsTwoKeys a={c.res ? x.a : null} b={c.res ? x.b : null}/> }),
  yes: x.answer === 'up' ? ['Up: towards the bird.', '위로: 새 쪽으로.'] : x.answer === 'down' ? ['Down: towards the turtle.', '아래로: 거북이 쪽으로.'] : ['The same note twice.', '같은 음이 두 번.'],
  no: x.answer === 'up' ? ['It went up, towards the bird. The keys show where.', '위로 갔어요, 새 쪽으로. 건반이 어디인지 보여 줘요.'] : x.answer === 'down' ? ['It went down, towards the turtle. The keys show where.', '아래로 갔어요, 거북이 쪽으로. 건반이 어디인지 보여 줘요.'] : ['It was the same note twice.', '같은 음이 두 번이었어요.'] }; };
const lsFindQ = (n, prev) => { let d, g = 0; do { d = 28 + Math.floor(Math.random() * 5); } while (prev && prev.d === d && g++ < 10);
  return { d, kind: 'tapkey', retry: true, prompt: ['Hear the note, sing it on "la", then find it in C position.', '음을 듣고 "라"로 불러 본 다음, C 자리에서 찾아요.'], ok: (v) => v === d, play: () => lsPlay(d, 1.1),
    fig: (c) => ({ mid: <LsKeys lit={c.res === 'ok' ? { [d]: 'cor' } : {}} letters={c.res === 'ok'} onTap={(k) => { lsPlay(k, 0.6); if (c.res !== 'ok') c.pick(k); }}/> }),
    yes: ['That\'s it: ' + hpLet(d) + '. Sing it with the key.', '찾았어요: ' + hpLet(d) + '. 건반과 함께 불러요.'], no: (k) => (d > k ? ['Higher: towards the bird. Sing it again, then try.', '더 높아요: 새 쪽으로. 다시 불러 보고 쳐요.'] : ['Lower: towards the turtle. Sing it again, then try.', '더 낮아요: 거북이 쪽으로. 다시 불러 보고 쳐요.']) }; };
const lsAdd = (id, i, en, ko, benEn, bko, make) => { const spec = lbhSpec('listen-sing', i, { make });
  TOOLS.push({ id, ch: 'concept', title: en, blurb: benEn, hidden: true, get kicker() { return t('Aural', '청음') + ' · ' + t('Listen and sing', '듣고 노래하기'); }, C: () => <KqEngine spec={spec}/> });
  lbhRetitle(id, en, ko, benEn, bko); };
lsAdd('ls-beat', 1, 'Keep the beat', '박 지키기', 'The music stops; the beat goes on.', '음악이 멈춰도 박은 계속 가요.', lsTapQ(LsBeatPad, () => ({}), ['Tap every beat; keep going through the quiet bar.', '박마다 쳐요. 조용한 마디에서도 계속 가요.']));
lsAdd('ls-echo', 2, 'Echo the rhythm', '리듬 메아리', 'Two bars heard, two bars tapped back.', '두 마디 듣고, 두 마디 따라 치기.', lsTapQ(LsEchoPad, (n) => ({ fixed: LS_ECHO[n % LS_ECHO.length] }), ['Listen to two bars, then tap them straight back.', '두 마디를 듣고, 바로 이어서 똑같이 쳐요.'], ['Echoed on the beat ✓', '박에 맞춰 메아리 ✓']));
lsAdd('ls-updown', 3, 'Up or down', '위로? 아래로?', 'Up to the bird, down to the turtle.', '위로는 새, 아래로는 거북이.', lsUpDownQ);
lsAdd('ls-find', 4, 'Find your note', '내 음 찾기', 'Sing it, then find it: higher or lower?', '부르고, 찾아요: 더 높아? 더 낮아?', lsFindQ);
lsAdd('ls-sing', 5, 'Sing it back', '따라 부르기', 'Listen, sing, play: three notes, then five.', '듣고, 부르고, 치기: 세 음, 그다음 다섯 음.', lsTapQ(LsSingPad, (n) => ({ fixed: LS_SING[n % 2 ? 5 : 3][Math.floor(n / 2) % 6] }), ['Listen, sing it back on "la", then play it in C position.', '듣고, "라"로 따라 부른 다음, C 자리에서 쳐요.'], ['Listen, sing, play ✓', '듣고, 부르고, 치기 ✓']));
