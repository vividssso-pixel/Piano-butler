#!/usr/bin/env python3
# Phase 487, second stage: the reviewer's must-fix and should-fix points on the unified Scale finder.
# Runs on the output of patch486.py.  python3 patch486b.py in.src.html out.src.html
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    if s.count(a) != n: raise SystemExit('found %d (want %d): %s' % (s.count(a), n, a[:100]))
    s = s.replace(a, b)

# F3: where the minor form's fingers would put a thumb on a black key the keyboard still lights the scale's notes
# (plain: no number, no group colour); the legend hides and the note is quiet, not an error red.
rep("  const fing = (h) => clash ? e[h].map(() => null) : e[h];", "  const fing = (h) => e[h];")
rep("fingers={fing('RH')} hand=\"RH\"/>", "fingers={fing('RH')} hand=\"RH\" plain={clash}/>")
rep("fingers={fing('LH')} hand=\"LH\"/>", "fingers={fing('LH')} hand=\"LH\" plain={clash}/>")
rep("{clash && <p style={{fontSize:13,color:'var(--bad)',margin:'8px 0 0',textAlign:'center',lineHeight:1.5}}>{t('The fingers change for this form: the harmonic fingering would put a thumb on a black key. Practise it from your book.', '이 형태는 손가락 번호가 달라져요: 화성 단음계 손가락으로 치면 엄지가 검은건반에 닿아요. 책으로 익혀요.')}</p>}",
    "{clash && <p style={{fontSize:13,color:'var(--muted)',margin:'8px 0 0',textAlign:'center',lineHeight:1.5}}>{t('No finger numbers for this form: the harmonic fingering would put a thumb on a black key. The lit keys are the notes of the scale; look the fingering up in your book.', '이 형태는 손가락 번호를 보여 주지 않아요: 화성 단음계 손가락으로 치면 엄지가 검은건반에 닿아요. 불 켜진 건반이 이 스케일의 음이에요. 손가락 번호는 책에서 확인해요.')}</p>}")
rep("<div style={{display:'flex',gap:10,flexWrap:'wrap',alignItems:'center',justifyContent:'center',marginTop:8,fontSize:12,fontWeight:700,color:'#4a4d86'}}>",
    "<div style={{display:clash ? 'none' : 'flex',gap:10,flexWrap:'wrap',alignItems:'center',justifyContent:'center',marginTop:8,fontSize:12,fontWeight:700,color:'#4a4d86'}}>")
rep("function ScaleKeyboard({ rootPc, offsets, fingers, hand }) {", "function ScaleKeyboard({ rootPc, offsets, fingers, hand, plain }) {")
rep("  offsets.forEach((off, idx) => { fingerAt[off] = fingers[idx]; });",
    "  const lit = {};\n  offsets.forEach((off, idx) => { fingerAt[off] = plain ? null : fingers[idx]; lit[off] = true; });")
rep("            fill={seg ? seg.fill : '#fff'}\n            stroke={seg ? seg.stroke : 'var(--muted)'}",
    "            fill={seg ? seg.fill : (plain && lit[k.i] ? '#dfe2f6' : '#fff')}\n            stroke={seg ? seg.stroke : (plain && lit[k.i] ? '#4a4d86' : 'var(--muted)')}")
rep("fill=\"#1d1c22\" stroke={seg ? seg.stroke : 'none'} strokeWidth={seg ? 3 : 0}/>",
    "fill=\"#1d1c22\" stroke={seg ? seg.stroke : (plain && lit[k.i] ? '#8c90d9' : 'none')} strokeWidth={seg || (plain && lit[k.i]) ? 3 : 0}/>")

# F4 and F5: Korean labels match the app (음계 이름 is the old degree-names tool; 걸음 is how the app says steps)
rep("{t('Degree names', '음 이름')}", "{t('Degree names', '음계 이름')}")
rep("{t('STEPS', '스텝')}", "{t('STEPS', '걸음')}")

# F1: the 7th of the natural minor is a whole tone below the tonic: the subtonic, not a leading note
rep("{LANG === 'ko' ? DEGREE_NAMES_KO[i] : nm} <span",
    "{mode === 'minor' && form === 'natural' && i === 6 ? t('subtonic', '서브토닉') : (LANG === 'ko' ? DEGREE_NAMES_KO[i] : nm)} <span")

# F2: say how the melodic minor comes down
rep("{form === 'melodic' && mode === 'minor' ? t(' · going up', ' · 올라갈 때') : ''}</div>",
    "{form === 'melodic' && mode === 'minor' ? t(' · going up', ' · 올라갈 때') : ''}</div>\n"
    "          {form === 'melodic' && mode === 'minor' && (() => { const nn = spellMinor(key, 'natural'); return <div style={{fontSize:13,fontWeight:700,marginTop:4}}>{t('Coming down it is the natural minor: ', '내려올 때는 자연 단음계예요: ')}{[nn[0], nn[6], nn[5], nn[4], nn[3], nn[2], nn[1], nn[0]].map(n => prettyAny(n)).join(' ')}</div>; })()}")

# F6: the top row wraps instead of clipping the last chip
rep("      <div style={{display:'flex',gap:4,marginBottom:6}}>{[['major', t('Major', '장조')],",
    "      <div style={{display:'flex',gap:4,marginBottom:6,flexWrap:'wrap'}}>{[['major', t('Major', '장조')],")

# F7: bigger tap targets on the new controls; F12: the form chips say which is pressed
rep("<button className={'chip' + (deg === 'name' ? ' active' : '')} style={{padding:'2px 9px',fontSize:12}}",
    "<button className={'chip' + (deg === 'name' ? ' active' : '')} aria-pressed={deg === 'name'} style={{padding:'9px 14px',fontSize:13,minHeight:40}}")
rep("style={{padding:'4px 12px',fontSize:13}} aria-pressed={sec === id}", "style={{padding:'9px 16px',fontSize:14,minHeight:40}} aria-pressed={sec === id}")
rep("<button key={f} className={'chip' + (form === f ? ' active' : '')} style={{padding:'3px 11px',fontSize:13}} onClick={() => setForm(f)}>",
    "<button key={f} className={'chip' + (form === f ? ' active' : '')} aria-pressed={form === f} style={{padding:'8px 13px',fontSize:14,minHeight:38}} onClick={() => setForm(f)}>")

# F8: each step sits on a line between its two numbers, so "6 [T+S] 7" reads as the step from 6 to 7
rep("""            {Array.from({ length: 8 }, (_, i) => <div key={i} style={{display:'flex',alignItems:'center',gap:5,minWidth:0}}>
              <span style={{color:i === 0 || i === 7 ? 'var(--text)' : '#4a4d86',minWidth:10}}>{i + 1}</span>
              {i < 7 && <span style={{fontSize:narrow ? 11 : 10,fontWeight:800,padding:'1px 4px',borderRadius:5,whiteSpace:'nowrap',""",
    """            {Array.from({ length: 8 }, (_, i) => <div key={i} style={{display:'flex',alignItems:'center',gap:3,minWidth:0}}>
              <span style={{color:i === 0 || i === 7 ? 'var(--text)' : '#4a4d86',minWidth:10}}>{i + 1}</span>
              {i < 7 && <span style={{flex:1,display:'flex',alignItems:'center',gap:2,minWidth:0}}><span style={{flex:1,height:1,background:'#c9c0aa'}}/><span style={{fontSize:narrow ? 11 : 10,fontWeight:800,padding:'1px 4px',borderRadius:5,whiteSpace:'nowrap',""")
rep("border:'1px solid ' + (STEP_PATTERNS[fm][i] === 'T' ? '#dbd2bd' : '#e4572e')}}>{STEP_PATTERNS[fm][i]}</span>}\n            </div>)}",
    "border:'1px solid ' + (STEP_PATTERNS[fm][i] === 'T' ? '#dbd2bd' : '#e4572e')}}>{STEP_PATTERNS[fm][i]}</span><span style={{flex:1,height:1,background:'#c9c0aa'}}/></span>}\n            </div>)}")

open(dst, 'w', encoding='utf-8').write(s)
print('patched b', len(s))
