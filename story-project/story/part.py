
import re

class Part():
    title = ''
    description = ''
    query = 'What do you do?'
    told = False
            
    #------------------------------------------------------------

    def on_think(cls):
        print("You are trying to think but nothing happens.")

    def on_look(cls):
        print(cls.description)

    def on_look_up_over_there(cls):
        print('Testing')

    #------------------------------------------------------------

    def on_bad_direction(cls):
        print("Doesn't look like you can go that way.")

    on_north = on_bad_direction


