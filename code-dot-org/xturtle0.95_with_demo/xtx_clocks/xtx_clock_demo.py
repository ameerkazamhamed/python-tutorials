#!/usr/bin/python
"""       xturtle-example-suite:

            xtx_clock_demo.py

Simple demonstration of 2 features of
xturtle:

(1) using a user defined pen shape, namely
the clock's hand (lines 21-33, 49-54)
(2) animation via onTimer (l. 56-61)

After drawing the clock-face and the hand
the program enters the EVENTLOOP. Only
Timer events are registered.

   Press STOP to exit the program!
   ===============================
"""
from xturtle import *

def main():
    reset()
    lt(90)

    polystart()
    fd(100)
    rt(90)
    fd(10)
    lt(120)
    fd(20)
    lt(120)
    fd(20)
    lt(120)
    fd(10)
    polyend()

    

    hand = get_poly()

    print 1

    lt(90)
    bk(100)
    clear()
    pensize(7)

    print 2

    pu()
    for i in range(12):
        fd(125)
        pd()
        fd(25)
        pu()
        bk(150)
        rt(30)
        
    addshape("hand", hand)
    shape("hand")
    resizemode("user")
    turtlesize(1, 1, 3)
    color("red", "blue")


    def tick():
        right(6)
        ontimer(tick, 1000)

    speed(1)
    ontimer(tick, 1000)
    return "EVENTLOOP"

if __name__ == '__main__':
    main()
    mainloop()    



    
