import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)

# Build AF-0 (part 1: the syllabus check for Grades 2-3, finding 2): five Home lessons marked Grade 4 are Grade 3 content or sit in a
# Grades 2-3 room. Music Craft Grade 3 lists all diatonic intervals and their inversions, the augmented 4th and diminished 5th,
# diminished triads (root and first inversion) and augmented triads (root position), and cadences closing phrases and periods.
# 'Sequences' moves with them: its room (Melody & Phrasing) and its twin lesson (mlx-seq) are already on the Grades 2-3 floor.
rep("""  set('4', 'iv-invert iv-tritone ch-da md-family md-ladder');""",
    """  set('4', 'md-family md-ladder');
  set('23', 'iv-invert iv-tritone ch-da');   // Build AF-0: Music Craft Grade 3 (was '4')""")
rep("""  set('4', 'ornaments grace-write question-answer melody-sequence');""",
    """  set('4', 'ornaments grace-write');
  set('23', 'question-answer melody-sequence');   // Build AF-0: Grade 3 phrases and periods; its room is on the Grades 2-3 floor (was '4')""")
# Grade 1 loose ends from the Prelim - Grade 1 syllabus check: Music Craft Grade 1 asks for the root-position I (i) and V in the
# grade's keys, majors and the harmonic minors A, E, D, G. The Chords drill had majors only: a tenth level, 'Minor keys: i or V?',
# shows the triad on the staff with the minor key's own signature; V's middle note is the raised 7th, an accidental. And
# Music Craft Preliminary's 'understand the concept of diatonic': a definition on Scales step 1.
rep("""  { n: 9, label: 'Extra: spell I, IV and V', num: '9', short: ['Spell I, IV, V', 'I, IV, V 음이름'], kind: 'spellR', time: 12 },
];""", """  { n: 9, label: 'Extra: spell I, IV and V', num: '9', short: ['Spell I, IV, V', 'I, IV, V 음이름'], kind: 'spellR', time: 12 },
  { n: 10, label: 'Minor keys: i or V?', num: '9', short: ['Minor: i or V', '단조: i, V'], kind: 'minorR', time: 9 },   // Build AF-0
];""")
rep("""'I, IV or V, in my keys': '나의 조: I, IV, V?', 'Extra: spell I, IV and V': '더 해 보기: I, IV, V의 음이름' });""",
    """'I, IV or V, in my keys': '나의 조: I, IV, V?', 'Extra: spell I, IV and V': '더 해 보기: I, IV, V의 음이름', 'Minor keys: i or V?': '단조: i일까, V일까?' });
const CHX_MINOR_KEYS = [['A', 'C', 'E'], ['E', 'G', 'B'], ['D', 'F', 'A'], ['G', 'Bb', 'D']];   // Build AF-0: [minor key, its key signature's major, the root of V]
const chxMinorKey = (k) => t(prettyNote(k) + ' minor', prettyNote(k) + '단조');""")
rep("""      return { kind: 'spellR', key, k, dg, notes: nt, answer: right, choices: shuffle([right, ...wrong]), uid };
    }
  }
  return { kind: 'spell', key: 'f', r: 'C', d: 28, answer: 'C E G', choices: ['C E G', 'C D E', 'C F A', 'C E A'], uid };
}
const chxCheck""", """      return { kind: 'spellR', key, k, dg, notes: nt, answer: right, choices: shuffle([right, ...wrong]), uid };
    }
    if (lv.kind === 'minorR') {   // Build AF-0: i is the minor tonic triad; V is major (its 3rd is the raised 7th)
      const [k, rel, five] = pick(CHX_MINOR_KEYS), dg = pick([1, 5]), key = 'mr' + k + dg;
      if (same(key)) continue;
      return { kind: 'minorR', key, k, rel, dg, notes: dg === 1 ? chxNotes(k, 'minor') : chxNotes(five, 'major'), answer: dg === 1 ? 'i' : 'V', choices: ['i', 'V'], uid };
    }
  }
  return { kind: 'spell', key: 'f', r: 'C', d: 28, answer: 'C E G', choices: ['C E G', 'C D E', 'C F A', 'C E A'], uid };
}
const chxCheck""")
rep("""  if (q.kind === 'tonic') return skgKeyName(q.k) + ': ' + chxNotesTxt(q.notes);
  return t(CHX_ROM[q.dg]""", """  if (q.kind === 'tonic') return skgKeyName(q.k) + ': ' + chxNotesTxt(q.notes);
  if (q.kind === 'minorR') { const nm = chxMinorKey(q.k), tx = chxNotesTxt(q.notes);
    return q.dg === 1 ? t('i in ' + nm + ': ' + tx + ', a minor triad', nm + '의 i: ' + tx + ', 단3화음') : t('V in ' + nm + ': ' + tx + ', a major triad; its middle note is the raised 7th', nm + '의 V: ' + tx + ', 장3화음. 가운데 음이 올라간 7번째 음이에요'); }
  return t(CHX_ROM[q.dg]""")
rep("""    tonic: t('Whose tonic triad is it?', '어느 조의 으뜸화음일까요?'), roman: t('I, IV or V?', 'I, IV, V 가운데 무엇일까요?'),""",
    """    tonic: t('Whose tonic triad is it?', '어느 조의 으뜸화음일까요?'), roman: t('I, IV or V?', 'I, IV, V 가운데 무엇일까요?'), minorR: t('i or V?', 'i일까요, V일까요?'),""")
rep("""  const head = (q.kind === 'roman' || q.kind === 'spellR') && <div style={{textAlign:'center',fontFamily:LB_SERIF,fontSize:pixel ? 14 : 22,fontWeight:900,color:pixel ? '#faf6ec' : 'var(--navy)',margin:'0 0 2px'}}>{sscSx(skgKeyName(q.k))}</div>;""",
    """  const head = (q.kind === 'roman' || q.kind === 'spellR' || q.kind === 'minorR') && <div style={{textAlign:'center',fontFamily:LB_SERIF,fontSize:pixel ? 14 : 22,fontWeight:900,color:pixel ? '#faf6ec' : 'var(--navy)',margin:'0 0 2px'}}>{sscSx(q.kind === 'minorR' ? chxMinorKey(q.k) : skgKeyName(q.k))}</div>;""")
rep("""    const kk = q.kind === 'tonic' || q.kind === 'roman' ? q.k : null;""", """    const kk = q.kind === 'tonic' || q.kind === 'roman' ? q.k : q.kind === 'minorR' ? q.rel : null;""")
rep("""        [t('C major', 'C장조 음계'), X('The major scale from C: all white keys. Its half steps are E F (3 to 4) and B C (7 to 8).', 'C에서 시작하는 장음계: 모두 흰건반. 반음은 E F(3과 4 사이)와 B C(7과 8 사이)예요.')],
      ]}/>""", """        [t('C major', 'C장조 음계'), X('The major scale from C: all white keys. Its half steps are E F (3 to 4) and B C (7 to 8).', 'C에서 시작하는 장음계: 모두 흰건반. 반음은 E F(3과 4 사이)와 B C(7과 8 사이)예요.')],
        [t('diatonic', '온음계적'), X('Belonging to the key: the seven notes of its scale. In C major the white keys are diatonic; the black keys are not.', '그 조에 속한 음: 음계의 일곱 음이에요. C장조에서는 흰건반이 온음계적인 음이고, 검은건반은 아니에요.')],   // Build AF-0: Music Craft Preliminary
      ]}/>""")

open(dst, 'w', encoding='utf-8').write(s)
print('ok')
