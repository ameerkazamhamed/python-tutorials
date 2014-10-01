#!/usr/bin/python
"""       xturtle-example-suite:

           xtx_minimal_hanoi.py

A minimal 'Towers of Hanoi' animation:
A tower of 6 discs is transferred from the
left to the right peg.

An imho quite elegant and concise
implementation using a tower class, which
is derived from the built-in type list.

Discs are turtles with shape "square", but
stretched to rectangles by turtlesize()
 ---------------------------------------
       To exit press STOP button
 ---------------------------------------      
"""
from xturtle import *

class Disc(Turtle):
    def __init__(self, n):
        Turtle.__init__(self, shape="square", visible=False)
        self.pu()
        self.turtlesize(1.5, n*1.5, 2) # square-->rectangle
        self.fillcolor(n/6., 0, 1-n/6.)
        self.st()

class Tower(list):
    "Hanoi tower, a subclass of built-in type list"
    def __init__(self, x):
        "create an empty tower. x is x-position of peg"
        self.x = x
    def push(self, d):
        d.setx(self.x)
        d.sety(-150+34*len(self))
        self.append(d)
    def pop(self):
        d = list.pop(self)
        d.sety(150)
        return d

def hanoi(n, _from, _with, _to):
    if n > 0:
        hanoi(n-1, _from, _to, _with) 
        _to.push(_from.pop())
        hanoi(n-1, _with, _from, _to)

def play():
    onkey(None,"space")
    clear()
    hanoi(6, t1, t2, t3)
    write("press STOP button to exit",
          align="center", font=("Courier", 16, "bold"))

def main():
    global t1, t2, t3
    ht(); penup(); goto(0, -225)   # writer turtle
    t1 = Tower(-250)
    t2 = Tower(0)
    t3 = Tower(250)
    # make tower of 6 discs
    for i in range(6,0,-1):
        t1.push(Disc(i))
    # prepare spartanic user interface ;-)        
    write("press spacebar to start game",
          align="center", font=("Courier", 16, "bold"))
    onkey(play, "space")
    listen()
    return "EVENTLOOP"
    
if __name__=="__main__":    
    msg = main()
    print msg
    mainloop()
