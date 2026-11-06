// Phase 484: the Toolbox in five areas and 13 concepts (her 2026-10-17: each area holds only its own kind of thing;
// inside it, a concept is taught whole, then practised step by step). The stories of music and the practice helpers sit
// beside the five. The order is the areas' order, then each concept from the first step to the furthest.
const TOOL_AREAS = [
  { id: 'pitch', en: 'Pitch', ko: '음높이', whatEn: 'what the notes are', whatKo: '어떤 음인지' },
  { id: 'rhythm', en: 'Rhythm', ko: '리듬', whatEn: 'how long they last', whatKo: '음이 얼마나 긴지' },
  { id: 'touch', en: 'Touch and expression', ko: '터치와 표현', whatEn: 'how they are played', whatKo: '음을 어떻게 치는지' },
  { id: 'tech', en: 'Technique', ko: '테크닉', whatEn: 'the body and the hands', whatKo: '몸과 손' },
  { id: 'piece', en: 'Pieces', ko: '곡', whatEn: 'reading a piece and how it is built', whatKo: '곡을 읽고 짜임을 보는 것' },
  { id: 'beside', en: 'Beside the five', ko: '그 밖에', whatEn: 'stories of music, practice helpers', whatKo: '음악 이야기, 연습 도우미' },
];
TOOL_AREAS.forEach(a => Object.defineProperty(a, 'name', { get: () => t(a.en, a.ko), enumerable: true, configurable: true }));
const TOOL_CATS = [
  { id: 'p-staff', area: 'pitch', name: 'Keys and staff', when: 'Black-key groups, A to G, the staff and its clefs, landmarks, ledger lines and 8va, high and low and why', color: '#e4572e' },
  { id: 'p-clock', area: 'pitch', name: 'Semitones and accidentals', when: 'Tones and semitones; sharps, flats and naturals; how long a sign lasts; one key, two names; the chromatic scale', color: '#e4572e' },
  { id: 'p-intervals', area: 'pitch', name: 'Intervals', when: 'Counting an interval; major, minor and perfect; hearing intervals', color: '#e4572e' },
  { id: 'p-scales', area: 'pitch', name: 'Scales and keys', when: 'The major scale from any note, key signatures, the circle of fifths, the minor and other scales', color: '#e4572e' },
  { id: 'p-chords', area: 'pitch', name: 'Chords', when: 'Triads on any note; I, IV and V; chords in a key; inversions, cadences, seventh chords and beyond; the 12-bar blues', color: '#e4572e' },
  { id: 'r-beat', area: 'rhythm', name: 'Beat and time', when: 'The steady beat, note and rest lengths, time signatures, rhythm patterns, compound time', color: '#e4572e' },
  { id: 't-touch', area: 'touch', name: 'Touch', when: 'Legato and staccato, slurs and accents, soft to loud, the pedals, ornaments', color: '#e4572e' },
  { id: 't-tempo', area: 'touch', name: 'Tempo and character', when: 'Slow to fast, the metronome, changing speed, the pause; Italian terms (the term cards hold every term)', color: '#e4572e' },
  { id: 'k-posture', area: 'tech', name: 'Posture and hands', when: 'Sitting, hand shape, arm weight, warm-ups, the posture checklist', color: '#e4572e' },
  { id: 'k-positions', area: 'tech', name: 'Positions and finger numbers', when: 'Finger numbers, C and G positions, five-finger positions in all 12 keys', color: '#e4572e' },
  { id: 'k-play', area: 'tech', name: 'Playing scales and chords', when: 'Scale fingerings, the thumb under; chords blocked and broken; one hand, then both', color: '#e4572e' },
  { id: 'c-reading', area: 'piece', name: 'Reading tunes', when: 'Up, down or the same; steps and skips; pitch and rhythm together; sight-reading; copying by ear', color: '#e4572e' },
  { id: 'c-map', area: 'piece', name: 'Melody and form', when: 'The line of a tune, phrases, question and answer, motif and sequence; repeat signs and road maps; binary, ternary and rondo', color: '#e4572e' },
  { id: 'about', area: 'beside', name: 'Stories of music', when: 'The piano’s story, composers and their periods, styles and textures, the instruments and their ranges', color: '#e4572e' },
  { id: 'practice', area: 'beside', name: 'Practice helpers', when: 'Metronome, timer, dice, perfect reps', color: '#e4572e' },
];
const CAT_KO = {
  'p-staff': ['건반과 오선', '검은건반 무리, A부터 G까지, 오선과 음자리표, 기준 음, 덧줄과 8va, 높고 낮은 소리와 그 까닭'],
  'p-clock': ['반음과 임시표', '온음과 반음, 샤프·플랫·내추럴, 임시표는 어디까지 유효한지, 한 건반의 두 이름, 반음계'],
  'p-intervals': ['음정', '음정 세기, 장·단·완전 음정, 음정 듣기'],
  'p-scales': ['스케일과 조', '어느 음에서나 시작하는 장음계, 조표, 5도권, 단음계와 다른 음계'],
  'p-chords': ['화음', '어느 음 위에나 쌓는 3화음, I·IV·V, 조 안의 화음, 전위, 케이던스, 7화음과 그 너머, 12마디 블루스'],
  'r-beat': ['박과 박자', '꾸준한 박, 음표와 쉼표의 길이, 박자표, 리듬 패턴, 겹박자'],
  't-touch': ['터치', '레가토와 스타카토, 이음줄과 악센트, 여리게부터 세게까지, 페달, 꾸밈음'],
  't-tempo': ['템포와 느낌', '느리게부터 빠르게까지, 메트로놈, 빠르기 바꾸기, 늘임표, 이탈리아어 용어 (용어 카드에는 모든 용어)'],
  'k-posture': ['자세와 손', '앉는 법, 손 모양, 팔 무게, 준비 운동, 자세 점검'],
  'k-positions': ['손 자리와 손가락 번호', '손가락 번호, C 자리와 G 자리, 12개 조의 다섯 손가락 자리'],
  'k-play': ['스케일과 화음 치기', '스케일의 손가락 번호, 엄지 밑으로 넣기, 함께 치는 화음과 펼친 화음, 한 손씩, 그다음 양손으로'],
  'c-reading': ['선율 읽기', '위로·아래로·같은 음, 한 걸음과 건너뛰기, 음높이와 리듬 함께 읽기, 초견, 듣고 따라 치기'],
  'c-map': ['선율과 형식', '선율선, 프레이즈, 질문과 대답, 동기와 동형 진행, 도돌이표와 악보 길찾기, 2부·3부·론도 형식'],
  about: ['음악 이야기', '피아노 이야기, 작곡가와 시대, 스타일과 텍스처, 악기와 음역'],
  practice: ['연습 도우미', '메트로놈, 타이머, 주사위, 완벽한 반복'],
};
// name and when become getters (Korean from CAT_KO); the English stays as nameEn/whenEn for search
TOOL_CATS.forEach(c => { const n = c.name, w = c.when; c.nameEn = n; c.whenEn = w;
  Object.defineProperty(c, 'name', { get: () => (LANG === 'ko' && CAT_KO[c.id] ? CAT_KO[c.id][0] : n), enumerable: true, configurable: true });
  Object.defineProperty(c, 'when', { get: () => (LANG === 'ko' && CAT_KO[c.id] ? CAT_KO[c.id][1] : w), enumerable: true, configurable: true }); });
// an area's name over its concepts: a larger Playfair line (not capitals, so it never reads as one more staff head) and what
// the area holds; navy only (coral stays for 'you are here')
const toolAreaHead = (a) => <div className="tool-area" style={{display:'flex',alignItems:'baseline',gap:'4px 12px',flexWrap:'wrap',margin:'30px 4px 10px',paddingBottom:6,borderBottom:'2px solid var(--navy)'}}>
  <span style={{fontFamily:"'Playfair Display', Georgia, serif",fontSize:'clamp(21px, 5.6vw, 26px)',fontWeight:900,lineHeight:1.1,color:'var(--navy)'}}>{a.name}</span>
  <span style={{fontSize:13,color:'var(--navy-soft)'}}>{t(a.whatEn, a.whatKo)}</span></div>;
