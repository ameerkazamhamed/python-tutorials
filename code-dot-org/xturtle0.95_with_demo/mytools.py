# -*- coding: cp1252 -*-
# Autor: Gregor Lingl
# Datum: 3. 8. 2006
# mytools.py : Bibliothek von selbst erstellten
# brauchbaren Funktionen f�r die Arbeit mit
# Python f�r Kids.

from xturtle import *

def jump(distanz, winkel=0):
    penup()
    right(winkel)
    forward(distanz)
    left(winkel)
    pendown()

def strichel(laenge, striche=10):
    spruenge = striche - 1
    strich = laenge / (striche + spruenge)
    for i in range(spruenge):
        forward(strich)
        jump(strich)
    forward(strich)
    
def krange(start,stop,step=1.0):
    """f�r start < stop und step > 0
    """
    zahlenliste = []
    element = float(start) # macht aus start sicher
                           # eine Kommazahl!
    while element < stop:
        zahlenliste.append(element)
        element = element + step
    return zahlenliste
