// ─── The Lesson Book on the Home (her call 2026-10-24: "Rhythm and Posture: apply the Lesson Book we made before; and put the
// fold of the staff that shows the landmarks in a fitting place"). A Home lesson opens like its book page: the page's title, words
// and picture, its Remember line under the butler; one by one is the page's 'At the piano', one step on each screen, with the
// page's moving picture above it (what the online book showed), then 'Not like this'; your turn is the app's own questions.
// The pages are the book's own (postureLbPages, plLbPages, ...), taken apart, not copied: change the book, the Home follows.
const LBH_FN = { 'posture-hands': (s) => postureLbPages(s), pulse: (s) => plLbPages(s), 'note-values': (s) => nvLbPages(s), 'time-signatures': (s) => tsLbPages(s), rhythm: (s) => srhLbPages(s), 'whole-staff': (s) => wsLbPages(s) };
const lbhCache = {};
const LBH_KNOWN = () => [LbLive, LbPic, LbSay, LbPiano, LbNot, LbRemember, LbTune, LbDefs, LbStageRows];
const lbhHas = (n) => { let f = false; React.Children.forEach(n, (x) => { if (f || !x || typeof x !== 'object') return; if (LBH_KNOWN().includes(x.type)) f = true; else if (x.props && x.props.children) f = lbhHas(x.props.children); }); return f; };
// a page taken apart: still (the printed picture), live (what moves on screen), say, defs, piano (steps), not, tunes, remember, extra
function lbhParse(pg) {
  const o = { title: pg.props.title, still: null, live: null, say: null, defs: null, piano: [], not: null, tunes: [], remember: null, extra: [] };
  const noTunes = (el) => { if (!el || typeof el !== 'object') return el; if (el.type === LbTune) { o.tunes.push(el); return null; }
    if (el.props && el.props.children && (el.type === React.Fragment || el.type === 'div') && lbhHas(el.props.children)) return React.cloneElement(el, {}, ...React.Children.toArray(el.props.children).map(noTunes)); return el; };
  const visit = (el) => {
    if (!el || typeof el !== 'object') return;
    if (Array.isArray(el)) { el.forEach(visit); return; }
    const ty = el.type;
    if (ty === LbOnly) { if (el.props.screen) visit(el.props.children); return; }
    if (ty === LbLive) { if (!o.still) o.still = noTunes(el.props.still); if (!o.live) o.live = el.props.live; return; }
    if (ty === LbPic) { if (!o.still) o.still = el; else o.extra.push(el); return; }
    if (ty === LbSay) { if (!o.say) o.say = el.props.children; return; }
    if (ty === LbDefs) { o.defs = el; return; }
    if (ty === LbPiano) { o.piano = el.props.steps; return; }
    if (ty === LbNot) { o.not = el.props.items; return; }
    if (ty === LbTune) { o.tunes.push(el); return; }
    if (ty === LbRemember) { o.remember = el.props.children; return; }
    if ((ty === React.Fragment || ty === 'div') && lbhHas(el.props.children)) { React.Children.forEach(el.props.children, visit); return; }
    o.extra.push(el);
  };
  React.Children.forEach(pg.props.children, visit);
  return o;
}
const lbhPage = (ch, i) => { const k = ch + ':' + LANG; if (!lbhCache[k]) lbhCache[k] = LBH_FN[ch](true).map(lbhParse); return lbhCache[k][i]; };
const lbhWrap = (ch, el) => el ? <LbScreenCtx.Provider value={true}><BkChapterCtx.Provider value={ch}><div className="lb-screen" style={{ display: 'flex', flexDirection: 'column', gap: 10, margin: '4px 0 8px', minWidth: 0 }}>{el}</div></BkChapterCtx.Provider></LbScreenCtx.Provider> : null;
// 'Not like this', down the screen: each small picture with its words beside it
const lbhNot = (items) => <div style={{ display: 'flex', flexDirection: 'column', gap: 10, maxWidth: 400, margin: '0 auto' }}>{items.map(([pic, cap], i) => <div key={i} style={{ display: 'flex', alignItems: 'center', gap: 12 }}>
  <span style={{ flex: '0 0 48%', display: 'flex', justifyContent: 'center', minWidth: 0 }}>{pic}</span><span style={{ flex: 1, minWidth: 0, fontSize: 14.5, fontWeight: 800, color: KQ.NV, lineHeight: 1.3 }}><span style={{ color: KQ.CO, fontWeight: 900 }}>✗ </span>{cap}</span></div>)}</div>;
const LBH_AT = ['At the piano', '피아노 앞에서'];
// One focus per screen: each At the piano step shows the page's printed picture; what moves on screen (the online book's tool)
// comes once, last, as 'Try it here'. The butler's Remember line sits under the whole picture (her 2026-10-24: keep the butler
// at the bottom). i: one page, or several in a row (the next page opens with its own picture and words, then its steps).
// o.steps: the lesson's own steps instead of 'At the piano' (a page with none, like the six warm-ups); o.noTry: no 'Try it here';
// o.make: the questions; o.onLast + o.lastLabel: the last step leads on (to the keyboard lesson) instead of to questions
const lbhRem = (ch, rem) => rem ? lbhWrap(ch, <LbRemember>{rem}</LbRemember>) : null;
const lbhSpec = (ch, i, o = {}) => ({
  get title() { if (o.title) return o.title; const p = lbhPage(ch, [].concat(i)[0]); return [p.title, p.title]; },
  get allLine() { const p = lbhPage(ch, [].concat(i)[0]); return [p.say, p.say]; },
  fig: () => { const p = lbhPage(ch, [].concat(i)[0]); return { mid: lbhWrap(ch, <>{p.still || p.live}{p.extra.length ? p.extra : null}</>), below: lbhRem(ch, p.remember) }; },
  onLast: o.onLast, lastLabel: o.lastLabel,
  get steps() { const out = []; [].concat(i).forEach((pi, k) => lbhSteps(ch, pi, k > 0, o).forEach(s => out.push(s))); return out; },
  make: o.make,
});
const lbhSteps = (ch, i, opener, o) => {
    const p = lbhPage(ch, i), n = p.piano.length, pic = p.still || p.live, out = [];
    if (opener) out.push({ title: [p.title, p.title], line: [p.say, p.say], fig: () => ({ mid: lbhWrap(ch, p.still || p.live), below: lbhRem(ch, p.remember) }) });
    if (p.defs) out.push({ title: ['The words', '낱말'], line: [p.title, p.title], fig: () => ({ mid: lbhWrap(ch, p.defs) }) });
    if (o.steps) o.steps.forEach(s => out.push(s));
    else p.piano.forEach((s, j) => out.push({ title: [LBH_AT[0] + (n > 1 ? ' · ' + (j + 1) + '/' + n : ''), LBH_AT[1] + (n > 1 ? ' · ' + (j + 1) + '/' + n : '')], line: [s, s], fig: () => ({ mid: lbhWrap(ch, pic) }) }));
    if (!o.steps && !n && p.tunes.length) p.tunes.forEach((tu) => out.push({ title: [tu.props.name, tu.props.name], line: [tu.props.how, tu.props.how], fig: () => ({ mid: lbhWrap(ch, tu) }) }));
    if (p.not) out.push({ title: ['Not like this', '이렇게는 안 돼요'], line: [p.remember, p.remember], fig: () => ({ mid: lbhWrap(ch, lbhNot(p.not)) }) });
    if (p.live && p.live !== p.still && !o.noTry) out.push({ title: out.length ? ['Try it here', '여기서 해 보기'] : [p.title, p.title], line: [p.remember || p.say, p.remember || p.say], fig: () => ({ mid: lbhWrap(ch, p.live) }) });
    if (!out.length) out.push({ title: [p.title, p.title], line: [p.remember || p.say, p.remember || p.say], fig: () => ({ mid: lbhWrap(ch, pic) }) });
    return out; };
// retitle a Home lesson after its book page (the list on the Home, the lesson's kicker stays)
const lbhRetitle = (id, en, ko, benEn, bko) => { const tl = TOOLS.find(x => x.id === id); if (!tl) return; TOOL_KO[id] = [ko, bko]; tl.titleEn = en; tl.blurbEn = benEn;
  Object.defineProperty(tl, 'title', { get: () => (LANG === 'ko' ? ko : en), enumerable: true, configurable: true });
  Object.defineProperty(tl, 'blurb', { get: () => (LANG === 'ko' ? bko : benEn), enumerable: true, configurable: true }); };
const lbhAdd = (id, concept, area, en, ko, benEn, bko, spec) => {
  TOOLS.push({ id, ch: 'concept', title: en, blurb: benEn, hidden: true, get kicker() { const c = homeCatById(concept); return TOOL_AREAS.find(a => a.id === area).name + ' · ' + (c.name || t(c.en, c.ko)); }, C: () => <KqEngine spec={spec}/> });
  TOOL_CONCEPT[id] = concept; lbhRetitle(id, en, ko, benEn, bko); };

// ══ Posture and hands: the book's chapter 1, page by page ══
// a tiny tune by finger numbers, one circle asked (the others show their numbers)
// (counts: the beat's count under each circle)
const lbhTuneRow = (seq, ask, show, counts) => { const bars = []; seq.forEach((x, i) => { if (x === '|' || !bars.length) bars.push([]); if (x !== '|') bars[bars.length - 1].push(i); });
  return <div style={{ display: 'flex', flexWrap: 'wrap', alignItems: 'flex-start', justifyContent: 'center', columnGap: 14, rowGap: 8, margin: '6px 0 8px' }}>{bars.map((b, bi) => <span key={bi} style={{ display: 'inline-flex', gap: 6, paddingLeft: bi ? 14 : 0, borderLeft: bi ? '1.6px solid rgba(38,41,107,0.5)' : 'none' }}>{b.map((i) => { const x = seq[i]; return <span key={i} style={{ display: 'inline-flex', flexDirection: 'column', alignItems: 'center', gap: 4 }}>{x === '-' ? <span style={{ width: 32, height: 32, boxSizing: 'border-box', borderRadius: 16, border: '1.6px dashed rgba(38,41,107,0.4)' }}/>
  : <span style={{ width: 32, height: 32, boxSizing: 'border-box', borderRadius: 16, background: i === ask ? KQ.CO : '#fff', border: '2px solid ' + (i === ask ? KQ.CO : KQ.NV), display: 'inline-flex', alignItems: 'center', justifyContent: 'center', fontSize: 16, fontWeight: 900, color: i === ask ? '#fff' : KQ.NV }}>{i === ask && !show ? '?' : x}</span>}
    {counts && <span style={{ fontSize: 15, fontWeight: 900, color: i === ask ? KQ.COD : KQ.NV }}>{counts[i]}</span>}</span>; })}</span>)}</div>; };
const LBH_TUNES = [['Hop on 3', '3번으로 깡충', '3 - 3 - | 3 3 3 -'], ['Neighbours', '이웃사촌', '2 3 2 3 | 3 2 3 -'], ['Up and back', '올라갔다 내려오기', '1 2 3 - | 3 2 1 -'], ['Little hill', '작은 언덕', '1 2 3 4 | 3 2 1 -'], ['Stairs and slide', '계단과 미끄럼틀', '1 2 3 4 5 - | 5 4 3 2 1 -']].map(([en, ko, s]) => [en, ko, s.split(' ')]);
const lbhWalkQ = (n, prev) => { let ti, g = 0; do { ti = kqRnd(LBH_TUNES.length); } while (prev && prev.ti === ti && g++ < 8); const [en, ko, seq] = LBH_TUNES[ti];
  if (n % 3 === 2) { const ans = seq.includes('-') ? 'h' : 'n';
    return { ti, kind: 'choice', cols: 1, prompt: ['“' + en + '”: what does an empty dashed circle mean?', '“' + ko + '”: 빈 점선 동그라미는 무슨 뜻일까요?'], opts: [{ id: 'h', label: () => t('Hold the note one more beat', '그 음을 한 박 더 누르고 있어요') }, { id: 'r', label: () => t('Play finger 1', '1번 손가락으로 쳐요') }, { id: 'n', label: () => t('Start again', '처음부터 다시 쳐요') }], ans: 'h', ok: (v) => v === 'h',
      fig: () => ({ mid: lbhTuneRow(seq, -1) }), yes: ['An empty dashed circle: hold the note one more beat.', '빈 점선 동그라미: 그 음을 한 박 더 누르고 있어요.'], no: ['An empty dashed circle: hold the note one more beat. One circle is one steady beat.', '빈 점선 동그라미는 그 음을 한 박 더 누르고 있어요. 동그라미 하나가 일정한 박 하나예요.'] }; }
  const idx = seq.map((x, i) => /\d/.test(x) ? i : -1).filter(i => i >= 0), a = kqPick(idx), f = seq[a];
  return { ti, kind: 'choice', cols: 5, prompt: ['“' + en + '”: which finger plays the coral circle?', '“' + ko + '”: 산호색 동그라미는 몇 번 손가락이 칠까요?'], opts: ['1', '2', '3', '4', '5'].map(x => ({ id: x, label: x })), ans: f, ok: (v) => v === f,
    fig: (c) => ({ mid: lbhTuneRow(seq, a, !!c.res) }), yes: ['Finger ' + f + '.', f + '번 손가락이에요.'], no: ['Read the circles in order: that one is finger ' + f + '.', '동그라미를 차례로 읽어 보세요. 그건 ' + f + '번 손가락이에요.'] }; };
TQ_SPEC['kp-sit'] = lbhSpec('posture-hands', 1, { make: TQ_SPEC['kp-sit'].make });
TQ_SPEC['kp-arm'] = lbhSpec('posture-hands', 2, { steps: TQ_SPEC['kp-arm'].steps, noTry: true, make: TQ_SPEC['kp-arm'].make });
TQ_SPEC['kp-hand'] = lbhSpec('posture-hands', 3, { make: TQ_SPEC['kp-hand'].make });
TQ_SPEC['kp-fingers'] = lbhSpec('posture-hands', 4, { make: TQ_SPEC['kp-fingers'].make });
TQ_SPEC['kp-walks'] = lbhSpec('posture-hands', 5, { make: lbhWalkQ });
TQ_SPEC['kp-check'] = lbhSpec('posture-hands', 6, { make: TQ_SPEC['kp-check'].make });
lbhAdd('kp-walks', 'k-posture', 'tech', 'Finger walks', '손가락 걷기', 'Five tiny tunes: one note, then two, up to five.', '작은 곡 다섯: 한 음부터 다섯 음까지.', TQ_SPEC['kp-walks']);

// ══ Rhythm: the book's chapters Pulse & Counting, Notes & Rests, Time Signatures and Rhythm, page by page ══
// the beat in your fingers: the book's three rows, one finger number on each beat
const LBH_FB = [['Small-house beat', '작은 집 박', '2 3 2 3 | 2 3 2 3'], ['Big-house beat', '큰 집 박', '2 3 4 3 | 2 3 4 3'], ['Left-hand beat', '왼손 박', '3 2 3 2 | 3 2 3 2']].map(([en, ko, s]) => [en, ko, s.split(' ')]);
const lbhFingerBeatQ = (n, prev) => { if (n % 2 === 1) return { ...rqTapQ(RQ_Q8, { listen: false, beats: true, tip: ['Count out loud: 1 2 3 4, 1 2 3 4.', '소리 내어 세요. 1 2 3 4, 1 2 3 4.'] }), prompt: ['Tap all eight beats with the click, counting 1 2 3 4 out loud.', '클릭에 맞춰 여덟 박을 쳐요. 1 2 3 4를 소리 내어 세면서.'], yes: ['Eight beats, all on time.', '여덟 박 모두 제때예요.'] };
  let r, g = 0; do { r = kqRnd(3); } while (prev && prev.r === r && g++ < 8); const [en, ko, seq] = LBH_FB[r], ni = seq.map((x, j) => x === '|' ? -1 : j).filter(j => j >= 0), b = kqPick(ni), f = seq[b], cnt = (ni.indexOf(b) % 4) + 1, counts = seq.map((x, j) => x === '|' ? '' : String(ni.indexOf(j) % 4 + 1));
  return { r, kind: 'choice', cols: 5, prompt: ['“' + en + '”: which finger plays on the coral beat?', '“' + ko + '”: 산호색 박은 몇 번 손가락이 칠까요?'], opts: ['1', '2', '3', '4', '5'].map(x => ({ id: x, label: x })), ans: f, ok: (v) => v === f,
    fig: (c) => ({ mid: lbhTuneRow(seq, b, !!c.res, counts) }), yes: ['Finger ' + f + ', on count ' + cnt + '.', cnt + '에서 ' + f + '번 손가락이에요.'], no: ['Read along the row: count ' + cnt + ' is finger ' + f + '.', '줄을 따라 읽어 보세요. ' + ivqJ(String(cnt), '은', '는') + ' ' + f + '번 손가락이에요.'] }; };
[['rb-beat', 'pulse', 1], ['rb-count', 'pulse', 2], ['rb-silent', 'pulse', 3], ['rb-words', 'pulse', 4], ['rn-q', 'note-values', 1], ['rn-h', 'note-values', 2], ['rn-long', 'note-values', 3], ['rn-p', 'note-values', 4], ['rn-rest', 'note-values', 5],
 ['rt-bars', 'time-signatures', 1], ['rt-ts', 'time-signatures', 2], ['rt-strong', 'time-signatures', 3], ['rt-fill', 'time-signatures', 4], ['rt-tie', 'time-signatures', 5], ['rp-beams', 'rhythm', 1], ['rp-alone', 'rhythm', 2], ['rp-dot', 'rhythm', 3], ['rp-up', 'rhythm', 4], ['rp-read', 'rhythm', 5]]
  .forEach(([id, ch, i]) => { RQ_SPEC[id] = lbhSpec(ch, i, { make: RQ_SPEC[id].make }); });
RQ_SPEC['rb-finger'] = lbhSpec('pulse', 5, { make: lbhFingerBeatQ });
lbhAdd('rb-finger', 'r-beat', 'rhythm', 'The beat in your fingers', '손가락으로 박 치기', 'A new finger on each beat; keep counting.', '박마다 다른 손가락으로, 계속 세면서.', RQ_SPEC['rb-finger']);
[['rb-beat', 'A steady beat', '꾸준한 박', 'The same gap every time.', '매번 똑같은 간격.'], ['rb-count', 'Count out loud', '소리 내어 세기', '1 2 3 4, then 1 again.', '1 2 3 4, 그리고 다시 1.'], ['rb-silent', 'When the notes stop', '음이 멈출 때', 'Silent beats still count.', '조용한 박도 세요.'], ['rb-words', 'Beat or rhythm?', '박일까, 리듬일까?', 'The beat stays steady; the rhythm is on top.', '박은 꾸준하게, 리듬은 그 위의 소리.'],
 ['rn-q', 'The crotchet: one beat', '4분음표: 한 박', 'Walk: one step on each beat.', '타: 박마다 한 걸음.'], ['rn-h', 'The minim: two beats', '2분음표: 두 박', 'Play, then hold.', '치고, 누르고 있어요.'], ['rn-long', 'Longer notes: 3 and 4 beats', '더 긴 음표: 3박과 4박', 'The dotted minim and the semibreve.', '점2분음표와 온음표.'], ['rn-p', 'Two quavers on one beat', '한 박에 8분음표 둘', 'run-ning: 1 +.', '티-티: 1 +.'], ['rn-rest', 'Rests: silence you count', '쉼표: 세면서 쉬어요', 'Count the silence.', '조용히 세요.'],
 ['rt-bars', 'Bars and bar lines', '마디와 세로줄', 'Bar lines make bars; two dots: again.', '세로줄이 마디를 만들어요. 점 두 개: 한 번 더.'], ['rt-ts', 'The two numbers', '두 숫자', 'Top: beats in a bar. Bottom 4: a crotchet.', '위: 한 마디의 박 수. 아래 4: 4분음표.'], ['rt-strong', 'Strong and weak beats', '센박과 여린박', 'Beat 1 is strong.', '1박은 센박.'], ['rt-fill', 'Fill the bar', '마디 채우기', 'Notes and rests fill each bar exactly.', '음표와 쉼표가 마디를 꼭 맞게 채워요.'], ['rt-tie', 'The tie', '붙임줄', 'Play once, hold for both.', '한 번 치고, 두 음표만큼 누르기.'],
 ['rp-beams', 'Grouping quavers', '8분음표 묶기', 'Beams group quavers by the beat.', '빔은 8분음표를 박마다 묶어요.'], ['rp-alone', 'A quaver alone', '혼자 있는 8분음표', 'A flag, and a quaver rest.', '꼬리, 그리고 8분쉼표.'], ['rp-dot', 'The dotted crotchet', '점4분음표', 'Long, short: 1 2 +.', '길게, 짧게: 1 2 +.'], ['rp-up', 'Before beat 1', '첫 박보다 먼저', 'Count the missing beats, then start.', '모자란 박을 세고 시작해요.'], ['rp-read', 'Count, clap, play', '세기, 손뼉 치기, 피아노 치기', 'Count it, clap it, play it.', '세고, 손뼉 치고, 피아노로 쳐요.']]
  .forEach(r => lbhRetitle(...r));

// ══ The fold at Clara's ladder (the book's Line and Space Names, page 5), before the five landmarks ══
// the grand staff with the fold line; o.a: the note asked (coral), o.b: its partner, shown with the dashed curve once answered
const LBH_FOLD = [[32, 24, ['the Queen’s G', '여왕의 G'], ['the King’s F', '왕의 F'], 'F'], [35, 21, ['treble C (the third space)', '높은음자리표 도 (셋째 칸)'], ['bass C (the second space)', '낮은음자리표 도 (둘째 칸)'], 'bC'], [28, 28, ['Clara (middle C)', '클라라 (가운데 도)'], ['Clara (middle C)', '클라라 (가운데 도)'], 'mC']];
const lbhFoldStaff = (a, b, show) => <div style={{ maxWidth: 360, margin: '0 auto' }}><SfStaff clef="grand" width={300} span={[4, 296]} pad={[24, 24]} label={t('The grand staff with the fold line', '접는 선이 있는 큰보표')}
  notes={[{ d: a, x: 140, staff: 'treble', color: PEN_C }].concat(show ? [{ d: b, x: 140, staff: 'bass', color: PEN_C }] : [])}
  extra={(yOf, layer, txt) => { const mid = (yOf(30, 'treble') + yOf(26, 'bass')) / 2;
    return layer === 'under' ? <line x1="4" x2="296" y1={mid} y2={mid} stroke={BK.coral} strokeWidth="1.6" strokeDasharray="6 5"/>
      : <g style={txt}><text x="10" y={mid - 6} fontSize="9" fontWeight="900" fill={BK.coral}>{t('fold here', '여기서 접어요')}</text>
        {show && <path d={`M152 ${yOf(a, 'treble')} Q176 ${mid} 152 ${yOf(b, 'bass')}`} fill="none" stroke={BK.ink} strokeWidth="1.3" strokeDasharray="3 3"/>}</g>; }}/></div>;
const lbhFoldQ = (n, prev) => { const k = n % 4;
  if (k === 3) return { k, kind: 'choice', cols: 2, prompt: ['Folded at Clara’s ladder, a note on a line lands on…', '클라라의 발판에서 접으면, 줄 위의 음은 어디에 닿을까요?'], opts: [{ id: 'l', label: () => t('a line', '줄') }, { id: 's', label: () => t('a space', '칸') }], ans: 'l', ok: (v) => v === 'l',
    fig: () => ({ mid: lbhFoldStaff(32, 24, false) }), yes: ['A line: lines land on lines, spaces on spaces.', '줄이에요. 줄은 줄에, 칸은 칸에 겹쳐요.'], no: ['Lines land on lines, spaces on spaces.', '줄은 줄에, 칸은 칸에 겹쳐요.'] };
  let i, g = 0; do { i = kqRnd(3); } while (prev && prev.i === i && g++ < 8); const [a, b, an, bn, id] = LBH_FOLD[i];
  return { i, k, kind: 'choice', cols: 1, prompt: ['Fold the grand staff at Clara’s ladder. Where does ' + an[0] + ' land?', '큰보표를 클라라의 발판에서 접어요. ' + ivqJ(an[1], '은', '는') + ' 어디에 닿을까요?'],
    opts: LBH_FOLD.map(x => ({ id: x[4], label: () => kqT(x[3]) })), ans: id, ok: (v) => v === id, fig: (c) => ({ mid: lbhFoldStaff(a, b, !!c.res) }),
    yes: id === 'mC' ? ['Clara lands on Clara: middle C sits right on the fold.', '클라라는 클라라에 닿아요. 가운데 도는 접는 선 바로 위에 있어요.'] : [an[0][0].toUpperCase() + an[0].slice(1) + ' lands on ' + bn[0] + '.', an[1] + ' → ' + ivqJ(bn[1], '이에요', '예요') + '.'],
    no: id === 'mC' ? ['Clara lands on Clara: middle C sits right on the fold, its own mirror.', '클라라는 클라라에 닿아요. 가운데 도는 접는 선 바로 위, 자기 자신이 거울이에요.'] : ['Fold at Clara: G meets F, C meets C. ' + an[0][0].toUpperCase() + an[0].slice(1) + ' lands on ' + bn[0] + '.', '클라라에서 접으면 G는 F와, C는 C와 만나요. ' + ivqJ(an[1], '은', '는') + ' ' + bn[1] + '에 닿아요.'] }; };
KQ_SPEC['kq-fold'] = lbhSpec('whole-staff', 4, { make: lbhFoldQ });
lbhAdd('kq-fold', 'p-staff', 'pitch', 'Fold at Clara’s ladder', '클라라의 발판에서 접기', 'G meets F, C meets C.', 'G는 F와, C는 C와 만나요.', KQ_SPEC['kq-fold']);

// ══ Scales and Key signatures (her calls 2026-10-24: "the Lesson Book's design, not its structure"): every lesson keeps its own
// screens, steps and order; it takes on the book's look: its keyboards in the book's picture frame (LbhFrameCtx, read by ScKeys)
// and the butler's Remember line under it -- the book's own line where a book page teaches the same thing, otherwise the
// lesson's own key sentence.
const LbhFrameCtx = React.createContext(false);
const LbhKeys = ({ Keys, rem, frame = true }) => <LbhFrameCtx.Provider value={frame}><Keys/>{lbhRem(null, kqT(rem))}</LbhFrameCtx.Provider>;
// each picture (keyboard, staff, fingering table, the circle of fifths) sits in the book's frame; a picture inside a framed one
// is not framed again, and two pictures one under the other share one frame (CSS: .lbh-fig + .lbh-fig)
const lbhFramed = (C, nm) => function LbhFramed(p) { const f0 = React.useContext(LbhFrameCtx), fr = f0 === true || (Array.isArray(f0) && f0.includes(nm));
  return fr ? <div className="lbh-fig"><LbhFrameCtx.Provider value={false}>{React.createElement(C, p)}</LbhFrameCtx.Provider></div> : React.createElement(C, p); };
ScKeys = lbhFramed(ScKeys, 'ScKeys'); AcKeys = lbhFramed(AcKeys, 'AcKeys'); SkgStaff = lbhFramed(SkgStaff, 'SkgStaff'); KSStaff = lbhFramed(KSStaff, 'KSStaff'); ScPair = lbhFramed(ScPair, 'ScPair'); FifthsRing = lbhFramed(FifthsRing, 'FifthsRing'); TapKeyboard = lbhFramed(TapKeyboard, 'TapKeyboard');
const lbhSetC = (id, C) => { const tl = TOOLS.find(x => x.id === id); if (tl) tl.C = C; };
const LBH_REM = {
  'sc-shape': ['A major scale: T\u00a0T\u00a0S\u00a0T\u00a0T\u00a0T\u00a0S. Whole, whole, half, whole, whole, whole, half.', '장음계: T\u00a0T\u00a0S\u00a0T\u00a0T\u00a0T\u00a0S. 온음, 온음, 반음, 온음, 온음, 온음, 반음.'],
  'sc-same': ['Start anywhere and keep T\u00a0T\u00a0S\u00a0T\u00a0T\u00a0T\u00a0S: a black key comes in to keep the pattern.', '어디서 시작하든 T\u00a0T\u00a0S\u00a0T\u00a0T\u00a0T\u00a0S를 지켜요. 패턴을 지키려고 검은건반이 들어와요.'],
  'sc-deg': ['Degrees 1 to 8. Degree 1, the tonic, is home.', '음의 번호는 1부터 8까지. 1번 음인 으뜸음이 집이에요.'],
  'sc-wr': ['A group of 3, a group of 4, finger 5 on top. Only F has different groups.', '3개 묶음, 4개 묶음, 맨 위는 5번. F만 묶음이 달라요.'],
  'sc-wl': ['5 at the bottom, a group of 4, a group of 3. Only B has different groups.', '맨 아래 5번, 4개 묶음, 3개 묶음. B만 묶음이 달라요.'],
  'sc-br': ['The right hand always starts on finger 2.', '오른손은 늘 2번으로 시작해요.'],
  'sc-bl': ['D♭, E♭, A♭, B♭: one shape. The left hand starts on finger 3.', 'D♭, E♭, A♭, B♭는 한 가지 모양. 왼손은 3번으로 시작해요.'],
  'sc-both': ['One column, one note: the right hand on top, the left hand below.', '한 칸에 음 하나: 위는 오른손, 아래는 왼손.'],
  'sc-all': ['One pattern, T\u00a0T\u00a0S\u00a0T\u00a0T\u00a0T\u00a0S, from any of the twelve notes.', '패턴은 하나, T\u00a0T\u00a0S\u00a0T\u00a0T\u00a0T\u00a0S. 열두 음 어디서든 시작해요.'],
  'sc-chrom': ['All twelve keys, one half step at a time.', '열두 건반 모두, 반음씩.'],
  'sc-min': ['Three minors from D: they differ only near the top.', '세 단음계 모두 D에서: 위쪽 한두 음만 달라요.'],
  'sc-penta': ['Pentatonic: the major scale without notes 4 and 7.', '5음 음계: 장음계에서 4번과 7번 음을 빼요.'],
  'kf-what': ['A key signature changes every note of its letter, for the whole piece.', '조표는 이름이 같은 음을 곡 끝까지 모두 바꿔요.'],
  'kf-sharps': ['Seven sharps, always in this order: Father Charles Goes Down And Ends Battle.', '샵은 일곱 개, 언제나 이 순서: Father Charles Goes Down And Ends Battle.'],
  'kf-flats': ['Seven flats: the order of sharps, backwards.', '플랫 일곱 개: 샵의 순서를 거꾸로.'],
  'kf-msharp': ['Sharps: the last sharp, up a half step, is the key.', '샵: 마지막 샵에서 반음 위가 그 조예요.'],
  'kf-mflat': ['Flats: the second last flat is the key.', '플랫: 뒤에서 두 번째 플랫이 그 조예요.'],
  'kf-minor': ['From the major key, three half steps down: its relative minor.', '장조에서 반음 세 칸 아래: 나란한 단조예요.'],
  'kf-piece': ['Every key in one circle: each step round adds one sharp, or one flat.', '모든 조가 한 바퀴에: 한 칸 갈 때마다 샵이나 플랫이 하나씩 늘어요.'],
  'kf-write': ['Straight after the clef, in their order, each on its own line or space.', '음자리표 바로 뒤에, 정해진 순서대로, 저마다 제 줄이나 칸에.'],
  'kf-trans': ['Every note keeps its number in the scale.', '음마다 음계의 번호는 그대로예요.'],
};
Object.entries(LBH_REM).forEach(([id, rem]) => { const tl = TOOLS.find(x => x.id === id); if (!tl) return; const K = tl.C;
  lbhSetC(id, () => <LbhKeys Keys={K} rem={rem} frame={id === 'kf-piece' ? ['FifthsRing'] : true}/>); });   // the circle of fifths: its two braced staves stay as they are
