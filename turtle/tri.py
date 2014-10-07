from turtle import Turtle

bob = Turtle()

bob.pensize(7)
bob.pencolor('purple')

for count in range(1,300):
    bob.forward(count)
    bob.right(121)
    
