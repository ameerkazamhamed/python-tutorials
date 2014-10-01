
name = input("Tell me your name perty-please?")
name = name.strip().title()

print("Nice to meet you " + name)

age = input("How old are you? ")
age = age.strip()
print("Awwww, you are " + age + " years old.")

age = int(age)

days_in_year = 365.242
days_old = age * days_in_year

print("You are " + str(days_old) + " days old")

