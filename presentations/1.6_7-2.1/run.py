import os
import platform

os.system('pdflatex 1.6_7-2.1.tex')
if platform.system() == 'Darwin':
   os.system('open 1.6_7-2.1.pdf')
if platform.system() == 'Linux':
   os.system('gnome-open 1.6_7-2.1.pdf')
os.system('rm *.bib *aux *key *log *nav *out *xml *snm *toc')
