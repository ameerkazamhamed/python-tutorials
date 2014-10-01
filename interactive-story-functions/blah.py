



def ask_age():

    while True:
        age = int(input("How old are you?" ))

        if age <=0:
            print("I'm very impressed with your in-womb typing ability.")
            print("But I think we need to wait until you are older.")
        elif age < 8:
            print("I'm sorry you have not yet reached the age of reason.")
            print("But that's perfectly fine. You seem very intelligent")
        elif age == 16:
            print("The glorious age of car driving mastery.")
        else:
            print("Thank you for revealing that delicate information")

        if age > 0: break
    
    return age

def ask_race():
    race = input("What is your race? [human, avian, drakon, terran]")
    race = race.strip()
    race = race.lower()
    if race == "human":
        print("You picked human. Not much more to say")
    elif race == "avian":
        print('''
You picked avian, the avians are an advanced old galactic race. evalved
from a bird like creature, avians get there energy from crystals harvested
from there home planet, Avok. Althow not as smart as Humans, Avians are a
force to be recognized
''')
    elif race == "drakon"
        print('''
You picked Drakon, the drakons are a bold, dragon/human like
race. Many discrimanate againced them, but the Drakons don't care much.
With thick scales and amazing physical abilitys, Drakons are a force to
be recognized.
''')    

def create_player():
    player = {}
    player["name"] = input("What is your name? ")
    player["age"] = ask_age()
    player["race"] = ask_race()
    return player

def tell_beginning(player):
    print('Mining Ship')
    print()
    print('''
{name}, you are on a {ship}
'''.format(**player))
    

#################################

player = create_player()

tell_beginning(player)









