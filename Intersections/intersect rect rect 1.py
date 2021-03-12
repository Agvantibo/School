from random import *
from tkinter import *

from intersection import *

master = Tk()
W, H = 800, 600
cnv = Canvas(master, width=W, height=H)
cnv.pack()

cx, cy = randint(W//4, 3*W//4), randint(H//4, 3*H//4)
rx, ry = randint(W//8, W//4), randint(H//8, H//4)
c = cnv.create_rectangle(cx - rx, cy - ry, cx + rx, cy + ry, fill='red')

for i in range(100):
    cx1, cy1 = randint(0, W), randint(0, H)
    rx1, ry1 = randint(10, 20), randint(10, 20)

    if intersect_rectangles(cx, cy, rx, ry, cx1, cy1, rx1, ry1):
        cnv.create_rectangle(cx1 - rx1, cy1 - ry1, cx1 + rx1, cy1 + ry1, outline='green', width=3)
    else:
        cnv.create_rectangle(cx1 - rx1, cy1 - ry1, cx1 + rx1, cy1 + ry1, outline='blue', width=3)

mainloop()
