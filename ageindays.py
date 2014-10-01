name = input("What is your name? ").strip().lower()

if name == "dayton":
    print("I'm honored.")
elif name == "reilly":
    print("Woah.")
else:
    print("DENIED!")
    exit()

print("Hello there " + name)


your_age = input("How old are you? ")
your_age = int(your_age)

days_old = 365 * your_age

print("You are at least " + str(days_old) + " days old.")


