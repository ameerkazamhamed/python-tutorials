from story import Part,Teller

INTRO = '''
This is the wonderous introduction.
'''

class Intro(Part):
    title = 'Intro'
    description = INTRO
    query = 'Decided what do do next?'

    def on_begin():
        print(Teller.part)
