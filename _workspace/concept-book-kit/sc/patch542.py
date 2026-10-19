import sys
s=open(sys.argv[1],encoding='utf-8').read()
a="t('Copy link for a student', '학생용 링크 복사')"
assert s.count(a)==1
s=s.replace(a,"t('Copy link', '링크 복사')")
open(sys.argv[2],'w',encoding='utf-8').write(s);print('ok')
