p='drills.src.html'; s=open(p).read()
if 'function RefRelated' in s: print('already'); raise SystemExit
comp=r'''// m23 (her 1 Nov: 'fill each shelf with whatever theory there is'): five more books on the Pitch and harmony shelf
const refB = (x) => <b style={{fontWeight:800}}>{x}</b>, refR = (x) => <b style={{fontFamily:LB_SERIF,fontWeight:900,whiteSpace:'nowrap'}}>{x}</b>;
function RefRelated() {
  return <div>
    <RefTable k="related" cols="minmax(0,1fr) 78px 78px auto" head={[t('Related key', '관계조'), t('C major', 'C장조'), t('A minor', 'a단조'), '']} rows={[
      [<span>{refB(t('relative', '나란한조'))} · {t('the same key signature', '조표가 같아요')}</span>, refR('A minor'), refR('C major'), <RefDoor room="minor-scales"/>],
      [<span>{refB(t('tonic major / minor', '같은으뜸음조'))} · {t('the same key note', '으뜸음이 같아요')}</span>, refR('C minor'), refR('A major'), <RefDoor room={null}/>],
      [<span>{refB(t('dominant', '딸림조'))} · {t('a 5th up: one sharp more, or one flat less', '5도 위: 샵 하나 더, 또는 플랫 하나 덜')}</span>, refR('G major'), refR('E minor'), <RefDoor room="keys-4"/>],
      [<span>{refB(t('subdominant', '버금딸림조'))} · {t('a 5th down: one flat more, or one sharp less', '5도 아래: 플랫 하나 더, 또는 샵 하나 덜')}</span>, refR('F major'), refR('D minor'), <RefDoor room="keys-4"/>],
      [<span>{refB(t('relative of the dominant', '딸림조의 나란한조'))}</span>, refR('E minor'), refR('G major'), <RefDoor room={null}/>],
      [<span>{refB(t('relative of the subdominant', '버금딸림조의 나란한조'))}</span>, refR('D minor'), refR('F major'), <RefDoor room={null}/>],
    ]}/>
    <RefNote>{t('The five closest keys to any key: its relative, dominant, subdominant and their relatives. They share all but one note with it.', '어느 조든 가장 가까운 다섯 조: 나란한조, 딸림조, 버금딸림조와 그 나란한조들. 음이 하나만 달라요.')}</RefNote>
    <RefLab>{t('Modulation: moving to a new key', '전조: 새 조로 옮겨 가기')}</RefLab>
    <RefTable k="modulation" cols="minmax(0,1fr) auto" rows={[
      [t('Look for a new accidental that keeps coming back: F♯ in C major points to G major; B♭ points to F major.', '계속 나오는 새 임시표를 찾아요: C장조에서 F♯이면 G장조, B♭이면 F장조.'), <RefDoor room="keys-4"/>],
      [t('Then a cadence in the new key (its V – I) confirms it.', '새 조의 종지(V – I)가 나오면 확실해요.'), <RefDoor room="keys-4"/>],
      [t('Most often: a major key goes to its dominant; a minor key to its relative major.', '가장 흔한 길: 장조는 딸림조로, 단조는 나란한 장조로.'), <RefDoor room="keys-5"/>],
    ]}/>
  </div>;
}
const REF_MODES = [   // white keys from each note; the steps; how it sounds
  ['Ionian', '이오니안', 'C', 'T T S T T T S', 'the major scale', '장음계'],
  ['Dorian', '도리안', 'D', 'T S T T T S T', 'minor, with a raised 6th', '단조, 6음이 올라감'],
  ['Phrygian', '프리지안', 'E', 'S T T T S T T', 'minor, with a flat 2nd', '단조, 2음이 내려감'],
  ['Lydian', '리디안', 'F', 'T T T S T T S', 'major, with a raised 4th', '장조, 4음이 올라감'],
  ['Mixolydian', '믹솔리디안', 'G', 'T T S T T S T', 'major, with a flat 7th', '장조, 7음이 내려감'],
  ['Aeolian', '에올리안', 'A', 'T S T T S T T', 'the natural minor', '자연단음계'],
  ['Locrian', '로크리안', 'B', 'S T T S T T T', 'a diminished 5th above the key note', '으뜸음 위 감5도'],
];
function RefModes() {
  return <div>
    <RefTable k="modes" cols="minmax(0,1fr) 34px minmax(0,1.1fr) auto" head={[t('Mode', '선법'), t('From', '시작'), t('Steps (T tone, S semitone)', '걸음 (T 온음, S 반음)'), '']}
      rows={REF_MODES.map(([en, ko, n, st, sen, sko]) => [<span>{refB(t(en, ko))}<br/><span style={{color:BK.muted,fontSize:12.5}}>{t(sen, sko)}</span></span>, refR(n), <span style={{fontFamily:LB_SERIF,fontWeight:700,letterSpacing:'0.04em',whiteSpace:'nowrap'}}>{st}</span>, <RefDoor room={null}/>])}/>
    <RefNote>{t('Each mode is the white keys from one note. On another key note keep the steps: D Dorian has no sharps or flats, G Dorian has one flat. From the brightest to the darkest: Lydian, Ionian, Mixolydian, Dorian, Aeolian, Phrygian, Locrian.', '선법마다 한 음에서 시작하는 흰건반. 다른 으뜸음에서는 걸음을 그대로: D 도리안은 조표 없음, G 도리안은 플랫 하나. 가장 밝은 것부터 어두운 것까지: 리디안, 이오니안, 믹솔리디안, 도리안, 에올리안, 프리지안, 로크리안.')}</RefNote>
  </div>;
}
function RefNonChord() {
  const row = (en, ko, den, dko, ex, room) => [<span>{refB(t(en, ko))} · {t(den, dko)}</span>, <span style={{fontFamily:LB_SERIF,fontWeight:700,whiteSpace:'nowrap',fontSize:12.5}}>{ex}</span>, <RefDoor room={room}/>];
  return <div>
    <RefTable k="nonchord" cols="minmax(0,1fr) 82px auto" head={[t('Note', '음'), t('Over C–E–G', 'C–E–G 위에서'), '']} rows={[
      row('passing note', '경과음', 'steps between two chord notes, in one direction', '두 화음음 사이를 한 방향으로 걸어가요', 'C D E', 'harmony-5'),
      row('auxiliary note', '보조음', 'steps away and back to the same chord note', '옆으로 갔다가 같은 화음음으로 돌아와요', 'E F E', 'harmony-5'),
      row('accented passing note', '강박 경과음', 'a passing note on the beat', '박 위에 오는 경과음', 'D C', 'harmony-6'),
      row('suspension', '계류음', 'held over from the chord before, then falls by step: prepare, hold, resolve (4-3, 7-6, 9-8)', '앞 화음에서 이어 잡고 있다가 한 걸음 내려가요: 준비, 계류, 해결 (4-3, 7-6, 9-8)', 'F → E', 'harmony-6'),
      row('appoggiatura', '앞꾸밈음 (비화성)', 'leaps to a clash on the beat, then steps to the chord note', '박 위의 불협화음으로 뛰었다가 화음음으로 걸어가요', 'A → G', null),
      row('échappée', '이탈음', 'steps away, then leaps the other way to the chord note', '한 걸음 벗어났다가 반대쪽으로 뛰어 화음음으로', 'E F D', null),
      row('anticipation', '선행음', 'a note of the next chord arrives early', '다음 화음의 음이 먼저 나와요', 'B C | C', null),
      row('changing notes', '변화음', 'one step above and one below, then the chord note', '위로 한 걸음, 아래로 한 걸음, 그리고 화음음', 'D B C', null),
      row('pedal point', '지속음 (페달 포인트)', 'one note held, often the tonic or dominant in the bass, while the chords change above', '한 음을 계속 잡아요, 흔히 베이스의 으뜸음이나 딸림음, 위의 화음은 바뀌어요', 'G . . .', null),
    ]}/>
  </div>;
}
function RefChromatic() {
  const row = (en, ko, den, dko, ex, room) => [<span>{refB(t(en, ko))} · {t(den, dko)}</span>, <span style={{fontFamily:LB_SERIF,fontWeight:700,fontSize:12.5}}>{ex}</span>, <RefDoor room={room}/>];
  return <div>
    <RefTable k="chromatic" cols="minmax(0,1fr) 96px auto" head={[t('Chord', '화음'), t('In C', 'C에서'), '']} rows={[
      row('secondary dominant', '부속화음', 'the dominant of another degree, borrowed for a moment: V of V leads to V', '다른 음의 딸림화음을 잠깐 빌려와요: V의 V는 V로 가요', 'V/V: D F♯ A → G', null),
      row('diminished 7th', '감7화음', 'on the leading note, three minor 3rds stacked; it leads home', '이끎음 위에 단3도 셋을 쌓아요; 으뜸으로 이끌어요', 'B D F A♭ → C', 'arps-6'),
      row('Neapolitan 6th', '나폴리 6화음', 'a major chord on the flat 2nd, in first inversion; it leads to V', '내려간 2음 위의 장3화음, 첫째 자리바꿈; V로 가요', 'F A♭ D♭ → V', null),
      row('Italian 6th', '이탈리아 6화음', 'A♭ and F♯, an augmented 6th, open out to the octave G', 'A♭과 F♯, 증6도가 바깥으로 벌어져 G 옥타브로', 'A♭ C F♯ → G', null),
      row('French 6th', '프랑스 6화음', 'the Italian, with the 2nd added', '이탈리아 6화음에 2음을 더해요', 'A♭ C D F♯', null),
      row('German 6th', '독일 6화음', 'the Italian, with the minor 3rd added', '이탈리아 6화음에 단3음을 더해요', 'A♭ C E♭ F♯', null),
      row('borrowed chord', '차용화음', 'a chord from the tonic minor, used in a major key', '같은으뜸음 단조의 화음을 장조에서 써요', 'iv: F A♭ C', null),
    ]}/>
    <RefNote>{t('Chromatic: a note from outside the key, here to lean into the next chord.', '반음계적: 조 밖의 음, 다음 화음으로 기울기 위해 와요.')}</RefNote>
  </div>;
}
function RefTranspose() {
  return <div>
    <RefTable k="transpose" cols="minmax(0,1fr) auto" head={[t('Transposing a tune', '선율 옮기기'), '']} rows={[
      [t('1. Choose the new key and write its key signature.', '1. 새 조를 정하고 그 조표를 써요.'), <RefDoor room={null}/>],
      [t('2. Move every note by the same interval (up a major 2nd: C → D, E → F♯).', '2. 모든 음을 같은 음정만큼 옮겨요 (장2도 위: C → D, E → F♯).'), <RefDoor room={null}/>],
      [t('3. An accidental moves with its note: a raised note stays raised in the new key.', '3. 임시표도 함께 옮겨요: 올린 음은 새 조에서도 올린 음.'), <RefDoor room={null}/>],
      [t('Up or down an octave: the same letters, a new clef or ledger lines.', '옥타브 위나 아래: 같은 글자, 새 음자리표나 덧줄.'), <RefDoor room="ledger-lines"/>],
    ]}/>
    <RefLab>{t('Transposing instruments: written ≠ heard', '이조악기: 쓴 음 ≠ 들리는 음')}</RefLab>
    <RefTable k="transpose-inst" cols="minmax(0,1fr) minmax(0,1fr)" head={[t('Instrument', '악기'), t('Sounds', '소리')]} rows={[
      [refB(t('clarinet, trumpet in B♭', 'B♭ 클라리넷, 트럼펫')), t('a major 2nd lower than written', '쓴 음보다 장2도 아래')],
      [refB(t('clarinet in A', 'A 클라리넷')), t('a minor 3rd lower', '단3도 아래')],
      [refB(t('horn in F', 'F 호른')), t('a perfect 5th lower', '완전5도 아래')],
      [refB(t('alto saxophone in E♭', 'E♭ 알토 색소폰')), t('a major 6th lower', '장6도 아래')],
      [refB(t('piccolo', '피콜로')), t('an octave higher', '옥타브 위')],
      [refB(t('double bass, guitar', '더블베이스, 기타')), t('an octave lower', '옥타브 아래')],
    ]}/>
  </div>;
}
'''
a="function RefShelf({ onChapter, onHouse, onTool }) {"
# insert before SHELF_TOOLS line
anchor="const SHELF_TOOLS = {"
assert s.count(anchor)==1
s=s.replace(anchor, comp+anchor)
old="refSec('chords', 'Chords', '화음'), refSec('cadences', 'Cadences', '종지'),"
assert s.count(old)==1
s=s.replace(old,"refSec('related', 'Related keys', '관계조'), refSec('modes', 'Modes', '선법'), refSec('chords', 'Chords', '화음'), refSec('cadences', 'Cadences', '종지'), refSec('nonchord', 'Non-chord notes', '비화성음'), refSec('chromatic', 'Chromatic chords', '반음계적 화음'), refSec('transposition', 'Transposition', '이조'),")
old="chords: RefChords, cadences: RefCadences, signs:"
assert s.count(old)==1
s=s.replace(old,"chords: RefChords, cadences: RefCadences, related: RefRelated, modes: RefModes, nonchord: RefNonChord, chromatic: RefChromatic, transposition: RefTranspose, signs:")
old="['Pitch and harmony', '음높이와 화성', [['keys', 'Keys', '조성'], ['scales', 'Scales', '음계'], ['intervals', 'Intervals', '음정'], ['chords', 'Chords', '화음'], ['cadences', 'Cadences', '종지']]],"
assert s.count(old)==1
s=s.replace(old,"['Pitch and harmony', '음높이와 화성', [['keys', 'Keys', '조성'], ['related', 'Related keys', '관계조'], ['scales', 'Scales', '음계'], ['modes', 'Modes', '선법'], ['intervals', 'Intervals', '음정'], ['chords', 'Chords', '화음'], ['cadences', 'Cadences', '종지'], ['nonchord', 'Non-chord notes', '비화성음'], ['chromatic', 'Chromatic chords', '반음계적 화음'], ['transposition', 'Transposition', '이조']]],")
# spine count from data
old="const spW = Math.floor((bw - 2 * 10 - 6 * 5 - 10 * 4) / 13),"
assert s.count(old)==1
s=s.replace(old,"const NB = REF_SHELVES.reduce((a, x) => a + x[2].length, 0), spW = Math.floor((bw - 2 * 10 - 6 * 5 - (NB - 3) * 4) / NB),")
s=s.replace("REF_SPINE_H[k++ % 13]","REF_SPINE_H[k++ % REF_SPINE_H.length]")
open(p,'w').write(s); print('ok')
