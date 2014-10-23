from turtle import Turtle
from random import random

def random_color():
    return (random(),random(),random())

bob = Turtle()

bob.pensize(7)
bob.pencolor(random_color())

for count in range(1,300):
    bob.forward(count)
    bob.right(121)
    
