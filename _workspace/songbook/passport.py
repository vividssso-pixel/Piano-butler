# The Composer Passport (her 6 Nov 21:17: "명곡 여권"): one page at the back of the Lesson Book. Lesson 1 issues it; every
# lesson after that earns a stamp, a composer or a country for a folk tune. Reads each lesson's `composer` field.
# Usage: python3 passport.py out.html  (the lesson files are listed in ORDER)
import json, base64, sys
ORDER = ['buns', 'home', 'mary', 'ode', 'jingle', 'twinkle', 'frere', 'london', 'surprise', 'elise']
N, C, MUTE = '#26296b', '#e4572e', '#6d6f9c'
FD = 'node_modules/@fontsource/'
def b64(p): return base64.b64encode(open(p, 'rb').read()).decode()
FF = (f"@font-face{{font-family:'AH';font-weight:400;src:url(data:font/woff2;base64,{b64(FD + 'atkinson-hyperlegible/files/atkinson-hyperlegible-latin-400-normal.woff2')}) format('woff2')}}"
      f"@font-face{{font-family:'AH';font-weight:700;src:url(data:font/woff2;base64,{b64(FD + 'atkinson-hyperlegible/files/atkinson-hyperlegible-latin-700-normal.woff2')}) format('woff2')}}"
      f"@font-face{{font-family:'PF';font-weight:700;src:url(data:font/woff2;base64,{b64(FD + 'playfair-display/files/playfair-display-latin-700-normal.woff2')}) format('woff2')}}")
songs = [json.load(open(f + '.json')) for f in ORDER]

def stamp(s):   # a dashed circle to stamp or sticker, the lesson number above, the composer and song under it
    cp = s.get('composer', {}); name = cp.get('stamp', '?'); who = cp.get('name', ''); yrs = cp.get('years', '')
    return (f'<div class="st"><div class="sl">Lesson {s["lesson"]}</div>'
            f'<svg viewBox="0 0 120 120" class="ring"><circle cx="60" cy="60" r="54" fill="none" stroke="{N}" stroke-width="2" stroke-dasharray="6 5"/>'
            f'<circle cx="60" cy="60" r="44" fill="none" stroke="{N}" stroke-width="1" opacity=".35"/>'
            f'<text x="60" y="66" text-anchor="middle" font-family="PF" font-weight="700" font-size="{15 if len(name) > 8 else 18}" fill="{N}" opacity=".25">{name}</text></svg>'
            f'<div class="sn">{s["title"]}</div><div class="sw">{who}</div><div class="sy">{yrs}</div></div>')

grid = ''.join(stamp(s) for s in songs)
body = f'''<section class="pg"><div class="top"><span>THE PIANO BUTLER LESSON BOOK · LEVEL 0</span><span>MY COMPOSER PASSPORT</span></div><div class="rule"></div>
<div class="body">
<div class="kick">Issued in Lesson 1</div><h1>My Composer Passport</h1>
<p class="lead">Every song in this book was written by someone, somewhere. Each time you finish a lesson, your teacher stamps the circle (or you stick a sticker in it). Ten stamps, and you have met the people behind the music.</p>
<div class="who"><span>Name</span><span class="line"></span><span>Teacher</span><span class="line"></span></div>
<div class="grid">{grid}</div>
<div class="next"><div class="kick">Where have you heard it?</div><p>Each song's Listening page plays the original: the symphony, the song, the band. Scan the code on the lesson's first page.</p></div>
<div class="foot2"><b>Stamped by your teacher</b> when the song is played from beginning to end, both hands if the lesson asks for it, at turtle speed or faster. A country stamp means a folk song: nobody knows who first sang it.</div>
</div><div class="foot"><span>Passport</span></div></section>'''
css = f'''@page {{ size: A4; margin: 0 }} *{{box-sizing:border-box}} body{{margin:0;background:#e9e4d8;font-family:'AH',Arial,sans-serif;color:{N}}}
.pg{{width:794px;height:1123px;background:#fff;margin:0 auto 24px;position:relative;overflow:hidden;padding:42px 58px 0;page-break-after:always}}
.top{{display:flex;justify-content:space-between;font-size:9.5px;font-weight:700;letter-spacing:.16em;color:#8a8cb0}} .rule{{height:5px;border-top:1.5px solid {N};border-bottom:.6px solid {N};margin:7px 0 18px}}
.body{{height:965px;overflow:hidden;display:flex;flex-direction:column}} .foot{{position:absolute;left:0;right:0;bottom:30px;text-align:center}} .foot span{{display:inline-block;color:{N};font:700 13px 'AH',Arial;letter-spacing:.08em}}
.kick{{font-size:12px;font-weight:700;letter-spacing:.18em;text-transform:uppercase;color:{C}}} h1{{font-family:'PF',Georgia,serif;font-size:40px;line-height:1.1;margin:3px 0 8px;font-weight:700}}
.lead{{font-size:16.5px;line-height:1.5;margin:0 0 10px}}
.who{{display:grid;grid-template-columns:auto 1fr auto 1fr;gap:10px 12px;align-items:end;font-size:11.5px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:{C};margin:6px 0 18px}} .who .line{{border-bottom:1.5px solid {N};height:26px}}
.grid{{display:grid;grid-template-columns:repeat(5,1fr);gap:44px 16px;margin-top:22px}}
.st{{display:flex;flex-direction:column;align-items:center;text-align:center}} .sl{{font-size:11px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:{C};margin-bottom:4px}}
.ring{{width:124px;height:124px;display:block}} .sn{{font-family:'PF',Georgia,serif;font-weight:700;font-size:14.5px;margin-top:8px;line-height:1.2}} .sw{{font-size:12.5px;margin-top:3px;line-height:1.3}} .sy{{font-size:11px;color:{MUTE};margin-top:1px}}
.next{{margin-top:34px;border:1.5px solid rgba(38,41,107,.22);border-radius:10px;padding:12px 16px}} .next p{{margin:4px 0 0;font-size:14.5px;line-height:1.5}}
.foot2{{margin-top:auto;font-size:13.5px;line-height:1.5;color:#3d4080;border-top:1px solid rgba(38,41,107,.18);padding-top:10px;margin-bottom:8px}}
@media print {{ body{{background:#fff}} .pg{{margin:0}} }}'''
html = f'<!doctype html><html><head><meta charset="utf-8"><title>My Composer Passport</title><style>{FF}</style><style>{css}</style></head><body>{body}</body></html>'
open(sys.argv[1], 'w').write(html); print('ok', len(html))
