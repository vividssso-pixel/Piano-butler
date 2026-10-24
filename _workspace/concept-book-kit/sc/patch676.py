import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)

# Build N (her question 2026-10-24 14:06, 'nothing more from the Lesson Book in Scales?'): what the book's chapter on the major
# scale says that the Scales lessons did not, put into the lessons as they are (no new lessons, no new steps):
# 1. The same pattern from any note: the book's 'each letter once' (G major has F♯, never G♭; F major B♭, never A♯)
rep("""text: ['So the 7th note is the next key on: F♯, a whole step from E.', '그래서 7번째 음은 한 건반 더 가서 F♯이에요. E에서 온음이에요.']""",
    """text: ['So the 7th note is F♯, a whole step from E. Not G♭: a scale uses every letter once.', '그래서 7번째 음은 E에서 온음인 F♯이에요. G♭이 아니에요. 음계는 글자를 한 번씩 써요.']""")
rep("""text: ['So the 4th note is the very next key: B♭, a half step from A.', '그래서 4번째 음은 바로 옆 건반 B♭이에요. A에서 반음이에요.']""",
    """text: ['So the 4th note is the very next key: B♭, a half step from A. Not A♯: every letter once.', '그래서 4번째 음은 바로 옆 건반 B♭이에요. A에서 반음이에요. A♯이 아니에요. 글자는 한 번씩.']""")
# 2. White keys: the book's 'thumb under' and '3 over' (right hand coming down, left hand going up)
rep("""{ hand: 'RH', n: 8, text: ['Finger 5 is on top.', '5번 손가락이 맨 위예요.'] },""",
    """{ hand: 'RH', n: 8, text: ['Finger 5 is on top. Coming down, 3 crosses over the thumb.', '5번 손가락이 맨 위예요. 내려올 때는 3번이 엄지 위로 넘어가요.'] },""")
rep("""{ hand: 'LH', n: 8, text: ['Then 3: fingers 3, 2, 1.', '그다음 3개: 3, 2, 1번 손가락.'] },""",
    """{ hand: 'LH', n: 8, text: ['Then 3 crosses over the thumb: fingers 3, 2, 1.', '그다음 3번이 엄지 위로 넘어가서 3개: 3, 2, 1번 손가락.'] },""")
# 3. The degrees: the book's '8 is 1 again, an octave higher'
rep("""{t('Every note of the scale has a number and a name.', '음계의 음마다 번호와 이름이 있어요.')}""",
    """{t('Every note of the scale has a number and a name. 8 is 1 again, an octave higher.', '음계의 음마다 번호와 이름이 있어요. 8은 한 옥타브 위의 1이에요.')}""")
# 4. All twelve keys: the whole picture is the book's keyboard clock (its cover: 'turned, C major's shape starts on any key');
#    tap a key and the shape turns to start there. One by one and Your turn are as before.
rep("""  const [tk, setTk] = useState('Eb'), [at, setAt] = useState(0), [bad, setBad] = useState(null);
  const P = useScPlay([view, i, kk, tk]);""", """  const [tk, setTk] = useState('Eb'), [at, setAt] = useState(0), [bad, setBad] = useState(null), [rk, setRk] = useState('C');
  const P = useScPlay([view, i, kk, tk]);""")
rep("""    const K = scIdx('C'), N = scNames('C'), marks = {}, names = {}; K.forEach((k, j) => { marks[k] = 'pass'; names[k] = N[j]; });
    body = <>
      <div style={scS.title}>{title}</div>
      <div style={scS.line}>{t('One pattern, T T S T T T S. Start it on any of the twelve notes.', '패턴은 하나, T T S T T T S. 열두 음 어디서든 시작할 수 있어요.')}</div>
      <ScKeys ks={K} marks={marks} names={names} arcs={ST.map((_, j) => mv(K, j, false))} nonce="all"/>
      <ScPills/>""", """    body = <>
      <div style={scS.title}>{title}</div>
      <div style={scS.line}>{t('One pattern, T T S T T T S. Start it on any of the twelve notes.', '패턴은 하나, T T S T T T S. 열두 음 어디서든 시작할 수 있어요.')}</div>
      <div className="lbh-fig" style={{maxWidth:330,margin:'4px auto 8px'}}>
        <div style={{maxWidth:280,margin:'0 auto'}}><KeyRing sel={rk} onPick={(k) => { clear(); setRk(k); playKey(pbKeyPc(k), 0.5); }} o={{ shape: true, both: true, center: (C) => <text x={C} y={C + 7} textAnchor="middle" fontSize="22" fontWeight="900" fill={PEN_N} style={{fontFamily:"'Playfair Display', Georgia, serif"}}>{pbAccT(prettyNote(rk))}</text> }} label={t('The keyboard clock: the twelve keys in a ring, clockwise up. The ' + prettyNote(rk) + ' major scale is drawn as one shape.', '건반 시계: 열두 건반이 원을 이루고, 시계 방향으로 올라가요. ' + prettyNote(rk) + '장음계가 모양 하나로 그려져 있어요.')}/></div>
        <div style={{textAlign:'center',fontSize:13,fontWeight:700,color:'#6d6f9c',margin:'2px 0 2px',textWrap:'balance'}}>{t('The twelve keys in a ring. Tap a key: the same shape turns to start there.', '열두 건반을 둥글게 이었어요. 건반을 누르면 같은 모양이 돌아서 거기서 시작해요.')}</div>
      </div>
      <ScPills/>""")
# 5. The Home's line for Black keys, left hand, in the lesson's order (from the group of 2)
rep("""'One shape for B♭, E♭, A♭ and D♭.', 'B♭, E♭, A♭, D♭는 한 가지 모양.'""", """'One shape for D♭, E♭, A♭ and B♭.', 'D♭, E♭, A♭, B♭는 한 가지 모양.'""")
# 6. Korean: 샵 ends in a consonant, so 샵이나 (not 샵나), app-wide
n = s.count('샵나 '); assert n == 21, n
s = s.replace('샵나 ', '샵이나 ')
open(dst, 'w', encoding='utf-8').write(s); print('ok')
