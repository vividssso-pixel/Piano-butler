import sys,re,json,os,urllib.parse as up
sys.path.insert(0,'/tmp/claude-0/pk'); import pagemap as PM, checkbank as CB
s=open('/tmp/claude-0/pk/readpage.py').read(); i=s.index('DRILL = {'); j=s.index('\n}\n',i)
D={}
for ch,body in re.findall(r"'([A-Z]\d)': \[(.*?)\]",s[i:j]):
    D[ch]=[(d,int(lv),lab) for d,lab,lv in re.findall(r"\('([a-z0-9-]+)', '([^']*)', (\d+)\)",body)]
T=dict(CB.TITLES); T['B1']='Posture and hand shape'
KO={'B1':'자세와 손 모양','P1':'건반','P2':'오선과 음자리표','P3':'오선과 건반','P4':'음 읽기','P5':'덧줄','P6':'올림표, 내림표, 제자리표','P7':'음정 세기','P8':'장·단·완전 음정',
'T1':'박, 빠르기, 마디','T2':'음표와 쉼표','T3':'음의 길이','T4':'박자표','T5':'겹박자와 불규칙 박자','T6':'리듬: 묶음과 못갖춘마디','T7':'리듬: 엇박','T8':'도돌이표와 길 표시',
'E1':'셈여림','E2':'터치: 부드럽게, 짧게, 강하게','E3':'빠르기말','E4':'페달','E5':'꾸밈음','S1':'장음계','S2':'단음계','S3':'조와 조표','S4':'조 찾기','S5':'오도권',
'H1':'화음과 3화음','H2':'네 가지 3화음','H3':'조 안의 화음','H4':'자리바꿈','H5':'7화음','H6':'색깔 화음','H7':'탑: 9, 11, 13','H8':'슬래시 화음',
'M1':'조 밖의 화음','M2':'마침꼴','M3':'선율 아래 화음','M4':'어디에나 있는 진행','F1':'동기와 프레이즈','F2':'반복과 모진행','F3':'짜임새','F4':'조바꿈','F5':'형식','F6':'시대별 양식',
'L1':'운지','L2':'잘 연습하기','L3':'초견','L4':'듣기','L5':'연주하기','G1':'화음 밖의 음'}
PART={'B':('Before you play','연주 전에'),'P':('Part I · Pitch','Part I · 음높이'),'T':('Part II · Time','Part II · 시간'),'E':('Part III · Expression','Part III · 표현'),'S':('Part IV · Scales and keys','Part IV · 음계와 조'),
'H':('Part V · Chords','Part V · 화음'),'M':('Part VI · Harmony in music','Part VI · 음악 속 화성'),'F':('Part VII · Shape and style','Part VII · 형식과 양식'),'L':('Part VIII · Playing and listening','Part VIII · 연주와 듣기'),'G':('Part IX · Going further','Part IX · 더 나아가기')}
WBF={'B':'Before you play','P':'Pitch','T':'Time','E':'Expression','S':'Scales and keys','H':'Chords and harmony','M':'Chords and harmony','F':'Shape and style','L':'Playing and listening','G':'Going further'}
WBN={'B':0,'P':1,'T':2,'E':3,'S':4,'H':5,'M':6,'F':7,'L':8,'G':9}
def wb(k):
    p,i=k[0],int(k[1:]); d='/mnt/user-data/outputs/books-latest/2 Workbook/'+WBF[p]
    pre=f'workbook-{WBN[p]}-{1 if p=="S" else i}-'
    f=[x for x in sorted(os.listdir(d)) if x.startswith(pre)]
    pages=str(i) if p=='S' else f'{2*i-1}–{2*i}'
    return ['Claude outputs/Books - latest/2 Workbook/'+WBF[p]+'/'+f[0], ('p. ' if p=='S' else 'pp. ')+pages]
# her 11 Nov: rooms hold slices -- the clips (1-based, in Read & listen order) a floor needs; no entry = the whole chapter
SLICE={'P1':[1,2,3,4,9],'T1':[1,3,6,7,8],'T2':[1,2],'E1':[1,7],
       'T3':[1,2,3,5,7,10,11,12],'T4':[1,2,3,4,6,8],'T8':[1,2,3,4,5],'E2':[1,2,3,4],'S1':[1,2,3,7],'S2':[1,2,4,6],
       'T5':[1,2,3,4,5,7],'T6':[1,2,3,4,7],'T7':[1,3]}   # her 11 Nov ("ok"): Grade 1 and up sliced too
FLOORS=[('Beginner','B1 P1 L1 P2 T1 T2 E1',[]),
('Prelim','L2 P3 P4 T3 T4 T8 E2 S1 S2 H1',[('P1','note-names',3,'The two ends and the eight Cs','양 끝과 여덟 개의 C',[5,6,7,8]),('T1','pulse',3,'Tempo, strong and weak beats','빠르기, 강박과 약박',[2,4,5]),('T2','note-values',4,'Quavers, stems and flags','8분음표, 기둥과 꼬리',[6,7,12,13]),('E1','dynamics',3,'mp, mf and the hairpins','mp, mf와 헤어핀',[2,3,5,6])]),
('Grade 1','P5 P6 P7 S3 T5 E3 H2 L3',[('S2','minor-scales',4,'D minor and the raised 7th','D 단음계와 올린 7음',[5]),('H1','chords',7,'Tonic triads: which key?','으뜸3화음: 무슨 조?'),
  ('S1','scales',3,'F major','F 장음계',[5]),('T3','note-values',7,'Dotted rhythms','점음표 리듬',[4,8,9,13]),('T4','time-signatures',8,'3/8 and changing time','3/8과 박자 바꾸기',[5,7]),
  ('T2','time-signatures',7,'The whole-bar rest','온마디 쉼표',[8]),('E1','dynamics',2,'sfz and fp','sfz와 fp',[4]),('E2','dynamics',5,'Two-note slurs','두 음 슬러',[5])]),
('Grade 2','P8 T6 S4 E4 H3 F1',[('S3','key-signatures',14,'Major keys from flats','플랫으로 장조 찾기'),('P7','intervals',5,'Melodic or harmonic?','가락 음정일까 화성 음정일까?'),
  ('S1','scales',3,'D major','D 장음계',[4]),('T8','signs',4,'D.C. and D.S.','D.C.와 D.S.',[6,7])]),
('Grade 3','S5 E5 H4 F2 L4',[('S3','key-signatures',15,'Sharps and flats mixed','샵과 플랫 섞어서'),('P8','intervals',7,'Intervals by ear','듣고 음정 맞히기'),('T6','rhythm',8,'Triplets and semiquavers','셋잇단음표와 16분음표',[5,6]),
  ('S1','scales',3,'A major','A 장음계',[6]),('S2','minor-scales',4,'C minor','C 단음계',[3])]),
('Grade 4','T7 M2 M3 F3 F4',[('P8','intervals',8,'Above the tonic, in my keys','으뜸음 위 음정'),('H4','harmony-4',2,'First inversions: which chord?','첫째 자리바꿈: 어떤 화음?'),('S3','keys-4',1,'The Level 4 keys','4급의 조'),
  ('T3','note-values',9,'The double dot','겹점',[6])]),
('Grade 5','F5 F6 M1 M4 G1 L5',[('F4','keys-5',5,'Dominant, subdominant or relative?','딸림조, 버금딸림조, 나란한조?'),('S2','keys-5',2,'The melodic minor','가락 단음계'),('H4','harmony-5',2,'I, Ib or Ic?','I, Ib, Ic?'),
  ('T5','time-signatures',10,'Irregular time (Extra)','불규칙 박자 (Extra)',[6])]),
('Grade 6','H5 H8',[('M2','harmony-3',6,'Perfect or plagal cadence?','정격일까 변격일까?'),('H5','harmony-6',1,'V7, V7b, V7c or V7d?','V7의 자리바꿈'),('H2','chords',5,'Major or minor by ear','듣고 장·단 맞히기')]),
('Grade 7','H6',[('M2','harmony-4',3,'Which cadence? (with interrupted)','어떤 마침꼴? (거짓마침 포함)'),('T7','rhythm',9,'Swing, hemiola and polyrhythm','스윙, 헤미올라, 폴리리듬',[2,4,5]),('F5','form',7,'Read the road','곡의 지도 읽기'),('F6','styles',4,'Which style is it?','어떤 양식?')]),
('Grade 8','H7',[('M4','harmony-5',4,'Which chord comes before V?','V 앞에 오는 화음은?'),('H2','harmony-6',4,'Is it a related key?','가까운 조일까?'),('F6','styles',9,'Which style? (by ear)','어떤 양식? (듣고)')]),
]
FLOOR_TXT={'Beginner':('Sitting and hands, the keyboard and the staff, beat and note values, loud and soft, and fingering.','자세와 손, 건반과 오선, 박과 음표 길이, 셈여림, 운지.'),
'Prelim':('How to practise, reading the notes, how long a note lasts, time signatures, repeats, touch, major and minor scales, and your first chords.','연습법, 음 읽기, 음의 길이, 박자표, 도돌이표, 터치, 장음계와 단음계, 첫 화음.'),
'Grade 1':('Ledger lines, sharps and flats, intervals, key signatures, 6/8, speed words, four kinds of triad and sight-reading.','덧줄, 올림·내림표, 음정, 조표, 6/8, 빠르기말, 네 가지 3화음, 초견.'),
'Grade 2':('Major, minor and perfect, upbeats and triplets, finding the key, the pedals, chords in a key, motifs and phrases.','장·단·완전, 못갖춘마디와 셋잇단음표, 조 찾기, 페달, 조 안의 화음, 동기와 프레이즈.'),
'Grade 3':('The circle of fifths, ornaments, inversions, repetition and sequence, and listening.','오도권, 꾸밈음, 자리바꿈, 반복과 모진행, 듣기.'),
'Grade 4':('Off the beat, cadences, chords under a melody, texture and changing key.','엇박, 마침꼴, 선율 아래 화음, 짜임새, 조바꿈.'),
'Grade 5':('Form, styles through time, chords from outside the key, progressions and performing.','형식, 시대별 양식, 조 밖의 화음, 진행, 연주하기.'),
'Grade 6':('Seventh chords and slash chords, and cadences by ear.','7화음과 슬래시 화음, 듣고 마침꼴 맞히기.'),
'Grade 7':('Colour chords (Extra), and every earlier chapter a step further.','색깔 화음(Extra), 그리고 앞의 챕터들 한 걸음 더.'),
'Grade 8':('Tall chords: 9, 11, 13 (Extra), and every earlier chapter a step further.','높은 화음 9·11·13(Extra), 그리고 앞의 챕터들 한 걸음 더.')}
# her 11 Nov: notes and rests one at a time on Level 0, crotchet first, the three-beat note included.
# chapter -> [(suffix, en, ko, clips, rows to show, drill, level, nv filter)]; the first entry renames the chapter's own room
STEPS={'T2':[('', 'Notes: crotchet and minim', '음표: 4분음표와 2분음표', [1,2,3], 'crotchets,minims', 'note-values', 2, 'nv=crotchet,rcrotchet,minim,rminim'),   # her 12 Nov: two lengths a room ("2개씩 합쳐도")
             ('-s2', 'Notes: three beats and the semibreve', '음표: 세 박과 온음표', [4,5,9,10,11,14], 'crotchets,minims,semibreve', 'note-values', 2, 'nv=crotchet,rcrotchet,minim,rminim,dminim,semibreve,rsemibreve')]}

# her 12 Nov ("aural도 있었는데 그 부분도 맞춰주고"): an Ear training room on every floor. Each part is one aural test of that
# grade (AMEB Manual of Syllabuses 2026, Aural Test Requirements, in data_aural_ameb.js), in plain words, with the app's own
# ear-training game for it (the old lessons' chapters ear-prep, listen-sing, listen-write, listen-23, listen-3 ... listen-8).
# (title en, title ko, what happens in the exam en, ko, drill, level)
EAR={
'Beginner':[('Low, middle or high?','낮은 음, 가운데, 높은 음?','Before the exams: is the sound low, in the middle or high?','시험 전 준비: 소리가 낮은지, 가운데인지, 높은지 들어 봐요.','ear-prep',1),
  ('Same rhythm or different?','같은 리듬? 다른 리듬?','Two rhythms: the same, or one small change?','두 리듬이 같은지, 조금 다른지 들어 봐요.','ear-prep',2),
  ('Same tune or different?','같은 가락? 다른 가락?','Two little tunes: the same, or one note changed?','두 가락이 같은지, 한 음이 바뀌었는지 들어 봐요.','ear-prep',3),
  ('Which way did it go?','어느 쪽으로 갔을까?','Three notes: going up, going down, or staying?','세 음이 올라가는지, 내려가는지, 그대로인지 들어 봐요.','ear-prep',4),
  ('Find the note','음 찾기','Hear a note, then find it on the keys.','음을 듣고 건반에서 찾아요.','ear-prep',5)],
'Prelim':[('Clap the beat','박 치기','The examiner plays in two- or three-beat time, slow, moderate or quick. You clap the beat, and keep going after the music stops.','시험관이 2박자나 3박자로 느리게, 보통으로, 빠르게 쳐요. 박에 맞춰 손뼉을 치고, 음악이 멈춘 뒤에도 계속 쳐요.','time-signatures',3),
  ('Echo the rhythm','리듬 따라 하기','The examiner plays a simple two-bar rhythm. You clap, tap, hum or sing it back.','시험관이 쉬운 두 마디 리듬을 쳐요. 손뼉이나 허밍으로 그대로 따라 해요.','listen-sing',2),
  ('Sing the tune','가락 따라 부르기','The examiner plays five or six notes, then again slowly. You sing or hum each note.','시험관이 다섯에서 여섯 음을 치고, 다시 천천히 쳐요. 한 음씩 따라 불러요.','listen-sing',3),
  ('Higher or lower?','높을까, 낮을까?','The examiner plays two notes, one after the other, at least a 3rd apart. You say which is higher or lower.','시험관이 3도 넘게 떨어진 두 음을 차례로 쳐요. 어느 음이 더 높은지, 낮은지 말해요.','listen-sing',1)],
'Grade 1':[('Find the home note','으뜸음 찾기','The examiner plays an unfinished phrase. You hum or sing the tonic, the home note.','시험관이 끝나지 않은 프레이즈를 쳐요. 으뜸음(집 음)을 허밍하거나 불러요.','listen-write',1),
  ('Clap it back','리듬 치기','The examiner plays a passage twice, in two or three time. You tap or clap it.','시험관이 2박자나 3박자 악구를 두 번 쳐요. 그 리듬을 손뼉으로 쳐요.','listen-write',4),
  ('Sing it back','따라 부르기','The examiner plays a short phrase twice. You hum or sing it: the tune and the rhythm together.','시험관이 짧은 프레이즈를 두 번 쳐요. 가락과 리듬을 함께 따라 불러요.','listen-write',3),
  ('Warm-up: which rhythm?','준비 운동: 어떤 리듬?','Not in the exam: a game that gets you ready for clapping back.','시험에는 없어요. 리듬 치기를 준비하는 게임이에요.','listen-write',2)],
'Grade 2':[('Clap it back','리듬 치기','The examiner plays a passage twice, in two or three time. You tap or clap it.','시험관이 2박자나 3박자 악구를 두 번 쳐요. 그 리듬을 손뼉으로 쳐요.','listen-23',2),
  ('Sing it back','따라 부르기','The examiner plays a short phrase twice. You hum or sing it: the tune and the rhythm together.','시험관이 짧은 프레이즈를 두 번 쳐요. 가락과 리듬을 함께 따라 불러요.','listen-23',3),
  ('Two notes together: sing one','두 음을 함께: 한 음 부르기','The examiner plays two notes together, a major 3rd or a perfect 5th apart. You hum or sing the higher or the lower one.','시험관이 장3도나 완전5도 떨어진 두 음을 함께 쳐요. 높은 음이나 낮은 음을 불러요.','listen-23',1)],
'Grade 3':[('Clap it back, then two or three?','리듬 치고, 2박자? 3박자?','The examiner plays a passage twice. You clap it, then say whether it is in duple or triple time.','시험관이 악구를 두 번 쳐요. 리듬을 치고, 2박자인지 3박자인지 말해요.','listen-3',4),
  ('Sing it back','따라 부르기','The examiner plays a short phrase twice. You hum or sing it: the tune and the rhythm together.','시험관이 짧은 프레이즈를 두 번 쳐요. 가락과 리듬을 함께 따라 불러요.','listen-3',5),
  ('Any two notes together: sing one','아무 두 음: 한 음 부르기','The examiner plays any two notes together, within an octave of Middle C. You hum or sing the higher or the lower one.','시험관이 가온 다에서 한 옥타브 안의 두 음을 함께 쳐요. 높은 음이나 낮은 음을 불러요.','listen-3',1),
  ('From the keynote: 2nd, 3rd, 4th or 5th?','으뜸음에서: 2도, 3도, 4도, 5도?','The examiner plays the keynote, then the 2nd, 3rd, 4th or 5th of the major scale. You sing it, then name it.','시험관이 으뜸음을 치고, 장음계의 2도, 3도, 4도, 5도 가운데 하나를 쳐요. 따라 부르고 이름을 말해요.','listen-3',2),
  ('Warm-up: duple or triple?','준비 운동: 2박자? 3박자?','Part of the clapping test: is the music in two or in three?','리듬 치기 시험의 한 부분: 2박자인지 3박자인지 들어요.','listen-3',3)],
'Grade 4':[('Clap it back, then two or three?','리듬 치고, 2박자? 3박자?','The examiner plays a passage twice. You clap it, then say whether it is in duple or triple time.','시험관이 악구를 두 번 쳐요. 리듬을 치고, 2박자인지 3박자인지 말해요.','listen-4',4),
  ('From the keynote: name the interval','으뜸음에서: 음정 이름','The examiner plays the keynote, then any note of the major scale. You sing it, then name the interval.','시험관이 으뜸음을 치고, 장음계의 한 음을 쳐요. 따라 부르고 음정 이름을 말해요.','listen-4',1),
  ('Two parts: sing the higher or the lower','두 성부: 높은 쪽이나 낮은 쪽','The examiner plays two intervals, one after the other. You sing the higher or the lower part from memory.','시험관이 음정 두 개를 이어서 쳐요. 높은 성부나 낮은 성부를 기억해서 불러요.','listen-4',2),
  ('A triad: hum the middle note','3화음: 가운데 음','The examiner plays a major or minor triad, in root position or an inversion. You hum or sing the middle note.','시험관이 장3화음이나 단3화음을 기본 위치나 자리바꿈으로 쳐요. 가운데 음을 불러요.','listen-4',3),
  ('All four, mixed, as in the exam','네 가지 섞어서, 시험처럼','The four tests in a row, as the examiner gives them.','시험처럼 네 가지를 이어서 해 봐요.','listen-4',5)],
'Grade 5':[('Clap it back, then two or three?','리듬 치고, 2박자? 3박자?','The examiner plays a passage twice. You clap it, then say whether it is in duple or triple time.','시험관이 악구를 두 번 쳐요. 리듬을 치고, 2박자인지 3박자인지 말해요.','listen-5',4),
  ('Any keynote: name the interval','아무 으뜸음에서: 음정 이름','The examiner plays a keynote, then any note of the major scale. You sing it, then name the interval.','시험관이 으뜸음을 치고, 장음계의 한 음을 쳐요. 따라 부르고 음정 이름을 말해요.','listen-5',1),
  ('Three intervals: sing one part','음정 세 개: 한 성부 부르기','The examiner plays three intervals slowly, one after the other. You sing the higher or the lower part from memory.','시험관이 음정 세 개를 천천히 이어서 쳐요. 높은 성부나 낮은 성부를 기억해서 불러요.','listen-5',2),
  ('A triad: sing all three notes','3화음: 세 음 모두 부르기','The examiner plays a major or minor triad, in root position or an inversion. You sing all three notes, going up or down as asked.','시험관이 장3화음이나 단3화음을 쳐요. 세 음을 올라가거나 내려가며 모두 불러요.','listen-5',3),
  ('All four, mixed, as in the exam','네 가지 섞어서, 시험처럼','The four tests in a row, as the examiner gives them.','시험처럼 네 가지를 이어서 해 봐요.','listen-5',5)],
'Grade 6':[('Major or harmonic minor: name the interval','장음계나 화성단음계: 음정 이름','The examiner plays a keynote, then any note of the major or harmonic minor scale. You sing it, then name the interval.','시험관이 으뜸음을 치고, 장음계나 화성단음계의 한 음을 쳐요. 따라 부르고 음정 이름을 말해요.','listen-6',1),
  ('A major triad: which position?','장3화음: 어느 자리?','The examiner plays a major triad, in root position or an inversion. You say which position it is in.','시험관이 장3화음을 기본 위치나 자리바꿈으로 쳐요. 어느 자리인지 말해요.','listen-6',2),
  ('Four intervals: sing one part','음정 네 개: 한 성부 부르기','The examiner plays four intervals, one after the other. You sing the higher or the lower part from memory.','시험관이 음정 네 개를 이어서 쳐요. 높은 성부나 낮은 성부를 기억해서 불러요.','listen-6',3),
  ('Perfect or plagal?','정격? 변격?','The examiner sounds the tonic chord, then plays a short piece in a major key. You name the perfect and plagal cadences as they come.','시험관이 으뜸화음을 들려준 뒤 장조의 짧은 곡을 쳐요. 정격마침과 변격마침을 알아맞혀요.','listen-6',4),
  ('All four, mixed, as in the exam','네 가지 섞어서, 시험처럼','The four tests in a row, as the examiner gives them.','시험처럼 네 가지를 이어서 해 봐요.','listen-6',5)],
'Grade 7':[('Major or minor, and which position?','장? 단? 그리고 어느 자리?','The examiner plays a major or minor triad, in root position or an inversion. You say which kind it is, and its position.','시험관이 장3화음이나 단3화음을 쳐요. 종류와 자리를 말해요.','listen-7',1),
  ('Perfect, plagal or interrupted?','정격, 변격, 거짓마침?','The examiner sounds the tonic chord, then plays a short piece in a major key. You name the perfect, plagal and interrupted cadences as they come.','시험관이 으뜸화음을 들려준 뒤 장조의 짧은 곡을 쳐요. 정격, 변격, 거짓마침을 알아맞혀요.','listen-7',2),
  ('Remember a two-bar phrase','두 마디 프레이즈 외우기','You have about a minute, away from the piano, to memorise a printed two-bar phrase. Then you play or sing it from memory.','피아노에서 떨어져 약 1분 동안 악보의 두 마디 프레이즈를 외워요. 그다음 외워서 치거나 불러요.','listen-7',3),
  ('Six notes: sing one part','여섯 음: 한 성부 부르기','The examiner plays a two-part phrase of up to six notes, slowly. You sing the higher or the lower part from memory.','시험관이 여섯 음 이내의 2성부 프레이즈를 천천히 쳐요. 높은 성부나 낮은 성부를 기억해서 불러요.','listen-7',4),
  ('All four, mixed, as in the exam','네 가지 섞어서, 시험처럼','The four tests in a row, as the examiner gives them.','시험처럼 네 가지를 이어서 해 봐요.','listen-7',5)],
'Grade 8':[('Major, minor or diminished, and which position?','장, 단, 감? 그리고 어느 자리?','The examiner plays a major or minor triad in any position, or a diminished triad in root position. You name the kind, and the position of a major or minor triad.','시험관이 장·단3화음을 아무 자리로, 또는 감3화음을 기본 위치로 쳐요. 종류를 말하고, 장·단3화음은 자리도 말해요.','listen-8',1),
  ('Which of the four cadences?','네 가지 마침꼴 가운데?','The examiner sounds the tonic chord, then plays a short piece in a major key. You name any of the four cadences as they come.','시험관이 으뜸화음을 들려준 뒤 장조의 짧은 곡을 쳐요. 네 가지 마침꼴을 알아맞혀요.','listen-8',2),
  ('Remember a three- or four-bar phrase','서너 마디 프레이즈 외우기','You have about a minute and a half, away from the piano, to memorise a printed phrase of three or four bars. Then you play or sing it from memory.','피아노에서 떨어져 약 1분 30초 동안 서너 마디 프레이즈를 외워요. 그다음 외워서 치거나 불러요.','listen-8',3),
  ('The lower part, with passing notes','지나가는 음이 있는 아래 성부','The examiner plays a two-part phrase with a few passing notes. You hum, sing or play the lower part from memory.','시험관이 지나가는 음이 조금 있는 2성부 프레이즈를 쳐요. 아래 성부를 기억해서 부르거나 쳐요.','listen-8',4),
  ('All four, mixed, as in the exam','네 가지 섞어서, 시험처럼','The four tests in a row, as the examiner gives them.','시험처럼 네 가지를 이어서 해 봐요.','listen-8',5)]}
rooms=[]; floors=[]
for fname,new,rev in FLOORS:
    ids=[]
    for k in new.split():
        a,c=PM.pages_of(k); pg=f'{a}' if c==1 else f'{a}–{a+c-1}'
        n=k[1:]
        if fname=='Beginner' and k in STEPS:
            for suf,en,ko,cl,rows,dd,lv,nv in STEPS[k]:
                rooms.append(dict(id='hbr-'+k+suf,ch=k,en=en,ko=ko,part=PART[k[0]],num=n,pages=pg,wb=wb(k),dr=[[dd,lv,'How many beats?',nv]],again=None,clips=cl,rows=rows or None))
                ids.append('hbr-'+k+suf)
            continue
        rooms.append(dict(id='hbr-'+k,ch=k,en=T[k],ko=KO[k],part=PART[k[0]],num=('' if k[0]=='B' else n),pages=pg,wb=wb(k),dr=[[d,lv,lab] for d,lv,lab in D[k]],again=None,clips=SLICE.get(k)))
        ids.append('hbr-'+k)
    rooms.append(dict(id='hbr-ear-'+fname.lower().replace(' ',''),ch='EAR',en='Ear training',ko='청음',part=('Ear training','청음'),num='',pages='',wb=None,dr=[],again=None,
        ear=[dict(en=a,ko=b,exam=c,examko=d,dr=[e,f,a]) for a,b,c,d,e,f in EAR[fname]]))
    ids.append('hbr-ear-'+fname.lower().replace(' ',''))
    # her 12 Nov ("단순하게"): a floor's revisits fold into ONE review room, a short list of parts (each: listen, then its drill)
    parts=[]
    for rv in rev:
        k,d,lv,en,ko=rv[:5]; cl=rv[5] if len(rv)>5 else None
        a,c=PM.pages_of(k)
        parts.append(dict(ch=k,en=en,ko=ko,chen=T[k],chko=KO[k],pages=f'{a}–{a+c-1}',clips=cl,dr=[d,lv,en]))
    if parts:
        rid=f'hbr-review-{fname.replace(" ","").lower()}'
        rooms.append(dict(id=rid,ch=parts[0]['ch'],en='Review',ko='복습',part=('Review','복습'),num='',pages='',wb=None,dr=[],again=None,review=parts))
        ids.append(rid)
    floors.append(dict(ids=ids,en=[fname,FLOOR_TXT[fname][0]],ko=[fname,FLOOR_TXT[fname][1]]))
assert len({r['ch'] for r in rooms if not r.get('review') and not r.get('ear')})>=50, len({r['ch'] for r in rooms if not r['again']})
open('/tmp/claude-0/house/data.js','w').write('const HB_ROOMS = '+json.dumps(rooms,ensure_ascii=False)+';\nconst HB_FLOORS = '+json.dumps(floors,ensure_ascii=False)+';\n')
print(len(rooms),'rooms', [len(f['ids']) for f in floors])
