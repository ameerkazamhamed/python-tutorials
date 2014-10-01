#!/usr/bin/python
"""       xturtle-example-suite:

             xtx_planets.py

Gravitational system simulation using the
approximation method from Feynman-lectures,
p.9-8, using turtlegraphics.

Example: heavy central body, light planet,
very light second planet! This one will be
deflected several times by the gravitational
force exerted by the first planet.

You can hold the movement temporarily by
pressing the left mouse button with mouse
on the scrollbar of the canvas.

"""
from xturtle import Vec, Shape, Turtle, mainloop
from time import sleep

G = 8   # gravitational constant

class GravSys(object):
    def __init__(self):
        self.planets = []
        self.dt = 0.01
    def init(self):
        for planet in self.planets:
            planet.init()
    def start(self):
        for i in range(20000):
            for planet in self.planets:
                planet.step()
            
class Star(Turtle):
    def __init__(self, m, x, v, gravSys, shape):
        Turtle.__init__(self, shape)
        self.resizemode("user")
        gravSys.planets.append(self)
        self.gravSys = gravSys
        self.dt = self.gravSys.dt
        self.penup()
        self.m = m
        self.setpos(x)
        self.vel = v
        self.pendown()
    def init(self):
        self.vel = self.vel + 0.5*self.dt*self.acc()
    def acc(self):
        a = Vec(0,0)
        for planet in self.gravSys.planets:
            if planet != self:
                r = planet.pos()-self.pos()
                a += (G*planet.m/abs(r)**3)*r
        return a
    def step(self):
        self.setpos(self.pos() + self.dt*self.vel)
        if self != sun:
            self.setheading(self.towards(sun))
        self.vel = self.vel + self.dt*self.acc()

## create compound yellow/blue turtleshape for planets
## yellow semicircle will always point towards the sun
def createPlanetShape():
    s = Turtle()
    s.tracer(0,0)
    s.ht()
    s.pu()
    s.fd(6)
    s.lt(90)
    s.begin_poly()
    s.circle(6, 180)
    s.end_poly()
    m1 = s.get_poly()
    s.begin_poly()
    s.circle(6,180)
    s.end_poly()
    m2 = s.get_poly()

    planetshape = Shape("compound")
    planetshape.addcomponent(m1,"orange")
    planetshape.addcomponent(m2,"blue")
    s.addshape("planet", planetshape)
    s.tracer(1,0)
    s.ht()

def main():
    global sun
    createPlanetShape()
    ## setup gravitational system
    gs = GravSys()
    sun = Star(1000000, Vec(0,0), Vec(0,-3.5), gs, "circle")
    sun.color("yellow")
    sun.turtlesize(1.8)
    sun.pu()
    earth = Star(10000, Vec(100,0), Vec(0,350), gs, "planet")
    earth.pencolor("green")
    venus = Star(4, Vec(-80,0), Vec(0,-350), gs, "planet")
    venus.pencolor("blue")
    venus.turtlesize(0.7)
    gs.init()
    gs.start()
    return "Done!"

if __name__ == '__main__':
    msg = main()
    print msg
    mainloop()
