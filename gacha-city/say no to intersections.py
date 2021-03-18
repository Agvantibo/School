from tkinter import *
from random import *
from intersection import *  # наш собственный файл

master = Tk()
W, H = 800, 600
cnv = Canvas(master, width=W, height=H)
cnv.pack()

circles = []  # пустой список, здесь будут храниться уже существующие круги
N = 500  # число попыток

for i in range(N):
    # новый случайный круг
    new_x = randint(0, W)
    new_y = randint(0, H)
    new_r = randint(15, 30)

    n_circles = len(circles)  # текущее количество уже существующих кругов

    n_intersections = 0  # число пересечений нового круга с уже существующими

    for j in range(n_circles):
        x1, y1, x2, y2 = cnv.coords(circles[j])  # координаты уже существующего круга из Canvas
        old_x, old_y, old_r = (x1 + x2) / 2, (y1 + y2) / 2, (x2 - x1) / 2  # центр и радиус

        if intersect_circles(new_x, new_y, new_r, old_x, old_y, old_r):
            n_intersections += 1  # если пересекаются, увеличь на единицу

    # добавим новый круг, только если он не пересекается ни с одним из старых
    if n_intersections == 0:
        new_circle = cnv.create_oval(new_x - new_r, new_y - new_r, new_x + new_r, new_y + new_r)

        circles.append(new_circle)  # добавить новый элемент в конец списка

mainloop()
