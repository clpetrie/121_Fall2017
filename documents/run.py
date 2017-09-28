import os
import platform

os.system('pdflatex syllabus.tex')
os.system('rm *.aux *.log *.out')
if platform.system() == 'Darwin':
   os.system('open syllabus.pdf')
if platform.system() == 'Linux':
   os.system('gnome-open syllabus.pdf')
