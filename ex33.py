#introduce while loop

def setNum(end, step):
    i = 0
    while i < end:
        print("At the top i is %d" %i)
        numbers.append(i)

        i += step
        print("Numbers now: ", numbers)
        print("At the bottom i is %d" %i)

numbers = []
numFor = []
setNum(10, 2)
setNum(3, 1)

for i in range(6):
    print("At the top i is %d" %i)
    numFor.append(i)
    print("Numbers now: ", numFor)
    print("At the bottom i is %d" % (i+1))


print("The numbers: ")

for num in numbers:
    print(num)

"""
Study Drill:
4. With function, we can repeat the actions for many times. numbers the list would keep add on everytime we call the function.
5. With for and range(), we don't need to increase i by 1 every loop. The for loop would add 1 to its iterator by itself by the end of each loop.
"""