import json

spam = {'foo':'bar',1:'one',"two":2}

print(spam)
print(type(spam))
print(json.dumps(spam))

if type(spam) is dict:
    print("Yep, I'm a dictionary.")

if type(spam) is not list:
    print("Nope, not a dictionary.")

if 1 in spam and 'two' in spam:
    print("But I lookup keys like in a list.")

spam = list(spam)
print(spam)
if type(spam) is list:
    print("And forcing me into a list grabs all my keys.")
