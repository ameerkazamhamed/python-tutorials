from turtle import Turtle
from random import random


def random_color():
    return (random(),random(),random())


bob = Turtle()
bob.pensize(100)

alice = Turtle()

while True:
    alice.right(20)
    alice.forward(200)
    for count in range(4):
        bob.pencolor(random_color())
        bob.forward(100)
        bob.right(90)
    bob.right(10)

input()


