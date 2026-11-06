#!/usr/bin/env python3
# Phase 448 on the site: the ledger-lines worksheet pictures (Workbook page 1) with the treble clefs' tails whole.
#   python3 site448.py <repo root> <this x dir>
import sys, os, shutil
root, x = sys.argv[1], sys.argv[2]
shutil.copyfile(os.path.join(x, 'img/ledger-lines-worksheet.jpg'), os.path.join(root, 'lessons/img/ledger-lines-worksheet.jpg')); print('copy lessons/img/ledger-lines-worksheet.jpg')
shutil.copyfile(os.path.join(x, 'img/wb-ledger-lines.jpg'), os.path.join(root, 'printables/img/wb-ledger-lines.jpg')); print('copy printables/img/wb-ledger-lines.jpg')
