
def welcome():
    print("Welcome!")

#-------------------------------------

def hello(name=''):
    print("Hello {}".format(name))

#-------------------------------------

def ask_name():
    name = input("What is your name? ").strip().title()
    return name

#-------------------------------------

def area_of_circle(radius):
    import math
    area = math.pi * (radius ** 2)
    return area

######################################

welcome()
hello('Rob')
hello()
name1 = ask_name()
print(name1)
area = area_of_circle(2)
print(area)


