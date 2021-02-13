#!/bin/python3
from libcolor import Color, bw2color
from tkinter import Tk, Canvas, mainloop, PhotoImage
from random import choice
from time import sleep
from animagick import rect_mid
# set window
root = Tk()
H, W = 700, 700
Cnv = Canvas(width=W, height=H, bg="black")
root.title("DVD")
Cnv.pack()


vx = 3
vy = 5
colors = ((255, 255, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255))
x1, y1 = 0, 0


def animate():
    global vx, vy, Cnv, x1, y1
    dvd_img = PhotoImage(file="tmp.png")
    x2, y2 = x1 + 201, y1 + 92
#    box = Cnv.create_image(x1, y1, image=dvd_img, anchor='nw')
    box = Cnv.create_rectangle(x1, y1, x2, y2, fill="white")
    print('recreation succeeded with values', x1, y1)
    if x1 < 0:
        vx = -vx
        bw2color('./assets/dvd.png', choice(colors))
    if x2 > W:
        vx = -vx
        bw2color('./assets/dvd.png', choice(colors))
    if y1 < 0:
        vy = -vy
        bw2color('./assets/dvd.png', choice(colors))
    if y2 > H:
        vy = -vy
        bw2color('./assets/dvd.png', choice(colors))
    Cnv.move(box, vx, vy)
    x1, y1, muda, muda = Cnv.coords(box)
    Cnv.after(10, animate)


animate()

mainloop()
