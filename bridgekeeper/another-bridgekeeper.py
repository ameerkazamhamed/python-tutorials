def ask(question):
    answer = input(question)
    answer = answer.strip().lower()
    print("You answered: " + answer)
    return answer

def die():
    print("Thou art thrown into the Gorge of Eternal Peril.")

def live():
    print("Fine, off you go then.")

##########################################

name = ask("What is your name? ")
quest = ask("What is your quest? ")

if name == 'lancelot':
    color = ask("What is your favorite color? ")
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
    color = ask("What is your favorite color? ")
    if color == "green":
        die()
    elif color == "blue":
        live()
    else:
        die()
elif name == 'arthur':
    answer = ask("What is the air speed velocity of an unlaiden swallow? ")
    if answer == 'what do you mean, an african or a european swallow':
        print("I don't know that.")
        print("The Bridgekeeper is thrown into the Gorge of Eternal Peril.")
        print("...")
    elif answer == '25 mph':
        live()
    else:
        die()
else:
    color = ask("What is your favorite color? ")
    if color != '':
        live()
    else:
        die()

