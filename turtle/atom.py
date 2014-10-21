import turtle

bob = turtle.Turtle()
bob.pensize(1)
bob.speed(50)
bob.left(90)
bob.forward(50)
bob.right(90)
for counter in range(600):
    bob.forward(counter)
    bob.right(counter)

input()
