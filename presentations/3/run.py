import os
import platform

os.system('pdflatex 3.tex')
if platform.system() == 'Darwin':
   os.system('open 3.pdf')
if platform.system() == 'Linux':
   os.system('gnome-open 3.pdf')
os.system('rm *.bib *aux *key *log *nav *out *xml *snm *toc')
