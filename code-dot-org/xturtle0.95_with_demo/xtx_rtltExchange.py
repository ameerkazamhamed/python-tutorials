#!/usr/bin/python
"""       xturtle-example-suite:

             rtltExchange.py

A tiny practical joke:

One of two pens has its right and
left methods exchanged. Performing
the same commands they draw a picture
and its reflexion.
"""
from xturtle import *

def main():
    p=Pen()
    p.pensize(5)
    p.left(90)
    p.up()
    p.bk(80)
    p.down()

    q=p.clone()
    p.color("#e40", "#04e")
    q.color("#04e", "#e40")

    q.right, q.left = q.left, q.right

    for t in p, q:
        t.right(90)
        t.fd(2.5)
        t.left(90)
        t.fd(60)
        t.right(45)
        t.forward(50)
        t.right(90)
        t.fill(True)
    for i in range(48):
        for t in p,q:
            t.forward(10)
            t.left(7.5)
    for t in p, q: t.fill(False)
    return "Done!"
        
if __name__=='__main__':
    msg = main()
    print msg
    mainloop()
