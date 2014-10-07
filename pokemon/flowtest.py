from cmd import Cmd

class PokemonShell(Cmd):
    intro  = 'Welcome to Pokemon shell. The text-only version of your favorite game.'
    prompt = '> '

    def do_north(self,arg):
        'Move North'
        print('You move north')

    def do_south(self,arg):
        'Move South'
        print('You move south')
    
    def do_east(self,arg):
        'Move East'
        print('You move east')

    def do_west(self,arg):
        'Move West'
        print(arg)
        print('You move west')

    def default(self,arg):
        print(arg)

if __name__ == '__main__':
    PokemonShell().cmdloop()
