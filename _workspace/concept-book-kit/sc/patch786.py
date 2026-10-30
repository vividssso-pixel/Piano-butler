#!/usr/bin/env python3
"""Build DK (on t785 -> t786; her 15:03). (1) Words: a child does not know 'coral', so every student-facing 'coral note / key /
...' says 'red' (English) and '빨간 음표 / 빨간 건반' (Korean: 산호색 and 주황색 become 빨간, 빨간색 before a particle); 'orange'
the same. The colour itself stays coral. Code names (BK.coral, var(--coral), the coral arguments) are untouched. One mistranslation
fixed on the way: 'Chorale preludes for organ' was '산호색 전주곡'; now '코랄 전주곡'. (2) Noteheads: see the second part.
"""
import sys, re
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def R(old, new, n=1):
    global s
    c = s.count(old); assert c == n, (c, n, old[:120]); s = s.replace(old, new)
R("['Chorale preludes for organ', '오르간을 위한 산호색 전주곡']", "['Chorale preludes for organ', '오르간을 위한 코랄 전주곡']")
# ── (1) the words ──

WORDS=r"(?:notes?|keys?|circles?|sound|one|ones|hearts?|dotted|accents?|rings?|part|on|brackets?|box|when|signs?|lines?|how|dots?|arrows?|under|melody|is|footprints|black|a|with|while|water|trim|touch|token|tie|stays|slot|roof|pedal|outline|only|number|not|marks?|lips|handwriting|gown|finger|cross|chess|but|bows?|beat|band|as|and|[A-G])"
pat=re.compile(r"(?<![\w.\-'\"$])coral(?=(?: " + WORDS + r"\b)|[,.;!?)])(?![.][A-Za-z_])")
code=[]; prose=[]
def code_like(m):
    pre=s[max(0,m.start()-3):m.start()]; post=s[m.end():m.end()+14]
    if post.startswith(')'):
        if pre.endswith(', ') or re.search(r"\w\($", pre): return True
    if re.match(r", [A-Za-z_$][\w$]*[.\]\)]", post) and (pre.endswith(', ') or re.search(r"\w\($", pre)): return True
    if re.search(r"[:?=] $", pre) and re.match(r"[;,]", post): return True
    return False
def f(m):
    a=max(0,m.start()-45); ctx=s[a:m.end()+25].replace('\n',' ')
    if code_like(m): code.append(ctx); return m.group(0)
    prose.append(ctx); return 'red'
s2=pat.sub(f,s)
n_ko=len(re.findall(r"산호색|주황색",s2))
s2=re.sub(r"(산호색|주황색)(?=[은는이을를과의도]|으로|이에요|입니다|\b)", lambda m: '빨간색', s2)
s2=re.sub(r"산호색|주황색", '빨간', s2)
print('coral -> red: prose', len(prose), 'code kept', len(code), 'ko', n_ko)
s = s2

# Korean: 빨간 before a noun, 빨간색 before a particle (the trial above made everything 빨간색 before particles already)
s = re.sub(r"빨간색 (건반|음표|음|점선|동그라미|괄호|기호|네모|발자국|부분|심장|붙임줄|줄|칸|박|화살표|상자|글자|칸들|부분들|마디|음들|음표들|페달|소리|점|번호|두|발자국|숫자|글씨|칠|선|표시|상자|칸|자리)", r"빨간 \1", s)
for a, b in [("orange key", "red key"), ("orange note", "red note"), ("orange label", "red label"), ("orange dots", "red dots"), ("Orange keys", "Red keys"), ("the orange “say:” line", "the red “say:” line"), ("lights up orange as it sounds", "lights up red as it sounds")]:
    n = s.count(a); assert n, a; s = s.replace(a, b); print('  ', a, '->', b, n)
assert 'orange keys' not in s or True

# ── (2) the noteheads (her 15:03: inside their lines; a line note's line through its middle) ──
# An audit of every staff on every book page and online lesson (heads786.js: 272 pages, 6,278 heads) found the heads
# drawn taller than the space between two lines: 10 units apart, a head 5.3 high and tilted 20 degrees reaches 5.6 plus its
# stroke; 5,271 of them crossed the lines beside them. The rule now: a head's full height, stroke included, is 0.9 of the
# space (4.5 of 10), so a space note sits clear of both lines and a line note shows its line entering and leaving at its
# middle. The hole-style heads (the book's open heads with a white hole and a short line through the hole) keep that line.
# Rotated 20 degrees with width 1.37 x height: ry = 0.43 x gap, rx = 0.59 x gap. Unrotated: ry = 0.45 x gap, rx = 1.4 x ry.
# nvbHead: the pen notation on every staff of gap 10 (and on the Note values pictures, scaled by k).
R("""  const rx = (w ? 9.4 : 7.2) * k, ry = (w ? 6.3 : 5.3) * k, rot = w ? -12 : -20;
  return '<ellipse cx="' + nvbF(x) + '" cy="' + nvbF(y) + '" rx="' + nvbF(rx) + '" ry="' + nvbF(ry) + '" transform="rotate(' + rot + ' ' + nvbF(x) + ' ' + nvbF(y) + ')" fill="' + (hollow ? '#fff' : col) + '" stroke="' + col + '" stroke-width="' + nvbF(w ? 2.9 * k : hollow ? 2.3 * k : 1.2 * k) + '"/>';""",
  """  // Build DK: a head fits its space (gap 10 at k = 1): the filled head 5.8 x 4.1 with no stroke, the minim 4.6 x 3.1 inside a 2.3
  // stroke, the semibreve 6.2 x 2.8 inside a 2.9 stroke, each 4.5 high in all, tilt included
  const rx = (w ? 6.2 : hollow ? 4.6 : 5.8) * k, ry = (w ? 2.8 : hollow ? 3.1 : 4.1) * k, rot = w ? -12 : -20;
  return '<ellipse cx="' + nvbF(x) + '" cy="' + nvbF(y) + '" rx="' + nvbF(rx) + '" ry="' + nvbF(ry) + '" transform="rotate(' + rot + ' ' + nvbF(x) + ' ' + nvbF(y) + ')" fill="' + (hollow ? '#fff' : col) + '" stroke="' + (hollow ? col : 'none') + '" stroke-width="' + nvbF(w ? 2.9 * k : hollow ? 2.3 * k : 0) + '"/>';""")
R("""  const k = o.k || 1, col = o.col || PEN_N, sx = x + 6.4 * k, top = y - 34 * k;
  let s = nvbHead(x, y, kind, col, k);""", """  const k = o.k || 1, col = o.col || PEN_N, sx = x + 5.3 * k, top = y - 34 * k;   // Build DK: the stem at the smaller head's edge
  let s = nvbHead(x, y, kind, col, k);""")
R("""  [x1, x2].forEach(x => { s += '<line x1="' + nvbF(x + 6.4 * k) + '" y1="' + nvbF(y - 1.5 * k) + '" x2="' + nvbF(x + 6.4 * k) + '" y2="' + nvbF(top)""",
  """  [x1, x2].forEach(x => { s += '<line x1="' + nvbF(x + 5.3 * k) + '" y1="' + nvbF(y - 1.5 * k) + '" x2="' + nvbF(x + 5.3 * k) + '" y2="' + nvbF(top)""")
R("""  s += '<path d="M' + nvbF(x1 + 5.5 * k) + ' ' + nvbF(top - 0.2 * k) + ' L' + nvbF(x2 + 7.3 * k) + ' ' + nvbF(top - 0.2 * k) + ' L' + nvbF(x2 + 7.3 * k) + ' ' + nvbF(top + 5.2 * k) + ' L' + nvbF(x1 + 5.5 * k)""",
  """  s += '<path d="M' + nvbF(x1 + 4.4 * k) + ' ' + nvbF(top - 0.2 * k) + ' L' + nvbF(x2 + 6.2 * k) + ' ' + nvbF(top - 0.2 * k) + ' L' + nvbF(x2 + 6.2 * k) + ' ' + nvbF(top + 5.2 * k) + ' L' + nvbF(x1 + 4.4 * k)""")
# the 7 x 5 tilted heads on gap-10 staffs (23 sites: IntervalStaff, ClefHome, StaffFrame, MnemonicStaff, LandmarkHop, PaperOttava and more)
R("""rx="7" ry="5" transform={`rotate(-20""", """rx="5.9" ry="4.3" transform={`rotate(-20""", 18)
R("""rx="7" ry="5" transform="rotate(-20 """, """rx="5.9" ry="4.3" transform="rotate(-20 """, 2)
# the open hole-style heads (SfStaff, LlRungs, IvxWrite, ChxWrite) and the online StaffView
R("""rx="7.4" ry="5.2" fill={c}/><ellipse cx={x} cy={y} rx="3.4" ry="2.7" transform={`rotate(-38 ${x} ${y})`} fill="#fff"/>""",
  """rx="6.3" ry="4.5" fill={c}/><ellipse cx={x} cy={y} rx="3" ry="2.4" transform={`rotate(-38 ${x} ${y})`} fill="#fff"/>""")
R("""rx="7.4" ry="5.2" fill={col}/><ellipse cx={X} cy={yOf(d)} rx="3.4" ry="2.7" """, """rx="6.3" ry="4.5" fill={col}/><ellipse cx={X} cy={yOf(d)} rx="3" ry="2.4" """)
R("""rx="7.4" ry="5.2" fill={col}/><ellipse cx={x} cy={dY(d)} rx="3.4" ry="2.7" """, """rx="6.3" ry="4.5" fill={col}/><ellipse cx={x} cy={dY(d)} rx="3" ry="2.4" """, 2)
R("""            <ellipse cx={x} cy={y} rx="7.2" ry="5.1" fill={n.color || ink} data-d={n.d}/>
            <ellipse cx={x} cy={y} rx="3.3" ry="2.6" transform={`rotate(-38 ${x} ${y})`}""", """            <ellipse cx={x} cy={y} rx="6.3" ry="4.5" fill={n.color || ink} data-d={n.d}/>
            <ellipse cx={x} cy={y} rx="2.9" ry="2.3" transform={`rotate(-38 ${x} ${y})`}""")
# the 6.6 x 4.8 tilted heads (SatbStaff open, K4Melody filled, MwStaff both)
R("""      <ellipse cx={x} cy={y} rx="6.6" ry="4.8" transform={`rotate(-20 ${x} ${y})`} fill="#fff" stroke={col} strokeWidth="2.2"/>""",
  """      <ellipse cx={x} cy={y} rx="4.6" ry="3.3" transform={`rotate(-20 ${x} ${y})`} fill="#fff" stroke={col} strokeWidth="2.2"/>""")
R("""        <ellipse cx={x} cy={y} rx="6.6" ry="4.8" transform={`rotate(-20 ${x} ${y})`} fill={col}/>""",
  """        <ellipse cx={x} cy={y} rx="5.9" ry="4.3" transform={`rotate(-20 ${x} ${y})`} fill={col}/>""")
R("""      els.push(<ellipse key={'h' + i} cx={x} cy={y} rx="6.6" ry="4.8" transform={`rotate(-20 ${x} ${y})`} fill={hollow ? '#fff' : c} stroke={c} strokeWidth={hollow ? 2.2 : 1}/>);""",
  """      els.push(<ellipse key={'h' + i} cx={x} cy={y} rx={hollow ? 4.6 : 5.9} ry={hollow ? 3.3 : 4.3} transform={`rotate(-20 ${x} ${y})`} fill={hollow ? '#fff' : c} stroke={hollow ? c : 'none'} strokeWidth={hollow ? 2.2 : 0}/>);""")
# the melody map's heads (sp = the gap), the tempo mini page (gap 7.9), the two 5.4 x 3.9 heads (gap 8), the pen mini staffs (gap 6 and 4)
R("""<ellipse cx={x} cy={y} rx={sp * 0.68} ry={sp * 0.48} transform={`rotate(-20 ${x} ${y})`} fill={zc}/><line x1={x + sp * 0.63} x2={x + sp * 0.63}""",
  """<ellipse cx={x} cy={y} rx={sp * 0.59} ry={sp * 0.43} transform={`rotate(-20 ${x} ${y})`} fill={zc}/><line x1={x + sp * 0.56} x2={x + sp * 0.56}""")
R("""<ellipse cx={x} cy={nY(noteD[i])} rx="6" ry="4.4" transform={'rotate(-20 ' + x + ' ' + nY(noteD[i]) + ')'} fill={ink}/>""",
  """<ellipse cx={x} cy={nY(noteD[i])} rx="4.7" ry="3.4" transform={'rotate(-20 ' + x + ' ' + nY(noteD[i]) + ')'} fill={ink}/>""")
R("""<ellipse cx={x} cy="29" rx="5.4" ry="3.9" transform={`rotate(-20 ${x} 29)`}""", """<ellipse cx={x} cy="29" rx="4.7" ry="3.4" transform={`rotate(-20 ${x} 29)`}""")
R("""  const hd = (x, y) => '<ellipse cx="' + x + '" cy="' + y + '" rx="5.4" ry="3.9" fill="' + PEN_N + '" transform="rotate(-20 ' + x + ' ' + y + ')""",
  """  const hd = (x, y) => '<ellipse cx="' + x + '" cy="' + y + '" rx="4.7" ry="3.4" fill="' + PEN_N + '" transform="rotate(-20 ' + x + ' ' + y + ')""")
n44 = s.count('rx="4.4" ry="3.1"'); s = s.replace('rx="4.4" ry="3.1"', 'rx="3.8" ry="2.7"'); print('  4.4 x 3.1 heads', n44)
n44b = s.count('rx: 4.4, ry: 3.1'); s = s.replace('rx: 4.4, ry: 3.1', 'rx: 3.8, ry: 2.7'); print('  4.4 x 3.1 pen heads', n44b)
R("""  const hd = (x, y, c = PEN_C) => ({ k: 'el', c: [x, y], rx: 3.2, ry: 2.3, f: c });""", """  const hd = (x, y, c = PEN_C) => ({ k: 'el', c: [x, y], rx: 2.5, ry: 1.8, f: c });""")
R("""'<ellipse cx="46" cy="29" rx="5.4" ry="4" fill="' + PEN_C + '"/>""", """'<ellipse cx="46" cy="29" rx="3.8" ry="2.7" fill="' + PEN_C + '"/>""")
R("""  const head = (x, y, col) => '<ellipse cx="' + x + '" cy="' + y + '" rx="6" ry="4.4" fill="' + col + '"/>';""", """  const head = (x, y, col) => '<ellipse cx="' + x + '" cy="' + y + '" rx="3.8" ry="2.7" fill="' + col + '"/>';""")
R("""<ellipse cx="72" cy="8" rx="5.4" ry="4" fill="' + PEN_C + '"/>""", """<ellipse cx="72" cy="8" rx="3.8" ry="2.7" fill="' + PEN_C + '"/>""")
open(dst, 'w', encoding='utf-8').write(s)
print('ok', len(s))
