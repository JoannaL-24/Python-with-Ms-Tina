#lists have index start with 0 as the order does not matter and is easier in math
animals = ["bear", "python", "peacock", "kangaroo", "whale", "platypus"]

print(f"The animal at 1 is the second animal, which is a {animals[1]}")
print(f"The third animal is at 2 and is a {animals[2]}.")
print(f"The first animal is at 0 and is a {animals[0]}.")
print(f"The animal at 3 is the fourth animal, which is a {animals[3]}.")
print(f"The fifth animal is at 4 and is a {animals[4]}.")
print(f"The animal at 2 is the third animal, which is a {animals[2]}.")
print(f"The sixth animal is at 5 and is a {animals[5]}.")
print(f"The animal at 4 is the fifth animal, which is a {animals[4]}.")

students = ["Bob", "Jessie", "Jack", "Malia", "BaBU"]
print(f"The second heighest student in the class is at 1 and is {students[1]}")
print(f"The student at 4 is the fifth highest, or the shortest, and is {students[4]}")
print(f"The second shortest student is at 3 and is {students[-2]}")

"""
Study Drill:
2. There must be the first day of January when there is the second of January. Since order matters for date, programmers' idea of index cannot apply. There is no such thing as a day of noting; the concept of zero collides with date.
"""