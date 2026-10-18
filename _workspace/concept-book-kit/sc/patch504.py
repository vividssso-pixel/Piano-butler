#!/usr/bin/env python3
# Phase 504 (her 'yes', 2026-10-19 10:10): the Scale finder's black-key step shows both names of each black key on its chips
# (C♯/D♭, D♯/E♭, F♯/G♭, G♯/A♭, A♯/B♭); the keyboard keeps the scale's own spelling; a line says when the same keys are also a real key
# with another name (D♭ = C♯ major, F♯ = G♭ major; the other three have no real twin, so no line).
import sys
s = open(sys.argv[1], encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, 'found %d (want %d): %s' % (s.count(a), n, a[:90])
    s = s.replace(a, b)
rep("function SfStage({ keys, k, setK, hand, setHand, titleFor, grid, go }) {", "const SF_TWO = { Db: ['C#', 'Db'], Eb: ['D#', 'Eb'], 'F#': ['F#', 'Gb'], Ab: ['G#', 'Ab'], Bb: ['A#', 'Bb'] };\nconst SF_TWIN = { Db: ['the same keys as C♯ major (7 sharps)', 'C♯장조(샤프 일곱)와 건반이 같아요'], 'F#': ['the same keys as G♭ major (6 flats)', 'G♭장조(플랫 여섯)와 건반이 같아요'] };\nfunction SfStage({ keys, k, setK, hand, setHand, titleFor, grid, go, both }) {")
rep("style={{...KF_BTN,minWidth:0,padding:'0 2px',fontSize:15}} onClick={() => setK(x)}>{prettyNote(x)}</button>)}",
    "style={{...KF_BTN,minWidth:0,padding:'0 2px',fontSize:both ? (tiny ? 12.5 : 14) : 15}} onClick={() => setK(x)}>{both && SF_TWO[x] ? prettyNote(SF_TWO[x][0]) + '/' + prettyNote(SF_TWO[x][1]) : prettyNote(x)}</button>)}")
rep("    <div style={{display:'flex',gap:6,justifyContent:'center',flexWrap:'wrap',marginTop:12}}>\n      <button className=\"ghost-btn\" style={{...KF_BTN,minWidth:120}} onClick={play}>",
    "    {both && SF_TWIN[k] && <div style={{textAlign:'center',fontSize:13,fontWeight:700,color:'#5a5d8f',marginTop:8}}>{t(SF_TWIN[k][0], SF_TWIN[k][1])}</div>}\n    <div style={{display:'flex',gap:6,justifyContent:'center',flexWrap:'wrap',marginTop:12}}>\n      <button className=\"ghost-btn\" style={{...KF_BTN,minWidth:120}} onClick={play}>")
rep("<SfStage key=\"s2\" keys={['Db', 'Eb', 'F#', 'Ab', 'Bb']}", "<SfStage key=\"s2\" both keys={['Db', 'Eb', 'F#', 'Ab', 'Bb']}")
open(sys.argv[2], 'w', encoding='utf-8').write(s); print('ok')
