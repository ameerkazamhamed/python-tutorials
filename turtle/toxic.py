from turtle import Turtle
from random import random

def random_color():
    return (random(),random(),random())

bob = Turtle()
bob.pensize(7)
bob.speed(0)

length = 10
direction = 1
while True:
    for count in range(200):
        bob.color(random_color())
        bob.forward(length)
        bob.left(185)
        length += 5 * direction
    direction = -direction

