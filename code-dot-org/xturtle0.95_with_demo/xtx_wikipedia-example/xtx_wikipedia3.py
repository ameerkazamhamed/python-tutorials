"""      xturtle-example-suite:

             xtx_wikipedia3.py

This is the third of a series of 4 examples
inspired by the Wikipedia article on turtle
graphics. (See example wikipedia1 for URLs)

It gives an alternate implementation:
First we create (ne-1) (i.e. 35 in this
example) copies of our first turtle p.
Then we let them perform their steps in
parallel.

Followed by a complete undo().  (NEW!)
"""
from xturtle import *
from time import clock, sleep

def mn_eck(ne,sz):
    global p
    turtles = [p]
    #create ne-1 additional turtles
    for i in range(1,ne):
        q = p.clone()
        q.rt(360.0/ne)
        turtles.append(q)
        p = q
    for i in range(ne):
        c = abs(ne/2.0-i)/(ne*.7)
        # let those ne turtles make a step
        # in parallel:
        for t in turtles:
            t.rt(360./ne)
            t.pencolor(1-c,0,c)
            t.fd(sz)

def main():
    global p
    p=Turtle()
    p.mode("logo")
    p.speed(0)
    p.hideturtle()
    p.getscreen().bgcolor("black")
    p.pencolor("red")
    p.pensize(3)

    p.tracer(36,0)

    at = clock()
    mn_eck(36,19)
    et = clock()
    z1 = et-at

    sleep(1)

    at = clock()
    for i in range(500):
        for t in turtles():
           t.undo()
    et = clock()
    return "Laufzeit: %.3f sec" % (z1+et-at)
    

if __name__ == '__main__':
    msg = main()
    print msg
    mainloop()


## on my desktop machine: approx. 1.65 sec.
## on my laptop: approx. 1.1 sec
