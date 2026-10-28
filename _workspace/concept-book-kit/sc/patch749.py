import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)

# Build CD (board call 22, her 09:50: check the facts against books you can find with authority, and write it up). Three checks
# of 152 claims (instruments; harmony and form; periods and genres) against Kennan, Kennedy's Oxford Dictionary of Music,
# Britannica, Grove (via its citations), open music-theory textbooks and the 2026 Manual. Notes: sc/research22/*.md.
# Three were wrong; these are fixed here, with the wordings that were loose.

# ── wrong ──
# 1. the horn in F sounds a perfect 5th lower: written C5 sounds F4 (w counts semitones; a perfect 5th is 7, not 5)
rep("""lo: -25, hi: 17, w: 5, tr: ['A transposing instrument: it sounds a perfect 5th lower than written.""",
    """lo: -25, hi: 17, w: 7, tr: ['A transposing instrument: it sounds a perfect 5th lower than written.""")
# 2. Grade 5, the chord before V: from IIb the bass steps up to V; from IVb it falls a step (A to G in C; F to E in A minor)
rep("""q.o === 'ivb' || q.o === 'iib' ? ' A first inversion: the bass steps up to V.' : ''), q.answer + '(베이스 ' + B + ')가 V–' + h5Rom(q.k, 1, 0) + '로 이어져요.' + (q.o === 'c64' ? ' ' + h5Rom(q.k, 1, 2) + '는 V와 베이스가 같고, 6도와 4도가 V로 내려가요.' : q.o === 'ivb' || q.o === 'iib' ? ' 첫째 자리바꿈: 베이스가 V로 한 음 올라가요.' : ''));""",
    """q.o === 'iib' ? ' A first inversion: the bass steps up to V.' : q.o === 'ivb' ? ' A first inversion: the bass falls a step to V.' : ''), q.answer + '(베이스 ' + B + ')가 V–' + h5Rom(q.k, 1, 0) + '로 이어져요.' + (q.o === 'c64' ? ' ' + h5Rom(q.k, 1, 2) + '는 V와 베이스가 같고, 6도와 4도가 V로 내려가요.' : q.o === 'iib' ? ' 첫째 자리바꿈: 베이스가 V로 한 음 올라가요.' : q.o === 'ivb' ? ' 첫째 자리바꿈: 베이스가 V로 한 음 내려가요.' : ''));""")
# 3. Grade 4 transposition: G major to F major is down a tone, so C♯ becomes B♮ (the Korean line had it right)
rep("""may change sign (F♯ in G major becomes B♮ in F major).""", """may change sign (C♯ in G major becomes B♮ in F major).""")

# ── loose wordings ──
# Grade 5: IIb is allowed in minor keys too (only root-position II is major keys only); six first inversions, not every one (no IIIb)
rep("""const h5Rom = (k, deg, inv) => (deg === 7 ? 'vii°' : H4_ROM[h4Min(k) ? 'min' : 'maj'][deg]) + ['', 'b', 'c'][inv];""",
    """const h5Rom = (k, deg, inv) => (deg === 7 ? 'vii°' : deg === 2 && h4Min(k) ? 'ii°' : H4_ROM[h4Min(k) ? 'min' : 'maj'][deg]) + ['', 'b', 'c'][inv];   // Build CD: ii°b in minor""")
rep("""const h5PreOpts = (k) => (h4Min(k) ? ['iv', 'ivb', 'vi', 'c64'] : ['iib', 'iv', 'ivb', 'c64']);""",
    """const h5PreOpts = (k) => (h4Min(k) ? ['iib', 'iv', 'ivb', 'vi', 'c64'] : ['iib', 'iv', 'ivb', 'c64']);   // Build CD: IIb in minor too (the syllabus stars root-position II only)""")
# ii°b–V–i in the five minor keys: the bass (the 3rd) doubled; the leading note rises to the tonic
MIN_IIB = {'Am': ["D5 F4 B3 D3", "B4 E4 G#3 E3", "C5 E4 A3 A2"], 'Em': ["A4 C4 F#3 A2", "F#4 B3 D#3 B2", "G4 B3 E3 E2"],
           'Dm': ["G5 Bb4 E4 G3", "E5 A4 C#4 A3", "F5 A4 D4 D3"], 'Gm': ["C5 Eb4 A3 C3", "A4 D4 F#3 D3", "Bb4 D4 G3 G2"],
           'Bm': ["E5 G4 C#4 E3", "C#5 F#4 A#3 F#3", "D5 F#4 B3 B2"]}
for k, v in MIN_IIB.items():
    old = '"%s":{"c64":' % k
    assert s.count(old) == 1, k
    s = s.replace(old, '"%s":{"iib":["%s","%s","%s"],"c64":' % (k, v[0], v[1], v[2]))
rep("""Before V: IIb, IV, IVb or Ic in a major key; IV, IVb, VI or Ic in a minor key (II is major keys only).""",
    """Before V: IIb, IV, IVb or Ic in a major key; IIb, IV, IVb, VI or Ic in a minor key (only II in root position is major keys only).""")
rep("""V 앞에: 장조에서는 IIb, IV, IVb, Ic; 단조에서는 IV, IVb, VI, Ic(II는 장조만).""", """V 앞에: 장조에서는 IIb, IV, IVb, Ic; 단조에서는 IIb, IV, IVb, VI, Ic(근음 자리의 II만 장조 전용).""")
rep("""  inv: [<>Grade 5 uses <b>every first inversion</b>: Ib, iib, IVb, Vb, vib, and one new chord,""", """  inv: [<>Grade 5 uses <b>six first inversions</b>: Ib, iib, IVb, Vb, vib, and one new chord,""")
rep("""    <>5급은 <b>모든 첫째 자리바꿈</b>을 써요: Ib, iib, IVb, Vb, vib, 그리고 새 화음""", """    <>5급은 <b>여섯 첫째 자리바꿈</b>을 써요: Ib, iib, IVb, Vb, vib, 그리고 새 화음""")
rep("""t('I name every first inversion, vii°b too', 'vii°b까지, 모든 첫째 자리바꿈의 이름을 말해요')""", """t('I name the six first inversions, vii°b too', 'vii°b까지, 여섯 첫째 자리바꿈의 이름을 말해요')""")
rep("""t('Play every first inversion in G major.', 'G장조의 모든 첫째 자리바꿈을 쳐요.')""", """t('Play the six first inversions in G major.', 'G장조의 여섯 첫째 자리바꿈을 쳐요.')""")
rep("""harmony, one step each: vii°b and every first inversion;""", """harmony, one step each: vii°b and the six first inversions;""")
rep("""'이론 5급 화성을 한 단계씩: vii°b와 모든 첫째 자리바꿈;""", """'이론 5급 화성을 한 단계씩: vii°b와 여섯 첫째 자리바꿈;""")
rep("""'G major: every first inversion; say each one\\'s bass note'""", """'G major: the six first inversions; say each one\\'s bass note'""")
rep("""'Every first inversion, and the chord on the leading note.', '모든 첫째 자리바꿈, 그리고 이끎음 위의 화음.'""", """'Six first inversions, and the chord on the leading note.', '여섯 첫째 자리바꿈, 그리고 이끎음 위의 화음.'""")
# Grade 6: two of the kinds of six-four are asked (textbooks name four)
rep("""<>6-4화음(둘째 자리바꿈)은 두 가지로 와요.""", """<>6-4화음(둘째 자리바꿈)에는 여러 종류가 있고, 이 급은 둘을 물어요.""")
rep("""<>A six-four (a second inversion) comes two ways.""", """<>There are several kinds of six-four (a second inversion); this grade asks for two.""")
# sonata form: a minor-key movement's second subject is usually in the relative major; K. 545's famous surprise
rep("""<b>the exposition</b> (two subjects, the second in the dominant),""", """<b>the exposition</b> (two subjects, the second in the dominant, or in a minor key usually the relative major),""")
rep("""<b>제시부</b>(두 주제, 둘째는 딸림조로),""", """<b>제시부</b>(두 주제, 둘째는 딸림조로, 단조라면 흔히 나란한조로),""")
rep("""{t('Listen to: Mozart, Sonata in C major K. 545, first movement · Beethoven, Sonata in F minor Op. 2 No. 1, first movement', '들어 볼 곡: 모차르트, 소나타 C장조 K. 545, 첫 악장 · 베토벤, 소나타 F단조 Op. 2 No. 1, 첫 악장')}""",
    """{t('Listen to: Mozart, Sonata in C major K. 545, first movement (a surprise: its recapitulation starts in F major) · Beethoven, Sonata in F minor Op. 2 No. 1, first movement (its second subject is in A♭ major)', '들어 볼 곡: 모차르트, 소나타 C장조 K. 545, 첫 악장(깜짝: 재현부가 F장조로 시작해요) · 베토벤, 소나타 F단조 Op. 2 No. 1, 첫 악장(둘째 주제는 A♭장조)')}""")
# Grade 5 set works: 'Comfort ye' is an accompanied recitative (strings); 'Ev'ry valley' is not a da capo aria
rep("""few repeats, a light accompaniment (often just harpsichord and cello). The aria shows a character\\'s feelings: a shaped melody, words repeated, a fuller accompaniment; in Handel often da capo, A B A.'""",
    """few repeats, a light accompaniment (often just harpsichord and cello; "Comfort ye" has the strings too). The aria shows a character\\'s feelings: a shaped melody, words repeated, a fuller accompaniment; many of Handel\\'s are da capo arias, A B A ("He was despised"), though "Ev\\'ry valley" is not.'""")
rep("""되풀이가 적고, 가벼운 반주(흔히 하프시코드와 첼로만). 아리아는 인물의 마음을 보여 줘요: 모양 있는 선율, 되풀이되는 가사, 더 풍성한 반주; 헨델에서는 흔히 다 카포, A B A.'""",
    """되풀이가 적고, 가벼운 반주(흔히 하프시코드와 첼로만; "위로하라"에는 현악기도 함께해요). 아리아는 인물의 마음을 보여 줘요: 모양 있는 선율, 되풀이되는 가사, 더 풍성한 반주; 헨델의 아리아 중 많은 곡이 다 카포 아리아, A B A("그는 멸시를 받아"), 하지만 "골짜기마다"는 아니에요.'""")
rep("""    ex: ['Mozart: Eine kleine Nachtmusik, K. 525, third movement', '모차르트: 아이네 클라이네 나흐트무지크 K. 525, 셋째 악장'] },""",
    """    ex: ['Mozart: Divertimento in E♭ major, K. 563, third movement · Eine kleine Nachtmusik, K. 525, third movement', '모차르트: 디베르티멘토 E♭장조 K. 563, 셋째 악장 · 아이네 클라이네 나흐트무지크 K. 525, 셋째 악장'] },""")
# the dances: the French courante is stately (the Italian corrente runs); where the sarabande and the gigue came from
rep("""    say: ['A "running" dance in triple time, its beats shifting between 3/2 and 6/4 (hemiola).', '세박자의 "달리는" 춤곡, 박이 3/2와 6/4 사이를 오가요(헤미올라).'] },""",
    """    say: ['Its name means "running", but the French courante is grand and stately, in triple time, its beats shifting between 3/2 and 6/4 (hemiola).', '이름은 "달리기"라는 뜻이지만, 프랑스 쿠랑트는 당당하고 위엄 있는 세박자 춤곡, 박이 3/2와 6/4 사이를 오가요(헤미올라).'] },""")
rep("""['Courante', '쿠랑트', 'running, in 3', '달리듯, 3박자']""", """['Courante', '쿠랑트', 'in 3; its name means "running"', '3박자; 이름은 "달리기"라는 뜻']""")
rep("""from: ['Spanish', '스페인']""", """from: ['Spanish and Latin American', '스페인과 라틴아메리카']""")
rep("""from: ['English (the jig)', '영국(지그)']""", """from: ['British (the jig)', '영국(지그)']""")
# pentatonic: the black keys are one pentatonic scale, not the only one
rep("""clue: ['Five notes, no semitones: the black keys.', '반음 없는 다섯 음: 검은건반.']""", """clue: ['Five notes, no semitones: the black keys, or C D E G A.', '반음 없는 다섯 음: 검은건반, 또는 C D E G A.']""")
# Grade 6 general knowledge: sonatas usually three movements; the 'Emperor' is the famous concerto without a cadenza; Figaro's overture is one quick piece
rep("""['sonata', ['Three movements for a pianist, or a violinist and a pianist.', '피아니스트 한 명, 또는 바이올리니스트와 피아니스트를 위한 세 악장.']]""",
    """['sonata', ['Usually three movements, for a pianist, or a violinist and a pianist.', '보통 세 악장, 피아니스트 한 명, 또는 바이올리니스트와 피아니스트를 위해.']]""")
rep("""    ex: ['Mozart: Piano Concerto No. 23 in A major, K. 488 · Beethoven: Piano Concerto No. 5 ("Emperor")', '모차르트: 피아노 협주곡 23번 A장조 K. 488 · 베토벤: 피아노 협주곡 5번("황제")'] },""",
    """    ex: ['Mozart: Piano Concerto No. 23 in A major, K. 488 (its first-movement cadenza is Mozart\\'s own) · Grieg: Piano Concerto in A minor', '모차르트: 피아노 협주곡 23번 A장조 K. 488(첫 악장 카덴차를 모차르트가 직접 썼어요) · 그리그: 피아노 협주곡 A단조'] },""")
rep("""then fast, the voices coming in one after another. Later there were concert overtures, single pieces for the concert hall.', '오페라, 오라토리오, 연극을 여는 관현악곡. 헨델의 서곡은 프랑스풍 서곡: 점음표 리듬으로 느리고 웅장하게, 그다음 성부가 차례로 들어오며 빠르게. 뒤에는 연주회장을 위한 한 곡짜리 연주회용 서곡도 나왔어요.'],""",
    """then fast, the voices coming in one after another. Mozart\\'s overture to Figaro is one quick piece. Later there were concert overtures, single pieces for the concert hall.', '오페라, 오라토리오, 연극을 여는 관현악곡. 헨델의 서곡은 프랑스풍 서곡: 점음표 리듬으로 느리고 웅장하게, 그다음 성부가 차례로 들어오며 빠르게. 모차르트의 피가로 서곡은 빠른 한 곡이에요. 뒤에는 연주회장을 위한 한 곡짜리 연주회용 서곡도 나왔어요.'],""")
# the genre cards a teacher could mark either way: each card now names the kind that belongs to one period
rep("""['oratorio', 'baroque', 'Oratorio', '오라토리오']""", """['oratorio', 'baroque', 'Oratorio by Handel (Messiah)', '헨델의 오라토리오(메시아)']""")
rep("""['symph', 'classical', 'Symphony', '교향곡']""", """['symph', 'classical', 'Symphony with a minuet (Haydn, Mozart)', '미뉴에트가 있는 교향곡(하이든, 모차르트)']""")
rep("""['quartet', 'classical', 'String quartet', '현악 4중주']""", """['quartet', 'classical', 'The string quartet is born (Haydn)', '현악 4중주의 탄생(하이든)']""")
rep("""['csonata', 'classical', 'Sonata in sonata form', '소나타 형식의 소나타']""", """['csonata', 'classical', 'Piano sonata, first movement in sonata form', '첫 악장이 소나타 형식인 피아노 소나타']""")
rep("""['serial', 'modern', 'Twelve-note (serial) music', '12음(음렬) 음악']""", """['serial', 'modern', 'Schoenberg\\'s twelve-note music (the 1920s)', '쇤베르크의 12음 음악(1920년대)']""")
# the tuba in F: the F is its size, not a transposition
rep("""tr: ['Written at the pitch it sounds, in bass clef. The bass of the brass.', '소리 나는 음 그대로, 낮은음자리표로 적어요. 금관의 베이스.']""",
    """tr: ['Written at the pitch it sounds, in bass clef: the F in its name is its size, not a transposition. The bass of the brass.', '소리 나는 음 그대로, 낮은음자리표로 적어요: 이름의 F는 크기이지 이조가 아니에요. 금관의 베이스.']""")
# the ranges table is at sounding pitch: the B♭ trumpet sounds E3 to B♭5, as the brass pad says (F♯3 to D6 was nearer its written range)
rep("""['Trumpet', 'F#3', 'D6']""", """['Trumpet', 'E3', 'Bb5']""")
# Grade 8, one chord four keys: the note that rises is the new key's leading note, so it takes that spelling (A♭ written G♯)
rep("""const fkKey = (pc, m) =>""", """const fkLn = (T) => { const L = 'CDEFGAB', NAT = [0, 2, 4, 5, 7, 9, 11], li = (L.indexOf(T[0]) + 6) % 7, pc = { C: 0, D: 2, E: 4, F: 5, G: 7, A: 9, B: 11 }[T[0]] + (T.includes('♯') ? 1 : T.includes('♭') ? -1 : 0);
  const d = spPc(pc - 1 - NAT[li]); return L[li] + (d === 0 ? '' : d === 1 ? '♯' : d === 2 ? '𝄪' : '♭'); };   // Build CD: the leading note of the key on T, spelled a letter below
const fkKey = (pc, m) =>""")
rep("""door != null ? t(nameOf(door) + ' rose a semitone to ' + FK_NAME[m][spPc(door + 1)] + ': ' + fkKey(spPc(door + 1), m) + '. ' + tried.length + ' of 4 keys.', nameOf(door) + '에서 반음 올라 ' + FK_NAME[m][spPc(door + 1)] + ': ' + fkKey(spPc(door + 1), m) + '. 네 조 중 ' + tried.length + '개.')""",
    """door != null ? (() => { const T = FK_NAME[m][spPc(door + 1)], ln = fkLn(T), as = ln === nameOf(door) ? '' : ln;
        return t(nameOf(door) + (as ? ', written ' + as + ' as the leading note,' : '') + ' rose a semitone to ' + T + ': ' + fkKey(spPc(door + 1), m) + '. ' + tried.length + ' of 4 keys.', nameOf(door) + (as ? '(이끔음으로는 ' + as + ')' : '') + '에서 반음 올라 ' + T + ': ' + fkKey(spPc(door + 1), m) + '. 네 조 중 ' + tried.length + '개.'); })()""")
rep("""(in a minor key iv, ivb, VI or ic). Each leads smoothly into V: hear it, then name it.</>,""", """(in a minor key ii°b, iv, ivb, VI or ic). Each leads smoothly into V: hear it, then name it.</>,""")
rep("""(단조에서는 iv, ivb, VI, ic). 모두 V로 매끄럽게 이어져요""", """(단조에서는 ii°b, iv, ivb, VI, ic). 모두 V로 매끄럽게 이어져요""")
rep("""iib, IV, IVb or Ic in a major key; iv, ivb, VI or ic in a minor key.">""", """iib, IV, IVb or Ic in a major key; ii°b, iv, ivb, VI or ic in a minor key.">""")
rep("""// the chord before a cadence (IIb, IV, IVb or Ic; in a minor key iv, ivb, VI or ic);""", """// the chord before a cadence (IIb, IV, IVb or Ic; in a minor key ii°b, iv, ivb, VI or ic: Build CD);""")

# Grade 8 double minor thirds (re-read in the book, p75): the right hand's fingers were right, the pattern was told loosely
# (the bottom does not simply alternate, the top does not simply go round). The real rule: the bottom note takes the thumb on a
# white key and 2 on a black key; the top note is Grade 7's 3-4-5 chromatic (black 3, white 4, F and C 5)
rep("""오른손 운지는 무늬가 있어요: 아랫음은 <b>1과 2가 번갈아</b>, 윗음은 <b>3, 4, 5</b>를 돌려요. <b>5번은 F와 C</b>에(3-4-5 반음계의 오른손처럼!).""",
    """오른손 운지는 무늬가 있어요: 아랫음은 <b>흰건반이면 엄지, 검은건반이면 2</b>; 윗음은 <b>7급의 3-4-5 반음계</b> 그대로: 검은건반 3, 흰건반 4, <b>F와 C는 5</b>.""")
rep("""The right hand's fingering has a pattern: the bottom notes <b>take turns with 1 and 2</b>; the top notes cycle <b>3, 4, 5</b>. <b>Finger 5 lands on F and C</b> (just as in the 3-4-5 chromatic!).""",
    """The right hand's fingering has a pattern: the bottom note takes <b>the thumb on a white key, 2 on a black key</b>; the top note plays <b>Grade 7's 3-4-5 chromatic</b>: 3 on black, 4 on white, <b>5 on F and C</b>.""")
rep("""<>아랫음은 1과 2가 <b>번갈아</b>, 윗음은 <b>3 4 5</b>를 돌아요. 5번은 <b>F와 C</b>에: 7급 3-4-5 반음계와 같은 자리!</> : <>The bottom notes <b>take turns, 1 and 2</b>; the top notes go round <b>3 4 5</b>. Finger 5 lands on <b>F and C</b>: the same places as Grade 7's 3-4-5 chromatic!</>""",
    """<>아랫음은 <b>흰건반이면 엄지, 검은건반이면 2</b>. 윗음은 <b>7급 3-4-5 반음계</b>와 똑같아요: 검은건반 3, 흰건반 4, <b>F와 C는 5</b>. 두 규칙만 알면 끝!</> : <>The bottom note: <b>the thumb on a white key, 2 on a black key</b>. The top note: exactly <b>Grade 7's 3-4-5 chromatic</b>: 3 on black, 4 on white, <b>5 on F and C</b>. Two rules, and you have it!</>""")
rep("""      <LbRemember>{t('1 and 2 take turns; 3 4 5 go round.', '1과 2는 번갈아; 3 4 5는 돌아요.')}</LbRemember>""",
    """      <LbRemember>{t('Bottom: thumb on white, 2 on black. Top: the 3-4-5 chromatic.', '아래: 흰건반 엄지, 검은건반 2. 위: 3-4-5 반음계.')}</LbRemember>""")
rep("""      say="“1 and 2 take turns; 3 4 5 go round.”"/>""", """      say="“Bottom: thumb on white, 2 on black. Top: the 3-4-5 chromatic.”"/>""")
rep("""'1 and 2 take turns; 3 4 5 go round.', '1과 2는 번갈아; 3 4 5는 돌아요.', lwTapQ(S8DThirdsPad""", """'Bottom: thumb on white, 2 on black. Top: the 3-4-5 chromatic.', '아래: 흰건반 엄지, 검은건반 2. 위: 3-4-5 반음계.', lwTapQ(S8DThirdsPad""")

open(dst, 'w', encoding='utf-8').write(s)
print('ok')
