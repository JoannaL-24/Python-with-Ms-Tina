ten_things = "Apples Oranges Crowns Telephone Light Sugar"

print("Wait there's not 10 things in that list, let's fix that.")

#splite(ten_things, " ") & call splite with ten_things and " "
#splite ten_things with " " betweem them
stuff = ten_things.split(" ")
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    #assign pop(more_stuff) into next_one & call pop with more_stuff
    #pop last elemente in more_stuff
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    #append(stuff, next_one) & call append with stuff and next_one
    #append next_one into stuff
    stuff.append(next_one)
    print("There's %d items now." %len(stuff))

print("There we go:", stuff)
print("Let's do some things with stuff")

print(stuff[1])
print(stuff[-1])
#pop(stuff) & call pop with stuff
#pop last elemente in stuff
print(stuff.pop())
#join(' ',stuff) & call join with ' ' and stuff
#join stuff with ' ' between them
print(' '.join(stuff))
#join("#",stuff[3:5]) & call join with ' ' and stuff[3:5]
#join stuff[3:5] with ' ' between them
#stuff [3:5] means elements with indexes 3(inclusive) to 5(exclusive)
print("#".join(stuff[3:5]))

"""
Study Drill:
5. class of something is the name of object's class(like an idea of type), whereas dir(something) is the attribute properties of that the class has.

"""