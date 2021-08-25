from sys import argv

script, filename = argv

print("We're going to erase %r" %filename)
print("Tf you don't want that, hit CTRL-C (^c).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file ...")
#the parameter 'w' tell the file to only be writen, so we can't access the information in the file
target = open(filename, 'r+')

print("Truncating the file. Goodbye!")
#truncate() deletes the pre-existing lines in the file
target.truncate()

print("T'm going to aks you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")


target.write(line1+"\n"+line2+"\n"+line3+"\n")


print("And finally, we close it.")
target.close()

target = open(filename, 'r')
print("I'm going to read the file.")
print(target.read())
target.close()