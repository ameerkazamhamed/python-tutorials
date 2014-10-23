from turtle import Turtle
from random import random,choice

bob = Turtle()
bob.pensize(100)
bob.speed(0)

colors = ['red','blue','gold','violet']

def random_color():
    return (random(),random(),random())

while True:
    bob.pencolor(random_color())
    for count in range(4):
        bob.forward(200)
        bob.right(90)
    bob.right(10)

input()
