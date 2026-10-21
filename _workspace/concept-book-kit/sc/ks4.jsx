
// Keyboard patterns and note names, one section (her order 2026-10-21): black keys in 2s and 3s, low/high direction, the small house C D E, the big house F G A B,
// every key with the same name, middle C, then the 12-key pattern with its 7 names together.
const ksHouse = (small) => { const Ls = small ? ['C', 'D', 'E'] : ['F', 'G', 'A', 'B'], show = small ? 'small' : 'big', house = small ? ['small house', '작은 집'] : ['big house', '큰 집'], nB = small ? 2 : 3;
  const kb = (names, marks) => ({ oct: 2, base: 0, names, marks, tint: true });
  const nm = (arr) => ksNames(2, arr), mk = (arr, st, b) => ksMarks(2, arr.map(L => KS_PC[L]), st, b);
  return {
    title: small ? ['Under 2 black keys: C D E', '검은건반 2개 아래: C D E'] : ['Under 3 black keys: F G A B', '검은건반 3개 아래: F G A B'],
    allLine: small ? ['Under the group of 2 black keys live 3 white keys. Their names are C, D and E.', '검은건반 2개짜리 무리 아래에는 흰건반 3개가 있어요. 이름은 C, D, E예요.']
      : ['Under the group of 3 black keys live 4 white keys. Their names are F, G, A and B.', '검은건반 3개짜리 무리 아래에는 흰건반 4개가 있어요. 이름은 F, G, A, B예요.'],
    fig: () => ({ top: <KpRoofs show={show}/>, kb: kb(nm(Ls), mk(Ls, 'target')) }),
    steps: Ls.map((L, i) => ({ title: [L + ': ' + KS_GUIDE[L][0].replace(/^[A-G] (is|lives) /, '').replace(/\.$/, ''), L + ': ' + KS_GUIDE[L][1].replace(/^[A-G]는 /, '').replace(/ (있어요|살아요)\.$/, '')], line: KS_GUIDE[L], fig: () => ({ top: <KpRoofs show={show}/>, kb: kb(nm(Ls.slice(0, i + 1)), mk(Ls.slice(0, i), 'pass', mk([L], 'target'))) }) })),
    make: () => { const L = ksPick(Ls); return { kind: 'key', retry: true, prompt: ['Tap ' + L + '. Think of the ' + house[0] + ' first.', L + '을 눌러 보세요. 먼저 ' + house[1] + '을 떠올려 봐요.'], fig: () => ({ top: <KpRoofs show={show}/>, kb: kb(null, {}) }), ok: (k) => k % 12 === KS_PC[L],
      yes: KS_GUIDE[L], no: (k) => [(KS_L[k % 12] ? 'That is ' + KS_L[k % 12] + '. ' : 'That is a black key. ') + KS_GUIDE[L][0], (KS_L[k % 12] ? '그건 ' + KS_L[k % 12] + '예요. ' : '그건 검은건반이에요. ') + KS_GUIDE[L][1]] }; },
  }; };
KS_SPEC['kp-small'] = ksHouse(true);
KS_SPEC['kp-big'] = ksHouse(false);
// one pattern is 12 keys with 7 names
const ksBr3n = (hl) => ksBr3(hl);
KS_SPEC['kp-repeat'] = {
  title: ['One pattern: 12 keys, 7 names', '무늬 하나: 건반 12개, 이름 7개'], allLine: ['A pattern is 12 keys: 7 white keys and 5 black keys. The 7 white keys are named C D E F G A B. Then the pattern starts again.', '무늬 하나는 건반 12개예요. 흰건반 7개와 검은건반 5개예요. 흰건반 7개의 이름은 C D E F G A B예요. 그다음 무늬가 다시 시작해요.'],
  fig: () => ({ top: ksBr3(null), kb: { oct: 3, base: 0, names: ksNames(3), marks: ksMarks(3, [0], 'target') } }),
  steps: [
    { title: ['12 keys: 7 white, 5 black', '건반 12개: 흰건반 7, 검은건반 5'], line: ['2 black keys and 3 black keys make 5. With the 7 white keys, that is 12 keys: one pattern.', '검은건반 2개와 3개가 5개예요. 흰건반 7개와 합쳐 12개, 무늬 하나예요.'], fig: () => ({ top: ksBr3(0), kb: { oct: 3, base: 0, marks: ksSpan(0, 11, 'pass') } }) },
    { title: ['7 names: C D E F G A B', '이름 7개: C D E F G A B'], line: ['The white keys of one pattern: C D E F G A B.', '무늬 하나의 흰건반: C D E F G A B.'], fig: () => ({ top: ksBr3(0), kb: { oct: 3, base: 0, names: ksNames(3).constructor === Object ? Object.fromEntries(Object.entries(ksNames(3)).filter(([k]) => k < 12)) : null, marks: ksSpan(0, 11, 'pass') } }) },
    { title: ['Then it starts again', '그리고 다시 시작'], line: ['After B comes C again: the same 7 names in the next pattern, a little higher.', 'B 다음에는 다시 C예요. 다음 무늬에서 같은 이름 7개가 조금 더 높게 되풀이돼요.'], fig: () => ({ top: ksBr3(null), kb: { oct: 3, base: 0, names: ksNames(3), marks: ksMarks(3, [0], 'target') } }) },
  ],
  make: (n) => n % 2 === 0 ? { kind: 'key', retry: true, prompt: ['Tap a key where a new pattern starts. What is its name?', '새 무늬가 시작되는 건반을 눌러 보세요. 이름이 뭘까요?'], fig: () => ({ top: ksBr3(null), kb: { oct: 3, base: 0 } }), ok: (k) => k % 12 === 0,
    yes: ['That key is C, where every pattern starts.', '그 건반은 C예요. 무늬는 모두 C에서 시작해요.'], no: (k) => [([1, 3, 6, 8, 10].includes(k % 12) ? 'That is a black key. ' : 'That is ' + KS_L[k % 12] + ', not the start. ') + 'A pattern starts at C: the white key just left of the group of 2.', ([1, 3, 6, 8, 10].includes(k % 12) ? '그건 검은건반이에요. ' : '그건 ' + KS_L[k % 12] + '예요, 시작이 아니에요. ') + '무늬는 C에서 시작해요: 검은건반 2개짜리 무리의 바로 왼쪽 흰건반이에요.'] }
    : { kind: 'choice', cols: 4, prompt: ['Which name comes after B?', 'B 다음에 오는 이름은?'], opts: ksLet7(), ans: 'C', ok: (v) => v === 'C', fig: () => ({ kb: { oct: 3, base: 0, names: ksNames(3), marks: ksMarks(3, [11], 'pass') } }),
      yes: ['After B the pattern starts again with C.', 'B 다음에는 무늬가 다시 C로 시작해요.'], no: ['After B the pattern starts again with C.', 'B 다음에는 무늬가 다시 C로 시작해요.'] },
};
const KS_ROWS_KEYS = ['p-keys', [
  ['kp-groups', 'Black keys in twos and threes', '검은건반은 두 개, 세 개씩', 'The black keys sit in groups of 2 and 3.', '검은건반은 두 개, 세 개씩 모여 있어요.', () => <KpGroups/>],
  ['kp-hear', 'Low and high', '낮은 소리, 높은 소리', 'Left is low, right is high.', '왼쪽은 낮은 소리, 오른쪽은 높은 소리.', () => <KsEngine spec={KS_SPEC['kp-hear']}/>],
  ['kp-small', 'Under 2 black keys: C D E', '검은건반 2개 아래: C D E', 'The three white keys of the small house.', '작은 집의 흰건반 세 개.', () => <KsEngine spec={KS_SPEC['kp-small']}/>],
  ['kp-big', 'Under 3 black keys: F G A B', '검은건반 3개 아래: F G A B', 'The four white keys of the big house.', '큰 집의 흰건반 네 개.', () => <KsEngine spec={KS_SPEC['kp-big']}/>],
  ['nn-find', 'Every key with the same name', '이름이 같은 건반 모두 찾기', 'The same letter in every pattern.', '무늬마다 있는 같은 글자.', () => <KsEngine spec={KS_SPEC['nn-find']}/>],
  ['kp-middle', 'Middle C', '가운데 도', 'The C in the middle of the keyboard.', '건반 한가운데 있는 C.', () => <KsEngine spec={KS_SPEC['kp-middle']}/>],
  ['kp-repeat', 'One pattern: 12 keys, 7 names', '무늬 하나: 건반 12개, 이름 7개', 'The pattern repeats, with the same 7 names.', '같은 이름 7개와 함께 무늬가 되풀이돼요.', () => <KsEngine spec={KS_SPEC['kp-repeat']}/>],
]];
