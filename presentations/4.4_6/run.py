import os
import platform

os.system('pdflatex 4.4_6.tex')
if platform.system() == 'Darwin':
   os.system('open 4.4_6.pdf')
if platform.system() == 'Linux':
   os.system('gnome-open 4.4_6.pdf')
os.system('rm *.bib *aux *key *log *nav *out *xml *snm *toc')
