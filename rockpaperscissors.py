import time
import random
import re

you_win = 0
i_win = 0
ties = 0

def pick():
    import random
    p = random.randrange(1,4)
    options = { 1: "rock", 2: "paper", 3:"scissors" }
    return options[p]

print("Let's play Rock, Paper, Scissors")
time.sleep(1)

for i in range(3, 0, -1):
    print(i)
    time.sleep(1)
    
while True:
    your_pick = input("Your pick? ").strip().lower()
    if re.search('^r', your_pick):
        your_pick = "rock"
    my_pick = pick()
    print("You: " + your_pick)
    print("Me: " + my_pick)
    if your_pick == my_pick:
        print("It's a tie.")
        ties += 1
    elif your_pick == "rock" and my_pick == "scissors":
        print("I lose.")
        you_win += 1
    elif your_pick == "rock" and my_pick == "paper":
        print("I win.")
        i_win += 1
    elif your_pick == "paper" and my_pick == "rock":
        print("You win.")
        you_win += 1
    elif your_pick == "paper" and my_pick == "scissors":
        print("I win.")
        i_win += 1
    elif your_pick == "scissors" and my_pick == "paper":
        print("You win.")
        you_win += 1
    elif your_pick == "scissors" and my_pick == "rock":
        print("I win.")
        i_win += 1
    else:
        print("Doh!")
    print("YOU: {} ME: {} TIES: {}".format(you_win, i_win, ties))
