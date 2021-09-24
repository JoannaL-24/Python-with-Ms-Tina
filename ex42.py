#Animal is-a object
class Animal(object):
    #Aminal has a function of speak()
    def speak(self):
        print("Hi!")

#Dog is a Animal
class Dog(Animal):
    def __init__(self, name):
        #Dog has a name
        self.name = name

#Cat is a Animal
class Cat(Animal):
    def __init__(self, name):
        #Cat has a name
        self.name = name

#Person is a object
class Person(object):
    def __init__(self,name):
        #Person has a name
        self.name = name
        #Person has-a pet of some kind
        self.pet = []
    #Person has a function of sleep()
    def sleep(self):
        print("ZZz--")

#Employee is a Person
class Employee(Person):
    def __init__(self, name, salary):
        #pass parameters for Person to the parent function
        super(Employee,self).__init__(name)
        #Employee has a salary
        self.salary = salary

#Fish is an object
class Fish(object):
    #Fish has a function of swim()
    def swim(self):
        print("swiming~~")

#Salmon is a Fish
class Salmon(Fish):
    pass

#Halibut is a Fish
class Halibut(Fish):
    pass

#rover is an object of Dog
rover = Dog("Rover")
#satan is an object of Cat
satan= Cat("Satan")
satan.speak()
#satan is an object of Cat
bob = Dog("Bob")

#mary is an object of Person
mary = Person("Mary")
#the object mary of class Person has a pet of satan
mary.pet = [satan, bob]
#frank is an Employee with a salary of 120000
frank = Employee("Frank",120000)
#the object frank of class employee has a pet of rover
frank.pet = [rover]
frank.sleep()

#flipper is a Fish
flipper = Fish()
#crouse is a Salmon
crouse = Salmon()
#harry is a Halibut
harry = Halibut()
crouse.swim()

"""
1. In python2, there are flaws in the original rendition, so there are new and old syntexes for class. However, in python3, there is two syntexes result the same.
2. Yes, class we created automatically inherent the object class. So, classes are object too.
6. yes, has-many relationship refers to multiple inheritance. It is not favor because if the child classes both have the same function, the compiler would be confused that which function from the classes is the code calling.
"""