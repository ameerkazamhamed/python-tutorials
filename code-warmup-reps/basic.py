#!/usr/bin/env python
## Code Reps

''' Print Hello '''
print("Hello")

''' Define a variable containing a string and print it. '''
name = "Monty"
print(name)

''' Ask user to type in their name, then put the user's answer in a variable. '''
name = input("What is your name? ")

''' Remove any spaces surrounding your name and capitalize it properly. '''
name = name.strip().title()

''' Print the user's name. '''
print(name)

''' Print 'Hello ' joined with the user's name,. '''
print("Hello " + name)

''' Define a variable containing the number of weeks in a year and print it. '''
weeks_in_year = 52
print("Weeks in a year:")
print(weeks_in_year)

''' Ask the user to type in how old they are, store it, then print it. '''
age = input("How old are you? ")
print("Your age:")
print(age)

''' Remove white spaces surround the age number and turn it into a number. '''
age = age.strip()
age = int(age)

''' Check that user entered a number greater than 0, if so ask them again.  '''
if age < 0:
    print("Ummmm, yeah right. Typing from the womb are we? lol")
    age = input("How old are you really?")
    age = age.strip()
    age = int(age)

''' Check if the user entered an age of 123. If so change the name variable
and print hello to the only 123-year-old man ever recorded, Carmelo Flores
Laura from Bolivia.'''
if age == 123:
    print("Hey there Carmelo, how's Bolivia these days?")
    name = "Carmelo"

''' Check that user entered a number less than 123, if so ask them again. '''
if age > 123:
    print("Either you are the undocumented oldest person ever, or your lying.")
    age = input("Either way, enter something smaller please: ")
    age = age.strip()
    age = int(age)

''' Tell the user how old they are using a string, '+', and the age variable. '''
print("You are " + str(age) + " years old.")

''' Calculate how old the user is in weeks and put into a variable. '''
age_in_weeks = weeks_in_year * age

''' Print the users age in years and weeks using a string and variables. '''
print("You are " + str(age) + " years old and " + str(age_in_weeks) + " weeks old.")

''' Print the users name, age, and age in weeks using a string and format(). '''
string = "{}, you are {} years old or {} weeks old."
formatted_string = string.format(name,age,age_in_weeks)
print(formatted_string)

