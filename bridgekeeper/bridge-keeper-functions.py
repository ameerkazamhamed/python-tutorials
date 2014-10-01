def die():
    print("You are thrown into the Gorge of Eternal Peril.")

def ask(question):
    answer = input(question).strip().lower()
    print("You answered: " + answer)
    return answer

############################################################

name = ask("What is your name? ")
quest = ask("What is your quest? ")

if name == "lancelot":
    color = ask("What is your favorite color? ")
    if color == 'blue':
        print("Ok, off you go then.")
    else:
        die()
elif name == "robin":
    capital = ask("What is the capital of Assyria? ")
    if capital == 'assur' or capital == 'ashur':
        print("Ok, off you go then.")
    else:
        print("You are thrown into the Gorge of Eternal Peril")
elif name == "arthur":
    speed = ask("What is the air speed velocity of an unladen swallow? ")
    if speed.startswith("what do you mean, an african or a european swallow"):
        print("The Bridgekeeper is thrown into the Gorge of Eternal Peril")
    else:
        die()
else:
    color = ask("What is your favorite color? ")
    if color != '':
        print("Ok, off you go then")
    else:
        die()
