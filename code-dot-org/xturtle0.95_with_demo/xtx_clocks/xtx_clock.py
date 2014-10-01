#!/usr/bin/python
# -*- coding: cp1252 -*-
"""       xturtle-example-suite:

              xtx_clock.py

Enhanced clock-program, showing date
and time
  ------------------------------------
   Press STOP to exit the program!
  ------------------------------------
"""
from xturtle import *
from mytools import jump
from datetime import datetime

#mode("logo")

def zeiger(laenge, spitze):
    fd(laenge*1.15)
    rt(90)
    fd(spitze/2.0)
    lt(120)
    fd(spitze)
    lt(120)
    fd(spitze)
    lt(120)
    fd(spitze/2.0)

def mache_zeiger_shape(name, laenge, spitze):
    reset()
    mode("logo")
    jump(-laenge*0.15)
    polystart()
    zeiger(laenge, spitze)
    polyend()
    zeiger_form = getpoly()
    addshape(name, zeiger_form)


def ziffernblatt(radius):
    reset()
    pensize(7)
    for i in range(60):
        jump(radius)
        if i % 5 == 0:
            fd(25)
            jump(-radius-25)
        else:
            dot(3)
            jump(-radius)
        rt(6)

def setup():
    global sekundenzeiger, minutenzeiger, stundenzeiger, writer
    #winsize(400, 400)
    mode("logo")
    mache_zeiger_shape("sekundenzeiger", 125, 25)
    mache_zeiger_shape("minutenzeiger",  130, 25)
    mache_zeiger_shape("stundenzeiger", 90, 25)
    ziffernblatt(160)
    sekundenzeiger = Turtle(mode="logo")
    #sekundenzeiger.mode("logo")
    sekundenzeiger.shape("sekundenzeiger")
    sekundenzeiger.color("gray20", "gray80")
    minutenzeiger = Turtle(mode="logo")
    minutenzeiger.shape("minutenzeiger")
    #minutenzeiger.mode("logo")
    minutenzeiger.color("blue1", "red1")
    stundenzeiger = Turtle(mode="logo")
    stundenzeiger.shape("stundenzeiger")
    #stundenzeiger.mode("logo")
    stundenzeiger.color("blue3", "red3")
    for zeiger in sekundenzeiger, minutenzeiger, stundenzeiger:
        zeiger.resizemode("user")
        zeiger.turtlesize(1, 1, 3)
        zeiger.speed(0)
    ht()
    writer = Turtle()
    #writer.mode("logo")
    writer.ht()
    writer.pu()
    writer.bk(85)
    

def wochentag(t):
    wochentag = ["Montag", "Dienstag", "Mittwoch",
        "Donnerstag", "Freitag", "Samstag", "Sonntag"]
    return wochentag[t.weekday()]

def datum(z):
    wochentag = ["Montag", "Dienstag", "Mittwoch",
        "Donnerstag", "Freitag", "Samstag", "Sonntag"]
    monat = ["Jan.", "Feb.", "März", "Apr.", "Mai", "Juni",
             "Juli", "Aug.", "Sep.", "Okt.", "Nov.", "Dez."]
    j = z.year % 100
    m = monat[z.month - 1]
    t = z.day
    return "%d. %s %02d" % (t, m, j)
    
def tick():
    t = datetime.today()
    sekunde = t.second + t.microsecond*0.000001
    minute = t.minute + sekunde/60.0
    stunde = t.hour + minute/60.0
    tracer(False)
    writer.clear()
    writer.home()
    writer.forward(65)
    writer.write(wochentag(t),
                 align="center", font=("Courier", 14, "bold"))
    writer.back(150)
    writer.write(datum(t),
                 align="center", font=("Courier", 14, "bold"))
    writer.forward(85)
    tracer(True)
    sekundenzeiger.setheading(6*sekunde)
    minutenzeiger.setheading(6*minute)
    stundenzeiger.setheading(30*stunde)
    tracer(True)
    ontimer(tick, 100)

def main():
    #title("xturtle clock")
    tracer(False)
    setup()
    tracer(True)
    tick()
    return "EVENTLOOP"
    
if __name__ == "__main__":
    msg = main()
    print msg
    #mainloop()
