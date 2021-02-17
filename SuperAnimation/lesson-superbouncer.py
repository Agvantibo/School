from tkinter import *

master = Tk()
W, H = 800, 600
cnv = Canvas(master, width=W, height=H)
cnv.pack()

cnv.create_rectangle(0, 0, W, H, fill='black')

r = 20
p = cnv.create_rectangle(W / 3, H / 3, 2 * W / 3, 2 * H / 3, fill='yellow')
b = cnv.create_rectangle(7 * W / 8 - r, 7 * H / 8 - r, 7 * W / 8 + r, 7 * H / 8 + r, fill='red')

vx, vy = -4.2, -2.9


def animate():
    global vx, vy

    cnv.move(b, vx, vy)

    x1, y1, x2, y2 = cnv.coords(b)
    px1, py1, px2, py2 = cnv.coords(p)

    if x2 > W:
        cnv.move(b, W - x2, (W - x2) * (vy / vx))
        vx = -vx
    elif x1 < 0:
        cnv.move(b, -x1, -x1 * (vy / vx))
        vx = -vx
    elif y2 > H:
        cnv.move(b, (H - y2) * (vx / vy), H - y2)
        vy = -vy
    elif y1 < 0:
        cnv.move(b, -y1 * (vx / vy), -y1)
        vy = -vy
    elif y1 < py1 < y2 and x1 < px1 < x2:
        if y2 - py1 < x2 - px1:
            cnv.move(b, (py1 - y2) * (vx / vy), py1 - y2)
            vy = -vy
        else:
            cnv.move(b, px1 - x2, (px1 - x2) * (vy / vx))
            vx = -vx
    elif y1 < py2 < y2 and x1 < px1 < x2:
        if py2 - y1 < x2 - px1:
            cnv.move(b, (py2 - y1) * (vx / vy), py2 - y1)
            vy = -vy
        else:
            cnv.move(b, px1 - x2, (px1 - x2) * (vy / vx))
            vx = -vx
    elif y1 < py1 < y2 and x1 < px2 < x2:
        if y2 - py1 < px2 - x1:
            cnv.move(b, (py1 - y2) * (vx / vy), py1 - y2)
            vy = -vy
        else:
            cnv.move(b, px2 - x1, (px2 - x1) * (vy / vx))
            vx = -vx
    elif y1 < py2 < y2 and x1 < px2 < x2:
        if py2 - y1 < px2 - x1:
            cnv.move(b, (py2 - y1) * (vx / vy), py2 - y1)
            vy = -vy
        else:
            cnv.move(b, px2 - x1, (px2 - x1) * (vy / vx))
            vx = -vx
    elif y1 < py1 < y2 and x2 > px1 and x1 < px2:
        cnv.move(b, (py1 - y2) * (vx / vy), py1 - y2)
        vy = -vy
    elif x1 < px2 < x2 and y2 > py1 and y1 < py2:
        cnv.move(b, px2 - x1, (px2 - x1) * (vy / vx))
        vx = -vx
    elif y1 < py2 < y2 and x2 > px1 and x1 < px2:
        cnv.move(b, (py2 - y1) * (vx / vy), py2 - y1)
        vy = -vy
    elif x1 < px1 < x2 and y2 > py1 and y1 < py2:
        cnv.move(b, px1 - x2, (px1 - x2) * (vy / vx))
        vx = -vx

    cnv.after(10, animate)


animate()

mainloop()
