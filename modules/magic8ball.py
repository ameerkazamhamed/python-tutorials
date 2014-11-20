import random

print('Welcome to the Magic Eight Ball!')
print('Please type your question for me.')

while True:
    question = input('> ')
    answers = [
        'Yes.', 
        'No.', 
        'Definitely.', 
        "I can't believe it.",
        'Maybe.'
    ]
    answer = random.choice(answers)
    print(answer)

