"""
File: bouncing ball
Name: Jason Huang
-------------------------
TODO: to create a program to imitate ball free fall if we give ball a force and it moves forward
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

# Define the parameters
VX = 7
VY = 3
DELAY = 30
GRAVITY = 2
SIZE = 20
REDUCE = 0.9
START_X = 100
START_Y = 200

# Define global variables
window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
count = 0


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball.filled = True
    ball.fill_color = 'black'
    window.add(ball)
    onmouseclicked(moving)


def moving(mouse):
    """
    This program is to carry out the order after clicking mouse left button.
    The program can be executed three times and then it will be blocked
    """
    global VX, VY, count
    original = window.get_object_at(START_X + SIZE/2, START_Y + SIZE/2)
    if original is not None and count < 3:
        count += 1
        while True:
            ball.move(VX, VY)
            VY += GRAVITY
            pause(DELAY)
            if ball.y + SIZE >= window.height:
                VY = -VY * REDUCE
            elif ball.x >= window.width:
                window.add(ball, x=START_X, y=START_Y)
                break


if __name__ == "__main__":
    main()
