class Protagonist():

    def __init__(self):
        self.name = "You"

class Story():
    text = {}

    def __init__(self,protagonist):
        self.protagonist = protagonist
        self.storyteller = None

    #---------------------------------------------------------

    text["introduction"]["title"] = "Introduction"
    text["introduction"]["description"] = '''
{name} you are standing before a home in an empty clearing.
'''

    def introduction(self):
        self.storyteller.tell("introduction")
        while True:
            response = self.storyteller.prompt()
            if response == "left":
                self.engine_room()
            elif response == "look":
                self.storyteller.tell()

    #---------------------------------------------------------
    
    def engine_room(self):
        self.storyteller.tell("You are in the engine room")
        while True:
            response = self.storyteller.prompt()
            if response == "left":
                self.engine_room()

class StoryTeller():

    def __init__(self,story):
        story.storyteller = self
        self.story = story
        self.actions = {
            'show_inventory': 'show_inventory',
            'show_stats': 'show_stats',
            'i': 'show_inventory',
            'inventory': 'show_inventory',
            'stats': 'show_stats'
            }
        self.keywords = {}

    def tell_story(self):
        self.story.introduction()

    def ask_name(self):
        name = input("What is your name? ")
        name = name.strip().lower().title()
        if name == "Joe":
            print("I'm sorry you have such a generic name. We'll have fun anyway.")
        elif name == "Stanley":
            print("Oh the cheek on this one.")
        else:
            print("Welcome {}".format(name))
        story.protagonist.name = name
        self.keywords["name"] = name

    def tell(self):
        print(self.story.current.format(**self.keywords))

    def prompt(self,string="What would you like to do? "):

        while True:
            action = input(string).strip().lower()
            action = '_'.join(action.split())
            if action in self.actions.keys():
                method = getattr(__class__, self.actions[action])
                if not method:
                    raise Exception("Action {} not implemented".format(action))
                method(self)
            else:
                return action

    def show_stats(self):
        print("Would show stats.")

    def show_inventory(self):
        print("Would show inventory")

##################################


you = Protagonist()
story = Story(you)
stanley = StoryTeller(story)

stanley.ask_name()
stanley.tell_story()






    
