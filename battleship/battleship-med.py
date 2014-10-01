
class Ship():
    size = None
    char = None

    def __init__(self):
        self.row = 0
        self.col = 0
        self.direction = None

class Carrier(Ship):
    size = 5
    char = 'C'

class Battleship(Ship):
    size = 4
    char ='B'

class Destroyer(Ship):
    size = 3
    char = 'D'

class Submarine(Ship):
    size = 3
    char = 'S'

class PatrolBoat(Ship):
    size = 2
    char = 'P'


my_carrier = Carrier()
my_battleship = Battleship()
my_destroyer = Destroyer()
my_submarine = Submarine()
my_patrolboat = PatrolBoat()

x_carrier = Carrier()
x_battleship = Battleship()
x_destroyer = Destroyer()
x_submarine = Submarine()
x_patrolboat = PatrolBoat()

print('Prepare for battle!')

w = '~'
hit = '*'

grid = [
    [' ',0,1,2,3,4,5,6,7,8,9],
    ['A',w,w,w,w,w,w,w,w,w,w],
    ['B',w,w,w,w,w,w,w,w,w,w],
    ['C',w,w,w,w,w,w,w,w,w,w],
    ['D',w,w,w,w,w,w,w,w,w,w],
    ['E',w,w,w,w,w,w,w,w,w,w],
    ['F',w,w,w,w,w,w,w,w,w,w],
    ['G',w,w,w,w,w,w,w,w,w,w],
    ['H',w,w,w,w,w,w,w,w,w,w],
    ['I',w,w,w,w,w,w,w,w,w,w],
    ['J',w,w,w,w,w,w,w,w,w,w]
]

def show_grid():
    for row in grid:
        for col in row:
            print(col, end=' ')
        print()

def shoot():
    (row,col) = ask_coord()
    grid[row][col] = hit

def ask_coord():
    row_num = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10}
    row = input('Row?').strip().lower()
    col = input('Col?').strip()
    row = row_num[row]
    col = int(col) + 1
    return (row,col)

def play():
    while True:
        show_grid()
        shoot()
        
show_grid()

for ship in [my_carrier,my_battleship,my_destroyer,my_submarine,my_patrolboat]:
    print("{} start coord:".format(ship.__class__.__name__))
    (ship.row,ship.col) = ask_coord()
    print("Horizontal or vertical [h|v]?")
    ship.direction = input('> ').lower().strip()
    if ship.direction == 'h':
        for col in range(ship.size):
            grid[ship.row][ship.col + col] = ship.char
    show_grid()
