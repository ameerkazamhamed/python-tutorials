#!/usr/bin/python
"""       xturtle-example-suite:

            xtx_moorhuhn.py

An event driven game with gif-images as
background and pen-shapes

Try to click at the moorhuhns ;-)
(Correct plural of moorhuhn is 'moorhuehner')

What's the English name for this game?
After 10 shots the game ends and displays
your score.

Note: dead moorhuhns' orbits are parabolas.

   Press STOP to exit the program!
   ===============================   
"""
from xturtle import Turtle, mainloop
import random, time, winsound


SHOTS = 10
VELOCITY = 1
WINWIDTH, WINHEIGHT = 800, 600
HIT = "getroffen.wav"
MISSED = "daneben.wav"
GOOD = "gameover.wav"
MODERATE = "applaus.wav"

class MHManager(Turtle):
    """Special Turtle, performs the task to manage the Moorhuhn-GUI.
    """
    def __init__(self, w, h):
        Turtle.__init__(self, width=w, height=h)
        self.hideturtle()
        self.speed(0)
        self.penup()
        self.goto(-WINWIDTH//2 + 50, -WINHEIGHT//2 + 20)
        self.pencolor("yellow")
    def message(self, txt):
        """Outputs text to graphics window.
        """
        self.clear()
        self.write(txt, font=("Courier", 18, "bold"))

class Huhn(Turtle):
    def __init__(self, bilddatei, game):
        Turtle.__init__(self, bilddatei)
        self.game = game
        self.penup()
        self.speed(0)
        self.onclick(self.hit)
        self.start()
    def start(self):
        self.hideturtle()
        self.setpos(-WINWIDTH//2-20, random.randint(-WINHEIGHT//3,WINHEIGHT//3))
        self.vx = random.randint(6,11) * VELOCITY
        self.vy = random.randint(-3,3) * VELOCITY
        self.getroffen = False
        self.tot = False
        self.showturtle()
        self.ausdemspiel = False
    def hit(self, x, y):
        if self.tot or self.game.shots==SHOTS: # game over
            return
        self.getroffen = True
        self.tot = True
        self.game.score += 1

    def step(self):
        if self.ausdemspiel:
            time.sleep(0.01)  # 
            return
        if self.tot:
            self.vy = self.vy - 0.25 * VELOCITY
        x, y = self.position()
        x = x + self.vx
        y = y + self.vy
        self.goto(x,y)
        if x > WINWIDTH//2 + 20 or abs(y) > WINHEIGHT//2 + 10: 
            if self.game.shots != SHOTS:
                self.start()
            else:
                self.ausdemspiel = True

class MoorhuhnGame(object):
    """Combines elements of Moorhuhn game.
    """
    def __init__(self):
        self.mhm = mhm= MHManager(800, 600) # erzeugt
                                     # Grafik-Fenster
        mhm.bgpic("landschaft800x600.gif")
        mhm.message("Press spacebar to start game!")

        mhm.addshape("huhn01.gif")
        mhm.addshape("huhn02.gif")
        self.huehner = [Huhn("huhn01.gif", self), Huhn("huhn02.gif", self)]
        
        self.gameover = True   # now a new game can start
        mhm.onscreenclick(self.shot, 1)
        mhm.onkey(self.game, "space")
        mhm.listen()
        mhm.getcanvas().config(cursor="X_cursor") # get into Tkinter ;-)
    def game(self):
        if not self.gameover:
            return   # game still running
        self.mhm.message("GAME RUNNING")
        self.shots = 0
        self.score = 0
        self.gameover = False
        for huhn in self.huehner:
            huhn.start()
        while not self.gameover:
            for huhn in self.huehner:
                huhn.step()
            gameover = self.shots == SHOTS
            for huhn in self.huehner:
                gameover = (gameover and huhn.ausdemspiel)
            self.gameover = gameover
            
        trefferrate = 1.0*self.score/self.shots
        self.mhm.message( ("Score: %1.2f" % trefferrate) +
                                        " - press spacebar!")
        if trefferrate > 0.55:
            self.sound(GOOD)
        else:
            self.sound(MODERATE)
    def shot(self, x, y):
        if self.shots == SHOTS:
            return # no game running, so no shot
        self.shots = self.shots + 1
        klangdatei = MISSED
        for huhn in self.huehner:
            if huhn.getroffen: 
                klangdatei = HIT
                huhn.getroffen = False
                break
        if self.shots == SHOTS:
            self.mhm.message("GAME OVER!")
        else:        
            self.mhm.message("hits/shots: %d/%d" %(self.score, self.shots))
        self.sound(klangdatei)
    def sound(self, soundfile):
        winsound.PlaySound(soundfile, winsound.SND_ASYNC) 

def main():  # for xturtleDemo
    MoorhuhnGame()
    return "EVENTLOOP"
    
if __name__ == "__main__":
    msg = main()
    print msg
    mainloop()
