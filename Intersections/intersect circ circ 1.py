from random import *
from tkinter import *

from intersection import *

master = Tk()
W, H = 800, 600
cnv = Canvas(master, width=W, height=H)
cnv.pack()

cx, cy, r = randint(W//4, 3*W//4), randint(H//4, 3*H//4), randint(H//8, H//4)
c = cnv.create_oval(cx - r, cy - r, cx + r, cy + r, fill='red')

for i in range(100):
    cx1, cy1, r1 = randint(0, W), randint(0, H), randint(10, 20)

    if intersect_circles(cx, cy, r, cx1, cy1, r1):
        cnv.create_oval(cx1 - r1, cy1 - r1, cx1 + r1, cy1 + r1, outline='green', width=3)
    else:
        cnv.create_oval(cx1 - r1, cy1 - r1, cx1 + r1, cy1 + r1, outline='blue', width=3)

mainloop()
