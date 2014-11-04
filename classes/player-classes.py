class Player:
    health = 10
    defense = 10
    strength = 10
    
    def take_damage(self,damage=1):
        if self.defense < 3:
            damage *= 2  
        elif self.defense > 17:
            damage /= 2
        self.health -= damage

player1 = Player()
player2 = Player()

player1.defense = 2

print(player1.health)
player1.take_damage()
print(player1.health)
player1.take_damage(5)
print(player1.health)

