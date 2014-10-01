from story.character import Character

class You(Character):
    name = ''
    items = []
    part = None

    def take(cls,item):
        # check inventory slots for availability
        cls.items.append(item)
        print('You take the {}'.format(item))

    def can_take(cls,item):
        pass

    def can_move(cls,direction):
        pass
    
