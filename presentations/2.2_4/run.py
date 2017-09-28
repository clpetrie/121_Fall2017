import os
import platform

os.system('pdflatex 2.2_4.tex')
if platform.system() == 'Darwin':
   os.system('open 2.2_4.pdf')
if platform.system() == 'Linux':
   os.system('gnome-open 2.2_4.pdf')
os.system('rm *.bib *aux *key *log *nav *out *xml *snm *toc')
