name = input("What is your name? ")
name = name.strip().lower()
quest = input("What is your quest? ")
quest = quest.strip().lower()

if name == "lancelot":
    color = ask("What is your favorite color? ")
    if color == 'blue':
        print("Ok, off you go then.")
    else:
        print("You are thown into the Gorge of Eternal Peril")
elif name == "robin":
    capital = input("What is the capital of Assyria? ").strip().lower()
    if capital == 'assur' or capital == 'ashur':
        print("Ok, off you go then.")
    else:
        print("You are thrown into the Gorge of Eternal Peril")
elif name == "arthur":
    speed = input("What is the air speed velocity of an unladen swallow? ")
    speed = speed.strip().lower()
    if speed.startswith("what do you mean, an african or a european swallow"):
        print("The Bridgekeeper is thrown into the Gorge of Eternal Peril")
    else:
        print("You are thrown into the Gorge of Eternal Peril")
else:
    color = ask("What is your favorite color? ")
    if color != '':
        print("Ok, off you go then")
    else:
        print("You are thrown into the Gorge of Eternal Peril")
