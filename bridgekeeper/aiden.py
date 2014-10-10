print('What is your name?')
name = input('> ')

print('What is your quest?')
name = input('> ')

if name.startswith('lancelot'):
    print('What is your favorite color?')
    answer = input('> ')
elif name.startswith('robin'):
    print('What is the capital of Assyria?')
    answer = input('> ')
else:
    print('I do not know you')
