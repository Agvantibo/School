#!/bin/pypy3
from libcolor import Color
from tkinter import Tk, Canvas, mainloop, PhotoImage
from random import choice
# set window
root = Tk()
H, W = 700, 700
Cnv = Canvas(width=W, height=H, bg="black")
root.title("Escherian Stairwell")
Cnv.pack()

if input("Colors? y/N").lower() == "y":
    colored = True
else:
    colored = False

vx = 3
vy = 5
colors = (Color(255, 255, 255), Color(255, 255, 0), Color(255, 0, 255), Color(0, 255, 255), Color(255, 0, 0),
          Color(0, 255, 0), Color(0, 0, 255))
x1, y1 = 0, 0

if colored:
    c_color = choice(colors)
else:
    c_color = Color(255, 255, 255)


def animate():
    global vx, vy, Cnv, x1, y1, c_color, colored
#    dvd_img = PhotoImage(file="assets/tmp.png")
    x2, y2 = x1 + 150, y1 + 200
#    cover_up = Cnv.create_rectangle(x1 - 40, y1 - 40, x2 + 40, y2 + 40, fill="black")
    box = Cnv.create_rectangle(x1, y1, x2, y2, fill=c_color.to_hex())
    print('recreation succeeded with values', x1, y1)
    if x1 < 0:
        vx = -vx
        if colored:
            c_color = choice(colors)
    if x2 > W:
        vx = -vx
        if colored:
            c_color = choice(colors)
    if y1 < 0:
        vy = -vy
        if colored:
            c_color = choice(colors)
    if y2 > H:
        vy = -vy
        if colored:
            c_color = choice(colors)
    Cnv.move(box, vx, vy)
    x1, y1, muda, muda = Cnv.coords(box)
    Cnv.after(10, animate)


animate()

mainloop()
