
def ask(question):
    print(question)
    answer = input('> ').strip()
    return answer

#-----------------------------------------------------------

print('''
Welcome to the age difference calculator!
''')

name1 = ask("What is your name?").title()
name2 = ask("What is the other person's name?").title()
age1 = int(ask("How old are you?"))
age2 = int(ask("How old is the other person?"))

years_apart = abs(age1 - age2)

print('{} and {} are {} years apart.'.format(name1,name2,years_apart))

#TODO calculate the rough number of days apart

#TODO improve to use calendar
