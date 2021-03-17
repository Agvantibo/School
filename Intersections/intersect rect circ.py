#!/bin/python3
from random import *
from tkinter import *
from intersection import *
from animagick import rect_mid

master = Tk()
W, H = 800, 600
cnv = Canvas(master, width=W, height=H, bg="black")
cnv.pack()

radius = 50

rx1, ry1, rx2, ry2 = rect_mid(W//2, H//2, 200, 300)
cul = cnv.create_oval(rect_mid(rx1, ry1, radius * 2, radius * 2), outline="lime", fill="black")
cur = cnv.create_oval(rect_mid(rx2, ry1, radius * 2, radius * 2), outline="lime", fill="black")
cll = cnv.create_oval(rect_mid(rx1, ry2, radius * 2, radius * 2), outline="lime", fill="black")
clr = cnv.create_oval(rect_mid(rx2, ry2, radius * 2, radius * 2), outline="lime", fill="black")
coll_rect_x = cnv.create_rectangle(rx1 - radius, ry1, rx2 + radius, ry2, outline="lime", fill="black")
coll_rect_y = cnv.create_rectangle(rx1, ry1 - radius, rx2, ry2 + radius, outline="lime", fill="black")
rect = cnv.create_rectangle(rx1, ry1, rx2, ry2, fill="white", outline="white")

for i in range(100):
    cxc, cyc = randint(0, W), randint(0, H)
    cx1, cy1, cx2, cy2 = rect_mid(cxc, cyc, radius, radius)
    if intersect_rectangles_2(rx1 - radius,  ry1 - radius, rx2 + radius, ry2 + radius, cx1, cy1, cx2, cy2):
        if intersect_circles_2(tuple(map(int, cnv.coords(cul))), cx1, cy1, cx2, cy2) or intersect_circles_2(tuple(map(int, cnv.coords(cur))), cx1, cy1, cx2, cy2) or intersect_circles_2(tuple(map(int, cnv.coords(cll))), cx1, cy1, cx2, cy2) or intersect_circles_2(tuple(map(int, cnv.coords(clr))), cx1, cy1, cx2, cy2):
            continue
    cnv.create_oval(cx1, cy1, cx2, cy2, outline="yellow")

mainloop()
