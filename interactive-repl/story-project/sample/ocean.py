from story import Part

OCEAN = '''
You stand at the foot of majestic salt water waves crashing into
the shore with ...
'''

class Ocean(Part):
    title = 'Ocean'
    description = OCEAN
    query = 'What now?'

    def on_up(cls):
        print('Up.')

    on_swim = on_up

    def on_down(cls):
        print('Down.')
