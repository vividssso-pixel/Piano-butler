# Worked first answers (her 4 Nov: children often don't know what to do). Applied to the built workbook HTML:
# for each exercise title, the first blank becomes the answer in red, or the right choice is ringed; the instruction gets 'The first is done.'
import re
def apply(html, table):
    pages = re.split(r'(?=<section class="pg")', html)
    seen = {}
    for pi, pg in enumerate(pages):
        if 'data-end="1"' in pg[:200]: continue
        for title, specs in table.items():
            start = 0
            while True:
                m = re.search(r'<span class="en">\d+</span><b>' + re.escape(title) + r'</b>', pg[start:])
                if not m: break
                at = start + m.end(); n = seen.get(title, 0); seen[title] = n + 1
                if n >= len(specs) or specs[n] is None: start = at; continue
                kind, val = specs[n]
                end = pg.find('<div class="ex2">', at); end = len(pg) if end < 0 else end
                seg = pg[at:end]
                if 'first is done' not in seg.lower() and 'first one is done' not in seg.lower() and 'first bar is done' not in seg.lower() and 'first row is done' not in seg.lower():
                    seg = re.sub(r'(<p class="how">.*?)(</p>)', lambda mm: mm.group(1) + ' The first is done.' + mm.group(2), seg, count=1)
                    hp = seg.find('</p>') + 4; head, body = seg[:hp], seg[hp:]   # answers go in the exercise body, never the instruction
                    acts = [(kind, val)] if kind != 'both' else val
                    for kd, vl in acts:
                        if kd == 'fill':
                            body = re.sub(r'<span class="(wl|ab|al(?: inl)?)"></span>', lambda mm: f'<span class="{mm.group(1)} hasdone"><b class="done2">{vl}</b></span>', body, count=1)   # the answer sits on its own line, so the cell keeps the same shape as the others
                        elif kd == 'ring':
                            body = body.replace(vl, f'<b class="done2 ringd">{vl}</b>', 1)
                    seg = head + body
                pg = pg[:at] + seg + pg[end:]; start = at + len(seg)
        pages[pi] = pg
    return ''.join(pages)
CSS = '.ringd{border:1.8px solid #e4572e;border-radius:50%;padding:1px 8px 3px} .wl.hasdone{display:inline-flex;align-items:flex-end;justify-content:center;width:auto;min-width:64px;padding:0 6px 3px;vertical-align:bottom} .hasdone>.done2{line-height:1;white-space:nowrap} .ab.hasdone{display:inline-flex;align-items:center;justify-content:center} .al.hasdone{display:inline-flex;align-items:flex-end;justify-content:center;padding-bottom:2px}'
