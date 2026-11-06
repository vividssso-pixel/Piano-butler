#!/usr/bin/env python3
# Phase 447 on the site: the guide pages' drawings and the ledger-lines worksheet pictures with the clefs on their lines.
#   python3 site447.py <repo root> <this x dir>
import sys, os, shutil, glob
root, x = sys.argv[1], sys.argv[2]
for f in sorted(glob.glob(os.path.join(x, 'svg', '*', '*.svg'))):
    rel = os.path.relpath(f, os.path.join(x, 'svg')); d = os.path.join(root, 'tools/lessons/svg', rel)
    shutil.copyfile(f, d); print('copy tools/lessons/svg/' + rel)
shutil.copyfile(os.path.join(x, 'img/ledger-lines-worksheet.jpg'), os.path.join(root, 'lessons/img/ledger-lines-worksheet.jpg')); print('copy lessons/img/ledger-lines-worksheet.jpg')
shutil.copyfile(os.path.join(x, 'img/wb-ledger-lines.jpg'), os.path.join(root, 'printables/img/wb-ledger-lines.jpg')); print('copy printables/img/wb-ledger-lines.jpg')
