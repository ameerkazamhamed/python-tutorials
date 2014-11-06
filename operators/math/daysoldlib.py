import random

def roll():
    number = random.randrange(3,19)
    return number



def calculate_days_old(years):
    return years * 365.242

def print_days_old():
    age = input("How old are you? ")
    age = int(age)
    days_old = calculate_days_old(age)
    print("You are {} days old".format(days_old))


def print_10(thing_to_print):
    print(thing_to_print * 10)

print(roll())
