#!/usr/bin/env python3
"""Build DM (on t787 -> t788; the board's next step after the split): own check-up items for the split Grades 2 and 3 rooms.
Until now a split room's check-up on paper was the base room's page with the other grade's parts hidden (numbered from the
middle), and Scales, Grade 2's parts asked Grade 3 keys. Now each room's Workbook ends with a check-up of its own, parts A..
from item 1, built from the room's own grade: Scales, Grade 2 (black-key thumbs, thumbs meeting, mirror twins, the chromatic
scale from D, all in the Grade 2 keys); Scales, Grade 3 (C melodic minor's raised and lowered notes, mirror twins in the
Grade 3 keys, the chromatic scale from A and E flat, thumbs meeting in the Grade 3 keys by chapter 32's rule); Intervals,
Grade 2 (name the interval above the tonic; major, minor or perfect); Chords and Cadences, Grade 3 (the degree names, the
chord with its inversion, perfect or plagal); Rhythm, Grade 2 (counts under semiquavers and triplets; how many); Rhythm,
Grade 3 (counts under dotted quavers, the minim beat and 9/8; beats in a bar; simple or compound). The teacher copies' answer
blocks and the floor checkpoints (CKP_ROOMS) follow. The three melody rooms keep no check-up page: their Workbook page is
the writing itself, which the teacher marks.
"""
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def R(old, new, n=1):
    global s
    c = s.count(old); assert c == n, (c, n, old[:120]); s = s.replace(old, new)
ALL = "['A', 'B', 'C', 'D']"

# ── Scales ──
R("""if (CKP) Object.assign(SCF_WB.chk, { meet: ['Bb', 'D', 'Gm', 'A'], chrom: [[1, 'R', 1], [0, 'L', 2], [2, 'L', 3], [0, 'R', 3]] });   // Build DF""",
  """if (CKP) Object.assign(SCF_WB.chk, { meet: ['Bb', 'D', 'Gm', 'A'], chrom: [[1, 'R', 1], [0, 'L', 2], [2, 'L', 3], [0, 'R', 3]] });   // Build DF
// Build DM: each room's own check-up, in its own grade's keys (the floor checkpoint takes the second set)
SCF_WB.chk2 = CKP
  ? { thumb: [['D', 'R'], ['Bb', 'L'], ['Bm', 'R'], ['Gm', 'R']], meet: ['Bb', 'Gm', 'D', 'Bm'], mirror: ['F', 'Dmh', 'G', 'Emh'], chrom: [[0, 'L', 1], [0, 'R', 3], [0, 'L', 3], [0, 'R', 2]] }
  : { thumb: [['Bb', 'L'], ['D', 'R'], ['Gm', 'L'], ['Bm', 'R']], meet: ['D', 'Bb', 'Bm', 'Gm'], mirror: ['G', 'F', 'Emh', 'Dmh'], chrom: [[0, 'R', 1], [0, 'L', 2], [0, 'R', 3], [0, 'L', 3]] };
SCF_WB.chk3 = CKP
  ? { mel: [['down', 7], ['up', 6], ['down', 6], ['up', 7]], mirror: ['Bb', 'Gmh', 'Bmh', 'D'], chrom: [[2, 'R', 1], [1, 'L', 3], [2, 'L', 2], [1, 'R', 3]], meet: ['Cm', 'A', 'Fsm', 'Eb'] }
  : { mel: [['up', 6], ['up', 7], ['down', 7], ['down', 6]], mirror: ['D', 'Bb', 'Bmh', 'Gmh'], chrom: [[1, 'R', 1], [2, 'L', 2], [1, 'L', 3], [2, 'R', 3]], meet: ['A', 'Eb', 'Cm', 'Fsm'] };
const scfwMel = ([dir, deg]) => (dir === 'up' ? SCF_MEL.Cm.up : SCF_MEL.Cm.dn.slice().reverse())[deg - 1];   // C melodic minor: the 6th or 7th going up or down""")
R("""function ScfPaperCheck() {
  const C = SCF_WB.chk;
  return <div className="lb-paper" style={{display:'flex',flexDirection:'column',gap:4}}>
    <LbPaperHead/>
    {bkSec('A', 'Which two letters does the thumb play?')}""",
  """function ScfPaperCheck({ g = 2 }) {   // Build DM: g = 2 Scales, Grade 2; g = 3 Scales, Grade 3 (its own parts)
  const C = g === 3 ? SCF_WB.chk3 : SCF_WB.chk2;
  if (g === 3) return <div className="lb-paper" style={{display:'flex',flexDirection:'column',gap:4}}>
    <LbPaperHead/>
    {bkSec('A', 'C melodic minor: write the note.')}
    <BkGrid cols={4} gap="6px 8px">{C.mel.map(([dir, deg], i) => <BkCell key={i} n={i + 1}><div style={{display:'grid',gap:4,padding:'14px 2px 2px',justifyItems:'center'}}><div style={{fontSize:11,fontWeight:900,color:BK.muted,textAlign:'center',lineHeight:1.25}}>{dir === 'up' ? 'going up' : 'coming down'}, the {deg}th</div>{bkBox(44, 24)}</div></BkCell>)}</BkGrid>
    {bkSec('B', 'Contrary motion from one note: mirror twins? Y or N')}
    <BkGrid cols={2} gap="6px 8px">{C.mirror.map((k, i) => <BkCell key={i} n={i + 5}><div style={{display:'grid',gridTemplateColumns:'1fr auto',alignItems:'center',gap:6,padding:'14px 0 0'}}><div><div style={{fontSize:10.5,fontWeight:900,color:BK.muted,textAlign:'center'}}>{scfCmName(k)}</div><ScfCmKb k={k} W={9} H={24}/></div>{bkBox(30, 24)}</div></BkCell>)}</BkGrid>
    {bkSec('C', 'Chromatic scale: which finger plays the red key?')}
    <BkGrid cols={4} gap="6px 8px">{C.chrom.map(([st, h, j], i) => { const s0 = SCF_CHROM[st][1]; return <BkCell key={i} n={i + 9}><div style={{display:'grid',gap:3,padding:'14px 0 0'}}>
      <div style={{fontSize:10,fontWeight:900,color:BK.muted,textAlign:'center',lineHeight:1.2}}>From {SCF_CHROM[st][0]}, {scfwHand(h)}</div><SpKb lo={s0} hi={s0 + 12} W={10} H={28} lit={{ [s0 + j]: 'cor' }} names={{ [s0]: SCF_CHROM[st][0] }} k={1}/>
      <div style={{display:'flex',justifyContent:'center'}}>{bkBox(30, 24)}</div></div></BkCell>; })}</BkGrid>
    {bkSec('D', 'Two octaves hands together: where do both thumbs play? (letters, or never)')}
    <BkGrid cols={2} gap="6px 8px">{C.meet.map((k, i) => <BkCell key={i} n={i + 13}><div style={{display:'flex',alignItems:'center',justifyContent:'space-between',gap:8,padding:'14px 4px 2px',fontSize:12.5,fontWeight:800,color:BK.ink}}>{SCF[k].en}{bkBox(100, 24)}</div></BkCell>)}</BkGrid>
  </div>;
  return <div className="lb-paper" style={{display:'flex',flexDirection:'column',gap:4}}>
    <LbPaperHead/>
    {bkSec('A', 'Which two letters does the thumb play?')}""")
R("""  return <>{g === 3 ? splitWb(pages, [], ['B', 'C', 'D'], startNo) : pages}</>;""",
  """  return <>{g === 3 ? [<WbPage key="chk" no={startNo + 1} chId={ch}><ScfPaperCheck g={3}/></WbPage>] : pages}</>;   // Build DM: its own check-up""")
R("""  P(<ScfPaperCheck/>);
  return <>{g === 3 ?""", """  P(<ScfPaperCheck g={2}/>);
  return <>{g === 3 ?""")
R("""  const finish = () => { if (one.length) pages.push(<SplitCtx.Provider key="one" value={{ steps: [3, 4, 5], secs: ['B', 'C', 'D'], pages: { 1: 1, 4: 2, 5: 3, 6: 4, 7: 5 } }}>""",
  """  const finish = () => { if (one.length) pages.push(<SplitCtx.Provider key="one" value={{ steps: [3, 4, 5], secs: """ + ALL + """, pages: { 1: 1, 4: 2, 5: 3, 6: 4, 7: 5 } }}>""")
R("""    <TcBlock page={7} title="The check-up on paper (the Workbook's last page)" answers={<>{tcAns('A', SCF_WB.chk.thumb.map(([k, h]) => scfwThumbs(k, h).join(', ')))}{tcAns('B', SCF_WB.chk.meet.map(scfwMeet), 5)}{tcAns('C', SCF_WB.chk.mirror.map(k => (scfMirror(k) ? 'Y' : 'N')), 9)}{tcAns('D', SCF_WB.chk.chrom.map(([st, h, j]) => String(scfChF(SCF_CHROM[st][1] + j, h, false))), 13)}
      <div style={{fontSize:12,color:BK.ink,marginTop:6,lineHeight:1.5}}>One mark for each answer. Score each part on its own (4 marks each, pass 3+). Not passed? Go back to that step's page: A p.2 · B p.3 · C p.5 · D p.6. Then hear each scale at the piano, from memory, at the grade's speed: an even run-ning through every turn.</div></>}/>""",
  """    {g === 3 ? <TcBlock page={7} title="The check-up on paper (the Workbook's last page)" answers={<>{tcAns('A', SCF_WB.chk3.mel.map(scfwMel))}{tcAns('B', SCF_WB.chk3.mirror.map(k => (scfMirror(k) ? 'Y' : 'N')), 5)}{tcAns('C', SCF_WB.chk3.chrom.map(([st, h, j]) => String(scfChF(SCF_CHROM[st][1] + j, h, false))), 9)}{tcAns('D', SCF_WB.chk3.meet.map(scfwMeet), 13)}
      <div style={{fontSize:12,color:BK.ink,marginTop:6,lineHeight:1.5}}>One mark for each answer. Score each part on its own (4 marks each, pass 3+). Not passed? Go back to that step's page: A p.2 · B p.3 · C p.4 · D: chapter {bkChapterNo('scales-23')}'s rule, thumbs meet or never. Then hear each scale at the piano, from memory, at the grade's speed.</div></>}/>
    : <TcBlock page={7} title="The check-up on paper (the Workbook's last page)" answers={<>{tcAns('A', SCF_WB.chk2.thumb.map(([k, h]) => scfwThumbs(k, h).join(', ')))}{tcAns('B', SCF_WB.chk2.meet.map(scfwMeet), 5)}{tcAns('C', SCF_WB.chk2.mirror.map(k => (scfMirror(k) ? 'Y' : 'N')), 9)}{tcAns('D', SCF_WB.chk2.chrom.map(([st, h, j]) => String(scfChF(SCF_CHROM[st][1] + j, h, false))), 13)}
      <div style={{fontSize:12,color:BK.ink,marginTop:6,lineHeight:1.5}}>One mark for each answer. Score each part on its own (4 marks each, pass 3+). Not passed? Go back to that step's page: A p.2 · B p.3 · C p.5 · D p.6. Then hear each scale at the piano, from memory, at the grade's speed: an even run-ning through every turn.</div></>}/>}""")

# ── Intervals, Grade 2 and Chords and Cadences, Grade 3 ──
R("""if (CKP) Object.assign(H3_WB.chk, { deg: [2, 6, 1, 5], cad: [['G', 'plagal'], ['Am', 'perfect'], ['F', 'plagal'], ['D', 'perfect']] });   // Build DF""",
  """if (CKP) Object.assign(H3_WB.chk, { deg: [2, 6, 1, 5], cad: [['G', 'plagal'], ['Am', 'perfect'], ['F', 'plagal'], ['D', 'perfect']] });   // Build DF
// Build DM: Intervals, Grade 2's own check-up: A name the interval above the tonic (treble, the step's keys); B major, minor or perfect
H3_WB.chk2 = CKP
  ? { iv: [['Em', 6, 'treble'], ['Dm', 2, 'treble'], ['Am', 5, 'treble'], ['Gm', 7, 'treble']], ql: [['Dm', 3, 'treble'], ['Am', 8, 'treble'], ['Em', 7, 'treble'], ['Gm', 4, 'treble']] }
  : { iv: [['Dm', 3, 'treble'], ['Am', 7, 'treble'], ['Em', 5, 'treble'], ['Gm', 6, 'treble']], ql: [['Am', 4, 'treble'], ['Em', 2, 'treble'], ['Dm', 6, 'treble'], ['Gm', 8, 'treble']] };""")
R("""function H3PaperCheck() {
  const SP = React.useContext(SplitCtx), C = SP && SP.steps.length === 1 ? { ...H3_WB.chk, iv: H3_WB.chk.iv.map(it => [it[0], it[1], 'treble']) } : H3_WB.chk;   // Build DG: Grade 2, treble only
  return <div className="lb-paper" style={{display:'flex',flexDirection:'column',gap:4}}>
    <LbPaperHead/>
    {bkSec('A', 'Name the interval above the tonic (M, m or P and the number).')}
    <BkGrid cols={4} gap="6px 8px">{C.iv.map((it, i) => { const [a, b] = h3Above(it[0], it[2], it[1]); return <BkCell key={i} n={i + 1}><div style={{display:'grid',gap:2,padding:'14px 0 0'}}><div style={{fontSize:10,fontWeight:900,color:BK.muted,textAlign:'center'}}>{H3_MIN[it[0]].en}</div><IntervalStaff clef={it[2]} notes={[a, b]} width={130}/><div style={{display:'flex',justifyContent:'center'}}>{bkBox(40, 24)}</div></div></BkCell>; })}</BkGrid>
    {bkSec('B', 'Write the name of the degree.')}
    <BkGrid cols={4} gap="6px 8px">{C.deg.map((d, i) => <BkCell key={i} n={i + 5}>""",
  """function H3PaperCheck({ g = 3 }) {   // Build DM: g = 2 Intervals, Grade 2 (its own two parts); g = 3 Chords and Cadences, Grade 3 (its own three, from item 1)
  const C = H3_WB.chk, ivCell = (it, i, n0) => { const [a, b] = h3Above(it[0], it[2], it[1]); return <BkCell key={i} n={i + n0}><div style={{display:'grid',gap:2,padding:'14px 0 0'}}><div style={{fontSize:10,fontWeight:900,color:BK.muted,textAlign:'center'}}>{H3_MIN[it[0]].en}</div><IntervalStaff clef={it[2]} notes={[a, b]} width={130}/><div style={{display:'flex',justifyContent:'center'}}>{bkBox(40, 24)}</div></div></BkCell>; };
  if (g === 2) return <div className="lb-paper" style={{display:'flex',flexDirection:'column',gap:4}}>
    <LbPaperHead/>
    {bkSec('A', 'Name the interval above the tonic (M, m or P and the number).')}
    <BkGrid cols={4} gap="6px 8px">{H3_WB.chk2.iv.map((it, i) => ivCell(it, i, 1))}</BkGrid>
    {bkSec('B', 'Major (M), minor (m) or perfect (P)?')}
    <BkGrid cols={4} gap="6px 8px">{H3_WB.chk2.ql.map((it, i) => ivCell(it, i, 5))}</BkGrid>
  </div>;
  const n0 = { deg: 1, inv: 5, cad: 9 }, L = { deg: 'A', inv: 'B', cad: 'C' };
  return <div className="lb-paper" style={{display:'flex',flexDirection:'column',gap:4}}>
    <LbPaperHead/>
    {bkSec(L.deg, 'Write the name of the degree.')}
    <BkGrid cols={4} gap="6px 8px">{C.deg.map((d, i) => <BkCell key={i} n={i + n0.deg}>""")
R("""    {bkSec('C', 'Name the chord: I, IV, V, Ib, IVb or Vb.')}
    <BkGrid cols={4} gap="6px 8px">{C.inv.map((it, i) => <BkCell key={i} n={i + 9}>""", """    {bkSec(L.inv, 'Name the chord: I, IV, V, Ib, IVb or Vb.')}
    <BkGrid cols={4} gap="6px 8px">{C.inv.map((it, i) => <BkCell key={i} n={i + n0.inv}>""")
R("""    {bkSec('D', 'Perfect (P) or plagal (Pl)?')}
    <BkGrid cols={4} gap="6px 8px">{C.cad.map(([k, id], i) => <BkCell key={i} n={i + 13}>""", """    {bkSec(L.cad, 'Perfect (P) or plagal (Pl)?')}
    <BkGrid cols={4} gap="6px 8px">{C.cad.map(([k, id], i) => <BkCell key={i} n={i + n0.cad}>""")
R("""  const pages = [], ch = g === 2 ? 'harmony-2' : 'harmony-3', STEPS = g === 2 ? [1] : [2, 3, 4, 5], secs = g === 2 ? ['A'] : ['B', 'C', 'D'];""",
  """  const pages = [], ch = g === 2 ? 'harmony-2' : 'harmony-3', STEPS = g === 2 ? [1] : [2, 3, 4, 5], secs = """ + ALL + """;   // Build DM: the check-up is the room's own""")
R("""    <TcBlock page={7} title="The check-up on paper (the Workbook's last page)" answers={<>{tcAns('A', H3_WB.chk.iv.map(h3wIv))}{tcAns('B', H3_WB.chk.deg.map(d => H3_DEGN[d - 1][0]), 5)}{tcAns('C', H3_WB.chk.inv.map(h3wInv), 9)}{tcAns('D', H3_WB.chk.cad.map(([k, id]) => (id === 'perfect' ? 'P' : 'Pl')), 13)}
      <div style={{fontSize:12,color:BK.ink,marginTop:6,lineHeight:1.5}}>One mark for each answer. Score each part on its own (4 marks each, pass 3+). Not passed? Go back to that step's page: {g === 2 ? 'A p.2' : 'B p.2 · C p.3 · D p.5'}. Then play each one at the piano.</div></>}/>""",
  """    {g === 2 ? <TcBlock page={7} title="The check-up on paper (the Workbook's last page)" answers={<>{tcAns('A', H3_WB.chk2.iv.map(h3wIv))}{tcAns('B', H3_WB.chk2.ql.map(([k, n]) => H3_QMIN[n]), 5)}
      <div style={{fontSize:12,color:BK.ink,marginTop:6,lineHeight:1.5}}>One mark for each answer. Score each part on its own (4 marks each, pass 3+). Not passed? Go back to the step's page: A and B p.2. Then play each interval at the piano.</div></>}/>
    : <TcBlock page={7} title="The check-up on paper (the Workbook's last page)" answers={<>{tcAns('A', H3_WB.chk.deg.map(d => H3_DEGN[d - 1][0]))}{tcAns('B', H3_WB.chk.inv.map(h3wInv), 5)}{tcAns('C', H3_WB.chk.cad.map(([k, id]) => (id === 'perfect' ? 'P' : 'Pl')), 9)}
      <div style={{fontSize:12,color:BK.ink,marginTop:6,lineHeight:1.5}}>One mark for each answer. Score each part on its own (4 marks each, pass 3+). Not passed? Go back to that step's page: A p.2 · B p.3 · C p.5. Then play each one at the piano.</div></>}/>}""")
R("""  return <>{splitWb(pages, g === 2 ? [1] : [2, 3, 4, 5], g === 2 ? ['A'] : ['B', 'C', 'D'], startNo)}</>;""",
  """  return <>{splitWb(pages, g === 2 ? [1] : [2, 3, 4, 5], """ + ALL + """, startNo)}</>;   // Build DM: the check-up page is the room's own""")
# H3Workbook's check page takes g
R("""  P(<H3PaperCheck/>);""", """  P(<H3PaperCheck g={g}/>);""")

# ── Rhythm ──
R("""function R2PaperCheck() {
  const rows = (items, n0) =>""", """// Build DM: each room's own check-up lines and items (the floor checkpoint takes the second set)
Object.assign(R2, {
  chk2A: { items: [['ts', 4], ['s4'], ['q'], ['p'], ['s4'], ['||']], g: 2 }, chk2B: { items: [['ts', 2], ['t3'], ['q'], ['|'], ['q'], ['t3'], ['||']], g: 2, so: { countFn: (p) => rqTripCount(p) } },
  chk3A: { items: [['ts', 4], ['ds'], ['q'], ['ds'], ['q'], ['||']], g: 3 }, chk3B: { items: [['ts', 2, 2], ['q'], ['q'], ['h'], ['|'], ['w'], ['||']], g: 3, unit: 2, clicks: 2, bpm: 96, so: { countStep: 1, heartStep: 2, countFn: (p) => rq22Count(p) } },
});
if (CKP) Object.assign(R2, { chk2A: { items: [['ts', 4], ['q'], ['s4'], ['s4'], ['p'], ['||']], g: 2 }, chk2B: { items: [['ts', 2], ['q'], ['t3'], ['|'], ['t3'], ['t3'], ['||']], g: 2, so: { countFn: (p) => rqTripCount(p) } },
  chk3A: { items: [['ts', 4], ['q'], ['ds'], ['ds'], ['q'], ['||']], g: 3 }, chk3B: { items: [['ts', 2, 2], ['h'], ['q'], ['q'], ['|'], ['h'], ['h'], ['||']], g: 3, unit: 2, clicks: 2, bpm: 96, so: { countStep: 1, heartStep: 2, countFn: (p) => rq22Count(p) } } });
const R2_CHK2 = CKP
  ? { how: [['quavers in a triplet', 3], ['semiquavers in a minim', 8], ['notes in a duplet', 2], ['semiquavers in a quaver', 2]] }
  : { how: [['semiquavers in a crotchet', 4], ['quavers in a triplet', 3], ['semiquavers in a minim', 8], ['notes in a duplet', 2]] };
const R2_CHK3 = CKP
  ? { beats: [['2/2', '2'], ['9/8', '3 (dotted crotchets)'], ['3/2', '3'], ['3/8', '3']], kind: [['3/2', 'S'], ['9/8', 'C'], ['2/2', 'S'], ['6/8', 'C']] }
  : { beats: [['3/2', '3'], ['2/2', '2'], ['3/8', '3'], ['9/8', '3 (dotted crotchets)']], kind: [['9/8', 'C'], ['3/8', 'S'], ['6/8', 'C'], ['3/2', 'S']] };
function R2PaperCheck({ g = 3 }) {   // Build DM: g = 2 Rhythm, Grade 2 (counts; how many); g = 3 Rhythm, Grade 3 (counts; beats in a bar; simple or compound)
  const rows = (items, n0) => <BkGrid cols={2} gap="6px 8px">{items.map(([l, w], i) => <BkCell key={i} n={i + n0}><div style={{display:'flex',alignItems:'center',justifyContent:'space-between',gap:8,padding:'14px 4px 2px',fontSize:12.5,fontWeight:800,color:BK.ink}}>{l}{bkBox(w || 44, 24)}</div></BkCell>)}</BkGrid>;
  const lines = (keys) => <div style={{display:'grid',gap:6}}>{keys.map((k, i) => <BkCell key={k} n={i === 0 ? '1–2' : '3–4'}><div style={{padding:'14px 2px 0'}}>{r2El(k, { counts: 'blank', hearts: true })}</div></BkCell>)}</div>;
  if (g === 2) return <div className="lb-paper" style={{display:'flex',flexDirection:'column',gap:4}}>
    <LbPaperHead/>
    {bkSec('A', 'Write the counts under the notes.')}
    {lines(['chk2A', 'chk2B'])}
    {bkSec('B', 'How many?')}
    {rows(R2_CHK2.how.map(([l]) => [l]), 5)}
  </div>;
  return <div className="lb-paper" style={{display:'flex',flexDirection:'column',gap:4}}>
    <LbPaperHead/>
    {bkSec('A', 'Write the counts under the notes.')}
    {lines(['chk3A', 'chk3B'])}
    {bkSec('B', 'How many beats in a bar?')}
    {rows(R2_CHK3.beats.map(([l]) => [l]), 5)}
    {bkSec('C', 'Simple (S) or compound (C)?')}
    {rows(R2_CHK3.kind.map(([l]) => [l]), 9)}
  </div>;
}
function R2PaperCheckBase() {   // the mixed room's page (kept for the record; no room prints it now)
  const rows = (items, n0) =>""")
R("""  const pages = [], ch = g === 2 ? 'rhythm-2' : 'rhythm-3', STEPS = g === 2 ? [1, 3] : [2, 4, 5], secs = g === 2 ? ['B'] : ['A', 'C', 'D'];""",
  """  const pages = [], ch = g === 2 ? 'rhythm-2' : 'rhythm-3', STEPS = g === 2 ? [1, 3] : [2, 4, 5], secs = """ + ALL + """;   // Build DM: the check-up is the room's own""")
R("""    <TcBlock page={7} title="The check-up on paper (the Workbook's last page)" answers={<><div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:'4px 14px',marginBottom:4}}>{['chkA', 'chkB'].map(k => <div key={k} style={{maxWidth:300}}>{r2El(k, { counts: 'ans', hearts: false })}</div>)}</div>{tcAns('B', R2_CHK.how.map(x => String(x[1])), 5)}{tcAns('C', R2_CHK.beats.map(x => x[1]), 9)}{tcAns('D', R2_CHK.kind.map(x => x[1]), 13)}
      <div style={{fontSize:12,color:BK.ink,marginTop:6,lineHeight:1.5}}>Part A: one mark for each bar counted right (4 marks). Parts B to D: one mark each. Score each part on its own (4 marks each, pass 3+). Not passed? Go back: A p.2 and p.3 · B p.2 to p.4 · C p.5 and p.6 · D p.6. Then clap and count each line to you. Transposition (Grades 2 and 3, a melody of up to eight bars into another key of the grade) is in the Transposing lesson on the Home.</div></>}/>""",
  """    {g === 2 ? <TcBlock page={7} title="The check-up on paper (the Workbook's last page)" answers={<><div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:'4px 14px',marginBottom:4}}>{['chk2A', 'chk2B'].map(k => <div key={k} style={{maxWidth:300}}>{r2El(k, { counts: 'ans', hearts: false })}</div>)}</div>{tcAns('B', R2_CHK2.how.map(x => String(x[1])), 5)}
      <div style={{fontSize:12,color:BK.ink,marginTop:6,lineHeight:1.5}}>Part A: one mark for each bar counted right (4 marks). Part B: one mark each. Score each part on its own (4 marks each, pass 3+). Not passed? Go back: A p.2 and p.3 · B p.2 and p.3. Then clap and count each line to you. Transposition (a melody of up to eight bars into another key of the grade) is in the Transposing lesson on the Home.</div></>}/>
    : <TcBlock page={7} title="The check-up on paper (the Workbook's last page)" answers={<><div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:'4px 14px',marginBottom:4}}>{['chk3A', 'chk3B'].map(k => <div key={k} style={{maxWidth:300}}>{r2El(k, { counts: 'ans', hearts: false })}</div>)}</div>{tcAns('B', R2_CHK3.beats.map(x => x[1]), 5)}{tcAns('C', R2_CHK3.kind.map(x => x[1]), 9)}
      <div style={{fontSize:12,color:BK.ink,marginTop:6,lineHeight:1.5}}>Part A: one mark for each bar counted right (4 marks). Parts B and C: one mark each. Score each part on its own (4 marks each, pass 3+). Not passed? Go back: A p.2 and p.3 · B p.3 and p.4 · C p.4. Then clap and count each line to you. Transposition (a melody of up to eight bars into another key of the grade) is in the Transposing lesson on the Home.</div></>}/>}""")
R("""  return <>{splitWb(pages, g === 2 ? [1, 3] : [2, 4, 5], g === 2 ? ['B'] : ['A', 'C', 'D'], startNo)}</>;""",
  """  return <>{splitWb(pages, g === 2 ? [1, 3] : [2, 4, 5], """ + ALL + """, startNo)}</>;   // Build DM""")
R("""  P(<R2PaperCheck/>);""", """  P(<R2PaperCheck g={g}/>);""")

# ── the floor checkpoints ──
R("""  'scales-23': { secs: ['A', 'D'], back: { A: [1, 2], D: [5, 6] }, Paper: () => <ScfPaperCheck/> },   // Build DJ: Grade 2 asks these
  'scales-3': { secs: ['B', 'C'], back: { B: [1, 2], C: [2, 3] }, Paper: () => <ScfPaperCheck/> },""",
  """  'scales-23': { secs: ['A', 'D'], back: { A: [1, 2], D: [5, 6] }, Paper: () => <ScfPaperCheck g={2}/> },   // Build DM: each room's own items
  'scales-3': { secs: ['A', 'C'], back: { A: [2], C: [4] }, Paper: () => <ScfPaperCheck g={3}/> },""")
R("""  'harmony-2': { secs: ['A'], back: { A: [1, 2] }, Paper: () => <SplitCtx.Provider value={{ steps: [1], secs: ['A'], pages: {} }}><H3PaperCheck/></SplitCtx.Provider> },   // Build DG
  'harmony-3': { secs: ['B', 'D'], back: { B: [1, 2], D: [4, 5] }, Paper: () => <H3PaperCheck/> },
  'rhythm-2': { secs: ['B'], back: { B: ['1 and 2', '2 and 3'] }, Paper: () => <R2PaperCheck/> },   // Build DH
  'rhythm-3': { secs: ['C', 'D'], back: { C: ['2 and 3', '3 and 4'], D: ['1 and 3', '2 and 4'] }, Paper: () => <R2PaperCheck/> },""",
  """  'harmony-2': { secs: ['B'], back: { B: [2] }, Paper: () => <H3PaperCheck g={2}/> },   // Build DM: one part, so the page fits (the room's check-up on paper has both)
  'harmony-3': { secs: ['A', 'C'], back: { A: [2], C: [4, 5] }, Paper: () => <H3PaperCheck g={3}/> },
  'rhythm-2': { secs: ['B'], back: { B: ['2 and 3'] }, Paper: () => <R2PaperCheck g={2}/> },   // its part A (two lines of counts) is too tall for the checkpoint's page
  'rhythm-3': { secs: ['B', 'C'], back: { B: ['3 and 4'], C: ['2 and 4'] }, Paper: () => <R2PaperCheck g={3}/> },""")
open(dst, 'w', encoding='utf-8').write(s)
print('ok', len(s))
