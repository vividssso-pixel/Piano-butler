import sys,re
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:90],s.count(a)); s=s.replace(a,b)
# ---- 1. the levels: the six that follow the lessons first, then the useful extras (old numbers kept)
a=s.index("const SKG_LEVELS = ["); b=s.index("];",a)+2
s=s[:a]+"""const SKG_LEVELS = [   // Phase 533: the first six follow the Home lessons (new numbers 11-16); the extras keep their old numbers
  { n: 11, label: 'The order: which is the Nth sharp or flat?', short: ['Order', '순서'], kind: 'kn-order', time: 8, noPrint: true },
  { n: 12, label: 'Sharp keys: name the major key', short: ['Sharp keys', '샵 조'], kind: 'kn-majS', time: 9, noPrint: true },
  { n: 13, label: 'Flat keys: name the major key', short: ['Flat keys', '플랫 조'], kind: 'kn-majF', time: 9, noPrint: true },
  { n: 14, label: 'All 15 keys: name the major key', short: ['All 15', '15개 조'], kind: 'kn-maj15', time: 9, noPrint: true },
  { n: 15, label: 'Relative minor: name the minor key', short: ['Relative minor', '나란한 단조'], kind: 'kn-min', time: 11, noPrint: true },
  { n: 16, label: 'The last note: which key is the piece in?', short: ['Last note', '끝음'], kind: 'kn-last', time: 12, noPrint: true },
  { n: 2, label: 'Which notes change?', short: ['Signs that change', '바뀌는 음'], extra: true, extraStart: true, kind: 'which', time: 9 },
  { n: 3, label: 'Name the coral note', short: ['Coral note', '산호색 음'], extra: true, kind: 'note', time: 10 },
  { n: 4, label: 'Key signature and accidental', short: ['Accidentals', '임시표'], extra: true, kind: 'acc', time: 12 },
  { n: 6, label: 'Which is written right?', short: ['Written right', '바른 조표'], extra: true, kind: 'write', time: 12 },
  { n: 7, label: 'Listen: right or wrong?', short: ['Listen', '듣기'], extra: true, kind: 'ear', time: 14, noPrint: true },
  { n: 8, label: 'The bass staff', short: ['Bass staff', '낮은음자리'], extra: true, kind: 'bass', time: 11 },
  { n: 10, label: 'My keys: name the key', short: ['My keys', '나의 조'], extra: true, kind: 'mykeys', time: 10 },
];"""+s[b:]
rep("  'Extra: three sharps or flats': '더 해 보기: 샤프나 플랫 셋', 'My keys: name the key': '나의 조: 조 이름 맞히기',\n});",
"""  'Extra: three sharps or flats': '더 해 보기: 샤프나 플랫 셋', 'My keys: name the key': '나의 조: 조 이름 맞히기',
  'The order: which is the Nth sharp or flat?': '순서: N번째 샵이나 플랫은?', 'Sharp keys: name the major key': '샵 조: 장조 이름 맞히기', 'Flat keys: name the major key': '플랫 조: 장조 이름 맞히기',
  'All 15 keys: name the major key': '15개 조: 장조 이름 맞히기', 'Relative minor: name the minor key': '나란한 단조: 단조 이름 맞히기', 'The last note: which key is the piece in?': '끝나는 음: 곡의 조는?',
});""")
# ---- 2. the chips say what they cover
rep("""                {concept.levels.map(l => (
                  <button key={l.n} className={'chip' + (l.n === lv.n ? ' active' : '')} onClick={() => onChange({ level: l.n })}
                    title={lvName(l.label)}>{t('Level ', '레벨 ')}{l.n}</button>
                ))}""",
"""                {concept.levels.map(l => (
                  <React.Fragment key={l.n}>
                    {l.extraStart && <div style={{flexBasis:'100%',fontSize:12,fontWeight:800,letterSpacing:'0.06em',textTransform:'uppercase',color:'var(--muted)',margin:'6px 0 0'}}>{t('More practice', '더 연습')}</div>}
                    <button className={'chip' + (l.n === lv.n ? ' active' : '')} onClick={() => onChange({ level: l.n })}
                      title={lvName(l.label)}>{l.short ? t(l.short[0], l.short[1]) : <>{t('Level ', '레벨 ')}{l.n}</>}</button>
                  </React.Fragment>
                ))}""")
rep("              {t('Level ', '레벨 ')}{lv.n} · {lvName(lv.label)} ·","              {lv.short ? '' : <>{t('Level ', '레벨 ')}{lv.n} · </>}{lvName(lv.label)} ·")
# ---- 3. the new questions
rep("function genSkgQuestion(lv, prev) {\n  if (lv.kind === 'mykeys') return genMyKeySigQ(prev);",
"""const KN_STEP = { E: 0, F: 1, G: 2, A: 3, B: 4, C: 5, D: 6 };   // a letter's place on the treble staff, bottom line = 0
function genKnQuestion(lv, prev) {   // Phase 533: the questions that follow the Home lessons (all 15 key signatures)
  const uid = Math.random(), kind = lv.kind;
  const nm = (k, which) => which === 'minor' ? minName(k) : majName(k);
  if (kind === 'kn-order') {
    const type = Math.random() < 0.5 ? 'sharp' : 'flat', order = type === 'sharp' ? SHARP_ORDER : FLAT_ORDER;
    let i = Math.floor(Math.random() * 7), g = 0;
    while (prev && prev.key === 'o' + type + i && g++ < 12) i = Math.floor(Math.random() * 7);
    const answer = order[i];
    return { kind, key: 'o' + type + i, type, idx: i, answer, choices: shuffle([answer, ...sampleN(order, 3, [answer])]), uid };
  }
  const pool = kind === 'kn-majS' ? KEY_SIGS.filter(x => x.type === 'sharp') : kind === 'kn-majF' ? KEY_SIGS.filter(x => x.type === 'flat') : KEY_SIGS;
  let k = pick(pool), g = 0;
  while (prev && prev.key === 'k' + k.major && g++ < 12) k = pick(pool);
  const near = (list) => list.filter(x => x !== k);
  const same = near(pool).filter(x => x.type === k.type || !k.type || !x.type);
  const others = (f) => sampleN(same.length >= 3 ? same : near(pool), 3).map(f);
  if (kind === 'kn-min') return { kind, key: 'k' + k.major, k, answer: minName(k), choices: shuffle([minName(k), ...others(minName)]), uid };
  if (kind === 'kn-last') {
    const which = Math.random() < 0.5 ? 'major' : 'minor', note = which === 'major' ? k.major : k.minor, letter = note[0];
    const step = KN_STEP[letter] + (KN_STEP[letter] <= 3 && Math.random() < 0.5 ? 7 : 0);
    const answer = nm(k, which), trap = nm(k, which === 'major' ? 'minor' : 'major');
    const ch = [...new Set([answer, trap, ...sampleN(same.length >= 2 ? same : near(pool), 2).map(x => nm(x, Math.random() < 0.5 ? 'major' : 'minor'))])].slice(0, 4);
    if (!ch.includes(answer)) ch[0] = answer;
    return { kind, key: 'k' + k.major + which, k, note, step, which, answer, choices: shuffle(ch), uid };
  }
  return { kind, key: 'k' + k.major, k, answer: majName(k), choices: shuffle([majName(k), ...others(majName)]), uid };
}
function genSkgQuestion(lv, prev) {
  if (lv.kind && lv.kind.indexOf('kn-') === 0) return genKnQuestion(lv, prev);
  if (lv.kind === 'mykeys') return genMyKeySigQ(prev);""")
rep("const SkgQuestionAll = (p) => p.q && p.q.kind === 'mykeys' ? <MyKeySigQuestion {...p}/> : <SkgQuestion {...p}/>;",
"""function KnQuestion({ q, given, locked, onAnswer, pixel }) {
  const board = useBoard(q, given);
  const done = !!given, ink = pixel ? '#faf6ec' : '#26296b', btnCls = pixel ? 'pixel-choice' : 'choice-btn';
  const st = (c) => !done ? '' : (String(c) === String(q.answer) ? ' good' : (String(given.ans) === String(c) ? ' bad' : ''));
  const prompt = (txt) => <p style={pixel ? {fontSize:11.5,textAlign:'center',margin:'0 0 10px',lineHeight:1.7} : {fontSize:17,fontWeight:900,textAlign:'center',margin:'0 0 10px',color:'var(--text)',textWrap:'balance',wordBreak:'keep-all'}}>{txt}</p>;
  const paper = (node, mw = 240) => <div style={{background:'#fff',borderRadius:pixel ? 0 : 8,padding:pixel ? 4 : '4px 0',margin:'0 auto 10px',maxWidth:mw}}>{node}</div>;
  let top;
  if (q.kind === 'kn-order') {
    const sym = q.type === 'sharp' ? t(' sharp', ' 샵') : t(' flat', ' 플랫');
    top = <>{prompt(t('The ' + ORDINALS[q.idx] + sym + ' is…', (q.idx + 1) + '번째' + sym + '은…'))}
      {done ? paper(<KSStaff count={q.idx + 1} type={q.type} ink={ink} upto={q.idx} width={170}/>) : <div style={{height:8}}/>}</>;
  } else if (q.kind === 'kn-min') {
    top = <>{prompt(t('Which minor key has this key signature?', '이 조표는 어떤 단조일까요?'))}{paper(<KSStaff count={q.k.count} type={q.k.type} ink={ink} width={170}/>)}</>;
  } else if (q.kind === 'kn-last') {
    top = <>{prompt(t('The piece ends on this note. Which key is it in?', '곡이 이 음으로 끝나요. 어떤 조일까요?'))}
      {paper(<KSStaff count={q.k.count} type={q.k.type} ink={ink} width={200} tonicPos={q.step}/>, 280)}
      <div style={{textAlign:'center',fontSize:15,fontWeight:800,color:'var(--muted)',margin:'-4px 0 10px'}}>{t('Last note: ', '마지막 음: ')}<b style={{color:'var(--text)'}}>{prettyNote(q.note)}</b></div></>;
  } else {
    top = <>{prompt(t('Which major key has this key signature?', '이 조표는 어떤 장조일까요?'))}{paper(<KSStaff count={q.k.count} type={q.k.type} ink={ink} width={170}/>)}</>;
  }
  return <div><BoardTrack b={board} pixel={pixel}/>{top}
    <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:8,marginTop:8}}>{q.choices.map(c => <button key={c} disabled={locked} onClick={() => onAnswer(c)} className={btnCls + st(c)} style={{padding:'14px 6px',minHeight:44}}>{q.kind === 'kn-order' ? prettyNote(c) : c}</button>)}</div></div>;
}
const SkgQuestionAll = (p) => p.q && p.q.kind === 'mykeys' ? <MyKeySigQuestion {...p}/> : p.q && p.q.kind && p.q.kind.indexOf('kn-') === 0 ? <KnQuestion {...p}/> : <SkgQuestion {...p}/>;""")
rep("function skgAnswerLabel(q) {\n  if (q.kind === 'mykeys') return myKeySigLabel(q);",
"""function skgAnswerLabel(q) {
  if (q.kind === 'mykeys') return myKeySigLabel(q);
  if (q.kind === 'kn-order') return prettyNote(q.answer);
  if (q.kind === 'kn-min') return majName(q.k) + ' → ' + q.answer;
  if (q.kind === 'kn-last') return q.answer + t(' (the last note is the key note)', ' (마지막 음이 그 조의 음이에요)');
  if (q.kind && q.kind.indexOf('kn-') === 0) return q.answer + ' (' + sigLabel(q.k) + ')';""")
open(sys.argv[2],'w',encoding='utf-8').write(s);print('ok')
