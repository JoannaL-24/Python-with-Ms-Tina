#these is the other I tried to use input()
name = input("What is your name? ")
age = input("How old are you? ")
gender = input("What is your gender? ")
height = input("How tall are you? ")
weight = input("How much do you weight? ")
hobby = input("What are some hobbies you like? ")

print("So, you're %r old, %r tall and %r heavy." %(age, height, weight))

#python raw_input() is combined with input() since python 3. Currently, input() takes all input from keyboard as strings
#because we use %r, the terminal prints the way we write the string when coding (the raw format in code). Making %r to %s would make '6\'2"' to '6'2"', which tells the terminal to print the height as a string