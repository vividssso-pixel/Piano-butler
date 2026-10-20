import sys
s=open(sys.argv[1],encoding='utf-8').read()
a="const sscScaleName = (k) => t(sscNameTxt(k) + ' major', sscNameTxt(k) + '장조 음계');"
assert s.count(a)==1
s=s.replace(a,"""// a black-key scale is titled with both names, like the keyboard: C♯ / D♭ major
const SSC_BOTH = { Db: 'C♯', Eb: 'D♯', Gb: 'F♯', Ab: 'G♯', Bb: 'A♯', 'C#': 'D♭', 'D#': 'E♭', 'F#': 'G♭', 'G#': 'A♭', 'A#': 'B♭' };
const sscTitleName = (k) => SSC_BOTH[k] ? (k[1] === 'b' ? SSC_BOTH[k] + ' / ' + sscNameTxt(k) : sscNameTxt(k) + ' / ' + SSC_BOTH[k]) : sscNameTxt(k);
const sscScaleName = (k) => t(sscTitleName(k) + ' major', sscTitleName(k) + '장조 음계');""")
open(sys.argv[2],'w',encoding='utf-8').write(s)
