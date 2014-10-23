from turtle import Turtle
from random import random

def color_random():
    return (random(),random(),random())

'''
turnRight(45);
moveForward(150);
for (var count3 = 0; count3 < 30; count3++) {
          for (var count2 = 0; count2 < 10; count2++) {
                  penColour(colour_random());
                      for (var count = 0; count < 7; count++) {
                                moveForward(20);
                                      turnRight(60);
                                          }
                          moveForward(20);
                            }
            turnRight(199);
            }
'''

bob = Turtle()
bob.pensize(7)

for count3 in range(30):
    for count2 in range(10):
        bob.pencolor(color_random())
        for count in range(7):
            bob.forward(20)
            bob.right(60)
        bob.forward(20)
    bob.right(199)

