from story import Part,Teller as t

HOUSE = '''
You find yourself in a house with a coffee machine ...
'''

class House(Part):
    title = 'House'
    description = HOUSE
    query = 'Decided what do do next?'

    def on_up(cls):
        t.tell('Upstairs.')

    def on_down(cls):
        t.tell('Downstairs.')

    def on_take_coffee(cls):
        t.tell('You pick up the coffee')
        cls.you.take('coffee')
