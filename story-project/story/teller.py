from story import You

class Teller():
    part = None
    actions = None

    @staticmethod
    def build_actions_dictionary(story):
        print(story.keys())
        
    @staticmethod
    def begin(story):
        Teller.build_actions_dictionary(story)
        Teller.tell(story.Intro)

    @staticmethod
    def prompt(part):
        print('[{}] {}'.format(part.title,part.query))
        return input('> ').strip().lower()
        
    @staticmethod
    def tell(part):
        Teller.part = part
        if not part.told:
            print(part.description)
            part.told = True
        action = Teller.prompt(part)
        #TODO finish verb lookup, pass it.
