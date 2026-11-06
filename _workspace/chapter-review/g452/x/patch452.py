#!/usr/bin/env python3
# Phase 452 (her 2026-10-12 22:46 '토큰 늘려주거나 다른걸로 채우던지'): the token page of the staff mat set was half empty.
# Now it also has coral note tokens (the note you are finding), the five landmark tokens (bass C, the King's F, middle C,
# the Queen's G, treble C: Phase 449's names), time-signature tiles exactly one staff tall (38 mm = four 9.5 mm spaces) for
# the tune staff, and a TRY THIS with three set tasks for them.
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(a, b):
    global s
    if s.count(a) != 1: raise SystemExit('found %d: %s' % (s.count(a), a[:90]))
    s = s.replace(a, b)
rep("""const CutGroup = ({ title, note, children }) =>""",
"""const CutCoralNoteToken = () => <CutToken fill="#fdece6"><ellipse cx="5" cy="5" rx="3.1" ry="2.25" transform="rotate(-20 5 5)" fill={BK.coral}/></CutToken>;
// Phase 452: a landmark token: its letter in navy inside a coral ring (the letter tokens are coral on pink)
const CutLandmarkToken = ({ l }) => <CutToken fill="#fff"><circle cx="5" cy="5" r="3.7" fill="none" stroke={BK.coral} strokeWidth="0.65"/><text x="5" y="6.9" fontSize="5.4" fontWeight="900" fill={BK.ink} textAnchor="middle">{l}</text></CutToken>;
const CUT_LANDMARKS = [['C', 'bass C'], ['F', 'the King’s F'], ['C', 'middle C'], ['G', 'the Queen’s G'], ['C', 'treble C']];
// a time signature, exactly one staff tall (four spaces of CUT_GAP), to lay at the start of the tune staff
function CutTimeTile({ top }) {
  const h = 4 * CUT_GAP, w = 14;
  return <svg viewBox={'0 0 ' + w + ' ' + h} style={{width:w + 'mm',height:h + 'mm',display:'block',flex:'0 0 auto',outline:'0.4mm dashed ' + CUT.cut,outlineOffset:'-0.2mm'}}>
    <rect width={w} height={h} fill="#fffaf0"/>
    <text x={w / 2} y={h / 2 - 4.5} fontSize="14" fontWeight="900" fill={BK.ink} textAnchor="middle" style={{fontFamily:CK_SERIF}}>{top}</text>
    <text x={w / 2} y={h - 4.5} fontSize="14" fontWeight="900" fill={BK.ink} textAnchor="middle" style={{fontFamily:CK_SERIF}}>4</text>
  </svg>;
}
const CutGroup = ({ title, note, children }) =>""")
rep("""      <CutGroup title="Ledger-line strips" note="· for notes above or below the staff">{Array.from({ length: 12 }, (_, i) => <CutLedgerToken key={i}/>)}</CutGroup>
    </CutPage>""",
"""      <CutGroup title="Ledger-line strips" note="· for notes above or below the staff">{Array.from({ length: 12 }, (_, i) => <CutLedgerToken key={i}/>)}</CutGroup>
      <CutGroup title="Coral note tokens" note="· 12, for the note you are finding">{Array.from({ length: 12 }, (_, i) => <CutCoralNoteToken key={i}/>)}</CutGroup>
      <CutGroup title="Landmark tokens" note="· the five notes to read from, low to high">{CUT_LANDMARKS.map(([l, name]) => <div key={name} style={{display:'flex',flexDirection:'column',alignItems:'center',gap:'1mm',width:'22mm'}}><CutLandmarkToken l={l}/><span style={{fontSize:9,fontWeight:800,color:BK.muted,textAlign:'center',lineHeight:1.2}}>{name}</span></div>)}</CutGroup>
      <CutGroup title="Time signatures" note="· two of each, one staff tall: lay one just after the clef on the tune staff">{[2, 3, 4].flatMap(n => [0, 1].map(k => <CutTimeTile key={n + '-' + k} top={n}/>))}</CutGroup>
      <CutTry items={[
        <>Put the five <b>landmark tokens</b> on the grand staff: bass C, the King’s F, middle C, the Queen’s G and treble C. Play each one on the piano.</>,
        <>Pick a landmark. Put a <b>coral token</b> a step above it and another a skip below it. Name all three notes.</>,
        <>Lay a <b>3/4 tile</b> at the start of the tune staff. Put three note tokens in every bar, then play your tune, counting 1 2 3.</>,
      ]}/>
    </CutPage>""")
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
