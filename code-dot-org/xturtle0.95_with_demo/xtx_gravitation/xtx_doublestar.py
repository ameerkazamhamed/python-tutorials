#!/usr/bin/python
"""       xturtle-example-suite:

             xtx_doublestar.py

Gravitational system simulation using the
approximation method from Feynman-lectures,
p.9-8, using turtlegraphics

Example: heavy bodies of equal mass, moving
around the center of mass of the system.

"""
from xturtle import Vec, Turtle, mainloop
from time import sleep

G = 8

class GravSys(object):
    def __init__(self):
        self.planets = []
        self.dt = 0.002
    def init(self):
        for p in self.planets:
            p.init()
    def start(self):
        for i in range(100000):
            for p in self.planets:
                p.step()
            
class Star(Turtle):
    def __init__(self, m, x, v, gravSys, shape):
        Turtle.__init__(self, shape)
        self.penup()
        self.m = m
        self.setpos(x)
        self.v = v
        gravSys.planets.append(self)
        self.gravSys = gravSys
        self.resizemode("user")
        self.pendown()
    def init(self):
        dt = self.gravSys.dt
        self.a = self.acc()
        self.v = self.v + 0.5*dt*self.a
    def acc(self):
        a = Vec(0,0)
        for planet in self.gravSys.planets:
            if planet != self:
                v = planet.pos()-self.pos()
                a += (G*planet.m/abs(v)**3)*v
        return a
    def step(self):
        dt = self.gravSys.dt
        self.setpos(self.pos() + dt*self.v)
        self.v = self.v + dt*self.acc()

def main():
    ## setup gravitational system
    gs = GravSys()
    sun1 = Star(400000, Vec(-150,0), Vec(0,-80), gs, "circle")
    sun1.color("red")
    sun2 = Star(400000, Vec(150,0), Vec(0,80), gs, "circle")
    sun2.color("orange")
    sun1.tracer(5,0)
    gs.init()
    gs.start()

if __name__ == '__main__':
    main()
    mainloop()

