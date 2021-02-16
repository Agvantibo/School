#!/bin/python3
from libcolor import Color
from tkinter import Tk, Canvas, mainloop
from animagick import rect_mid

# set window
root = Tk()
H, W = 700, 700
Cnv = Canvas(width=W, height=H, bg="black")
root.title("Jumpy Squares")
Cnv.pack()

# Draw initial stuff
color_slow = Color(106, 255, 0)     # green
box = Cnv.create_rectangle(0, 0, 50, 50, fill=color_slow.to_hex())

vx = 5
vy = 3


def animate():
    global vx, vy

    x1, y1, x2, y2 = Cnv.coords(box)
    if x1 < 0:
        vx = -vx
    if x2 > W:
        vx = -vx
    if y1 < 0:
        vy = -vy
    if y2 > H:
        vy = -vy

    Cnv.move(box, vx, vy)

    Cnv.after(10, animate)


animate()

mainloop()
