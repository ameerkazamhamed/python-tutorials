from story import Part
from sample.ocean import Ocean
from sample.house import House

MEADOW = '''
You are standing in a fresh green meadow with a house to the left
and an ocean to your right.
'''

class Meadow(Part):
    title = 'Meadow'
    description = MEADOW

    def on_ocean(cls):
        Ocean.enter()

    on_right = on_ocean

    def on_house(cls):
        House.enter()
