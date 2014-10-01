
'''
A simple example of string factoring to enable easy internationalization.
In other words, why the format() method rocks (and should be used over '+'
join operator, etc.)

You will need to understand the following concepts:

* string types
* variable assignment
* print() function
* input() function
* strip() method
* lower() method
* boolean types
* basic conditions
* == operator
* if/elif/else
* format() method basics

You should also fully understanding type casting (even though format() makes
this so easy you don't have to really think about it).

'''

## These strings are suitable for inclusion in a separate file where they
## can be loaded rather than hard-coded into the program because you do not
## have to know the values of the variables to be included, only where they
## will be positioned in the string (for now we just introduce {} although it
## can be used even more powerfully):

question_string_en = "What is your favorite color? "
question_string_fr = "Quelle est votre couleur préférée?"
answer_string_en = "You answered that '{}' is your favorite color."
answer_string_fr = "Vous avez répondu que '{}' est votre couleur préférée."

## In practice the 'en' and 'fr' can be determined simply by looking at the
## operating system preferences rather than asking directly:

lang = input("Language? (English or French) ")
lang = lang.strip()
lang = lang.lower()

## This too is done automatically by most internationalization libraries. We
## do it this way here to understand what is going on and why format() works:

if lang == 'english':
    lang == 'en'
    question_string = question_string_en
    answer_string = answer_string_en  
elif lang == "french":
    lang == 'fr'
    question_string = question_string_fr
    answer_string = answer_string_fr
else:
    print("I'm sorry, I don't speak that language")

## Note how clean the following is after string factoring. Consider how this
## code would look if we tried to do the same with the '+' join operator:
    
color = input(question_string)
print(answer_string.format(color))

