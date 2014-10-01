import random

class Player():
    
    def __init__(self):
        self.strength = self.roll_ability()
        self.dexterity = self.roll_ability()
        self.constitution = self.roll_ability()
        self.intelligence = self.roll_ability()
        self.wisdom = self.roll_ability()
        self.charisma = self.roll_ability()

    def roll_ability(cls):
        return random.randint(3,18)
    
    def show_abilities(self):
        print('Strength:',self.strength)
        print('Dexterity:',self.dexterity)
        print('Constitution:',self.constitution)
        print('Intelligence:',self.intelligence)
        print('Wisdom:',self.wisdom)
        print('Charisma:',self.charisma)

    def show(self):
        self.show_abilities()

while True:
    me = Player()
    me.show()
    input()
