
class Player():
    pass

class ComputerPlayer(Player):
    pass

class HumanPlayer(Player):
    pass

class ShellController():

    def run(self):
        print('Welcome to ConnectFour!')

if __name__ == '__main__':

    #game = ShellController()
    #game.run()
    grid = Grid() 
    print(grid.rows)

