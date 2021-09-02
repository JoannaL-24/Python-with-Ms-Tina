#learn if statements and comparison
people = 20
cats = 30
dogs = 15

if people <cats:
    print("Too many cats! The world is doomed!")

if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")

dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")

if people == dogs:
    print("People are dogs.")

if people != 30 and cats > 10:
    print("People are cats")
    print("This is a world with cats, yeah")

if True:
    print("This line is always printed.")

if not False:
    print("So does this line.")

"""
Study Drill:
1. if statement wrap the code it with indention. Only when the condition of the if statement is met, the wrapped codes would be run.
2. As Python can not use {} for coding blocks such as functions and if statements, 4 spaces indention takes place instead to identify the coding blocks
3. Without indention, the compiler would not recognize the code to belone to the if statement, and the compiler would throw an error tell that it expect a indented coding block.
5. the result in the terminal would be different as the greates to smallest relationships between the variables may change.
"""