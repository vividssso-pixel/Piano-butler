#!/usr/bin/env python3
# Phase 486 (her 2026-10-18 23:04 '스케일은 스케일 파인더로 거의 티칭이 가능하더라고 심플하게' / 23:07 '하나에 다 흡수할 수 있는거면 더 좋아.
# 선법은 따로 놔둬 필요할때 꺼내써여하니까 스케일 기능에 두는게 맞아'): the Scale finder becomes the one scale tool.
# New in the Toolbox card only (a lesson step that drives the finder with ext/onKey stays exactly as it was):
#  - minor: natural, harmonic and melodic (fingers hidden where a thumb would land on a black key, as in MinorViewer)
#  - the step pattern (T/S) with the degree numbers 1 to 8 under the keys, and a switch for the degree names
#  - four small sections that open the parts that were separate cards: Build it, Fingering patterns, Stamps, Modes
# The tools it absorbs stay in the app as hidden cards (old links, lessons and saved stamps keep working).
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    if s.count(a) != n: raise SystemExit('found %d (want %d): %s' % (s.count(a), n, a[:100]))
    s = s.replace(a, b)

# 1. state: the minor form, the degree switch, the open section; hub = the Toolbox card (no lesson drives it)
rep("  const [oct, setOct] = useState(1);\n  const [q, setQ] = useState('');\n  const lastExt = useRef(ext);",
    "  const [oct, setOct] = useState(1);\n  const [q, setQ] = useState('');\n"
    "  const hub = !onKey && !ext; // the Toolbox card; a lesson step that passes ext/onKey keeps the old finder\n"
    "  const [form, setForm] = useState('harmonic'); // minor only: natural | harmonic | melodic\n"
    "  const [deg, setDeg] = useState('num'); // under the keys: num | name\n"
    "  const [sec, setSec] = useState(null); // build | patterns | stamps | modes\n"
    "  const lastExt = useRef(ext);")

# 2. the notes, offsets and fingering follow the minor form (the same rule MinorViewer uses)
rep("  const names = spellFor(key, mode), ks = scaleSig(key, mode);",
    "  const fm = mode === 'minor' ? form : 'major', names = mode === 'minor' ? spellMinor(key, form) : spellFor(key, mode), ks = scaleSig(key, mode);\n"
    "  const offs = mode === 'minor' && form !== 'harmonic' ? minorOffsets(form, oct) : e.offsets;\n"
    "  const clash = mode === 'minor' && form !== 'harmonic' && ['RH', 'LH'].some(h => e[h].some((f, i) => f === 1 && [1, 3, 6, 8, 10].includes((info.rootPc + offs[i]) % 12)));\n"
    "  const fing = (h) => clash ? e[h].map(() => null) : e[h];\n"
    "  const spell = (nm) => mode === 'minor' ? spellMinor(nm, form) : spellFor(nm, mode);\n"
    "  const hot = (i) => mode === 'minor' && (form === 'harmonic' ? i === 6 : form === 'melodic' ? i === 5 || i === 6 : false);\n"
    "  const FORM_NAME = { natural: t('natural minor', '자연 단음계'), harmonic: t('harmonic minor', '화성 단음계'), melodic: t('melodic minor', '가락 단음계') };")
# a theory-only key (A♯ major ...) is spelled for major and harmonic minor only
rep("const theory = !twinKs && ks.type && [1, 3, 6, 8, 10].includes(pc) && altName;",
    "const theory = !twinKs && ks.type && [1, 3, 6, 8, 10].includes(pc) && altName && (mode !== 'minor' || form === 'harmonic');")
rep("const ns = paper ? thy.names : spellFor(nm, mode); return (", "const ns = paper ? thy.names : spell(nm); return (")
rep("<span key={i} style={{color:mode === 'minor' && i === 6 ? '#e4572e' : 'var(--text)'}}>{paper ? fmtTheory(n) : prettyAny(n)}</span>)}",
    "<span key={i} style={{color:hot(i) ? '#e4572e' : 'var(--text)'}}>{paper ? fmtTheory(n) : prettyAny(n)}</span>)}")

# 3. heading and the line under it
rep("{twinKs ? prettyNote(myName) + ' / ' + prettyNote(nameOf(twinKs)) : prettyNote(key)} {mode === 'minor' ? t('harmonic minor', '화성 단음계') : t('major', '장조')}</div>",
    "{twinKs ? prettyNote(myName) + ' / ' + prettyNote(nameOf(twinKs)) : prettyNote(key)} {mode === 'minor' ? FORM_NAME[form] : t('major', '장조')}</div>")
rep("{mode === 'minor' && !twinKs ? t(' · raised 7th: ', ' · 올린 7음: ') + prettyAny(names[6]) : ''}",
    "{mode === 'minor' && !twinKs && form === 'harmonic' ? t(' · raised 7th: ', ' · 올린 7음: ') + prettyAny(names[6]) : ''}"
    "{mode === 'minor' && !twinKs && form === 'melodic' ? t(' · going up, raised 6th and 7th: ', ' · 올라갈 때 올린 6음과 7음: ') + prettyAny(names[5]) + ' ' + prettyAny(names[6]) : ''}")

# 4. controls: Minor (hub) and the three forms
rep("['minor', t('Harmonic minor', '화성 단음계')]].map(([m, l])",
    "['minor', hub ? t('Minor', '단조') : t('Harmonic minor', '화성 단음계')]].map(([m, l])")
rep("      <div style={{display:'flex',gap:4,flexWrap:'wrap',marginBottom:10}}>{keys.map(k =>",
    "      {hub && mode === 'minor' && <div style={{display:'flex',gap:4,flexWrap:'wrap',marginBottom:6}}>{['natural', 'harmonic', 'melodic'].map(f => <button key={f} className={'chip' + (form === f ? ' active' : '')} style={{padding:'3px 11px',fontSize:13}} onClick={() => setForm(f)}>{FORM_NAME[f]}</button>)}</div>}\n"
    "      <div style={{display:'flex',gap:4,flexWrap:'wrap',marginBottom:10}}>{keys.map(k =>")

# 5. the step pattern with the degree numbers (and a switch for their names), above the keyboards
rep("        <div style={{fontSize:12,fontWeight:900,color:'var(--muted)',letterSpacing:'0.05em',marginBottom:4}}>{t('RIGHT HAND', '오른손')}</div>\n"
    "        <ScaleKeyboard rootPc={info.rootPc} offsets={e.offsets} fingers={e.RH} hand=\"RH\"/>",
    "        {hub && <div style={{margin:'0 0 12px'}}>\n"
    "          <div style={{display:'flex',alignItems:'center',justifyContent:'space-between',gap:8,marginBottom:2}}>\n"
    "            <span style={{fontSize:12,fontWeight:900,color:'var(--muted)',letterSpacing:'0.05em'}}>{t('STEPS', '스텝')}</span>\n"
    "            <button className={'chip' + (deg === 'name' ? ' active' : '')} style={{padding:'2px 9px',fontSize:12}} onClick={() => setDeg(d => d === 'name' ? 'num' : 'name')}>{t('Degree names', '음 이름')}</button>\n"
    "          </div>\n"
    "          <div style={{display:'grid',gridTemplateColumns:narrow ? 'repeat(4,minmax(0,1fr))' : 'repeat(7,minmax(0,1fr)) auto',rowGap:6,alignItems:'center',fontWeight:900,fontSize:15}}>\n"
    "            {Array.from({ length: 8 }, (_, i) => <div key={i} style={{display:'flex',alignItems:'center',gap:5,minWidth:0}}>\n"
    "              <span style={{color:i === 0 || i === 7 ? 'var(--text)' : '#4a4d86',minWidth:10}}>{i + 1}</span>\n"
    "              {i < 7 && <span style={{fontSize:narrow ? 11 : 10,fontWeight:800,padding:'1px 4px',borderRadius:5,whiteSpace:'nowrap',background:STEP_PATTERNS[fm][i] === 'T' ? '#e9e2d0' : '#fbe3da',color:STEP_PATTERNS[fm][i] === 'T' ? '#6d6f9c' : '#e4572e',border:'1px solid ' + (STEP_PATTERNS[fm][i] === 'T' ? '#dbd2bd' : '#e4572e')}}>{STEP_PATTERNS[fm][i]}</span>}\n"
    "            </div>)}\n"
    "          </div>\n"
    "          <div style={{fontSize:12,fontWeight:700,color:'var(--muted)',marginTop:2}}>{t('T = tone, S = semitone', 'T = 온음, S = 반음')}{form === 'melodic' && mode === 'minor' ? t(' · going up', ' · 올라갈 때') : ''}</div>\n"
    "          {deg === 'name' && <div style={{display:'grid',gridTemplateColumns:'repeat(auto-fit,minmax(112px,1fr))',gap:'2px 8px',marginTop:6,fontSize:13}}>\n"
    "            {DEGREE_NAMES.map((nm, i) => <div key={i}><b style={{color:'#e4572e'}}>{i + 1}</b> {LANG === 'ko' ? DEGREE_NAMES_KO[i] : nm} <span style={{color:'var(--muted)'}}>{prettyAny(names[i])}</span></div>)}\n"
    "          </div>}\n"
    "        </div>}\n"
    "        <div style={{fontSize:12,fontWeight:900,color:'var(--muted)',letterSpacing:'0.05em',marginBottom:4}}>{t('RIGHT HAND', '오른손')}</div>\n"
    "        <ScaleKeyboard rootPc={info.rootPc} offsets={offs} fingers={fing('RH')} hand=\"RH\"/>")
rep("        <ScaleKeyboard rootPc={info.rootPc} offsets={e.offsets} fingers={e.LH} hand=\"LH\"/>",
    "        <ScaleKeyboard rootPc={info.rootPc} offsets={offs} fingers={fing('LH')} hand=\"LH\"/>")

# 6. the fingering note for a form, the hearing (melodic comes down as the natural minor), and the four sections
rep("        <div style={{textAlign:'center',marginTop:8}}><button className=\"ghost-btn\" onClick={() => playScaleNotes(info.rootPc, e.offsets)}>{t('♪ Hear it up and down', '♪ 올라갔다 내려오며 듣기')}</button></div>\n      </div>\n    </div>\n  );\n}",
    "        {clash && <p style={{fontSize:13,color:'var(--bad)',margin:'8px 0 0',textAlign:'center',lineHeight:1.5}}>{t('The fingers change for this form: the harmonic fingering would put a thumb on a black key. Practise it from your book.', '이 형태는 손가락 번호가 달라져요: 화성 단음계 손가락으로 치면 엄지가 검은건반에 닿아요. 책으로 익혀요.')}</p>}\n"
    "        <div style={{textAlign:'center',marginTop:8}}><button className=\"ghost-btn\" onClick={() => playScaleNotes(info.rootPc, offs, mode === 'minor' && form === 'melodic' ? minorOffsets('natural', oct) : null)}>{t('♪ Hear it up and down', '♪ 올라갔다 내려오며 듣기')}</button></div>\n"
    "      </div>\n"
    "      {hub && <div style={{display:'flex',gap:6,flexWrap:'wrap',marginTop:12}}>{[['build', t('Build it', '직접 만들기')], ['patterns', t('Fingering patterns', '손가락 번호 패턴')], ['stamps', t('Stamps', '도장')], ['modes', t('Modes', '선법')]].map(([id, l]) => <button key={id} className={'chip' + (sec === id ? ' active' : '')} style={{padding:'4px 12px',fontSize:13}} aria-pressed={sec === id} onClick={() => setSec(sec === id ? null : id)}>{l}</button>)}</div>}\n"
    "      {hub && sec === 'build' && <div style={{marginTop:10}}><ScaleBuilder key={mode} mode={mode}/></div>}\n"
    "      {hub && sec === 'patterns' && <div style={{marginTop:10}}><ScalePatterns sel={key} onPick={pick} mode={mode}/></div>}\n"
    "      {hub && sec === 'stamps' && <div style={{marginTop:10}}>{mode === 'minor' ? <ScalePath sel={key} onPick={pick} keys={MINOR_PATH} prefix=\"m:\" mode=\"minor\"/> : <ScalePath sel={key} onPick={pick}/>}</div>}\n"
    "      {hub && sec === 'modes' && <div style={{marginTop:10}}><Modes/></div>}\n"
    "    </div>\n  );\n}")

# 6b. the stamp grid takes a column count (the Toolbox card is narrow on a phone: two columns there)
rep("function ScalePath({ sel, onPick, keys = SCALE_PATH, prefix = '', mode = 'major' }) {",
    "function ScalePath({ sel, onPick, keys = SCALE_PATH, prefix = '', mode = 'major', cols = 3 }) {")
rep("      <div style={{display:'grid',gridTemplateColumns:'repeat(3,1fr)',gap:6}}>\n        {keys.map((k, ki) => PATH_STEPS.map((s, si) => {",
    "      <div style={{display:'grid',gridTemplateColumns:'repeat(' + cols + ',minmax(0,1fr))',gap:6}}>\n        {keys.map((k, ki) => PATH_STEPS.map((s, si) => {")
rep("<ScalePath sel={key} onPick={pick} keys={MINOR_PATH} prefix=\"m:\" mode=\"minor\"/> : <ScalePath sel={key} onPick={pick}/>}",
    "<ScalePath sel={key} onPick={pick} keys={MINOR_PATH} prefix=\"m:\" mode=\"minor\" cols={narrow ? 2 : 3}/> : <ScalePath sel={key} onPick={pick} cols={narrow ? 2 : 3}/>}")
rep("  const hub = !onKey && !ext; // the Toolbox card;",
    "  const narrow = typeof window !== 'undefined' && window.innerWidth < 480;\n  const hub = !onKey && !ext; // the Toolbox card;")

# 7. playing: an optional second set of offsets for the way down (the melodic minor comes down as the natural minor)
rep("function playScaleNotes(rootPc, offsets) {", "function playScaleNotes(rootPc, offsets, downOffsets) {")
rep("seq = [...offsets, ...offsets.slice(0, -1).reverse()];", "seq = [...offsets, ...(downOffsets || offsets).slice(0, -1).reverse()];")

# 8. the card: what it now does; the cards it absorbs stay as hidden cards (old links, lessons and stamps keep working)
rep("title: 'Scale finder', blurb: 'Type any scale: fingering for both hands, key signature (both spellings for black-key scales), notes.',",
    "title: 'Scale finder', blurb: 'Type or tap any scale, major or minor (natural, harmonic, melodic): the steps and degrees, key signature, notes, fingering for both hands. Build one, stamp it, modes.',")
rep("'scale-finder': ['스케일 찾기', '아무 스케일이나 입력: 양손 손가락 번호, 조표(검은건반 스케일은 두 가지 표기 모두), 음.'],",
    "'scale-finder': ['스케일 찾기', '아무 스케일이나 입력하거나 눌러요. 장조와 단조(자연·화성·가락): 스텝과 음 번호, 조표, 음, 양손 손가락 번호. 직접 만들기, 도장, 선법까지.'],")
rep("'scale-finder': ['scales', 0, 3, 'show home']", "'scale-finder': ['scales', 0, 3, 'show game write ear home']")
for tid in ['ssc-steps', 'ssc-fingers', 'ssc-degrees', 'ssc-g', 'ssc-f', 'major-shape', 'build-major', 'build-minor', 'degree-names',
            'major-fingering', 'minor-fingering', 'minor-forms', 'modes']:
    rep("  { id: '%s', ch: " % tid, "  { id: '%s', hidden: true, ch: " % tid)

# 9. the concept book's ladder and the exam kit point at the one tool
rep("['ssc-steps', 'ssc-g', 'ssc-f', 'skg-five']", "['scale-finder', 'skg-five']")
rep("['build-major', 'sharps-order', 'flats-order', 'relative-minor', 'build-minor']", "['scale-finder', 'sharps-order', 'flats-order', 'relative-minor']")
rep("['circle-fifths', 'place-it', 'minor-forms', 'csx-penta', 'scale-finder']", "['circle-fifths', 'place-it', 'csx-penta', 'scale-finder']")
rep("['all-keys', 'chromatic', 'modes']", "['all-keys', 'chromatic', 'scale-finder']")
rep("['has a theory exam coming', ['sharps-order', 'place-it', 'build-major',", "['has a theory exam coming', ['sharps-order', 'place-it', 'scale-finder',")

open(dst, 'w', encoding='utf-8').write(s)
print('patched', len(s))
