"""Fundamental conversion of direction and distance to a new x,y position.

Pay attention in Trigonometry in school. Here's why. Say you are at
some given position on a game board or canvas. You have a direction in
degrees, say 10 degrees to the right/east (on a world-ish map where 0
degrees is up). You travel a distance of say 50. You are at coordinates
10,13 currently on a traditional cartesian grid system, like the one you
learn about in school. What will be your new x and y coordinates?

The answer can only be determined using the `math.sin()` and `math.cos()`
functions.

"""

import math

# what we know
x = 10
y = 13
direction = 10
distance = 50

# what we want to know
newx = math.sin(math.radians(direction)) * distance + x
newy = math.cos(math.radians(direction)) * distance + y

print('newx',newx)
print('newy',newy)

# you can round if you like, but sometimes this introduces floating point
# problems

print('rounded x',round(newx))
print('rounded y',round(newy))
