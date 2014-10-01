from random import randrange

def roll():
    return randrange(3,18)

strength = roll()
intelligence = roll()
speed = roll()

print("Strength:      {:>3}".format(strength))
print("Intelligence:  {:>3}".format(intelligence))
print("Speed:         {:>3}".format(speed))

