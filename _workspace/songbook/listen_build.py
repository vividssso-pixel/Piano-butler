# Build listen.html: the page the lesson book's QR codes open (thepianobutler.com/listen.html#<song>).
# It plays each lesson's tune (and its More to play tunes) from the same data the book is engraved from.
import json, re, sys
SONGS = ['buns', 'home', 'mary', 'ode', 'jingle', 'twinkle', 'frere', 'london', 'surprise', 'elise']   # her 6 Nov 21:25: the whole songs, Goin' Home, Twinkle and Für Elise in   # hb.json (Happy Birthday) waits for Level 1, the G position
TEMPO = {'hb': 96, 'jingle': 116, 'home': 72, 'ode': 100, 'twinkle': 96, 'frere': 96, 'london': 104, 'surprise': 92, 'elise': 84}
data = []
for f in SONGS:
    j = json.load(open(f + '.json'))
    tunes = [{'t': 'The song', 'b': [[n[:4] for n in bar] for bar in j['bars']]}]
    for m in j.get('more', []): tunes.append({'t': m['title'], 'bpm': m.get('bpm'), 'b': [[n[:4] + ([n[6]] if len(n) > 6 else []) for n in bar] for bar in m['bars']]})
    data.append({'id': re.sub(r'\d', '', f), 'n': j.get('lesson'), 'title': j['title'], 'meter': j.get('meter', '4/4'), 'bpm': TEMPO.get(f, 100), 'tunes': tunes, 'band': j.get('band'), 'piano': j.get('piano'), 'ens': j.get('ens')})
page = open('listen_tpl.html').read().replace('/*DATA*/[]', json.dumps(data, ensure_ascii=False, separators=(',', ':')))
open(sys.argv[1], 'w').write(page); print('ok', len(page))
