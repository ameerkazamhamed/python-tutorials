import time

def badgers():
    badgers = 1
    while badgers <= 12:
        print(badgers,"badger")
        badgers += 1
        time.sleep(0.35)

def mushroom():
    for mushroom in range(2):
        print("MUUUSSSHRRROOMM!")
        time.sleep(0.7)

def snake(): pass

def run():
    badgers()
    mushroom()
    snake()

run()
