from sys import argv

script, first, second, third = argv

print(f"The script is called: {script}")
print(f"Your first variable is: {first}")
print(f"Your second variable is: {second}")
print(f"Your third variable is: {third}")

forth = input("Hello, what is your name? ")
print(f"Nice to meet you, {forth}")
print("BaBU ~ !")

#assigning the unpacked values from argv requires the amount of variables to be equal to the the amount of words from argv