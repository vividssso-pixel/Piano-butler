#!/usr/bin/env python3
"""Build DC (on t777 -> t778): the Grade 1 checkpoint on paper, as Prelim's (DA) and Beginner's (CX).
`?book=check&floor=2` and `?book=checkkey&floor=2`: two parts of each Grade 1 room's check-up on paper, new items on the
checkpoint route only (answers computed from the data); Ear Training, Grade 1 has no Workbook, so two listening parts the
teacher plays (home or not home; in two or in three). Parts: listen-write A B (new), accidentals A E, key signatures A B,
terms A C, six-eight A C, intervals B C, chords B C, form A B.
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
# accidentals: F sharp, B flat, D natural; F sharp E F G | F A flat G A: the sign changes the 3rd note (F sharp) and the
# 8th (A flat), not the F after the bar line
after_obj('SAC_CHK', "if (CKP) Object.assign(SAC_CHK, { signs: [[31, '#'], [34, 'b'], [36, 'n']], circ: sacT([[31, '#'], 30, 31, 32, '|', 31, [33, 'b'], 32, 33, '||']) });   // Build DC")
# key signatures: D, F and G major to name; G's and B flat's signs to write
after_obj('SKG_CHK', "if (CKP) Object.assign(SKG_CHK, { name: [['D', 'treble'], ['F', 'bass'], ['G', 'treble']], which: [['G', 'treble'], ['Bb', 'bass']] });   // Build DC")
after_obj('TMX_CHK', "if (CKP) Object.assign(TMX_CHK, { mean: ['Lento', 'accel.', 'decresc.', 'cantabile'], pick: [['faster', 'Andante', 'Presto'], ['louder', 'mp', 'f']] });   // Build DC")
R("""  chk: { len: ['qd', 'e', 'hd', 'q'], count: [['m1', 3], ['ls2', 3], ['m2', 5], ['dot', 1]], see: ['big', 't34', 't34', 'big'], fill: [5, 2, 1, 4] },""",
  """  chk: CKP ? { len: ['hd', 'q', 'e', 'qd'], count: [['m1', 3], ['ls2', 3], ['m2', 5], ['dot', 1]], see: ['t34', 'big', 'big', 't34'], fill: [5, 2, 1, 4] }   // Build DC: the checkpoint's own order
    : { len: ['qd', 'e', 'hd', 'q'], count: [['m1', 3], ['ls2', 3], ['m2', 5], ['dot', 1]], see: ['big', 't34', 't34', 'big'], fill: [5, 2, 1, 4] },""")
# intervals: a 5th above D (A), a 4th above C (F), a 3rd above F (A); E-B melodic, D-G harmonic
after_obj('IVX_CHK', "if (CKP) Object.assign(IVX_CHK, { above: [[29, 'treble', 5], [21, 'bass', 4], [31, 'treble', 3]], mh: [['treble', ivxP(30, 34)], ['treble', ivxP(29, 32, 1)]] });   // Build DC")
after_obj('CHX_CHK', "if (CKP) Object.assign(CHX_CHK, { draw: [['D', 'treble'], ['G', 'bass'], ['F', 'treble']], mm: [['G', 'major'], ['A', 'minor']] });   // Build DC")
after_obj('FMX_CHK', "if (CKP) Object.assign(FMX_CHK, { sd: [['D', 'A'], ['E', 'E']], bt: [['A', 'B'], ['A', 'B', 'A'], ['A', 'A', 'B', 'B']] });   // Build DC")

# 2. the Grade 1 rooms in the checkpoint
R("""  signs: { secs: ['A', 'B'], back: { A: ['1 and 3', '2 and 4'], B: ['1, 3 and 4', '2, 4 and 5'] }, Paper: () => <SgnPaperCheck/> },
};""", """  signs: { secs: ['A', 'B'], back: { A: ['1 and 3', '2 and 4'], B: ['1, 3 and 4', '2, 4 and 5'] }, Paper: () => <SgnPaperCheck/> },
  // Build DC: Grade 1
  'listen-write': { secs: ['A', 'B'], back: { A: [1, 2], B: [2, 3] }, Paper: () => <LwCkpPaper/>, key: () => <LwCkpKey/> },
  accidentals: { secs: ['A', 'E'], back: { A: ['1 and 2', '2 and 3'], E: ['3 and 4', '4 and 5'] }, Paper: () => <SacPaperCheck/> },
  'key-signatures': { secs: ['A', 'B'], back: { A: ['2, 3 and 5', '3, 4 and 6'], B: ['1, 3 and 5', '2, 4 and 6'] }, Paper: () => <SkgPaperCheck/> },
  terms: { secs: ['A', 'C'], back: { A: ['1 to 4', '2 to 5'], C: ['1 and 3', '2 and 4'] }, Paper: () => <TmxPaperCheck/> },
  'six-eight': { secs: ['A', 'C'], back: { A: [2, 3], C: [4, 5] }, Paper: () => <E8PaperCheck/> },
  intervals: { secs: ['B', 'C'], back: { B: ['2 and 3', '3 and 4'], C: [4, 5] }, Paper: () => <IvxPaperCheck/> },
  chords: { secs: ['B', 'C'], back: { B: [1, 2], C: [2, 3] }, Paper: () => <ChxPaperCheck/> },
  form: { secs: ['A', 'B'], back: { A: [2, 3], B: ['3 and 4', '4 and 5'] }, Paper: () => <FmxPaperCheck/> },
};""")
R("""const CKP_PAGES = { '1': [""", """const CKP_PAGES = { '2': [['listen-write', 'accidentals'], ['key-signatures', 'terms'], ['six-eight', 'intervals'], ['chords', 'form']], '1': [""")
R("""function CkpRoomHead({ id }) {""", """// Ear Training, Grade 1: two listening parts, the teacher plays (Build DC)
function LwCkpPaper() {
  const pick = (a, b) => <div style={{display:'flex',flexDirection:'column',alignItems:'center',gap:9,padding:'16px 4px 6px',fontSize:13.5,fontWeight:800,color:BK.ink}}><span>{a}</span><span>{b}</span></div>;
  return <div className="lb-paper" style={{display:'flex',flexDirection:'column',gap:4}}>
    {bkSec('A', 'Your teacher plays a short tune and stops. Did it stop on the home note? Circle home or not home.')}
    <BkGrid cols={4} gap="6px 8px">{[1, 2, 3, 4].map(n => <BkCell key={n} n={n}>{pick('home', 'not home')}</BkCell>)}</BkGrid>
    {bkSec('B', 'Your teacher plays a short passage, twice. Circle in two or in three.')}
    <BkGrid cols={4} gap="6px 8px">{[5, 6, 7, 8].map(n => <BkCell key={n} n={n}>{pick('in two', 'in three')}</BkCell>)}</BkGrid>
  </div>;
}
function LwCkpKey() {
  const line = (n0) => [0, 1, 2, 3].map(i => <span key={i} style={{marginRight:12,whiteSpace:'nowrap'}}><i style={{color:BK.muted}}>{n0 + i}</i> <span style={{display:'inline-block',width:58,borderBottom:'1px solid ' + BK.ink}}>&nbsp;</span></span>);
  return <div className="ckp-key-ans" style={{fontSize:12,color:BK.ink,lineHeight:1.65}}>
    <div data-sec="A"><b style={{color:BK.muted,fontSize:10.5,letterSpacing:'0.06em'}}>A</b>  A short tune in C, G or F major; stop on its home note (the tonic) or before it. Write what you played: {line(1)}</div>
    <div data-sec="B"><b style={{color:BK.muted,fontSize:10.5,letterSpacing:'0.06em'}}>B</b>  Four bars in 2/4 or 3/4, with a clear first beat. Write in two or in three: {line(5)}</div>
  </div>;
}
function CkpRoomHead({ id }) {""")
# 'steps 1 to 5' as well as 'steps 1 and 3'
R("""  const pl = (w, v) => w + (/ and /.test(String(v)) ? 's ' : ' ') + v;   // Build DA""", """  const pl = (w, v) => w + (/ (and|to) /.test(String(v)) ? 's ' : ' ') + v;   // Build DA""")

open(dst, 'w', encoding='utf-8').write(s)
print('ok', len(s))
