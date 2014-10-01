
class World():
    '''A place for things to happen'''
    pass

class Entity():
    '''The living things in the World'''
    pass

class Event():
    '''Things that happen in the world'''
    def __init__(self,name,**kwargs):
        self.name = name
        self.data = kwargs

class Trainer(Entity):
    pass

class Computer(Trainer):
    '''An AI version of a trainer, for playing single player.'''
    pass

class Pokemon(Entity):
    pass

class PokemonMove():
    '''One of the many things a Pokemon can do, mostly in battle.
    (This should be subclassed for each move)'''
    pass

class Game():
    '''The main controller of the game'''

    def __init__(self):
        self.world = World()
        self.trainer = Trainer()
        self.computer = Computer()
        self.events = [] 

    def start():
        '''Setup the game and hand off'''
        mainloop()

    def mainloop(): 
        '''The main loop of the game.'''

''' class Event(): pass

class Move():

    def __init__(self):
        self.name = None

    def do(pokemon,foe):
        pass

class Pokemon():
    def __init__(self):
        self.moves = []
        self.player = None

    def do(self,move,foe):
        return move.do(self,foe)

class Player():

    def __init__(self):
        self.party = []
        self.pokemon = None

    def on_find_pokemon(self,pokemon):
        action = Game.ask()
        if action == 'fight':
            self.fight(pokemon)
        elif action == 'bag':
            self.bag()
        elif action == 'pokemon':
            self.select_pokemon()
        elif action == 'run':
            self.run()
        else:
            self._unknown_action()

    def fight(self,foe):
        Game.handle_fight(self,foe)
        move = Game.ask('Select a move ' + pokemon.moves + ': ')
        pokemon.do(move,foe)
        foe.do(move,pokemon)

    def bag(self): pass

    def select_pokemon(self): pass 

    def run(self): pass

    def _unknown_action(self): pass

class Game():

    def ask(text='What would you like to do?'):
        return input(text).strip().lower()

    def handle_fight(player,foe):

player = Player()
player.on_find_pokemon()
'''
