#!/bin/pypy3
from tkinter import *
from PIL import Image
from PIL import ImageTk

root = Tk()
w, h = 1474, 1056
cnv = Canvas(root, width=w, height=h)

root.title("It is totally not suspicious")
root.geometry(str(h) + "x" + str(w))
root.configure(background="black")


class Example(Frame):
    def __init__(self, master, *pargs):
        Frame.__init__(self, master, *pargs)

        self.image = Image.open('./assets/creepy/stop/stop_it/okay/informatics.png')
        self.img_copy= self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

    def _resize_image(self, event):

        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image =  self.background_image)


e = Example(root)
e.pack(fill=BOTH, expand=YES)
mainloop()
