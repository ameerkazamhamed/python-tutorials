import random

class Spheal():

    def __init__(self):
        self.strength = random.randint(15,20)

    def attack(self, enemy):
        pass

#------------------------------------------

you = Spheal()
print(you.strength)
