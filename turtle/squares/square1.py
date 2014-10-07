from turtle import Turtle
from random import random

def random_color():
    return (random(),random(),random())


artist = Turtle()
artist.penup()
artist.pensize(400)
artist.speed(7)
artist.hideturtle()
artist.backward(200)
artist.left(90)
artist.forward(200)
artist.right(90)
artist.pendown()

while True:
    for count in range(4):
        artist.pencolor(random_color())
        artist.forward(500)
        artist.right(90)

input()
