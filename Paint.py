from tkinter import *
import PIL
from PIL import Image, ImageDraw
import numpy as np
from pathlib import Path
import uuid


class Paint(object):
    pen_size = 10
    pen_color = 'white'

    def __init__(self):
        self.window = Tk()
        self.window.title('Digit Drawer')
        self.window.resizable(height='False', width='False')
        self.window.minsize(height=200, width=300)
        self.result = StringVar()
        self.result.set("")
        self.instuction_lable = Label(self.window, text='Please draw an image then save')
        self.instuction_lable.pack()
        self.result_entry = Entry(self.window, width=33, textvariable=self.result, justify = CENTER)
        self.result_entry.pack()
        self.canvas = Canvas(self.window, width=80, height=80, background='black')
        self.image = PIL.Image.new('RGB', (80, 80), 'black')
        self.canvas.pack()
        self.predict_button = Button(self.window, text='Save', command=self.predict)
        self.predict_button.pack()
        self.clear_button = Button(self.window, text='Redraw', command=self.clear)
        self.clear_button.pack()
        self.setup()
        self.window.mainloop()

    def setup(self):
        self.old_x = None
        self.old_y = None
        self.line_width = self.pen_size
        self.color = self.pen_color
        self.canvas.bind('<1>', self.activate_paint)
        self.draw = ImageDraw.Draw(self.image)
        self.canvas.bind('<B1-Motion>', self.paint)

        self.window.bind('<ButtonRelease-1>', self.reset)

    def activate_paint(self, event):
        self.canvas.bind('<B1-Motion>', self.paint)
        self.old_x, self.old_y = event.x, event.y

    def paint(self, event):
        if self.old_x and self.old_y:
            self.canvas.create_line(self.old_x, self.old_y, event.x, event.y,
                               width=self.pen_size, fill=self.pen_color,
                               capstyle=ROUND, smooth=TRUE, splinesteps=36)
        self.draw.line((self.old_x, self.old_y, event.x, event.y), fill=self.pen_color, width=self.pen_size)
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x, self.old_y = None, None

    def clear(self):
        self.canvas.delete("all")
        self.draw.rectangle((0, 0, 80, 80), fill='black')

    def predict(self):
        save_img = self.image.resize((16,16)).convert('1')
        save_img.save(f"datasets/4/{uuid.uuid1()}.png")

if __name__ == '__main__':
    Paint()
