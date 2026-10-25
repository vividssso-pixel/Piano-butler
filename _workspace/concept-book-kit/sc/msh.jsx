
// ══ Build AC: Minor scales on the Home (Pitch → Scales, its own group 'Minor scales'). Each lesson is the book's page
// (lbhSpec); the questions after it are the page's own ══
LBH_FN['minor-scales'] = (s) => msLbPages(s);
const msHomeAdd = (id, i, en, ko, benEn, bko, make) => lbhAdd(id, 'p-scale', 'pitch', en, ko, benEn, bko, lbhSpec('minor-scales', i, { make }));
const msThirdQ = (n, prev) => { let r, q, g = 0; do { r = pick(MS_ROOTS); q = Math.random() < 0.5 ? 'maj' : 'min'; } while (prev && prev.r === r && prev.ans === q && g++ < 10);
  const ear = n % 2 === 1, K = msThirdKeys(r, q);
  return { r, kind: 'choice', cols: 2, prompt: ear ? ['Listen: a major or a minor third?', '들어 봐요: 장3도일까요, 단3도일까요?'] : ['Count the half steps: a major or a minor third?', '반음을 세어요: 장3도일까요, 단3도일까요?'],
    opts: [['maj', ['Major third', '장3도']], ['min', ['Minor third', '단3도']]].map(([id, l]) => ({ id, label: () => t(l[0], l[1]) })), ans: q, ok: (v) => v === q, play: ear ? () => msPlayThird(r, q) : undefined,
    fig: (c) => ({ mid: <SpKb lo={-1} hi={17} W={22} H={64} lit={!ear || c.res ? K.lit : {}} up={c.res ? K.up : {}}/> }),
    yes: q === 'maj' ? ['Four half steps: a major third.', '반음 4개: 장3도.'] : ['Three half steps: a minor third.', '반음 3개: 단3도.'],
    no: q === 'maj' ? ['It was four half steps: a major third. Count them on the keys.', '반음 4개였어요: 장3도. 건반에서 세어 봐요.'] : ['It was three half steps: a minor third. Count them on the keys.', '반음 3개였어요: 단3도. 건반에서 세어 봐요.'] }; };
const msRelQ = (n, prev) => { let m, g = 0; do { m = pick(MS_KEYS); } while (prev && prev.m === m && g++ < 10); const M = MS_REL[m];
  return { m, kind: 'choice', cols: 2, prompt: ['Which minor key has this key signature?', '이 조표를 쓰는 단조는 무엇일까요?'], opts: MS_KEYS.map(x => ({ id: x, label: () => msName(x) })), ans: m, ok: (v) => v === m,
    fig: (c) => ({ mid: <div><div style={{maxWidth:220,margin:'0 auto'}}><SkgStaff items={[['sp', 6]]} k={M} width={200} full pad={[22, 16]} o={{ ...SKG_AL, ksCol: PEN_C }} label={msSigWords(M)}/></div>{c.res && <MsRelKeys m={m}/>}</div> }),
    yes: ['Yes: ' + m + ' minor, three half steps below ' + prettyNote(M) + '.', '맞아요: ' + m + '단조, ' + prettyNote(M) + '에서 반음 세 칸 아래.'], no: [msMajName(M) + '’s key signature: three half steps down is ' + m + ' minor.', msMajName(M) + '의 조표: 반음 세 칸 아래는 ' + m + '단조.'] }; };
const msRaiseQ = (n, prev) => { let m, g = 0; do { m = pick(MS_KEYS); } while (prev && prev.m === m && g++ < 10); const ans = msNames(m, 'harmonic')[6], N7 = msNames(m, 'natural')[6], pool = shuffle(['G♯', 'D♯', 'C♯', 'F♯', 'B♭', 'E♭'].filter(x => x !== ans)).slice(0, 3);
  return { m, kind: 'choice', cols: 4, prompt: [m + ' harmonic minor: which note is the raised 7th?', m + ' 화성 단음계: 올라간 7번째 음은 무엇일까요?'], opts: shuffle([ans].concat(pool)).map(x => ({ id: x, label: x })), ans, ok: (v) => v === ans,
    fig: (c) => ({ mid: <MsStaff m={m} form={c.res ? 'harmonic' : 'natural'} hl={c.res ? [6] : []}/> }),
    yes: ['Yes: the 7th, ' + N7 + ', goes up to ' + ans + '.', '맞아요: 7번째 음 ' + N7 + ' → ' + ans + '.'], no: ['Always the 7th: ' + N7 + ' → ' + ans + ', beside the note.', '언제나 7번째 음: ' + N7 + ' → ' + ans + ', 음표 옆에.'] }; };
const msGapQ = (n, prev) => { let m, j, g = 0; do { m = pick(MS_KEYS); j = n % 3 === 2 ? 5 : Math.floor(Math.random() * 7); } while (prev && prev.m === m && prev.j === j && g++ < 10);
  const N = msNames(m, 'harmonic'), K = msKeys(m, 'harmonic'), a = MS_GAPS[j];
  return { m, j, kind: 'choice', cols: 3, prompt: [m + ' harmonic minor, ' + N[j] + ' to ' + N[j + 1] + ': a tone, a semitone, or a tone and a half?', m + ' 화성 단음계, ' + N[j] + '에서 ' + N[j + 1] + ': 온음, 반음, 온음 반?'],
    opts: [2, 1, 3].map(x => ({ id: x, label: () => msGapLong(x) })), ans: a, ok: (v) => v === a,
    fig: (c) => ({ mid: <SpKb lo={K[0]} hi={K[7]} W={28} H={66} lit={{ [K[j]]: 'cor', [K[j + 1]]: 'cor' }} names={spNameMap(K, N)} up={c.res ? Object.fromEntries(Array.from({ length: a }, (_, i) => [K[j] + i + 1, i + 1])) : {}}/> }),
    yes: [N[j] + ' to ' + N[j + 1] + ': ' + ['', 'a semitone', 'a tone', 'a tone and a half'][a] + '.', N[j] + '에서 ' + N[j + 1] + ': ' + ['', '반음', '온음', '온음 반'][a] + '.'], no: ['Count the half steps on the keys: ' + a + '.', '건반에서 반음을 세어요: ' + a + '.'] }; };
const msEarQ = (n, prev) => { let x, g = 0; do { x = pick(MS_EAR); } while (prev && prev.x && prev.x[0] === x[0] && prev.x[1] === x[1] && g++ < 10); const K = msEarKeys(x);
  return { x, kind: 'choice', cols: 2, prompt: ['Listen: a major scale, or a harmonic minor?', '들어 봐요: 장음계일까요, 화성 단음계일까요?'], opts: [['maj', ['Major', '장음계']], ['min', ['Harmonic minor', '화성 단음계']]].map(([id, l]) => ({ id, label: () => t(l[0], l[1]) })), ans: x[1], ok: (v) => v === x[1],
    play: () => spPlay(spUpDown(8).map((j, s) => ({ at: s, keys: [K[j]], len: s === 14 ? 2 : 1 })), 100),
    fig: (c) => ({ mid: <SpKb lo={K[0]} hi={K[7]} W={28} H={66} lit={c.res ? Object.fromEntries(K.map(y => [y, 'pale'])) : {}} names={c.res ? spNameMap(K, x[1] === 'maj' ? spellScale(x[0]).concat([x[0]]).map(prettyNote) : msNames(x[0], 'harmonic')) : null}/> }),
    yes: ['Yes: ' + (x[1] === 'maj' ? prettyNote(x[0]) + ' major' : x[0] + ' harmonic minor') + '.', '맞아요: ' + (x[1] === 'maj' ? prettyNote(x[0]) + '장조' : x[0] + ' 화성 단음계') + '.'],
    no: ['It was ' + (x[1] === 'maj' ? prettyNote(x[0]) + ' major: a bright third, even steps.' : x[0] + ' harmonic minor: listen for the wide step under the top.'), '정답: ' + (x[1] === 'maj' ? prettyNote(x[0]) + '장조, 밝은 셋째 음과 고른 걸음.' : x[0] + ' 화성 단음계, 꼭대기 밑의 넓은 걸음을 들어 봐요.')] }; };
msHomeAdd('ms-third', 1, 'Major or minor third?', '장3도? 단3도?', 'Four half steps or three.', '반음 4개, 아니면 3개.', msThirdQ);
msHomeAdd('ms-rel', 2, 'The minor key’s key signature', '단조의 조표', 'Three half steps below the major.', '장조에서 반음 세 칸 아래.', msRelQ);
msHomeAdd('ms-har', 3, 'The harmonic minor', '화성 단음계', 'The 7th goes up, beside the note.', '7번째 음을 올려요, 음표 옆에.', msRaiseQ);
msHomeAdd('ms-gaps', 4, 'Tone, semitone, tone and a half', '온음, 반음, 온음 반', 'T S T T S T½ S.', 'T S T T S T½ S.', msGapQ);
msHomeAdd('ms-ear', 5, 'Major or harmonic minor?', '장음계? 화성 단음계?', 'A darker third, a wide step near the top.', '어두운 셋째 음, 꼭대기 밑의 넓은 걸음.', msEarQ);
