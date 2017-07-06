"""
tkflag.py

Draw the Swedish flag in color on a tkinter Canvas widget.
"""
import tkinter

#dimensions of entire flag, in pixels
yellowHeight = 50           #width and height of yellow band
height = 5 * yellowHeight   #yellow band plus blue blocks height
width = int(height * 16/10) #Wikipedia says aspect ratio of flag is 10:16

#The root widget is the window that will contain everything we draw.
root = tkinter.Tk()
root.title("Flag of Sweden")
root.geometry(str(width) + "x" + str(height))

#some Swedish colors
swedishBlue = "#005b99"
swedishYellow = "#fcd116"

canvas = tkinter.Canvas(root, highlightthickness = 0, background = swedishBlue)

def drawPixel(x, y, color):
    """
    Color the pixel at coordinates (x, y).
    """
    assert isinstance(x, int) and isinstance(y, int) and isinstance(color, str)
    canvas.create_rectangle(x, y, x + 1, y + 1, width = 0, fill = color)

for y in range(height):

    for x in range(width):

        if width * 5/16 <= x and x < width * 7/16 or 2 * yellowHeight < y and y < 3 * yellowHeight:
            drawPixel(x, y, swedishYellow)
        

#Make the canvas visible by packing it into the root.
canvas.pack(expand = tkinter.YES, fill = "both")

root.mainloop()