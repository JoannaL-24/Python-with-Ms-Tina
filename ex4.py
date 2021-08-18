# variable assignment
cars = 100
# variable assignment
space_in_a_car = 4.0
# variable assignment
drivers = 30
# variable assignment
passengers = 90
# variable assignment
cars_not_driven = cars - drivers
# variable assignment
cars_driven = drivers
# variable assignment
carpool_capacity = cars_driven * space_in_a_car
# variable assignment
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,
      "in each car.")
#Python has no comment block
#triple "" is ignored in python as the string doesn't do anything
'''
Study Drill:
0. the NameError means the variable 'car_pool_capacity' is not declared yet
1. the 4.0 adds the floating point (decimal) to the result of calculations
'''