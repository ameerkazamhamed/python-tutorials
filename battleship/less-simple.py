class Ship():
    size = None
    
    def __init__(self):
        self.location = ()

class Carrier(Ship):
    size = 5

class Battleship(Ship):
    size = 4

class Submarine(Ship):
    size = 3

class Destroyer(Ship):
    size = 3

class PatrolBoat(Ship):
    size = 2

#-------------------------------

print('Welcome to Battleship!')
#TODO add really cool ASCII Art
#TODO ask computer difficulty
#TODO print grid

grid = [[' ~' * 10] * 10]

for row in grid:
    for col in row:
        print(col)

carrier = Carrier()

start_row = input('Enter start row for Carrier:').strip().lower()
start_col = input('Enter start col for Carrier:').strip().lower()
direction = input('Enter direction for Carrier [n,s,e,w]:').strip().lower()

#TODO sanity check input values, loop asking again until valid
#TODO include checking occupied positions as invalid

#TODO make the computer make guesses and talk smack
6



