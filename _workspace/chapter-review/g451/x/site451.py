#!/usr/bin/env python3
# Phase 451 on the site: the printables page's pictures of the two cut-out sets whose first page changed.
#   python3 site451.py <repo root> <this x dir>
import sys, os, shutil
root, x = sys.argv[1], sys.argv[2]
for f in ['cut-chord-loop.jpg', 'cut-cards-elements.jpg']:
    shutil.copyfile(os.path.join(x, 'img', f), os.path.join(root, 'printables/img', f)); print('copy printables/img/' + f)
