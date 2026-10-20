import sys
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:90],s.count(a)); s=s.replace(a,b)
def cut(startmark, endmark, new, after=0):
    global s
    a = s.index(startmark, after); b = s.index(endmark, a)
    s = s[:a] + new + s[b:]
    return a
# shared word helper
HELP = r"""
// ─── Phase 585 (her ask, 2026-10-20 13:32): the way back down is checked too. The path is up the scale, then down the same keys (melodic minor comes down as natural minor).
const scStepWord = (sz, dn) => dn ? (sz === 1 ? t('a half step down (S)', '반음 아래로 (S)') : sz === 2 ? t('a whole step down (T)', '온음 아래로 (T)') : t('a tone and a semitone down (T+S)', '온음에 반음을 더해 아래로 (T+S)'))
  : (sz === 1 ? t('a half step up (S)', '반음 위로 (S)') : sz === 2 ? t('a whole step up (T)', '온음 위로 (T)') : t('a tone and a semitone up (T+S)', '온음에 반음을 더해 위로 (T+S)'));
"""
rep("\n// lesson 5: the natural.", HELP + "\n// lesson 5: the natural.")
MAJ = r"""    const K = scIdx(KK), N = scNames(KK), Q = K.concat(K.slice(0, 7).reverse()), N2 = N.concat(N.slice(0, 7).reverse()), QS = Q.slice(1).map((k, j) => Math.abs(k - Q[j])), done = at >= 14, marks = {}, names = {}, arcs = [];
    for (let j = 0; j <= at; j++) { marks[Q[j]] = j === at && !done ? 'pick' : 'pass'; names[Q[j]] = N2[j]; }
    for (let j = 0; j < at; j++) arcs.push([Q[j], Q[j + 1], j === at - 1, SC_COL[QS[j]]]);
    if (bad != null) marks[bad] = 'bad';
    const dn = at >= 7, word = (j) => scStepWord(QS[j], j >= 7);
    const line = done ? t('That is ' + N[0] + ' major, up and down: the same pattern.', N[0] + ' 장음계를 올라가고 내려왔어요. 같은 패턴이에요.')
      : bad != null ? t('Not that key. From ' + N2[at] + ', go ' + word(at) + '.', '그 건반이 아니에요. ' + N2[at] + '에서 ' + word(at) + ' 가요.')
      : at === 0 ? t('Start on ' + N[0] + '. Then tap ' + word(0) + '.', N[0] + '에서 시작해요. 그다음 ' + word(0) + ' 건반을 눌러요.')
      : at === 7 ? t('Now come back down. From ' + N2[at] + ', tap ' + word(at) + '.', '이제 내려와요. ' + N2[at] + '에서 ' + word(at) + ' 건반을 눌러요.')
      : t('From ' + N2[at] + ', tap ' + word(at) + '.', N2[at] + '에서 ' + word(at) + ' 건반을 눌러요.');
    const tap = (k) => { if (done) return; clear(); if (k === Q[at + 1]) { setBad(null); setAt(at + 1); setNonce(n => n + 1); playKey(Q[at], 0.35); timers.current.push(setTimeout(() => playKey(k, 0.6), 400)); }
      else { setBad(k); playKey(k, 0.4); timers.current.push(setTimeout(() => setBad(null), 1100)); } };
"""
for KK, mark in (('kk', "    const K = scIdx(kk), N = scNames(kk), done = at >= 7, marks = {}, names = {}, arcs = [];"), ('tk', "    const K = scIdx(tk), N = scNames(tk), done = at >= 7, marks = {}, names = {}, arcs = [];")):
    a = cut(mark, "    body = <>", MAJ.replace('scIdx(KK)', 'scIdx(' + KK + ')').replace('scNames(KK)', 'scNames(' + KK + ')'))
    # the pills line right after this point
    b = s.index("<ScPills upTo={at} cur={at - 1}/>", a)
    s = s[:b] + "<ScPillRow st={QS} upTo={at} cur={at - 1}/>" + s[b + len("<ScPills upTo={at} cur={at - 1}/>"):]
# marks passed to ScKeys use K[0]; fine (K defined). Minor.
MIN = r"""    const M = mk(fm), K = M.K, D = fm === 'melodic' ? mk('natural') : M, Q = K.concat(D.K.slice(0, 7).reverse()), N2 = M.N.concat(D.N.slice(0, 7).reverse()), QS = Q.slice(1).map((k, j) => Math.abs(k - Q[j])), done = at >= 14, marks = {}, names = {}, arcs = [];
    for (let j = 0; j <= at; j++) { marks[Q[j]] = j === at && !done ? 'pick' : (j < 8 && M.marks[Q[j]] === 'target') ? 'target' : 'pass'; names[Q[j]] = N2[j]; }
    for (let j = 0; j < at; j++) arcs.push([Q[j], Q[j + 1], j === at - 1, scColOf(QS[j])]);
    if (bad != null) marks[bad] = 'bad';
    const word = (j) => scStepWord(QS[j], j >= 7);
    const fl = MINOR_FORMS[fm].label;
    const raised = fm === 'melodic' && at >= 7 && bad != null && (bad === K[5] || bad === K[6]);
    const line = done ? (fm === 'melodic' ? t('That is A melodic minor: up with F♯ and G♯, down as the natural minor.', 'A 가락 단음계예요: 올라갈 때는 F♯과 G♯, 내려올 때는 자연 단음계예요.') : t('That is A ' + fl.toLowerCase() + ' minor, up and down.', 'A ' + fl + ' 단음계를 올라가고 내려왔어요.'))
      : raised ? t('Not that key. Coming down, the melodic minor plays the natural minor: ' + N2[at + 1] + ', not ' + prettyAny(spellMinor('A', 'melodic')[bad === K[5] ? 5 : 6]) + '.', '그 건반이 아니에요. 내려올 때 가락 단음계는 자연 단음계를 쳐요: ' + prettyAny(spellMinor('A', 'melodic')[bad === K[5] ? 5 : 6]) + ' 말고 ' + N2[at + 1] + '이에요.')
      : bad != null ? t('Not that key. From ' + N2[at] + ', go ' + word(at) + '.', '그 건반이 아니에요. ' + N2[at] + '에서 ' + word(at) + ' 가요.')
      : at === 0 ? t('Start on A. Then tap ' + word(0) + '.', 'A에서 시작해요. 그다음 ' + word(0) + ' 건반을 눌러요.')
      : at === 7 ? (fm === 'melodic' ? t('Now come back down. Melodic minor comes down as the natural minor. From A, tap ' + word(at) + '.', '이제 내려와요. 가락 단음계는 내려올 때 자연 단음계예요. A에서 ' + word(at) + ' 건반을 눌러요.') : t('Now come back down. From A, tap ' + word(at) + '.', '이제 내려와요. A에서 ' + word(at) + ' 건반을 눌러요.'))
      : t('From ' + N2[at] + ', tap ' + word(at) + '.', N2[at] + '에서 ' + word(at) + ' 건반을 눌러요.');
    const tap = (k) => { if (done) return; clear(); if (k === Q[at + 1]) { setBad(null); setAt(at + 1); setNonce(n => n + 1); playKey(Q[at], 0.35); timers.current.push(setTimeout(() => playKey(k, 0.6), 400)); }
      else { setBad(k); playKey(k, 0.4); timers.current.push(setTimeout(() => setBad(null), 1100)); } };
"""
a = cut("    const M = mk(fm), K = M.K, ST = M.ST, done = at >= 7, marks = {}, names = {}, arcs = [];", "    body = <>", MIN)
rep("<ScPillRow st={ST} upTo={at} cur={at - 1}/>", "<ScPillRow st={QS} upTo={at} cur={at - 1}/>")
# chromatic: up then down, fingers
rep("const K = K0, done = at >= 13, marks = {}, names = {};\n    K.forEach((k, j) => { if (j < at) { marks[k] = 'good'; names[k] = String(chromFinger(k % 12, hand, j === 0)); } else marks[k] = 'pass'; });\n    if (!done) marks[K[at]] = bad != null ? 'bad' : 'pick';\n    const k0 = done ? 0 : K[at], pc = k0 % 12, isBlack = [1, 3, 6, 8, 10].includes(pc), right = chromFinger(pc, hand, at === 0);",
    "const K = K0, Q = K0.concat(K0.slice(0, 12).reverse()), L = Q.length, done = at >= L, marks = {}, names = {};\n    K.forEach(k => { marks[k] = 'pass'; });\n    for (let j = 0; j < at; j++) { marks[Q[j]] = 'good'; names[Q[j]] = String(chromFinger(Q[j] % 12, hand, j === 0 || j === L - 1)); }\n    if (!done) marks[Q[at]] = bad != null ? 'bad' : 'pick';\n    const lowest = at === 0 || at === L - 1, k0 = done ? 0 : Q[at], pc = k0 % 12, isBlack = [1, 3, 6, 8, 10].includes(pc), right = chromFinger(pc, hand, lowest);")
rep("const guide = at === 0 ? t('The lowest note","const guide = lowest ? t('The lowest note")
rep("t('All thirteen notes. That is the chromatic fingering, ' + handW + '.', '열세 음을 다 했어요. ' + handKo(hand) + ' 반음계 운지예요.')",
    "t('All ' + L + ' notes, up and down. That is the chromatic fingering, ' + handW + '.', L + '개 음을 올라가고 내려왔어요. ' + handKo(hand) + ' 반음계 운지예요.')")
rep("t('Which finger plays ' + CHROM_UP[pc] + '? ' + handW + ' (' + (at + 1) + '/13)', CHROM_UP[pc] + '는 몇 번 손가락일까요? ' + handKo(hand) + ' (' + (at + 1) + '/13)')",
    "t((at >= 13 ? 'Coming down. ' : '') + 'Which finger plays ' + (at >= 13 ? CHROM_DOWN[pc] : CHROM_UP[pc]) + '? ' + handW + ' (' + (at + 1) + '/' + L + ')', (at >= 13 ? '내려와요. ' : '') + (at >= 13 ? CHROM_DOWN[pc] : CHROM_UP[pc]) + '는 몇 번 손가락일까요? ' + handKo(hand) + ' (' + (at + 1) + '/' + L + ')')")
open(sys.argv[2],'w',encoding='utf-8').write(s)
