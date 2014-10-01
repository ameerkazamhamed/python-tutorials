desc_ocean = '''
OCEAN

You stand at the foot of majestic salt water waves crashing into
the shore with ...
'''

def area_ocean():
    print(desc_ocean)

#----------------------------------------------------------

desc_house = '''
HOUSE

You enter an old beach house... You see an ocean beach out the
back window from through the door.
'''

def area_house():
    print(desc_house)
    while True:
        action = prompt()
        if action.startswith(('back door','ocean')):
            area_ocean()
        elif action.startswith(('front')):
            area_meadow()

#----------------------------------------------------------

desc_meadow = '''
MEADOW

You are standing in a fresh green meadow with a house to the left
and an ocean to your right.
'''

def area_meadow():
    print(desc_meadow)
    while True:
        action = prompt()
        if action.startswith(('go right','ocean','go ocean')):
            area_ocean()
        elif action.startswith(('house','go house')):
            area_house()
        else:
            i_dont_know()
#----------------------------------------------------------

def prompt():
    print('What would you like to do?')
    answer = input('> ').strip().lower()
    return answer

def i_dont_know():
    print("You can't do that.")

#############################################################

area_meadow()




