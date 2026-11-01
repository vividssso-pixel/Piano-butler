p='drills.src.html'; s=open(p).read()
if 'function RefRhythm' in s: print('already'); raise SystemExit
comp=r'''// m24: the other two shelves filled (Rhythm, Ornaments; Form, Texture, Kinds of pieces, Composers)
const refRow2 = (en, ko, den, dko, room) => [<span>{refB(t(en, ko))} · {t(den, dko)}</span>, <RefDoor room={room}/>];
const refRow3 = (en, ko, den, dko, ex, room) => [<span>{refB(t(en, ko))} · {t(den, dko)}</span>, <span style={{fontFamily:LB_SERIF,fontWeight:700,fontSize:12.5}}>{ex}</span>, <RefDoor room={room}/>];
function RefRhythm() {
  return <div>
    <RefTable k="rhythm" cols="minmax(0,1fr) auto" head={[t('Rhythm', '리듬'), '']} rows={[
      refRow2('dot', '점', 'adds half the note’s value; a double dot adds half and then a quarter', '음표 길이의 절반을 더해요; 겹점은 절반과 그 절반을 더', 'rhythm'),
      refRow2('tie', '붙임줄', 'joins two notes of the same pitch into one sound', '같은 높이의 두 음을 한 소리로 이어요', 'rhythm'),
      refRow2('anacrusis', '못갖춘마디', 'notes before the first full bar; the last bar is short by the same amount', '첫 온마디 앞의 음; 마지막 마디가 그만큼 짧아요', 'rhythm-4'),
      refRow2('triplet', '셋잇단음표', 'three notes in the time of two', '두 음의 시간에 세 음', 'rhythm-2'),
      refRow2('duplet', '둘잇단음표', 'two notes in the time of three, in compound time', '세 음의 시간에 두 음, 겹박자에서', 'rhythm-2'),
      refRow2('syncopation', '당김음', 'the stress falls off the beat', '강세가 박 밖에 와요', 'rhythm-4'),
      refRow2('hemiola', '헤미올라', 'two bars of three felt as three bars of two', '3박 두 마디를 2박 세 마디처럼 느껴요', 'rhythm-4'),
      refRow2('grouping', '음표 묶기', 'beams show the beats: in 4/4 never across the middle of the bar; in 6/8 in threes', '빔이 박을 보여 줘요: 4/4에서는 마디 가운데를 넘지 않고, 6/8에서는 셋씩', 'rhythm-4'),
      refRow2('swing', '스윙', 'pairs of quavers played long–short, like a triplet', '8분음표 둘을 길게–짧게, 셋잇단처럼', 'styles'),
      refRow2('polyrhythm', '폴리리듬', 'two rhythms at once: three against two', '두 리듬이 동시에: 3 대 2', 'scales-7'),
      refRow2('rubato', '루바토', 'time given and taken back, for expression', '표현을 위해 시간을 주고 다시 돌려받아요', null),
    ]}/>
  </div>;
}
function RefOrnaments() {
  return <div>
    <RefTable k="ornaments" cols="minmax(0,1fr) 88px auto" head={[t('Ornament', '꾸밈음'), t('On C', 'C에서'), '']} rows={[
      refRow3('trill', '트릴', 'the note and the one above, fast; in Baroque music it starts on the upper note', '그 음과 위의 음을 빠르게; 바로크 음악에서는 위의 음부터', 'D C D C…', null),
      refRow3('upper mordent', '윗 모르덴트', 'the note, the one above, the note, quickly on the beat', '음, 위의 음, 음을 박 위에서 빠르게', 'C D C', null),
      refRow3('lower mordent', '아랫 모르덴트', 'the note, the one below, the note', '음, 아래 음, 음', 'C B C', null),
      refRow3('turn', '턴', 'above, the note, below, the note', '위, 음, 아래, 음', 'D C B C', null),
      refRow3('inverted turn', '역턴', 'below first: below, the note, above, the note', '아래부터: 아래, 음, 위, 음', 'B C D C', null),
      refRow3('appoggiatura', '앞꾸밈음', 'a small note that leans on the beat and takes half the main note (two-thirds of a dotted note)', '박 위에 기대는 작은 음, 큰 음 길이의 절반을 가져가요 (점음표면 3분의 2)', 'D–C', null),
      refRow3('acciaccatura', '짧은 앞꾸밈음', 'a small note with a slash: crushed in as quickly as possible', '빗금 그은 작은 음: 가능한 한 빨리 짓눌러 넣어요', 'ᵈC', null),
      refRow3('slide', '슬라이드', 'two small notes stepping up into the main note', '두 작은 음이 걸어 올라와 큰 음으로', 'A B C', null),
      refRow3('spread chord', '펼침화음', 'a wavy line: the notes one after another from the bottom', '물결선: 아래부터 한 음씩', 'C E G ↗', null),
      refRow3('tremolo', '트레몰로', 'slashes on the stem: two notes alternated, or one repeated, very fast', '기둥의 빗금: 두 음을 번갈아, 또는 한 음을 아주 빠르게', 'C E C E…', null),
    ]}/>
    <RefNote>{t('Play an ornament in the style of its period; an edition’s footnote often writes it out.', '꾸밈음은 그 시대의 방식으로; 악보 각주에 풀어 써 있을 때가 많아요.')}</RefNote>
  </div>;
}
function RefForm() {
  return <div>
    <RefTable k="form" cols="minmax(0,1fr) 70px auto" head={[t('Form', '형식'), t('Plan', '짜임'), '']} rows={[
      refRow3('binary', '2부 형식', 'two halves, often each repeated; the first moves to a new key, the second comes home', '두 부분, 흔히 각각 반복; 앞부분은 새 조로, 뒷부분은 집으로', 'A B', 'form'),
      refRow3('ternary', '3부 형식', 'a contrasting middle, then the first part again', '대조되는 가운데, 그리고 처음 부분이 다시', 'A B A', 'form'),
      refRow3('rondo', '론도', 'a refrain that keeps coming back between episodes', '삽입부 사이마다 돌아오는 후렴', 'A B A C A', 'form'),
      refRow3('minuet and trio', '미뉴에트와 트리오', 'two dances, the minuet played again after the trio', '두 춤곡, 트리오 뒤에 미뉴에트를 다시', 'M T M', 'pieces-78'),
      refRow3('theme and variations', '주제와 변주', 'a theme, then new versions of it', '주제, 그리고 그 새 모습들', 'A A¹ A²…', 'pieces-78'),
      refRow3('sonata form', '소나타 형식', 'exposition (two subjects, two keys), development, recapitulation (both in the home key)', '제시부 (두 주제, 두 조), 발전부, 재현부 (둘 다 으뜸조)', 'E D R', 'pieces-78'),
      refRow3('fugue', '푸가', 'a subject taken up by each voice in turn, with episodes between', '주제를 성부마다 차례로, 사이에 삽입부', 'S A S…', 'pieces-78'),
      refRow3('strophic', '유절 형식', 'the same music for every verse', '모든 절에 같은 음악', 'A A A', null),
      refRow3('through-composed', '통작 형식', 'new music all the way through', '끝까지 새 음악', 'A B C D', null),
    ]}/>
  </div>;
}
function RefTexture() {
  return <div>
    <RefTable k="texture" cols="minmax(0,1fr) auto" head={[t('Texture', '짜임새'), '']} rows={[
      refRow2('monophonic', '단선율', 'one line alone', '한 선율만', 'styles'),
      refRow2('homophonic', '화성적', 'a melody with chords', '선율과 화음', 'styles'),
      refRow2('chordal', '화음적 (찬송가풍)', 'every part moves together, like a hymn', '모든 성부가 함께 움직여요, 찬송가처럼', 'styles'),
      refRow2('melody and accompaniment', '선율과 반주', 'the tune on top, a pattern underneath (Alberti bass: low, high, middle, high)', '위에 선율, 아래에 반주형 (알베르티 베이스: 낮게, 높게, 가운데, 높게)', 'arps-7'),
      refRow2('polyphonic (counterpoint)', '다성적 (대위법)', 'two or more lines, each a tune of its own', '두 개 이상의 선율, 각자 자기 노래', 'styles'),
      refRow2('imitation, canon', '모방, 캐논', 'one voice copies another a little later', '한 성부가 조금 뒤에 다른 성부를 따라 해요', null),
      refRow2('heterophonic', '헤테로포니', 'versions of one tune at the same time', '한 선율의 여러 모습이 동시에', null),
    ]}/>
  </div>;
}
function RefKinds() {
  const r = (en, ko, den, dko, room) => refRow2(en, ko, den, dko, room);
  return <div>
    <RefTable k="kinds" cols="minmax(0,1fr) auto" head={[t('Kind of piece', '곡의 종류'), '']} rows={[
      r('sonata', '소나타', 'a work in several movements for one or two players', '한두 연주자를 위한 여러 악장의 작품', 'pieces-78'), r('sonatina', '소나티네', 'a small, light sonata', '작고 가벼운 소나타', 'pieces-78'),
      r('suite', '모음곡', 'a set of dances: allemande, courante, sarabande, gigue, with minuets, gavottes, bourrées', '춤곡 모음: 알르망드, 쿠랑트, 사라방드, 지그, 그리고 미뉴에트, 가보트, 부레', 'pieces-78'),
      r('invention', '인벤션', 'a short piece in two-part counterpoint', '2성 대위법의 짧은 곡', null), r('prelude', '전주곡', 'an opening piece, or a short free one', '여는 곡, 또는 짧고 자유로운 곡', null),
      r('toccata', '토카타', 'a brilliant piece for the fingers', '손가락을 위한 화려한 곡', null), r('étude', '연습곡', 'a study of one technique', '한 가지 테크닉을 위한 곡', null),
      r('nocturne', '녹턴', 'a night piece: a singing tune over broken chords', '밤의 곡: 분산화음 위의 노래하는 선율', null), r('waltz', '왈츠', 'a dance in 3/4, felt one in a bar', '3/4 춤곡, 한 마디를 하나로', null),
      r('mazurka, polonaise', '마주르카, 폴로네즈', 'Polish dances in 3/4', '3/4 폴란드 춤곡', null), r('scherzo', '스케르초', 'a quick, playful movement', '빠르고 장난스러운 곡', null),
      r('impromptu', '즉흥곡', 'as if made up on the spot', '그 자리에서 지은 듯이', null), r('song without words', '무언가', 'a song for the piano alone', '피아노만을 위한 노래', null),
      r('fantasia, rhapsody', '환상곡, 랩소디', 'free in form', '형식이 자유로워요', null), r('concerto', '협주곡', 'a soloist with an orchestra', '독주자와 오케스트라', null),
    ]}/>
  </div>;
}
const REF_COMPOSERS = [
  ['Baroque', '바로크', [['Purcell', '퍼셀', '1659–1695'], ['Couperin', '쿠프랭', '1668–1733'], ['J. S. Bach', '바흐', '1685–1750'], ['Handel', '헨델', '1685–1759'], ['D. Scarlatti', '스카를라티', '1685–1757']]],
  ['Classical', '고전', [['Haydn', '하이든', '1732–1809'], ['Clementi', '클레멘티', '1752–1832'], ['Mozart', '모차르트', '1756–1791'], ['Beethoven', '베토벤', '1770–1827']]],
  ['Romantic', '낭만', [['Schubert', '슈베르트', '1797–1828'], ['Mendelssohn', '멘델스존', '1809–1847'], ['Chopin', '쇼팽', '1810–1849'], ['Schumann', '슈만', '1810–1856'], ['Liszt', '리스트', '1811–1886'], ['Brahms', '브람스', '1833–1897'], ['Tchaikovsky', '차이콥스키', '1840–1893'], ['Grieg', '그리그', '1843–1907']]],
  ['Modern', '근대', [['Debussy', '드뷔시', '1862–1918'], ['Rachmaninoff', '라흐마니노프', '1873–1943'], ['Ravel', '라벨', '1875–1937'], ['Bartók', '바르톡', '1881–1945'], ['Prokofiev', '프로코피예프', '1891–1953'], ['Shostakovich', '쇼스타코비치', '1906–1975']]],
  ['Contemporary', '현대', [['Messiaen', '메시앙', '1908–1992'], ['Sculthorpe', '스컬소프', '1929–2014'], ['Pärt', '패르트', 'b. 1935'], ['Glass', '글래스', 'b. 1937'], ['Kats-Chernin', '카츠-체르닌', 'b. 1957']]],
];
function RefComposers() {
  return <div>
    <RefTable k="composers" cols="96px minmax(0,1fr) auto" head={[t('Period', '시대'), t('Composers', '작곡가'), '']}
      rows={REF_COMPOSERS.map(([en, ko, list]) => [refB(t(en, ko)), <span>{list.map(([n, nk, y], i) => <span key={n} style={{whiteSpace:'nowrap'}}>{i ? ' · ' : ''}{t(n, nk)} <span style={{color:BK.muted,fontSize:11.5}}>{y}</span></span>)}</span>, <RefDoor room="composers"/>])}/>
    <RefNote>{t('A few of the composers pianists meet most, in order of birth. The Periods book has the dates and the sound of each period.', '피아니스트가 가장 자주 만나는 작곡가 몇 명, 태어난 순서로. 시대마다의 연도와 소리는 Periods 책에.')}</RefNote>
  </div>;
}
'''
anchor="const SHELF_TOOLS = {"
assert s.count(anchor)==1
s=s.replace(anchor, comp+anchor)
old="refSec('periods', 'Periods', '시대'),"
assert s.count(old)==1
s=s.replace(old,"refSec('rhythm', 'Rhythm', '리듬'), refSec('ornaments', 'Ornaments', '꾸밈음'), refSec('form', 'Form', '형식'), refSec('texture', 'Texture', '짜임새'), refSec('kinds', 'Kinds of pieces', '곡의 종류'), refSec('periods', 'Periods', '시대'), refSec('composers', 'Composers', '작곡가'),")
old="transposition: RefTranspose, signs:"
assert s.count(old)==1
s=s.replace(old,"transposition: RefTranspose, rhythm: RefRhythm, ornaments: RefOrnaments, form: RefForm, texture: RefTexture, kinds: RefKinds, composers: RefComposers, signs:")
old="['Reading music', '악보 읽기', [['staff', 'Staff and clefs', '오선과 음자리표'], ['notes', 'Notes and rests', '음표와 쉼표'], ['time', 'Time signatures', '박자표'], ['signs', 'Signs', '기호']]],"
assert s.count(old)==1
s=s.replace(old,"['Reading music', '악보 읽기', [['staff', 'Staff and clefs', '오선과 음자리표'], ['notes', 'Notes and rests', '음표와 쉼표'], ['rhythm', 'Rhythm', '리듬'], ['time', 'Time signatures', '박자표'], ['signs', 'Signs', '기호'], ['ornaments', 'Ornaments', '꾸밈음']]],")
old="['Words and history', '용어와 역사', [['play', 'How to play', '연주 용어'], ['terms', 'Music words', '음악 낱말'], ['periods', 'Periods', '시대'], ['instruments', 'Instruments', '악기']]],"
assert s.count(old)==1
s=s.replace(old,"['Words and history', '용어와 역사', [['play', 'How to play', '연주 용어'], ['terms', 'Music words', '음악 낱말'], ['form', 'Form', '형식'], ['texture', 'Texture', '짜임새'], ['kinds', 'Kinds of pieces', '곡의 종류'], ['periods', 'Periods', '시대'], ['composers', 'Composers', '작곡가'], ['instruments', 'Instruments', '악기']]],")
open(p,'w').write(s); print('ok')
