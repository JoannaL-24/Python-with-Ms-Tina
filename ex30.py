#introduce elif, which only consider when if statement before is not met.
people = 43
cars = 90
buses = 57

if cars > people:
    print("We should take cars.")
elif cars < people:
    print("We should not tale cars.")
else:
    print("We can;t decide.")

if buses > cars:
    print("That's tpp many buses.")
elif buses < cars:
    print("Maybe we could take the buses.")
else:
    print("We still can't decide.")

if people > buses:
    print("Alright, let's just take the buses.")
else:
    print("Fine, let's stay home then.")

if people > buses and people > cars:
    print("The world explodes.")
elif buses <= cars:
    print("Beep---!")

if buses > cars or people > cars:
    print("There are too less cars :(")

"""
Study Drill:
1. if statements check the condition follow, only if the conditions are met, the coding block under it would run. elif only run when the if statement before it doesn't run.
   In other words, elif must has a if statement before it.
"""