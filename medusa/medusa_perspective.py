#!/bin/pypy3
from tkinter import*
from random import*
from math import*

master=Tk()
w=700
cnv = Canvas(master, width = w, height = w)
cnv.pack()
img=PhotoImage(file='medusa.png')
cnv.create_image(0,0,anchor=NW, image=img)


def center_get(w, x, y,):
    dx = w/2 - x
    dy = w/2 - y
    return sqrt(dx ** 2 + dy ** 2)


for i in range(30000):
    x=randint(0,w-1)
    y=randint(0,w-1)
    r,g,b=img.get(x,y)
    if r < 220:
        color='gray'+str(int(r/2.55))
        r=2 + center_get(w, x, y)/27
        cnv.create_oval(x-r,y-r,x+r,y+r,fill = color)

mainloop()
