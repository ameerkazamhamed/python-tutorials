
print('''
Stop. Who would cross the Bridge of Death must answer me these questions three,
ere the other side he see.
''')

name = input("What ... is your name? ")
print("You answered: {}".format(name))

quest = input("What ... is your quest? ")
print("You answered: {}".format(quest))

color = input("What is your favorite color?")
print("You answered: {}".format(color))

while True:

    if quest == "to seek the grail":
        print("Most excellent the grail must be found")
        break
    
    elif quest.startswith("to seek")":
        print("Yes! The Holy Poop of Antioche must be found")
        break
    
    else:
        print("I'm not aware of that quest")

print("Alrighty then.")
