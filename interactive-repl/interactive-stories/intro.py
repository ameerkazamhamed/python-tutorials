title = 'Introduction'
text = 'This is the wonderous introduction.'

def begin(story):
    print('Beginning  part of the story')
    print(text)

def end(story):
    print('Ending  part of the story')

def on_enter(story):
    print('You enter the house.')
    story.part = 'closing'

