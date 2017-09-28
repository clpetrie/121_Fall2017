#!/usr/bin/env python
from Tkinter import *
import os
import platform
import math
import wave
import struct
#import random
from random import randint

root = Tk()

root.title('Random Name Generator: Phy121 Fall 2017')
root.geometry('600x70')

names=('Alec Allard', 'Kyle Brown', 'Erica English', 'William Griffin', 'Ben Helferstay', 'Charles Holtzworth', 'Ryan Jones', 'Allen Karahasan', 'Elliot Lilikes', 'Christine Liu', 'Guangfa Ma', 'Salvador Mendoza', 'Areli Miller', 'Anthony Muhlenkamp', 'Martin Mumba', 'Christopher Okonya', 'Kameron Reed-Franklin', 'Cristian Reyes Lopez', 'Brandon Robertson', 'Vanessa Sanders', 'Diego Santos', 'Clint Skouson', 'Devan Strong', 'Gabriel Wahlberg')
num=len(names)

def callback():
   mynum=randint(0,num-1)
   text=names[mynum]
   TextBox.delete(1.0, END)
   TextBox.insert(END, text)

TextBox = Text(root,relief=RIDGE,height=1,width=30,borderwidth=2,font=("Helvetica",32))
TextBox.grid(row=0,column=1)

click_button = Button(root, text="Go", command=callback).grid(row=0,column=0)
#close_button = Button(root, text="Close", command=root.quit).grid(row=1,column=0)

root.mainloop()
