#introduce for loop and list
the_count = [1, 2, 3, 4, 5]
fruits = ['apples ', 'organges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in the_count:
    print("This is count %d"%number)

for fruit in fruits:
    print("A fruit of type: %s"% fruit)
for i in change:
    print("I got %r"%i)

elements = []

for i in range(0,6):
    print("Adding %d to the list."%i)
    elements.append(i)

for i in elements:
    print("Element was: %d"%i)

"""
Study Drill:
1.for can use in to loop list and range can be range(start, end, step), range(start, end), and range(stop)
2. yes
3.We can also do insert(), extend(), remove(), and pop()
  var-name = list[3:8] can slice a list from index 3 to 8 and store into another List called var-name
  To access data in a list: list[index]
"""