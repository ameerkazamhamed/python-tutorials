'''
Games need randomization. This little script introduces you to the
essential 'random' library module -- especially the randrange() function.

By now you should have a strong understanding of the basics
(types, variables, lists, if statments, loops, functions and methods).
'''

from random import randrange

def roll():
    minimum = 5
    maximum = 18
    return randrange(minimum, maximum)

def print_stats():
    print("-----------------")
    print("Strength:     {:>2}".format(strength))
    print("Intelligence: {:>2}".format(intelligence))
    print("Speed:        {:>2}".format(speed))
    print("-----------------")

while True:
    strength = roll()
    intelligence = roll()
    speed = roll()
    print_stats()

    if strength > 15 and intelligence > 15 and speed > 15:
        print("WOAHHHHH! Keep this one.")

    # any key to roll again (keeps the loop from going crazy, don't forget)
    input()
