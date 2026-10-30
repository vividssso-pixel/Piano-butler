#!/usr/bin/env python3
"""Build DO fix (on t791 -> t792): the opener's 'Bring with you' line (Build DO) took 30px from the opener's picture, and the
Chords picture re-laid itself as a tall stack (its caption then touched the frame). The line now sits in the QR row, to the
left of the QR, where the opener had empty space; an opener with no QR row keeps the line as its own block (hidden when the
QR row carries it)."""
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def R(old, new, n=1):
    global s
    c = s.count(old); assert c == n, (c, n, old[:120]); s = s.replace(old, new)

LINE = """<div data-term-print={@@} style={{fontSize:11.5,color:BK.muted,fontWeight:700,STYLE}}>{t('Bring with you: ', '가져올 것: ') + DICT_BRING[@@].filter(id => dictEarlier(id, @@)).map(id => dictName(DICT_BY_ID[id]) + ' (' + (LANG === 'ko' ? bkChapterNo(DICT_BY_ID[id].room) + '장' : 'ch. ' + bkChapterNo(DICT_BY_ID[id].room)) + ')').join(' · ')}</div>"""
old_page = LINE.replace('@@', 'chId').replace('STYLE', "marginTop:'auto'")
assert s.count(old_page) == 1
# the QR row carries the line
R("""    <div data-lb-drill style={{display:'flex',justifyContent:'flex-end',alignItems:'center',gap:8,marginTop:'auto'}}>
      <span style={{fontSize:10.5,color:BK.muted}}>{t('online', '온라인')}</span>""",
  """    <div data-lb-drill style={{display:'flex',justifyContent:'flex-end',alignItems:'center',gap:8,marginTop:'auto'}}>
      {DICT_BRING[id] && DICT_BRING[id].some(x => dictEarlier(x, id)) && """ + LINE.replace('id => dictEarlier(id, @@)', 'x => dictEarlier(x, @@)').replace('.map(id => dictName(DICT_BY_ID[id])', '.map(x => dictName(DICT_BY_ID[x])').replace("DICT_BY_ID[id].room", "DICT_BY_ID[x].room").replace('@@', 'id').replace('STYLE', "flex:1,minWidth:0,marginRight:'auto',lineHeight:1.35") + """}
      <span style={{fontSize:10.5,color:BK.muted}}>{t('online', '온라인')}</span>""")
# the page's own line stays for an opener without the QR row
R("""  .bk-page { padding-bottom: 11.5mm !important; }""",
  """  .bk-page { padding-bottom: 11.5mm !important; }
  .bk-body:has([data-lb-drill]) > [data-term-print] { display: none; }   /* Build DO fix: the QR row carries the line */""")
open(dst, 'w', encoding='utf-8').write(s)
print('ok', len(s))
