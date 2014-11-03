#!/usr/bin/env python3

import random

class Ship(): # abstract-ish
    size = None
    char = None
    placed = None

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

class Player():
    def __init__(self):
        self.name = 'Player'
        self.carrier = Carrier()
        self.battleship = Battleship()
        self.destroyer = Destroyer()
        self.submarine = Submarine()
        self.patrolboat = PatrolBoat()
        self.ships = [
            self.carrier,
            self.battleship,
            self.destroyer,
            self.submarine,
            self.patrolboat
        ]
        self.ships_grid = Grid()
        self.shots_grid = Grid()

class Computer(Player):
    pass

class BadDirection(Exception): pass

class Grid():
    row_num = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10}
    WATER = '~'
    EMPTY = WATER

    def __init__(self):
        w = Grid.WATER
        self.squares = [
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
        self.row_count = 10
        self.col_count = 10

    def is_empty_at(self,col=1,row=1):
        return self.squares[row][col] == self.EMPTY

    def is_row_empty_at(self,row=1,col=1,size=1,reverse=False):
        if reverse:
            cols = range(col+size,col,-1)
        else:
            cols = range(col,col+size,1)
        for col in cols:
            if not self.is_empty_at(col,row):
                return False
        return True

    def find_empty(self,size):
        while True:
            x = random.randint(1,self.size_x)
            y = random.randint(1,self.size_y)


class Controller():
    def __init__(self):
        self.player = Player()
        self.computer = Player()

    def greet(self):
        print('Well hello there. What is your name?')
        self.player.name = input('> ').strip().title()
        print('Prepare for battle {}!'.format(self.player.name))

    def ask_coord(self):
        row = input('Row?').strip().lower()
        col = input('Col?').strip()
        row = Grid.row_num[row]
        col = int(col) + 1
        return (row,col)

    def shoot(self):
        (row,col) = self.ask_coord()
        # TODO have to change what is printed on grid
        # depending on if it is a hit or not
        self.computer.ships_grid.squares[row][col] = '*'
        self.player.shots_grid.squares[row][col] = '*'

    def play(self):
        #TODO trap all exceptions to keep from bailing to early
        self.greet()
        self._place_ships_random(self.player)
        while True:
            self.print_player_grids(self.player)
            self.shoot()

    def _place_ships_random(self,player):
        print('Placing ships randomly for {}.'.format(player.name))
        for ship in player.ships:
            size = ship.size
            char = ship.char
            while not ship.placed:
                max_row = 9
                max_col = 9
                direction =  random.choice(['x','-x','y','-y'])


    def print_player_grids(self,player):

        # define box characters
        ul =  '\u250F' 
        ur =  '\u2513'
        ll =  '\u2517' 
        lr =  '\u251B'
        h =   '\u2501'
        v =   '\u2503'
        uhv = '\u2533'
        lhv = '\u253B'

        print(ul + h * 24 + uhv + h * 24 + ur)
        print(v + '       -~-SHIPS-~-     ' ,
              v + '       -~-SHOTS-~-      ' + v)

        for row in range(10):
            print(v + ' ',end='')
            for col in player.ships_grid.squares[row]:
                print(col, end=' ')
            print(' ' + v, end=' ')
            for col in player.shots_grid.squares[row]:
                print(col, end=' ')
            print(' ' + v,end='')
            print()

        print(ll + h * 24 + lhv + h * 24 + lr)


if __name__ == '__main__':
    Controller().play()

#------------------------------------------
'''


for ship in player.ships:
    print("{} start coord:".format(ship.__class__.__name__))
    (ship.row,ship.col) = ask_coord()
    print("Horizontal or vertical [h|v]?")
    ship.direction = input('> ').lower().strip()
    if ship.direction == 'h':
        for col in range(ship.size):
            grid[ship.row][ship.col + col] = ship.char
    show_grid()
'''
