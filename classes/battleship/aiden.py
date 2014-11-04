import time
import random

def typeit(it,low=0.03,high=0.00000000000):
    for letter in it:
        print(letter,end='')
        time.sleep(random.uniform(low,high))
    print()
    
typeit("Prepare for warrrrrr",0.1,0.1)
typeit("Dont break please c:")

class  Ship():
    size = None

class Carrier(Ship):
    size = 5

class Battleship(Ship):
    size = 4

class Submarine(Ship):
    size = 3

class Destroyer(Ship):
    size = 2
    
class PatrolBoat(Ship):
    size = 2

class Grid():
    pass

class Player():
    def __init__(self):
        self.grid = Grid()
        self.carrier = Carrier()
        self.battleship = Battleship()
        self.destroyer = Destroyer()
        self.submarine = Submarine()
        self.patrolboat = PatrolBoat()

class Computer(Player):
    pass

class Controller():

    def __init__(self):
        self.player1 = Player()
        self.player2 = Computer()

    def place_ships(self):
        self.ask_where_to_place_ships(player1)
        self.place_random_ships(player2)

    @staticmethod
    def place_random_ships(player):
        pass

    @staticmethod
    def ask_where_to_place_ships(player):
        pass

#-----------------------------------------------

hit = '*'

grid = [
    [' ','1','2','3','4','5','6','7','8','9','10',],
    ['A','~','~','~','~','~','~','~','~','~','~',],
    ['B','~','~','~','~','~','~','~','~','~','~',],
    ['C','~','~','~','~','~','~','~','~','~','~',],
    ['D','~','~','~','~','~','~','~','~','~','~',],
    ['E','~','~','~','~','~','~','~','~','~','~',],
    ['F','~','~','~','~','~','~','~','~','~','~',],
    ['G','~','~','~','~','~','~','~','~','~','~',],
    ['H','~','~','~','~','~','~','~','~','~','~',],
    ['I','~','~','~','~','~','~','~','~','~','~',],
    ['J','~','~','~','~','~','~','~','~','~','~',],
]




def show(grid):
    for row in grid:
        for col in row:
            print(col, end=' ')
        print()

row_numbers = { 'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10}

while True:
    shoot_row = input("Target Row: ").lower().strip()
    if shoot_row in 'abcdefgh':
        shoot_row = row_letters[shoot_row]
    else:
        shoot_row = int(shoot_row)
    
    shoot_col = int(input("Target Column: ").lower().strip())
    grid[shoot_row][shoot_col] = '*'
    show(grid)
