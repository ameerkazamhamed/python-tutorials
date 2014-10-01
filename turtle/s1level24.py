
'''
This is the JavaScript we are going to port:

moveForward(100)
turnRight(90)
moveForward(100)

'''

from random import random

def random_color():
    return (random(),random(),random())


from turtle import Turtle
sloan = Turtle()

sloan.pensize(7)
sloan.pencolor('green')

while True:
    for count in range(4):
        sloan.pencolor(random_color())
        sloan.forward(100)
        sloan.right(90)
    sloan.right(10)

input()
