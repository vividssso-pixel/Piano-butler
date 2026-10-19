import sys
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:90],s.count(a)); s=s.replace(a,b)
# numbers follow the Home lessons
rep("{!l.extra && <span style={{opacity:0.55,marginRight:6,fontWeight:900}}>{concept.levels.slice(0, li + 1).filter(z => z.short && !z.extra).length}</span>}","{l.num && <span style={{opacity:0.55,marginRight:6,fontWeight:900}}>{l.num}</span>}")
rep("short: ['Sharp order', '샵 순서'],","short: ['Sharp order', '샵 순서'], num: '1',")
rep("short: ['Flat order', '플랫 순서'],","short: ['Flat order', '플랫 순서'], num: '2',")
rep("short: ['Major: sharps', '장조: 샵'],","short: ['Major: sharps', '장조: 샵'], num: '3',")
rep("short: ['Major: flats', '장조: 플랫'],","short: ['Major: flats', '장조: 플랫'], num: '4',")
rep("{ n: 15, label: 'All 15 keys: name the major key', short: ['All 15', '15개 조'],","{ n: 15, label: 'Sharps and flats mixed: name the major key', short: ['Major: ♯ + ♭', '장조: 샵 + 플랫'], num: '3+4',")
rep("short: ['Relative minor', '나란한 단조'],","short: ['Relative minor', '나란한 단조'], num: '5',")
rep("short: ['Last note', '끝음'],","short: ['Last note', '끝음'], num: '6',")
rep("'Which notes get a sharp or a flat?': '샵이나 플랫이 붙는 음은?',","'Which notes get a sharp or a flat?': '샵이나 플랫이 붙는 음은?', 'Sharps and flats mixed: name the major key': '샵과 플랫 섞어서: 장조 이름 맞히기',")
open(sys.argv[2],'w',encoding='utf-8').write(s);print('ok')
