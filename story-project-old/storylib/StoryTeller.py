
class StoryTeller():

    def __init__(self,story):
        self.story = story

    def welcome(self):
        print("Welcome!")
        print()

    def ask_player_race(self):
        while True:
            race = input("What race would you like? [human|elf|wolf] ")
            race = race.strip().lower()
            if race.startswith('h'):
                print("You've picked human.")
                self.player.race = 'human'
                break
            elif race.startswith('e'):
                print("You've picked elf.")
                self.player.race = 'elf'
                break
            elif race.startswith('w'):
                print("You've picked wolf")
                self.player.race = 'wolf'
                break
            else:
                print("Sorry that's not a supported race.")

    def ask_player_gender(self): pass

    def ask_player_age(self): pass

    def show_player_race(self):
        print("Race: {}".format(self.player.race))
        
    def show_player_stats(self):
        p = self.player
        print("Strength: {}".format(p.strength))

    def show_player(self):
        self.show_player_stats()
        self.show_player_race()

    def set_game(self,game):
        self.game = game
        
