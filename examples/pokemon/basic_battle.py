import random

class Pokemon: pass

pokemon = Pokemon()
opponent = Pokemon()

pokemon.name = "Picachu"
pokemon.level = 1
pokemon.hp = 12
pokemon.attack = 6
pokemon.defense = 5
pokemon.special_attack = 6
pokemon.special_defense = 6
pokemon.speed = 7
pokemon.moves = [
    'growl',
    'thundershock'
]

opponent.name = "Rattata"
opponent.level = 1
opponent.hp = 11
opponent.attack = 6
opponent.defense = 5
opponent.special_attack = 6
opponent.special_defense = 6
opponent.speed = 6
opponent.moves = [
    'tailwhip',
    'tackle'
]

# first see who goes first
if pokemon.speed > opponent.speed:
    goes_first = pokemon
elif opponent.speed > pokemon.speed:
    goes_first = opponent
else:
    goes_first = random.choice([pokemon,opponent])

# then who goes last
if goes_first == pokemon:
    goes_last = opponent
else:
    goes_last = pokemon

# Battle!!
print("Your moves: {}".format(pokemon.moves))
pokemon.move = input("Which move would you like to use? ")
opponent.move = random.choice(opponent.moves)

print("{} uses {}".format(goes_first.name,goes_first.move))
print("{} uses {}".format(goes_last.name,goes_last.move))





