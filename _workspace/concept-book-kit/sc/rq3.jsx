// ─── Rhythm on the Home, part 3: more rhythm. Counting as the app already has it: 1 e + a (semiquavers), 1 trip let
// (triplets), 6/8 counted in quavers 1 2 3 4 5 6, grouped in threes, 1 and 4 strongest (her way, Phase 464), 2/2 in minims.
const rqTripCount = (pos) => { const w = Math.floor(pos + 1e-6), f = pos - w; return f < 1e-6 ? String(w + 1) : Math.abs(f - 1 / 3) < 0.02 ? 'trip' : Math.abs(f - 2 / 3) < 0.02 ? 'let' : Math.abs(f - 0.5) < 1e-6 ? '+' : ''; };
const rq68Count = (pos) => String(Math.round(pos / 0.5) % 6 + 1);
const rq22Count = (pos) => Math.abs(pos % 2) < 1e-6 ? String(pos / 2 + 1) : '+';
const RQ_MORE = {
  semi: { items: [['ts', 4], ['s4'], ['s4'], ['q'], ['q'], ['||']] },
  semiB: { items: [['ts', 4], ['q'], ['s4'], ['p'], ['q'], ['||']] },
  trip: { items: [['ts', 4], ['t3'], ['q'], ['t3'], ['q'], ['||']], so: { countFn: rqTripCount } },
  tripB: { items: [['ts', 4], ['q'], ['t3'], ['p'], ['q'], ['||']], so: { countFn: rqTripCount } },
  pairs: { items: [['ts', 4], ['p'], ['q'], ['p'], ['q'], ['||']] },
  e68: { items: [['ts', 6, 8], ['e3'], ['e3'], ['|'], ['qd'], ['qd'], ['||']], unit: 0.5, clicks: 6, accentAt: [0, 3], bpm: 54, so: { countStep: 0.5, heartStep: 0.5, countFn: rq68Count } },
  e68B: { items: [['ts', 6, 8], ['q'], ['e'], ['q'], ['e'], ['|'], ['qd'], ['e3'], ['||']], unit: 0.5, clicks: 6, accentAt: [0, 3], bpm: 54, so: { countStep: 0.5, heartStep: 0.5, countFn: rq68Count } },
  cut: { items: [['ts', 2, 2], ['h'], ['h'], ['|'], ['w'], ['||']], unit: 2, clicks: 2, bpm: 96, so: { countStep: 1, heartStep: 2, countFn: rq22Count } },
  cutB: { items: [['ts', 2, 2], ['q'], ['q'], ['h'], ['|'], ['h'], ['h'], ['||']], unit: 2, clicks: 2, bpm: 96, so: { countStep: 1, heartStep: 2, countFn: rq22Count } },
  sync: { items: [['ts', 4], ['e'], ['q'], ['e'], ['q'], ['q'], ['||']] },
  syncB: { items: [['ts', 4], ['q'], ['e'], ['q'], ['e'], ['h'], ['||']] },
  plain: { items: [['ts', 4], ['q'], ['q'], ['q'], ['q'], ['||']] },
  swing: { items: [['ts', 4], ['p'], ['p'], ['p'], ['p'], ['||']] },
};
const rqMoreProps = (key, extra = {}) => { const R = RQ_MORE[key]; return { items: R.items, unit: R.unit, clicks: R.clicks, accentAt: R.accentAt, accent: !!R.accentAt, bpm: R.bpm, so: R.so, ...extra }; };
const rqMoreEl = (key, o = {}) => { const R = RQ_MORE[key]; return rqStaffEl(R.items, { ...(R.so || {}), ...o }); };
const rqMorePlay = (key, o = {}) => { const R = RQ_MORE[key]; return rqRunS(R.items, { unit: R.unit, clicks: R.clicks, accentAt: R.accentAt, accent: !!R.accentAt, bpm: R.bpm, ...o }); };
const rqMoreHear = (keys, i) => ({ kind: 'choice', cols: 1, prompt: ['Listen: which line was it?', '들어 보세요. 어느 줄이었을까요?'], opts: keys.map((k, j) => ({ id: String(j), label: () => <div style={{ width: '100%', minWidth: 0 }}>{rqMoreEl(k, { counts: false, hearts: false })}</div> })), ans: String(i), ok: (v) => v === String(i),
  play: () => rqMorePlay(keys[i]), fig: () => ({ mid: null }), yes: ['That is the one.', '바로 그거예요.'], no: ['Listen again and count along.', '다시 들으면서 함께 세어 보세요.'] });
const rqMoreLesson = (o) => ({ title: o.title, allLine: o.allLine, fig: () => ({ mid: <RqStaff {...rqMoreProps(o.rows[0])}/> }),
  steps: o.steps.map(s => ({ title: s[0], line: s[1], fig: () => s[2] === 'fn' ? s[3]() : ({ mid: <RqStaff {...rqMoreProps(s[2])} tap={s[3] !== false}/> }) })),
  make: (n, prev) => { const k = n % 3; let i, g = 0; do { i = kqRnd(o.rows.length); } while (prev && prev.i === i && o.rows.length > 1 && g++ < 8); const key = o.rows[i], R = RQ_MORE[key];
    if (k === 0 && !o.noTap) return { i, ...rqStaffQ(R.items, { unit: R.unit, clicks: R.clicks, accentAt: R.accentAt, accent: !!R.accentAt, bpm: R.bpm, so: R.so }) };
    if (k === 1 || o.noTap && k === 0) return { i, ...o.ask(n) };
    if (!o.hear || o.hear.length < 2) return { i, ...o.ask(n) };
    const j = kqRnd(o.hear.length); return { i, ...rqMoreHear(o.hear, j) }; } });

RQ_SPEC['rm-semi'] = rqMoreLesson({ title: ['Semiquavers', '16분음표'], allLine: ['Four semiquavers share one beat, joined by two beams. Count them 1 e + a.', '16분음표 넷이 한 박을 나눠요. 빔 두 개로 묶어요. 1 e + a로 세요.'],
  rows: ['semi', 'semiB'], hear: ['semi', 'semiB', 'pairs'],
  steps: [[['Four on one beat', '한 박에 넷'], ['1 e + a: four even sounds in the time of one crotchet.', '1 e + a: 4분음표 하나의 시간에 고른 소리 넷.'], 'semi', false], [['Mix them', '섞어 보기'], ['Crotchet, semiquavers, quavers, crotchet: 1, 2 e + a, 3 +, 4.', '4분음표, 16분음표, 8분음표, 4분음표: 1, 2 e + a, 3 +, 4.'], 'semiB']],
  ask: () => ({ kind: 'choice', cols: 4, prompt: ['How many semiquavers make one crotchet beat?', '16분음표 몇 개가 4분음표 한 박이 될까요?'], opts: ['2', '3', '4', '8'].map(x => ({ id: x, label: x })), ans: '4', ok: (v) => v === '4', fig: () => ({ mid: rqMoreEl('semi') }),
    yes: ['Four: 1 e + a.', '넷이에요. 1 e + a.'], no: ['Two quavers make a beat, and each quaver is two semiquavers: four.', '8분음표 둘이 한 박이고, 8분음표 하나는 16분음표 둘이에요. 그래서 넷이에요.'] }) });
RQ_SPEC['rm-trip'] = rqMoreLesson({ title: ['Triplets', '셋잇단음표'], allLine: ['A triplet fits three quavers into one beat, where two would normally go. A small 3 sits over the beam. Count 1 trip let.', '셋잇단음표는 보통 둘이 들어가는 한 박에 8분음표 셋을 넣어요. 빔 위에 작은 3이 있어요. 1 trip let으로 세요.'],
  rows: ['trip', 'tripB'], hear: ['trip', 'tripB', 'pairs'],
  steps: [[['Three in one beat', '한 박에 셋'], ['1 trip let: three even sounds, then a crotchet.', '1 trip let: 고른 소리 셋, 그다음 4분음표.'], 'trip', false], [['Two or three?', '둘일까, 셋일까?'], ['Quavers split a beat in two; a triplet splits it in three.', '8분음표는 한 박을 둘로, 셋잇단음표는 셋으로 나눠요.'], 'tripB']],
  ask: () => { const three = Math.random() < 0.5; return { kind: 'choice', cols: 2, prompt: ['Listen: two notes or three on each beat?', '들어 보세요. 한 박에 음이 둘일까요, 셋일까요?'], opts: [{ id: '2', label: () => t('Two: quavers', '둘: 8분음표') }, { id: '3', label: () => t('Three: a triplet', '셋: 셋잇단음표') }], ans: three ? '3' : '2', ok: (v) => v === (three ? '3' : '2'),
    play: () => rqMorePlay(three ? 'trip' : 'pairs'), fig: (c) => ({ mid: c.res ? rqMoreEl(three ? 'trip' : 'pairs') : null }), yes: three ? ['Three to a beat: 1 trip let.', '한 박에 셋: 1 trip let.'] : ['Two to a beat: 1 +.', '한 박에 둘: 1 +.'], no: three ? ['It was three to a beat, a triplet. Press ♪ Again.', '한 박에 셋, 셋잇단음표였어요. ♪ 다시를 눌러 보세요.'] : ['It was two to a beat: plain quavers. Press ♪ Again.', '한 박에 둘, 8분음표였어요. ♪ 다시를 눌러 보세요.'] }; } });
RQ_SPEC['rm-68'] = rqMoreLesson({ title: ['6/8 time', '6/8박자'], allLine: ['6/8: six quavers in a bar. Count every quaver, 1 2 3 4 5 6, grouped in threes: 1 and 4 are the strongest.', '6/8: 한 마디에 8분음표 여섯. 8분음표마다 1 2 3 4 5 6으로 세고, 셋씩 묶어요. 1과 4가 가장 세요.'],
  rows: ['e68', 'e68B'], hear: ['e68', 'e68B'],
  steps: [[['Six quavers', '8분음표 여섯'], ['Two groups of three: 1 2 3, 4 5 6. Listen for the stronger 1 and 4.', '셋씩 두 묶음: 1 2 3, 4 5 6. 더 센 1과 4를 들어 보세요.'], 'e68', false], [['Long and short', '길고 짧게'], ['A crotchet lasts two quavers, a dotted crotchet three: 1 (2) 3, 4 (5) 6.', '4분음표는 8분음표 둘, 점4분음표는 셋이에요. 1 (2) 3, 4 (5) 6.'], 'e68B']],
  ask: (n) => n % 2 ? ({ kind: 'choice', cols: 2, prompt: ['In 6/8, which counts are the strongest?', '6/8에서 가장 센 셈은?'], opts: ['1 and 3', '1 and 4', '1 and 5', '3 and 6'].map(x => ({ id: x, label: x.replace('and', LANG === 'ko' ? '과' : 'and') })), ans: '1 and 4', ok: (v) => v === '1 and 4', fig: () => ({ mid: rqMoreEl('e68') }),
    yes: ['1 and 4: the start of each group of three.', '1과 4: 셋씩 묶인 묶음의 첫 음이에요.'], no: ['The quavers go in threes, so the strong ones start each group: 1 and 4.', '8분음표가 셋씩 묶여서, 묶음의 첫 음이 세요. 1과 4예요.'] })
    : ({ kind: 'choice', cols: 4, prompt: ['How many quavers are in a bar of 6/8?', '6/8 한 마디에 8분음표가 몇 개 들어갈까요?'], opts: ['3', '4', '6', '8'].map(x => ({ id: x, label: x })), ans: '6', ok: (v) => v === '6', fig: () => ({ mid: rqMoreEl('e68', { counts: false }) }),
      yes: ['Six: the top number.', '여섯이에요. 위의 숫자예요.'], no: ['The top number is 6 and the bottom 8 means quavers: six quavers.', '위의 숫자가 6, 아래의 8은 8분음표라는 뜻이에요. 8분음표 여섯이에요.'] }) });
RQ_SPEC['rm-cut'] = rqMoreLesson({ title: ['2/2: cut time', '2/2박자'], allLine: ['In 2/2 the minim is the beat: two minim beats in a bar. The same notes as 4/4, felt in two. It is also written as a C with a line through it.', '2/2에서는 2분음표가 한 박이에요. 한 마디에 2분음표 두 박. 4/4와 같은 음표를 둘로 느껴요. 세로선이 그어진 C로도 써요.'],
  rows: ['cut', 'cutB'], hear: ['cut', 'cutB'],
  steps: [[['The minim beat', '2분음표 박'], ['Two clicks a bar, one on each minim: 1, 2.', '한 마디에 클릭 둘, 2분음표마다 하나: 1, 2.'], 'cut', false], [['Crotchets in 2/2', '2/2의 4분음표'], ['Crotchets are half a beat now: 1 + 2.', '이제 4분음표는 반 박이에요: 1 + 2.'], 'cutB']],
  ask: () => ({ kind: 'choice', cols: 2, prompt: ['In 2/2, which note gets one beat?', '2/2에서 한 박인 음표는?'], opts: [['crotchet', NV_NOTES[2]], ['minim', NV_NOTES[1]], ['semibreve', NV_NOTES[0]], ['quaver', NV_NOTES[3]]].map(([x, g]) => ({ id: x, label: () => <Glyph item={g} size={46}/> })), ans: 'minim', ok: (v) => v === 'minim', fig: () => ({ mid: rqMoreEl('cut') }),
    yes: ['The minim: the bottom 2 means minim beats.', '2분음표예요. 아래의 2는 2분음표 박이라는 뜻이에요.'], no: ['The bottom number 2 means the minim is the beat.', '아래의 숫자 2는 2분음표가 한 박이라는 뜻이에요.'] }) });
RQ_SPEC['rm-sync'] = rqMoreLesson({ title: ['Syncopation', '당김음'], allLine: ['Syncopation puts a long note off the beat: short, long, short. The long one starts on a +, between the beats.', '당김음은 긴 음을 박과 박 사이에 놓아요. 짧게, 길게, 짧게. 긴 음이 박 사이의 + 에서 시작해요.'],
  rows: ['sync', 'syncB'], hear: ['sync', 'syncB', 'plain'],
  steps: [[['Short, long, short', '짧게, 길게, 짧게'], ['1, then the long note on 1 +, held through beat 2, then 2 +.', '1, 그다음 1 + 에서 긴 음을 2박까지 누르고, 그다음 2 +.'], 'sync', false], [['Tap it', '쳐 보기'], ['Count every + out loud; the long note starts on one.', '+ 를 모두 소리 내어 세요. 긴 음은 + 에서 시작해요.'], 'sync']],
  ask: () => ({ kind: 'choice', cols: 4, prompt: ['On which count does the long note start?', '긴 음은 어느 셈에서 시작할까요?'], opts: ['1', '1 +', '2', '2 +'].map(x => ({ id: x, label: x })), ans: '1 +', ok: (v) => v === '1 +', fig: (c) => ({ mid: rqMoreEl('sync', { counts: c.res ? undefined : false }) }),
    yes: ['On 1 +: off the beat, so it sounds pushed.', '1 + 에서요. 박에서 벗어나서 앞으로 당겨진 느낌이에요.'], no: ['The quaver takes 1, so the long note starts half a beat later, on 1 +.', '8분음표가 1을 차지하니까, 긴 음은 반 박 뒤 1 + 에서 시작해요.'] }) });
const rqSwingBtns = () => <div style={{ display: 'flex', gap: 6, justifyContent: 'center', flexWrap: 'wrap', margin: '0 0 8px' }}><button className="ghost-btn" onClick={() => rqMorePlay('swing')}>{t('▶ Straight', '▶ 스트레이트')}</button><button className="ghost-btn" onClick={() => rqMorePlay('swing', { swing: true })}>{t('▶ Swing', '▶ 스윙')}</button></div>;
RQ_SPEC['rm-swing'] = rqMoreLesson({ title: ['Straight or swing?', '스트레이트? 스윙?'], allLine: ['The same written quavers can be played even (straight) or long-short (swing). Jazz and blues often swing.', '같은 8분음표를 고르게(스트레이트) 칠 수도, 길게-짧게(스윙) 칠 수도 있어요. 재즈와 블루스는 스윙으로 치는 일이 많아요.'],
  rows: ['swing'], hear: null, noTap: true,
  steps: [[['Straight', '스트레이트'], ['Even quavers: 1 + 2 + 3 + 4 +, every gap the same.', '고른 8분음표: 1 + 2 + 3 + 4 +, 간격이 모두 같아요.'], 'swing', false], [['Swing', '스윙'], ['The first of each pair longer, the second shorter: a lilt. Listen to both.', '짝마다 첫 음은 길게, 둘째 음은 짧게. 흔들리는 느낌이에요. 둘 다 들어 보세요.'], 'fn', () => ({ mid: <>{rqMoreEl('swing')}{rqSwingBtns()}</> })]],
  ask: () => { const sw = Math.random() < 0.5; return { kind: 'choice', cols: 2, prompt: ['Listen: straight or swing?', '들어 보세요. 스트레이트일까요, 스윙일까요?'], opts: [{ id: 's', label: () => t('Straight', '스트레이트') }, { id: 'w', label: () => t('Swing', '스윙') }], ans: sw ? 'w' : 's', ok: (v) => v === (sw ? 'w' : 's'),
    play: () => rqMorePlay('swing', { swing: sw }), fig: () => ({ mid: rqMoreEl('swing') }), yes: sw ? ['Swing: long, short, long, short.', '스윙이에요. 길게, 짧게, 길게, 짧게.'] : ['Straight: all even.', '스트레이트예요. 모두 고르게.'], no: sw ? ['It swung: each pair long-short. Press ♪ Again.', '스윙이었어요. 짝마다 길게-짧게. ♪ 다시를 눌러 보세요.'] : ['It was straight: every quaver even. Press ♪ Again.', '스트레이트였어요. 8분음표가 모두 고르게. ♪ 다시를 눌러 보세요.'] }; } });

const RQ_ROWS3 = [
  ['rm-semi', 'Semiquavers', '16분음표', 'Four on a beat: 1 e + a.', '한 박에 넷: 1 e + a.'],
  ['rm-trip', 'Triplets', '셋잇단음표', 'Three in one beat: 1 trip let.', '한 박에 셋: 1 trip let.'],
  ['rm-68', '6/8 time', '6/8박자', 'Six quavers, in two groups of three.', '8분음표 여섯, 셋씩 두 묶음.'],
  ['rm-cut', '2/2: cut time', '2/2박자', 'The minim is the beat.', '2분음표가 한 박.'],
  ['rm-sync', 'Syncopation', '당김음', 'A long note off the beat.', '박 사이의 긴 음.'],
  ['rm-swing', 'Straight or swing?', '스트레이트? 스윙?', 'Even quavers, or long-short.', '고른 8분음표, 또는 길게-짧게.'],
];
RQ_ROWS3.forEach(([id, en, ko, benEn, bko]) => {
  TOOLS.push({ id, ch: 'concept', title: en, blurb: benEn, hidden: true, get kicker() { return TOOL_AREAS.find(a => a.id === 'rhythm').name + ' · ' + homeCatById('r-beat').name; }, C: () => <KqEngine spec={RQ_SPEC[id]}/> });
  TOOL_KO[id] = [ko, bko];
  const tl = TOOLS[TOOLS.length - 1], k = TOOL_KO[id], ti = tl.title, bl = tl.blurb; tl.titleEn = ti; tl.blurbEn = bl;
  Object.defineProperty(tl, 'title', { get: () => (LANG === 'ko' ? k[0] : ti), enumerable: true, configurable: true });
  Object.defineProperty(tl, 'blurb', { get: () => (LANG === 'ko' ? k[1] : bl), enumerable: true, configurable: true });
  TOOL_CONCEPT[id] = 'r-beat';
});
