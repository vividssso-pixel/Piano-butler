import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)
SC = '/home/claude/pbtest/sc/'

# Build L (her calls 2026-10-24 11:24-11:31, on t673): Scales lessons.
# lbh.jsx again (her butler lines: only F / only B has different groups; the same pattern: start anywhere, keep T T S T T T S)
i = s.index("// ─── The Lesson Book on the Home (her call 2026-10-24"); j = s.index("\nconst scDirTag = ")
s = s[:i] + open(SC + 'lbh.jsx', encoding='utf-8').read() + s[j:]
# 1. White keys, right hand: no stop on the thumb; the thumb goes under and the group of 4 appears in one step
rep("""  { hand: 'RH', n: 4, text: ['Then the thumb goes under and starts the next group.', '그다음 엄지가 밑으로 들어가서 다음 묶음을 시작해요.'] },
  { hand: 'RH', n: 7, text: ['Now a group of 4: fingers 1, 2, 3, 4.', '이제 4개 묶음: 1, 2, 3, 4번 손가락.'] },""",
    """  { hand: 'RH', n: 7, text: ['Then the thumb goes under: a group of 4, fingers 1, 2, 3, 4.', '그다음 엄지가 밑으로 들어가서 4개 묶음: 1, 2, 3, 4번 손가락.'] },""")
# 2. Black keys: from the group of 2 up (D♭ E♭, then G♭ A♭ B♭), each with both its names
rep("""const SC_BR = [
  { key: 'Bb', text: ['B♭ major starts on a black key. The right hand always starts on finger 2, and the thumb goes on the first white key: C.', 'B♭ 장음계는 검은건반에서 시작해요. 오른손은 늘 2번으로 시작하고, 엄지는 처음 닿는 흰건반 C에 가요.'] },
  { key: 'Eb', text: ['E♭: start on finger 2. The first white key is F: the thumb goes there.', 'E♭: 2번으로 시작해요. 처음 닿는 흰건반은 F: 엄지가 거기 가요.'] },
  { key: 'Ab', text: ['A♭: start on finger 2. The first white key is C: the thumb goes there.', 'A♭: 2번으로 시작해요. 처음 닿는 흰건반은 C: 엄지가 거기 가요.'] },
  { key: 'Db', text: ['D♭: start on finger 2. The first white key is F. In all four keys the right-hand thumbs go on C and F.', 'D♭: 2번으로 시작해요. 처음 닿는 흰건반은 F. 네 조 모두 오른손 엄지는 C와 F에 가요.'] },
  { key: 'Gb', text: ['G♭ / F♯: three black keys in a row. Fingers 2, 3, 4 cover them; the thumb lands on the first white key, C♭ (B).', 'G♭ / F♯: 나란히 있는 검은건반 세 개. 2, 3, 4번이 그 셋을 맡고, 엄지는 처음 닿는 흰건반 C♭(B)에 놓여요.'] },
];""", """const SC_BR = [
  { key: 'Db', text: ['C♯ / D♭ major starts on a black key. The right hand always starts on finger 2, and the thumb goes on the first white key: F.', 'C♯ / D♭ 장음계는 검은건반에서 시작해요. 오른손은 늘 2번으로 시작하고, 엄지는 처음 닿는 흰건반 F에 가요.'] },
  { key: 'Eb', text: ['D♯ / E♭: start on finger 2. The first white key is F: the thumb goes there.', 'D♯ / E♭: 2번으로 시작해요. 처음 닿는 흰건반은 F: 엄지가 거기 가요.'] },
  { key: 'Gb', text: ['F♯ / G♭: three black keys in a row. Fingers 2, 3, 4 cover them; the thumb lands on the first white key, C♭ (B).', 'F♯ / G♭: 나란히 있는 검은건반 세 개. 2, 3, 4번이 그 셋을 맡고, 엄지는 처음 닿는 흰건반 C♭(B)에 놓여요.'] },
  { key: 'Ab', text: ['G♯ / A♭: start on finger 2. The first white key is C: the thumb goes there.', 'G♯ / A♭: 2번으로 시작해요. 처음 닿는 흰건반은 C: 엄지가 거기 가요.'] },
  { key: 'Bb', text: ['A♯ / B♭: start on finger 2. The first white key is C. In D♭, E♭, A♭ and B♭ the right-hand thumbs go on C and F.', 'A♯ / B♭: 2번으로 시작해요. 처음 닿는 흰건반은 C. D♭, E♭, A♭, B♭ 모두 오른손 엄지는 C와 F에 가요.'] },
];""")
rep("""  { key: 'Bb', text: ['B♭, E♭, A♭, D♭: the left hand starts on finger 3 and is one shape for all four: 3-2-1, 4-3-2-1, 3.', 'B♭, E♭, A♭, D♭: 왼손은 3번으로 시작하고 네 조 모두 한 가지 모양이에요: 3-2-1, 4-3-2-1, 3.'] },
  { key: 'Gb', text: ['G♭ / F♯: three black keys""", """  { key: 'Db', text: ['C♯ / D♭, D♯ / E♭, G♯ / A♭, A♯ / B♭: the left hand starts on finger 3 and is one shape for all four: 3-2-1, 4-3-2-1, 3.', 'C♯ / D♭, D♯ / E♭, G♯ / A♭, A♯ / B♭: 왼손은 3번으로 시작하고 네 조 모두 한 가지 모양이에요: 3-2-1, 4-3-2-1, 3.'] },
  { key: 'Gb', text: ['F♯ / G♭: three black keys""")
rep("""  const [i, setI] = useState(0), [nonce, setNonce] = useState(0), [kk, setKk] = useState('Bb');
  const [found, setFound] = useState([]), [bad, setBad] = useState(null), [why, setWhy] = useState(''), [ph, setPh] = useState(0);""",
    """  const [i, setI] = useState(0), [nonce, setNonce] = useState(0), [kk, setKk] = useState('Db');
  const [found, setFound] = useState([]), [bad, setBad] = useState(null), [why, setWhy] = useState(''), [ph, setPh] = useState(0);""")
rep("""      <div style={scS.line}>{RHd ? t('The same groups of 3 and 4, in another order. The right hand always starts on finger 2.', '같은 3개, 4개 묶음이 순서만 바뀌어요. 오른손은 늘 2번으로 시작해요.') : t('One shape for B♭, E♭, A♭ and D♭. The left hand starts on finger 3.', 'B♭, E♭, A♭, D♭는 한 가지 모양이에요. 왼손은 3번으로 시작해요.')}</div>
      <ScStrip rows={RHd ? [{ keys: 'B♭', key: 'Bb', hand }, { keys: 'E♭', key: 'Eb', hand }, { keys: 'A♭', key: 'Ab', hand }, { keys: 'D♭', key: 'Db', hand }, { keys: 'G♭', key: 'Gb', hand }] : [{ keys: 'B♭ E♭ A♭ D♭', key: 'Bb', hand }, { keys: 'G♭', key: 'Gb', hand }]}/>""",
    """      <div style={scS.line}>{RHd ? t('The same groups of 3 and 4, in another order. The right hand always starts on finger 2.', '같은 3개, 4개 묶음이 순서만 바뀌어요. 오른손은 늘 2번으로 시작해요.') : t('One shape for D♭, E♭, A♭ and B♭. The left hand starts on finger 3.', 'D♭, E♭, A♭, B♭는 한 가지 모양이에요. 왼손은 3번으로 시작해요.')}</div>
      <ScStrip rows={['Db', 'Eb', 'Gb', 'Ab', 'Bb'].map(k => ({ keys: scKeyBtn(k), key: k, hand }))}/>""")
rep("""        {['Bb', 'Eb', 'Ab', 'Db', 'Gb'].map(k => <button key={k} className={'chip' + (kk === k ? ' active' : '')} aria-pressed={kk === k} style={{...KF_BTN,minHeight:40,padding:'0 4px'}} onClick={() => { clear(); setKk(k); reset(); playKey(SCALES[k].rootPc, 0.5); }}>{scKeyBtn(k)}</button>)}""",
    """        {['Db', 'Eb', 'Gb', 'Ab', 'Bb'].map(k => <button key={k} className={'chip' + (kk === k ? ' active' : '')} aria-pressed={kk === k} style={{...KF_BTN,minHeight:40,padding:'0 4px'}} onClick={() => { clear(); setKk(k); reset(); playKey(SCALES[k].rootPc, 0.5); }}>{scKeyBtn(k)}</button>)}""")
# 3. Both hands: the keys from C, a half step at a time (the lesson stays as a tool; on the Home, All twelve keys covers it)
rep("""  const KEYS = ['C', 'G', 'D', 'A', 'E', 'B', 'F', 'Bb', 'Eb', 'Ab', 'Db', 'Gb'];
  const newRound = (k) => { setTk(k);""", """  const KEYS = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B'];
  const newRound = (k) => { setTk(k);""")
# 4. All twelve keys: each set from C up (white keys C D E F G A B; black keys from the group of 2), both names on the buttons
rep("""const SC_W7 = ['C', 'G', 'D', 'A', 'E', 'F', 'B'], SC_B5 = ['Bb', 'Eb', 'Ab', 'Db', 'Gb'],""", """const SC_W7 = ['C', 'D', 'E', 'F', 'G', 'A', 'B'], SC_B5 = ['Db', 'Eb', 'Gb', 'Ab', 'Bb'],""")
rep("""  { set: SC_W7, text: ['White-key starts: C G D A E F B. Tap one: the pattern T T S T T T S stays the same.', '흰건반에서 시작하는 조: C G D A E F B. 하나 눌러봐요. 패턴 T T S T T T S는 그대로예요.'] },
  { set: SC_B5, text: ['Black-key starts: B♭ E♭ A♭ D♭ G♭. Tap one: the same pattern again.', '검은건반에서 시작하는 조: B♭ E♭ A♭ D♭ G♭. 하나 눌러봐요. 같은 패턴이에요.'] },""",
    """  { set: SC_W7, text: ['White-key starts: C D E F G A B. Tap one: the pattern T T S T T T S stays the same.', '흰건반에서 시작하는 조: C D E F G A B. 하나 눌러봐요. 패턴 T T S T T T S는 그대로예요.'] },
  { set: SC_B5, text: ['Black-key starts, from the group of 2: C♯ / D♭, D♯ / E♭, then F♯ / G♭, G♯ / A♭, A♯ / B♭. Tap one: the same pattern again.', '검은건반에서 시작하는 조, 2개 묶음부터: C♯ / D♭, D♯ / E♭, 그다음 F♯ / G♭, G♯ / A♭, A♯ / B♭. 하나 눌러봐요. 같은 패턴이에요.'] },""")
# 5. On the Home, All twelve keys covers Both hands together (its fingering table is in every key): one lesson, not two
rep("""    lessons: ['sc-shape', 'sc-same', 'sc-deg', 'sc-wr', 'sc-wl', 'sc-br', 'sc-bl', 'sc-both', 'sc-all', 'sc-chrom', 'sc-min', 'sc-penta'], check: 'scales',""",
    """    lessons: ['sc-shape', 'sc-same', 'sc-deg', 'sc-wr', 'sc-wl', 'sc-br', 'sc-bl', 'sc-all', 'sc-chrom', 'sc-min', 'sc-penta'], check: 'scales',""")
open(dst, 'w', encoding='utf-8').write(s); print('ok')
