from random import randrange

MIN_STRENGTH = 3
MAX_STRENGTH = 18

def roll():
    return randrange(MIN_STRENGTH,MAX_STRENGTH)

def reverse(to_reverse):
    return to_reverse[::-1]
