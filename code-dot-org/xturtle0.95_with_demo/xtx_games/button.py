# Button
# 8. 3. 2007
# Gregor Lingl

from xturtle import Turtle

class Button(Turtle):
    def __init__(self, picfile, action):
        Turtle.__init__(self)
        self.addshape(picfile)
        self.shape(picfile)
        def _action(x,y):
            action()
        self.onclick(_action)
        self.pu()
        self.speed(0)
