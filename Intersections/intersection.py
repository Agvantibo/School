from math import *


def dist(x1, y1, x2, y2):
    dx = x1 - x2
    dy = y1 - y2
    return sqrt(dx * dx + dy * dy)


def intersect_circles(cx1, cy1, r1, cx2, cy2, r2):
    d = dist(cx1, cy1, cx2, cy2)

    return d < r1 + r2


def intersect_circles_2(x11, y11, x12, y12, x21, y21, x22, y22):
    cx1 = (x11 + x12) / 2
    cy1 = (y11 + y12) / 2
    r1 = (x12 - x11) / 2
    cx2 = (x21 + x22) / 2
    cy2 = (y21 + y22) / 2
    r2 = (x22 - x21) / 2

    return intersect_circles(cx1, cy1, r1, cx2, cy2, r2)


def intersect_rectangles(cx1, cy1, rx1, ry1, cx2, cy2, rx2, ry2):
    dx = abs(cx1 - cx2)
    dy = abs(cy1 - cy2)

    return dx < rx1 + rx2 and dy < ry1 + ry2


def intersect_rectangles_2(x11, y11, x12, y12, x21, y21, x22, y22):
    return x12 < x21 or x11 > x22 or y12 < y21 or y11 > y22
