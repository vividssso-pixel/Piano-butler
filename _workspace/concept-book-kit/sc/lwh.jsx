
// ══ Build AE: Listen, clap, write on the Home (the Aural door, after Listen and sing). Each lesson is the book's page (lbhSpec);
// the questions are heard and tapped, as the page's pads ══
LBH_FN['listen-write'] = (s) => lwLbPages(s);
const lwAdd = (id, i, en, ko, benEn, bko, make) => { const spec = lbhSpec('listen-write', i, { make });
  TOOLS.push({ id, ch: 'concept', title: en, blurb: benEn, hidden: true, get kicker() { return t('Aural', '청음') + ' · ' + t('Listen, clap, write', '듣고, 치고, 적기'); }, C: () => <KqEngine spec={spec}/> });
  lbhRetitle(id, en, ko, benEn, bko); };
const lwTapQ = (Pad, extra, prompt, yes) => (n) => ({ kind: 'tap', retry: true, prompt, ok: (v) => !!(v && v.ok),
  fig: (c) => ({ mid: <Pad key={c.qn} {...extra(n)} onResult={(r) => c.pick(r)}/> }),
  yes: yes || ['Well heard ✓', '잘 들었어요 ✓'], no: () => ['Nearly. Listen again and try once more.', '거의 다 왔어요. 다시 듣고 한 번 더 해 봐요.'] });
const lwMetreQ = (n) => { const m = Math.random() < 0.5 ? 2 : 3;
  return { kind: 'choice', cols: 2, prompt: ['Listen: two or three beats in a bar?', '들어 봐요: 한 마디에 두 박일까요, 세 박일까요?'], opts: [{ id: 2, label: () => t('Two: oom-pah', '두 박: 쿵-짝') }, { id: 3, label: () => t('Three: oom-pah-pah', '세 박: 쿵-짝-짝') }], ans: m, ok: (v) => v === m,
    play: () => lwMetrePlay(m), fig: (c) => ({ mid: c.res ? <PlCircles n={m * 4} r={11} gap={27} group={m} kind={(i) => (i % m === 0 ? 'play' : 'beat')} label={(i) => String(i % m + 1)}/> : null }),
    yes: m === 2 ? ['Oom-pah: two beats.', '쿵-짝: 두 박.'] : ['Oom-pah-pah: three beats.', '쿵-짝-짝: 세 박.'], no: m === 2 ? ['It was oom-pah: two beats. Count from each low note.', '쿵-짝, 두 박이었어요. 낮은 음마다 1부터 세어 봐요.'] : ['It was oom-pah-pah: three beats. Count from each low note.', '쿵-짝-짝, 세 박이었어요. 낮은 음마다 1부터 세어 봐요.'] }; };
lwAdd('lw-home', 1, 'The home note', '집 음', 'The tune stops; hum home, then find it.', '선율이 멈추면 집 음을 흥얼거리고 찾아요.', lwTapQ(LwHomePad, (n) => ({ fixed: { pos: n % 2 ? 'G' : 'C', i: n % LW_HOME.length } }), ['Hear the tune, hum the home note, then find it.', '선율을 듣고, 집 음을 흥얼거린 다음, 찾아요.'], ['Home ✓', '집 ✓']));
lwAdd('lw-metre', 2, 'Two or three?', '두 박? 세 박?', 'Oom-pah or oom-pah-pah.', '쿵-짝, 아니면 쿵-짝-짝.', lwMetreQ);
lwAdd('lw-clap', 3, 'Clap it back', '따라 치기', 'Heard twice, then clapped back.', '두 번 듣고 따라 치기.', lwTapQ(LwClapPad, (n) => ({ fixed: n % LW_CLAP.length }), ['Listen twice, then tap it back with the clicks.', '두 번 듣고, 클릭에 맞춰 따라 쳐요.'], ['Clapped back on time ✓', '제때 따라 쳤어요 ✓']));
lwAdd('lw-phrase', 4, 'Sing it with its rhythm', '리듬까지 따라 부르기', 'Walk, run-ning, hold: sing it, then play it.', '타, 티-티, 길게: 부르고 치기.', lwTapQ(LwPhrasePad, (n) => ({ fixed: n % LW_PH.length }), ['Listen twice, sing it back with its rhythm, then play it.', '두 번 듣고, 리듬까지 따라 부른 다음, 쳐요.'], ['Sung and played ✓', '부르고 쳤어요 ✓']));
lwAdd('lw-write', 5, 'Write the rhythm', '리듬 받아 적기', 'Two bars of crotchets and minims.', '4분음표와 2분음표 두 마디.', lwTapQ(LwWritePad, (n) => ({ fixed: n % LW_DICTS.length }), ['Listen, count the beats, then fill the two bars.', '듣고, 박을 세고, 두 마디를 채워요.'], ['Written right ✓', '맞게 적었어요 ✓']));
