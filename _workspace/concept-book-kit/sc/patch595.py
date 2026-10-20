import sys
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:90],s.count(a)); s=s.replace(a,b)
HELP = r"""
// ─── Phase 588 (her call, 2026-10-20 14:53): the staff with its key signature. Lesson 11 shows D minor (one flat, B♭): the natural minor follows the key signature; the raised notes of the harmonic and melodic minors are accidentals beside the notes, not in the key signature.
const SC_D0 = { C: 28, G: 32, D: 29, A: 33, E: 30, B: 27, F: 31, Bb: 27, Eb: 30, Ab: 33, Db: 29, Gb: 32 };
function ScStaffScale({ k, ring, only, width = 330 }) {
  const d0 = SC_D0[k], items = Array.from({ length: 8 }, (_, j) => ['q', 1, d0 + j]).concat([['||']]), hl = skgOf(items, k, n => n.byKey);
  return <SkgStaff items={items} k={k} width={width} o={{ boxS: 26, D: 30, hl, ...skgUnder(items, k, only, hl), ring: ring == null ? [] : [ring] }}/>;
}
// D minor on the treble staff, d 29 to 36, with the key signature of F major (B♭). Up or down; signs only where the form raises a note.
function scMinItems(form, dir) {
  const up = [29, 30, 31, 32, 33, 34, 35, 36], idx = dir === 'up' ? up : up.slice().reverse();
  const sign = (j) => form === 'harmonic' && j === 6 ? '#' : form === 'melodic' && dir === 'up' && j === 5 ? 'n' : form === 'melodic' && dir === 'up' && j === 6 ? '#' : null;
  return idx.map((d, q) => { const j = dir === 'up' ? q : 7 - q, sg = sign(j); return sg ? ['q', 1, d, sg] : ['q', 1, d]; }).concat([['||']]);
}
"""
rep("\nconst scDirTag =", HELP + "\nconst scDirTag =")
# ---- ScMinor: D minor
a = s.index("const SC_MF = ['natural'"); b = s.index("// lesson 5: the natural.", a)
seg = s[a:b]
def r(x, y, n=1):
    global seg
    assert seg.count(x) == n, (x[:80], seg.count(x)); seg = seg.replace(x, y)
r("natural: ['Natural minor: the same notes as its relative major. A minor uses C major’s white keys, starting on A.', '자연 단음계: 나란한조인 장조와 음이 똑같아요. A 단조는 C 장조의 흰건반을 그대로 쓰고, A에서 시작해요.'],",
  "natural: ['Natural minor: follow the key signature. D minor has one flat, B♭, and no other sign is added.', '자연 단음계: 조표대로 쳐요. D 단조의 조표는 플랫 하나(B♭)이고, 따로 붙는 표는 없어요.'],")
r("harmonic: ['Harmonic minor, the one you’ll play most: raise the 7th note a semitone, going up and coming down. G becomes G♯.', '화성 단음계, 가장 많이 치게 될 단음계: 7번째 음을 반음 올려요, 올라갈 때도 내려올 때도. G가 G♯이 돼요.'],",
  "harmonic: ['Harmonic minor, the one you’ll play most: the 7th note is raised, C becomes C♯, going up and coming down. That sharp is not in the key signature: it is written beside the note.', '화성 단음계, 가장 많이 치게 될 단음계: 7번째 음을 올려요. C가 C♯이 돼요, 올라갈 때도 내려올 때도. 이 샤프는 조표에 있는 게 아니라 음표 옆에 따로 적어요.'],")
r("melodic: ['Melodic minor: going up, raise the 6th and 7th (F♯ and G♯). Coming down, play the natural minor.', '가락 단음계: 올라갈 때는 6음과 7음(F♯과 G♯)을 올려요. 내려올 때는 자연 단음계를 쳐요.'],",
  "melodic: ['Melodic minor: going up, the 6th and 7th are raised: B♭ becomes B♮ and C becomes C♯, written beside the notes. Coming down, back to the key signature: the natural minor.', '가락 단음계: 올라갈 때는 6음과 7음을 올려요. B♭이 B♮이 되고 C가 C♯이 돼요. 음표 옆에 따로 적어요. 내려올 때는 조표대로, 자연 단음계를 쳐요.'],")
r("K = stp.map(x => 9 + x).concat([21]), N = spellMinor('A', f).map(prettyAny).concat(['A'])", "K = stp.map(x => 2 + x).concat([14]), N = spellMinor('D', f).map(prettyAny).concat(['D'])")
r("t('All three start on A. They differ in only one or two notes near the top.', '셋 모두 A에서 시작해요. 위쪽 한두 음만 달라요.')", "t('All three start on D. They differ in only one or two notes near the top.', '셋 모두 D에서 시작해요. 위쪽 한두 음만 달라요.')")
r("t('That is A melodic minor: up with F♯ and G♯, down as the natural minor.', 'A 가락 단음계예요: 올라갈 때는 F♯과 G♯, 내려올 때는 자연 단음계예요.')", "t('That is D melodic minor: up with B♮ and C♯, down as the natural minor.', 'D 가락 단음계예요: 올라갈 때는 B♮과 C♯, 내려올 때는 자연 단음계예요.')")
r("t('That is A ' + fl.toLowerCase() + ' minor, up and down.', 'A ' + fl", "t('That is D ' + fl.toLowerCase() + ' minor, up and down.', 'D ' + fl")
r("spellMinor('A', 'melodic')", "spellMinor('D', 'melodic')", 2)
r("t('Start on A. Then tap ' + word(0) + '.', 'A에서 시작해요.", "t('Start on D. Then tap ' + word(0) + '.', 'D에서 시작해요.")
r("From A, tap ' + word(at) + '.', '이제 내려와요. 가락 단음계는 내려올 때 자연 단음계예요. A에서 '", "From D, tap ' + word(at) + '.', '이제 내려와요. 가락 단음계는 내려올 때 자연 단음계예요. D에서 '")
r("t('Now come back down. From A, tap ' + word(at) + '.', '이제 내려와요. A에서 '", "t('Now come back down. From D, tap ' + word(at) + '.', '이제 내려와요. D에서 '")
r("playKey(9, 0.5)", "playKey(2, 0.5)")
# 'one' view: the staff with its key signature
i0 = seg.index("  } else if (view === 'one') {"); i1 = seg.index("  } else {\n    const M = mk(fm)", i0)
ONE = r"""  } else if (view === 'one') {
    const f = SC_MF[i], M = mk(f), Dn = f === 'melodic' ? mk('natural') : M, Q = M.K.concat(Dn.K.slice(0, 7).reverse()), QS = Q.slice(1).map((k, j) => Math.abs(k - Q[j])), an = P.an;
    const upI = scMinItems(f, 'up'), dnI = scMinItems(f, 'down');
    const cUp = f === 'harmonic' ? [6] : f === 'melodic' ? [5, 6] : [], cDn = f === 'harmonic' ? [1] : [];
    const onlyUp = an >= 0 ? Array.from({ length: Math.min(an, 7) + 1 }, (_, j) => j) : null, onlyDn = an >= 0 ? (an >= 7 ? Array.from({ length: an - 6 }, (_, j) => j) : []) : null;
    const stf = (items, coral, only, ring, key) => <SkgStaff key={key} items={items} k="F" width={330} o={{ boxS: 26, D: 30, hl: coral, signHl: coral, ring: ring == null ? [] : [ring], ...skgUnder(items, 'F', only, coral) }}/>;
    body = <>
      <div style={scS.title}>{title}</div>
      <div style={scS.line}>{t(TXT[f][0], TXT[f][1])}</div>
      {scDirTag(false)}
      {stf(upI, cUp, onlyUp, an >= 0 && an <= 7 ? an : null, 'u' + f + an)}
      {scDirTag(true)}
      {stf(dnI, cDn, onlyDn, an >= 7 ? an - 7 : null, 'd' + f + an)}
      {an >= 0 ? <ScPillRow st={QS} upTo={an} cur={an - 1}/> : <ScPillRow st={M.ST} upTo={7}/>}
      {scPlayBtn(P, Q)}
      {scRow(<>
        <button className="ghost-btn" style={scS.back} onClick={() => { clear(); if (i === 0) setView('all'); else { setI(i - 1); setNonce(n => n + 1); } }}>{t('← Back', '← 이전')}</button>
        <button className="ghost-btn" style={scS.prim} onClick={() => { clear(); if (i === 2) { setView('try'); setAt(0); setBad(null); setNonce(n => n + 1); } else { setI(i + 1); setNonce(n => n + 1); } }}>{i === 2 ? t('Your turn →', '내가 해보기 →') : t('Next →', '다음 →')}</button>
      </>)}
    </>;
"""
seg = seg[:i0] + ONE + seg[i1:]
s = s[:a] + seg + s[b:]
# ---- ScAll: the staff under the keyboard
rep("      {A ? <ScPillRow st={QS} upTo={P.an} cur={P.an - 1}/> : <ScPills/>}\n      {scPlayBtn(P, Q)}\n      {scRow(<>\n        <button className=\"ghost-btn\" style={scS.back} onClick={() => { clear(); if (i === 0) setView('all'); else { const p = SC_ALLSTEPS",
    "      {A ? <ScPillRow st={QS} upTo={P.an} cur={P.an - 1}/> : <ScPills/>}\n      <ScStaffScale k={kk} ring={A ? (P.an <= 7 ? P.an : 14 - P.an) : null}/>\n      {scPlayBtn(P, Q)}\n      {scRow(<>\n        <button className=\"ghost-btn\" style={scS.back} onClick={() => { clear(); if (i === 0) setView('all'); else { const p = SC_ALLSTEPS")
# ---- ScSame: the staff on the two screens that finish a scale (G, F)
a = s.index("function ScSame() {"); b = s.index("function ScDeg()", a)
seg = s[a:b]
x = "      <ScPills upTo={E.arc != null ? E.arc + 1 : Math.max(E.n - 1, 0)} cur={E.arc != null ? E.arc : -1}/>\n"
assert seg.count(x) == 1
seg = seg.replace(x, x + "      {E.n === 8 && <ScStaffScale k={E.key}/>}\n")
s = s[:a] + seg + s[b:]
open(sys.argv[2],'w',encoding='utf-8').write(s)
