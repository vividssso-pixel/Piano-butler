
// ══ Build X: Listen and sing on the Home (the Aural door). Each lesson is the book's page (lbhSpec, as Rhythm and Posture);
// the questions are heard: they play by themselves, and ♪ Again plays them again ══
LBH_FN['listen-sing'] = (s) => lsLbPages(s);
const lsTapQ = (Pad, extra, prompt, yes) => (n) => ({ kind: 'tap', retry: true, prompt, ok: (v) => !!(v && v.ok),
  fig: (c) => ({ mid: <Pad key={c.qn} {...extra(n)} onResult={(r) => c.pick(r)}/> }),
  yes: yes || ['On the beat ✓', '박에 맞았어요 ✓'], no: () => ['Nearly. Listen again, count inside, and try once more.', '거의 다 왔어요. 다시 듣고, 속으로 세면서 한 번 더 해 봐요.'] });
const lsUpDownQ = (n, prev) => { const x = lsPair(prev && prev.x); return { x, kind: 'choice', cols: 2, prompt: ['Listen: is the second note higher or lower?', '들어 봐요: 두 번째 음은 더 높을까요, 더 낮을까요?'],
  opts: ['up', 'down'].map(id => ({ id, label: () => <span style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 4 }}>{lsDirIcon(id, 28)}{LS_DIR[id]()}</span> })),
  ans: x.answer, ok: (v) => v === x.answer, play: () => lsSeq([x.a, x.b], 750),
  fig: (c) => ({ mid: <LsTwoKeys a={c.res ? x.a : null} b={c.res ? x.b : null}/> }),
  yes: x.answer === 'up' ? ['Higher: up towards the bird.', '더 높아요: 새 쪽으로 위.'] : ['Lower: down towards the turtle.', '더 낮아요: 거북이 쪽으로 아래.'],
  no: x.answer === 'up' ? ['It was higher: up towards the bird. The keys show where.', '더 높았어요: 새 쪽으로 위. 건반이 어디인지 보여 줘요.'] : ['It was lower: down towards the turtle. The keys show where.', '더 낮았어요: 거북이 쪽으로 아래. 건반이 어디인지 보여 줘요.'] }; };
const lsFindQ = (n, prev) => { let d, g = 0; do { d = 28 + Math.floor(Math.random() * 5); } while (prev && prev.d === d && g++ < 10);
  return { d, kind: 'tapkey', retry: true, prompt: ['Hear the note, sing it on "la", then find it in C position.', '음을 듣고 "라"로 불러 본 다음, C 자리에서 찾아요.'], ok: (v) => v === d, play: () => lsPlay(d, 1.1),
    fig: (c) => ({ mid: <LsKeys lit={c.res === 'ok' ? { [d]: 'cor' } : {}} letters={c.res === 'ok'} onTap={(k) => { lsPlay(k, 0.6); if (c.res !== 'ok') c.pick(k); }}/> }),
    yes: ['That\'s it: ' + hpLet(d) + '. Sing it with the key.', '찾았어요: ' + hpLet(d) + '. 건반과 함께 불러요.'], no: (k) => (d > k ? ['Higher: towards the bird. Sing it again, then try.', '더 높아요: 새 쪽으로. 다시 불러 보고 쳐요.'] : ['Lower: towards the turtle. Sing it again, then try.', '더 낮아요: 거북이 쪽으로. 다시 불러 보고 쳐요.']) }; };
const lsAdd = (id, i, en, ko, benEn, bko, make) => { const spec = lbhSpec('listen-sing', i, { make });
  TOOLS.push({ id, ch: 'concept', title: en, blurb: benEn, hidden: true, get kicker() { return t('Aural', '청음') + ' · ' + t('Listen and sing', '듣고 노래하기'); }, C: () => <KqEngine spec={spec}/> });
  lbhRetitle(id, en, ko, benEn, bko); };
lsAdd('ls-beat', 1, 'Keep the beat', '박 지키기', 'In two or three, slow to quick; the music stops, the beat goes on.', '두 박이나 세 박, 느리게부터 빠르게까지. 음악이 멈춰도 박은 계속.', lsTapQ(LsBeatPad, (n) => ({ meter: n % 2 ? 3 : 2, speed: ['slow', 'moderate', 'quick'][Math.floor(n / 2) % 3], fixed: true }), ['Tap every beat; keep going through the quiet bars.', '박마다 쳐요. 조용한 마디에서도 계속 가요.']));
lsAdd('ls-echo', 2, 'Echo the rhythm', '리듬 메아리', 'Two bars heard, two bars tapped back.', '두 마디 듣고, 두 마디 따라 치기.', lsTapQ(LsEchoPad, (n) => ({ fixed: LS_ECHO[n % LS_ECHO.length] }), ['Listen to two bars, then tap them straight back.', '두 마디를 듣고, 바로 이어서 똑같이 쳐요.'], ['Echoed on the beat ✓', '박에 맞춰 메아리 ✓']));
lsAdd('ls-updown', 3, 'Higher or lower', '높을까, 낮을까?', 'Higher: up to the bird. Lower: down to the turtle.', '높으면 새 쪽으로, 낮으면 거북이 쪽으로.', lsUpDownQ);
lsAdd('ls-find', 4, 'Find your note', '내 음 찾기', 'Sing it, then find it: higher or lower?', '부르고, 찾아요: 더 높아? 더 낮아?', lsFindQ);
lsAdd('ls-sing', 5, 'Sing it back', '따라 부르기', 'Listen, sing, play: three notes, then five or six.', '듣고, 부르고, 치기: 세 음, 그다음 다섯·여섯 음.', lsTapQ(LsSingPad, (n) => ({ fixed: LS_SING[[3, 5, 6][n % 3]][Math.floor(n / 3) % 6] }), ['Listen, sing it back on "la", then play it in C position.', '듣고, "라"로 따라 부른 다음, C 자리에서 쳐요.'], ['Listen, sing, play ✓', '듣고, 부르고, 치기 ✓']));
