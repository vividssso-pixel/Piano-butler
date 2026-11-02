p='drills.src.html'; s=open(p).read()
if 'm43' in s: print('already'); raise SystemExit
def rep(old, new, cnt=1):
    global s
    assert s.count(old)==cnt, (s.count(old), old[:90])
    s=s.replace(old,new)

# ── 1. student tabs: Today · Practice (House and Library live inside Practice); visitors have no tab bar ──
rep("{!st.lock && !(showToday && !T) && (", "{!st.lock && (T || showToday) && (   /* m43: a linked student gets Today · Practice */")
rep(": (showToday ? [['today', t('Today', '오늘')], ['map', t('Map', '지도')], ['practice', t('Practice', '연습')]] : [['map', t('Map', '지도')], ['practice', t('Practice', '연습')]]))",
    ": [['today', t('Today', '오늘')], ['practice', t('Practice', '연습')]])")
rep("v === 'lib' ? !!st.lib && (st.view === 'home' || (st.view === 'tools' && st.ret === 'home')) : st.view === v;",
    "v === 'lib' ? !!st.lib && (st.view === 'home' || (st.view === 'tools' && st.ret === 'home')) : (!T && v === 'practice') ? ['practice', 'path', 'chapters', 'home', 'tools'].includes(st.view) : st.view === v;")
rep("drill: (v === 'practice' || v === 'students') ? st.drill : null", "drill: T && (v === 'practice' || v === 'students') ? st.drill : null")
# House and Library go back to Practice for every student and visitor
rep("const todayBack = showToday && !T ? <button className=\"ghost-btn\" style={{fontSize:13,padding:'5px 12px',marginBottom:12}} onClick={() => { update({ view: 'today', tool: null, kit: null, drill: null, from: null }); try { window.scrollTo(0, 0); } catch (e) {} }}>{t('← Today', '← 오늘')}</button> : null;",
    "const todayBack = !T ? <button className=\"ghost-btn\" data-testid=\"back-practice\" style={{fontSize:13,padding:'5px 12px',marginBottom:12}} onClick={() => { update({ view: 'practice', tool: null, kit: null, drill: null, from: null, lib: false }); try { window.scrollTo(0, 0); } catch (e) {} }}>{t('← Practice', '← 연습')}</button> : null;   // m43: House and Library sit inside Practice")
rep("<>{todayBack}<PracticeView onOpen={(id) => { update({ tool: id }); try { window.scrollTo(0, 0); } catch (e) {} }}/></>",
    "<PracticeView onOpen={(id) => { update({ tool: id }); try { window.scrollTo(0, 0); } catch (e) {} }} onHouse={() => { update({ view: 'path', tool: null, drill: null, from: null, lib: false }); try { window.scrollTo(0, 0); } catch (e) {} }} onLibrary={HM ? () => { update({ view: 'home', lib: false, ha: null, hc: null, hs: null, drill: null, from: null }); try { window.scrollTo(0, 0); } catch (e) {} } : null}/>")

# ── 2. the student's Practice: two doors, then the tools in three groups ──
rep("function PracticeView({ onOpen }) {\n  return (",
    "const PRACTICE_GROUPS = [[['Play', '연습'], ['echo', 'sight-reading', 'count-along', 'beat-target', 'find-every', 'write-note', 'fill-bar', 'term-cards', 'make-card']], [['Body', '몸'], ['posture-check', 'arm-moves']], [['Tools', '도구'], ['metronome', 'practice-timer', 'practice-dice', 'perfect-counter']]];   // m43\n"
    "function PracticeView({ onOpen, onHouse, onLibrary }) {\n"
    "  if (!UI_TEACHER) {   // m43 (her 2 Nov: 'Today and Practice only; House and Library inside Practice')\n"
    "    const door = (bg, title, sub, fn, id) => <button type=\"button\" data-testid={id} onClick={fn} style={{flex:1,minWidth:0,textAlign:'left',border:'none',borderRadius:14,background:bg,color:'#fff',padding:'14px 12px',cursor:'pointer',font:'inherit'}}><b style={{display:'block',fontFamily:\"'Playfair Display', Georgia, serif\",fontSize:21,fontWeight:800}}>{title}</b><span style={{display:'block',fontSize:12.5,opacity:0.88,marginTop:3,lineHeight:1.35}}>{sub}</span></button>;\n"
    "    return (\n"
    "      <div className=\"fade-up\" data-testid=\"student-practice\">\n"
    "        <div style={{display:'flex',gap:10,marginBottom:6}}>\n"
    "          {onHouse && door('var(--navy)', t('House', '집'), t('Your rooms, floor by floor', '층마다 나의 방'), onHouse, 'door-house')}\n"
    "          {onLibrary && door('#2e8a6e', t('Library', '서재'), t('Books to look things up', '찾아보는 책들'), onLibrary, 'door-library')}\n"
    "        </div>\n"
    "        {PRACTICE_GROUPS.map(([nm, ids]) => <div key={nm[0]} style={{marginTop:16}}>\n"
    "          <div style={{fontSize:11,fontWeight:900,letterSpacing:'0.1em',textTransform:'uppercase',color:'var(--coral)',margin:'0 0 2px'}}>{t(nm[0], nm[1])}</div>\n"
    "          {ids.map((id, i) => { const tl = TOOLS.find(x => x.id === id); if (!tl) return null; return <SlimRow key={id} title={id === 'perfect-counter' ? t('5 in a row', '5번 연속') : LANG === 'ko' && TOOL_KO[id] ? TOOL_KO[id][0] : tl.title} sub={tl.blurb} onClick={() => onOpen(id)} last={i === ids.length - 1}/>; })}\n"
    "        </div>)}\n"
    "      </div>\n"
    "    );\n"
    "  }\n"
    "  return (")

# ── 3. Today: greeting, teacher, practised, the next room in one line, my progress, quick tools ──
rep("function TodayView({ link, onOpenChapter, onOpenTool, onAll, head, compact }) {", "function TodayView({ link, onOpenChapter, onOpenTool, onAll, head, compact, greet, tail }) {   // m43: greet(dateLabel), tail before the saved line")
rep("      <h2 style={{ fontFamily: \"'Playfair Display', Georgia, serif\", fontWeight: 900, fontSize: 32, margin: '0 0 2px', letterSpacing: '-0.02em', color: 'var(--navy)' }}>{t('Today', '오늘')}</h2>\n      <div style={{ color: 'var(--muted)', fontSize: 15, marginBottom: 16 }}>{dateLabel}</div>\n",
    "      {greet ? greet(dateLabel) : <><h2 style={{ fontFamily: \"'Playfair Display', Georgia, serif\", fontWeight: 900, fontSize: 32, margin: '0 0 2px', letterSpacing: '-0.02em', color: 'var(--navy)' }}>{t('Today', '오늘')}</h2>\n      <div style={{ color: 'var(--muted)', fontSize: 15, marginBottom: 16 }}>{dateLabel}</div></>}\n")
rep("<span>{lesson ? t('This week', '이번 주') + (lessonLabel ? ' · ' + t('lesson on ', '') + lessonLabel + t('', ' 레슨') : '') : t('From your teacher', '선생님이 올려준 것')}</span>",
    "<span style={{ color: greet ? 'var(--coral)' : undefined }}>{greet ? t('From your teacher', '선생님이 올려준 것') + (lessonLabel ? ' · ' + lessonLabel : '') : lesson ? t('This week', '이번 주') + (lessonLabel ? ' · ' + t('lesson on ', '') + lessonLabel + t('', ' 레슨') : '') : t('From your teacher', '선생님이 올려준 것')}</span>")
rep("          <div style={kicker}>{t('Did you practise at the piano today?', '오늘 피아노 연습했어요?')}</div>",
    "          <div style={{ ...kicker, color: greet ? 'var(--coral)' : kicker.color }}>{t('Did you practise at the piano today?', '오늘 피아노 연습했어요?')}</div>")
rep("      {(() => {\n        const line = syncStatus === 'saved'", "      {tail}\n      {(() => {\n        const line = syncStatus === 'saved'")

a = s.index("function StudentHome({ link, onOpenChapter, onOpenTool, onHome }) {")
b = s.index("// ─── Phase 357: \"My rhythms\"", a)
s = s[:a] + r'''function StudentHome({ link, onOpenChapter, onOpenTool, onAll }) {   // m43 (her 2 Nov): teacher, practised, next room in a line, my progress, three quick tools
  const [open, setOpen] = useState(null);   // 'scales' | 'rhythms': the old stamp sheets, opened from My progress
  const totals = loadStepTotals(), ids = pathIds();
  const status = Object.fromEntries(ids.map(id => [id, chapterStatus(id, totals)]));
  const focus = guideFocus(status, ids), next = focus ? focus.id : null, nDone = ids.filter(id => status[id] === 'done').length;
  const st = loadStamps(), nSc = ['major', 'minor'].reduce((a, m) => a + CLOCK_KEYS[m].reduce((b, k) => b + CLOCK_STEPS.filter(([x]) => st[(m === 'minor' ? 'm:' : '') + k + ':' + x]).length, 0), 0);
  const nRh = [...RS_NOTES, ...RS_DOTS, ...RS_TIMES].filter(r => st['r:' + r.id]).length;
  const k = next ? stageOfChapter(next) : -1, lv = k >= 0 ? floorName(k) : '';
  const h = new Date().getHours(), hello = h < 12 ? t('Good morning.', '좋은 아침이에요.') : h < 18 ? t('Good afternoon.', '안녕하세요.') : t('Good evening.', '좋은 저녁이에요.');
  const greet = (date) => <div data-testid="today-greet" style={{ display: 'flex', gap: 12, alignItems: 'center', margin: '0 0 14px' }}>
    <img src={VIC_CAMEO} alt="" style={{ height: 58, flex: '0 0 auto' }}/>
    <div><div style={{ fontFamily: "'Playfair Display', Georgia, serif", fontStyle: 'italic', fontSize: 22, color: 'var(--navy)', lineHeight: 1.2 }}>{'“' + hello + '”'}</div>
      <div style={{ fontSize: 13.5, color: 'var(--muted)', marginTop: 2 }}>{date}{lv ? ' · ' + lv : ''}</div></div>
  </div>;
  const lab = { fontSize: 11, fontWeight: 900, letterSpacing: '0.08em', textTransform: 'uppercase', color: 'var(--coral)', marginBottom: 10 };
  const tile = (n, of, word, fn, on, id) => <button type="button" data-testid={id} aria-expanded={on == null ? undefined : on} onClick={fn} style={{ flex: 1, minWidth: 0, textAlign: 'left', background: on ? '#fff3ee' : 'var(--surface)', border: '1.5px solid ' + (on ? 'var(--coral)' : 'var(--navy-line)'), borderRadius: 12, padding: '10px 10px', cursor: 'pointer', font: 'inherit' }}>
    <b style={{ display: 'block', fontSize: 22, color: 'var(--navy)', lineHeight: 1.1 }}>{n}{of ? <span style={{ fontSize: 14, color: 'var(--muted)' }}>/{of}</span> : null}</b><span style={{ fontSize: 12, color: 'var(--muted)', lineHeight: 1.3 }}>{word}</span></button>;
  const quick = [['scale-finder', '♯'], ['metronome', '♩'], ['practice-timer', '◷']];
  const tail = <>
    {next && <button type="button" data-testid="today-next" onClick={() => onOpenChapter(next)} style={{ display: 'flex', width: '100%', alignItems: 'center', gap: 6, background: 'none', border: 'none', borderTop: '1px solid var(--navy-line)', borderBottom: '1px solid var(--navy-line)', padding: '11px 4px', margin: '0 0 14px', font: 'inherit', fontSize: 14.5, color: 'var(--navy)', cursor: 'pointer', textAlign: 'left' }}>
      <span style={{ color: 'var(--muted)', whiteSpace: 'nowrap' }}>{focus.kind === 'resume' ? t('Keep going:', '이어서:') : t('Next room:', '다음 방:')}</span>
      <b style={{ minWidth: 0, overflowWrap: 'anywhere' }}>{bkChapterNo(next) + ' · ' + bkChapterName(next)}</b>
      <span style={{ marginLeft: 'auto', color: 'var(--coral)', fontWeight: 900, whiteSpace: 'nowrap' }}>{t('Go in ›', '들어가기 ›')}</span></button>}
    <div data-testid="today-progress" style={{ background: 'var(--surface)', border: '1.5px solid var(--navy-line)', borderRadius: 16, padding: 16, marginBottom: 14, boxShadow: '0 4px 18px rgba(38,41,107,0.05)' }}>
      <div style={lab}>{t('My progress', '나의 진도')}</div>
      <div style={{ display: 'flex', gap: 8 }}>
        {tile(nDone, null, t(nDone === 1 ? 'room done' : 'rooms done', '끝낸 방'), onAll, null, 'prog-rooms')}
        {tile(nSc, 72, t('scale stamps', '스케일 도장'), () => setOpen(o => o === 'scales' ? null : 'scales'), open === 'scales', 'prog-scales')}
        {tile(nRh, RS_TOTAL, t('rhythm stamps', '리듬 도장'), () => setOpen(o => o === 'rhythms' ? null : 'rhythms'), open === 'rhythms', 'prog-rhythms')}
      </div>
      {open === 'scales' && <div style={{ marginTop: 12 }}><StudentScales onOpenTool={onOpenTool}/></div>}
      {open === 'rhythms' && <div style={{ marginTop: 12 }}><RhythmSheet/></div>}
    </div>
    <div style={{ ...lab, margin: '4px 0 8px' }}>{t('Quick tools', '바로 쓰는 도구')}</div>
    <div data-testid="today-quick" style={{ display: 'grid', gridTemplateColumns: 'repeat(3, minmax(0,1fr))', gap: 8, marginBottom: 14 }}>
      {quick.map(([id, g]) => { const tl = TOOLS.find(x => x.id === id); if (!tl) return null; return <button key={id} type="button" data-tool={id} onClick={() => onOpenTool(id)} style={{ background: 'var(--surface)', border: '1.5px solid var(--navy-line)', borderRadius: 12, padding: '10px 4px', cursor: 'pointer', font: 'inherit', textAlign: 'center' }}>
        <span aria-hidden="true" style={{ display: 'block', fontSize: 20, color: 'var(--coral)', lineHeight: 1.1 }}>{g}</span><b style={{ display: 'block', fontSize: 13, color: 'var(--navy)', marginTop: 3 }}>{LANG === 'ko' && TOOL_KO[id] ? TOOL_KO[id][0] : tl.title}</b></button>; })}
    </div>
  </>;
  return (
    <div data-testid="student-home">
      <TodayView link={link} onOpenChapter={onOpenChapter} onOpenTool={onOpenTool} onAll={onAll} compact greet={greet} tail={tail}/>
    </div>
  );
}

''' + s[b:]

# ── 4. Where should you start?: the exam's own names on the chips, our Levels in the answer ──
rep("const PLACE_PIANO = [['0', 'Not yet', '아직'], ['P', 'Prelim', 'Prelim'],", "const PLACE_PIANO = [['0', 'None', '없음'], ['P', 'Preliminary', 'Preliminary'], /* m43: the exam you passed, by its own name */")
rep("const PLACE_THEORY = [['0', 'Not yet', '아직'],", "const PLACE_THEORY = [['0', 'None', '없음'],")
rep("They can be at different grades, and that is fine.', '빠른 문제로 10분쯤, 두 부분: 피아노(귀, 건반, 스케일; 소리 켜기)와 이론. 둘의 급이 달라도 괜찮아요.')",
    "They can be at different levels, and that is fine.', '빠른 문제로 10분쯤, 두 부분: 피아노(귀, 건반, 스케일; 소리 켜기)와 이론. 둘의 레벨이 달라도 괜찮아요.')")
rep("{t('Piano exam passed', '통과한 피아노 시험')}", "{t('Last piano exam you passed', '마지막으로 통과한 피아노 시험')}")
rep("{t('Theory exam passed', '통과한 이론 시험')}", "{t('Last theory exam you passed', '마지막으로 통과한 이론 시험')}")
rep("{t('Not sure? Choose Not yet: the questions will find your level.', '잘 모르겠으면 ‘아직’을 골라요: 문제가 알아서 찾아 줘요.')}", "{t('Not sure? Choose None: the questions will find your level.', '잘 모르겠으면 ‘없음’을 골라요: 문제가 알아서 찾아 줘요.')}")
rep("const theoryName = (n) => t('Theory Grade ' + n, '이론 ' + n + '급');", "const theoryName = (n) => t('Theory, Level ' + n, '이론 레벨 ' + n);   // m43")
rep("t('Every theory grade was easy!', '모든 이론 급이 쉬웠어요!')", "t('Every theory level was easy!', '모든 이론 레벨이 쉬웠어요!')")
# the result says where that sits among the usual exam steps, once
rep("{allPiano ? t('Every floor was easy. Start at the top: ', '모든 층이 쉬웠어요. 맨 위에서: ') + floorName(p.k) : floorName(p.k)}</div>",
    "{allPiano ? t('Every floor was easy. Start at the top: ', '모든 층이 쉬웠어요. 맨 위에서: ') + floorName(p.k) : floorName(p.k)}</div>\n"
    "          {placeExam(p.k) && <div data-testid=\"place-exam\" style={{fontSize:12.5,color:'var(--muted)',marginTop:1}}>{t('About where a ' + placeExam(p.k) + ' exam sits', placeExam(p.k) + ' 시험쯤이에요')}</div>}")
rep("{th ? theoryName(th.n) : t('Every theory level was easy!', '모든 이론 레벨이 쉬웠어요!')}</div>",
    "{th ? theoryName(th.n) : t('Every theory level was easy!', '모든 이론 레벨이 쉬웠어요!')}</div>\n"
    "          {th && <div style={{fontSize:12.5,color:'var(--muted)',marginTop:1}}>{t('About where a Grade ' + th.n + ' theory exam sits', '이론 ' + th.n + '급 시험쯤이에요')}</div>}")
rep("function placeStartRung(lad, said) {",
    "const placeExam = (k) => { const s = PATH_STAGES[k]; if (!s || s.attic || s.stories || !s.en) return ''; const n = s.en[0]; return n === 'Prelim' ? 'Preliminary' : /^Grade \\d$/.test(n) ? n : ''; };   // m43\n"
    "function placeStartRung(lad, said) {")
# How it works: our levels beside the usual exam steps, so anyone can compare
i = s.index('data-testid="map-help-panel"'); j = s.index("\n      </div>}", i) + len("\n      </div>}")
s = s[:i] and s[:j] + "\n      {help && <LevelCompare/>}" + s[j:]
rep("function MapHead({ onOpen }) {",
    "function LevelCompare() {   // m43 (her 2 Nov: 'comparable, without copying the exam names')\n"
    "  const rows = [['Level 0', t('Before a first exam', '첫 시험 전')], ['Level ½', 'Preliminary'], ['Level 1–8', 'Grade 1–8']];\n"
    "  return <div data-testid=\"level-compare\" style={{marginTop:10,background:'var(--surface)',border:'1.5px solid var(--navy-line)',borderRadius:12,padding:'10px 12px'}}>\n"
    "    <div style={{fontSize:13,color:'var(--navy-soft)',lineHeight:1.45,marginBottom:6}}>{t('Our levels follow the usual exam steps, so you can compare.', '우리 레벨은 보통의 시험 단계를 따라가요. 그래서 비교할 수 있어요.')}</div>\n"
    "    {rows.map(([a, b]) => <div key={a} style={{display:'flex',justifyContent:'space-between',gap:10,padding:'5px 0',borderTop:'1px solid var(--navy-line)',fontSize:13.5}}><b style={{color:'var(--navy)'}}>{a}</b><span style={{color:'var(--muted)'}}>≈ {b}</span></div>)}\n"
    "  </div>;\n"
    "}\n"
    "function MapHead({ onOpen }) {")
open(p,'w').write(s); print('ok')
