# Build listen.html: the page the lesson book's QR codes open (thepianobutler.com/listen.html#<song>).
# It plays each lesson's tune (and its More to play tunes) from the same data the book is engraved from.
import json, re, sys
SONGS = ['buns', 'clair', 'mary', 'ode', 'jingle', 'rain6']
TEMPO = {'jingle': 116, 'clair': 92, 'ode': 100, 'rain6': 96}
data = []
for f in SONGS:
    j = json.load(open(f + '.json'))
    tunes = [{'t': 'The song', 'b': [[n[:4] for n in bar] for bar in j['bars']]}]
    for m in j.get('more', []): tunes.append({'t': m['title'], 'b': [[n[:4] for n in bar] for bar in m['bars']]})
    data.append({'id': re.sub(r'\d', '', f), 'n': j.get('lesson'), 'title': j['title'], 'meter': j.get('meter', '4/4'), 'bpm': TEMPO.get(f, 100), 'tunes': tunes})
page = open('listen_tpl.html').read().replace('/*DATA*/[]', json.dumps(data, ensure_ascii=False, separators=(',', ':')))
open(sys.argv[1], 'w').write(page); print('ok', len(page))
