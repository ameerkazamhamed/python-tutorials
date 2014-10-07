from turtle import Turtle
from random import random

def random_color():
    return(random(),random(),random())

bob = Turtle()
bob.pensize(100)
bob.speed(0)
'''
while True:
    for counter in range(1,1000):
        bob.pencolor(random_color())
        bob.forward(counter + 20)
        bob.right(90)
    bob.up()
    bob.home()
    bob.down()
'''

size = 100
while True:
    for angle in range(36):
        bob.pencolor(random_color())
        for count in range(4):
            bob.forward(size)
            bob.right(90)
        bob.right(10)
    size += 5

input()
