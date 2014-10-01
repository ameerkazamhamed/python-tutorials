def ask(question):
    answer = input(question + "\n> ").strip().title()
    return answer


name = ask("Hey there, what do you call yourself?")
print("Well hello there {}".format(name))

other_name = ask("What is the name of the other person?")
print("Tell {} hello for me.".format(other_name))

first_age = int(ask("How old are you {}?".format(name)))
other_age = int(ask("How old is {}?".format(other_name)))

to_print = "So you, {}, are {} years old and {} is {} years old"
print(to_print.format(name, first_age, other_name, other_age))

years_apart = abs(first_age - other_age)
days_apart = years_apart * 365.242

to_print = "which makes you roughly {} years apart (about {} days)."
print(to_print.format(years_apart,days_apart))

if years_apart >= 15:
    if first_age > other_age:
        older = name
        younger = other_name
    else:
        older = other_name
        younger = name
    print("Wow, {} could be your parent, {}".format(older, younger))
