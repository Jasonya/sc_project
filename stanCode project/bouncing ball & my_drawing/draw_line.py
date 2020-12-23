"""
File: draw_line
Name: Jason Huang
-------------------------
TODO: This program is to help users to draw a line if they point out extreme points of the line
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE = 10

# Define global variables
window = GWindow()
click = 0
x = 0
y = 0


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(extreme_point)


def extreme_point(mouse):
    """
    This program is to carry out the order when clicking the mouse left button.
    At first click it will draw a circle as line original point. Second time, it will draw
    a line between original point and your mouse location.
    """
    global click, x, y
    click += 1
    if (click % 2) == 1:
        oral = GOval(SIZE, SIZE, x=mouse.x - SIZE / 2, y=mouse.y - SIZE / 2)
        oral.filled = False
        window.add(oral)
        x = oral.x + SIZE / 2
        y = oral.y + SIZE / 2

    else:
        line = GLine(x, y, mouse.x, mouse.y)
        c = window.get_object_at(x, y)
        window.remove(c)
        window.add(line)


if __name__ == "__main__":
    main()
