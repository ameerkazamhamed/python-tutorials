#!/usr/bin/python
"""       xturtle-example-suite:

             xtx_plotter.py

This example was originally developed for
interactive use to plot arbitrary
(differentiable :-) ) functions along with
their derivatives. You may easily use it
from within IDLE, provided xturtle.py is
on your sys.path

Here it's used to plot sine (and cosine).

After plotting the graphs the program goes
into EVENTLOOP mode and responds to mouse
clicks. Try it out!

Hint: You may find it useful to enlarge your
         xturtleDemo-window

  ---------------------------------------
  Play around by clicking into the canvas
  ---------------------------------------
        To exit press STOP button
  ---------------------------------------      
"""
from xturtle import *

WIDTH = 720.0
HEIGHT = 480.0

def frange(_from, _to, delta):
    return [_from+i*delta for i in range(1+int((_to-_from)/delta))]

def graph( f, _from, _to, delta ):
    return [(x,f(x)) for x in frange(_from, _to, delta)]

def derivative(f, h=1e-8):
    def f1(x):
        return (f(x+h)-f(x))/h
    return f1

class Plotter:
    def __init__(self):
        self.p = Turtle()
        self.k = Turtle()
        self.c = Turtle()
        self.k.tracer(0)
        self.k.pencolor("blue")
        self.k.fillcolor(0.8,0.8,0.9)
        self.k.ht()

    def setup(self, f, _from, _to, steps=120, yfrac=1.0):
        for t in self.p, self.k, self.c:
            t.clear()
        self._from = _from
        self._to = _to
        self.steps = steps
        self.yfrac = yfrac
        self.delta = 1.0*(_to-_from)/steps
        self.f = f
        self.g = graph(f,_from,_to,self.delta)
        self.f1 = derivative(f)
        self.g1 = graph(self.f1,_from,_to,self.delta)
        self.yrange = [y for (x,y) in self.g]
        self.ex = WIDTH/(_to-_from)
        self.ey = self.yfrac*HEIGHT / (max(self.yrange) - min(self.yrange))
        self.ox = -WIDTH/2.0-_from*self.ex
        self.oy = -self.yfrac*HEIGHT/2.0-min(self.yrange)*self.ey
        self.plotcoosys()
        self.plot(self.g)
        self.plot(self.g1, "red")
        self.p.update()
        self.p.getscreen().onclick(self.slope,1)

    def screen(self,x,y):
        return (self.ox+self.ex*x, self.oy+self.ey*y)

    def plotcoosys(self):
        p = self.c
        p.clear()
        p.ht()
        p.up(); p.goto(self.screen(self._from,0))
        p.pd(); p.goto(self.screen(self._to,0));
        p.pu(); p.goto(self.screen(0,min(self.yrange)));
        p.pd(); p.goto(self.screen(0,max(self.yrange)));
        p.pu(); p.goto(self.screen(0,1)); p.bk(6); p.pd(); p.fd(12)
        p.pu(); p.goto(self.screen(1,0)); p.lt(90); p.bk(6); p.pd(); p.fd(12); p.rt(90)
        p.pu()
        
    def plot(self, g, pencol="black"):
        p = self.p
        p.pencolor(pencol)
        p.pu()
        for (x,y) in g:
            p.goto(self.screen(x,y))
            if self.steps < 150:
                p.dot(4)
            p.pd()
        p.up()

    def slope(self, x, y):
        f, f1 = self.f, self.f1
        k = self.k
        x = self._from + (x+WIDTH/2.0)/self.ex
        k.pencolor("blue")
        k.pu()
        k.clear()
        k.goto(self.screen(x+1, f(x)))
        k.pensize(3)
        k.pd()
        k.fill(True)
        k.goto(self.screen(x+1, f(x)+f1(x) ))
        k.pu()
        k.goto(self.screen(x,f1(x)))
        k.pd()
        k.goto(self.screen(x,0))
        k.pu()
        k.goto(self.screen(x+1, f(x)))
        k.fill(False)
        k.pd()
        k.pensize(1)
        k.goto(self.screen(x, f(x)))
        k.pu()        
        k.goto(self.screen(x+1, f(x)+f1(x) ))
        k.pd()
        k.pensize(2)
        k.pencolor(0,0.7,0)
        k.goto(self.screen(x-1,f(x)-f1(x)))
        # redraw curve
        k.pensize(1)
        k.pencolor("black")
        k.pu()
        for (x1,y1) in self.g:
            if x-self.delta <= x1 <= x+1+self.delta:
                k.goto(self.screen(x1,y1))
                if self.steps < 150:
                    k.dot(4)
                k.pd()
        k.pencolor("red")
        k.pu()
        for (x1,y1) in self.g1:
            if x-self.delta <= x1 <= x+1+self.delta:
                k.goto(self.screen(x1,y1))
                if self.steps < 150:
                    k.dot(4)
                k.pd()
        k.pu()
        self.plotcoosys()
        k.update()
        
def main():        
    from math import cos
    p = Plotter()
    p.setup(cos,-1.6,3.2)
    return "EVENTLOOP"

if __name__ == '__main__':
    msg = main()
    print msg
    mainloop()
