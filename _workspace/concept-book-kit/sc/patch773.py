#!/usr/bin/env python3
"""Build CX (on t771 -> t773): the Beginner floor's two checkpoints on paper, with a teacher key.
?book=check&floor=0a|0b : the student's pages (two parts of each room's check-up on paper, chapter by chapter)
?book=checkkey&floor=0a|0b : the teacher's key (the same parts' answers from each Teacher copy, and where to go back)
Fresh items: on the checkpoint pages every seeded generator gets its own seed, and the fixed check-up data of the
parts used is replaced by new items, so a child never meets the Workbook's check-up page again.
"""
import sys, re
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()

def nb(x):
    for _ in range(3): x = re.sub(r'(?<![A-Za-z0-9])([A-G0-9]) (?=[A-G0-9](?![A-Za-z0-9]))', '\\1\u00a0', x)
    return x
def R(old, new, n=1):
    global s
    if s.count(old) == 0 and s.count(nb(old)) > 0: old, new = nb(old), nb(new)
    c = s.count(old)
    assert c == n, (c, n, old[:120])
    s = s.replace(old, new)

# 1. the route, read before any seeded data is made
R("""const { useState, useEffect, useRef, useMemo } = React;\n""",
  """const { useState, useEffect, useRef, useMemo } = React;
// Build CX: the paper checkpoints (?book=check|checkkey&floor=0a). Read first, before any seeded data is made, so every
// generator, and the fixed check-up data of the parts a checkpoint uses, give the checkpoint its own items.
const CKP = (() => { try { const q = new URLSearchParams(location.search), b = q.get('book'); return b === 'check' || b === 'checkkey' ? { key: q.get('floor') || '0a', teacher: b === 'checkkey' } : null; } catch (e) { return null; } })();
""", 1)
R("""function withSeed(key, fn) { const r = Math.random; Math.random = bkRand(bkHash(key));""",
  """function withSeed(key, fn) { const r = Math.random; Math.random = bkRand(bkHash((CKP ? 'ckp-' + CKP.key + ':' : '') + key));""")

# 2. fresh items for the fixed data of the parts used
R("""const PH_FILL_CHK = [""", """const PH_FILL_CHK = CKP ? [['1', '?2', '3', '4', '5'], ['5', '4', '3', '?2', '1'], ['3', '?4', '5'], ['5', '?4', '3', '4', '5']] : [""")
R("""wh: shuffle([0, 4, 2, 6])""", """wh: shuffle(CKP ? [1, 5, 3, 2] : [0, 4, 2, 6])""")
R("""const NN_CHK_WORDS = ['BAG', 'FACE'];""", """const NN_CHK_WORDS = CKP ? ['BEAD', 'CAGE'] : ['BAG', 'FACE'];""")
R("""    tr: shuffle([29, 30, 31, 32]),
    ba: shuffle([25, 26, 27, 24]),""", """    tr: shuffle(CKP ? [28, 29, 31, 32] : [29, 30, 31, 32]),
    ba: shuffle(CKP ? [24, 26, 27, 28] : [25, 26, 27, 24]),""")
R("""  q: shuffle([30, 33, 36, 38]),
  k: shuffle([18, 21, 25, 26]),""", """  q: shuffle(CKP ? [32, 35, 31, 37] : [30, 33, 36, 38]),
  k: shuffle(CKP ? [20, 23, 24, 19] : [18, 21, 25, 26]),""")
def after_obj(name, add):
    global s
    m = re.search(r'^const ' + name + r' = \{\n', s, re.M); assert m, name
    e = s.index('\n};\n', m.end()) + 4
    s = s[:e] + add + '\n' + s[e:]
after_obj('PL_CHK', "if (CKP) Object.assign(PL_CHK, { fill: [{ 1: 2, 6: 3 }, { 3: 4, 4: 1 }, { 0: 1, 7: 4 }, { 2: 3, 5: 2 }], sounds: [['bird', 'bird', 'bird', 'turtle'], ['turtle', 'turtle', 'bird', 'turtle'], ['bird', 'turtle', 'turtle', 'bird'], ['bird', 'bird', 'bird', 'bird']] });   // Build CX")
after_obj('HP_WB', "if (CKP) Object.assign(HP_WB.chk, { c: [['R', 5], ['L', 2], ['R', 3], ['L', 4]], where: [['C', 'R'], ['G', 'L'], ['G', 'R'], ['C', 'L']] });   // Build CX")
after_obj('NV_CHK', "if (CKP) Object.assign(NV_CHK, { name: ['q', 'w', 'h', 'hd', 'q', 'h'], count: [[['h', 2], ['q', 1], ['q', 1]], [['hd', 3], ['q', 1]]] });   // Build CX")
after_obj('SDY_CHK', "if (CKP) Object.assign(SDY_CHK, { order: ['mf', 'p', 'f', 'pp'], touch: [['legato', [28, 29, 30, 31]], ['staccato', [31, 30, 29, 30]]] });   // Build CX")
after_obj('SSK_CHK', "if (CKP) Object.assign(SSK_CHK, { ss: [['treble', 33, 31], ['bass', 21, 22], ['treble', 30, 30], ['bass', 24, 26]], fing: [{ clef: 'treble', pos: 'C', hand: 'rh', items: sskW([29, 31, 28, 32]) }, { clef: 'bass', pos: 'C', hand: 'lh', items: sskW([21, 22, 24, 25]) }] });   // Build CX")
after_obj('TS_CHK', "if (CKP) Object.assign(TS_CHK, { bl: { top: 3, bars: [['q', 'q', 'q'], ['h', 'q'], ['hd']] }, sig: [{ top: 3, bars: [['h', 'q']] }, { top: 4, bars: [['q', 'q', 'h']] }] });   // Build CX")
after_obj('TN_CHK', "if (CKP) Object.assign(TN_CHK, { half: [['w1', -1], ['b3', 1], ['w5', 1], ['w6', -1]], names: ['b5', 'b0', 'b3'] });   // Build CX")

# 3. a part's letter on its header and on its answers, so a checkpoint can show only the parts it uses
R("""const bkSec = (letter, title) => <div style={{display:'flex',alignItems:'center',gap:9,margin:'7px 0 3px'}}>""",
  """const bkSec = (letter, title) => <div data-sec={letter} style={{display:'flex',alignItems:'center',gap:9,margin:'7px 0 3px'}}>""")
R("""const tcAns = (label, list, n0 = 1) => <div style={{fontSize:12,""", """const tcAns = (label, list, n0 = 1) => <div data-sec={label} style={{fontSize:12,""")

# 4. a page's own head, and the teacher key mode of TcBlock
R("""function WbPage({ no, chId, children, bare, teacher }) {""", """function WbPage({ no, chId, children, bare, teacher, head, left }) {""")
R("""      {!bare && <VicHead left={teacher ? <b style={{color:BK.coral}}>Teacher copy</b> : t('Workbook', '워크북')} right={chId === 'front' ?""",
  """      {!bare && <VicHead left={left || (teacher ? <b style={{color:BK.coral}}>Teacher copy</b> : t('Workbook', '워크북'))} right={head ? head : chId === 'front' ?""")
R("""function TcBlock({ page, title, answers, watch, say, goBack }) {
  return (""", """const CkpKeyCtx = React.createContext(null);   // Build CX: a checkpoint key collects one Teacher copy's check-up answers
function TcBlock({ page, title, answers, watch, say, goBack }) {
  const K = React.useContext(CkpKeyCtx);
  if (K) {   // key mode: only the check-up block, only the parts the checkpoint uses, drawn in the key's own slot
    if (!K.el || !/^(The check-up on paper|Check-up)/.test(title || '')) return null;
    const kids = React.Children.toArray(answers && answers.props && answers.props.children !== undefined ? answers.props.children : answers)
      .filter(c => c && c.props && c.props['data-sec'] != null && String(c.props['data-sec']).split(' · ').some(L => K.secs.includes(L)));
    return ReactDOM.createPortal(<div className="ckp-key-ans">{kids}</div>, K.el);
  }
  return (""")

# 5. the checkpoint books
CKP_JS = r"""
// ─── Build CX: the floor checkpoints on paper ───
// Two parts of each room's check-up on paper (the Workbook's last page), chapter by chapter, with fresh items; the
// teacher's key takes the same parts' answers from each Teacher copy. Not a mock exam: no score, no pass mark; a part
// with any wrong answer means that room is visited again (the last page has the list to tick).
const CKP_ROOMS = {
  'posture-hands': { secs: ['A', 'E'], back: { A: [1, 2], E: [5, 6] }, Paper: () => <PhPaperCheck/> },
  'first-steps': { secs: ['C', 'D'], back: { C: [2, 3], D: [3, 4] }, Paper: () => <FsPaperCheck/> },
  pulse: { secs: ['B', 'D'], back: { B: [2, 3], D: [4, 5] }, Paper: () => <PlPaperCheck/> },
  'note-names': { secs: ['A', 'E'], back: { A: ['1 and 4', '2 and 5'], E: [6, 7] }, Paper: () => <NnPaperCheck/> },
  'hand-positions': { secs: ['A', 'C'], back: { A: [1, 2], C: [3, 4] }, Paper: () => <HpPaperCheck/> },
  'ear-prep': { secs: ['A', 'B'], back: { A: [1, 2], B: [3, 4] }, Paper: () => <EpCkpPaper/>, key: () => <EpCkpKey/> },
  'note-values': { secs: ['A', 'C'], back: { A: ['1 to 3', '2 to 4'], C: ['2 and 3', '3 and 4'] }, Paper: () => <NvPaperCheck/> },
  dynamics: { secs: ['A', 'D'], back: { A: [2, 3], D: [4, 5] }, Paper: () => <SdyPaperCheck/> },
  staff: { secs: ['C', 'D'], back: { C: [3, 4], D: [4, 5] }, Paper: () => <SfPaperCheck/> },
  'reading-steps': { secs: ['B', 'C'], back: { B: [2, 3], C: [3, 4] }, Paper: () => <SskPaperCheck/> },
  'whole-staff': { secs: ['B', 'C'], back: { B: [2, 3], C: [3, 4] }, Paper: () => <WsPaperCheck/> },
  'time-signatures': { secs: ['A', 'B'], back: { A: [1, 2], B: [2, 3] }, Paper: () => <TsPaperCheck/> },
  tones: { secs: ['A', 'D'], back: { A: [1, 2], D: [4, 5] }, Paper: () => <TnPaperCheck/> },
};
// which rooms share a printed page (measured, so no page overflows)
const CKP_PAGES = { '0a': [['posture-hands', 'first-steps'], ['pulse', 'note-names'], ['hand-positions', 'ear-prep'], ['note-values']], '0b': [['dynamics', 'staff'], ['reading-steps', 'whole-staff'], ['time-signatures', 'tones']] };
const ckpFloor = (fk) => checkFloors().find(f => f.key === fk) || null;
const ckpTitle = (f) => floorName(f.k) + ' checkpoint' + (f.part ? ' ' + f.part : '');
const ckpChapters = (ids) => 'Chapters ' + bkChapterNo(ids[0]) + ' to ' + bkChapterNo(ids[ids.length - 1]);
// Ear Prep has no Workbook: two listening parts, the teacher plays
function EpCkpPaper() {
  const opt = (k, ic, w) => <div key={k} style={{display:'flex',flexDirection:'column',alignItems:'center',gap:3}}>{ic}<span style={{fontSize:11.5,fontWeight:800,color:BK.ink}}>{w}</span></div>;
  return <div className="lb-paper" style={{display:'flex',flexDirection:'column',gap:4}}>
    {bkSec('A', 'Your teacher plays one note. Circle the turtle (low), middle C or the bird (high).')}
    <BkGrid cols={2} gap="6px 10px">{[1, 2, 3, 4].map(n => <BkCell key={n} n={n}><div style={{display:'flex',justifyContent:'center',alignItems:'flex-end',gap:22,padding:'14px 4px 4px'}}>{[opt('t', turtleIcon(36), 'low'), opt('m', lsMidC(32), 'middle C'), opt('b', birdIcon(36), 'high')]}</div></BkCell>)}</BkGrid>
    {bkSec('B', 'Your teacher plays two short tunes. Circle same or different.')}
    <BkGrid cols={4} gap="6px 8px">{[5, 6, 7, 8].map(n => <BkCell key={n} n={n}><div style={{display:'flex',flexDirection:'column',alignItems:'center',gap:9,padding:'16px 4px 6px',fontSize:13.5,fontWeight:800,color:BK.ink}}><span>same</span><span>different</span></div></BkCell>)}</BkGrid>
  </div>;
}
function EpCkpKey() {
  const line = (n0) => [0, 1, 2, 3].map(i => <span key={i} style={{marginRight:12,whiteSpace:'nowrap'}}><i style={{color:BK.muted}}>{n0 + i}</i> <span style={{display:'inline-block',width:58,borderBottom:'1px solid ' + BK.ink}}>&nbsp;</span></span>);
  return <div className="ckp-key-ans" style={{fontSize:12,color:BK.ink,lineHeight:1.65}}>
    <div data-sec="A"><b style={{color:BK.muted,fontSize:10.5,letterSpacing:'0.06em'}}>A</b>  Your choice, as the app does: low, two octaves below middle C; middle, near middle C; high, two octaves above. Write what you played: {line(1)}</div>
    <div data-sec="B"><b style={{color:BK.muted,fontSize:10.5,letterSpacing:'0.06em'}}>B</b>  Two short tunes of four notes; for different, change one note. Write same or different: {line(5)}</div>
  </div>;
}
function CkpRoomHead({ id }) {
  return <div style={{display:'flex',alignItems:'baseline',gap:10,borderTop:'2.2px solid ' + BK.ink,paddingTop:5,marginTop:4}}>
    <span style={{fontSize:10,fontWeight:900,color:'#fff',background:BK.ink,padding:'2px 7px',letterSpacing:'0.08em'}}>{bkChapterNo(id)}</span>
    <span style={{fontFamily:LB_SERIF,fontSize:18,fontWeight:800,color:BK.ink}}>{bkChapterName(id)}</span></div>;
}
// one room's two parts: its check-up page drawn whole, then everything but the two parts hidden
function CkpRoomPaper({ id }) {
  const R = CKP_ROOMS[id], box = useRef(null);
  React.useLayoutEffect(() => {
    const el = box.current && box.current.querySelector('.lb-paper'); if (!el) return;
    let cur = null;
    [...el.children].forEach(c => { const sec = c.getAttribute('data-sec'); if (sec != null) cur = sec;
      const on = cur != null && cur.split(' · ').some(L => R.secs.includes(L)); if (!on) c.style.display = 'none'; });   // a shown part keeps its own display (flex, grid)
    el.style.flex = '0 0 auto';
  });
  return <div className="ckp-room" data-ckp-room={id} style={{display:'flex',flexDirection:'column',gap:2}}><CkpRoomHead id={id}/><div ref={box}>{R.Paper()}</div></div>;
}
function CkpPaperBook({ fk }) {
  const f = ckpFloor(fk), groups = (CKP_PAGES[fk] || []).map(g => g.filter(id => CKP_ROOMS[id]));
  if (!f || !groups.length) return <p style={{textAlign:'center',fontSize:16,margin:'40px 16px'}}>No checkpoint on paper for “{fk}” yet.</p>;
  const ids = groups.flat(), last = groups.length - 1;
  return <>{groups.map((g, gi) => <WbPage key={gi} no={gi + 1} chId={g[0]} left="Checkpoint" head={ckpTitle(f) + ' · ' + ckpChapters(ids)}>
    {gi === 0 && <div style={{display:'flex',alignItems:'flex-end',justifyContent:'space-between',gap:12,flexWrap:'wrap',margin:'0 0 6px'}}>
      <div><div style={{fontFamily:LB_SERIF,fontSize:30,fontWeight:900,color:BK.ink,lineHeight:1.05}}>{ckpTitle(f)}</div>
        <div style={{fontSize:13.5,color:BK.ink,marginTop:3}}>Show what you remember! {ckpChapters(ids)}, two parts from each. No piano, no help, about 15 minutes.</div></div>
      <span style={{fontSize:12,color:BK.muted}}>Name <span style={{display:'inline-block',width:120,borderBottom:'1px solid ' + BK.ink}}>&nbsp;</span>  Date <span style={{display:'inline-block',width:60,borderBottom:'1px solid ' + BK.ink}}>&nbsp;</span></span></div>}
    <div style={{display:'flex',flexDirection:'column',gap:10}}>{g.map(id => <CkpRoomPaper key={id} id={id}/>)}</div>
    {gi === last && <div className="ckp-end" style={{display:'flex',gap:16,alignItems:'stretch',marginTop:'auto',paddingTop:10}}>
      <div style={{flex:1,...VIC_PANEL,padding:'8px 12px'}}><div style={{fontSize:12.5,fontWeight:900,color:BK.ink,marginBottom:4}}>Rooms to visit again (your teacher ticks)</div>
        <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:'3px 14px'}}>{ids.map(id => <span key={id} style={{display:'flex',alignItems:'center',gap:7,fontSize:12.5,color:BK.ink}}><span style={{flex:'0 0 auto',width:14,height:14,border:'1.4px solid ' + BK.green,borderRadius:2}}/>{bkChapterNo(id) + ' ' + bkChapterName(id)}</span>)}</div></div>
      <div style={{flex:'0 0 auto',width:118,display:'flex',alignItems:'center',justifyContent:'center'}}><div style={{width:104,height:104,borderRadius:52,border:'2px dashed ' + BK.coral,display:'flex',alignItems:'center',justifyContent:'center',textAlign:'center',fontSize:12,fontWeight:900,color:BK.coral,lineHeight:1.3,letterSpacing:'0.04em'}}>CHECKPOINT<br/>DONE!</div></div>
    </div>}
  </WbPage>)}</>;
}
// one room's answers: its Teacher copy drawn hidden; its check-up block sends the two parts' answers here
function CkpRoomKey({ id }) {
  const R = CKP_ROOMS[id], [el, setEl] = useState(null), Teacher = TEACHER_COPIES[id];
  const back = Object.entries(R.back).map(([L, [st, pg]]) => L + ' → step ' + st + ' (Lesson Book page ' + pg + ')').join(' · ');
  return <div className="ckp-room-key" data-ckp-room={id} style={{breakInside:'avoid'}}>
    <CkpRoomHead id={id}/>
    {R.key ? R.key() : <div ref={setEl} className="ckp-key-slot" style={{marginTop:3}}/>}
    {!R.key && el && Teacher && <CkpKeyCtx.Provider value={{ el, secs: R.secs }}><div style={{display:'none'}}><Teacher/></div></CkpKeyCtx.Provider>}
    <div style={{fontSize:11.5,color:BK.ink,marginTop:2}}><b style={{color:BK.coral}}>Any wrong: visit again.</b> {back}</div>
  </div>;
}
function CkpKeyBook({ fk }) {
  const f = ckpFloor(fk), ids = (CKP_PAGES[fk] || []).flat().filter(id => CKP_ROOMS[id]);
  if (!f || !ids.length) return <p style={{textAlign:'center',fontSize:16,margin:'40px 16px'}}>No checkpoint key for “{fk}” yet.</p>;
  const css = '.ckp-key-ans [data-sec] { margin-bottom: 1px }';
  return <WbPage no={1} chId={ids[0]} teacher head={ckpTitle(f) + ' · key'}>
    <style>{css}</style>
    <div style={{fontFamily:LB_SERIF,fontSize:26,fontWeight:900,color:BK.ink,margin:'2px 0 2px'}}>Key · {ckpTitle(f)}</div>
    <div style={{fontSize:12.5,color:BK.muted,margin:'0 0 8px',lineHeight:1.5}}>{ckpChapters(ids)}, two parts of each room's check-up on paper, with new items (the Workbook's own check-up page is never repeated). Not a mock exam: no score, no pass mark. A part with any wrong answer means that room is visited again: tick it on the student's last page, and go back to the step shown.</div>
    <div style={{display:'flex',flexDirection:'column',gap:8}}>{ids.map(id => <CkpRoomKey key={id} id={id}/>)}</div>
  </WbPage>;
}
"""
R("""function BookRoot({ kind, ch }) {""", CKP_JS + """
function BookRoot({ kind, ch }) {""")
R("""  const fixed = kind === 'concept' || kind === 'spread' || kind === 'work' || kind === 'teacher' || kind === 'cutouts' || (kind === 'lesson' && ids.every(id => LESSON_BOOKS[id]));""",
  """  const fixed = kind === 'check' || kind === 'checkkey' || kind === 'concept' || kind === 'spread' || kind === 'work' || kind === 'teacher' || kind === 'cutouts' || (kind === 'lesson' && ids.every(id => LESSON_BOOKS[id]));""")
R("""      {fixed
        ? kind === 'spread' ?""", """      {fixed
        ? kind === 'check' ? <CkpPaperBook fk={(CKP && CKP.key) || '0a'}/> : kind === 'checkkey' ? <CkpKeyBook fk={(CKP && CKP.key) || '0a'}/>
        : kind === 'spread' ?""")
R("""printParams.get('book') === 'spread' || printParams.get('book') === 'concept')) {""", """printParams.get('book') === 'spread' || printParams.get('book') === 'concept' || printParams.get('book') === 'check' || printParams.get('book') === 'checkkey')) {""")

# 6. the Books shelf: each checkpoint right after the last room it checks
R("""          {st.ids.map(id => (
            <div key={id} style={{display:'flex',alignItems:'center',gap:'4px 10px',flexWrap:'wrap',padding:'6px 0',borderTop:'1px solid #efe9d9'}}>""",
  """          {st.ids.map(id => [
            <div key={id} style={{display:'flex',alignItems:'center',gap:'4px 10px',flexWrap:'wrap',padding:'6px 0',borderTop:'1px solid #efe9d9'}}>""")
R("""                {LESSON_BOOKS[id] && WORKBOOKS[id] && pill('spread', id, t('Lesson + Workbook, side by side', '레슨북 + 워크북 나란히'), true)}
              </span>
            </div>
          ))}""", """                {LESSON_BOOKS[id] && WORKBOOKS[id] && pill('spread', id, t('Lesson + Workbook, side by side', '레슨북 + 워크북 나란히'), true)}
              </span>
            </div>,
            ...checkFloors().filter(f => f.k === st.n && CKP_PAGES[f.key] && f.ids[f.ids.length - 1] === id).map(f => (   // Build CX
              <div key={'ckp-' + f.key} data-testid={'ckp-shelf-' + f.key} style={{display:'flex',alignItems:'center',gap:'4px 10px',flexWrap:'wrap',padding:'7px 0',borderTop:'1px solid #efe9d9',background:'linear-gradient(90deg, rgba(228,87,46,0.06), transparent)'}}>
                <span style={{flex:'1 1 150px',fontSize:14,fontWeight:800,color:'var(--navy)'}}>{t('Checkpoint', '중간점검') + (f.part ? ' ' + f.part : '')}<span style={{color:'var(--muted)',fontWeight:600,fontSize:12,marginLeft:8}}>{t('on paper, chapters ', '종이로, 챕터 ') + bkChapterNo(f.ids[0]) + '–' + bkChapterNo(f.ids[f.ids.length - 1])}</span></span>
                <span style={{display:'flex',gap:5,flexWrap:'wrap'}}>
                  <a href={'?book=check&floor=' + f.key + '&lang=en'} target="_blank" rel="noopener" style={{fontSize:11.5,fontWeight:800,color:KIND.work.col,border:'1.5px solid ' + KIND.work.col,borderRadius:8,padding:'3px 9px',textDecoration:'none',background:'#fff',whiteSpace:'nowrap'}}>{t('Student', '학생용')}</a>
                  <a href={'?book=checkkey&floor=' + f.key + '&lang=en'} target="_blank" rel="noopener" style={{fontSize:11.5,fontWeight:800,color:KIND.teacher.col,border:'1.5px solid ' + KIND.teacher.col,borderRadius:8,padding:'3px 9px',textDecoration:'none',background:'#fff',whiteSpace:'nowrap'}}>{t('Key', '정답')}</a>
                </span>
              </div>)),
          ])}""")

open(dst, 'w', encoding='utf-8').write(s)
print('ok', len(s))
