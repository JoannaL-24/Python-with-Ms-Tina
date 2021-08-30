def add(a,b):
    print("ADDING %d + %d" %(a,b))
    return a+b

def subtract(a,b):
    print("SUBTRACTING %d - %d"%(a, b))
    return a-b

def multiply(a,b):
    print("MULTIPLYING %d * %d"%(a,b))
    return a*b

def divide(a,b):
    print("DIVING %d / %d"%(a,b))
    return a/b

print("Let's do some math with just functions!")

age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print("Age: %d, Height: %d, Weight: %d, IQ: %d" %(age,height,weight,iq))

print("Here is a puzzle.")

what = add(age, subtract(height,multiply(weight,divide(iq,2))))
# normal formula: (age + (height - weight*iq/2))

print("That becomes: ", what, "Can you do it by hand?")

print("\nCalculate it with changed formula:")
print("weight/age + 16/9*iq is eqaull to:")
print(add(divide(weight, age),multiply(divide(16, 9),iq)))
print(weight/age + 16/9*iq)

print("\nCalculate it with changed formula:")
print("age + (height*age - weight*(iq+height)/2) is eqaull to:")
print(add(age,subtract(multiply(height, age),multiply(weight,divide(add(iq, height), 2)))))