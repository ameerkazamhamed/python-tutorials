"""A simple interactive story engine."""

import importlib

class Story:
    
    def __init__(self):
        """All stories must have an intro module"""
        pass

    @property
    def part(self):
        return self._part

    @part.setter
    def part(self,part):
        """Set current part of the story to the corresponding module."""
        if isinstance(part,str):
            self._part = importlib.import_module(part)
        else:
            self._part = part

class Character():
    health = 100
    items = []

class Teller:
    def __init__(self,story,you):
        self.story = story
        self.you = you

    def on(self,action):
        try: 
            (getattr(self.story, 'on_' + action))()
            #TODO: add cascading calls to characters, items, room
        except AttributeError:
            pass

    def goto(self,part):
        self.story.part = part
        self.story.part.begin(story)

class Item: pass

if __name__ == '__main__':
    story = Story()
    you = Character()
    teller = Teller(story,you)

    teller.goto('intro')
    teller.on('enter')
    print(story.part.title)
    teller.goto('closing')
