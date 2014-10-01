"""      xturtle-example-suite:

             xtx_wikipedia3_how2.py

This is the fourth of a series of 4 examples
inspired by the Wikipedia article on turtle
graphics. (See example wikipedia1 for URLs)

It's essentially the same as example
wikipedia3, but for fewer polygons with
fewer edges.

It show graphically how it works, by
using normal speed and tracer(1). So
it's execution time is (intentionally) much
longer.
"""
from xturtle import *
from time import clock

def mn_eck(ne,sz):
    global p
    turtles = [p]
    for i in range(ne-1):
        q = p.clone()
        q.rt(360.0/ne)
        turtles.append(q)
        p = q
    for i in range(ne):
        c = abs(ne/2.0-i)/(ne*.7)
        for t in turtles:
            t.rt(360./ne)
            t.pencolor(1-c,0,c)
            t.fd(sz)

def main():
    global p
    p=Turtle()
    p.mode("logo")
    p.bgcolor("black")
    p.pencolor("red")
    p.pensize(3)
    p.speed(1)

    p.tracer(1,10)
    print p.speed(), p.delay()

    at = clock()
    mn_eck(13,39)   # or: (7,60)
    et = clock()
    return "Laufzeit: %.3f sec" % (et-at)

if __name__ == '__main__':
    msg = main()
    print msg
    mainloop()


## on my machine: approx. 48 sec.
