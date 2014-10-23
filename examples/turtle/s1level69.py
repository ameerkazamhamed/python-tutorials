#!/bin/env python3

from turtle import Turtle
from random import random

def random_color():
    return (random(),random(),random())


bob = Turtle()
bob.pensize(6)
bob.speed(0)

for counter in range(1,900):
    bob.pencolor(random_color())
    bob.forward(counter)
    bob.right(67)























input()
