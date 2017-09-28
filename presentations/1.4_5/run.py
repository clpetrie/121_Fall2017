import os
import platform

os.system('pdflatex 1.4_5.tex')
if platform.system() == 'Darwin':
   os.system('open 1.4_5.pdf')
if platform.system() == 'Linux':
   os.system('gnome-open 1.4_5.pdf')
os.system('rm *.bib *aux *key *log *nav *out *xml *snm *toc')
