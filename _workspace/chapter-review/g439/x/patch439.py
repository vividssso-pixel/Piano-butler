#!/usr/bin/env python3
# Phase 439 (A8 and the Korean line breaks; her 2026-10-12 14:52 '내 생각엔 줄을 잘 정리해야할 것 같아. 읽기 쉽게'): a double
# dash stays with the word before it and never splits in two; Korean lines break between words, not inside them.
import sys
src, out = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    c = s.count(a)
    if c != n: raise SystemExit('count %d != %d for: %s' % (c, n, a[:100]))
    s = s.replace(a, b)
rep("""    .fade-up { animation: fadeUp 0.18s ease both; }
""", """    .fade-up { animation: fadeUp 0.18s ease both; }
    /* Phase 439: Korean lines break between words, never inside one (a word too long for its box may still break) */
    html[lang="ko"] body { word-break: keep-all; overflow-wrap: anywhere; }
""")
rep("""  LANG = lang;
  function toggleLang() {""", """  LANG = lang;
  try { document.documentElement.lang = lang; } catch (e) {}   // Phase 439: the Korean line rule (and the browser's Hangul font) follow the switch
  function toggleLang() {""")
rep("""ReactDOM.createRoot(document.getElementById('root')).render(""", """// Phase 439 (A8): ' -- ' is the house dash. It stays with the word before it (a no-break space) and its two strokes never
// part (a word joiner): every text node that shows on the page is fixed as it arrives or changes.
const PB_DASH = / --(?=[\\s\\u00a0.,;:!?)\\]'"\\u2019\\u201d]|$)/g;
function pbGlue(node) {
  if (node.nodeType === 3) { const v = node.nodeValue; if (v && v.indexOf(' --') >= 0) { const f = v.replace(PB_DASH, '\\u00a0-\\u2060-'); if (f !== v) node.nodeValue = f; } return; }
  if (node.nodeType !== 1 || node.nodeName === 'SCRIPT' || node.nodeName === 'STYLE') return;
  const w = document.createTreeWalker(node, NodeFilter.SHOW_TEXT); let n; while ((n = w.nextNode())) pbGlue(n);
}
try { new MutationObserver(ms => ms.forEach(m => { if (m.type === 'characterData') pbGlue(m.target); else m.addedNodes.forEach(pbGlue); })).observe(document.getElementById('root'), { childList: true, subtree: true, characterData: true }); } catch (e) {}
ReactDOM.createRoot(document.getElementById('root')).render(""")
open(out, 'w', encoding='utf-8').write(s); print('439 ok')
