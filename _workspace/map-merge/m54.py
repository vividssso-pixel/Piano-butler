import re
p='drills.src.html'; s=open(p).read()
n0=s.count('Grade')
# 1. room names and titles that end in ', Grade N' (en) or ', Grade N' / ', N급' (ko): Level N
s,a=re.subn(r"'([^'\n\\]{1,60}), Grade ([1-8])'", r"'\1, Level \2'", s)
s,b=re.subn(r"'([^'\n\\]{1,40}), ([1-8])급'", r"'\1, 레벨 \2'", s)
for o,n in [("'Knowing Your Pieces, Grades 7 and 8'","'Knowing Your Pieces, Levels 7 and 8'"), ("'Knowing your pieces, Grades 7 and 8'","'Knowing your pieces, Levels 7 and 8'"),
            ("'내 곡 알기, Grade 7과 8'","'내 곡 알기, 레벨 7과 8'"), ("Grade 8 and Diplomas'","Level 8 and Diplomas'"), ("'Ear Training, Prelim'","'Ear Training, Level ½'"), ("'청음, Prelim'","'청음, 레벨 ½'"),
            ("'Musical terms, Grades 1-4, with sound.'","'Musical terms, Levels 1–4, with sound.'"),
            ("t('Grade ' + grade + ' terms', grade + '급 용어')","t('Level ' + grade + ' terms', '레벨 ' + grade + ' 용어')"),
            ("t('Grade ' + x, x + '급')","t('Level ' + x, '레벨 ' + x)")]:
    c=s.count(o); assert c>=1,o; s=s.replace(o,n)
# 2. drill step names that start with 'Grade N' and their Korean (LEVEL_KO keys and values change together)
for o in ['Grade 8 walk: I, IV or V?','Grade 8 grand scale: major or harmonic minor?','Grade 7 contrary motion: mirror twins?','Grade 6 contrary motion: mirror twins?','Grade 5 keys: where does finger 4 go?','Grade 5 contrary motion: mirror twins?','Grade 5 arpeggios: which finger?','Grade 4 contrary motion: mirror twins?','Grade 1 terms','Grade 2 terms','Grade 1: what does it mean?','Grade 2: what does it mean?']:
    c=s.count("'"+o+"'"); assert c>=1,o; s=s.replace("'"+o+"'", "'"+o.replace('Grade','Level',1)+"'")
s,c=re.subn(r": '([1-8])급 ([^'\n]{1,40})'", r": '레벨 \1 \2'", s)
s=s.replace("l.label.replace(/^Grade 8 /, '')", "l.label.replace(/^(Grade|Level) 8 /, '')")
open(p,'w').write(s); print('ok', a, b, c, n0, '->', s.count('Grade'))
# 3. Korean names say 레벨
s=open(p).read()
s,k=re.subn(r"'([^'\n\\]*[가-힣][^'\n\\]*), Level ([1-8])'", r"'\1, 레벨 \2'", s)
open(p,'w').write(s); print('ko', k)
