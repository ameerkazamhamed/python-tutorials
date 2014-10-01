
def die():
    print("Thou art cast into the Gorge of Eternal Peril")
    print("You have died.")

def live():
    print("Fine, off you go then.")
    print("You live on.")

def ask(question):
    answer = input(question)
    answer = answer.strip().lower()
    print("Thou hast answered: " + answer)
    return answer

def ask_color():
    answer = ask("What is your favorite color? ")
    return answer

##########################################

name = ask("What is your name? ")
quest = ask("What is your quest? ")

if name == 'lancelot':
    color = ask_color()
    if color == 'blue':
        live()
    else:
        die()
elif name == 'robin':
    capital = ask("What is the capital of Assyria? ")
    if capital == 'assur' or capital == 'ashur':
        live()
    else:
        die()
elif name == 'galahad':
    color = ask_color()
    if color == 'blue':
        die()
    else:
        live()
elif name == 'arthur':
    answer = ask("What is the air speed velocity of an unladen swallow? ")
    if answer == "what do you mean, an african or a european swallow?":
        live()
        print("The BridgeKeeper is thrown into the Gorge of Eternal Peril")
    elif answer == '25 mph':
        live()
    else:
        die()
else:
    color = ask("What is your favorite color? ")
    if not color == '':
        live()
    else:
        die()


