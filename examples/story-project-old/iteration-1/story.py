#!/usr/bin/env python3

#------------------------------------------------

narrator_name = "Thomas"

print('''
Welcome to Python Stories. My name is {} and I will be your narrator.
'''.format(narrator_name))

#------------------------------------------------

name = input("We haven't met before, what may I call you? ")
name = name.strip().title()

#------------------------------------------------

print('''
Well hello there {}. I hope you enjoy the story. Unlike other stories which
you have read in this story _you_ are the protagonist, an active
participant. You make the decisions. You forward the plot.

Of course this means there are many paths and potential outcomes. With
each new release of this story the possibilities increase.
'''.format(name))

while True:
    answer = input("Shall we continue? ").strip().lower()
    if answer.startswith('y'):
        print("Wonderful! I do hope you enjoy yourself.")
        break
    elif answer.startswith('n'):
        print("Well ok then. But do try again soon.")
        exit()
    else:
        print("Um, I didn't catch that.")

#------------------------------------------------

print('''
Introduction.

You are standing on one side of a large ravine 

''')
