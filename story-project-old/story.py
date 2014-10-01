from storylib.Protagonist import Protagonist
from storylib.StoryTeller import StoryTeller
from stories.Sample import Story

protagonist = Protagonist()
story = Story(protagonist)
teller = StoryTeller(story)

teller.welcome()
teller.ask_race()
teller.ask_gender()
teller.ask_age()
teller.show_status()



