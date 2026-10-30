#!/usr/bin/env python3
"""Build DF (on t780 -> t781): the Grade 2 and Grade 3 checkpoints on paper, as Prelim's and Grade 1's (DA, DC).
`?book=check&floor=3|4` and `?book=checkkey&floor=3|4` (two pages and a key each). Parts: Ear Training Grade 2 A B
(new, the teacher plays: higher or lower; same or different rhythm), Melody B C, Scales further B D; Ear Training
Grade 3 A B (new: which degree from the keynote; two or three), Intervals and chords further B D, Rhythm further C D.
Rhythm further's parts B to D were written out by hand in both the check and the key: now data (R2_CHK), with the
checkpoint's own items.
"""
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def R(old, new, n=1):
    global s
    c = s.count(old); assert c == n, (c, n, old[:120]); s = s.replace(old, new)
def after_obj(name, line):
    global s
    i = s.index('\nconst ' + name + ' = {'); j = s.index('\n};', i) + 3
    s = s[:j] + '\n' + line + s[j:]

# 1. fresh items on the checkpoint route
R("""MLX_CHK.qa = MLX_CHK.qa.slice(0, 2);   // Build AO: a question and an answer, side by side (room for section E)""",
  """MLX_CHK.qa = MLX_CHK.qa.slice(0, 2);   // Build AO: a question and an answer, side by side (room for section E)
if (CKP) Object.assign(MLX_CHK, { qa: [[mB([0, 1, 2, 0], 28), mB([1, 0, 1, 2], 29), mB([2, 1, 0, 1], 29), mW(28)], [mB([0, 2, 1, 3], 28), mB([2, 1, 0, 1], 29), mB([3, 2, 1, 0], 30), mW(32)]], word: ['phrasing', 'high point', 'repetition', 'question phrase'] });   // Build DF""")
R("""  chk: { thumb: [['Eb', 'L'], ['A', 'R'], ['Gm', 'L'], ['Fsm', 'L']], meet: ['A', 'Eb', 'Gm', 'Bm'], mirror: ['D', 'Bb', 'Emh', 'Gmh'], chrom: [[0, 'R', 1], [1, 'L', 2], [2, 'R', 1], [1, 'R', 3]] },
};""", """  chk: { thumb: [['Eb', 'L'], ['A', 'R'], ['Gm', 'L'], ['Fsm', 'L']], meet: ['A', 'Eb', 'Gm', 'Bm'], mirror: ['D', 'Bb', 'Emh', 'Gmh'], chrom: [[0, 'R', 1], [1, 'L', 2], [2, 'R', 1], [1, 'R', 3]] },
};
if (CKP) Object.assign(SCF_WB.chk, { meet: ['Bb', 'D', 'Gm', 'A'], chrom: [[1, 'R', 1], [0, 'L', 2], [2, 'L', 3], [0, 'R', 3]] });   // Build DF""")
R("""  chk: { iv: [['Dm', 3, 'treble'], ['Am', 7, 'bass'], ['Em', 5, 'treble'], ['Gm', 6, 'treble']], deg: [4, 7, 3, 5], inv: [['G', 1, 1, 'bass'], ['C', 4, 0, 'treble'], ['D', 5, 1, 'treble'], ['F', 1, 0, 'bass']], cad: [['D', 'perfect'], ['C', 'plagal'], ['Dm', 'plagal'], ['G', 'perfect']] },
};""", """  chk: { iv: [['Dm', 3, 'treble'], ['Am', 7, 'bass'], ['Em', 5, 'treble'], ['Gm', 6, 'treble']], deg: [4, 7, 3, 5], inv: [['G', 1, 1, 'bass'], ['C', 4, 0, 'treble'], ['D', 5, 1, 'treble'], ['F', 1, 0, 'bass']], cad: [['D', 'perfect'], ['C', 'plagal'], ['Dm', 'plagal'], ['G', 'perfect']] },
};
if (CKP) Object.assign(H3_WB.chk, { deg: [2, 6, 1, 5], cad: [['G', 'plagal'], ['Am', 'perfect'], ['F', 'plagal'], ['D', 'perfect']] });   // Build DF""")
# Rhythm further: parts B to D as data
R("""function R2PaperCheck() {""", """const R2_CHK = CKP   // Build DF: the checkpoint's own items
  ? { how: [['semiquavers in a minim', 8], ['quavers in a crotchet', 2], ['semiquavers in a quaver', 2], ['quavers in a triplet', 3]], beats: [['2/2', '2'], ['9/8', '3 (dotted crotchets)'], ['3/2', '3'], ['6/8', '2 (dotted crotchets)']], kind: [['3/2', 'S'], ['9/8', 'C'], ['2/2', 'S'], ['6/8', 'C']] }
  : { how: [['semiquavers in a crotchet', 4], ['semiquavers in a dotted quaver', 3], ['quavers in a triplet', 3], ['notes in a duplet', 2]], beats: [['3/2', '3'], ['2/2', '2'], ['3/8', '3'], ['9/8', '3 (dotted crotchets)']], kind: [['9/8', 'C'], ['3/8', 'S'], ['6/8', 'C'], ['3/2', 'S']] };
function R2PaperCheck() {""")
R("""    {rows([['semiquavers in a crotchet'], ['semiquavers in a dotted quaver'], ['quavers in a triplet'], ['notes in a duplet']], 5)}
    {bkSec('C', 'How many beats in a bar?')}
    {rows([['3/2'], ['2/2'], ['3/8'], ['9/8']], 9)}
    {bkSec('D', 'Simple (S) or compound (C)?')}
    {rows([['9/8'], ['3/8'], ['6/8'], ['3/2']], 13)}""", """    {rows(R2_CHK.how.map(([l]) => [l]), 5)}
    {bkSec('C', 'How many beats in a bar?')}
    {rows(R2_CHK.beats.map(([l]) => [l]), 9)}
    {bkSec('D', 'Simple (S) or compound (C)?')}
    {rows(R2_CHK.kind.map(([l]) => [l]), 13)}""")
R("""{tcAns('B', ['4', '3', '3', '2'], 5)}{tcAns('C', ['3', '2', '3', '3 (dotted crotchets)'], 9)}{tcAns('D', ['C', 'S', 'C', 'S'], 13)}""",
  """{tcAns('B', R2_CHK.how.map(x => String(x[1])), 5)}{tcAns('C', R2_CHK.beats.map(x => x[1]), 9)}{tcAns('D', R2_CHK.kind.map(x => x[1]), 13)}""")

# 2. the rooms
R("""  form: { secs: ['A', 'B'], back: { A: [2, 3], B: ['3 and 4', '4 and 5'] }, Paper: () => <FmxPaperCheck/> },
};""", """  form: { secs: ['A', 'B'], back: { A: [2, 3], B: ['3 and 4', '4 and 5'] }, Paper: () => <FmxPaperCheck/> },
  // Build DF: Grades 2 and 3
  'listen-23': { secs: ['A', 'B'], back: { A: [1, 2], B: [2, 3] }, Paper: () => <L2CkpPaper g={2}/>, key: () => <L2CkpKey g={2}/> },
  melody: { secs: ['B', 'C'], back: { B: [3, 4], C: ['1 to 5', '2 to 6'] }, Paper: () => <MlxPaperCheck/> },
  'scales-23': { secs: ['B', 'D'], back: { B: [2, 3], D: [5, 6] }, Paper: () => <ScfPaperCheck/> },
  'listen-3': { secs: ['A', 'B'], back: { A: [2, 3], B: [3, 4] }, Paper: () => <L2CkpPaper g={3}/>, key: () => <L2CkpKey g={3}/> },
  'harmony-23': { secs: ['B', 'D'], back: { B: [2, 3], D: [5, 6] }, Paper: () => <H3PaperCheck/> },
  'rhythm-23': { secs: ['C', 'D'], back: { C: ['4 and 5', '5 and 6'], D: ['3 and 5', '4 and 6'] }, Paper: () => <R2PaperCheck/> },
};""")
R("""const CKP_PAGES = { '2': [""", """const CKP_PAGES = { '3': [['listen-23', 'melody'], ['scales-23']], '4': [['listen-3', 'harmony-23'], ['rhythm-23']], '2': [""")
R("""function CkpRoomHead({ id }) {""", """// Ear Training, Grades 2 and 3: two listening parts, the teacher plays (Build DF)
function L2CkpPaper({ g }) {
  const pick = (ws) => <div style={{display:'flex',flexDirection:'column',alignItems:'center',gap:ws.length > 2 ? 4 : 9,padding:'14px 4px 6px',fontSize:13.5,fontWeight:800,color:BK.ink}}>{ws.map(w => <span key={w}>{w}</span>)}</div>;
  return <div className="lb-paper" style={{display:'flex',flexDirection:'column',gap:4}}>
    {g === 3
      ? <>{bkSec('A', 'Your teacher plays the keynote, then another note. Circle which it is.')}
        <BkGrid cols={4} gap="6px 8px">{[1, 2, 3, 4].map(n => <BkCell key={n} n={n}>{pick(['2nd', '3rd', '4th', '5th'])}</BkCell>)}</BkGrid>
        {bkSec('B', 'Your teacher plays an accompaniment. Circle in two or in three.')}
        <BkGrid cols={4} gap="6px 8px">{[5, 6, 7, 8].map(n => <BkCell key={n} n={n}>{pick(['in two', 'in three'])}</BkCell>)}</BkGrid></>
      : <>{bkSec('A', 'Your teacher plays two notes together, then one of them alone. Circle higher or lower.')}
        <BkGrid cols={4} gap="6px 8px">{[1, 2, 3, 4].map(n => <BkCell key={n} n={n}>{pick(['the higher', 'the lower'])}</BkCell>)}</BkGrid>
        {bkSec('B', 'Your teacher claps a rhythm twice, then once more. Circle same or different.')}
        <BkGrid cols={4} gap="6px 8px">{[5, 6, 7, 8].map(n => <BkCell key={n} n={n}>{pick(['same', 'different'])}</BkCell>)}</BkGrid></>}
  </div>;
}
function L2CkpKey({ g }) {
  const line = (n0) => [0, 1, 2, 3].map(i => <span key={i} style={{marginRight:12,whiteSpace:'nowrap'}}><i style={{color:BK.muted}}>{n0 + i}</i> <span style={{display:'inline-block',width:58,borderBottom:'1px solid ' + BK.ink}}>&nbsp;</span></span>);
  const B = (x) => <b style={{color:BK.muted,fontSize:10.5,letterSpacing:'0.06em'}}>{x}</b>;
  return <div className="ckp-key-ans" style={{fontSize:12,color:BK.ink,lineHeight:1.65}}>
    {g === 3
      ? <><div data-sec="A">{B('A')}  The keynote, then the 2nd, 3rd, 4th or 5th of its major scale, as in the room's step 2. Write which: {line(1)}</div>
        <div data-sec="B">{B('B')}  Four bars of oom-pah or oom-pah-pah, as in step 3. Write in two or in three: {line(5)}</div></>
      : <><div data-sec="A">{B('A')}  Two notes a major 3rd or a perfect 5th apart, together within an octave from middle C, then the higher or the lower alone. Write which you played alone: {line(1)}</div>
        <div data-sec="B">{B('B')}  A two-bar rhythm with a dotted crotchet, twice; then the same, or one beat changed. Write same or different: {line(5)}</div></>}
  </div>;
}
function CkpRoomHead({ id }) {""")
open(dst, 'w', encoding='utf-8').write(s)
print('ok', len(s))
