p='drills.src.html'; s=open(p).read()
if 'function RefMelody' in s: print('already'); raise SystemExit
def rep(old, new, cnt=1):
    global s
    assert s.count(old)==cnt, (s.count(old), old[:80])
    s=s.replace(old,new)

# ---- new books: Melody, Technique, Aural; ranges and pitch for Instruments
comp=r'''// m28 (her 'apply all of it'): Melody, Technique, Aural; figured bass; the Signs filled in; range and frequency
function RefMelody() {
  return <div>
    <RefTable k="melody" cols="minmax(0,1fr) auto" head={[t('Melody', '선율'), '']} rows={[
      refRow2('phrase', '프레이즈', 'a musical sentence, often two or four bars, ending at a cadence', '음악의 한 문장, 흔히 두 마디나 네 마디, 종지에서 끝나요', 'melody'),
      refRow2('question and answer', '질문과 대답', 'the first phrase stops on an open note (often V), the answer comes home (I)', '앞 프레이즈는 열린 음(흔히 V)에서 멈추고, 대답은 집(I)으로 와요', 'melody'),
      refRow2('motif', '동기', 'a short idea of a few notes that the tune is built from', '선율을 짓는 몇 음의 짧은 생각', 'melody'),
      refRow2('repetition', '반복', 'the same idea again, so the ear can follow', '같은 생각을 다시, 귀가 따라올 수 있게', 'melody'),
      refRow2('sequence', '모진행', 'the idea repeated a step higher or lower', '그 생각을 한 음 위나 아래에서 되풀이', 'melody'),
      refRow2('contour, high point', '윤곽, 정점', 'the shape of the line, rising to one high point', '선의 모양, 정점 하나를 향해 올라가요', 'melody'),
      refRow2('step and leap', '차례가기와 뛰기', 'mostly steps; after a leap, step back the other way', '대부분 차례가기; 뛴 다음에는 반대쪽으로 한 걸음', 'melody-3'),
      refRow2('writing a tune', '선율 짓기', 'start and end on the tonic chord’s notes, outline the chords, a cadence at the end', '으뜸화음의 음에서 시작하고 끝내기, 화음을 따라 그리기, 끝에 종지', 'melody-3'),
      refRow2('setting words', '가사 붙이기', 'strong syllables on strong beats; one phrase for each line', '강한 음절은 강박에; 한 줄에 한 프레이즈', 'melody-4'),
      refRow2('a longer verse', '긴 가사', 'phrases that go away and come home, with phrase marks and rests', '멀어졌다가 돌아오는 프레이즈, 프레이즈 표시와 쉼표', 'melody-5'),
    ]}/>
  </div>;
}
function RefTechnique() {
  return <div>
    <RefTable k="technique" cols="minmax(0,1fr) auto" head={[t('Technique', '테크닉'), '']} rows={[
      refRow2('finger numbers', '손가락 번호', 'thumb 1 to little finger 5, the same in both hands', '엄지 1부터 새끼손가락 5까지, 두 손 모두 같아요', 'posture-hands'),
      refRow2('posture', '자세', 'sit tall on the front half of the stool, forearms level with the keys', '의자 앞쪽 절반에 바르게, 팔뚝은 건반과 수평', 'posture-hands'),
      refRow2('hand shape', '손 모양', 'round, as if holding a ball; play on the fingertips', '공을 쥔 듯 둥글게; 손끝으로', 'posture-hands'),
      refRow2('hand position', '손 자리', 'five fingers over five keys, ready to play without looking', '다섯 손가락을 다섯 건반 위에, 보지 않고 칠 수 있게', 'hand-positions'),
      refRow2('legato touch', '레가토 터치', 'the next key goes down as the last one comes up: no gap', '다음 건반이 내려갈 때 앞 건반이 올라와요: 틈 없이', 'scale-play'),
      refRow2('staccato touch', '스타카토 터치', 'a quick bounce off the key, from a loose wrist', '느슨한 손목으로 건반에서 빠르게 튀어 올라요', null),
      refRow2('thumb under, finger over', '엄지 넘기기, 손가락 넘기기', 'how a scale keeps going past five notes', '다섯 음을 넘어 스케일이 이어지는 방법', 'scale-play'),
      refRow2('arm weight', '팔 무게', 'a full tone comes from the arm’s weight, not from hitting with the finger', '풍부한 소리는 손가락으로 치는 게 아니라 팔의 무게에서', null),
      refRow2('balance (voicing)', '균형 (보이싱)', 'the tune louder than the accompaniment', '선율을 반주보다 크게', null),
      refRow2('legato pedalling', '레가토 페달', 'pedal down just after the chord, up and down again at the next', '화음 바로 뒤에 밟고, 다음 화음에서 떼었다 다시', 'dynamics'),
      refRow2('finger substitution', '손가락 바꾸기', 'change fingers on a held key to keep the line joined', '누른 건반 위에서 손가락을 바꿔 선을 잇기', null),
    ]}/>
  </div>;
}
function RefAural() {
  return <div>
    <RefTable k="aural" cols="minmax(0,1fr) auto" head={[t('What the ear learns, step by step', '귀가 차례로 배우는 것'), '']} rows={[
      refRow2('beat and time', '박과 박자', 'clap the beat; is it in two or in three?', '박을 손뼉으로; 2박일까 3박일까?', 'listen-sing'),
      refRow2('high or low, step or leap', '높고 낮게, 차례가기와 뛰기', 'which note is higher; does the tune step or jump?', '어느 음이 높은지; 선율이 걷는지 뛰는지?', 'ear-prep'),
      refRow2('sing it back', '따라 부르기', 'hear a short phrase and sing it back', '짧은 프레이즈를 듣고 따라 불러요', 'listen-sing'),
      refRow2('clap it back', '따라 치기', 'hear a rhythm and clap it back', '리듬을 듣고 손뼉으로 따라 쳐요', 'listen-write'),
      refRow2('the home note', '으뜸음', 'does the tune end at home or sound unfinished?', '선율이 집에서 끝나는지, 덜 끝난 듯한지?', 'listen-write'),
      refRow2('two notes together', '동시에 두 음', 'which is higher; then name the interval', '어느 것이 높은지; 그다음 음정 이름', 'listen-23'),
      refRow2('intervals', '음정', 'name the distance between two notes', '두 음 사이의 거리 이름', 'listen-3'),
      refRow2('two parts', '두 성부', 'follow the lower part as well as the tune', '선율과 함께 아래 성부도 따라가요', 'listen-4'),
      refRow2('chords', '화음', 'major, minor or diminished, and which position', '장, 단, 감, 그리고 어느 자리', 'listen-6'),
      refRow2('cadences', '종지', 'perfect, plagal, imperfect or interrupted, by ear', '정격, 변격, 반, 거짓 종지를 귀로', 'listen-7'),
      refRow2('memory', '기억', 'remember a longer phrase and sing or play it', '더 긴 프레이즈를 기억해 부르거나 쳐요', 'listen-8'),
    ]}/>
    <RefNote>{t('In my own order of skills, not any exam board’s list.', '어느 시험 기관의 목록이 아닌, 제 순서대로 정리한 기술들.')}</RefNote>
  </div>;
}
const refHz = (m) => { const f = 440 * Math.pow(2, (m - 69) / 12); return f < 100 ? f.toFixed(1) : Math.round(f).toLocaleString('en-AU'); };
const refNoteName = (n) => n.replace('b', '♭').replace('#', '♯');
function RefRanges() {
  const groups = RANGES.filter(g => !g.hist);
  return <div>
    <RefLab>{t('Range and pitch: from the lowest note to the highest, in hertz', '음역과 음높이: 가장 낮은 음부터 가장 높은 음까지, 헤르츠로')}</RefLab>
    <RefTable k="ranges" cols="minmax(0,1fr) 78px minmax(0,1fr)" head={[t('Instrument', '악기'), t('Notes', '음'), t('Hz', 'Hz')]}
      rows={groups.flatMap(g => g.rows.map(([n, lo, hi], i) => [<span>{i === 0 ? <span style={{fontSize:10.5,fontWeight:900,color:BK.coral,letterSpacing:'0.04em',display:'block'}}>{rangeName(g.g).toUpperCase()}</span> : null}{refB(rangeName(n))}</span>,
        <span style={{fontFamily:LB_SERIF,fontWeight:700,whiteSpace:'nowrap'}}>{refNoteName(lo)}–{refNoteName(hi)}</span>, <span style={{whiteSpace:'nowrap'}}>{refHz(nm(lo))} – {refHz(nm(hi))}</span>]))}/>
    <RefTable k="hertz" cols="minmax(0,1fr) auto" rows={[
      [t('A sound is a vibration; how many times it vibrates in a second is its frequency, in hertz (Hz). More vibrations, a higher note.', '소리는 떨림; 1초에 몇 번 떨리는지가 주파수, 단위는 헤르츠(Hz). 많이 떨릴수록 높은 음.'), <RefDoor room="pitch-range"/>],
      [t('An octave up doubles it: A3 220 Hz, A4 440 Hz (the tuning note), A5 880 Hz. Middle C is about 262 Hz.', '한 옥타브 위는 두 배: A3 220 Hz, A4 440 Hz (조율 음), A5 880 Hz. 가운데 C는 약 262 Hz.'), <RefDoor room="pitch-range"/>],
      [t('The piano runs from 27.5 Hz (A0) to 4,186 Hz (C8). People hear from about 20 Hz to 20,000 Hz.', '피아노는 27.5 Hz (A0)부터 4,186 Hz (C8)까지. 사람은 약 20 Hz부터 20,000 Hz까지 들어요.'), <RefDoor room="pitch-range"/>],
      [t('Each note also sounds fainter overtones above it; their mix is the instrument’s colour (timbre).', '음마다 위로 여린 배음이 함께 울려요; 그 섞임이 악기의 음색.'), <RefDoor room={null}/>],
    ]}/>
  </div>;
}
'''
rep("const SHELF_TOOLS = {", comp + "const SHELF_TOOLS = {")

# Instruments: add the ranges at the end
i = s.index("function RefInstruments() {")
j = s.index("  return <div data-ref-instruments>", i)
k = s.index("\n  </div>;\n}", j)
s = s[:k] + "\n    <RefRanges/>" + s[k:]

# Chords: figured bass after the positions table (part a)
old = "      [t('Diminished 7th of a key: it starts on the key’s leading note.', '조의 감7화음: 그 조의 이끎음에서 시작.'), <RefDoor room=\"arps-6\"/>],\n    ]}/>\n"
fb = old + r'''    <RefLab>{t('Figured bass: the numbers under the bass', '숫자저음: 베이스 아래의 숫자')}</RefLab>
    <RefTable k="figured" cols="54px minmax(0,1fr) 92px auto" head={[t('Figures', '숫자'), t('Means', '뜻'), t('On G7', 'G7에서'), '']} rows={[
      [refR('5 3'), t('root position (often no figures at all)', '기본 위치 (흔히 숫자 없음)'), refR('G B D'), <RefDoor room="harmony-3"/>],
      [refR('6'), t('first inversion (6 3)', '첫째 자리바꿈 (6 3)'), refR('B D G'), <RefDoor room="harmony-3"/>],
      [refR('6 4'), t('second inversion', '둘째 자리바꿈'), refR('D G B'), <RefDoor room="harmony-5"/>],
      [refR('7'), t('a 7th chord, root position', '7화음, 기본 위치'), refR('G B D F'), <RefDoor room="harmony-6"/>],
      [refR('6 5'), t('7th chord, first inversion', '7화음, 첫째 자리바꿈'), refR('B D F G'), <RefDoor room="harmony-6"/>],
      [refR('4 3'), t('7th chord, second inversion', '7화음, 둘째 자리바꿈'), refR('D F G B'), <RefDoor room="harmony-6"/>],
      [refR('4 2'), t('7th chord, third inversion (or just 2)', '7화음, 셋째 자리바꿈 (또는 2만)'), refR('F G B D'), <RefDoor room="harmony-6"/>],
      [refR('♯ ♭ ♮'), t('alone: raise or lower the 3rd above the bass', '혼자 있으면: 베이스 위 3음을 올리거나 내려요'), refR(''), <RefDoor room={null}/>],
    ]}/>
'''
rep(old, fb)

# Signs: new rows
rep("['arp', 'spread chord: bottom to top', '펼침화음: 아래에서 위로', null], ['gliss', 'glissando: slide across the keys', '글리산도: 건반 위로 미끄러지듯', null]]],",
    "['arp', 'spread chord: bottom to top', '펼침화음: 아래에서 위로', null], ['gliss', 'glissando: slide across the keys', '글리산도: 건반 위로 미끄러지듯', null],\n    ['staccatissimo', 'staccatissimo: very short', '스타카티시모: 아주 짧게', null], ['marcato', 'marcato: strongly marked', '마르카토: 강하게 두드러지게', null], ['mezzostacc', 'mezzo-staccato: a little detached', '메조 스타카토: 조금 떨어지게', null]]],   /* m28 */")
rep("['8vb', '8vb: an octave lower', '8vb: 한 옥타브 낮게', 'signs']]],",
    "['8vb', '8vb: an octave lower', '8vb: 한 옥타브 낮게', 'signs'], ['15ma', '15ma: two octaves higher', '15ma: 두 옥타브 높게', null], ['breath', 'breath mark: a small break', '숨표: 잠깐 끊기', null], ['caesura', 'caesura: a full stop in the sound', '체수라: 소리를 완전히 멈춤', null]]],")
rep("['unacorda', 'una corda: the soft pedal', '우나 코르다: 약음 페달', 'terms', 'Grade 3'],",
    "['unacorda', 'una corda: the soft pedal', '우나 코르다: 약음 페달', 'terms', 'Grade 3'], ['trecorde', 'tre corde: let the soft pedal up', '트레 코르데: 약음 페달을 떼요', null], ['sost', 'sostenuto pedal: holds only the notes already down', '소스테누토 페달: 이미 누른 음만 잡아요', null],")
rep("    case 'unacorda': return",
    "    case 'staccatissimo': return refHead(30, 30) + refStemUp(30, 30) + '<path d=\"M27 38 L33 38 L30 47 Z\" fill=\"' + P + '\"/>';\n"
    "    case 'marcato': return refHead(30, 30) + refStemUp(30, 30) + '<path d=\"M23 39 L30 48 L37 39\" fill=\"none\" stroke=\"' + P + '\" stroke-width=\"2.2\" stroke-linejoin=\"round\"/>';\n"
    "    case 'mezzostacc': return refHead(30, 30) + refStemUp(30, 30) + refLn(23, 40, 37, 40, 2) + '<circle cx=\"30\" cy=\"46\" r=\"2.2\" fill=\"' + P + '\"/>';\n"
    "    case '15ma': return refTx('15ma', 4, 24, 13, { a: 'start' }) + '<path d=\"M33 19 H58 V26\" fill=\"none\" stroke=\"' + P + '\" stroke-width=\"1.3\" stroke-dasharray=\"3 3\"/>';\n"
    "    case 'breath': return refStaff5() + refTx('’', 33, 18, 30, { it: false });\n"
    "    case 'caesura': return refStaff5() + refLn(26, 44, 32, 8, 2.4) + refLn(33, 44, 39, 8, 2.4);\n"
    "    case 'trecorde': return refTx('tre corde', 32, 30, 12.5, { w: 800 });\n"
    "    case 'sost': return refTx('Sost. Ped.', 32, 30, 12, { w: 800 });\n"
    "    case 'unacorda': return")

# Music words: the kinds, forms and texture now have their own books (her '2 as well')
rep("<RefWordGroups groups={[...(part !== 'b' ? [['kinds', 'Kinds of piece', '곡의 종류', kinds]] : []), ...(part !== 'a' ? [['forms', 'Forms', '형식', forms], ['tex', 'Texture, style and sound', '짜임, 양식, 소리', tex],\n      ['voices', 'Voices', '목소리', voices], ['more', 'More words', '낱말 더', more('more')]] : [])]}/>",
    "<RefWordGroups groups={[...(part !== 'a' ? [['voices', 'Voices', '목소리', voices], ['more', 'More words', '낱말 더', more('more')]] : [])]}/>   {/* m28: kinds, forms and texture moved to their own books */}")

# sections, bodies, shelves
rep("refSec('nonchord', 'Non-chord notes', '비화성음'),", "refSec('melody', 'Melody', '선율'), refSec('nonchord', 'Non-chord notes', '비화성음'),")
rep("refSec('composers', 'Composers', '작곡가'),", "refSec('composers', 'Composers', '작곡가'), refSec('technique', 'Technique', '테크닉'), refSec('aural', 'Aural', '청음'),")
rep("composers: RefComposers, signs:", "composers: RefComposers, melody: RefMelody, technique: RefTechnique, aural: RefAural, signs:")
rep("['cadences', 'Cadences', '종지'], ['nonchord', 'Non-chord notes', '비화성음'],", "['cadences', 'Cadences', '종지'], ['melody', 'Melody', '선율'], ['nonchord', 'Non-chord notes', '비화성음'],")
rep("['composers', 'Composers', '작곡가'], ['instruments', 'Instruments', '악기']]],",
    "['composers', 'Composers', '작곡가'], ['instruments', 'Instruments', '악기']]],\n  ['Playing and listening', '연주와 듣기', [['technique', 'Technique', '테크닉'], ['aural', 'Aural', '청음']]],")
# paper
rep("['cadences'], ['chords:b'], ['nonchord'],", "['cadences'], ['chords:b'], ['melody'], ['nonchord'],") if "['cadences'], ['chords:b'], ['nonchord']," in s else None
open(p,'w').write(s); print('ok')
