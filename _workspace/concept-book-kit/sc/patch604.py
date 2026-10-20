import sys
s=open(sys.argv[1],encoding='utf-8').read()
a="tryLine: ['Three steps: white keys, black keys, all twelve', '세 단계: 흰건반, 검은건반, 열두 조'],"
assert s.count(a)==1
s=s.replace(a,"tryLine: ['Eleven short lessons: the shape, fingering, all twelve keys, the minor scales', '열한 개의 짧은 레슨: 모양, 손가락, 열두 조, 단음계'],")
open(sys.argv[2],'w',encoding='utf-8').write(s)
