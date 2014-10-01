# -*- coding: cp1252 -*-
docsdict = {

'pensize' :
"""Setze Strichdicke width / ohne Argument: gib Strichdicke zur�ck.
        Alias-Namen: pensize | width
	Wenn resizemode auf 'auto' gestellt ist und die Turtleshape
	ein Polygon ist, wird das Polygon mit derselben Strichdicke
	dargestellt.
        ---
        (Optionales) Argument: positive Zahl
        
        Aufruf: pensize(<positive Zahl>)
        
        Beispiel (f�r ein Turtle-Objekt namens turtle):
        
        >>> turtle.pensize()
        1
        turtle.pensize(10)  # von hier weg werden Linien mit
                            # Strichdicke 10 Pixel gezeichnet.       
""",

'penup' :
"""Hebe Zeichenstift an. Zeichne nicht bei nachfolgenden Bewegungen.
        Alias-Namen: penup | pu | up
        ---
        Kein Argument
        
        Beispiel (f�r ein Turtle-Objekt namens turtle):
        
        >>> turtle.penup()        
""",

'isdown' :
"""Gib True zur�ck, wenn Zeichenstift unten ist, False wenn er oben ist.
        Alias-Namen: isdown | pendownp
        ---
        Kein Argument.

        Beispiel (f�r ein Turtle-Objekt namens turtle):
        >>> turtle.penup()
        >>> turtle.isdown()
        False
        >>> turtle.pendown()
        >>> turtle.isdown()
        True        
""",

'color' :
"""Setze Zeichen- und F�llfarbe / gib sie (als Paar) zur�ck.
	Wenn die Turtle-Gestalt durch ein Polygon festgelegt wird,
	wird der Rand und das Innere in diesen Farben dargestellt.
	
        Argumente:
        Verschiedene Eingabeformate sind erlaubt:
	Sie verwenden 0, 1, 2, 3 oder 6 Argumente wie folgt:.
          - color()
	    gibt die aktuelle Zeichenfarbe und die aktuelle F�llfarbe
	    als Paar von Farb-Strings zur�ck, wie sie con pencolor bzw.
	    fillcolor zur�ckgegeben werden.
          - color(s), color((r,g,b)), color(r,g,b)
	    Eingaben wie in pencolor. Setzt sowohl die Zeichenfarbe wie
	    auch die F�llfarbe auf den gegebenen Wert.
          - color(s1, s2),
            color((r1,g1,b1), (r2,g2,b2))
            color(r1, g1, b1, r2, g2, b2)
	    Gleichwertig mit pencolor(s1) und fillcolor(s2) und entsprechend
	    falls f�r die Argumente die anderen Formate verwendet werden.
        
        Aufruf: color(<colorstring>)
        --oder: color(<colorstring>, <colorstring>)
        --oder mit <zahl>en im Bereich 0 .. colormode (d.h. 1.0 or 255):
        -     color((<zahl>, <zahl>, <zahl>))
        -     color((<zahl>, <zahl>, <zahl>), (<zahl>, <zahl>, <zahl>))
        -     color((<zahl>, <zahl>, <zahl>, <zahl>, <zahl>, <zahl>))
        -     color()        
        
        Beispiel (f�r ein Turtle-Objekt namens turtle):
        
        >>> turtle.color('red', 'green')
        >>> turtle.color()
        ('red', 'green')
        >>> colormode(255)
        >>> color(40, 80, 120, 160, 200, 240)
        >>> color()
        ('#285078', '#a0c8f0')   
""",

'pendown' :
"""Setze Zeichenstift nach unten. Zeichne bei nachfolgenden Bewegungen.        
        Alias-Namen: pendown | pd | down
        ---
        Kein Argument
        
        Beispiel (f�r ein Turtle-Objekt namens turtle):
        >>> turtle.pendown()        
""",

'turtlesize' :
"""Setze/gib zur�ck: x/y-stretch-Faktoren bzw. outline der Turtleform,
	wenn resizemode auf "user" gesetzt ist.
	Wenn stretchx=sx und stretchy=sy ist, wird die Turtle-Gestalt
	um den Faktor sx senkrecht zur Bewegungsrichtung und
	um den Faktor sy in Bewgungsrichtung getreckt dargestellt.
	Die Umrisslinie wird mit der Strichdicke outline dargestellt.
        ---
        (Optionale) Argumente:
           stretchx : positive Zahl
           stretchy : positive Zahl
           outline  : positive Zahl

        Aufruf: turtlesize(<zahl>)
          oder: turtlesize(<zahl>, <zahl>)
          oder: turtlesize(<zahl>, <zahl>, <zahl>)
          oder: turtlesize()
        oder auch mit Schl�sselwortartgumenten:
                turtlesize(5, outline=8)
        
        Beispiele (f�r ein Turtle-Objekt namens turtle):
        
        >>> turtle.resizemode("user")
        >>> turtlesize(5, 8)
        >>> turtlesize(outline=12)
        >>> turtlesize()
        (5, 8, 12)        
""",

'fillcolor' :
""" Setze/gib zur�ck: die F�llfarbe. 
	Wenn die Turtle-Gestalt durch ein Polygon festgelegt wird,
	wird der Innere in dieser Farbe dargestellt.
	---
        Argumente:
        Vier Eingabeformate sind erlaubt:
          - fillcolor()
	    gibt die aktuelle F�llfarbe als Farb-String zur�ck,
	    m�glicherweise im Hexadezimalzahl-Format (sieheauch pencolor).
	    Kann als Argument f�r einen nachfolgenden Aufruf von
	    color/pencolor/fillcolor verwendet werden.
          - fillcolor(s)
            s ist ein Tkinter-Farbname wie z. B.: "red" oder "yellow"
          - fillcolor((r, g, b))
            *ein Tuple* von Zahlen r, g, and b, die eine RGB-Farbe darstellen.
            Jede der drei Zahlen r, g, and b muss im Bereich 0..colormode
	    liegen, wobei colormode entweder 1.0 oder 255 ist.
          - fillcolor(r, g, b)
            r, g, und b stellen jeweils eine RGB-Farbe durch eine Zahl im
	    Bereich 0..colormode dar.
        
        Aufruf: fillcolor(<colorstring>)
        --oder mit <zahl>en im Bereich 0 .. colormode (d. h. 1.0 oder 255)
        -     fillcolor(<zahl>, <zahl>, <zahl>)
        -     fillcolor((<zahl>, <zahl>, <zahl>))
        -     fillcolor()        
        
        Beispiel (f�r ein Turtle-Objekt namens turtle):
        
        >>> turtle.fillcolor('violet')
        >>> tup = turtle.pencolor()
        >>> turtle.fillcolor(tup)
        >>> turtle.fillcolor(0, .5, 0)
        
""",

'speed' :
"""Setze/gib zur�ck: Bewegungsgeschwindigkeit der Turtle (0 .. 10)
        Wenn das Argument eine Zahl gr��er als 10 oder kleiner als 0.5
	ist, wird speed auf 0 gesetzt.
	speed kann auch einer der folgenden f�nf Strings sein, die wie
	angegeben den Zahlenwerten von speed entsprechen:
            'fastest' :  0
            'fast'    :  10
            'normal'  :  6 
            'slow'    :  3
            'slowest' :  1
	speed.Werte im Bereich von 1 bis 10 bewirken eine zunehmend 
	schneller Animation der Turtle-Bewegung (auch der Drehung).
        ***************
        speed = 0 : KEINE ANIMATION! forward/back bewirken, dass die 
	Turtle vom Startpunkt zum Endpunkt springt. Entsprechend 
	bewirken left/right eine augenblicklichen Drfehung.
        Optionales Argument: ganze Zahl im Bereich 0 .. 10 oder einer der
        Strings 'fastest', 'fast', 'normal', 'slow', 'slowest'
        (aus Gr�nden der Kompatibilit�t mir turtle.py)
        ***************
        ---
        Optionales Argument: Zahl im Bereich 0..10, oder eine
	'speed-Zeichenkette' wie weiter oben beschrieben.
        
        Aufruf: speed(1)  # langsam
        --oder: speed(10) # schnellste Animation
        --oder: speed('fastest')
        --oder: speed(0)  # augenblickliche VErschiebung/Drehung der Turtle.
        
        Beispiel (f�r ein Turtle-Objekt namens turtle):
        
        >>> turtle.speed(3)       
""",

'resizemode' :
"""Setze/gib zur�ck: resize-Modus ("auto", "user" oder "noresize")
	Die verschiedenen resize-Modi haben folgende Wirkung:
          - "auto": passt die Gr��e der Turtle automatisch an den Wert
	            von pensize an.
          - "user": Darstellung der Turtle wird durch die Werte von
	            stretchfactor und outlinewidth festgelegt. Diese werden
		    durch die Funktion/Methode turtlesize() gesetzt.
          - "noresize" es findet keine Anpassung der Turtle-Darstellung statt.
        ---
        (Optionales) Argument: Eine der Zeichenketten
                "auto", "user", "noresize"
        
        Aufruf: resizemode("user") # zum Beispiel
        --oder: resizemode()
        
        Beispiel (f�r ein Turtle-Objekt namens turtle):
        
        >>> turtle.resizemode("noresize")
        >>> turtle.resizemode()
        'noresize'        
""",

'hideturtle' :
"""Macht die Turtle unsichtbar.
	Es ist eine gute Idee, dies w�hrend der Erstellung kompliziertzer
	Grafiken zu verwenden, weil das Verstecken der Turtle die
	Geschwindigkeit des Zeichenvoprgangs merkbar erh�ht.
        ---
        Kein Argument.
        
        Beispiel (f�r ein Turtle-Objekt namens turtle):
        
        >>> turtle.hideturtle()        
""",

'isvisible' :
"""Gib True zur�ck, wenn die Turtle sichtbar ist, False sonst.
        Alias-Namen: isvisible | shownp
        ---
        Kein Argument.
        
        Beispiel (f�r ein Turtle-Objekt namens turtle):

        >>> turtle.hideturtle()
        >>> if not turtle.isvisible():
                print "Turtle ist unsichtbar!"
                
        Turtle ist unsichtbar!
""",

'pencolor' :
"""Setze/gib zur�ck: die Zeichenfarbe. 
	Wenn die Turtle-Gestalt durch ein Polygon festgelegt wird,
	wird der Rand in dieser Farbe dargestellt.
        ---
        Argumente:
        Vier Eingabeformate sind erlaubt:
          - pencolor()
	    gibt die aktuelle Zeichenfarbe als Farb-String zur�ck,
	    m�glicherweise im Hexadezimalzahl-Format (siehe Beispiel).
	    Kann als Argument f�r einen nachfolgenden Aufruf von
	    color/pencolor/fillcolor verwendet werden.
          - pencolor(s)
            s ist ein Tkinter-Farbname wie z. B.: "red" oder "yellow"
          - pencolor((r, g, b))
            *ein Tuple* von Zahlen r, g, and b, die eine RGB-Farbe darstellen.
            Jede der drei Zahlen r, g, and b muss im Bereich 0..colormode
	    liegen, wobei colormode entweder 1.0 oder 255 ist.
          - pencolor(r, g, b)
            r, g, und b stellen jeweils eine RGB-Farbe durch eine Zahl im
	    Bereich 0..colormode dar.
        
        Aufruf: pencolor(<colorstring>)
        --oder mit <zahl>en im Bereich 0 .. colormode (i.e. 1.0 or 255)
        -     pencolor(<zahl>, <zahl>, <zahl>)
        -     pencolor((<zahl>, <zahl>, <zahl>))
        -     pencolor()        
        
        Beispiel (f�r ein Turtle-Objekt namens turtle):
                
        >>> turtle.pencolor('brown')
        >>> tup = (0.2, 0.8, 0.55)
        >>> turtle.pencolor(tup)
        >>> turtle.pencolor()
        '#33cc8c'       
""",

'pen' :
"""Setze/gib zur�ck: die Eigenschaften des Zeichenstiftes
        antsprechend dem als Argument �bergebenen Dictionarys
        und/oder der �bergebenen Schl�sselwort-Argumente.
        Wenn keine Argumente angegeben werden, 	wird das
        pen-Dictionary zur�ckgegeben.
	Das pen-Dictionary hat folgende Schl�ssel/Wert-Paare:
           "shown"      :   True/False
           "pendown"    :   True/False
           "pencolor"   :   color-string or color-tuple
           "fillcolor"  :   color-string or color-tuple
           "pensize"    :   positive number
           "speed"      :   number in range 0..10
           "resizemode" :   "auto" or "user" or "noresize"
           "stretchfactor": positive number
           "outline"    :   positive number        
        Dieses Dictionary kann als Argument f�r nachfolgende pen()-
	Aufrufe verwendet werden um einen fr�heren pen-Zustand wieder
	herzustellen. Mit Schl�sselwort-Argumenten k�nnen mehrere
	Turtle-Eigenschaften in einem Statement gesetzt werden.
	---
        Argumente:
            pen : Ein Dictionary mit einigen oder allen der oben aufgelisteten
	          Schl�ssel.
            **pendict : einige oder mehrer Schl�sselwort-Argumente mit
	          den oben aufgelisteten Schl�sseln als Schl�sselw�rtern.
                  
        Beispiele (f�r ein Turtle-Objekt namens turtle):
        
        >>> turtle.pen(fillcolor="black", pencolor="red", pensize=10)
        >>> turtle.pen()
        {'pensize': 10, 'shown': True, 'resizemode': 'auto', 'outline': 1,
        'pencolor': 'red', 'pendown': True, 'fillcolor': 'black',
        'stretchfactor': 1, 'speed': 3}
        >>> penstate=turtle.pen()
        >>> turtle.color("yellow","")
        >>> turtle.penup()
        >>> turtle.pen()
        {'pensize': 10, 'shown': True, 'resizemode': 'auto', 'outline': 1,
        'pencolor': 'yellow', 'pendown': False, 'fillcolor': '',
        'stretchfactor': 1, 'speed': 3}
        >>> p.pen(penstate, fillcolor="green")
        >>> p.pen()
        {'pensize': 10, 'shown': True, 'resizemode': 'auto', 'outline': 1,
        'pencolor': 'red', 'pendown': True, 'fillcolor': 'green',
        'stretchfactor': 1, 'speed': 3}        
""",

'showturtle' :
"""Macht die Turtle sichtbar.
        Alias-Namen: showturtle | st
        ---
        Kein Argument.
        
        Beispiel (f�r ein Turtle-Objekt namens turtle):
        
        >>> turtle.hideturtle()
        >>> turtle.showturtle()        
""",

'right' :
"""Drehe die Turtle um angle Winkeleinheiten nach rechts.
        Alias-Namen: right | rt
        (Voreingestellte Winkeleinheit is Grad; das kann mittels
        der Funktionen degrees() und radians() ge�ndert werden.
        ---
        Argument: eine Zahl
        
        Aufruf: right(<zahl>)
        --oder: rt(<zahl>)
        
        Beispiel (f�r ein Turtle-Objekt namens turtle):
        
        >>> turtle.heading()
        22.0
        >>> turtle.right(45)
        >>> turtle.heading()
        337.0        
""",

'setpos' :
"""Bewege die Turtle zum Punkt mit absoluten Koordinaten (x,y).
        Alias-Namen: setpos | setposition | goto
	Wenn die Feder unten ist, wird eine Strecke gezeichnet.
	Die Orientierung der Turtle wird nicht ge�ndert.
        ---
        Argumente: zwei Zahlen (dann ist pos die x-coordinate)
	     oder: pos ist ein Paar (2er-Tupel) oder ein Vektor
	           aus zwei Zahlen und y ist None
        
        Aufruf: goto(<zahl>,<zahl>)    # zwei Koordinaten
        --oder: goto((<zahl>,<zahl>))  # ein Paar von  Koordinaten
        --oder: goto(<2-vector>)       # wie z. B. von pos() zur�ckgegeben. 

        Beispiele (f�r ein Turtle-Objekt namens turtle):

        >>> tp = turtle.pos()
        >>> tp
        (0.00, 0.00)
        >>> turtle.setpos(60,30)
        >>> turtle.pos()
        (60.00,30.00)
        >>> turtle.goto((20,80))
        >>> turtle.position()
        (20.00,80.00)
        >>> turtle.setposition(tp)
        >>> turtle.pos()
        (0.00,0.00)
""",

'odometer_on' :
"""Schalte den Wegmesser an.
        ---
        Kein Argument.

        Beispiel (f�r ein Turtle-Objekt namens turtle):

        >>> odometer_on()                
""",

'odometer_off' :
"""Schalte den Wegmesser ab.
        ---
        Kein Argument.

        Beispiel (f�r ein Turtle-Objekt namens turtle):

        >>> odometer_off()        
""",

'get_odometer' :
"""Gib den aktuelle Stand des Wegmessers zur�ck.
        ---
        Kein Argument.

        Beispiel (f�r ein Turtle-Objekt namens turtle):

        >>> odometer_on()
            ...
        >>> weglaenge = get_odometer()
        >>> weglaenge
        360
        >>> while get_odometer() < 400:
                 forward(13.29)
                 left(26.1)
""",

'reset_odometer' :
"""Setze den Wegmesser auf Null.
        ---
        Kein Argument.

        Beispiel (f�r ein Turtle-Objekt namens turtle):

        >>> reset_odometer()        
""",

'ycor' :
"""Gib die y-Koordinate der Turtle zur�ck.
        ---
        Keine Argumente.
        
        Beispiel (f�r ein Turtle-Objekt namens turtle):
        
        >>> reset()
        >>> turtle.left(60)
        >>> turtle.forward(100)
        >>> print turtle.ycor()
        86.6025403784
""",

'sety' :
""" Setze die zweite Koordinate der Turtle auf y.
        Die erste Koordinate bleibt unge�ndert.
        ---
        Argument: eine Zahl
        
        Aufruf: sety(<zahl>)
        
        Beispiel (f�r ein Turtle-Objekt namens turtle):
        
        >>> turtle.position()
        (0.00, 40.00)
        >>> turtle.sety(-10)
        >>> turtle.position()
        (0.00, -10.00)
""",

'towards' :
"""Gib die Orientierung zum Punkt (x,y) zur�ck.
        Das ist der Winkel zwischen
         - der Linie von der aktuellen Turtle-Position zu (x,y)
         - und der Startorientierung der Turtle (siehe: heading()).
        Im Modus 'standard' ist die Startorientierung 'ost'
        und positive Winkel werden im Gegenuhrzeigersinn gemessen.
        Im Modus 'logo' ist die Startorientierung 'nord'
        und positive Winkel werden im Uuhrzeigersinn gemessen.
        ---
        Argumente: zwei Zahlen (d. h. zwei Koordinaten)
	     oder: x ist ein Paar (2er-Tupel) oder Vektor aus zwei
		   Zahlen und y ist None
	     oder: x ist ein Turtle-Objekt (eine Turtle) und y ist None
        
        Aufruf: towards(<zahl>,<zahl>)    # zwei Koordinaten
        --oder: towards((<zahl>,<zahl>))  # ein Paar (2-Tuple) von Koordinaten
        --oder: towards(<2-vector>) # wie es z. B. von pos() zur�ckgegeben wird.	                                
        --oder: towards(mypen)            # wobei mypen eine andere Turtle ist
        
        Beispiel (f�r ein Turtle-Objekt namens turtle):
        
        >>> turtle.pos()
        (10.00, 10.00)
        >>> turtle.towards(0,0)
        225.0        
""",

'degrees' :
""" Setze Einheit f�r die Winkelmessung auf Grad.
        ---
	Optionales Argument: fullcircle. (Anzahl der 'Grade'
	f�r einen vollen Winkel, Standardwert ist 360.0)
        
        Aufruf: degrees()   # fullcircle ist auf 360� voreingestellt.
        
        Beispiel (f�r ein Turtle-Objekt namens turtle):
        
        >>> turtle.left(90)
        >>> turtle.heading()
        90
        >>> turtle.degrees(400.0)  # angle measurement in gon
        >>> turtle.heading()
        100
        >>> turtle.degrees()
        >>> turtle.heading()
        90
""",

'forward' :
"""Bewege die Turtle um distance nach vorne,
        Alias-Namen: forward | fd
        Bewegung nach vorne hei�t in Richtung der Orientierung
        der Turtle.
        ---
        Argument: ein Zahl
        
        Aufruf: forward(<zahl>)
        --oder: fd(<zahl>)
        
        Beispiel (f�r ein Turtle-Objekt namens turtle):
        
        >>> turtle.position()
        (0.00, 0.00)
        >>> turtle.forward(25)
        >>> turtle.position()
        (25.00,0.00)
        >>> turtle.forward(-75)
        >>> turtle.position()
        (-50.00,0.00)        
""",

'circle' :
"""Kreis(bogen) mit radius und Winkel extent.
	Der Kreismittelpunkt ist radius Einheiten links von der
	Turtle; der Winkel extent gibt an, welcher Teil des
	Kreises gezeichnet wird. Wenn extent fehlt, wird (als
	Voreinstellung) ein voller Kreis gezeichnet.
        -
	Wenn extent kein voller Kreis ist, dann ist ein Endpunkt
	des Bogens die aktuelle Turtle-Position. Wenn der Radius
	positiv ist, wird der Bogen im Gegenuhrzeigersinn gezeichnet.
	F�r negative Radien wird der wird der Bogen im Uhrzeigersinn
	gezeichnet. Nachdem Zeichnen des Bogens ist die Orientierung
	der Turtle um extent ge�ndert.
        -
	Da der Kreis durch ein eingeschriebenes regul�res Polygon
	angen�hert wird, bestimmt steps die Anzahl der Schritte, die
	daf�r verwendet wird. Wenn steps nicht angegeben wird, wird
	automatisch ein (hoffentlich passender) Wert ermittelt.
        ---
        Argument: Zahl,
        Optionale Argumente: Zahl, Ganzzahl
        
        Aufruf: circle(<zahl>)  # voller Kreis
        --oder: circle(<zahl>, <zahl>) # Bogen
        --oder: circle(<zahl>, <zahl>, <ganzzahl>)
        
        Beispiel (f�r ein Turtle-Objekt namens turtle):
        
        >>> turtle.circle(50)
        >>> turtle.circle(120, 180)  # semicircle        
""",

'back' :
"""Bewege die turtle um distance r�ckw�rts.
        Alias-Namen: back | backward | bk
        Bewegung r�ckw�rts hei�t, in die Richtung, die der Orientierung
        der Turtle entgegengesetzt ist. Die Ausrichtung der Turtle �ndert
        sich dabei nicht.
        ---
        Argument: eine Zahl
        
        Aufruf: back(<zahl>)
        --oder: bk(<zahl>)
        --oder: backward(<zahl>)
        
        Beispiel (f�r ein Turtle-Objekt namens turtle):
        
        >>> turtle.position()
        (0.00, 0.00)
        >>> turtle.backward(30)
        >>> turtle.position()
        (-30.00, 0.00)       
""",

'xcor' :
"""Gib die x-Koordinate der Turtle zur�ck.
        ---
        Keine Argumente.
        
        Beispiel (f�r ein Turtle-Objekt namens turtle):
        
        >>> reset()
        >>> turtle.left(60)
        >>> turtle.forward(100)
        >>> print turtle.xcor()
        50.0        
""",

'distance' :
"""Gib die Entfernung der Turtle  von (x,y) zur�ck.
        ---
        Argumente: zwei Zahlen (d. h. zwei Koordinaten)
	     oder: x ist ein Paar (2er-Tupel) oder Vektor
	           aus zwei Zahlen und y ist None
	     oder: x ist ein Turtle-Objekt (eine Turtle) und y ist None

        Aufruf: towards(<zahl>,<zahl>)    # zwei Koordinaten
        --oder: towards((<zahl>,<zahl>))  # ein Paar (2-Tuple) von Koordinaten
        --oder: towards(<2-vector>) # wie es z. B. von pos() zur�ckgegeben wird.	                                
        --oder: towards(mypen)            # wobei mypen eine andere Turtle ist
        
        Beispiel (f�r ein Turtle-Objekt namens turtle):
        
        >>> turtle.pos()
        (0.00, 0.00)
        >>> turtle.distance(30,40)
        50.0
        >>> pen = Turtle()
        >>> pen.forward(77)
        >>> turtle.distance(pen)
        77.0        
""",

'radians' :
"""Setze Einheit f�r die Winkelmessung auf Radiant (Bogenma�).
        ---
        Keine Argumente.
        
        Beispiel (f�r ein Turtle-Objekt namens turtle):
        
        >>> turtle.heading()   
        90
        >>> turtle.radians()
        >>> turtle.heading()
        1.5707963267948966
        
""",

'heading' :
"""Gib die aktuelle Orientierung der Turtle zur�ck.
        Die Orientierung ist der Winkel zwischen der Richtung,
        in die die Turtle schaut und der Startausrichtung der
        Turtle.
        Im Modus 'standard' ist die Startausrichting 'ost' und
        positive Winkel werden im Gegenuhrzeigesinn gemessen.
        Im Modus 'logo' ist die Startausrichting 'nord' und
        positive Winkel werden im Uhrzeigesinn gemessen.
        ---
        Keine Argumente.
        
        Beispiel (f�r ein Turtle-Objekt namens turtle):
        >>> turtle.left(67)
        >>> turtle.heading()
        67.0        
""",

'setheading' :
"""Orientiere die Turtle in Richtung to_angle.
        Alias-Namen: sethaeding | seth
        Die Orientierung erfolgt unter Ber�cksichtigung
        des eingestellten Modus. (Siehe mode()).
        Hier sind einige gebr�uchliche Richtungen in Grad:
        -
         standard - Modus:    �� logo-Modus:                  
        -------------------|--------------------
            0 - ost                0 - nord
           90 - nord              90 - ost
          180 - west             180 - s�d
          270 - s�d              270 - west
        ---
        Argument: eine Zahl
        
        Aufruf: setheading(<zahl>)
        
        Beispiel (f�r ein Turtle-Objekt namens turtle):
        >>> turtle.setheading(90)
        >>> turtle.heading()
        90      
""",

'mode' :
"""Setze Turtle-Modus auf 'standard' oder 'logo' zur�ck,
        d. h. f�hre ein reset() aus.
        Modus 'standard' ist kompatibel mit turtle.py.
	Mode 'logo' ist kompatibel mit den meisten Turtle-Grafik
	Implementationen in Logo.
	---
	Optionales Argument: 'standard' oder 'logo'
        
        Aufruf: mode('standard')
        --oder: mode('logo')
        --oder: mode()
         
             Modus     Anf�ngliche Orientierung     positive Winkel
	                     der Turtle
         ------------|-------------------------|---------------------   
          'standard'    nach rechts (Osten)     im Gegenuhrzeigersinn
            'logo'      nach oben (Norden)         im Uhrzeigersinn
        
        Beispiel (f�r ein Turtle-Objekt namens turtle):
        
        >>> turtle.mode('logo') # setzt turtle zur�ck, nach Norden orientiert
        >>> turtle.mode()
        'logo'        
""",

'position' :
"""Gib aktuelle Position der Turtle zur�ck.
        Alias-Namen: position | pos
        R�ckgabewert (x,y) ist ein 2-Vektor - somit auch ein 2-Tupel.
        ---
        Keine Argumente.
        
        Beispiel (f�r ein Turtle-Objekt namens turtle):
        
        >>> turtle.pos()
        (0.00, 240.00)       
""",

'setx' :
"""Setzt die erste Koordinate der Turtle auf x.
        Die zweite Koordinate bleibt unge�ndert.
        ---
        Argument: eine Zahl
        
        Aufruf: setx(<zahl>)
        
        Beispiel (f�r ein Turtle-Objekt namens turtle):
        
        >>> turtle.position()
        (0.00, 240.00)
        >>> turtle.setx(10)
        >>> turtle.position()
        (10.00, 240.00)        
""",

'left' :
""" Drehe die Turtle um angle Winkeleinheiten nach links.
        Alias-Namen: left | lt
        (Voreingestellte Winkeleinheit ist Grad; das kann mittels
        der Funktionen degrees() und radians() ge�ndert werden.
        ---
        Argument: eine Zahl
        
        Aufruf: left(<zahl>)
        --oder: lt(<zahl>)
        
        Beispiel (f�r ein Turtle-Objekt namens turtle):
        >>> turtle.left(45)
        >>> turtle.forward(135)
        >>> turtle.lt(135)
""",

'clearscreen' :
"""Setze alle Turtles auf ihre Anfangswerte zur�ck
        (mit Ausnahme der Turtlegestalten).
        Alias-Namen: clearscreen | resetscreen
        ---
        Kein Argument
        
	--- DAS IST EINE FENSTER-ORIENTIERTE METHODE ---

        Beispiel (f�r ein Turtle-Objekt namens turtle):
        
        >>> turtle.clearscreen()
""",

'end_fill' :
"""F�llt die Figur, die seit dem letzen begin_fill() gezeichnet wurde.
        ---
        Kein Argument.
        
        Example (for a Turtle instance named turtle):
        >>> turtle.begin_fill()
        >>> turtle.forward(100)
        >>> turtle.left(90)
        >>> turtle.forward(100)
        >>> turtle.left(90)
        >>> turtle.forward(100)
        >>> turtle.left(90)
        >>> turtle.forward(100)
        >>> turtle.end_fill()        
""",

'window_width' :
"""Gibt die Breite des Turtlegrafik-Fensters zur�ck.
        ---
        Kein Argument

        Beispiel (f�r ein Turtle-Objekt namens turtle):
        >>> turtle.window_width()
        640        
""",


'getScreen' :
"""Gibt das TurtleScreen-Objekt zur�ck, auf dem die Turtle zeichnet.
        Einige der Methoden von RawTurtle - n�mlich gerade die
        FENSTER-ORIENTIERTEN - k�nnen auch als Methoden von
        urtleScreen-Objekten aufgerufen werden.
        ---
        Kein Argument        
        
	--- DAS IST EINE FENSTER-ORIENTIERTE METHODE ---
	
        Beispiel (f�r ein Turtle-Objekt namens turtle):
        
        >>> ts = turtle.getScreen()
        >>> ts
        <xturtle.TurtleScreen object at 0x0106B770>
        
""",

'shape' :
"""Setze die Turtleform auf name / gib Namen der Turtleform zur�ck.
        Die angegebene Gestalt muss in dem shape-dictionary von
        TurtleScreen existieren. Anf�nglich gibt es f�nf Polygon-Formen:
	'arrow', 'turtle', 'circle'. 'square', 'triangle'
	und dazu 'blank' als leeres Bild.
        ---
        (Optionales) Argument:
           Name einer Turtleform aus dem Turtle-Dictionry.
           Dieses kann mit getshapes() abgefragt werden.
        
        Beispiel (f�r ein Turtle-Objekt namens turtle):
        
        >>> turtle.shape()
        'arrow'
        >>> getshapes()
        ['arrow', 'blank', 'circle', 'square', 'triangle', 'turtle']
        >>> turtle.shape("turtle")
        >>> shape()
        'turtle'        
""",

'fill' :
"""fill(True) ist aufzurufen, bevor die Figur gezeichnet wird,
	die gef�llt werden soll. Wenn die Figur fertig gezeichnet ist,
	wird sie durch einen weiteren Aufruf von fill() gef�llt - und
	zwar:
	    fill(False) f�llt. Die Turtle zeichnet dann normal weiter.
	    fill(True) f�llt und beginnt sofort einen neuen F�llvorgang.
	---           
        Argument: True/False (beziehungsweise 1/0)
        
        Beispiel (f�r ein Turtle-Objekt namens turtle):
        >>> turtle.fill(True)
        >>> turtle.forward(100)
        >>> turtle.left(90)
        >>> turtle.forward(100)
        >>> turtle.left(90)
        >>> turtle.forward(100)
        >>> turtle.left(90)
        >>> turtle.forward(100)
        >>> turtle.fill(False)        
""",

'write' :
"""Schreibe Text an die aktuelle Turtle-Position,
        entsprechend dem Wert von align ("left", "center" oder right")
        und mit der f�r font angeebenen Schriftart.
        Wenn move True ist, wird die Turtle zum rechten unteren Ende
	des Textes bewegt. Voreinstellung f�r move ist False.
        ---
        Argumente:
        
        Beispiel (f�r ein Turtle-Objekt namens turtle):
        
        >>> turtle.write('The race is on!')
        >>> turtle.write('Home = (0, 0)', True, align="center")        
""",

'delay' :
"""Setze den delay-Wert f�r das Grafik-Update in Millisekunden,
        das ist die Zeit zwischen zwei aufeinanderfolgenden Grafik-Updates.
	delay() ist eine FENSTER_ORIENTIERTE Methode/Funktion, d. h.
	sie betrifft alle Turtles auf dem Bildschirm.
	Ohne Argument aufgerufen, gibt delay() den aktuellen delay-Wert
	zur�ck.
	
        Argument: Zahl >= 0 oder kein Argument.
        
	--- DAS IST EINE FENSTER-ORIENTIERTE METHODE ---
	
        Beispiel (f�r ein Turtle-Objekt namens turtle):
        
        >>> turtle.delay(15)
        >>> turtle.delay()
        15
        
""",

'bgcolor' :
"""Setze/gib zur�ck: die Hintergrundfarbe des Turtlegrafik-Fensters.
        ---        
        (Optionale(s)) Argument(e): ein Farb-String oder drei Zahlen im 
	Bereich 0 .. colormode oder ein Tupel aus drei solchen Zahlen. 
        
	--- DAS IST EINE FENSTER-ORIENTIERTE METHODE ---
	
        Beispiele (f�r ein Turtle-Objekt namens turtle):
        
        >>> turtle.bgcolor("orange")
        >>> turtle.bgcolor()
        'orange'
        >>> turtle.bgcolor(0.5,0,0.5)
        >>> turtle.bgcolor()
        '#800080'        
""",

'polystart' :
"""Beginne die Aufzeichnung der Eckpunkte eines Polygons.
	Die aktuelle Turtle-Position ist der erste Punkt des Polygons.
        
        Beispiel (f�r ein Turtle-Objekt namens turtle):
        >>> turtle.polystart()
        
""",

'onkey' :
"""Bindet fun an das Tastendruck-Ereignis f�r die Taste key.
        (Genauer: an das Ereignis des Loslassens der Taste. Dies hat den
        Sinn, dass fun nicht auf Gedr�ckthalten der Taste reagieren soll.)
	Damit dieses Ereignis f�r das Grafik-Fensgter registriert wird,
	muss dieses den Fokus haben. (Siehe Methode listen().)
	---
	Argumente:
	   fun: Funktion ohne Argumente
	   key: Tastenbezeichnung, wie etwa "a", oder auch "Up", "Down", ...
        
        Beispiel (f�r ein Turtle-Objekt namens turtle):
        
        >>> def f():
                turtle.fd(50)
                turtle.lt(60)

                
        >>> turtle.onkey(f, "Up")
        >>> turtle.listen()
        
        ### In der Folge kann die Turtle bewegt werden, indem wiederholt
        ### die Aufw�rts-Pfeil-Taste gedr�ckt wird; sie zeichnet auf diese 
        ### Weise ein regelm��iges Sechseck.        
""",

'bgpic' :
"""Setze Hintergrundbild aus der gif-Datei picname / gib picname zur�ck.
	Wenn als picname "nopic" oder  der Leerstring "" verwendet wird, 
	wird das Hintergrundbild entfernt.
        ---
        (ptionales) Argument: Ein String, der der Name einer
             gif-Bilddatei ist oder "nopic" beziehungsweise "".
        
	--- DAS IST EINE FENSTER-ORIENTIERTE METHODE ---

        Beispiele (f�r ein Turtle-Objekt namens turtle):

        >>> turtle.bgpic()
        'nopic'
        >>> turtle.bgpic("landscape.gif")
        >>> turtle.bgpic()
        'landscape.gif'
        >>> turtle.bgpic("nopic")        
""",

'getpoly' :
"""Gib das zuletzt aufgezeichnete Polygon zur�ck.
        
        Beispiel (f�r ein Turtle-Objekt namens turtle):
        >>> p = turtle.getpoly()
        >>> turtle.addshape("myFavouriteShape", p)
        
""",

'getPen' :
"""gibt das Turtle-Objekt selbst zur�ck.
	Einzige sinnvolle Verwendung: als Funktion, um einen Verweis
	auf die "anonyme Turtle" zu erhalten:
        
        Beispiel:
        >>> turtle = getPen()
        >>> turtle.fd(50)
        >>> turtle
        <xturtle.Turtle object at 0x0187D810>
        >>> turtles()
        [<xturtle.Turtle object at 0x0187D810>]
        
""",

'addshape' :
""" F�gt eine Turtle-Form zum shape-dictionary der TurtleScreen hinzu.
        ---
        Argumente:
        (1) name ist der Dateiname einer gif-Datei und shape its None.
            Installiere die entspr#chend Bild-Form
        (2) name ist eine beliebige Zeichenkette und shape ist ein Tupel
	    von Koordinaten-Paaren. Installiert die entsprechende
	    Polygon-Form.
        (3) name ist eine beliebige Zeichenkette und shape ist ein
            zusammengesetztes Shape-Objekt. Installiert die entsprechend
	    zusammengesetzte Turtle-Form.
       
	--- DAS IST EINE FENSTER-ORIENTIERTE METHODE ---
	Um eine Turtle-Form zu verwenden, muss die Methode
	turtle.shape(shapename) verwendet werden.
                
        Beispiel (f�r ein Turtle-Objekt namens turtle):

        >>> turtle.addshape("triangle", ((5,-3),(0,5),(-5,-3)))       
""",

'polyend' :
"""Beende die Aufzeichnung der Eckpunkte eines Polygons.
	Die aktuelle Turtle-Position ist der letze Punkt des Polygons.
	Dieser wird mit dem ersten Punkt verbunden werden.
        
        Beispiel (f�r ein Turtle-Objekt namens turtle):
        >>> turtle.polyend()
        
""",

'listen' :
"""Setze den Fokus auf die Zeichenfl�che, um Tasten-Ereignisse zu registrieren.
        ---
        Keine Argumente.
        (Dummy Argumente sind angegeben, damit listen as Argument der
	onclick-Methode verwendet werden kann. Dadurch bekommt die 
	Zeichenfl�che den Fokus, wenn man sie anklickt.)
        
	--- DAS IST EINE FENSTER-ORIENTIERTE METHODE ---
	
        Beispiel (f�r ein Turtle-Objekt namens turtle):
        
        >>> turtle.listen()                
""",

'screen_width' :
"""Gibt die Breite der Turtle-Zeichenfl�che zur�ck.

        Beispiele (f�r ein Turtle-Objekt namens turtle):
        >>> turtle.screen_width()
        800
        
""",

'window_height' :
"""Gibt die H�he des Turtlegrafik-Fensters zur�ck.

        Beispiele (f�r ein Turtle-Objekt namens turtle):
        >>> turtle.window_height()
        480
        
""",

'colormode' :
"""Setze colormode auf 1.0 oder 255. / Gib colormode zur�ck.
        ---
        Argument: None oder einer der Werte 1.0 oder 255
        
        Aufruf:  colormode(255) # zum Beispiel
        --oder:  colormode()
        
	--- DAS IST EINE  FENSTE-ORIENTIERTE METHODE ---        
        Beispiel (f�r ein Turtle-Objekt namens turtle):
        >>> turtle.colormode(255)
        >>> turtle.pencolor(240,160,80)
        
""",

'clone' :
"""Erzeuge einen Klon der Turtle und gib dieses Objekt zur�ck -
        mit denselben Werten f�r Position, Orientierung
        und Stift-Eigenschaften.
        
        Beispiel (f�r ein Turtle-Objekt namens turtle):
        turtle = Turtle()
        tortoise = turtle.clone()
        
""",

'update' :
"""F�hrt ein Update der Grafik im Turtlegrafik-Fenster aus.
	Speziell n�tzlich um Grafik-Updates zu kontrollieren,
	wenn tracer(False) gesetzt ist.
        
	--- DAS IST EINE FENSTER-ORIENTIERTE METHODE ---

        Beispiel (f�r ein Turtle-Objekt namens turtle):
        >>> tracer(0)
        >>> for i in range(36):
                for j in range(5):
                        turtle.fd(100)
                        turtle.lt(72)
                turtle.update() # draws a pentagon at once
                turtle.lt(10)        
        
""",

'screensize' :
"""Setze die Gr��e der Zeichenfl�che des Turtlegrafik-Fensters,
	ohne die Gr��e des Turtlegrafik-Fensters selbst zu �ndern.
	Durch Verwendung der Schiebebalken kann die Zeichenfl�che im Fenster
	bewegt werden. 
	Vergr��ern der Zeichenfl�che kann Teile einer Zeichnung sichtbar
	machen, die vorher au�erhalb der Zeichenfl�che lagen.
        
        Argumente: zwei positive Zahlen.
        
        Beispiel (f�r ein Turtle-Objekt namens turtle):
        >>> turtle.screensize(2000,1500)
            ### zum Beispiel um nach einer versehentlich entfleuchten Turtle
	    ### zu suchen.
""",

'onclick' :
"""Binde den Aufruf von fun and das Maus-Klick-Ereignis des
	Grafikfensters.
        
        Argumente: fun muss eine Funktion mit zwei Argumenten sein,
	denen beim Aufruf die Koordinaten das Klick-Punktes auf dem
	Grafik-Fenster �bergeben werden.
        btn ist die Nummer der Maustaste. Standardwert ist 1 und entspricht
	der linken Maustaste. 2 entspricht der mittleren, 3 der rechten
	Maustaste.
        
	--- DAS IST EINE FENSTER-ORIENTIERTE METHODE ---

        Beispiel (f�r ein Turtle-Objekt namens turtle):        

        >>> turtle.onclick(turtle.goto)

        ### In der Folge bewirkt Klicken auf das Grafikfenster, dass
        ### die Turtle sich zu dem angeklickten Punkt hinbewegt.
        >>> turtle.onclick(None)
        ### Ereignisbindung wird entfernt.        
""",


'reset' :
"""L�scht die Zeichnungen der Turtle und setzt sie auf Anfangswerte.
        Genauer: setzt die Turtle in den Mittelpunkt des Fensters und alle
	Attribute auf ihre Anfangswerte (mit Ausnahme der Turtle-Gestalt).
        ---
        Kein Argument
        
        Beispiel (f�r ein Turtle-Objekt namens turtle):
        
        >>> turtle.position()
        (0.00,-22.00)
        >>> turtle.seth(100)
        >>> turtle.position()
        (0.00,-22.00)
        >>> turtle.heading()
        100.0
        >>> turtle.reset()
        >>> turtle.position()
        (0.00,0.00)
        >>> turtle.heading()
        0.0               
""",

'tracer' :
"""tracer(True/False) dreht die Turtle-Animation an/ab.
        tracer akzeptiert auch positive ganze Zahlen als erstes Argument.
        tracer(n) hat den Effekt, dass nur jededs n.te update wirklich
        ausgef�hrt wird. Kann dazu ben�tzt werden, das Zeichnen komplexer
        Grafiken zu beschleunigen.
        Das zweite Argument setzt den delay-Wert. (siehe RawTurtle.delay())
	Ohne Argument wird der aktuelle Wert von flag zur�ckgegeben.
	---
	(Optionale) Argumente:
	    flag: True/False
	    delay: positive ganze Zahl
        
        Beispiel (f�r ein Turtle-Objekt namens turtle):
        
        >>> turtle.tracer(8, 25)
        >>> l=2
        >>> for i in range(200):
                turtle.fd(l)
                turtle.rt(90)
                l+=2
        
""",

'turtles' :
"""Gib Liste der auf der Zeichenfl�che vorhandenen Turtles zur�ck.
        
        Beispiel (f�r ein Turtle-Objekt namens turtle):
        >>> turtle.turtles()
        [<xturtle.Turtle object at 0x00E11FB0>]
        
""",

'clear' :
"""L�scht die Zeichnungen der Turtle vom Grafikfenster.
        Die Turtle wird nicht bewegt, Zeichnungen anderer Turtles
	werden nicht beeinflusst.
        
        Beispiel (f�r ein Turtle-Objekt namens turtle):
        >>> turtle.clear()
""",

'begin_fill' :
"""Wird aufgerufen, wenn mit dem Zeichnen einer Figur begonnen wird,
        die schlie�lich gef�llt werden soll.
        ---
        Kein Argument.
        
        Beispiel (f�r ein Turtle-Objekt namens turtle):
        
        >>> turtle.begin_fill()
        >>> turtle.forward(100)
        >>> turtle.left(90)
        >>> turtle.forward(100)
        >>> turtle.left(90)
        >>> turtle.forward(100)
        >>> turtle.left(90)
        >>> turtle.forward(100)
        >>> turtle.end_fill()        
""",

'getshapes' :
"""Gib Liste der Name aller zur Verf�gung stehenden Turtle-Formen zur�ck.
        ---
        Kein Argument.
        
	--- DAS IST EINE FENSTER-ORIENTIERTE METHODE ---
	
        Beispiel (f�r ein Turtle-Objekt namens turtle):
        >>> turtle.getshapes()
        ['arrow', 'blank', 'circle', 'turtle']        
""",

'getCanvas' :
"""Gibt einen Verweis auf das Canvas-Objekt (Zeichenfl�che) zur�ck,
        auf dem die Turtle zeichnet. (F�rt jene fortgeschrittenen
	Benutzer, die mit dem Canvas direkt etwas anfangen wollen.)
	---
	Kein Argument.
        
	--- DAS IST EINE FENSTER-ORIENTIERTE METHODE ---
	
        Beispiel (f�r ein Turtle-Objekt namens turtle):
        
        >>> cv = turtle.getCanvas()
        >>> cv
        <xturtle.ScrolledCanvas instance at 0x010742D8>        
""",

'ontimer' :
"""Installiere einen Timer, der nach t Millisekunden fun aufruft.
        ---
        Argumente:
        fun ist eine Funktion ohne Argumente.
        t is eine Zahl >= 0
        
	--- DAS IST EINE FENSTER-ORIENTIERTE METHODE ---
	
        Beispiel (f�r ein Turtle-Objekt namens turtle):
        
        >>> running = True
        >>> def f():
                if running:
                        turtle.fd(50)
                        turtle.lt(60)
                        turtle.ontimer(f, 250)

        >>> f()   ### Turtle lauft herum.
        >>> running = False                
""",

'dot' :
"""Zeichne eine Punkt mit dem Durchmesser size, zweites Argument: Farbe
	Wenn die Farbe nicht angegeben wird, wird  die Turtle-Farbe verwendet.
	Wenn auch die size nicht angegeben wird, wird pensize()+4 verwendet.
        ---
        Argument: size ist eine Zahl >= 1 (wenn angegeben)
                  color is ein Farbstring oder ein numerisches Farbtupel
        
        Beispiel (f�r ein Turtle-Objekt namens turtle):
        
        >>> turtle.dot()
        >>> turtle.fd(50); turtle.dot(20, "blue"); turtle.fd(50)     
""",

'screen_height' :
"""Gib die H�he der Zeichenfl�che f�r die Turtle zur�ck.

        Beispiel (f�r ein Turtle-Objekt namens turtle):
        
        >>> turtle.screen_height()
        600
        
""",

'stamp' :
"""Erzeuge 'Stempelabdruck' der Turtle-Gestalt auf der Zeichenfl�che.
        Gibt eine Kennung f�r den Stempelabdruck zur�ck - zum allf�lligen
        L�schen.
        ---
        Kein Argument.
        
        Beispiel (f�r ein Turtle-Objekt namens turtle):
        
        >>> turtle.stamp()
        34
        >>> probe = turtle.stamp()
        >>> clearstamp(probe)
        
""",

'clearstamp' :
"""L�sche den Stempelabdruck mit der Kennung stampid.
        ---
        Argument: eine stampid, die vorher von einem stamp()-Aufruf
            zur�ck gegeben wurd.

        Beispiel (f�r ein Turtle-Objekt namens turtle):
        
        >>> probe = turtle.stamp()
        >>> clearstamp(probe)            
""",

'clearstamps' :
"""L�sche alle oder n der vorhandenen Stempelabdrucke.
       Wenn n>0 ist, werden die ersten n Stempelabdrucke gel�scht,
       wenn n<0 ist, die n zuletzt erzeugten.
       ---
       Argument:
           n : ganze Zahl. Anzahl der Stempelabdrucke, die gel�scht
               werden.

        Beispiel (f�r ein Turtle-Objekt namens turtle):
        
        >>> for i in range(10):
                turtle.stamp()
                turtle.fd(40)
        >>> clearstamps(2)
        >>> clearstamps(-3)
        >>> clearstamps()
           
""",

'setup' :
"""Setze Geometrie des Turtlegrafik-Fensters

        Argumente:
        width: als ganze Zahl die Fensterbreite in Pixel, als Kommazahl
               der Bruchteil der Bildschirmbreite, den das Fenster einnimmt.
               Standarwert ist 50% der Bildschirmbreite.
        height: als ganze Zahl die Fensterh�he in Pixel, als Kommazahl
               der Bruchteil der Bildschirmh�he, den das Fenster einnimmt.
               Standarwert ist 75% der Bildschirmh�he.
        startx: wenn positiv, Entfernung des Fensters vom linken Bildschirmrand
               in Pixel; wenn negativ, Entfernung vom rechten Bildschirmrand.
               Standarwert, startx=None, zentriert das Fenster horizontal.
        starty: wenn positiv, Entfernung des Fensters vomoberen Bildschirmrand
               in Pixel; wenn negativ, Entfernung vom unteren Bildschirmrand.
               Standarwert, starty=None, zentriert das Fenster vertikal.      

        Beispiele (wenn als Funktion aufgerufen):
        >>> setup (width=200, height=200, startx=0, starty=0)

        setzt Fentergr��e auf 200x200 pixels, in der oberen linken
        Bildschirmecke.

        >>> setup(width=.75, height=0.5, startx=None, starty=None)

        Setzt die Fenstergr��e auf 75% der Bildschirmbreite und 50%
        der Bildschirmh�he und zentriert das Fenster auf dem Bildschirm.        
""",

'bye' :
"""Schlie�e das Turtlegrafik-Fenster.
        
        Beispiel (f�r ein Turtle-Objekt namens turtle):
        >>> turtle.bye()        
""",

'winsize' :
"""Setze die Geometrie des Turtlegrafik-Fensters
        ---
        Argumente: w and h sind die neue Breite und H�he des Fensters.
        lr ('left/right') und tb ('top/bottom') sind Koordinaten der
	Kanten des Turtlegrafik-Fensters auf dem Bildschirm.
	+ wird f�r die Angabe der oberen/linken Kante ben�tzt.
        - wird f�r die Angabe der unteren/rechten Kante ben�tzt. 	
        
        Beispiel (f�r ein Turtle-Objekt namens turtle):
        >>> turtle.winsize(800, 600, -10, 10)
            ### Setzt Fenstergr��e auf 800x600 und die Lage des Fensters so,
            ### die rechte Fensterkante 10 Pixel vom rechten Bildschirmrand,
            ### und die obere Fensterkante 10 Pixel vom oberen Bildschirmrand
	    ### entfernt sind.
"""

}
