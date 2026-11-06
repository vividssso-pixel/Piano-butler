#!/usr/bin/env python3
# Phase 420 on the site: the guide drawings and the chapter 3 sample worksheet with crowns instead of faces.
#   python3 site421.py <repo root> <this x dir>
import sys, os, shutil
root, x = sys.argv[1], sys.argv[2]
for ch, names in [('first-steps', ['hero']), ('note-names', ['who-lives']), ('staff', ['hero', 'kings-five', 'queens-five', 'same-key'])]:
    for n in names:
        shutil.copyfile(os.path.join(x, 'svg', ch, n + '.svg'), os.path.join(root, 'tools/lessons/svg', ch, n + '.svg')); print('svg', ch, n)
shutil.copyfile(os.path.join(x, 'img/note-names-worksheet.jpg'), os.path.join(root, 'lessons/img/note-names-worksheet.jpg')); print('img lessons/img/note-names-worksheet.jpg')
shutil.copyfile(os.path.join(x, 'img/wb-note-names.jpg'), os.path.join(root, 'printables/img/wb-note-names.jpg')); print('img printables/img/wb-note-names.jpg')
