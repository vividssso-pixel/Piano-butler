#!/usr/bin/env python3
# Phase 442: her 15:56-15:58 notes. (1) The rabbit back in two pictures: chapter 1's puppet (he holds the strings) and
# chapter 2's opener (he stands between the houses). (2) A floor's rooms count from the bottom left: 1 2 3 below, 4 5 6
# above. (3) The front door opens again on every page load (the house is remembered only until the page reloads).
#   python3 patch442.py <in.src.html> <out.src.html> <old.src.html with the rabbit puppet>
import sys, json
src, dst, old = sys.argv[1], sys.argv[2], sys.argv[3]
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    c = s.count(a)
    if c != n: raise SystemExit('found %d (want %d): %s' % (c, n, a[:100]))
    s = s.replace(a, b)
# (1a) the puppet with the rabbit holding the control bar (Phase 369's drawing), the ground line navy as since Phase 425
o = open(old, encoding='utf-8').read()
i = o.index('\n"puppet": "'); j = o.index('\n', i + 2); old_line = o[i + 1:j]
i = s.index('\n"puppet": "'); j = s.index('\n', i + 2); cur_line = s[i + 1:j]
assert old_line.endswith(',') == cur_line.endswith(',')
svg = json.loads('{' + old_line.rstrip(',') + '}')['puppet']
assert svg.count('stroke="#bdb7a6"') == 1 and 'viewBox="0 0 270 214"' in svg
svg = svg.replace('stroke="#bdb7a6"', 'stroke="rgba(38,41,107,0.4)"')
new_line = '"puppet": ' + json.dumps(svg, ensure_ascii=False) + (',' if cur_line.endswith(',') else '')
rep(cur_line, new_line)
# (1b) chapter 2's opener: the rabbit on the ground between the houses again
rep("    return [...fsCoverShapes({ letters: false })];   // Phase 420: no rabbit in the lesson pictures (he stays in the REMEMBER band)",
    "    return [...fsCoverShapes({ letters: false }), { k: 'raw', svg: rabbit }];   // Phase 442 (her 15:56): the rabbit is back between the houses")
rep('label="A small house of keys and a big house on the ground; the sea and a turtle at the low end, clouds and a bird at the high end"',
    'label="The rabbit butler stands on the ground between a small house of keys and a big house; the sea and a turtle at the low end, clouds and a bird at the high end"')
# (2) rooms from the bottom left (her 15:58 '순서가 아래 왼쪽부터 1 2 3 이렇게 되야 맞는거 아닌가?'): row 0 is the lowest
rep("""    st.ids.forEach((id, j) => {
      const r = Math.floor(j / c), cc = j - r * c, rw = rwOf(j);
      body += thRoom(view, state, id, RX0 + cc * rw, yy + LH + r * rh, rw, rh, fs, out, o.dimNew, lay);""",
"""    const nr = Math.ceil(n / c);   // Phase 442: the first rooms on the lowest row, counted from the bottom left -- you climb the house
    st.ids.forEach((id, j) => {
      const r = Math.floor(j / c), cc = j - r * c, rw = rwOf(j);
      body += thRoom(view, state, id, RX0 + cc * rw, yy + LH + (nr - 1 - r) * rh, rw, rh, fs, out, o.dimNew, lay);""")
# (3) the door on every page load (her 15:58 '다시 웹페이지 로드했을 때 문열수있게'): in memory, not sessionStorage
rep("const HOUSE_IN_KEY = 'pb_house_in_v1';   // this session has come in through the door",
    "let houseCameIn = false;   // came in through the door since this page loaded (Phase 442: a reload shows the door again)")
rep("  const [inside, setInside] = useState(() => { try { return sessionStorage.getItem(HOUSE_IN_KEY) === '1'; } catch (e) { return false; } });",
    "  const [inside, setInside] = useState(() => houseCameIn);")
rep("setInside(true); try { sessionStorage.setItem(HOUSE_IN_KEY, '1'); } catch (e) {} }", "setInside(true); houseCameIn = true; }")
rep("in, the map shows the house straight away for the rest of the session.", "in, the map shows the house straight away until the page is loaded again (then the door again, Phase 442).")
rep("your chapter in coral -- the same order as the app's house, level 1 at the top.", "your chapter in coral -- level 1 at the top, like a list.")
open(dst, 'w', encoding='utf-8').write(s); print('442 applied')
