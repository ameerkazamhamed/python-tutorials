# -*- coding: utf-8 -*-
"""Simple interactive story engine.

This module contains some minimal classes and structure to create
interactive stories (sometimes called interactive fiction) written
entirely in Python. Authors can create stories as simple or as complex
as they like since it is all just Python even including minigames within
a given ``part`` of the story.

"""

import importlib

class Story:

    @property
    def part(self):
        """Reference to the imported module containing part of story."""
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
