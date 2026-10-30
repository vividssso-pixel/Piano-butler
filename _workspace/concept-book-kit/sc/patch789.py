#!/usr/bin/env python3
"""Build DN (on t788 -> t789; her 21:41 'go with your recommendation' on call 32): the Toolbox tab goes. Every activity opens
from its chapter, the Practice tab, a room's 'Make your own' card or the Home (checked: 316 activities, none only in the
Toolbox), so the teacher's tabs are Home · Chapters · Books · Printables · Practice. Old addresses (?view=toolbox) and
'← Toolbox' go to the Home; a tool found with the Find button goes back to the Home; the one Home category that still sent
people to the Toolbox (Practice, under 'Beside the piano') goes to the Practice tab. Kits are retired with the tab (a device's
kit data stays; a kit link still opens its kit, and goes back to the Home). The Toolbox's Students button opened a view that
no longer renders (the dashboard took it over), so it goes too; the header's Dashboard link is the way to the students.
"""
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def R(old, new, n=1):
    global s
    c = s.count(old); assert c == n, (c, n, old[:120]); s = s.replace(old, new)

# the address: ?view=toolbox lands on the Home (and ?view=toolbox&sec=books on Books, as before)
R("""p.get('view') === 'printables' ? 'printables' : p.get('view') === 'toolbox' ? 'toolbox' :""",
  """p.get('view') === 'printables' ? 'printables' : p.get('view') === 'toolbox' ? 'home' :""")
# the tab row
R("""...(booksUnlocked() ? [['books', t('Books', '책')], ['printables', t('Printables', '교구')]] : []), ['toolbox', t('Toolbox', '도구함')],""",
  """...(booksUnlocked() ? [['books', t('Books', '책')], ['printables', t('Printables', '교구')]] : []),""")
R("""color:(st.view === v || (v === 'path' && st.view === 'chapters') || (T && v === 'toolbox' && st.view === 'tools' && st.ret === 'toolbox') || (T && v === 'home' && st.view === 'tools' && st.ret === 'home')) ?""",
  """color:(st.view === v || (v === 'path' && st.view === 'chapters') || (T && v === 'home' && st.view === 'tools' && (st.ret === 'home' || st.ret === 'toolbox'))) ?""")
# the Home category that still went to the Toolbox: the Practice tab instead
R("""            else { go({ view: 'toolbox' }); setTimeout(() => { try { const el = document.getElementById('cat-' + c.id); if (el) el.scrollIntoView(); } catch (e) {} }, 300); }""",
  """            else go({ view: 'practice', tool: null });   // Build DN: no Toolbox; the Practice tab holds these""")
# in a chapter, jumping, the address
R("""  const inChapter = (st.view === 'path' || st.view === 'chapters' || st.view === 'toolbox' || st.view === 'books' || st.view === 'printables' || (HM && st.view === 'home')) && !!st.drill;""",
  """  const inChapter = (st.view === 'path' || st.view === 'chapters' || st.view === 'books' || st.view === 'printables' || (HM && st.view === 'home')) && !!st.drill;""")
R("""      else if (!st.drill) p.set('view', (st.view === 'chapters' || st.view === 'toolbox') ? st.view : 'path');""",
  """      else if (!st.drill) p.set('view', st.view === 'chapters' ? st.view : 'path');""")
R("""update({ view: (T && (st.view === 'toolbox' || st.view === 'chapters' || st.view === 'books' || st.view === 'printables')) ? st.view : 'path',""",
  """update({ view: (T && (st.view === 'chapters' || st.view === 'books' || st.view === 'printables')) ? st.view : 'path',""")
# a tool found with Find goes back to the Home
R("""onJump={(id) => { setFindOpen(false); update({ view: 'tools', tool: id, kit: null, ret: 'toolbox' });""",
  """onJump={(id) => { setFindOpen(false); update({ view: 'tools', tool: id, kit: null, ret: 'home' });""")
# a kit's way back, and a tool's last-resort way back
R("""onClick={() => update({ view: 'toolbox', kit: null, kn: '' })}>{t('← Toolbox', '← 도구함')}</button>}<KitVie""",
  """onClick={() => update({ view: 'home', kit: null, kn: '' })}>{t('← Home', '← 홈')}</button>}<KitVie""")
R("""toolBackCh ? '← ' + bkChapterName(toolBackCh) : '← Toolbox'}""", """toolBackCh ? '← ' + bkChapterName(toolBackCh) : homeBack}""")
R("""update({ tool: null, view: (st.view === 'practice' ? null : st.ret) || (T && st.view === 'tools' ? 'toolbox' : st.view), ret: null })}""",
  """update({ tool: null, view: (st.view === 'practice' ? null : st.ret === 'toolbox' ? 'home' : st.ret) || (T && st.view === 'tools' ? 'home' : st.view), ret: null })}""")
# the tab's screen
i = s.index("""          : T && st.view === 'toolbox'
            ? <ToolboxTab onOpenTool=""")
j = s.index("""                onChapter={jumpToChapter}/>
""", i) + len("""                onChapter={jumpToChapter}/>
""")
s = s[:i] + s[j:]
# a locked tool (a student's link) shows no generic way back, as before; the generic label is now the Home's
R("""function ToolView({ id, locked, onBack, onChapter, backLabel = '← Toolbox', backAlways }) {""", """function ToolView({ id, locked, onBack, onChapter, backLabel = '← Home', backAlways }) {   // Build DN: the Home is the generic way back""")
R("""      {(!locked || backAlways || backLabel !== '← Toolbox') && <button className="ghost-btn" data-testid="tool-back""" + '"', """      {(!locked || backAlways || backLabel !== '← Home') && <button className="ghost-btn" data-testid="tool-back""" + '"')
open(dst, 'w', encoding='utf-8').write(s)
print('ok', len(s))
