import os
import platform

os.system('pdflatex 2.5_7.tex')
if platform.system() == 'Darwin':
   os.system('open 2.5_7.pdf')
if platform.system() == 'Linux':
   os.system('gnome-open 2.5_7.pdf')
os.system('rm *.bib *aux *key *log *nav *out *xml *snm *toc')
