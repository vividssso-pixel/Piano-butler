# The sample sheet for the classical street: before/after, then close-ups of every building (SVG inlined so the fonts apply)
import json, re
from common import FONTS
new = open('streetc.svg').read(); old = open('street-before.svg').read(); R = {int(k): v for k, v in json.load(open('streetc-ranges.json')).items()}
def crop(svg, y0, y1, w, x0=0, x1=360):
    inner = svg[svg.index('>') + 1:svg.rindex('</svg>')]
    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="%.1f %.1f %.1f %.1f" style="width:%s;height:auto;display:block">%s</svg>' % (x0, y0, x1 - x0, y1 - y0, w, inner)
def full(svg, h): return svg.replace('<svg ', '<svg style="height:%s;width:auto;display:block" ' % h, 1)
TITLE = ['The Lodge', 'The Library', 'The Clock Tower', 'The Conservatory', 'The Academy', 'The Theatre', 'The Museum']
WHAT = ['carved bargeboards, a finial, quoins, chimneys with pots', 'a balustrade with urns over a full cornice, pilasters at the corners',
        'a spire, an arcaded belfry, a clock stage between pilasters', 'a palm house: curved glass shoulders on iron ribs, a raised lantern, a low stone wall',
        'a temple front: a pediment with an oculus, Ionic columns, steps', 'a mansard roof with round dormers, an arched attic with a lyre, an arcade on columns',
        'a ribbed dome on an arcaded drum, a lantern, a balustrade, quoins']
css = '''<style>
@page { size: A4 landscape; margin: 0; }
html, body { margin: 0; background: #fff; color: #26296b; font-family: Inter, sans-serif; }
.sheet { width: 297mm; height: 210mm; box-sizing: border-box; padding: 9mm 12mm 8mm; break-after: page; overflow: hidden; display: flex; flex-direction: column; }
.top { display: flex; justify-content: space-between; align-items: baseline; font-size: 9px; font-weight: 700; letter-spacing: .16em; text-transform: uppercase; color: #6d6f9c; border-bottom: 1.4px solid #26296b; padding-bottom: 4px; }
.top b { color: #26296b; font-weight: 800; }
.cap { display: flex; align-items: baseline; gap: 12px; margin: 6px 0 6px; }
.cap h2 { font-family: 'Playfair Display', Georgia, serif; font-weight: 900; font-size: 21px; margin: 0; }
.cap span { font-size: 12px; color: #6d6f9c; }
.row { flex: 1; min-height: 0; display: flex; gap: 8mm; align-items: flex-start; justify-content: center; }
figure { margin: 0; display: flex; flex-direction: column; align-items: center; gap: 4px; }
figcaption { font-size: 9.5px; font-weight: 800; letter-spacing: .18em; color: #6d6f9c; text-transform: uppercase; }
figure.now figcaption { color: #26296b; }
figure .box { border: 1px solid #e3ddcd; padding: 3mm; }
.notes { width: 82mm; font-size: 12px; line-height: 1.5; }
.notes p { margin: 0 0 8px; } .notes b { font-weight: 800; }
.notes ul { margin: 4px 0 10px; padding-left: 16px; } .notes li { margin-bottom: 3px; }
.what { font-size: 10.5px; color: #6d6f9c; max-width: 70mm; text-align: center; line-height: 1.35; }
</style>'''
H = '170mm'
p1 = '''<section class="sheet"><div class="top"><span><b>Piano Butler</b> · the street, drawn classically</span><span>1 / 5</span></div>
<div class="cap"><h2>Simple lines, classical shapes</h2><span>Lines only, navy on white. Coral = where you are, green = done. The same moment: chapters 1-7 done, chapter 8 (Pulse) where you are.</span></div>
<div class="row"><figure><figcaption>Round 1</figcaption><div class="box">%s</div></figure>
<figure class="now"><figcaption>Classical</figcaption><div class="box">%s</div></figure>
<div class="notes"><p><b>No colour added.</b> The classicism comes from the shapes -- the vocabulary of a real Victorian street:</p>
<ul><li><b>Entablatures</b> on every building: a cornice with dentils, a frieze with the building's name in spaced capitals, an architrave.</li>
<li><b>Windows with architraves</b>: a moulded surround, a keystone on each arch, a sill on two little brackets.</li>
<li><b>Quoins</b> (the stepped corner stones) on the Lodge, the Clock Tower and the Museum; pilasters on the Library.</li>
<li><b>Columns with bases and capitals</b> -- Ionic at the Academy, slim ones between the Theatre's arches.</li>
<li><b>Balustrades with turned balusters and urns</b>; finials on the roofs; a plinth under every building.</li></ul>
<p>Every building shares one storey -- the plaque, the windows, the numbers and names -- so the street reads the same all the way up; only the tops change.</p>
<p>The plaque, the chess-square numbers, the names and Clara's place are unchanged.</p></div></div></section>''' % (full(old, H), full(new, H))
def fig(k, w='122mm'): return '<figure class="now"><figcaption>%d · %s</figcaption><div class="box">%s</div><div class="what">%s</div></figure>' % (k + 1, TITLE[k], crop(new, R[k][0], R[k][1], w), WHAT[k])
def sheet(n, title, sub, body): return '<section class="sheet"><div class="top"><span><b>Piano Butler</b> · the street, drawn classically</span><span>%d / 5</span></div><div class="cap"><h2>%s</h2><span>%s</span></div><div class="row">%s</div></section>' % (n, title, sub, body)
c = R[2]; zoom = crop(new, c[1] - 22 - 136, c[1] - 22 - 9, '100mm', 30, 176)
p4 = sheet(5, 'Close up', 'The top of the street, and one window at full size.', fig(6) + '<figure class="now"><figcaption>One window, enlarged</figcaption><div class="box">%s</div><div class="what">A moulded arch with a keystone, a sill on two brackets; the number on a chess square, the name under it. Coral and Clara mark where you are.</div></figure>' % zoom)
html = '<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Classical street</title>%s%s</head><body>%s%s%s%s</body></html>' % (FONTS, css, p1, sheet(2, 'Close up', 'From the bottom of the street.', fig(0) + fig(1)) + sheet(3, 'Close up', 'Going up.', fig(2) + fig(3)), sheet(4, 'Close up', 'Going up.', fig(4) + fig(5)), p4)
open('streetc-sheet.html', 'w').write(html)
