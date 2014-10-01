import random

answers = ['Yes.','No.','Maybe.']

print("Welcome to the Magic Eight Ball")

while True:
    print("Ask me a question")
    question = input('> ')
    answer = random.choice(answers)
    print(answer)
