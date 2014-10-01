 
class Ship():
    size = None

class Carrier(Ship):
   size = 5

   def __init__(self):
       self.location = None

player_carrier = Carrier()
enemy_carrier = Carrier()

enemy_carrier.location = 'a5'

print(enemy_carrier.location)
print(player_carrier.location)
