import os
import platform

os.system('pdflatex 5.1_3.tex')
if platform.system() == 'Darwin':
   os.system('open 5.1_3.pdf')
if platform.system() == 'Linux':
   os.system('gnome-open 5.1_3.pdf')
os.system('rm *.bib *aux *key *log *nav *out *xml *snm *toc')
