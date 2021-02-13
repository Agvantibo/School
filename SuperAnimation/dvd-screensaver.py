#!/bin/python3
from libcolor import Color, bw2color
from tkinter import Tk, Canvas, mainloop, PhotoImage
from animagick import rect_mid

# set window
root = Tk()
H, W = 700, 700
Cnv = Canvas(width=W, height=H, bg="black")
root.title("Jumpy Squares")
Cnv.pack()

# Draw initial stuff
color_slow = Color(106, 255, 0)     # green

vx = 3
vy = 5
colors = ((255, 255, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255))
x1, y1 = 0, 0


def animate():
    global vx, vy, Cnv, x1, y1
    dvd_img = PhotoImage("./assets/tmp.png")
    x2, y2 = x1 + 201, y1 + 92
    box = Cnv.create_image(x1, y1, x2, y2)

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
