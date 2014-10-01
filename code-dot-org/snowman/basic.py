#!/usr/bin/env python3

# smallinbig - http://studio.code.org/s/1/level/66

## TODO port to another library, this is WAY too slow.

'''javascript

// draw_a_snowman
turnLeft(90);
var distances = [(250) * 0.5, (250) * 0.3,(250) * 0.2];
for (var counter = 0; counter < 6; counter++) {

  var distance = distances[counter < 3 ? counter: 5 - counter] / 57.5;
  for (var degree = 0; degree < 90; degree++) {
    moveForward(distance);
    turnRight(2);
  }
  if (counter != 2) {
    turnLeft(180);
  }
}
turnLeft(90);

'''

import tk.turtle

window = turtle.Screen()
george = turtle.Turtle()

george.width(3)
george.color('green')
george.speed(0)

george.left(180)
distances = [250 * 0.5, 250 * 0.3, 250 * 0.2]
for counter in range(0,6):
    if counter < 3:
        distance_index = counter
    else:
        distance_index = 5 - counter
    distance = distances[distance_index] / 57.5 
    for degree in range(0,90):
        george.forward(distance)
        george.right(2)
    if counter != 2:
        george.left(180)
george.left(180)

window.mainloop()
