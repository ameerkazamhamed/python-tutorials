
# agetool-part1 (overly commented for student reference)

# print a generic welcome statement
print("Welcome!")

# get the name, strip off white space, make initial capital letters
name = input("What is your name? ").strip().title()

# join two strings and print (using '+' operand)
print("Hello " + name + ".")

# get the other person's name
other_name = input("What is the other person's name? ").strip().title()

# print a hello string for other person using perferred 'format()' method
print("Please tell {} hello for me.".format(other_name))

# get the ages using personalized prompts
first_age = input("How old are you {}? ".format(name)).strip()
other_age = input("And how old is {}?".format(other_name)).strip()

# convert the 'str' types (first_age, other_age) into numbers (int)
first_age = int(first_age)
other_age = int(other_age)

# calculate the age difference between them and make it always positive
years_apart = abs(first_age - other_age)

# convert the age difference to days (365.242 days per year)
days_apart = 365.242 * years_apart

# print the results for both years and days using a single 'format()'
print("You are {} years apart ({} days).".format(years_apart,days_apart))
