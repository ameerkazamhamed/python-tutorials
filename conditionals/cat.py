import random

name = input("What do you call yourself?")
print('Yo ' + name + ' wasssssup')

ate_cat = input(name + " did you eat my cat?")

if ate_cat == 'yes':
    answers = ['No way','Cool']
    print(random.choice(answers))
elif ate_cat == 'maybe':
    print('I bet you did.')
elif ate_cat == 'nah':
    print('I so do not believe you.')
else:
    print('I wonder who did.')

