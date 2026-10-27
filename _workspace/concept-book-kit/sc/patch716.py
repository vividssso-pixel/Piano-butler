import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)

# Build AW (board call 18, the two Stories steps): Theory of Music Grade 4 general knowledge, in Stories of music. (c) the stringed
# instruments of the symphony orchestra and their tunings, using the appropriate clefs (violin, viola, violoncello, double bass): a
# new Instruments piece, 'Four strings, four clefs'. (b) the form, time, character, texture and other idiomatic features of the dances
# in the keyboard suites of Purcell, Bach and Handel (allemande, courante, corrente, sarabande, gavotte, minuet, gigue): a new
# Composers piece, 'Dances of the Baroque suite'. The tunings, clefs and dance features are the usual textbook ones, from my own
# knowledge: flagged on the board for her to check.

rep("""  'pitch-range': ['spr-zone', 'spr-big', 'spr-fam', 'spr-ladder', 'spr-range',""", """  'pitch-range': ['spr-zone', 'spr-big', 'spr-fam', 'spr-ladder', 'spr-tune', 'spr-range',""")
rep("""  'composers': ['cpx-map', 'cpx-baroque', 'cpx-classical',""", """  'composers': ['cpx-map', 'cpx-baroque', 'cpx-dances', 'cpx-classical',""")
rep("""  set('23', CHAPTER_TOOL_ORDER.composers.concat(CHAPTER_TOOL_ORDER.styles).join(' '));""", """  set('23', CHAPTER_TOOL_ORDER.composers.concat(CHAPTER_TOOL_ORDER.styles).join(' '));
  set('4', 'spr-tune cpx-dances');   // Build AW: Grade 4 general knowledge in Stories of music (after the composers line, which would mark the dances Grades 2-3)""")

HOME = r'''
// ══ Build AW: Grade 4 general knowledge in Stories of music: the violin family's tunings and clefs; the dances of the Baroque suite ══
const SPR_TUNE = [   // the open strings as written, low to high; the double bass sounds an octave lower than written
  { n: 'Violin', clef: 'treble', s: ['G3', 'D4', 'A4', 'E5'], en: 'Four strings tuned in 5ths: G, D, A, E. It reads the treble clef.', ko: '네 줄을 5도씩: G, D, A, E. 높은음자리표를 읽어요.' },
  { n: 'Viola', clef: 'alto', s: ['C3', 'G3', 'D4', 'A4'], en: 'A 5th below the violin: C, G, D, A. It reads the alto clef, the C clef whose middle line is middle C.', ko: '바이올린보다 5도 아래: C, G, D, A. 알토음자리표, 가운데 줄이 가운데 도인 C음자리표를 읽어요.' },
  { n: 'Cello', clef: 'bass', s: ['C2', 'G2', 'D3', 'A3'], en: 'An octave below the viola: C, G, D, A. It reads the bass clef, and the tenor and treble clefs for high notes.', ko: '비올라보다 한 옥타브 아래: C, G, D, A. 낮은음자리표를 읽고, 높은 음은 테너·높은음자리표로.' },
  { n: 'Double bass', clef: 'bass', s: ['E2', 'A2', 'D3', 'G3'], down: 12, en: 'Tuned in 4ths: E, A, D, G. It reads the bass clef and sounds an octave lower than written.', ko: '4도씩: E, A, D, G. 낮은음자리표를 읽고, 적힌 것보다 한 옥타브 낮게 소리 나요.' },
];
const sprTunePlay = (v) => spPlay(v.s.map((x, j) => ({ at: j * 1.1, keys: [h3Semi(h3N(x)) - (v.down || 0)], len: 1.0, vol: 0.16 })), 72);
const sprClefName = (c) => ({ treble: t('treble clef', '높은음자리표'), alto: t('alto clef', '알토음자리표'), bass: t('bass clef', '낮은음자리표') })[c];
function SprTunePad() {
  const [i, setI] = useState(0), [quiz, setQuiz] = useState(null), [pickd, setPick] = useState(null);
  const v = SPR_TUNE[quiz ? quiz.i : i], hide = quiz && pickd == null;
  const ask = () => { let j, g = 0; do { j = Math.floor(Math.random() * 4); } while (quiz && quiz.i === j && g++ < 8); setQuiz({ i: j }); setPick(null); sprTunePlay(SPR_TUNE[j]); };
  return (
    <div className="try-box" style={actBox} data-spr="tune">
      <div style={actTitle}>{t('Four strings, four clefs', '네 줄, 네 음자리표')}</div>
      <div style={actNote}>{t('Each of the violin family has four strings. Tap one to see its open strings on the clef it reads, and hear them.', '바이올린 가족은 모두 줄이 넷. 하나를 눌러, 읽는 음자리표 위의 개방현을 보고 들어 봐요.')}</div>
      {!quiz && spChips(SPR_TUNE.map((x, j) => [j, sprRName(x.n)]), i, (j) => { setI(j); sprTunePlay(SPR_TUNE[j]); })}
      <div style={{textAlign:'center',fontSize:15,fontWeight:900,color:BK.ink,margin:'2px 0 0'}}>{hide ? t('Which instrument?', '어느 악기일까요?') : sprRName(v.n) + ' · ' + sprClefName(v.clef)}</div>
      <div style={{maxWidth:320,margin:'0 auto'}}><IntervalStaff clef={v.clef} notes={v.s.map(h3N)} labels={v.s.map(x => x[0])} width={240}/></div>
      {quiz ? <div style={{display:'grid',gridTemplateColumns:'repeat(2,minmax(0,1fr))',gap:8,marginTop:8}}>{SPR_TUNE.map((x, j) => <button key={j} className={'choice-btn' + (pickd == null ? '' : j === quiz.i ? ' good' : j === pickd ? ' bad' : '')} onClick={() => { if (pickd == null) setPick(j); }} style={{padding:'11px 4px',fontSize:15,fontWeight:900}}>{sprRName(x.n)}</button>)}</div> : null}
      {!hide && spMsg(t(v.en, v.ko), quiz ? (pickd === quiz.i ? BK.green : BK.coral) : undefined)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        <button className="ghost-btn" style={spBtn} onClick={() => sprTunePlay(v)}>{t('▶ The open strings', '▶ 개방현')}</button>
        <button className="ghost-btn" style={spBtn} onClick={ask}>{quiz && pickd == null ? t('▶ Hear it again', '▶ 다시 듣기') : t('▶ Your turn', '▶ 내가 해보기')}</button>
        {quiz && <button className="ghost-btn" style={spBtn} onClick={() => { setQuiz(null); setPick(null); }}>{t('← Back', '← 돌아가기')}</button>}
      </div>
    </div>
  );
}
// the dances: where from, the time, the speed, the character; a rhythm to hear (each bar as the dance often moves)
const BQ_DANCE = [
  { id: 'allemande', en: 'Allemande', ko: '알망드', from: ['German', '독일'], time: '4/4', speed: ['moderate', '보통 빠르기'], line: { items: [['ts', 4], ['s4'], ['s4'], ['p'], ['q'], ['|'], ['p'], ['s4'], ['h'], ['||']], bpm: 66 },
    say: ['Flowing, often in running semiquavers; it often begins with a short upbeat and usually opens the suite.', '흐르듯이, 흔히 이어지는 16분음표로; 짧은 못갖춘마디로 시작하는 일이 많고, 대개 모음곡의 첫 춤곡.'] },
  { id: 'courante', en: 'Courante', ko: '쿠랑트', from: ['French', '프랑스'], time: '3/2', speed: ['moderate', '보통 빠르기'], line: { items: [['ts', 3, 2], ['h'], ['q'], ['q'], ['h'], ['|'], ['hd'], ['q'], ['h'], ['||']], unit: 2, clicks: 3, bpm: 100, so: { countStep: 1, heartStep: 2, countFn: (p) => rq22Count(p) } },
    say: ['A "running" dance in triple time, its beats shifting between 3/2 and 6/4 (hemiola).', '세박자의 "달리는" 춤곡, 박이 3/2와 6/4 사이를 오가요(헤미올라).'] },
  { id: 'corrente', en: 'Corrente', ko: '코렌테', from: ['Italian', '이탈리아'], time: '3/4', speed: ['quick', '빠르게'], line: { items: [['ts', 3], ['p'], ['p'], ['p'], ['|'], ['p'], ['p'], ['q'], ['|'], ['p'], ['p'], ['p'], ['|'], ['hd'], ['||']], bpm: 132 },
    say: ['The Italian courante: quicker and lighter, with running quavers.', '이탈리아식 쿠랑트: 더 빠르고 가볍게, 이어지는 8분음표.'] },
  { id: 'sarabande', en: 'Sarabande', ko: '사라방드', from: ['Spanish', '스페인'], time: '3/4', speed: ['slow', '느리게'], line: { items: [['ts', 3], ['q'], ['h'], ['|'], ['q'], ['qd'], ['e'], ['|'], ['q'], ['h'], ['|'], ['hd'], ['||']], bpm: 58 },
    say: ['Slow and stately; the weight often falls on the second beat of the bar.', '느리고 위엄 있게; 무게가 흔히 마디의 둘째 박에 실려요.'] },
  { id: 'gavotte', en: 'Gavotte', ko: '가보트', from: ['French', '프랑스'], time: '4/4', speed: ['moderate', '보통 빠르기'], line: { items: [['ts', 4], ['q'], ['q'], ['|'], ['h'], ['q'], ['q'], ['|'], ['qd'], ['e'], ['q'], ['q'], ['|'], ['h'], ['||']], from: 2, bpm: 92 },
    say: ['Lively but even; it begins halfway through the bar, with a two-crotchet upbeat.', '경쾌하지만 고르게; 마디의 중간에서, 4분음표 둘의 못갖춘마디로 시작해요.'] },
  { id: 'minuet', en: 'Minuet', ko: '미뉴에트', from: ['French', '프랑스'], time: '3/4', speed: ['moderate', '보통 빠르기'], line: { items: [['ts', 3], ['q'], ['q'], ['q'], ['|'], ['h'], ['q'], ['|'], ['p'], ['p'], ['q'], ['|'], ['hd'], ['||']], bpm: 108 },
    say: ['Elegant, in even crotchets; often two minuets in a pair, the first played again after the second.', '우아하게, 고른 4분음표; 흔히 미뉴에트 둘이 짝을 이루고, 둘째 다음에 첫째를 다시 쳐요.'] },
  { id: 'gigue', en: 'Gigue', ko: '지그', from: ['English (the jig)', '영국(지그)'], time: '6/8', speed: ['quick', '빠르게'], line: { items: [['ts', 6, 8], ['q'], ['e'], ['q'], ['e'], ['|'], ['e3'], ['e3'], ['|'], ['q'], ['e'], ['qd'], ['|'], ['hd'], ['||']], unit: 0.5, clicks: 6, accentAt: [0, 3], bpm: 84, so: { D: 44, countStep: 0.5, heartStep: 1.5, countFn: r2Cmp(6) } },
    say: ['Lively, in compound time (6/8 or 12/8); often one voice imitates another; usually the last dance.', '활기차게, 겹박자(6/8이나 12/8); 흔히 한 성부가 다른 성부를 흉내 내요; 대개 마지막 춤곡.'] },
];
const bqFacts = (d) => t(d.from[0] + ' · ' + d.time + ' · ' + d.speed[0], d.from[1] + ' · ' + d.time + ' · ' + d.speed[1]);
function CpxDancePad() {
  const [i, setI] = useState(0), [quiz, setQuiz] = useState(null), [pickd, setPick] = useState(null);
  const d = BQ_DANCE[quiz ? quiz.i : i], L = d.line, hide = quiz && pickd == null;
  const ask = () => { let j, g = 0; do { j = Math.floor(Math.random() * BQ_DANCE.length); } while (quiz && quiz.i === j && g++ < 8); const others = shuffle(BQ_DANCE.map((_, k) => k).filter(k => k !== j)).slice(0, 3); setQuiz({ i: j, opts: shuffle([j, ...others]) }); setPick(null); };
  return (
    <div className="try-box" style={actBox} data-cpx="dances">
      <div style={actTitle}>{t('Dances of the Baroque suite', '바로크 모음곡의 춤곡')}</div>
      <div style={actNote}>{t('Purcell, Bach and Handel wrote keyboard suites: a set of dances, all in one key. Each dance is in binary form, two halves, each repeated; the first half ends in a new key (the dominant, or the relative major), the second comes home. The texture is often two voices in counterpoint.', '퍼셀, 바흐, 헨델은 건반 모음곡을 썼어요: 모두 한 조로 된 춤곡 모음. 춤곡마다 두도막 형식, 두 부분을 각각 반복; 앞부분은 새 조(딸림조, 또는 나란한 장조)에서 끝나고, 뒷부분이 집으로 돌아와요. 짜임은 흔히 대위법의 두 성부.')}</div>
      {!quiz && spChips(BQ_DANCE.map((x, j) => [j, t(x.en, x.ko)]), i, (j) => setI(j))}
      <div style={{textAlign:'center',margin:'4px 0 2px'}}>{hide ? <div style={{fontFamily:LB_SERIF,fontSize:22,fontWeight:900,color:BK.ink}}>{t('Which dance?', '어떤 춤곡일까요?')}</div> : <div style={{fontFamily:LB_SERIF,fontSize:26,fontWeight:900,color:BK.ink}}>{t(d.en, d.ko)}</div>}
        <div style={{fontSize:13,fontWeight:800,color:BK.coral,marginTop:2}}>{hide ? d.time + ' · ' + t(d.speed[0], d.speed[1]) : bqFacts(d)}</div></div>
      <div style={{fontSize:14,color:BK.ink,textAlign:'center',lineHeight:1.45,margin:'4px 0 6px',textWrap:'balance'}}>{t(d.say[0], d.say[1])}</div>
      <RqStaff key={d.id + (quiz ? 'q' : '')} items={L.items} from={L.from || 0} unit={L.unit} clicks={L.clicks} accentAt={L.accentAt} accent={!!L.accentAt} bpm={L.bpm} so={L.so || {}} tap={false}/>
      {quiz && <div style={{display:'grid',gridTemplateColumns:'repeat(2,minmax(0,1fr))',gap:8,marginTop:8}}>{quiz.opts.map(j => <button key={j} className={'choice-btn' + (pickd == null ? '' : j === quiz.i ? ' good' : j === pickd ? ' bad' : '')} onClick={() => { if (pickd == null) setPick(j); }} style={{padding:'11px 4px',fontSize:15,fontWeight:900}}>{t(BQ_DANCE[j].en, BQ_DANCE[j].ko)}</button>)}</div>}
      {quiz && pickd != null && spMsg(pickd === quiz.i ? t('Yes: the ' + d.en.toLowerCase() + '.', '맞아요: ' + d.ko + '.') : t('It was the ' + d.en.toLowerCase() + ': ' + bqFacts(d) + '.', d.ko + '였어요: ' + bqFacts(d) + '.'), pickd === quiz.i ? BK.green : BK.coral)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        <button className="ghost-btn" style={spBtn} onClick={ask}>{quiz && pickd == null ? t('▶ Another', '▶ 다른 것') : t('▶ Your turn', '▶ 내가 해보기')}</button>
        {quiz && <button className="ghost-btn" style={spBtn} onClick={() => { setQuiz(null); setPick(null); }}>{t('← All the dances', '← 모든 춤곡')}</button>}
      </div>
    </div>
  );
}
TOOLS.push({ id: 'spr-tune', ch: 'pitch-range', title: 'Four strings, four clefs', blurb: 'The violin family’s tunings, and the clefs they read.', C: () => <SprTunePad/> },
  { id: 'cpx-dances', ch: 'composers', title: 'Dances of the Baroque suite', blurb: 'Allemande, courante, sarabande, gavotte, minuet, gigue: their time and character.', C: () => <CpxDancePad/> });
lbhRetitle('spr-tune', 'Four strings, four clefs', '네 줄, 네 음자리표', 'The violin family’s tunings, and the clefs they read.', '바이올린 가족의 조율과 읽는 음자리표.');
lbhRetitle('cpx-dances', 'Dances of the Baroque suite', '바로크 모음곡의 춤곡', 'Allemande, courante, sarabande, gavotte, minuet, gigue: their time and character.', '알망드, 쿠랑트, 사라방드, 가보트, 미뉴에트, 지그: 박자와 성격.');
Object.assign(TOOL_META, { 'spr-tune': ['about', 0, 3, 'show ear'], 'cpx-dances': ['about', 0, 3, 'show ear'] });
Object.assign(TOOL_CONCEPT, { 'spr-tune': 'about', 'cpx-dances': 'about' });
'''
rep("""
lbhAdd('rb-finger', 'r-beat', 'rhythm', 'The beat in your fingers'""", HOME + """
lbhAdd('rb-finger', 'r-beat', 'rhythm', 'The beat in your fingers'""")
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
