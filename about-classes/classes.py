class Pig():

    def __init__(self):
        self.upside_down = False
        self.color = 'pink'

    def oink(self):
        print(self.color.title() + " Oink")

    def flip(self):
        self.upside_down = True

##################################################

grumm = Pig()
grumm.color = 'blue'
print(grumm.color)
grumm.oink()

george = Pig()
george.color = 'red'
print(george.color)
george.oink()
george.flip()
print(george.upside_down)
