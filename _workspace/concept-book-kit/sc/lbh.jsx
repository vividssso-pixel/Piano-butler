// ─── The Lesson Book on the Home (her call 2026-10-24: "Rhythm and Posture: apply the Lesson Book we made before; and put the
// fold of the staff that shows the landmarks in a fitting place"). A Home lesson opens like its book page: the page's title, words
// and picture, its Remember line under the butler; one by one is the page's 'At the piano', one step on each screen, with the
// page's moving picture above it (what the online book showed), then 'Not like this'; your turn is the app's own questions.
// The pages are the book's own (postureLbPages, plLbPages, ...), taken apart, not copied: change the book, the Home follows.
const LBH_FN = { scales: (s) => sscLbPages(s), 'key-signatures': (s) => skgLbPages(s), 'posture-hands': (s) => postureLbPages(s), pulse: (s) => plLbPages(s), 'note-values': (s) => nvLbPages(s), 'time-signatures': (s) => tsLbPages(s), rhythm: (s) => srhLbPages(s), 'whole-staff': (s) => wsLbPages(s) };
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

// ══ Scales and Key signatures (her call 2026-10-24: "the same feel for Scales and Key signatures, and the butler at the bottom") ══
// A lesson with a book page: the page first (the whole picture, the words, At the piano, the butler), then 'On the keys →' opens
// the keyboard lesson the Home already had (its own whole picture, one by one, your turn), with the butler under it.
// A keyboard lesson with no page of its own keeps its screens and gets the butler under it, with its own key sentence.
function LbhBook({ ch, pages, Keys, title }) {
  const [part, setPart] = useState('book');
  const spec = React.useMemo(() => lbhSpec(ch, pages, { title, noTry: true, onLast: () => { setPart('keys'); try { window.scrollTo(0, 0); } catch (e) {} }, lastLabel: ['On the keys →', '건반에서 해 보기 →'] }), []);
  const last = lbhPage(ch, [].concat(pages).slice(-1)[0]);
  if (part === 'keys') return <>
    <div style={{ display: 'flex', justifyContent: 'flex-start', margin: '0 0 8px' }}><button className="ghost-btn" style={{ fontSize: 13, padding: '6px 12px' }} onClick={() => setPart('book')}>{t('← The book page', '← 레슨북 쪽')}</button></div>
    <Keys/>{lbhRem(ch, last.remember)}</>;
  return <KqEngine spec={spec}/>;
}
const LbhKeys = ({ Keys, rem }) => <><Keys/>{lbhRem(null, kqT(rem))}</>;
const lbhSetC = (id, C) => { const tl = TOOLS.find(x => x.id === id); if (tl) tl.C = C; };
const SC_KEYS = { 'sc-shape': ScShape, 'sc-wr': () => <ScWhite hand="RH"/>, 'sc-wl': () => <ScWhite hand="LH"/>, 'sc-deg': ScDeg, 'sc-same': ScSame, 'sc-br': () => <ScBlackHand hand="RH"/>, 'sc-bl': () => <ScBlackHand hand="LH"/>, 'sc-both': ScBoth, 'sc-all': ScAll, 'sc-chrom': ScChrom, 'sc-min': ScMinor };
[['sc-shape', 1], ['sc-wr', 2], ['sc-deg', 3], ['sc-same', [4, 5]]].forEach(([id, pg]) => { const K = SC_KEYS[id]; lbhSetC(id, () => <LbhBook ch="scales" pages={pg} Keys={K} title={id === 'sc-same' ? ['G major and F major', 'G장조와 F장조 음계'] : undefined}/>); });
[['kf-what', 1, 'what']].forEach(([id, pg, only]) => lbhSetC(id, () => <LbhBook ch="key-signatures" pages={pg} Keys={() => <KeyFinder only={only}/>}/>));
// the keyboard lessons with no page of their own: each keeps its screens; the butler says its key sentence (the lesson's own words)
const LBH_REM = {
  'sc-wl': ['The mirror of the right hand: 5 at the bottom, a group of 4, then a group of 3.', '오른손의 거울: 맨 아래 5번, 4개 묶음, 그다음 3개 묶음.'],
  'sc-br': ['The right hand always starts on finger 2.', '오른손은 늘 2번으로 시작해요.'],
  'sc-bl': ['B♭, E♭, A♭, D♭: one shape. The left hand starts on finger 3.', 'B♭, E♭, A♭, D♭는 한 가지 모양. 왼손은 3번으로 시작해요.'],
  'sc-both': ['One column, one note: the right hand on top, the left hand below.', '한 칸에 음 하나: 위는 오른손, 아래는 왼손.'],
  'sc-all': ['One pattern, T T S T T T S, from any of the twelve notes.', '패턴은 하나, T T S T T T S. 열두 음 어디서든 시작해요.'],
  'sc-chrom': ['All twelve keys, one half step at a time.', '열두 건반 모두, 반음씩.'],
  'sc-min': ['Three minors from D: they differ only near the top.', '세 단음계 모두 D에서: 위쪽 한두 음만 달라요.'],
  'sc-penta': ['Pentatonic: the major scale without notes 4 and 7.', '5음 음계: 장음계에서 4번과 7번 음을 빼요.'],
  'kf-sharps': ['Seven sharps, always in this order: Father Charles Goes Down And Ends Battle.', '샵은 일곱 개, 언제나 이 순서: Father Charles Goes Down And Ends Battle.'],
  'kf-flats': ['Seven flats: the order of sharps, backwards.', '플랫 일곱 개: 샵의 순서를 거꾸로.'],
  'kf-msharp': ['Sharps: the last sharp, up a half step, is the key.', '샵: 마지막 샵에서 반음 위가 그 조예요.'],
  'kf-mflat': ['Flats: the second last flat is the key.', '플랫: 뒤에서 두 번째 플랫이 그 조예요.'],
  'kf-minor': ['From the major key, three half steps down: its relative minor.', '장조에서 반음 세 칸 아래: 나란한 단조예요.'],
  'kf-piece': ['Every key in one circle: each step round adds one sharp, or one flat.', '모든 조가 한 바퀴에: 한 칸 갈 때마다 샵이나 플랫이 하나씩 늘어요.'],
  'kf-write': ['Straight after the clef, in their order, each on its own line or space.', '음자리표 바로 뒤에, 정해진 순서대로, 저마다 제 줄이나 칸에.'],
  'kf-trans': ['Every note keeps its number in the scale.', '음마다 음계의 번호는 그대로예요.'],
};
Object.entries(LBH_REM).forEach(([id, rem]) => { const tl = TOOLS.find(x => x.id === id); if (!tl) return; const K = SC_KEYS[id] || tl.C; lbhSetC(id, () => <LbhKeys Keys={K} rem={rem}/>); });
[['sc-shape', 'The major scale', '장음계', 'Whole, whole, half, whole, whole, whole, half.', '온, 온, 반, 온, 온, 온, 반.'], ['sc-wr', 'C major fingering', 'C장조 손가락 번호', 'Thumb under after 3; 3 over after the thumb.', '3번 다음 엄지 밑으로, 엄지 다음 3번 넘기기.'],
 ['sc-deg', 'Scale degrees', '음의 번호', 'Degrees 1 to 8. The tonic is home.', '1부터 8까지. 으뜸음이 집이에요.'], ['sc-same', 'G major and F major', 'G장조와 F장조 음계', 'G major: one sharp, F♯. F major: one flat, B♭.', 'G장조: 샵 하나, F♯. F장조: 플랫 하나, B♭.'],
 ['kf-what', 'The key signature', '조표', 'It changes every note of its letter, for the whole piece.', '이름이 같은 음을 곡 끝까지 모두 바꿔요.']].forEach(r => lbhRetitle(...r));

// the book's other key signature pages, with questions of their own
const lbhSig = (key, clef = 'treble') => <div style={{ maxWidth: 240, margin: '0 auto 6px' }}><PgSigSvg clef={clef} signs={key === 'C' ? [] : pgSigns(key, clef)}/></div>;
const LBH_KS = { G: ['G major', 'G장조', 'F', 'F♯', '♯'], F: ['F major', 'F장조', 'B', 'B♭', '♭'] };
const LBH_LINE = { G: { treble: ['the top line', '맨 윗줄'], bass: ['the fourth line', '넷째 줄'] }, F: { treble: ['the middle line', '가운데 줄'], bass: ['the second line', '둘째 줄'] } };
const lbhGfQ = (n, prev) => { const key = n % 2 === 0 ? 'G' : 'F', K = LBH_KS[key], kind = Math.floor(n / 2) % 3, clef = Math.random() < 0.5 ? 'treble' : 'bass';
  if (kind === 0) { const opts = [['F', 'F♯'], ['C', 'C♯'], ['B', 'B♭'], ['E', 'E♭']], ans = K[3];
    return { kind: 'choice', cols: 2, prompt: ['This is ' + K[0] + '’s key signature. Which note does it change?', K[1] + '의 조표예요. 어떤 음을 바꿀까요?'], opts: opts.map(([, v]) => ({ id: v, label: v })), ans, ok: (v) => v === ans, fig: () => ({ mid: lbhSig(key, clef) }),
      yes: [K[0] + '’s key signature: one ' + (key === 'G' ? 'sharp' : 'flat') + ', ' + ans + '.', K[1] + '의 조표: ' + (key === 'G' ? '샵' : '플랫') + ' 하나, ' + ans + '.'], no: ['It sits on the ' + K[2] + ' line: every ' + K[2] + ' becomes ' + ans + '.', K[2] + ' 줄에 있어요. 모든 ' + ivqJ(K[2], '이', '가') + ' ' + ivqJ(ans, '으로', '로') + ' 바뀌어요.'] }; }
  if (kind === 1) { const L = LBH_LINE[key], ans = clef, cl = clef === 'treble' ? ['treble', '높은음자리표'] : ['bass', '낮은음자리표'], all = [['the top line', '맨 윗줄'], ['the fourth line', '넷째 줄'], ['the middle line', '가운데 줄'], ['the second line', '둘째 줄']], right = L[clef];
    return { kind: 'choice', cols: 2, prompt: ['On the ' + cl[0] + ' staff, where does ' + K[0] + '’s ' + (key === 'G' ? 'sharp' : 'flat') + ' sit?', cl[1] + ' 오선에서 ' + K[1] + '의 ' + (key === 'G' ? '샵' : '플랫') + '은 어디에 있을까요?'], opts: all.map(x => ({ id: x[0], label: () => kqT(x) })), ans: right[0], ok: (v) => v === right[0], fig: (c) => ({ mid: c.res ? lbhSig(key, clef) : lbhSig('C', clef) }),
      yes: ['On ' + right[0] + ': the ' + K[2] + ' line.', ivqJ(right[1], '이에요', '예요') + '. ' + K[2] + ' 줄이에요.'], no: ['It sits on ' + right[0] + ', the ' + K[2] + ' line.', right[1] + ', ' + K[2] + ' 줄에 있어요.'] }; }
  const R = Math.random() < 0.5, f = R ? '4' : '2';
  return { kind: 'choice', cols: 5, prompt: [K[0] + ', ' + (R ? 'right' : 'left') + ' hand' + (key === 'G' ? (R ? ' (1 2 3, thumb under, 1 2 3 4 5)' : ' (5 4 3 2 1, 3 over, 3 2 1)') : (R ? ' (1 2 3 4, thumb under, 1 2 3 4)' : ' (5 4 3 2 1, 3 over, 3 2 1)')) + ': which finger plays ' + K[3] + '?', K[1] + ', ' + (R ? '오른손' : '왼손') + (key === 'G' ? (R ? ' (1 2 3, 엄지 밑으로, 1 2 3 4 5)' : ' (5 4 3 2 1, 3번 넘기기, 3 2 1)') : (R ? ' (1 2 3 4, 엄지 밑으로, 1 2 3 4)' : ' (5 4 3 2 1, 3번 넘기기, 3 2 1)')) + ': ' + ivqJ(K[3], '은', '는') + ' 몇 번 손가락이 칠까요?'],
    opts: ['1', '2', '3', '4', '5'].map(x => ({ id: x, label: x })), ans: f, ok: (v) => v === f, fig: () => ({ mid: lbhSig(key, R ? 'treble' : 'bass') }), yes: ['Finger ' + f + ' plays ' + K[3] + '.', f + '번 손가락이 ' + ivqJ(K[3], '을', '를') + ' 쳐요.'], no: ['Count the fingers along the scale: ' + K[3] + ' falls on finger ' + f + '.', '음계를 따라 손가락을 세어 보세요. ' + ivqJ(K[3], '은', '는') + ' ' + f + '번 손가락이에요.'] }; };
const lbhAccQ = (n) => { const k = n % 4;
  if (k < 2) { const sig = k === 0, ans = sig ? 'p' : 'b';
    return { kind: 'choice', cols: 1, prompt: [sig ? 'How long does a key signature last?' : 'How long does an accidental last?', sig ? '조표는 언제까지 효과가 있을까요?' : '임시표는 언제까지 효과가 있을까요?'], opts: [{ id: 'p', label: () => t('The whole piece', '곡 끝까지') }, { id: 'b', label: () => t('Until the bar line', '세로줄까지') }, { id: 'n', label: () => t('Just that one note', '그 음 하나만') }], ans, ok: (v) => v === ans, fig: () => ({ mid: lbhSig('G') }),
      yes: ['Key signature: the whole piece. Accidental: until the bar line.', '조표는 곡 끝까지, 임시표는 세로줄까지.'], no: ['Key signature: the whole piece, in every octave. Accidental: until the bar line.', '조표는 곡 끝까지, 모든 옥타브에서. 임시표는 세로줄까지예요.'] }; }
  const same = k === 2, ans = same ? 'n' : 's';
  return { kind: 'choice', cols: 2, prompt: [same ? 'The key signature has F♯. A natural ♮ comes before an F. Later in the same bar, an F is…' : 'The key signature has F♯. A natural ♮ came before an F in bar 1. In bar 2, an F is…', same ? '조표에 F♯이 있어요. F 앞에 내추럴 ♮이 붙었어요. 같은 마디에서 뒤에 오는 F는?' : '조표에 F♯이 있어요. 1마디의 F 앞에 내추럴 ♮이 붙었어요. 2마디의 F는?'], opts: [{ id: 's', label: 'F♯' }, { id: 'n', label: 'F ♮' }], ans, ok: (v) => v === ans, fig: () => ({ mid: lbhSig('G') }),
    yes: same ? ['F: the natural lasts until the bar line.', 'F예요. 내추럴은 세로줄까지 효과가 있어요.'] : ['F♯: after the bar line, the key signature holds again.', 'F♯이에요. 세로줄 다음에는 다시 조표대로예요.'], no: same ? ['The natural lasts until the bar line, so it is still F.', '내추럴은 세로줄까지 가니까 아직 F예요.'] : ['After the bar line, the key signature holds again: F♯.', '세로줄 다음에는 다시 조표대로: F♯이에요.'] }; };
const LBH_DB = [['C', 'C', 'C장조'], ['G', 'G', 'G장조'], ['D', 'D', 'D장조'], ['F', 'F', 'F장조'], ['Bb', 'B♭', 'B♭장조']];
const lbhDbQ = (n, prev) => { let i, g = 0; do { i = kqRnd(5); } while (prev && prev.i === i && g++ < 8); const [key, nm] = LBH_DB[i], clef = Math.random() < 0.5 ? 'treble' : 'bass';
  return { i, kind: 'choice', cols: 5, prompt: ['Count the signs. Which major key?', '조표를 세어 보세요. 무슨 장조일까요?'], opts: LBH_DB.map(x => ({ id: x[0], label: x[1] })), ans: key, ok: (v) => v === key, fig: () => ({ mid: lbhSig(key, clef) }),
    yes: [nm + ' major.', LBH_DB[i][2] + '예요.'], no: ['Count the signs: none C; one sharp G, two D; one flat F, two B♭. This is ' + nm + ' major.', '조표를 세어요: 없으면 C, 샵 하나면 G, 둘이면 D, 플랫 하나면 F, 둘이면 B♭. ' + LBH_DB[i][2] + '예요.'] }; };
lbhAdd('kf-gf', 'p-keysig', 'pitch', 'G major and F major', 'G장조와 F장조', 'One sharp, F♯; one flat, B♭.', '샵 하나 F♯, 플랫 하나 B♭.', lbhSpec('key-signatures', [2, 3], { title: ['G major and F major', 'G장조와 F장조'], make: lbhGfQ }));
lbhAdd('kf-acc', 'p-keysig', 'pitch', 'Key signature and accidental', '조표와 임시표', 'The whole piece; until the bar line.', '곡 끝까지, 세로줄까지.', lbhSpec('key-signatures', 4, { make: lbhAccQ }));
lbhAdd('kf-dbb', 'p-keysig', 'pitch', 'D major and B♭ major', 'D장조와 B♭장조', 'Count the signs and name the key.', '조표를 세고 조 이름을 말해요.', lbhSpec('key-signatures', 5, { make: lbhDbQ }));
