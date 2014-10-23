import turtle 
import random 

def random_color():
    return (random.random(),random.random(),random.random())

bob = turtle.Turtle()
bob.pensize(7)
bob.speed(100)

for count3 in range(20):
    for count2 in range(10):
        bob.pencolor(random_color())
        for count in range(4):
            bob.forward(20)
            bob.right(90)
        bob.forward(20)
    bob.left(120)
    bob.left(90)























input()
