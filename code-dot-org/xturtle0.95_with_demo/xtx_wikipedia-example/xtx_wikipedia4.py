"""      xturtle-example-suite:

             xtx_wikipedia4.py

This is the fourth of a series of 4 examples
inspired by the Wikipedia article on turtle
graphics. (See example wikipedia1 for URLs)

It gives an alternate implementation:
First we create (ne-1) (i.e. 35 in this
example) copies of our first turtle p.
Then we let them perform their steps in
parallel.

Version without cloning using the turtles()
method of TurtleScreen
"""
from xturtle import *
from time import clock

def create_turtles(ne):
    for i in range(ne):
        p=Pen()
        if i==0:
            # screen settings
            p.bgcolor("black")
            p.tracer(36,0)
        p.ht()
        p.speed(0)
        p.seth(i*360.0/ne)
        p.width(3)
    return p.turtles()

def mn_eck(ne,sz):
    #create ne turtles
    myturtles = create_turtles(ne)
    for i in range(ne):
        c = abs(ne/2.0-i)/(ne*.7)
        # let alle those turtles make a step
        # in parallel:
        for t in myturtles:
            t.rt(360./ne)
            t.pencolor(1-c,0,c)
            t.fd(sz)

def main():
    at = clock()
    mn_eck(36,19)
    et = clock()
    return "Laufzeit: %.3f sec" % (et-at)

if __name__ == '__main__':
    msg = main()
    print msg
    mainloop()


## on my desktop machine: approx. 1.65 sec.
## on my laptop: approx. 1.1 sec
