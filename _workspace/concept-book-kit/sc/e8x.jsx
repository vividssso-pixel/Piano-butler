
// ─── Chapter: 6/8 Time (Build AD, 2026-10-26; the syllabus check's finding 2: 6/8 is Grade 1, so it comes down to Prelim – Grade 1) ───
// Six quavers in a bar, felt as two big beats of three: counted 1 2 3 4 5 6, 1 and 4 the strong ones; the dotted crotchet is one
// big beat; a crotchet and a quaver make long-short inside it; 3/4 and 6/8 hold the same six quavers, grouped 2 2 2 or 3 3; then
// lines to count, clap and play. The rows are the rhythm chapter's (srhRaw, RqStaff): quavers as the counted unit (unit 0.5).
const E8 = {
  big: [['ts', 6, 8], ['e3'], ['e3'], ['|'], ['e3'], ['e3'], ['||']],
  dot: [['ts', 6, 8], ['qd'], ['qd'], ['|'], ['e3'], ['qd'], ['||']],
  ls: [['ts', 6, 8], ['q'], ['e'], ['q'], ['e'], ['|'], ['qd'], ['e3'], ['||']],
  ls2: [['ts', 6, 8], ['q'], ['e'], ['e3'], ['|'], ['q'], ['e'], ['qd'], ['||']],
  m1: [['ts', 6, 8], ['e3'], ['q'], ['e'], ['|'], ['qd'], ['qd'], ['||']],
  m2: [['ts', 6, 8], ['qd'], ['e3'], ['|'], ['q'], ['e'], ['q'], ['e'], ['||']],
  m3: [['ts', 6, 8], ['e3'], ['e3'], ['|'], ['hd'], ['||']],
  t34: [['ts', 3], ['p'], ['p'], ['p'], ['|'], ['p'], ['p'], ['p'], ['||']],
};
const E8_READ = ['m1', 'ls2', 'm2', 'm3'];
const E8P = { unit: 0.5, clicks: 6, accentAt: [0, 3], accent: true, bpm: 54, so: { countStep: 0.5, heartStep: 1.5, countFn: (p) => rq68Count(p) } };   // rq68Count is defined further down the file
const E8P34 = { accent: true, bpm: 72 };
const e8Props = (key) => (key === 't34' ? E8P34 : E8P);
const e8El = (key, o = {}) => rqStaffEl(E8[key], { ...(key === 't34' ? {} : E8P.so), ...o });
const e8Play = (key) => rqRunS(E8[key], { ...e8Props(key) });
const e8Btn = { padding:'10px 14px', fontSize:14, minHeight:44 };
const e8Msg = (txt, col) => <div style={{textAlign:'center',fontSize:15,fontWeight:900,color:col || 'var(--navy)',minHeight:22,lineHeight:1.35,textWrap:'balance'}}>{txt}</div>;
const e8Box = (title, note, body, tag) => <div className="try-box" style={actBox} data-e8={tag}><div style={actTitle}>{title}</div><div style={actNote}>{note}</div>{body}</div>;
// a note and the quavers it lasts: = and the quavers drawn as small beamed groups
const e8Eq = (glyph, n) => <div style={{display:'flex',alignItems:'center',justifyContent:'center',gap:10,margin:'4px 0 8px'}}><Glyph item={glyph} size={56}/><span style={{fontSize:22,fontWeight:900,color:BK.ink}}>=</span>
  <span style={{display:'inline-flex',gap:3}}>{Array.from({ length: n }, (_, i) => <Glyph key={i} item={NV_NOTES[3]} size={40}/>)}</span><span style={{fontSize:15,fontWeight:900,color:BK.coral}}>{t(n + (n === 1 ? ' quaver' : ' quavers'), '8분음표 ' + n)}</span></div>;

function E8BigPad() {
  return e8Box(t('Two big beats', '큰 박 둘'), LANG === 'ko' ? <>8분음표 여섯을 <b>1 2 3 4 5 6</b>으로 세요. 셋씩 묶여서 <b>1과 4가 센박</b>: 큰 박 둘이에요(하트). 먼저 듣고, 그다음 센박에서만 쳐요.</> : <>Count the six quavers <b>1 2 3 4 5 6</b>. They go in threes, so <b>1 and 4 are strong</b>: two big beats (the hearts). Listen first, then tap only the strong beats.</>,
    <RqStaff items={E8.big} {...E8P} only={[0, 3, 6, 9]}/>, 'big');
}
function E8DotPad() {
  return e8Box(t('The dotted crotchet', '점4분음표'), LANG === 'ko' ? <>점4분음표 하나가 <b>8분음표 셋</b>, 곧 <b>큰 박 하나</b>예요. 1 (2 3), 4 (5 6): 누르고 있는 동안 속으로 세어요.</> : <>One dotted crotchet lasts <b>three quavers</b>: <b>one big beat</b>. 1 (2 3), 4 (5 6): keep counting inside while you hold it.</>,
    <>{e8Eq(NV_DOTTED[1], 3)}<RqStaff items={E8.dot} {...E8P}/></>, 'dot');
}
function E8LsPad() {
  return e8Box(t('Long, short', '길게, 짧게'), LANG === 'ko' ? <>큰 박 하나를 <b>4분음표(8분음표 둘)와 8분음표 하나</b>로 나눠요: 길게, 짧게. 1 (2) 3, 4 (5) 6.</> : <>Split one big beat into <b>a crotchet (two quavers) and a quaver</b>: long, short. 1 (2) 3, 4 (5) 6.</>,
    <>{e8Eq(NV_NOTES[2], 2)}<RqStaff items={E8.ls} {...E8P}/></>, 'ls');
}
// 3/4 or 6/8: the same six quavers, grouped 2 2 2 (three beats) or 3 3 (two big beats); heard by where the strong clicks fall
function E8TwoPad({ onResult }) {
  const [mys, setMys] = useState(null), [ans, setAns] = useState(null), [run, setRun] = useState(0);
  const fresh = () => { const k = Math.random() < 0.5 ? 't34' : 'big'; setMys(k); setAns(null); e8Play(k); };
  const say = (c) => { if (!mys || ans) return; setAns(c); const ok = c === mys; setRun(n => (ok ? n + 1 : 0)); if (onResult) onResult({ ok }); };
  const row = (key, lab) => <div><div style={{fontSize:13,fontWeight:900,color:key === 'big' ? BK.coral : BK.ink,textAlign:'center'}}>{lab}</div>{e8El(key)}</div>;
  return e8Box(t('3/4 or 6/8?', '3/4? 6/8?'), LANG === 'ko' ? <>둘 다 한 마디에 8분음표 여섯. <b>3/4</b>는 둘씩 묶어 <b>세 박</b>, <b>6/8</b>은 셋씩 묶어 <b>큰 박 둘</b>. 센 클릭이 어디 오는지 들어 봐요.</> : <>Both hold six quavers in a bar. <b>3/4</b> groups them in twos: <b>three beats</b>. <b>6/8</b> in threes: <b>two big beats</b>. Listen for where the strong clicks fall.</>,
    <>{row('t34', t('3/4: three beats, 2 2 2', '3/4: 세 박, 2 2 2'))}{row('big', t('6/8: two big beats, 3 3', '6/8: 큰 박 둘, 3 3'))}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        <button className="ghost-btn" style={e8Btn} onClick={() => { setMys(null); setAns(null); e8Play('t34'); }}>{t('▶ 3/4', '▶ 3/4')}</button>
        <button className="ghost-btn" style={e8Btn} onClick={() => { setMys(null); setAns(null); e8Play('big'); }}>{t('▶ 6/8', '▶ 6/8')}</button>
        <button className="ghost-btn" style={e8Btn} onClick={fresh}>{t('▶ Which one?', '▶ 어느 쪽?')}</button>
        {mys && <button className="ghost-btn" style={e8Btn} onClick={() => e8Play(mys)}>{t('♪ Again', '♪ 다시')}</button>}
      </div>
      {mys && <div style={{display:'grid',gridTemplateColumns:'repeat(2,1fr)',gap:8,marginTop:10}}>{[['t34', t('3/4: three beats', '3/4: 세 박')], ['big', t('6/8: two big beats', '6/8: 큰 박 둘')]].map(([id, lab]) => <button key={id} className={'choice-btn' + (!ans ? '' : id === mys ? ' good' : id === ans ? ' bad' : '')} onClick={() => say(id)} style={{padding:'12px 4px',fontSize:15,fontWeight:900}}>{lab}</button>)}</div>}
      {ans && e8Msg(ans === mys ? t('Yes! ' + (run > 1 ? run + ' in a row.' : ''), '맞아요! ' + (run > 1 ? run + '번 연속.' : '')) : t('Count the clicks between the strong ones: two quavers each (3/4), or three (6/8).', '센 클릭 사이의 클릭을 세어 봐요: 둘씩(3/4)인지, 셋씩(6/8)인지.'), ans === mys ? BK.green : BK.coral)}</>, 'two');
}
function E8ReadPad() {
  const [k, setK] = useState(E8_READ[0]);
  return e8Box(t('Count, clap, play', '세고, 손뼉 치고, 치기'), LANG === 'ko' ? <>새 줄: 먼저 음표마다 셈(1~6)을 찾아 소리 내어 말하고, 손뼉 치고, 그다음 쳐요.</> : <>A new line: find each note's count (1 to 6), say it out loud, clap it, then tap it.</>,
    <>{spChips(E8_READ.map((x, i) => [x, t('Line ' + (i + 1), (i + 1) + '번 줄')]), k, setK)}<RqStaff key={k} items={E8[k]} {...E8P}/></>, 'read');
}

// ── the pictures on paper ──
const e8PicBig = () => ({ shapes: [{ k: 'raw', svg: [0, 1, 2, 3, 4, 5].map(i => lsCircleSvg(8 + i * 13 + (i > 2 ? 4 : 0), 22, 5.5, i === 0 || i === 3 ? 'play' : 'beat', String(i + 1))).join('') }], vb: [0, 0, 84, 44] });
const e8PicDot = () => ({ shapes: [{ k: 'raw', svg: '<ellipse cx="18" cy="30" rx="6" ry="4.4" fill="#26296b" transform="rotate(-22 18 30)"/><line x1="23.6" x2="23.6" y1="29" y2="8" stroke="#26296b" stroke-width="1.8"/><circle cx="30" cy="31" r="2.2" fill="#26296b"/><text x="56" y="31" text-anchor="middle" font-family="Inter, sans-serif" font-size="12" font-weight="900" fill="#e4572e">= 3</text>' }], vb: [0, 0, 80, 44] });
const e8PicLs = () => ({ shapes: [{ k: 'raw', svg: '<rect x="8" y="18" width="34" height="8" rx="4" fill="#26296b"/><rect x="46" y="18" width="16" height="8" rx="4" fill="#e4572e"/>' }], vb: [0, 0, 70, 44] });
const e8PicTwo = () => ({ shapes: [{ k: 'raw', svg: '<text x="20" y="28" text-anchor="middle" font-family="Playfair Display, Georgia, serif" font-size="15" font-weight="900" fill="#26296b">3/4</text><text x="40" y="28" text-anchor="middle" font-family="Inter, sans-serif" font-size="11" font-weight="900" fill="#6d6f9c">or</text><text x="60" y="28" text-anchor="middle" font-family="Playfair Display, Georgia, serif" font-size="15" font-weight="900" fill="#e4572e">6/8</text>' }], vb: [0, 0, 80, 44] });
const e8PicRead = () => ({ shapes: [{ k: 'raw', svg: [1, 2, 3, 4, 5, 6].map((n, i) => '<text x="' + (8 + i * 12) + '" y="28" text-anchor="middle" font-family="Inter, sans-serif" font-size="12" font-weight="900" fill="' + (n === 1 || n === 4 ? '#e4572e' : '#26296b') + '">' + n + '</text>').join('') }], vb: [0, 0, 80, 44] });

function e8LbPages(scr = false) {
  const ch = 'six-eight';
  const checks5 = [[e8PicBig(), t('I count 6/8 in six and feel two big beats, 1 and 4', '6/8을 여섯으로 세고 큰 박 둘(1과 4)을 느껴요')], [e8PicDot(), t('I hold a dotted crotchet for one big beat', '점4분음표를 큰 박 하나만큼 눌러요')],
    [e8PicLs(), t('I play long-short: a crotchet and a quaver', '길게-짧게를 쳐요: 4분음표와 8분음표')], [e8PicTwo(), t('I tell 3/4 from 6/8, by eye and by ear', '3/4과 6/8을 눈과 귀로 구별해요')], [e8PicRead(), t('I count, clap and play a new line in 6/8', '6/8의 새 줄을 세고, 손뼉 치고, 쳐요')]];
  const pen = (x) => <PenArt shapes={x.shapes} vb={x.vb} style={{width:90}}/>;
  const toc = [[t('Two big beats', '큰 박 둘'), 2], [t('The dotted crotchet', '점4분음표'), 3], [t('Long, short', '길게, 짧게'), 4], [t('3/4 or 6/8?', '3/4? 6/8?'), 5], [t('Count, clap, play', '세고, 손뼉 치고, 치기'), 6], [t('My five checks', '나의 다섯 가지 확인'), 7]];
  const still = (key, mw = 560) => <LbPic h={150}><div style={{width:'100%',maxWidth:mw,margin:'0 auto'}}>{e8El(key)}</div></LbPic>;
  return [
    <LbPage key="1" no={1} chId={ch} teacher={<>{t('6/8 is a Grade 1 time signature (with or without an anacrusis). Count every quaver (1 2 3 4 5 6) while learning, and feel the two big beats (1 and 4) once it is easy: the clicks here are quavers, the strong click on 1 and 4. Chapter ' + bkChapterNo('time-signatures') + ' has the two numbers; chapter ' + bkChapterNo('rhythm') + ' the quaver groups and the dotted crotchet in 2/4, 3/4 and 4/4.', '6/8은 Grade 1 박자표예요(못갖춘마디가 있든 없든). 배울 때는 8분음표마다 세고(1 2 3 4 5 6), 익숙해지면 큰 박 둘(1과 4)을 느껴요: 여기 클릭은 8분음표마다, 센 클릭은 1과 4. 박자표의 두 숫자는 ' + bkChapterNo('time-signatures') + '장, 8분음표 묶음과 점4분음표(2/4, 3/4, 4/4)는 ' + bkChapterNo('rhythm') + '장에 있어요.')}</>} qr={bkLink('drill=' + ch + '&lock=1')}>
      <LbOnly print><div data-ch={ch}>
        <div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>CHAPTER {bkChapterNo(ch)}</div>
        <div style={{fontFamily:LB_SERIF,fontSize:50,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{t('6/8 Time', '6/8박자')}</div>
      </div></LbOnly>
      {still('big', 600)}
      <LbSay size={18}>{t('Six quavers in a bar, in two groups of three: two big beats. Count 1 2 3 4 5 6; 1 and 4 are strong.', '한 마디에 8분음표 여섯, 셋씩 두 묶음: 큰 박 둘. 1 2 3 4 5 6으로 세고, 1과 4가 세요.')}</LbSay>
      <div className="lb-toc" style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:20}}>
        <LbOnly print><div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('In this chapter', '이 챕터에서는')}</div>
          {toc.map(([n, p]) => <div key={p} className="lb-toc-row" style={{display:'flex',justifyContent:'space-between',alignItems:'center',fontSize:14.5,padding:'5px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}><span style={{display:'flex',alignItems:'center',gap:9}}>{bkGoal(15)}{n}</span><span style={{color:BK.muted,fontWeight:800}}>{p}</span></div>)}
        </div></LbOnly>
        <div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('By the end, you can', '이 챕터를 마치면')}</div>
          {[t('count 6/8 and feel its two big beats', '6/8을 세고 큰 박 둘을 느낄 수 있어요'), t('hold a dotted crotchet for one big beat', '점4분음표를 큰 박 하나만큼 누를 수 있어요'), t('play long-short in 6/8', '6/8에서 길게-짧게를 칠 수 있어요'), t('tell 3/4 from 6/8', '3/4과 6/8을 구별할 수 있어요'), t('count, clap and play a new line in 6/8', '6/8의 새 줄을 세고, 손뼉 치고, 칠 수 있어요')].map(x => <div key={x} style={{display:'flex',gap:9,alignItems:'flex-start',fontSize:14.5,padding:'5px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}><span style={{flex:'0 0 auto',marginTop:3}}>{bkGoal(15)}</span><span>{x}</span></div>)}
        </div>
      </div>
      <LbOnly print><LbDrillStrip id={ch}/></LbOnly>
    </LbPage>,
    <LbPage key="2" no={2} chId={ch} kicker={t('Step 1', '1단계')} title={t('Two big beats', '큰 박 둘')}
      teacher={<>{t('Clap all six quavers, then only 1 and 4; then walk the big beats round the room while you clap the quavers. Watch for a child who hears 6/8 as three in a bar (1 3 5 strong): say 1 2 3, 4 5 6 with the 1 and 4 louder.', '8분음표 여섯을 모두 손뼉 치고, 그다음 1과 4만 쳐요. 그다음 선생님이 8분음표를 치는 동안 아이는 큰 박에 맞춰 방을 걸어요. 6/8을 세 박(1 3 5가 센박)으로 듣는 아이가 있으면, 1과 4를 크게 해서 1 2 3, 4 5 6으로 말해 주세요.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=1')}>
      <LbLive still={still('big')} live={<E8BigPad/>}/>
      <LbSay>{LANG === 'ko' ? <>6/8: 한 마디에 <b>8분음표 여섯</b>. 셋씩 묶어서 <b>1 2 3, 4 5 6</b>으로 세고, <b>1과 4가 센박</b>이에요. 그래서 6/8은 <b>큰 박 둘</b>로 느껴요.</> : <>6/8: <b>six quavers</b> in a bar. Count them in threes, <b>1 2 3, 4 5 6</b>, and <b>1 and 4 are strong</b>. So 6/8 feels like <b>two big beats</b>.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>8분음표 여섯을 손뼉 치며 세요: 1 2 3 4 5 6. 1과 4를 더 크게.</>, <>이번엔 1과 4에서만 손뼉. 나머지는 속으로 세요.</>, <>피아노로: 1과 4에 가운데 도, 나머지는 그 옆 D를 살짝.</>]
        : [<>Clap six quavers and count: 1 2 3 4 5 6. Make 1 and 4 louder.</>, <>Now clap only on 1 and 4; count the rest inside.</>, <>At the piano: middle C on 1 and 4, a soft D for the others.</>]}/>
      <LbRemember>{t('Six quavers, two big beats: 1 and 4.', '8분음표 여섯, 큰 박 둘: 1과 4.')}</LbRemember>
    </LbPage>,
    <LbPage key="3" no={3} chId={ch} kicker={t('Step 2', '2단계')} title={t('The dotted crotchet', '점4분음표')}
      teacher={<>{t('In 6/8 the dotted crotchet is the big beat (in 2/4, 3/4 and 4/4 it was a beat and a half). Hold it while counting the three quavers inside, out loud at first.', '6/8에서는 점4분음표가 큰 박 하나예요(2/4, 3/4, 4/4에서는 한 박 반이었어요). 처음에는 소리 내어, 그 안의 8분음표 셋을 세면서 누르고 있어요.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=2')}>
      <LbLive still={<LbPic h={180}><div style={{width:'100%',maxWidth:560,margin:'0 auto'}}>{e8Eq(NV_DOTTED[1], 3)}{e8El('dot')}</div></LbPic>} live={<E8DotPad/>}/>
      <LbSay>{LANG === 'ko' ? <>점4분음표 하나 = <b>8분음표 셋</b> = <b>큰 박 하나</b>. 1 (2 3), 4 (5 6): 누르는 동안 속으로 세어요.</> : <>One dotted crotchet = <b>three quavers</b> = <b>one big beat</b>. 1 (2 3), 4 (5 6): count inside while you hold it.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>점4분음표 둘: 1에서 누르고 2 3을 세고, 4에서 누르고 5 6을 세요.</>, <>둘째 마디: 8분음표 셋, 그다음 점4분음표 하나.</>, <>가운데 도로 쳐요. 소리 내어 세면서.</>]
        : [<>Two dotted crotchets: press on 1 and count 2 3; press on 4 and count 5 6.</>, <>Bar two: three quavers, then one dotted crotchet.</>, <>Play it on middle C, counting out loud.</>]}/>
      <LbRemember>{t('Dotted crotchet: three quavers, one big beat.', '점4분음표: 8분음표 셋, 큰 박 하나.')}</LbRemember>
    </LbPage>,
    <LbPage key="4" no={4} chId={ch} kicker={t('Step 3', '3단계')} title={t('Long, short', '길게, 짧게')}
      teacher={<>{t('The crotchet-quaver pair is the sound of 6/8: a lilt. Say it on the counts first (1, 3; 4, 6), then tap. A crotchet in 6/8 lasts two quavers, not one beat.', '4분음표-8분음표 짝이 6/8다운 소리예요: 흔들리는 느낌. 먼저 셈으로 말하고(1, 3; 4, 6), 그다음 쳐요. 6/8에서 4분음표는 한 박이 아니라 8분음표 둘이에요.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=5')}>
      <LbLive still={<LbPic h={180}><div style={{width:'100%',maxWidth:560,margin:'0 auto'}}>{e8Eq(NV_NOTES[2], 2)}{e8El('ls')}</div></LbPic>} live={<E8LsPad/>}/>
      <LbSay>{LANG === 'ko' ? <>큰 박 하나를 <b>4분음표 + 8분음표</b>로 나눠요: 길게, 짧게. 4분음표는 8분음표 둘. 셈은 <b>1 (2) 3, 4 (5) 6</b>.</> : <>Split a big beat into <b>a crotchet and a quaver</b>: long, short. The crotchet lasts two quavers. Count <b>1 (2) 3, 4 (5) 6</b>.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>셈으로 말해요: 1, 3, 4, 6. 그다음 같은 리듬으로 손뼉.</>, <>둘째 마디: 점4분음표, 그다음 8분음표 셋.</>, <>피아노로, 가운데 도. 길게, 짧게가 흔들리듯이.</>]
        : [<>Say the counts: 1, 3, 4, 6. Then clap the same rhythm.</>, <>Bar two: a dotted crotchet, then three quavers.</>, <>At the piano on middle C: long, short, with a lilt.</>]}/>
      <LbRemember>{t('Crotchet + quaver = one big beat: long, short.', '4분음표 + 8분음표 = 큰 박 하나: 길게, 짧게.')}</LbRemember>
    </LbPage>,
    <LbPage key="5" no={5} chId={ch} kicker={t('Step 4', '4단계')} title={t('3/4 or 6/8?', '3/4? 6/8?')}
      teacher={<>{t('Both bars hold six quavers; the beaming shows the beat: 3/4 beams them in twos (three crotchet beats), 6/8 in threes (two dotted-crotchet beats). By ear, the strong clicks: every second quaver in 3/4, every third in 6/8.', '두 마디 모두 8분음표 여섯이에요. 빔이 박을 보여 줘요: 3/4은 둘씩(4분음표 세 박), 6/8은 셋씩(점4분음표 두 박). 귀로는 센 클릭: 3/4은 둘째 8분음표마다, 6/8은 셋째마다.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=3')}>
      <LbLive still={<LbPic h={220}><div style={{display:'flex',flexDirection:'column',gap:6,width:'100%',maxWidth:560,margin:'0 auto'}}><div style={{fontSize:13,fontWeight:900,color:BK.ink,textAlign:'center'}}>{t('3/4: three beats, 2 2 2', '3/4: 세 박, 2 2 2')}</div>{e8El('t34')}<div style={{fontSize:13,fontWeight:900,color:BK.coral,textAlign:'center'}}>{t('6/8: two big beats, 3 3', '6/8: 큰 박 둘, 3 3')}</div>{e8El('big')}</div></LbPic>} live={<E8TwoPad/>}/>
      <LbSay>{LANG === 'ko' ? <>둘 다 8분음표 여섯. <b>3/4</b>은 <b>둘씩</b> 묶어서 세 박, <b>6/8</b>은 <b>셋씩</b> 묶어서 큰 박 둘. 빔을 보면 알 수 있고, 센 클릭으로 들을 수 있어요.</> : <>Both hold six quavers. <b>3/4</b> groups them <b>in twos</b>: three beats. <b>6/8</b> <b>in threes</b>: two big beats. The beams show it; the strong clicks let you hear it.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>3/4로 세요: 1 + 2 + 3 +. 그다음 6/8: 1 2 3 4 5 6. 센 곳만 크게.</>, <>선생님이 둘 중 하나를 치면, 3/4인지 6/8인지 말해요.</>, <>내가 치고, 선생님이 맞혀요.</>]
        : [<>Count 3/4: 1 + 2 + 3 +. Then 6/8: 1 2 3 4 5 6. Loud only on the strong ones.</>, <>Your teacher plays one of them: say 3/4 or 6/8.</>, <>Now you play, and your teacher guesses.</>]}/>
      <LbRemember>{t('3/4: in twos, three beats. 6/8: in threes, two big beats.', '3/4: 둘씩, 세 박. 6/8: 셋씩, 큰 박 둘.')}</LbRemember>
    </LbPage>,
    <LbPage key="6" no={6} chId={ch} kicker={t('Step 5', '5단계')} title={t('Count, clap, play', '세고, 손뼉 치고, 치기')}
      teacher={<>{t('Every new line in the same order: the counts under the notes, said out loud; clapped; then tapped or played on one note. The dotted minim fills a whole bar of 6/8.', '새 줄은 언제나 같은 순서로: 음표 아래 셈을 소리 내어 말하고, 손뼉 치고, 그다음 한 음으로 쳐요. 점2분음표는 6/8 한 마디를 다 채워요.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=6')}>
      <LbLive still={<LbPic h={220}><div style={{display:'flex',flexDirection:'column',gap:8,width:'100%',maxWidth:560,margin:'0 auto'}}>{e8El('m1')}{e8El('m3')}</div></LbPic>} live={<E8ReadPad/>}/>
      <LbSay>{LANG === 'ko' ? <>새 줄: 음표마다 <b>셈을 찾아서</b>(1~6) 소리 내어 말하고, <b>손뼉 치고</b>, 그다음 <b>쳐요</b>. 점2분음표는 한 마디 전체: 1부터 6까지.</> : <>A new line: <b>find each note's count</b> (1 to 6) and say it, <b>clap it</b>, then <b>play it</b>. A dotted minim fills the whole bar: 1 to 6.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>첫 줄의 셈을 말해요: 1 2 3, 4 6 | 1, 4.</>, <>손뼉 치며 세어요. 그다음 가운데 도로 쳐요.</>, <>둘째 줄: 점2분음표는 여섯까지 누르고 있어요.</>]
        : [<>Say the first line's counts: 1 2 3, 4 6 | 1, 4.</>, <>Clap it while counting. Then play it on middle C.</>, <>Line two: hold the dotted minim through all six.</>]}/>
      <LbRemember>{t('Find the counts, say them, clap, play.', '셈을 찾고, 말하고, 손뼉 치고, 쳐요.')}</LbRemember>
    </LbPage>,
    <LbPage key="7" no={7} chId={ch} kicker={t('Check-up', '점검')} title={t('My five checks', '나의 다섯 가지 확인')}
      teacher={<>{t('Clapped or played to you, counting out loud. For the fourth, play a bar of either and the child names it.', '소리 내어 세면서 선생님에게 손뼉이나 연주로 들려줘요. 넷째는 선생님이 둘 중 한 마디를 치고 아이가 이름을 말해요.')}</>}>
      <LbSay>{t('Tick each one: not yet, nearly, or got it!', '하나씩 표시해요: 아직, 거의, 됐어요!')}</LbSay>
      <LbLive still={<LbStageRows big rows={checks5.map(([a, txt]) => [pen(a), txt])}/>} live={<FiveChecks376 rows={checks5} storeKey="pb_e8_five"/>}/>
    </LbPage>,
  ];
}
function SixEightLessonBook() { return <>{e8LbPages(false)}</>; }
function E8Learn({ onStart }) {
  const pages = e8LbPages(true), opener = pages[0];
  return (
    <Lesson id="six-eight" title={t('6/8 time', '6/8박자')} onStart={onStart} noArt
      head={<LbScreenCtx.Provider value={true}><BkChapterCtx.Provider value="six-eight"><div className="lb-screen lb-open" style={{display:'flex',flexDirection:'column',gap:12,margin:'0 0 8px'}}>{lbWordsFirst(opener.props.children)}</div></BkChapterCtx.Provider></LbScreenCtx.Provider>}>
      {pages.slice(1).map((pg, i) => <Step key={i} title={pg.props.title}><LbScreenPage page={pg}/></Step>)}
    </Lesson>
  );
}

// ── the drill ──
const E8_LEVELS = [
  { n: 1, label: 'On which count?', kind: 'count', time: 10 },
  { n: 2, label: 'How many quavers?', kind: 'len', time: 8 },
  { n: 3, label: '3/4 or 6/8? Look at the beams', kind: 'see', time: 8 },
  { n: 4, label: 'Listen: 3/4 or 6/8?', kind: 'hear', time: 14, noPrint: true },
  { n: 5, label: 'Fill the bar', kind: 'fill', time: 12 },
  { n: 6, label: 'Tap it', kind: 'tap', time: 30, noPrint: true },
];
Object.assign(LEVEL_KO, { 'On which count?': '몇째 셈에서?', 'How many quavers?': '8분음표 몇 개?', '3/4 or 6/8? Look at the beams': '3/4? 6/8? 빔을 봐요', 'Listen: 3/4 or 6/8?': '듣기: 3/4? 6/8?', 'Fill the bar': '마디 채우기', 'Tap it': '쳐 보기' });
const E8_LEN = [['e', 1, () => NV_NOTES[3]], ['q', 2, () => NV_NOTES[2]], ['qd', 3, () => NV_DOTTED[1]], ['hd', 6, () => NV_DOTTED[0]]];
// a bar of 6/8 with one note missing (the box), and the note that fills it
const E8_FILL = [[[['q'], ['e'], ['q'], ['box', 0.5]], 'e'], [[['qd'], ['box', 1.5]], 'qd'], [[['e3'], ['box', 1], ['e']], 'q'], [[['q'], ['e'], ['box', 1.5]], 'qd'], [[['box', 1], ['e'], ['qd']], 'q'], [[['qd'], ['q'], ['box', 0.5]], 'e']];
function genE8Question(lv, prev) {
  const uid = Math.random(), kind = lv.kind;
  if (kind === 'count') { let key, i, g = 0, S; do { key = pick(['ls', 'ls2', 'm1', 'm2', 'dot']); S = srhSounds(E8[key]).map((s, j) => [s, j]).filter(([s]) => !s.rest); i = pick(S)[1]; } while (prev && prev.key === key + i && g++ < 10);
    const s = srhSounds(E8[key])[i]; return { kind, row: key, i, answer: rq68Count(s.b), choices: ['1', '2', '3', '4', '5', '6'], key: key + i, uid }; }
  if (kind === 'len') { let x, g = 0; do { x = pick(E8_LEN); } while (prev && prev.key === x[0] && g++ < 10); return { kind, n: x[0], answer: String(x[1]), choices: ['1', '2', '3', '6'], key: x[0], uid }; }
  if (kind === 'see' || kind === 'hear') { const a = Math.random() < 0.5 ? 't34' : 'big'; return { kind, row: a, answer: a === 't34' ? '3/4' : '6/8', choices: ['3/4', '6/8'], key: a + Math.random(), uid }; }
  if (kind === 'fill') { let i, g = 0; do { i = Math.floor(Math.random() * E8_FILL.length); } while (prev && prev.key === 'f' + i && g++ < 10); return { kind, i, answer: E8_FILL[i][1], choices: ['e', 'q', 'qd'], key: 'f' + i, uid }; }
  let key, g = 0; do { key = pick(['big', 'dot', 'ls', 'ls2', 'm1', 'm2', 'm3']); } while (prev && prev.row === key && g++ < 10);
  return { kind: 'tap', row: key, answer: 'ok', choices: [], key: 'tap' + key, uid };
}
const E8_NOTE = { e: () => NV_NOTES[3], q: () => NV_NOTES[2], qd: () => NV_DOTTED[1] };
const e8NoteName = (k) => ({ e: t('quaver', '8분음표'), q: t('crotchet', '4분음표'), qd: t('dotted crotchet', '점4분음표') })[k];
function e8AnswerLabel(q) {
  if (q.kind === 'count') return t('count ' + q.answer, q.answer + '번째 셈');
  if (q.kind === 'len') return t(q.answer + ' quaver' + (q.answer === '1' ? '' : 's'), '8분음표 ' + q.answer + '개');
  if (q.kind === 'fill') return e8NoteName(q.answer);
  if (q.kind === 'tap') return t('tapped on time', '제때 치기');
  return q.answer;
}
function E8Question({ q, given, locked, onAnswer, pixel }) {
  const done = !!given, btnCls = pixel ? 'pixel-choice' : 'choice-btn', cls = (c) => btnCls + (!done ? '' : c === q.answer ? ' good' : given.ans === c ? ' bad' : '');
  useEffect(() => { if (q.kind !== 'hear') return; const id = setTimeout(() => e8Play(q.row), 350); return () => { clearTimeout(id); stopClicks(); }; }, [q.uid]);
  let title, fig = null, label = (c) => c, cols = q.choices.length;
  if (q.kind === 'count') { title = t('6/8: on which count does the coral note start?', '6/8: 산호색 음은 몇째 셈에서 시작할까요?'); fig = rqStaffEl(E8[q.row], { ...E8P.so, lit: q.i, counts: done ? undefined : false, hearts: false }); cols = 6; }
  else if (q.kind === 'len') { const x = E8_LEN.find(y => y[0] === q.n); title = t('In 6/8, how many quavers does this note last?', '6/8에서 이 음표는 8분음표 몇 개만큼일까요?'); fig = <div style={{display:'flex',justifyContent:'center',margin:'4px 0 8px'}}><Glyph item={x[2]()} size={90}/></div>; }
  else if (q.kind === 'see') { title = t('Six quavers, no time signature. 3/4 or 6/8? Look at the beams.', '8분음표 여섯, 박자표가 없어요. 3/4일까요, 6/8일까요? 빔을 봐요.'); fig = rqStaffEl(E8[q.row].filter(it => it[0] !== 'ts').slice(0, q.row === 't34' ? 3 : 2).concat([['||']]), { counts: done ? undefined : false, hearts: false }); }
  else if (q.kind === 'hear') { title = t('Listen to the strong clicks: 3/4 or 6/8?', '센 클릭을 들어 봐요: 3/4일까요, 6/8일까요?'); fig = done ? e8El(q.row, { hearts: false }) : null; }
  else if (q.kind === 'fill') { title = t('Which note fills this bar of 6/8?', '6/8 이 마디를 채우는 음표는?'); fig = rqStaffEl([['ts', 6, 8]].concat(E8_FILL[q.i][0], [['||']]), { counts: false, hearts: false }); label = (c) => <Glyph item={E8_NOTE[c]()} size={pixel ? 34 : 44}/>; }
  else { title = t('Tap it: press for each note and hold it for its length.', '쳐 보세요: 음표마다 누르고, 그 길이만큼 누르고 있어요.'); fig = <RqStaff key={q.uid} items={E8[q.row]} {...e8Props(q.row)} onResult={(r) => { if (!locked && !done) onAnswer(r.ok ? 'ok' : 'no'); }}/>; cols = 0; }
  const why = !done ? null : q.kind === 'count' ? t('Count every quaver: 1 2 3 4 5 6; the coral note starts on ' + q.answer + '.', '8분음표마다 세어요: 1 2 3 4 5 6. 산호색 음은 ' + q.answer + '에서 시작해요.')
    : q.kind === 'len' ? t('Quaver 1, crotchet 2, dotted crotchet 3, dotted minim 6.', '8분음표 1, 4분음표 2, 점4분음표 3, 점2분음표 6.')
    : q.kind === 'see' || q.kind === 'hear' ? t(q.answer === '3/4' ? '3/4: quavers in twos, three beats.' : '6/8: quavers in threes, two big beats.', q.answer === '3/4' ? '3/4: 8분음표 둘씩, 세 박.' : '6/8: 8분음표 셋씩, 큰 박 둘.')
    : q.kind === 'fill' ? t('A bar of 6/8 holds six quavers: the missing part is a ' + e8NoteName(q.answer) + '.', '6/8 한 마디는 8분음표 여섯: 빈 곳은 ' + e8NoteName(q.answer) + '.') : null;
  return (<div>
    <p style={pixel ? {fontSize:11.5,textAlign:'center'} : {fontSize:15,fontWeight:700,textAlign:'center',margin:'0 0 8px',color:'var(--muted)',textWrap:'balance'}}>{title}</p>
    {q.kind === 'hear' && <div style={{textAlign:'center',marginBottom:10}}><button className={pixel ? 'pixel-btn' : 'ghost-btn'} style={{minHeight:44}} onClick={() => e8Play(q.row)}>{t('▶ Play it again', '▶ 다시 듣기')}</button></div>}
    <div style={{marginBottom:12}}>{fig}</div>
    {cols > 0 && <div style={{display:'grid',gridTemplateColumns:'repeat(' + cols + ',minmax(0,1fr))',gap:8}}>{q.choices.map(c => <button key={c} disabled={locked} className={cls(c)} style={{padding:pixel ? '14px 4px' : '12px 4px',fontSize:pixel ? 9.5 : 16,fontWeight:900,display:'flex',justifyContent:'center',alignItems:'center'}} onClick={() => { if (locked || done) return; stopClicks(); onAnswer(c); }}>{label(c)}</button>)}</div>}
    {why && !pixel && <div style={{marginTop:10,fontSize:13.5,color:'#4a4d86',background:'#fff',borderRadius:8,padding:'7px 10px',lineHeight:1.45}}>{why}</div>}
  </div>);
}
Object.assign(SIX_EIGHT_DRILL, { levels: E8_LEVELS, generate: genE8Question, check: (q, ans) => ans !== null && ans !== undefined && ans === q.answer, answerLabel: e8AnswerLabel, Question: E8Question, Learn: E8Learn });
