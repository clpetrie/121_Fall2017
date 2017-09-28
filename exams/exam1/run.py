import os
import platform

os.system("sed -i -e 's/toggletrue/togglefalse/g' exam1.tex")
os.system('pdflatex exam1.tex')
os.system('pdflatex exam1.tex')
os.system('mv exam1.pdf exam1_SOLUTIONS.pdf')

os.system("sed -i -e 's/togglefalse/toggletrue/g' exam1.tex")
os.system('pdflatex exam1.tex')
os.system('pdflatex exam1.tex')
os.system('rm *.bib *aux *key *log *nav *out *xml *snm *toc')

if platform.system() == 'Darwin':
   os.system('open exam1.pdf')
   os.system('open exam1_SOLUTIONS.pdf')
if platform.system() == 'Linux':
   os.system('gnome-open exam1.pdf')
   os.system('gnome-open exam1_SOLUTIONS.pdf')
