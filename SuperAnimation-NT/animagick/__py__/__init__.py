#! /bin/echo 'This file is not meant to be run...'
from tkinter import *
from sys import exit
from libcolor import *


def rect_mid(x, y, h, w):
    return x - w // 2, y - h // 2, x + w // 2, y + h // 2


class Coordinate:
    """ A simple two-value array."""
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def to_tuple(self):
        return self.x, self.y


class RigidBox:
    x1, y1, x2, y2 = 0, 0, 100, 100

