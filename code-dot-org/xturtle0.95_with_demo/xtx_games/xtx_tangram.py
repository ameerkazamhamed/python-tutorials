#!/usr/bin/python
"""       xturtle-example-suite:

             xtx_tangram.py

Simple version of tangram game,
demonstrating the use of ondrag.

(1) Drag pieces with left mouse button
(2) Turn pieces counterclockwise with middle
    mouse button
(3) Turn pieces right with rigth mouse button
(4) Doubleclick left mouse button do flip
    rhombus.

Tangram pieces are turtles of various shapes
and turtlesizes. Buttons are turtles with
image-shapes.

Pressing the NEXT button chooses randomly a
pattern from a library of 100 patterns, which
are stored in a separate file. 
Pressing HELP show the outline of the
solution for approx. half a second.
 -------------------------------------------
          To exit press STOP button
 -------------------------------------------  
"""
from xturtle import * 
from button import Button
import sys, math, random, time

from tangramdata import tangramdata

sys.setrecursionlimit(20000)
title("Tangram")

startdata = tangramdata[0]
tangramdata = tangramdata[1:]

A = 198.0
a = A / 4.0
d = a * math.sqrt(2)

def makerhombusshapes():
    mode("logo")
    tracer(0)
    pu()
    left(45)
    fd(d/2.0)
    begin_poly()
    rt(90)
    fd(d)
    rt(135)
    fd(2*a)
    rt(45)
    fd(d)
    end_poly()
    addshape("rhombus1", get_poly())
    home()
    left(135)
    fd(d/2.0)
    begin_poly()
    lt(90)
    fd(d)
    lt(135)
    fd(2*a)
    lt(45)
    fd(d)
    end_poly()
    addshape("rhombus2", get_poly())
    tracer(1)
    ht()

class TStein(Turtle):
    def __init__(self, size, shape="arrow", clickable=True):
        Turtle.__init__(self)
        self.mode("logo")
        self.tracer(0)
        self.size = size
        self.pu()
        self.shape(shape)
        self.resizemode("user")
        self.turtlesize(size,size,3)
        #self.speed(0)
        self.clicktime = -1
        if clickable:
            self.onclick(self.turnleft, 2)
            self.onclick(self.turnright, 3)
            self.onclick(self.store, 1)
            self.ondrag(self.move, 1)
            self.onrelease(self.match, 1)
    def turnleft(self,x,y):
        self.lt(15)
    def turnright(self,x,y):
        self.rt(15)
    def store(self,x,y):
        self.clickpos = Vec(x,y)
    def move(self,x,y):
        self.tracer(0)
        neu = Vec(x,y)
        self.goto(self.pos() + (neu-self.clickpos))
        self.clickpos = neu
        self.tracer(1)
        self.update()
    def place(self, x, y, h):
        self.goto(x,y)
        self.setheading(h)
    def match(self,x,y):
        matching = False
        for cand in STiles:
            if self.size == cand.size and self.shape() == cand.shape():
                if self.distance(cand) < 20:
                    i = STiles.index(cand)
                    if i < 5 and self.heading() == cand.heading():
                        matching = cand
                    elif (i in [0,1] and
                          STiles[0].distance(STiles[1])<5
                          and (self.heading()-cand.heading())%90==0):
                        matching = cand
                    elif (i in [3,4] and
                          STiles[3].distance(STiles[4])<5
                          and (self.heading()-cand.heading())%90==0):
                        matching = cand
                    elif i == 5 and (self.heading()-cand.heading())%90 == 0:
                        matching = cand
                    elif (i == 6 and self.flipped == cand.flipped and
                          (self.heading()-cand.heading())%180 == 0):
                        matching = cand
                    if matching:
                        self.setpos(cand.pos())
                        break

class TRhombus(TStein):
    def __init__(self, clickable=True):
        TStein.__init__(self, 1, shape="rhombus1", clickable=clickable)
        self.flipped = False
        self.mode("logo")
        self.pu()
    def flip(self):
        if not self.flipped:
            self.shape("rhombus2")
            self.flipped = True
        else:
            self.shape("rhombus1")
            self.flipped = False
    def store(self, x, y):
        clicktime = time.clock()
        if clicktime - self.clicktime < 0.4:
            self.flip()
            self.clicktime = -1
        else:
            self.clicktime = clicktime
        self.clickpos = Vec(x,y)
        
def init():
    global TTiles, STiles
    tracer(0)
    makerhombusshapes()
    bgcolor("gray10")
    STiles = [TStein(A/20., clickable=False),
              TStein(A/20., clickable=False),
              TStein(2*d/20., clickable=False),
              TStein(A/40., clickable=False),
              TStein(A/40., clickable=False),
              TStein(d/20., "square", clickable=False),
              TRhombus(clickable=False)]
    TTiles = [TStein(A/20.),
              TStein(A/20.),
              TStein(2*d/20.),
              TStein(A/40.),
              TStein(A/40.),
              TStein(d/20., "square"),
              TRhombus()]
    for s in STiles:
        s.color((1,1,0.9))
        s.turtlesize(s.size, s.size, 2)
        s.ht()
    tracer(1)
    ht()
    goto(-390,-288)
    pencolor("gray70")
    write("Inspired by Pawel Boytchev's Elica-Logo implementation of the tangram game",
          font=("Courier", 10, "bold"))
    nextBtn = Button("next.gif", resetgame)
    nextBtn.setpos(320,220)
    helpBtn = Button("help.gif", helpme)
    helpBtn.setpos(320,-220)

def resetTiles():
    c1, c2, c3 = random.random()/2, random.random()/2, random.random()/2
    arrangeTiles(startdata, TTiles)
    if TTiles[6].flipped:
        TTiles[6].flip()
    if STiles[6].flipped:
        STiles[6].flip()
    for i in range(7):
        TTiles[i].pencolor(c1, c2, c3) 
        TTiles[i].fillcolor(c1+random.random()/2, c2+random.random()/2, c3+random.random()/2) 

def arrangeTiles(data, tileset):
    flip = data[-1] == -1
    l = data[:7]
    for i in range(7):
        x,y,h = data[i]
        if i==6 and flip:
            tileset[6].flip()
        tileset[i].place(x, y, h)

def resetgame():
    data = random.choice(tangramdata)
    tracer(0)
    resetTiles()
    arrangeTiles(data, STiles)
    tracer(1)
    ht()
    for t in TTiles:
        t.st()
    for t in STiles:
        t.st()
    tracer(1)
    update()

def helpme():
    tracer(0)
    c = STiles[0].pencolor()
    x,y,s = STiles[0].turtlesize()
    for t in STiles:
        t.pencolor("black")
        t.turtlesize(t.size, t.size, 1)
    tracer(1)
    update()
    time.sleep(0.5)
    tracer(0)
    for t in STiles:
        t.pencolor(c)
        t.turtlesize(t.size, t.size,s)
    tracer(1)
    update()

def main():    
    init()    
    resetgame()
    return "EVENTLOOP"

if __name__ == "__main__":
    msg = main()
    print msg
    mainloop()
