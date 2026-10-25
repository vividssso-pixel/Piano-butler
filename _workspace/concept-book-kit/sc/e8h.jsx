
// ══ Build AD: 6/8 time on the Home (Rhythm → The steady beat …, its own group '6/8 time'). Each lesson is the book's page
// (lbhSpec); the questions after it are the page's own: tapped rows (RqStaff, scored) and one look-or-listen question each ══
LBH_FN['six-eight'] = (s) => e8LbPages(s);
const e8HomeAdd = (id, i, en, ko, benEn, bko, make) => lbhAdd(id, 'r-beat', 'rhythm', en, ko, benEn, bko, lbhSpec('six-eight', i, { make }));
const e8TapQ = (key, o = {}) => rqStaffQ(E8[key], { ...e8Props(key), ...o });
const e8Choice = (prompt, opts, ans, fig, yes, no) => ({ kind: 'choice', cols: opts.length > 3 ? 4 : opts.length, prompt, opts: opts.map(([id, l]) => ({ id, label: typeof l === 'function' ? l : () => l })), ans, ok: (v) => v === ans, fig: () => ({ mid: fig }), yes, no });
const e8BigQ = (n) => (n % 2 === 0 ? e8TapQ('big', { only: [0, 3, 6, 9], prompt: ['Tap only the strong beats: 1 and 4.', '센박에서만 쳐요: 1과 4.'] })
  : e8Choice(['In 6/8, which counts are the strong ones?', '6/8에서 센박은 몇째 셈일까요?'], [['1 3', '1, 3'], ['1 4', '1, 4'], ['1 5', '1, 5'], ['3 6', '3, 6']], '1 4', e8El('big', { counts: false }),
    ['1 and 4: the start of each group of three.', '1과 4: 셋씩 묶인 묶음의 첫 음이에요.'], ['The quavers go in threes: the strong ones are 1 and 4.', '8분음표가 셋씩 묶여서, 센박은 1과 4예요.']));
const e8DotQ = (n) => (n % 2 === 0 ? e8TapQ('dot')
  : e8Choice(['In 6/8, how many quavers does a dotted crotchet last?', '6/8에서 점4분음표는 8분음표 몇 개만큼일까요?'], [['1', '1'], ['2', '2'], ['3', '3'], ['6', '6']], '3', <div style={{display:'flex',justifyContent:'center',margin:'4px 0 8px'}}><Glyph item={NV_DOTTED[1]} size={90}/></div>,
    ['Three: one big beat.', '셋: 큰 박 하나.'], ['A crotchet is two quavers; the dot adds one more: three.', '4분음표는 8분음표 둘, 점이 하나를 더해요: 셋.']));
const e8LsQ = (n) => (n % 2 === 0 ? e8TapQ(n % 4 === 0 ? 'ls' : 'ls2')
  : e8Choice(['Long, short: on which counts do the two notes start?', '길게, 짧게: 두 음은 몇째 셈에서 시작할까요?'], [['1 2', '1, 2'], ['1 3', '1, 3'], ['1 4', '1, 4']], '1 3', e8El('ls', { counts: false }),
    ['1 and 3: the crotchet holds through 2.', '1과 3: 4분음표가 2까지 이어져요.'], ['The crotchet lasts two quavers (1 2), so the quaver comes on 3.', '4분음표가 8분음표 둘(1 2)이라서, 8분음표는 3에서 와요.']));
const e8TwoQ = (n) => { const a = Math.random() < 0.5 ? 't34' : 'big', ans = a === 't34' ? '3/4' : '6/8';
  return { kind: 'choice', cols: 2, prompt: ['Listen to the strong clicks: 3/4 or 6/8?', '센 클릭을 들어 봐요: 3/4일까요, 6/8일까요?'], opts: [{ id: '3/4', label: () => t('3/4: three beats', '3/4: 세 박') }, { id: '6/8', label: () => t('6/8: two big beats', '6/8: 큰 박 둘') }], ans, ok: (v) => v === ans,
    play: () => e8Play(a), fig: (c) => ({ mid: c.res ? e8El(a, { hearts: false }) : null }), yes: ans === '3/4' ? ['3/4: strong on every second quaver.', '3/4: 둘째 8분음표마다 센박.'] : ['6/8: strong on every third quaver.', '6/8: 셋째 8분음표마다 센박.'],
    no: ans === '3/4' ? ['It was 3/4: the strong clicks came every two quavers. Press ♪ Again.', '3/4이었어요: 센 클릭이 8분음표 둘마다 왔어요. ♪ 다시를 눌러 보세요.'] : ['It was 6/8: the strong clicks came every three quavers. Press ♪ Again.', '6/8이었어요: 센 클릭이 8분음표 셋마다 왔어요. ♪ 다시를 눌러 보세요.'] }; };
const e8ReadQ = (n) => e8TapQ(E8_READ[n % E8_READ.length]);
e8HomeAdd('e8-big', 1, 'Two big beats', '큰 박 둘', 'Six quavers; 1 and 4 are strong.', '8분음표 여섯, 1과 4가 센박.', e8BigQ);
e8HomeAdd('e8-dot', 2, 'The dotted crotchet', '점4분음표', 'Three quavers: one big beat.', '8분음표 셋: 큰 박 하나.', e8DotQ);
e8HomeAdd('e8-ls', 3, 'Long, short', '길게, 짧게', 'A crotchet and a quaver: 1 (2) 3.', '4분음표와 8분음표: 1 (2) 3.', e8LsQ);
e8HomeAdd('e8-34', 4, '3/4 or 6/8?', '3/4? 6/8?', 'Twos or threes.', '둘씩, 아니면 셋씩.', e8TwoQ);
e8HomeAdd('e8-read', 5, 'Count, clap, play', '세고, 손뼉 치고, 치기', 'New lines in 6/8.', '6/8의 새 줄.', e8ReadQ);
