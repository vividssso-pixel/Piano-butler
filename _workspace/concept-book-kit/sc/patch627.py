import sys
a, bb = sys.argv[1], sys.argv[2]
s = open(a, encoding='utf-8').read()
def rep(x, y, n=1):
    global s
    assert s.count(x) == n, (s.count(x), x[:90])
    s = s.replace(x, y)
blk = open('/home/claude/pbtest/sc/st_block.jsx', encoding='utf-8').read()
# Home structure: Keys and staff becomes six concepts
rep("const homeCats = (areaId) => TOOL_CATS.filter(c => c.area === areaId).flatMap(c => c.id === 'p-scales' ? HOME_VIRTUAL : [c]);\nconst homeCatById = (id) => TOOL_CATS.find(c => c.id === id) || HOME_VIRTUAL.find(c => c.id === id);",
"""const HOME_STAFF = [{ id: 'p-keys', area: 'pitch', en: 'Keyboard patterns', ko: '건반 무늬' }, { id: 'p-names', area: 'pitch', en: 'Note names', ko: '음 이름' }, { id: 'p-stf', area: 'pitch', en: 'The staff and clefs', ko: '오선과 음자리표' },
  { id: 'p-lines', area: 'pitch', en: 'Line and space names', ko: '줄과 칸의 이름' }, { id: 'p-ledger', area: 'pitch', en: 'Ledger lines and 8va', ko: '덧줄과 8va' }, { id: 'p-range', area: 'pitch', en: 'Pitch and range', ko: '음높이와 음역' }]
  .map(v => ({ id: v.id, area: v.area, get name() { return LANG === 'ko' ? v.ko : v.en; } }));
const homeCats = (areaId) => TOOL_CATS.filter(c => c.area === areaId).flatMap(c => c.id === 'p-scales' ? HOME_VIRTUAL : c.id === 'p-staff' ? HOME_STAFF : [c]);
const homeCatById = (id) => TOOL_CATS.find(c => c.id === id) || HOME_VIRTUAL.find(c => c.id === id) || HOME_STAFF.find(c => c.id === id);""")
rep("const HOME_LINE = {\n", """const HOME_LINE = {
  'p-keys': ['Small houses and big houses', '작은 집과 큰 집'],
  'p-names': ['The letters A to G', 'A부터 G까지의 글자'],
  'p-stf': ['Lines, spaces and the two clefs', '줄, 칸, 두 음자리표'],
  'p-lines': ['The name of every line and space', '모든 줄과 칸의 이름'],
  'p-ledger': ['Past the five lines, and 8va', '다섯 줄 밖으로, 그리고 8va'],
  'p-range': ['High, low and how far a piano reaches', '높고 낮음, 그리고 피아노가 닿는 범위'],
""")
rep("const HOME_LIVE = {\n", """const HOME_LIVE = {
  'p-keys': { lessons: ['kp-hear', 'kp-houses', 'kp-white', 'kp-piano', 'kp-song'], check: 'first-steps', tools: [], more: [], checkLine: ['Questions, level by level', '문제를 단계별로'] },
  'p-names': { lessons: ['nn-letters', 'nn-wheel', 'nn-updown', 'nn-find', 'nn-skip'], check: 'note-names', tools: [], more: [], checkLine: ['Questions, level by level', '문제를 단계별로'] },
  'p-stf': { lessons: ['sf-lines', 'sf-climb', 'sf-treble', 'sf-bass', 'sf-clefs', 'sf-story'], check: 'staff', tools: [], more: [], checkLine: ['Questions, level by level', '문제를 단계별로'] },
  'p-lines': { lessons: ['ws-clef', 'ws-treble', 'ws-bass', 'ws-landmarks', 'ws-hop', 'ws-fold', 'ws-write', 'ws-flash'], check: 'whole-staff', tools: [], more: [], checkLine: ['Questions, level by level', '문제를 단계별로'] },
  'p-ledger': { lessons: ['ll-rungs', 'll-up', 'll-down', 'll-twins', 'll-fold', 'll-cs', 'll-8va'], check: 'ledger-lines', tools: [], more: [], checkLine: ['Questions, level by level', '문제를 단계별로'] },
  'p-range': { lessons: ['sr-zone', 'sr-big', 'sr-family', 'sr-ladder', 'sr-range'], check: 'pitch-range', tools: [], more: [], checkLine: ['Questions, level by level', '문제를 단계별로'] },
""")
# components and registrations, placed before scDirTag like the modes block
reg = r"""
const KS_ROWS = [
  ['p-keys', [
    ['kp-hear', 'High or low?', '높을까, 낮을까?', 'Hear a note and say: high or low.', '소리를 듣고 높은지 낮은지 말해요.', ksL('High or low?', '높을까, 낮을까?', 'Hear a note and say: high or low.', '소리를 듣고 높은지 낮은지 말해요.', <HighLowGame pitchOnly/>)],
    ['kp-houses', 'Small house, big house', '작은 집, 큰 집', 'Two black keys are a small house. Three are a big house.', '검은건반 두 개는 작은 집, 세 개는 큰 집이에요.', ksL('Small house, big house', '작은 집, 큰 집', 'Two black keys are a small house. Three black keys are a big house.', '검은건반 두 개는 작은 집, 세 개는 큰 집이에요.', <KeyHouses modes={['houses']}/>)],
    ['kp-white', 'The white keys of each house', '집마다 있는 흰건반', 'Which white keys live under each roof.', '지붕 아래에 어떤 흰건반이 사는지.', ksL('The white keys of each house', '집마다 있는 흰건반', 'Which white keys live under each roof.', '지붕 아래에 어떤 흰건반이 사는지 알아봐요.', <WhoseHouse/>)],
    ['kp-piano', 'The whole piano', '피아노 전체', '88 keys: 7 small houses, 7 big houses, and where middle C lives.', '88건반: 작은 집 7개, 큰 집 7개, 그리고 가운데 도의 자리.', ksL('The whole piano', '피아노 전체', '88 keys: 7 small houses, 7 big houses, and where middle C lives.', '88건반: 작은 집 7개, 큰 집 7개, 그리고 가운데 도의 자리.', <WholePiano/>)],
    ['kp-song', 'First black-key song', '첫 검은건반 노래', 'Hot Cross Buns and Mary, by rote.', '따라 치는 Hot Cross Buns와 Mary.', ksL('First black-key song', '첫 검은건반 노래', 'Hot Cross Buns and Mary, by rote.', '따라 치는 Hot Cross Buns와 Mary.', <BlackKeySong/>)],
  ]],
  ['p-names', [
    ['nn-letters', 'A to G on the keys', '건반 위의 A~G', 'The letters live at the houses: C D E at the small house, F G A B at the big.', '글자는 집마다 살아요: 작은 집에 C D E, 큰 집에 F G A B.', ksL('A to G on the keys', '건반 위의 A~G', 'The letters live at the houses: C D E at the small house, F G A B at the big house.', '글자는 집마다 살아요: 작은 집에 C D E, 큰 집에 F G A B.', <><KeyHouses modes={['small', 'big']}/><WhichLetter/></>)],
    ['nn-wheel', 'The seven letters', '일곱 글자', 'A to G, then back to A.', 'A부터 G까지, 그리고 다시 A.', ksL('The seven letters', '일곱 글자', 'Only A to G. After G the letters start again at A.', 'A부터 G까지만 있어요. G 다음은 다시 A예요.', <NameReveal/>)],
    ['nn-updown', 'Up and down the letters', '글자 위로, 아래로', 'Right is up, forwards through the letters.', '오른쪽은 위, 글자를 앞으로.', ksL('Up and down the letters', '글자 위로, 아래로', 'Right is up: forwards through the letters. Left is down: backwards.', '오른쪽은 위로 글자를 앞으로, 왼쪽은 아래로 글자를 뒤로 가요.', <UpDownWalk/>)],
    ['nn-find', 'Find every letter', '모든 글자 찾기', 'The same letter comes back once in every octave.', '같은 글자는 옥타브마다 한 번씩 돌아와요.', ksL('Find every letter', '모든 글자 찾기', 'The same letter comes back once in every octave. Find them all.', '같은 글자는 옥타브마다 한 번씩 돌아와요. 모두 찾아보세요.', <FindAll/>)],
    ['nn-skip', 'Skip a letter', '글자 건너뛰기', 'Say the letter two or three steps on.', '두 걸음, 세 걸음 뒤의 글자를 말해요.', ksL('Skip a letter', '글자 건너뛰기', 'Say the letter two or three steps on.', '두 걸음, 세 걸음 뒤의 글자를 말해요.', <LetterChainDrill sizes={[2, 3]}/>)],
  ]],
  ['p-stf', [
    ['sf-lines', 'Lines and spaces', '줄과 칸', 'The staff has 5 lines and 4 spaces, counted from the bottom.', '오선은 5개의 줄과 4개의 칸이고, 아래에서부터 세요.', ksL('Lines and spaces', '줄과 칸', 'The staff has 5 lines and 4 spaces, counted from the bottom.', '오선은 5개의 줄과 4개의 칸이고, 아래에서부터 세요.', <StaffBasics/>)],
    ['sf-climb', 'Up the staff, up the piano', '오선을 오르면 건반도 올라가요', 'Line, space, line: each step up the staff is the next white key.', '줄, 칸, 줄: 오선에서 한 걸음 올라가면 흰건반도 다음 건반이에요.', ksL('Up the staff, up the piano', '오선을 오르면 건반도 올라가요', 'Line, space, line: each step up the staff is the next white key to the right.', '줄, 칸, 줄: 오선에서 한 걸음 올라가면 오른쪽 다음 흰건반이에요.', <StaffClimb/>)],
    ['sf-treble', 'The Queen’s five', '여왕의 다섯 음', 'The treble clef: Clara to the Queen, C D E F G.', '높은음자리표: 클라라에서 여왕까지, C D E F G.', () => <KsFive clef="treble"/>],
    ['sf-bass', 'The King’s five', '왕의 다섯 음', 'The bass clef: the King to Clara, F G A B C.', '낮은음자리표: 왕에서 클라라까지, F G A B C.', () => <KsFive clef="bass"/>],
    ['sf-clefs', 'The grand staff', '큰보표', 'Two staves, one key: middle C.', '오선 두 개, 건반 하나: 가운데 도.', ksL('The grand staff', '큰보표', 'Treble and bass make the grand staff. They meet at middle C.', '높은음자리표와 낮은음자리표가 큰보표를 이루고, 가운데 도에서 만나요.', <ClefBasics/>)],
    ['sf-story', 'Why the G clef and the F clef', '왜 G 음자리표와 F 음자리표일까', 'The Queen and the King.', '여왕과 왕.', ksL('Why the G clef and the F clef', '왜 G 음자리표와 F 음자리표일까', 'The Queen’s clef curls round G. The King’s two dots guard F.', '여왕의 소용돌이는 G를 감싸고, 왕의 두 점은 F를 지켜요.', <ClefStory/>)],
  ]],
  ['p-lines', [
    ['ws-clef', 'Same place, two names', '같은 자리, 두 이름', 'Read the clef first: the same line has a different name in each.', '음자리표를 먼저 읽어요: 같은 줄도 이름이 달라요.', ksL('Same place, two names', '같은 자리, 두 이름', 'Read the clef first: the same line has a different name in each clef.', '음자리표를 먼저 읽어요: 같은 줄도 음자리표마다 이름이 달라요.', <WsCrownFlip/>)],
    ['ws-treble', 'Treble clef: the sayings', '높은음자리표의 문장', 'Every Good Boy Does Fine, and the spaces spell FACE.', '줄과 칸을 문장으로 외워요.', ksL('Treble clef: the sayings', '높은음자리표의 문장', 'Tap the lines and the spaces from the bottom and the saying builds.', '아래에서부터 줄과 칸을 눌러 문장을 만들어요.', <MnemonicStaff fixed="treble"/>)],
    ['ws-bass', 'Bass clef: the sayings', '낮은음자리표의 문장', 'The same for the King’s staff.', '왕의 오선도 같은 방법으로.', ksL('Bass clef: the sayings', '낮은음자리표의 문장', 'Tap the lines and the spaces from the bottom and the saying builds.', '아래에서부터 줄과 칸을 눌러 문장을 만들어요.', <MnemonicStaff fixed="bass"/>)],
    ['ws-landmarks', 'The five landmarks', '다섯 기준 음', 'The Queen’s G, the King’s F, middle C and the two space Cs.', '여왕의 G, 왕의 F, 가운데 도, 그리고 칸에 있는 두 C.', ksL('The five landmarks', '다섯 기준 음', 'The Queen’s G, the King’s F, middle C and the two space Cs.', '여왕의 G, 왕의 F, 가운데 도, 그리고 칸에 있는 두 C.', <StaffExplorer/>)],
    ['ws-hop', 'Count from a landmark', '기준 음에서 세기', 'Name a note by counting from the nearest landmark.', '가장 가까운 기준 음에서 세어서 이름을 맞혀요.', ksL('Count from a landmark', '기준 음에서 세기', 'Name a note by counting from the nearest landmark.', '가장 가까운 기준 음에서 세어서 이름을 맞혀요.', <LandmarkHop/>)],
    ['ws-fold', 'Fold at Clara’s ladder', '클라라의 사다리에서 접기', 'The two staves are mirror images: G meets F, C meets C.', '두 오선은 거울이에요: G는 F와, C는 C와 만나요.', ksL('Fold at Clara’s ladder', '클라라의 사다리에서 접기', 'The two staves are mirror images: G meets F, C meets C.', '두 오선은 거울이에요: G는 F와, C는 C와 만나요.', <FoldStaff/>)],
    ['ws-write', 'Write the note', '음 쓰기', 'Tap the line or space where the named note belongs.', '이름이 주어진 음이 놓일 줄이나 칸을 눌러요.', ksL('Write the note', '음 쓰기', 'Tap the line or space where the named note belongs.', '이름이 주어진 음이 놓일 줄이나 칸을 눌러요.', <WriteTheNote/>)],
    ['ws-flash', 'Flash cards', '플래시 카드', 'Know the note at a glance, without counting.', '세지 않고 한눈에 음을 알아봐요.', ksL('Flash cards', '플래시 카드', 'Know the note at a glance, without counting.', '세지 않고 한눈에 음을 알아봐요.', <FlashCards/>)],
  ]],
  ['p-ledger', [
    ['ll-rungs', 'Drawing ledger lines', '덧줄 그리기', 'A little wider than the note, the same spacing, no gaps.', '음표보다 조금 넓게, 같은 간격으로, 빈틈 없이.', ksL('Drawing ledger lines', '덧줄 그리기', 'Clara’s ladder is a ledger line: a little wider than the note, the same spacing, no gaps.', '클라라의 사다리는 덧줄이에요: 음표보다 조금 넓게, 같은 간격으로, 빈틈 없이.', <LlRungs/>)],
    ['ll-up', 'Up into the sky', '하늘로 올라가기', 'Climb above the staff, one ledger line at a time.', '덧줄을 하나씩 오선 위로 올라가요.', ksL('Up into the sky', '하늘로 올라가기', 'Climb above the treble staff, one ledger line at a time.', '높은음자리표 위로 덧줄을 하나씩 올라가요.', <LlClimb clef="treble"/>)],
    ['ll-down', 'Down into the sea', '바다로 내려가기', 'Go below the bass staff, one ledger line at a time.', '낮은음자리표 아래로 덧줄을 하나씩 내려가요.', ksL('Down into the sea', '바다로 내려가기', 'Go below the bass staff, one ledger line at a time.', '낮은음자리표 아래로 덧줄을 하나씩 내려가요.', <LlClimb clef="bass"/>)],
    ['ll-twins', 'Between the staves', '두 오선 사이', 'One key, written on either clef.', '건반 하나, 두 음자리표 어느 쪽에서도 쓸 수 있어요.', ksL('Between the staves', '두 오선 사이', 'A note between the staves can be written on either clef, and it is one key.', '두 오선 사이의 음은 어느 음자리표로도 쓸 수 있고, 건반은 하나예요.', <LlTwins/>)],
    ['ll-fold', 'The Cs meet too', 'C도 만나요', 'Fold the staves with the ledger Cs.', '덧줄 C까지 넣어서 오선을 접어요.', ksL('The Cs meet too', 'C도 만나요', 'Fold the staves again: with the ledger lines, the Cs meet as well.', '오선을 다시 접어요: 덧줄까지 넣으면 C끼리도 만나요.', <FoldStaff ledger/>)],
    ['ll-cs', 'The five Cs', '다섯 개의 C', 'Name a ledger note by hopping from the nearest C.', '가장 가까운 C에서 세어서 덧줄 음의 이름을 알아봐요.', ksL('The five Cs', '다섯 개의 C', 'Name a ledger note by hopping from the nearest C.', '가장 가까운 C에서 세어서 덧줄 음의 이름을 알아봐요.', <LlFiveCs/>)],
    ['ll-8va', '8va and 8vb', '8va와 8vb', 'An octave higher or lower than written.', '쓰인 것보다 한 옥타브 위나 아래.', ksL('8va and 8vb', '8va와 8vb', 'An octave higher or lower than written.', '쓰인 것보다 한 옥타브 위나 아래로 쳐요.', <OttavaDemo/>)],
  ]],
  ['p-range', [
    ['sr-zone', 'Low, middle or high?', '낮음, 중간, 높음', 'Hear a note low, middle or high on the keys, then say where it was.', '건반에서 낮은 소리, 중간 소리, 높은 소리를 듣고 어디였는지 말해요.', ksL('Low, middle or high?', '낮음, 중간, 높음', 'Hear a note low, middle or high on the keys, then say where it was.', '건반에서 낮은 소리, 중간 소리, 높은 소리를 듣고 어디였는지 말해요.', <SprZonePad/>)],
    ['sr-big', 'Big is low, small is high', '큰 것은 낮고 작은 것은 높아요', 'Longer bars sound lower.', '긴 막대일수록 낮은 소리예요.', ksL('Big is low, small is high', '큰 것은 낮고 작은 것은 높아요', 'Longer bars sound lower, shorter bars sound higher.', '긴 막대는 낮은 소리, 짧은 막대는 높은 소리예요.', <SprBigPad/>)],
    ['sr-family', 'The instrument families', '악기 가족', 'Each family has small, high members and big, low ones.', '악기 가족마다 작고 높은 악기와 크고 낮은 악기가 있어요.', ksL('The instrument families', '악기 가족', 'Each family has small, high members and big, low ones.', '악기 가족마다 작고 높은 악기와 크고 낮은 악기가 있어요.', <SprFamilyPad/>)],
    ['sr-ladder', 'Low to high', '낮은 것에서 높은 것까지', 'The violin family and the voices, from low to high.', '바이올린 가족과 목소리를 낮은 것에서 높은 것까지.', ksL('Low to high', '낮은 것에서 높은 것까지', 'The violin family and the voices, from low to high.', '바이올린 가족과 목소리를 낮은 것에서 높은 것까지 놓아 봐요.', <SprLadderPad/>)],
    ['sr-range', 'The piano’s range', '피아노의 음역', 'How far a piano reaches, low to high.', '피아노가 낮은 쪽에서 높은 쪽까지 닿는 범위.', ksL('The piano’s range', '피아노의 음역', 'How far a piano reaches, from the lowest key to the highest.', '피아노가 가장 낮은 건반에서 가장 높은 건반까지 닿는 범위.', <SprRangePad/>)],
  ]],
];
KS_ROWS.forEach(([concept, rows]) => rows.forEach(([id, en, ko, benEn, bko, Comp]) => {
  TOOLS.push({ id, ch: 'concept', title: en, blurb: benEn, hidden: true, get kicker() { return TOOL_AREAS.find(a => a.id === 'pitch').name + ' · ' + homeCatById(concept).name; }, C: Comp });
  TOOL_KO[id] = [ko, bko];
  const tl = TOOLS[TOOLS.length - 1], k = TOOL_KO[id], ti = tl.title, bl = tl.blurb; tl.titleEn = ti; tl.blurbEn = bl;
  Object.defineProperty(tl, 'title', { get: () => (LANG === 'ko' ? k[0] : ti), enumerable: true, configurable: true });
  Object.defineProperty(tl, 'blurb', { get: () => (LANG === 'ko' ? k[1] : bl), enumerable: true, configurable: true });
  TOOL_CONCEPT[id] = concept;
}));
"""
rep("\nconst scDirTag = (dn) =>", blk + reg + "\nconst scDirTag = (dn) =>")
open(bb, 'w', encoding='utf-8').write(s)
