#!/usr/bin/python
"""       xturtle-example-suite:

             xtx_peace.py

A very simple drawing suitable as a beginner's
programming example.

A bit more advanced than xtx_peace.py: uses a few
commands from xturtle.py (such as hideturtle() and
the xturtle vocabulary.

USe of variables makes it more versatile and adaptable
"""

from xturtle import *

def main():

    WIDTH = 800
    HEIGHT = 612
    STRIPE_WIDTH = HEIGHT/7.
    RADIUS = 2.5 * STRIPE_WIDTH
    CIRCLE_WIDTH = 0.35 * STRIPE_WIDTH

    peacecolors = ("red3",  "orange", "yellow",
                   "seagreen4", "orchid4",
                   "royalblue1", "dodgerblue4")

    reset()
    speed(0)
    ht()
    pu()
    setpos(-WIDTH/2.0, -3*STRIPE_WIDTH)
    pensize(STRIPE_WIDTH)

    for pcolor in peacecolors:
        pencolor(pcolor)
        pd()
        fd(WIDTH)
        pu()
        bk(WIDTH)
        lt(90)
        fd(STRIPE_WIDTH)
        rt(90)

    pensize(CIRCLE_WIDTH)
    pencolor("white")
    setpos(0,-RADIUS)
    pd()

    circle(RADIUS, steps=60)
    left(90)
    fd(2*RADIUS)
    pu()
    lt(180)
    fd(RADIUS)
    rt(45)
    pd()
    fd(RADIUS)
    pu()
    bk(RADIUS)
    lt(90)
    pd()
    fd(RADIUS)
    up()

    return "Done!!"
    
if __name__ == "__main__":
    main()
    mainloop()
