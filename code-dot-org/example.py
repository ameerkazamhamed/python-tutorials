
# http://studio.code.org/s/1/level/25

'''

'''

from turtle import Turtle
from random import random

def random_color():
    return (random(),random(),random())

bob = Turtle()
bob.pensize(7)


while True:
    for count in range(4):
        bob.color(random_color())
        bob.forward(100)
        bob.right(90)
    bob.right(10)

input()
