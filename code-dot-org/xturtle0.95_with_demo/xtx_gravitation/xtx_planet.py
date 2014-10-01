#!/usr/bin/python
"""       xturtle-example-suite:

             xtx_planet.py

Gravitational system simulation using the
approximation method from Feynman-lectures,
p.9-8, using turtlegraphics

Example: heavy central body, light planet,
Note the (small) movement of the sun!

Demostrates two features of the xturtle
module:
(1) use of "compound turtle shapes"-
planets consist of two semicircles of
different colour.
(2) Vec class (derived from tuple) allows
for a very concisev formulation of the orbit
calculation algorithm. (Note that methods
like pos() return Vec-s.)
"""
from xturtle import Vec, Shape, Turtle, mainloop
from time import sleep

G = 8

class GravSys(object):
    def __init__(self):
        self.planets = []
        self.dt = 0.01
    def init(self):
        for p in self.planets:
            p.init()
    def start(self):
        for i in range(10000):
            for p in self.planets:
                p.step()
            
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
## yellow semicircle will point towards the sun
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
    s.tracer(True,0)
    s.ht()
    

def main():
    global sun
    createPlanetShape()
    ## setup gravitational system
    gs = GravSys()
    sun = Star(1000000, Vec(50,0), Vec(0,-3.5), gs, "circle")
    sun.color("yellow")
    sun.turtlesize(1.8)
    sun.pu()
    earth = Star(10000, Vec(150,0), Vec(0,350), gs, "planet")
    earth.pencolor("green")
    gs.init()
    gs.start()
    return "Done!"

if __name__ == '__main__':
    msg = main()
    print msg
    mainloop()

