import time

def ask(question):
    answer = input(question)
    answer = answer.strip().lower()
    #print("You answered: {}".format(answer))
    return answer

def likes(food):
    yeah = ('yeah','yes','yup','uhun','yea')
    answer = ask('Do you like {}?'.format(food))
    if answer.startswith(yeah):
        print("♫ Yeah we like {}! ♫".format(food))
        time.sleep(1)
    return answer.startswith(yeah)

def doo_doo_doo_dupe():
    print('♫ Doo, doo doo dupe ♫')

def mouthful():
    print("♫ Can't wait to get a mouthful! ♫")
    time.sleep(2)

def chorus():
    time.sleep(1)
    for count in range(4):
        print("♫ WAFFFFFFLES!!! ♫")
        time.sleep(2.75)
    
#-------------------------------------------------

for verse in range(2):
    if likes('waffles'):
        if likes('pancakes'):
            if likes('french toast'):
                doo_doo_doo_dupe()
                mouthful()
                chorus()
