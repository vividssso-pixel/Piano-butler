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
'L1':'운지','L2':'잘 연습하기','L3':'초견','L4':'듣기','L5':'연주하기'}
PART={'B':('Before you play','연주 전에'),'P':('Part I · Pitch','Part I · 음높이'),'T':('Part II · Time','Part II · 시간'),'E':('Part III · Expression','Part III · 표현'),'S':('Part IV · Scales and keys','Part IV · 음계와 조'),
'H':('Part V · Chords','Part V · 화음'),'M':('Part VI · Harmony in music','Part VI · 음악 속 화성'),'F':('Part VII · Shape and style','Part VII · 형식과 양식'),'L':('Part VIII · Playing and listening','Part VIII · 연주와 듣기')}
WBF={'B':'Before you play','P':'Pitch','T':'Time','E':'Expression','S':'Scales and keys','H':'Chords and harmony','M':'Chords and harmony','F':'Shape and style','L':'Playing and listening'}
WBN={'B':0,'P':1,'T':2,'E':3,'S':4,'H':5,'M':6,'F':7,'L':8}
def wb(k):
    p,i=k[0],int(k[1:]); d='/mnt/user-data/outputs/books-latest/2 Workbook/'+WBF[p]
    pre=f'workbook-{WBN[p]}-{1 if p=="S" else i}-'
    f=[x for x in sorted(os.listdir(d)) if x.startswith(pre)]
    pages=str(i) if p=='S' else f'{2*i-1}–{2*i}'
    return ['Claude outputs/Books - latest/2 Workbook/'+WBF[p]+'/'+f[0], ('p. ' if p=='S' else 'pp. ')+pages]
FLOORS=[('Beginner','B1 P1 L1 P2 T1 T2 E1 L2',[]),
('Prelim','P3 P4 T3 T4 T8 E2 S1 S2 H1',[]),
('Grade 1','P5 P6 P7 S3 T5 E3 H2 L3',[('S2','minor-scales',4,'The raised 7th','올린 7음'),('H1','chords',7,'Tonic triads: which key?','으뜸3화음: 무슨 조?')]),
('Grade 2','P8 T6 S4 E4 H3 F1',[('S3','key-signatures',14,'Major keys from flats','플랫으로 장조 찾기'),('P7','intervals',5,'Melodic or harmonic?','가락 음정일까 화성 음정일까?')]),
('Grade 3','S5 E5 H4 F2 L4',[('S3','key-signatures',15,'Sharps and flats mixed','샵과 플랫 섞어서'),('P8','intervals',7,'Intervals by ear','듣고 음정 맞히기'),('T6','rhythm',8,'Semiquavers: 1 e + a','16분음표: 1 e + a')]),
('Grade 4','T7 M2 M3 F3 F4',[('P8','intervals',8,'Above the tonic, in my keys','으뜸음 위 음정'),('H4','harmony-4',2,'First inversions: which chord?','첫째 자리바꿈: 어떤 화음?'),('S3','keys-4',1,'The Level 4 keys','4급의 조')]),
('Grade 5','F5 F6 M1 M4 L5',[('F4','keys-5',5,'Dominant, subdominant or relative?','딸림조, 버금딸림조, 나란한조?'),('S2','keys-5',2,'The melodic minor','가락 단음계'),('H4','harmony-5',2,'I, Ib or Ic?','I, Ib, Ic?')]),
('Grade 6','H5 H8',[('M2','harmony-3',6,'Perfect or plagal cadence?','정격일까 변격일까?'),('H5','harmony-6',1,'V7, V7b, V7c or V7d?','V7의 자리바꿈'),('H2','chords',5,'Major or minor by ear','듣고 장·단 맞히기')]),
('Grade 7','H6',[('M2','harmony-4',3,'Which cadence? (with interrupted)','어떤 마침꼴? (거짓마침 포함)'),('T7','rhythm',9,'Syncopation','싱코페이션'),('F5','form',7,'Read the road','곡의 지도 읽기'),('F6','styles',4,'Which style is it?','어떤 양식?')]),
('Grade 8','H7',[('M4','harmony-5',4,'Which chord comes before V?','V 앞에 오는 화음은?'),('H2','harmony-6',4,'Is it a related key?','가까운 조일까?'),('F6','styles',9,'Which style? (by ear)','어떤 양식? (듣고)'),('L4','listen-8',0,'Ear training for Level 8','8급 청음')]),
]
FLOOR_TXT={'Beginner':('Sitting and hands, the keyboard and the staff, beat and note values, loud and soft, fingering and how to practise.','자세와 손, 건반과 오선, 박과 음표 길이, 셈여림, 운지와 연습법.'),
'Prelim':('Reading the notes, how long a note lasts, time signatures, repeats, touch, major and minor scales, and your first chords.','음 읽기, 음의 길이, 박자표, 도돌이표, 터치, 장음계와 단음계, 첫 화음.'),
'Grade 1':('Ledger lines, sharps and flats, intervals, key signatures, 6/8, speed words, four kinds of triad and sight-reading.','덧줄, 올림·내림표, 음정, 조표, 6/8, 빠르기말, 네 가지 3화음, 초견.'),
'Grade 2':('Major, minor and perfect, upbeats and triplets, finding the key, the pedals, chords in a key, motifs and phrases.','장·단·완전, 못갖춘마디와 셋잇단음표, 조 찾기, 페달, 조 안의 화음, 동기와 프레이즈.'),
'Grade 3':('The circle of fifths, ornaments, inversions, repetition and sequence, and listening.','오도권, 꾸밈음, 자리바꿈, 반복과 모진행, 듣기.'),
'Grade 4':('Off the beat, cadences, chords under a melody, texture and changing key.','엇박, 마침꼴, 선율 아래 화음, 짜임새, 조바꿈.'),
'Grade 5':('Form, styles through time, chords from outside the key, progressions and performing.','형식, 시대별 양식, 조 밖의 화음, 진행, 연주하기.'),
'Grade 6':('Seventh chords and slash chords, and cadences by ear.','7화음과 슬래시 화음, 듣고 마침꼴 맞히기.'),
'Grade 7':('Colour chords (Extra), and every earlier chapter a step further.','색깔 화음(Extra), 그리고 앞의 챕터들 한 걸음 더.'),
'Grade 8':('Tall chords: 9, 11, 13 (Extra), and every earlier chapter a step further.','높은 화음 9·11·13(Extra), 그리고 앞의 챕터들 한 걸음 더.')}
rooms=[]; floors=[]
for fname,new,rev in FLOORS:
    ids=[]
    for k in new.split():
        a,c=PM.pages_of(k); pg=f'{a}' if c==1 else f'{a}–{a+c-1}'
        n=k[1:]
        rooms.append(dict(id='hbr-'+k,ch=k,en=T[k],ko=KO[k],part=PART[k[0]],num=('' if k[0]=='B' else n),pages=pg,wb=wb(k),dr=[[d,lv,lab] for d,lv,lab in D[k]],again=None))
        ids.append('hbr-'+k)
    for k,d,lv,en,ko in rev:
        a,c=PM.pages_of(k); pg=f'{a}–{a+c-1}'
        rid=f'hbr-{k}-{fname.replace(" ","").lower()}'
        rooms.append(dict(id=rid,ch=k,en=T[k],ko=KO[k],part=PART[k[0]],num=k[1:],pages=pg,wb=wb(k),dr=[[d,lv,en]],again=[en,ko]))
        ids.append(rid)
    floors.append(dict(ids=ids,en=[fname,FLOOR_TXT[fname][0]],ko=[fname,FLOOR_TXT[fname][1]]))
assert len({r['ch'] for r in rooms if not r['again']})==50, len({r['ch'] for r in rooms if not r['again']})
open('/tmp/claude-0/house/data.js','w').write('const HB_ROOMS = '+json.dumps(rooms,ensure_ascii=False)+';\nconst HB_FLOORS = '+json.dumps(floors,ensure_ascii=False)+';\n')
print(len(rooms),'rooms', [len(f['ids']) for f in floors])
