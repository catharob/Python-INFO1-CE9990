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

canvas = tkinter.Canvas(root, highlightthickness = 0, background = swedishYellow)

def drawPixel(x, y, color):
    """
    Color the pixel at coordinates (x, y).
    """
    assert isinstance(x, int) and isinstance(y, int) and isinstance(color, str)
    canvas.create_rectangle(x, y, x + 1, y + 1, width = 0, fill = color)

y = 0
while y < height:

    x = 0
    while x < width:

        if x < width * 5/16 and y < 2 * yellowHeight:
            drawPixel(x, y, swedishBlue)
        elif x > width * 7/16 and y < 2 * yellowHeight:
            drawPixel(x, y, swedishBlue)
        elif x < width * 5/16 and y > 3 * yellowHeight:
            drawPixel(x, y, swedishBlue)
        elif x > width * 7/16 and y > 3 * yellowHeight:
            drawPixel(x, y, swedishBlue)
        x += 1
    y += 1

#Make the canvas visible by packing it into the root.
canvas.pack(expand = tkinter.YES, fill = "both")

root.mainloop()