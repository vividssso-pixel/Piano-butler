import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)

# Build W (her 2026-10-26 00:45: 'keep the Home, it is a different way in -- but the content is the same, isn't it? place them where
# they fit'; and the chip 'Stories of music'): every room of the house now has a door on the Home too, so the two ways in lead to
# the same lessons and the same checks. Six rooms had none: The Musical Alphabet, Tones & Semitones, Accidentals, The Piano,
# Composers, Styles.
# 1. Pitch, Keys and staff: the alphabet gets its own group (the chapter's lessons), after Keyboard patterns.
rep("""    { id: 'p-keys', en: 'Keyboard patterns and note names', ko: '건반 패턴과 음 이름', lessons: ['kq-black', 'kq-houses', 'kq-names', 'kq-octave'], check: 'first-steps' },""",
    """    { id: 'p-keys', en: 'Keyboard patterns', ko: '건반 패턴', lessons: ['kq-black', 'kq-houses', 'kq-names', 'kq-octave'], check: 'first-steps' },
    { id: 'p-alpha', en: 'The musical alphabet', ko: '음악 알파벳', lessons: ['name-reveal', 'step-updown', 'letter-chain', 'find-every'], check: 'note-names' },   // Build W""")
# 2. Pitch, Accidentals: three groups, each with its chapter's questions (the old Accidentals drill keeps the double signs).
rep("""  'p-clock': {
    lessons: ['ac-half', 'ac-whole', 'ac-sharp', 'ac-flat', 'ac-natural', 'ac-bar', 'ac-play', 'ac-two', 'ac-double', 'ac-cmp'], check: 'clock', tools: [], more: [],
    checkLine: ['Questions, level by level', '문제를 단계별로'],
  },""", """  'p-clock': { lessons: [], groups: [   // Build W: the chapters Tones & Semitones and Accidentals, then the double signs
    { id: 'ac-steps', en: 'Tones and semitones', ko: '온음과 반음', lessons: ['ac-half', 'ac-whole', 'ac-sharp', 'ac-flat', 'ac-two'], check: 'tones' },
    { id: 'ac-signs', en: 'Accidentals in a tune', ko: '곡 속의 임시표', lessons: ['ac-natural', 'ac-bar', 'ac-play', 'ac-cmp'], check: 'accidentals' },
    { id: 'ac-dbl', en: 'Double sharps and flats', ko: '겹샵과 겹플랫', lessons: ['ac-double'], check: 'clock', level: 35 },
  ] },""")
# 3. Stories of music: a sixth door on the Home (the piano's story, composers, styles: each chapter's lessons and its five checks).
rep("""  'c-map': { lessons: [], groups: [""", """  about: { lessons: [], groups: [   // Build W: Stories of music, the three rooms of the house's 'Stories of music' chip
    { id: 'ab-piano', en: 'The piano’s story', ko: '피아노 이야기', lessons: CHAPTER_TOOL_ORDER['piano-story'].slice(), check: 'piano-story' },
    { id: 'ab-comp', en: 'Composers', ko: '작곡가', lessons: CHAPTER_TOOL_ORDER.composers.slice(), check: 'composers' },
    { id: 'ab-styles', en: 'Styles', ko: '스타일', lessons: CHAPTER_TOOL_ORDER.styles.slice(), check: 'styles' },
  ] },
  'c-map': { lessons: [], groups: [""")
rep("""  set('home', 'tempo-walk tempo-race tap-tempo same-tune-tempo draw-tune form-builder complete-melody');
  return m;""", """  set('home', 'tempo-walk tempo-race tap-tempo same-tune-tempo draw-tune form-builder complete-melody');
  // Build W: the alphabet and one key, two names (both now Beginner rooms), the piano's story (floor 2), composers and styles (floor 4)
  set('G', 'name-reveal step-updown letter-chain find-every ac-two');
  set('P1', CHAPTER_TOOL_ORDER['piano-story'].join(' '));
  set('23', CHAPTER_TOOL_ORDER.composers.concat(CHAPTER_TOOL_ORDER.styles).join(' '));
  return m;""")
# the Home lets the one 'beside' concept with lessons open (Practice helpers stay in the Toolbox)
rep("""cat = cat0 && cat0.area !== 'beside' ? cat0 : undefined;""", """cat = cat0 && (cat0.area !== 'beside' || HOME_LIVE[cat0.id]) ? cat0 : undefined;""")
rep("""            <HomeChev on/>
          </button>
        ))}""", """            <HomeChev on/>
          </button>
        ))}
        <button style={homeRow(false)} onClick={() => go({ ha: null, hc: 'about', hs: null })}>
          <HomeAreaIcon id="about"/>
          <span style={{flex:1,minWidth:0,display:'block'}}><span style={{...homeTitle,fontSize:24}}>{t('Stories of music', '음악 이야기')}</span><span style={homeSub}>{t('The piano, composers and styles', '피아노, 작곡가, 스타일')}</span></span>
          <HomeChev on/>
        </button>""")
rep("""  if (id === 'tech') return <svg {...p} strokeWidth="3">""", """  if (id === 'about') return <svg {...p}><path d="M24 12C19 8.5 11 8.5 5 10.5V39C11 37 19 37 24 40.5C29 37 37 37 43 39V10.5C37 8.5 29 8.5 24 12Z"/><path d="M24 12V40.5"/><path d="M34 9V20L37.5 17L41 20V9.6" stroke="#e4572e" fill="#e4572e"/></svg>;   // Build W: an open book with a ribbon
  if (id === 'tech') return <svg {...p} strokeWidth="3">""")
# 4. the house's chip: 'Stories of music' (her pick, 00:45)
rep(""".map(a => [a.id, a.name]), have.has('aural')""", """.map(a => [a.id, a.id === 'beside' ? t('Stories of music', '음악 이야기') : a.name]), have.has('aural')""")

open(dst, 'w', encoding='utf-8').write(s)
print('ok')
