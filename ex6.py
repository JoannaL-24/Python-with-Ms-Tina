#assign 10 into the variable called types_of_people
types_of_people = 10
#assign the string "There are {types_of_people} types of people.", where {types_of_people} refers the variable "types_of_people", into x
x = f"There are {types_of_people} types of people."

#assign the string "binary" into the variable called binary
binary = "binary"
#assign the string "don't" into the variable called do_not
do_not = "don't"
#assign the formated string "Those who know {binary} and those who {do_not}." into the variable called binary
#where the {binary} refers to the variable binary in line 7 and {do_not} refers to the variable do_not in line 9
y = f"Those who know {binary} and those who {do_not}."

#tell the terminal to print(display) the string stored in the variable x and y with enter between
print(x)
print(y)

#tell the terminal to print a formated string, which is "I said: {x}" and {x} refers to the variable x
print(f"I said: {x}")
#tell the terminal to print a formated string, which is "I also said: '{y}'" and {y} refers to the variable y
#Thus, the sentence printed is "I also said: 'Those who know binary and those who don't.'"
print(f"I also said: '{y}'")

#create a variable called hilarious and assign False to it
hilarious = False
#create a variable called joke_evaluation and assign the string "Isn't that joke so funny?! {}" with the {} providing a space for any variable to fill in
joke_evaluation = "Isn't that joke so funny?! {}"

#print another form of formatted string, which refers to the variable joke_evaluation and plug another variable hilarious into the {} in joke_evaluation
print(joke_evaluation.format(hilarious))

#assaign "This is the left side of..." into a variable called w
w = "This is the left side of..."
#assaign "a string with a right side." into a variable called e
e = "a string with a right side."

#print the combination of the variable w and e, which results "This is the left side of ...a string with a right side."
print(w + e)

#below is not a comment, but that is for format and convenience
"""
Where string is put inside in another string:
- lines 4, 12, 19, 22, 30

Explain why adding the two strings w and e with + makes a longer string.
- line 38 adds the two strings togather and print the result. It is a string w with another string called e following behind.
"""