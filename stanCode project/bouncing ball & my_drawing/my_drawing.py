"""
File: my_drawing
Name: Jason Huang
----------------------
TODO: This is the GO game record of Lee Sedol, one of the best GO player in the history, against AlphaGo. The match is
best of 5 and this is the forth game of the match. And also this record is the only game human can beat artificial
intelligence. Therefore, i will say this is the milestone human did before because almost nobody can beat artificial
intelligence nowadays.

In the beginning, I try to create a GO game. However, I face some unsolvable problem so I tend to present the record
of on of the impressive game in the past. I will try to finish the game in the future when my ability is improved.
"""

from campy.graphics.gobjects import GOval, GRect, GLine, GLabel
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked


SIZE = 37

window = GWindow(800, 800)
rect = GRect(800, 800)


def main():
    """
    TODO: The create the board of GO game. After clicking, the recorded game will appear.
    """
    rect.filled = True
    rect.fill_color = 'sandybrown'
    window.add(rect)
    for i in range(40, 800, 40):
        hor = GLine(40, i, 760, i)
        window.add(hor)
    for j in range(40, 800, 40):
        vert = GLine(j, 40, j, 760)
        window.add(vert)
    original = GOval(10, 10)
    upper_left = GOval(10, 10)
    upper_right = GOval(10, 10)
    lower_left = GOval(10, 10)
    lower_right = GOval(10, 10)
    original = GOval(10, 10)
    original.filled = True
    upper_right.filled = True
    upper_left.filled = True
    lower_right.filled = True
    lower_left.filled = True
    upper_left.fill_color = original.fill_color
    upper_right.fill_color = original.fill_color
    lower_left.fill_color = original.fill_color
    lower_right.fill_color = original.fill_color
    original.fill_color = 'black'
    window.add(original, x=395, y=395)
    window.add(upper_left, x=155, y=155)
    window.add(upper_right, x=635, y=155)
    window.add(lower_left, x=155, y=635)
    window.add(lower_right, x=635, y=635)
    a = GLabel('A')
    b1 = GLabel('B')
    c = GLabel('C')
    d = GLabel('D')
    e = GLabel('E')
    f = GLabel('F')
    g = GLabel('G')
    h = GLabel('H')
    i = GLabel('I')
    j = GLabel('J')
    k = GLabel('K')
    l1 = GLabel('L')
    m = GLabel('M')
    n = GLabel('N')
    o = GLabel('O')
    p = GLabel('P')
    q = GLabel('Q')
    r = GLabel('R')
    s = GLabel('S')
    t = GLabel('T')

    window.add(a, x=40 - a.width / 2, y=40)
    window.add(b1, x=80 - a.width / 2, y=40)
    window.add(c, x=120 - a.width / 2, y=40)
    window.add(d, x=160 - a.width / 2, y=40)
    window.add(e, x=200 - a.width / 2, y=40)
    window.add(f, x=240 - a.width / 2, y=40)
    window.add(g, x=280 - a.width / 2, y=40)
    window.add(h, x=320 - a.width / 2, y=40)
    window.add(i, x=360 - a.width / 2, y=40)
    window.add(j, x=400 - a.width / 2, y=40)
    window.add(k, x=440 - a.width / 2, y=40)
    window.add(l1, x=480 - a.width / 2, y=40)
    window.add(m, x=520 - a.width / 2, y=40)
    window.add(n, x=560 - a.width / 2, y=40)
    window.add(o, x=600 - a.width / 2, y=40)
    window.add(p, x=640 - a.width / 2, y=40)
    window.add(q, x=680 - a.width / 2, y=40)
    window.add(r, x=720 - a.width / 2, y=40)
    window.add(s, x=760 - a.width / 2, y=40)
    for number in range(1, 20, 1):
        window.add(GLabel(str(number)), x=20, y=40 * number + 8)

    onmouseclicked(go)


def go(mouse):
    # Click to show the recorded game
    window.add(black(), x=200 - SIZE / 2, y=80 - SIZE / 2)
    window.add(black(), x=560 - SIZE / 2, y=80 - SIZE / 2)
    window.add(white(), x=360 - SIZE / 2, y=80 - SIZE / 2)
    window.add(white(), x=440 - SIZE / 2, y=80 - SIZE / 2)

    window.add(black(), x=160 - SIZE / 2, y=120 - SIZE / 2)
    window.add(black(), x=240 - SIZE / 2, y=120 - SIZE / 2)
    window.add(black(), x=320 - SIZE / 2, y=120 - SIZE / 2)
    window.add(black(), x=440 - SIZE / 2, y=120 - SIZE / 2)
    window.add(black(), x=560 - SIZE / 2, y=120 - SIZE / 2)
    window.add(white(), x=400 - SIZE / 2, y=120 - SIZE / 2)
    window.add(white(), x=480 - SIZE / 2, y=120 - SIZE / 2)
    window.add(white(), x=520 - SIZE / 2, y=120 - SIZE / 2)

    window.add(black(), x=120 - SIZE / 2, y=160 - SIZE / 2)
    window.add(black(), x=200 - SIZE / 2, y=160 - SIZE / 2)
    window.add(black(), x=280 - SIZE / 2, y=160 - SIZE / 2)
    window.add(black(), x=320 - SIZE / 2, y=160 - SIZE / 2)
    window.add(black(), x=440 - SIZE / 2, y=160 - SIZE / 2)
    window.add(black(), x=520 - SIZE / 2, y=160 - SIZE / 2)
    window.add(black(), x=560 - SIZE / 2, y=160 - SIZE / 2)
    window.add(black(), x=640 - SIZE / 2, y=160 - SIZE / 2)
    window.add(black(), x=720 - SIZE / 2, y=160 - SIZE / 2)
    window.add(white(), x=240 - SIZE / 2, y=160 - SIZE / 2)
    window.add(white(), x=360 - SIZE / 2, y=160 - SIZE / 2)

    window.add(black(), x=320 - SIZE / 2, y=200 - SIZE / 2)
    window.add(black(), x=520 - SIZE / 2, y=200 - SIZE / 2)
    window.add(black(), x=600 - SIZE / 2, y=200 - SIZE / 2)
    window.add(black(), x=760 - SIZE / 2, y=200 - SIZE / 2)
    window.add(white(), x=200 - SIZE / 2, y=200 - SIZE / 2)
    window.add(white(), x=240 - SIZE / 2, y=200 - SIZE / 2)
    window.add(white(), x=280 - SIZE / 2, y=200 - SIZE / 2)
    window.add(white(), x=360 - SIZE / 2, y=200 - SIZE / 2)
    window.add(white(), x=560 - SIZE / 2, y=200 - SIZE / 2)
    window.add(black(), x=600 - SIZE / 2, y=200 - SIZE / 2)

    window.add(black(), x=160 - SIZE / 2, y=240 - SIZE / 2)
    window.add(white(), x=240 - SIZE / 2, y=240 - SIZE / 2)
    window.add(black(), x=280 - SIZE / 2, y=240 - SIZE / 2)
    window.add(black(), x=320 - SIZE / 2, y=240 - SIZE / 2)
    window.add(white(), x=360 - SIZE / 2, y=240 - SIZE / 2)
    window.add(black(), x=480 - SIZE / 2, y=240 - SIZE / 2)
    window.add(white(), x=520 - SIZE / 2, y=240 - SIZE / 2)
    window.add(white(), x=560 - SIZE / 2, y=240 - SIZE / 2)
    window.add(black(), x=600 - SIZE / 2, y=240 - SIZE / 2)
    window.add(black(), x=680 - SIZE / 2, y=240 - SIZE / 2)
    window.add(black(), x=720 - SIZE / 2, y=240 - SIZE / 2)
    window.add(white(), x=760 - SIZE / 2, y=240 - SIZE / 2)

    window.add(white(), x=80 - SIZE / 2, y=280 - SIZE / 2)
    window.add(white(), x=120 - SIZE / 2, y=280 - SIZE / 2)
    window.add(black(), x=160 - SIZE / 2, y=280 - SIZE / 2)
    window.add(white(), x=200 - SIZE / 2, y=280 - SIZE / 2)
    window.add(white(), x=240 - SIZE / 2, y=280 - SIZE / 2)
    window.add(black(), x=280 - SIZE / 2, y=280 - SIZE / 2)
    window.add(black(), x=320 - SIZE / 2, y=280 - SIZE / 2)
    window.add(white(), x=400 - SIZE / 2, y=280 - SIZE / 2)
    window.add(black(), x=520 - SIZE / 2, y=280 - SIZE / 2)
    window.add(white(), x=560 - SIZE / 2, y=280 - SIZE / 2)
    window.add(black(), x=640 - SIZE / 2, y=280 - SIZE / 2)
    window.add(white(), x=680 - SIZE / 2, y=280 - SIZE / 2)
    window.add(white(), x=720 - SIZE / 2, y=280 - SIZE / 2)
    window.add(white(), x=760 - SIZE / 2, y=280 - SIZE / 2)

    window.add(black(), x=40 - SIZE / 2, y=320 - SIZE / 2)
    window.add(black(), x=80 - SIZE / 2, y=320 - SIZE / 2)
    window.add(black(), x=120 - SIZE / 2, y=320 - SIZE / 2)
    window.add(white(), x=160 - SIZE / 2, y=320 - SIZE / 2)
    window.add(white(), x=200 - SIZE / 2, y=320 - SIZE / 2)
    window.add(black(), x=240 - SIZE / 2, y=320 - SIZE / 2)
    window.add(white(), x=280 - SIZE / 2, y=320 - SIZE / 2)
    window.add(white(), x=360 - SIZE / 2, y=320 - SIZE / 2)
    window.add(white(), x=400 - SIZE / 2, y=320 - SIZE / 2)
    window.add(black(), x=440 - SIZE / 2, y=320 - SIZE / 2)
    window.add(black(), x=480 - SIZE / 2, y=320 - SIZE / 2)
    window.add(black(), x=520 - SIZE / 2, y=320 - SIZE / 2)
    window.add(white(), x=560 - SIZE / 2, y=320 - SIZE / 2)
    window.add(black(), x=600 - SIZE / 2, y=320 - SIZE / 2)
    window.add(black(), x=680 - SIZE / 2, y=320 - SIZE / 2)
    window.add(white(), x=720 - SIZE / 2, y=320 - SIZE / 2)

    window.add(white(), x=40 - SIZE / 2, y=360 - SIZE / 2)
    window.add(white(), x=120 - SIZE / 2, y=360 - SIZE / 2)
    window.add(white(), x=200 - SIZE / 2, y=360 - SIZE / 2)
    window.add(black(), x=240 - SIZE / 2, y=360 - SIZE / 2)
    window.add(white(), x=280 - SIZE / 2, y=360 - SIZE / 2)
    window.add(white(), x=360 - SIZE / 2, y=360 - SIZE / 2)
    window.add(black(), x=400 - SIZE / 2, y=360 - SIZE / 2)
    window.add(black(), x=480 - SIZE / 2, y=360 - SIZE / 2)
    window.add(white(), x=520 - SIZE / 2, y=360 - SIZE / 2)
    window.add(white(), x=600 - SIZE / 2, y=360 - SIZE / 2)
    window.add(white(), x=640 - SIZE / 2, y=360 - SIZE / 2)
    window.add(white(), x=680 - SIZE / 2, y=360 - SIZE / 2)

    window.add(white(), x=80 - SIZE / 2, y=400 - SIZE / 2)
    window.add(white(), x=120 - SIZE / 2, y=400 - SIZE / 2)
    window.add(white(), x=160 - SIZE / 2, y=400 - SIZE / 2)
    window.add(black(), x=200 - SIZE / 2, y=400 - SIZE / 2)
    window.add(black(), x=240 - SIZE / 2, y=400 - SIZE / 2)
    window.add(black(), x=320 - SIZE / 2, y=400 - SIZE / 2)
    window.add(white(), x=360 - SIZE / 2, y=400 - SIZE / 2)
    window.add(black(), x=400 - SIZE / 2, y=400 - SIZE / 2)
    window.add(black(), x=440 - SIZE / 2, y=400 - SIZE / 2)
    window.add(white(), x=480 - SIZE / 2, y=400 - SIZE / 2)
    window.add(white(), x=520 - SIZE / 2, y=400 - SIZE / 2)
    window.add(white(), x=560 - SIZE / 2, y=400 - SIZE / 2)
    window.add(white(), x=680 - SIZE / 2, y=400 - SIZE / 2)
    window.add(white(), x=720 - SIZE / 2, y=400 - SIZE / 2)
    window.add(white(), x=760 - SIZE / 2, y=400 - SIZE / 2)

    window.add(white(), x=40 - SIZE / 2, y=440 - SIZE / 2)
    window.add(black(), x=80 - SIZE / 2, y=440 - SIZE / 2)
    window.add(black(), x=120 - SIZE / 2, y=440 - SIZE / 2)
    window.add(black(), x=160 - SIZE / 2, y=440 - SIZE / 2)
    window.add(black(), x=240 - SIZE / 2, y=440 - SIZE / 2)
    window.add(black(), x=280 - SIZE / 2, y=440 - SIZE / 2)
    window.add(white(), x=320 - SIZE / 2, y=440 - SIZE / 2)
    window.add(white(), x=360 - SIZE / 2, y=440 - SIZE / 2)
    window.add(black(), x=440 - SIZE / 2, y=440 - SIZE / 2)
    window.add(white(), x=520 - SIZE / 2, y=440 - SIZE / 2)
    window.add(white(), x=560 - SIZE / 2, y=440 - SIZE / 2)
    window.add(white(), x=600 - SIZE / 2, y=440 - SIZE / 2)

    window.add(white(), x=80 - SIZE / 2, y=480 - SIZE / 2)
    window.add(black(), x=120 - SIZE / 2, y=480 - SIZE / 2)
    window.add(black(), x=240 - SIZE / 2, y=480 - SIZE / 2)
    window.add(white(), x=280 - SIZE / 2, y=480 - SIZE / 2)
    window.add(white(), x=400 - SIZE / 2, y=480 - SIZE / 2)
    window.add(black(), x=440 - SIZE / 2, y=480 - SIZE / 2)
    window.add(black(), x=520 - SIZE / 2, y=480 - SIZE / 2)
    window.add(white(), x=560 - SIZE / 2, y=480 - SIZE / 2)
    window.add(white(), x=640 - SIZE / 2, y=480 - SIZE / 2)
    window.add(white(), x=680 - SIZE / 2, y=480 - SIZE / 2)
    window.add(white(), x=720 - SIZE / 2, y=480 - SIZE / 2)
    window.add(white(), x=760 - SIZE / 2, y=480 - SIZE / 2)

    window.add(white(), x=280 - SIZE / 2, y=520 - SIZE / 2)
    window.add(black(), x=360 - SIZE / 2, y=520 - SIZE / 2)
    window.add(black(), x=440 - SIZE / 2, y=520 - SIZE / 2)
    window.add(white(), x=600 - SIZE / 2, y=520 - SIZE / 2)

    window.add(black(), x=80 - SIZE / 2, y=560 - SIZE / 2)
    window.add(black(), x=120 - SIZE / 2, y=560 - SIZE / 2)
    window.add(black(), x=160 - SIZE / 2, y=560 - SIZE / 2)
    window.add(black(), x=200 - SIZE / 2, y=560 - SIZE / 2)
    window.add(white(), x=320 - SIZE / 2, y=560 - SIZE / 2)
    window.add(black(), x=360 - SIZE / 2, y=560 - SIZE / 2)

    window.add(white(), x=120 - SIZE / 2, y=600 - SIZE / 2)
    window.add(white(), x=200 - SIZE / 2, y=600 - SIZE / 2)
    window.add(white(), x=240 - SIZE / 2, y=600 - SIZE / 2)
    window.add(white(), x=280 - SIZE / 2, y=600 - SIZE / 2)
    window.add(black(), x=320 - SIZE / 2, y=600 - SIZE / 2)
    window.add(black(), x=600 - SIZE / 2, y=600 - SIZE / 2)
    window.add(white(), x=640 - SIZE / 2, y=600 - SIZE / 2)

    window.add(white(), x=80 - SIZE / 2, y=640 - SIZE / 2)
    window.add(white(), x=160 - SIZE / 2, y=640 - SIZE / 2)
    window.add(black(), x=200 - SIZE / 2, y=640 - SIZE / 2)
    window.add(white(), x=240 - SIZE / 2, y=640 - SIZE / 2)
    window.add(white(), x=320 - SIZE / 2, y=640 - SIZE / 2)
    window.add(black(), x=520 - SIZE / 2, y=640 - SIZE / 2)
    window.add(black(), x=600 - SIZE / 2, y=640 - SIZE / 2)
    window.add(white(), x=680 - SIZE / 2, y=640 - SIZE / 2)

    window.add(white(), x=120 - SIZE / 2, y=680 - SIZE / 2)
    window.add(white(), x=240 - SIZE / 2, y=680 - SIZE / 2)
    window.add(black(), x=360 - SIZE / 2, y=680 - SIZE / 2)
    window.add(black(), x=560 - SIZE / 2, y=680 - SIZE / 2)
    window.add(white(), x=600 - SIZE / 2, y=680 - SIZE / 2)
    window.add(white(), x=640 - SIZE / 2, y=680 - SIZE / 2)

    window.add(white(), x=200 - SIZE / 2, y=720 - SIZE / 2)
    window.add(black(), x=240 - SIZE / 2, y=720 - SIZE / 2)
    window.add(black(), x=280 - SIZE / 2, y=720 - SIZE / 2)
    window.add(black(), x=600 - SIZE / 2, y=720 - SIZE / 2)
    window.add(black(), x=640 - SIZE / 2, y=720 - SIZE / 2)
    window.add(white(), x=680 - SIZE / 2, y=720 - SIZE / 2)

    window.add(white(), x=160 - SIZE / 2, y=760 - SIZE / 2)
    window.add(black(), x=200 - SIZE / 2, y=760 - SIZE / 2)
    window.add(black(), x=640 - SIZE / 2, y=760 - SIZE / 2)
    window.add(white(), x=680 - SIZE / 2, y=760 - SIZE / 2)


def black():
    b = GOval(SIZE, SIZE)
    b.filled = True
    b.fill_color = 'black'
    b.color = b.fill_color
    return b


def white():
    w = GOval(SIZE, SIZE)
    w.filled = True
    w.fill_color = 'white'
    w.color = 'black'
    return w


if __name__ == '__main__':
    main()
