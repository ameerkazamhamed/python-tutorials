#!/usr/bin/python
"""       xturtle-example-suite:

          xtx_penrose_animation.py

Animated construction of a penrose-tilings,
using and visualizing composition rules.

Contributed by Wolfgang Urban:
    http://www.hib-wien.at/leute/wurban/

For more information on penrose tilings see:
 http://en.wikipedia.org/wiki/Penrose_tiling
 -------------------------------------------  
"""
from xturtle import *
import math
import time

SPEED = 4

PHI = (1.0+5.0**0.5)/2.0
W = math.pi/180.0

###############################
# create kite and dart turtles
###############################

class MyPen(Pen):
    def __init__(self,size,homepos):
        Pen.__init__(self)
        self.mode("logo")
        self.speed(SPEED)
        self.homepos = homepos
        self.st()
        self.pu()
        self.s = size
        self.resizemode("auto")
        self.width(3)
        self.turtlesize(1,1,3)
        self.rest()

    # forward scaled
    def walk(self,d): self.fd(self.s*d)

    # go to resting position
    def rest(self): self.setpos(self.homepos)

    # enter the game, home()
    def act(self): self.setpos(0,0)

    # walk a path
    def travel(self,path):
        for (length,angle) in path:
            self.walk(length)
            self.rt(angle)
        self.lastpath = path

    # travel backwards
    def backhome(self):
        self.lastpath.reverse()
        for (length,angle) in self.lastpath:
            self.lt(angle)
            self.walk(-length)
        self.lastpath = []

    # stamp n adjacent copies, symmetric
    def multistamp(self,n):
        self.lt((n-1)*72/2)
        for i in range(n-1):
            self.stamp()
            self.rt(72)
        self.stamp()
        self.lt((n-1)*72/2)
        
##############
# our turtles
##############

class Kite(MyPen):
    def __init__(self,s,myshape):
        MyPen.__init__(self,s,(250,-260))
        self.shape(myshape)
                              
class Dart(MyPen):
    def __init__(self,s,myshape):
        MyPen.__init__(self,s,(-250,-260))
        self.shape(myshape)


########################
# paint the Penrose sun    
########################

def sun(s=40,kite="kite0",dart="dart0"):

    # draw    
    k = Kite(s,kite)
    d = Dart(s,dart)
    
    k.act()
    for i in range(5):
        k.stamp()
        k.rt(72)
    k.rest()

    d.act()
    d.rt(36)
    for i in range(5):
        d.travel([(1+PHI,180)])
        d.stamp()
        d.backhome()
        d.rt(72)
    d.lt(36)
    d.rest()

    k.act()
    for i in range(5):
        k.travel([(PHI,0)])
        k.multistamp(2)
        k.backhome()
        k.rt(72)

    k.rt(36)
    for i in range(5):
        k.travel([(2*PHI+1,0)])
        for j in range(5):
            k.stamp()
            k.rt(72)
        k.backhome()
        k.rt(72)
    k.lt(36)
    k.rest()
    
    d.act()
    for i in range(5):
        d.travel([(2*PHI+1,-180)])
        d.multistamp(3)
        d.backhome()
        d.rt(72)
    d.rest()

    k.act()
    for i in range(5):
        k.travel([(2*PHI+1,-72),(PHI,36+72)])
        k.multistamp(2)
        k.backhome()
        k.travel([(2*PHI+1,72),(PHI,-36-72)])
        k.multistamp(2)
        k.backhome()
        k.rt(72)
    k.rest()
    
    d.act()
    d.rt(36)
    for i in range(5):
        d.travel([(2*PHI+1,-36),(PHI+1,180)])
        d.stamp()                 
        d.backhome()
        d.travel([(2*PHI+1,36),(PHI+1,180)])
        d.stamp()
        d.backhome()
        d.rt(72)
    d.lt(36)

    for i in range(5):
        d.travel([(3*PHI+2,180)])
        d.multistamp(2)
        d.backhome()
        d.rt(72)
        
    d.rest()

    k.ht()
    d.ht()

# shape with color arcs as "kite1", "dart1"
# ... could be cleaned up a little....
def buildshapes1(s):
    speed(10)
    mode("logo")
    s = s/PHI
    shape("turtle")

    # prepare kite shape
    pu()
    width(3)
    bk(60)
    color("black")
    write("the Penrose kite",font=("Arial",24),align="center")
    fd(60)

    myshape = Shape("compound")
    # black border
    polystart()
    pd()
    color("grey")
    lt(36)
    fd(s*(PHI+1))
    rt(108)
    fd(s*PHI)
    rt(36)
    fd(s*PHI)
    rt(108)
    fd(s*(PHI+1))
    rt(144)
    polyend()
    m1 = getpoly()
    myshape.addcomponent(m1,(1.0,0.9,0.9),"grey")
    # blue arc
    color("blue")
    pu()
    lt(36); fd(s*PHI); rt(90);
    polystart()
    pd(); circle(-s*PHI,72,10); pu()
    rt(180); circle(s*PHI,72,10);   # connect to starting point
    polyend()
    rt(90); bk(s*PHI); rt(36)
    m3 = getpoly()
    myshape.addcomponent(m3,"white","blue")
    # red arc
    color("red")
    pu()
    fd(s+s*PHI); rt(180-72); fd(s); rt(90)
    polystart()
    pd();
    circle(-s,72*2,10);
    rt(180);
    circle(s,72*2,10);
    pu()
    polyend()
    lt(90); fd(s); rt(72)
    bk(s+s*PHI)
    m2 = getpoly()
    myshape.addcomponent(m2,"white","red")
    # build    
    addshape("kite1",myshape)
    clear()

    # prepare dart shape
    pu()
    bk(60)
    color("black")
    write("the Penrose dart",font=("Arial",24),align="center")
    fd(60)

    width(3)
    myshape = Shape("compound")
    # black border
    polystart()
    color("grey")
    pd()
    lt(36)
    fd(s*(PHI+1))
    rt(144)
    fd(s*(1+1/PHI))
    lt(36)
    fd(s*(1+1/PHI))
    rt(144)
    fd(s*(PHI+1))
    rt(144)
    polyend()
    m1 = getpoly()
    myshape.addcomponent(m1,(0.9,0.9,1),"grey")
    # blue arc
    color("blue")
    pu()
    lt(36); fd(s); rt(90);
    polystart()
    pd(); circle(-s,72,10); pu()
    rt(180); circle(s,72,10);   # connect to starting point
    polyend()
    rt(90); bk(s); rt(36)
    m3 = getpoly()
    myshape.addcomponent(m3,"white","blue")
    # red arc
    color("red")
    pu()
    fd(s+s/PHI); rt(72); fd(s/PHI); rt(90)
    polystart()
    pd();
    circle(-s/PHI,216,10);
    rt(180);
    circle(s/PHI,216,10);
    pu()
    polyend()
    lt(90); fd(s/PHI); rt(108)
    bk(s+s/PHI)
    m2 = getpoly()
    myshape.addcomponent(m2,"white","red")
    # build    
    addshape("dart1",myshape)
    ht()

#######################################################################
# demo
#######################################################################

def main():
    s=40
    # prepare window
##    winsize(650,650)
##    screensize(650-50,650-50)
    reset()
    mode("logo")

    # basic patterns
    clearscreen()       # !!! doesn't work
##    buildshapes0(s)
##    clear()
##    sun(40,"kite0","dart0")

    # circle pattern
    buildshapes1(s)
    clear()
    sun(40,"kite1","dart1")
    return "Done!"
    
if __name__ == "__main__":
    main()
    mainloop()
