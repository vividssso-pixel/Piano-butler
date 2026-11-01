# Reference, what is missing (2026-11-01, her 'are those all the cadences? add whatever exists and is missing'):
# cadences (Phrygian, cadential 6-4, Picardy third; the other names), scales (Dorian, Phrygian, Mixolydian, Locrian, minor
# pentatonic, blues, whole-tone), intervals (unison, the common augmented and diminished ones, tritone, compound).
# The printed ?book=reference keeps its pages as they were (first rows only), so no A4 page overflows.
import sys
p = sys.argv[1]; h = open(p, encoding='utf-8').read()
def rep(o, n, c=1):
    global h
    k = h.count(o)
    if k != c: raise SystemExit("count %d != %d for %r" % (k, c, o[:100]))
    h = h.replace(o, n)
# scales
rep("  ['lyd', 'Lydian mode: the major with its 4th raised', '리디안 선법: 4도를 올린 장음계', [0, 2, 4, 6, 7, 9, 11, 12], 'scales-7'],\n];",
    """  ['lyd', 'Lydian mode: the major with its 4th raised', '리디안 선법: 4도를 올린 장음계', [0, 2, 4, 6, 7, 9, 11, 12], 'scales-7'],
  // more scales in common use (the printed page keeps the first seven)
  ['dor', 'Dorian mode: the natural minor with its 6th raised', '도리안 선법: 6도를 올린 자연 단음계', [0, 2, 3, 5, 7, 9, 10, 12], null],
  ['phr', 'Phrygian mode: the natural minor with its 2nd lowered', '프리지안 선법: 2도를 내린 자연 단음계', [0, 1, 3, 5, 7, 8, 10, 12], null],
  ['mix', 'Mixolydian mode: the major with its 7th lowered', '믹솔리디안 선법: 7도를 내린 장음계', [0, 2, 4, 5, 7, 9, 10, 12], null],
  ['loc', 'Locrian mode: the natural minor with its 2nd and 5th lowered', '로크리안 선법: 2도와 5도를 내린 자연 단음계', [0, 1, 3, 5, 6, 8, 10, 12], null],
  ['mpent', 'minor pentatonic', '단 5음 음계', [0, 3, 5, 7, 10, 12], null],
  ['blues', 'blues scale: the minor pentatonic with the flattened 5th', '블루스 음계: 단 5음 음계에 ♭5', [0, 3, 5, 6, 7, 10, 12], null],
  ['whole', 'whole-tone: six tones', '온음 음계: 온음 여섯', [0, 2, 4, 6, 8, 10, 12], null],
];
const REF_SCALES_PAPER = 7;""")
rep("      rows={REF_SCALES.map(([id, en, ko, semis, room]) =>", "      rows={(paper ? REF_SCALES.slice(0, REF_SCALES_PAPER) : REF_SCALES).map(([id, en, ko, semis, room]) =>")
# a note after the scale table (screen only): Ionian and Aeolian
rep("    {!paper && <div style={{margin:'8px 0 0'}}>\n      <button type=\"button\" className=\"ghost-btn\" data-ref-scalesmap",
    "    {!paper && <RefNote>{t('The major is also the Ionian mode, the natural minor the Aeolian. The pentatonic on the black keys is the major pentatonic.', '장음계는 이오니안 선법, 자연 단음계는 에올리안 선법이기도 해요. 검은건반 5음 음계는 장 5음 음계예요.')}</RefNote>}\n    {!paper && <div style={{margin:'8px 0 0'}}>\n      <button type=\"button\" className=\"ghost-btn\" data-ref-scalesmap")
# intervals: unison and the common augmented / diminished ones (4th element true = not on the printed page)
rep("""const REF_IV = [[2, [['minor', '단', 1], ['major', '장', 2]]], [3, [['minor', '단', 3], ['major', '장', 4]]], [4, [['perfect', '완전', 5], ['augmented', '증', 6]]], [5, [['diminished', '감', 6], ['perfect', '완전', 7]]],
  [6, [['minor', '단', 8], ['major', '장', 9]]], [7, [['minor', '단', 10], ['major', '장', 11]]], [8, [['perfect', '완전', 12]]]];""",
"""const REF_IV = [[1, [['perfect', '완전', 0, 1], ['augmented', '증', 1, 1]], 1], [2, [['minor', '단', 1], ['major', '장', 2], ['augmented', '증', 3, 1]]], [3, [['minor', '단', 3], ['major', '장', 4]]],
  [4, [['diminished', '감', 4, 1], ['perfect', '완전', 5], ['augmented', '증', 6]]], [5, [['diminished', '감', 6], ['perfect', '완전', 7], ['augmented', '증', 8, 1]]],
  [6, [['minor', '단', 8], ['major', '장', 9], ['augmented', '증', 10, 1]]], [7, [['diminished', '감', 9, 1], ['minor', '단', 10], ['major', '장', 11]]], [8, [['perfect', '완전', 12]]]];   // [n, qualities [en, ko, semitones, extra], extra row]""")
rep("  const nm = (n) => n === 8 ? t('octave', '옥타브(8도)') : t(H3_ORD[n], H3_ORDK[n]);",
    "  const nm = (n) => n === 8 ? t('octave', '옥타브(8도)') : n === 1 ? t('unison', '완전1도(같은 음)') : t(H3_ORD[n], H3_ORDK[n]);\n  const paper = React.useContext(RefPaper), ivRows = REF_IV.filter(r => !(paper && r[2])).map(([n, qs]) => [n, qs.filter(q => !(paper && q[3]))]);")
rep("      rows={REF_IV.map(([n, qs]) =>", "      rows={ivRows.map(([n, qs]) =>")
rep("""      [t('Upside down: the numbers add to 9; major and minor swap, augmented and diminished swap, perfect stays perfect.', '자리바꿈: 숫자의 합은 9, 장↔단, 증↔감, 완전은 그대로.'), <RefDoor room="keys-5"/>],
    ]}/>""", """      [t('Upside down: the numbers add to 9; major and minor swap, augmented and diminished swap, perfect stays perfect.', '자리바꿈: 숫자의 합은 9, 장↔단, 증↔감, 완전은 그대로.'), <RefDoor room="keys-5"/>],
      ...(paper ? [] : [
        [t('Six semitones: the tritone, an augmented 4th or a diminished 5th (the same keys, two names).', '반음 여섯: 트라이톤, 증4도 또는 감5도(같은 건반, 두 이름).'), <RefDoor room="keys-5"/>],
        [t('Wider than an octave: compound intervals. A 9th is an octave and a 2nd, a 10th an octave and a 3rd; the quality stays the same.', '옥타브보다 넓으면 겹음정: 9도는 옥타브+2도, 10도는 옥타브+3도, 성질은 그대로.'), <RefDoor room={null}/>],
      ]),
    ]}/>""")
# cadences
rep("""      [<span><b style={{fontWeight:800}}>{t('interrupted', '거짓종지')}</b> · {t('the surprise', '깜짝')}</span>, <b style={{fontFamily:LB_SERIF}}>V – vi</b>, <RefDoor room="harmony-4"/>],
    ]}/></>}""", """      [<span><b style={{fontWeight:800}}>{t('interrupted', '거짓종지')}</b> · {t('the surprise', '깜짝')}</span>, <b style={{fontFamily:LB_SERIF}}>V – vi</b>, <RefDoor room="harmony-4"/>],
      ...(React.useContext(RefPaper) ? [] : [
        [<span><b style={{fontWeight:800}}>{t('cadential 6-4', '종지 6-4')}</b> · {t('the 6-4 leans into V', '6-4가 V로 기대요')}</span>, <b style={{fontFamily:LB_SERIF}}>Ic – V – I</b>, <RefDoor room="harmony-5"/>],
        [<span><b style={{fontWeight:800}}>{t('Phrygian', '프리지안 종지')}</b> · {t('an imperfect cadence in a minor key, the bass falling a semitone', '단조의 반종지, 베이스가 반음 내려가요')}</span>, <b style={{fontFamily:LB_SERIF}}>ivb – V</b>, <RefDoor room={null}/>],
        [<span><b style={{fontWeight:800}}>{t('Picardy third', '피카르디 3도')}</b> · {t('a minor-key piece ends on the major tonic', '단조 곡이 장3화음 으뜸화음으로 끝나요')}</span>, <b style={{fontFamily:LB_SERIF}}>V – I</b>, <RefDoor room={null}/>],
      ]),
    ]}/>
    {!React.useContext(RefPaper) && <RefNote>{t('Other names: perfect = authentic, imperfect = half cadence, interrupted = deceptive.', '다른 이름: 정격종지 = authentic, 반종지 = half cadence, 거짓종지 = deceptive.')}</RefNote>}</>}""")
open(p, 'w', encoding='utf-8').write(h); print('m9 ok')
