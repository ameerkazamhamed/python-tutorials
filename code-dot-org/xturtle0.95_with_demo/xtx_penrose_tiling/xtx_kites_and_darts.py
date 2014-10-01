#!/usr/bin/python
"""       xturtle-example-suite:

          xtx_kites_and_darts.py

Constructs two aperiodic penrose-tilings,
consisting of kites and darts, by the method
of inflation in six steps.

Starting points are the patterns "sun"
consisting of five kites and "star"
consisting of five darts.

For more information see:
 http://en.wikipedia.org/wiki/Penrose_tiling
 -------------------------------------------  
"""
from xturtle import *
from math import cos, pi
from time import clock, sleep

f = (5**0.5-1)/2.0   # (sqrt(5)-1)/2 -- goldener Schnitt
d = 2 * cos(3*pi/10)

def kite(l):
    fl = f * l
    lt(36)
    fd(l)
    rt(108)
    fd(fl)
    rt(36)
    fd(fl)
    rt(108)
    fd(l)
    rt(144)

def dart(l):
    fl = f * l
    lt(36)
    fd(l)
    rt(144)
    fd(fl)
    lt(36)
    fd(fl)
    rt(144)
    fd(l)
    rt(144)

def inflatekite(l, n):
    if n == 0:
        px, py = pos()
        h, x, y = int(heading()), round(px,3), round(py,3)
        tiledict[(h,x,y)] = True
        return
    fl = f * l
    lt(36)
    inflatedart(fl, n-1)
    fd(l)
    rt(144)
    inflatekite(fl, n-1)
    lt(18)
    fd(l*d)
    rt(162)
    inflatekite(fl, n-1)
    lt(36)       
    fd(l)
    rt(180)
    inflatedart(fl, n-1)
    lt(36)

def inflatedart(l, n):
    if n == 0:
        px, py = pos()
        h, x, y = int(heading()), round(px,3), round(py,3)
        tiledict[(h,x,y)] = False
        return
    fl = f * l
    inflatekite(fl, n-1)
    lt(36)
    fd(l)
    rt(180)
    inflatedart(fl, n-1)
    lt(54)
    fd(l*d)
    rt(126)
    inflatedart(fl, n-1)
    fd(l)
    rt(144)

def draw(l, n, th=2):
    clear()
    l = l * f**n
    turtlesize(l/100.0, l/100.0, th)    
    for k in tiledict:
        h, x, y = k
        setpos(x, y)
        setheading(h)
        if tiledict[k]:
            shape("kite")
            color("black", "green")
        else:
            shape("dart")
            color("black", "red")
        stamp()

def sun(l, n):
    for i in range(5):
        inflatekite(l, n)
        lt(72)

def star(l,n):
    for i in range(5):
        inflatedart(l, n)
        lt(72)

def makeshapes():
    tracer(0)
    begin_poly()
    kite(100)
    end_poly()
    addshape("kite", get_poly())
    begin_poly()
    dart(100)
    end_poly()
    addshape("dart", get_poly())
    tracer(1)
    
def start():
    #winsize(800, 800)
    reset()
    ht()
    pu()
    makeshapes()
    resizemode("user")
    
def test(l=200, n=4, fun=sun, th=2):
    global tiledict
    home()
    setheading(0)
    tiledict = {}
    a = clock()
    tracer(0)
    fun(l, n)
    b = clock()
    draw(l, n, th)
    tracer(1)
    c = clock()
    print "Rechnen:   %7.4f s" % (b - a)
    print "Zeichnen:  %7.4f s" % (c - b)
    print "Insgesamt: %7.4f s" % (c - a)
    nk = len([x for x in tiledict if tiledict[x]])
    nd = len([x for x in tiledict if not tiledict[x]])
    print "%d kites und %d darts = zusammen %d Teile." % (nk, nd, nk+nd)

def demo(fun=sun):
    start()
    for i in range(8):
        a = clock()
        test(300, i, fun)
        b = clock()
        t = b - a
        if t < 4:
            sleep(4 - t)
        
def main():
    #title("Penrose-Parkettierung mit Kites und Darts.")
    mode("logo")
    demo(sun)
    sleep(4)
    demo(star)
    pencolor("black")
    goto(0,-200)
    pencolor((1,0.9,0.7))
    write("Please wait...",
          align="center", font=('Arial Black', 36, 'bold'))
    test(600, 8)
    return "Done"

if __name__ == "__main__":
    msg = main()
    mainloop()
    
