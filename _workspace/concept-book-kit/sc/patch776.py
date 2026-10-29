#!/usr/bin/env python3
"""Build DA (on t775 -> t776): the Prelim checkpoint on paper, as the Beginner ones (Build CX).
`?book=check&floor=1` and `?book=checkkey&floor=1`: two parts of each Prelim room's check-up on paper, with new items on
the checkpoint route only; Ear Training, Prelim has no Workbook, so two listening parts the teacher plays (higher or lower,
with the bird and the turtle; same or different rhythm). The key takes each room's answers from its own Teacher copy.
Parts: listen-sing A B (new), tempo B F, rhythm C E, ledger lines B C, scales A C, scale playing A C, minor scales B D,
signs A B. The Books shelf shows it after the floor's last room (signs), as CX does for Beginner.
"""
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def R(old, new, n=1):
    global s
    c = s.count(old); assert c == n, (c, n, old[:120]); s = s.replace(old, new)
def after_obj(name, line):
    """put `line` right after the object literal `const NAME = {...};` (top level, closed by a line '};')"""
    global s
    i = s.index('\nconst ' + name + ' = {'); j = s.index('\n};', i) + 3
    s = s[:j] + '\n' + line + s[j:]

# 1. fresh items on the checkpoint route (answers are computed from the data, or given with it and checked by hand)
after_obj('STM_CHK', "if (CKP) Object.assign(STM_CHK, { mean: [['Moderato', ['at a medium speed', 'slow']], ['Adagio', ['fast and lively', 'slow']], ['Allegro', ['fast and lively', 'at a walking pace']], ['Andante', ['at a medium speed', 'at a walking pace']]], feel: ['rush2', 'steady2', 'drag'] });   // Build DA")
# beats: a minim 2, a quaver rest ½, a dotted crotchet 1½, two quavers 1; starts: a crotchet before a 4/4 bar starts on 4, two crotchets before a 3/4 bar on 2
after_obj('SRH_CHK', "if (CKP) Object.assign(SRH_CHK, { beats: [['h', '2'], ['er', '½'], ['qd', '1½'], ['p', '1']], start: [[4, ['q'], 3, ['h', 'q', 'q']], [3, ['q', 'q'], 1, ['hd']]] });   // Build DA")
# ledger lines: sky A5 D6 E6 B5; sea B1 E2 C2 F2
R("""  sky: [41, 44, 39, 42], sea: [15, 12, 17, 14],""", """  sky: CKP ? [40, 43, 44, 41] : [41, 44, 39, 42], sea: CKP ? [13, 16, 14, 17] : [15, 12, 17, 14],   // Build DA: the checkpoint's own""")

# scales: D E whole, E F half, B flat C whole, F sharp G half; C major degrees D 2, B 7, C 1, G 5 (the choices start at the third number)
after_obj('SSC_CHK', "if (CKP) Object.assign(SSC_CHK, { pairs: [['D E', 'whole'], ['E F', 'half'], ['B♭ C', 'whole'], ['F♯ G', 'half']], degs: [[29, 2, 1], [34, 7, 5], [28, 1, 1], [32, 5, 3]] });   // Build DA")
R("""    mirror: [['C', 1], ['C', 5], ['Amh', 2], ['Amh', 4]], fing: [['C', 'R', [3]], ['G', 'L', [5]], ['G', 'R', [6]], ['C', 'L', [2]]] },
};""", """    mirror: [['C', 1], ['C', 5], ['Amh', 2], ['Amh', 4]], fing: [['C', 'R', [3]], ['G', 'L', [5]], ['G', 'R', [6]], ['C', 'L', [2]]] },
};
if (CKP) Object.assign(SP_WB.chk, { turn: [['C', 'L', 'dn'], ['G', 'R', 'up'], ['C', 'R', 'dn'], ['G', 'L', 'up']], mirror: [['C', 3], ['C', 6], ['Amh', 1], ['Amh', 5]] });   // Build DA""")
R("""    gap: [['E', 1], ['D', 3], ['G', 5], ['A', 1]], kind: [['G', 'min'], ['F', 'maj'], ['A', 'min'], ['D', 'maj']] },
};""", """    gap: [['E', 1], ['D', 3], ['G', 5], ['A', 1]], kind: [['G', 'min'], ['F', 'maj'], ['A', 'min'], ['D', 'maj']] },
};
if (CKP) Object.assign(MS_WB.chk, { sig: ['G', 'Bb', 'C', 'F'], gap: [['A', 5], ['D', 0], ['E', 4], ['G', 6]] });   // Build DA""")
# signs: a start-repeat (1 2 3 2 3) and D.C. al Fine (1 2 3 1 2); Fine, D.C., an end-repeat and the segno alone
after_obj('SGN_CHK', "if (CKP) Object.assign(SGN_CHK, { ord: [[sgnB('q30 q32 h31'), sgnB('q29 q31 h30', { start: true }), sgnB('q31 q29 h28', { end: true })], [sgnB('q28 q30 h32'), sgnB('q31 q29 h30', { fine: true }), sgnB('q32 q31 h30', { dc: true })]], mean: [['fine', [SGN_W1(28, { fine: true })]], ['dc', [SGN_W1(30, { dc: true })]], ['end', [SGN_W1(31, { end: true })]], ['segno', [SGN_W1(29, { segno: true })]]] });   // Build DA")
# the signs Teacher copy writes its answers with skgTcAns: give it the part's letter too, so a key can pick its parts
R("""const skgTcAns = (label, list, n0 = 1) => <div style={{fontSize:12,""", """const skgTcAns = (label, list, n0 = 1) => <div data-sec={label} style={{fontSize:12,""")

# 2. the Prelim rooms in the checkpoint, and Ear Training, Prelim's two listening parts
R("""  tones: { secs: ['A', 'D'], back: { A: [1, 2], D: [4, 5] }, Paper: () => <TnPaperCheck/> },
};""", """  tones: { secs: ['A', 'D'], back: { A: [1, 2], D: [4, 5] }, Paper: () => <TnPaperCheck/> },
  // Build DA: Prelim
  'listen-sing': { secs: ['A', 'B'], back: { A: [3, 4], B: [2, 3] }, Paper: () => <LsCkpPaper/>, key: () => <LsCkpKey/> },
  tempo: { secs: ['B', 'F'], back: { B: [2, 3], F: [5, 6] }, Paper: () => <StmPaperCheck/> },
  rhythm: { secs: ['C', 'E'], back: { C: [2, 3], E: [4, 5] }, Paper: () => <SrhPaperCheck/> },
  'ledger-lines': { secs: ['B', 'C'], back: { B: [2, 3], C: [3, 4] }, Paper: () => <LlPaperCheck/> },
  scales: { secs: ['A', 'C'], back: { A: [1, 2], C: [3, 4] }, Paper: () => <SscPaperCheck/> },
  'scale-play': { secs: ['A', 'C'], back: { A: [1, 2], C: [4, 5] }, Paper: () => <SpPaperCheck/> },
  'minor-scales': { secs: ['B', 'D'], back: { B: [2, 3], D: [4, 5] }, Paper: () => <MsPaperCheck/> },
  signs: { secs: ['A', 'B'], back: { A: ['1 and 3', '2 and 4'], B: ['1, 3 and 4', '2, 4 and 5'] }, Paper: () => <SgnPaperCheck/> },
};""")
R("""const CKP_PAGES = { '0a': [""", """const CKP_PAGES = { '1': [['listen-sing', 'tempo', 'rhythm'], ['ledger-lines', 'scales'], ['scale-play', 'minor-scales'], ['signs']], '0a': [""")
R("""function CkpRoomHead({ id }) {""", """// Ear Training, Prelim has no Workbook either: two listening parts, the teacher plays (Build DA)
function LsCkpPaper() {
  const opt = (k, ic, w) => <div key={k} style={{display:'flex',flexDirection:'column',alignItems:'center',gap:3}}>{ic}<span style={{fontSize:11.5,fontWeight:800,color:BK.ink}}>{w}</span></div>;
  return <div className="lb-paper" style={{display:'flex',flexDirection:'column',gap:4}}>
    {bkSec('A', 'Your teacher plays two notes. Is the second one higher or lower? Circle the bird (higher) or the turtle (lower).')}
    <BkGrid cols={4} gap="6px 8px">{[1, 2, 3, 4].map(n => <BkCell key={n} n={n}><div style={{display:'flex',justifyContent:'center',alignItems:'flex-end',gap:20,padding:'14px 4px 4px'}}>{[opt('b', birdIcon(34), 'higher'), opt('t', turtleIcon(34), 'lower')]}</div></BkCell>)}</BkGrid>
    {bkSec('B', 'Your teacher claps two short rhythms. Circle same or different.')}
    <BkGrid cols={4} gap="6px 8px">{[5, 6, 7, 8].map(n => <BkCell key={n} n={n}><div style={{display:'flex',flexDirection:'column',alignItems:'center',gap:9,padding:'16px 4px 6px',fontSize:13.5,fontWeight:800,color:BK.ink}}><span>same</span><span>different</span></div></BkCell>)}</BkGrid>
  </div>;
}
function LsCkpKey() {
  const line = (n0) => [0, 1, 2, 3].map(i => <span key={i} style={{marginRight:12,whiteSpace:'nowrap'}}><i style={{color:BK.muted}}>{n0 + i}</i> <span style={{display:'inline-block',width:58,borderBottom:'1px solid ' + BK.ink}}>&nbsp;</span></span>);
  return <div className="ckp-key-ans" style={{fontSize:12,color:BK.ink,lineHeight:1.65}}>
    <div data-sec="A"><b style={{color:BK.muted,fontSize:10.5,letterSpacing:'0.06em'}}>A</b>  Two notes a third or more apart, as in the room's step 3; mix higher and lower. Write what you played: {line(1)}</div>
    <div data-sec="B"><b style={{color:BK.muted,fontSize:10.5,letterSpacing:'0.06em'}}>B</b>  Two short rhythms of one bar each; for different, change one beat. Write same or different: {line(5)}</div>
  </div>;
}
function CkpRoomHead({ id }) {""")

# a longer checkpoint gets a little more time; 'steps 1 and 3 (Lesson Book pages 2 and 4)' when a part has two
R("""two parts from each. No piano, no help, about 15 minutes.</div></div>""", """two parts from each. No piano, no help, about {ids.length > 7 ? 20 : 15} minutes.</div></div>""")
R("""  const back = Object.entries(R.back).map(([L, [st, pg]]) => L + ' → step ' + st + ' (Lesson Book page ' + pg + ')').join(' · ');""",
  """  const pl = (w, v) => w + (/ and /.test(String(v)) ? 's ' : ' ') + v;   // Build DA
  const back = Object.entries(R.back).map(([L, [st, pg]]) => L + ' → ' + pl('step', st) + ' (Lesson Book ' + pl('page', pg) + ')').join(' · ');""")

open(dst, 'w', encoding='utf-8').write(s)
print('ok', len(s))
