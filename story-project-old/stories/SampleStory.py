class Story:
    keywords = {
        'name': 'you'
        }

    def tell(string):
        print(string.format(**Story.keywords))
    

    def game_intro():
        Story.tell("Welcome {name} to our {color} humble game")

Story.keywords['color'] = 'red'
Story.game_intro()
