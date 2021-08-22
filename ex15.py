#import argv module from the sys libery
from os import close
from sys import argv

#unpack argv and assign the 1st word to the variable script, 2nd word to another variable filename
script, filename = argv

#create a file type variable called txt from the parameter of filename
txt = open(filename)

#display "Here's your file %r:," while %r is filled with the raw code form of filename (the variable)
print("Here's your file %r:" % filename)
#tell the File to read in the content from filename and tell the terminal to print it down
print(txt.read())
#\n creates a next line character, and print "Type the filename again:"
print("\nType the filename again:")
#prompt the user for another input following "> " from the parameter
file_again = input("> ")

#create a file type variable called txt_again from the parameter of file_again
txt_again = open(file_again)

#tell the File called txt_again to read in the content from file_again and tell the terminal to print it out
print(txt_again.read())

close(txt)
close(txt_again)
#input() only take one line from the user(keyboard), which makes the text hard to see
#However, opening File from filename save a complete file and can display the content in a clear view.
#read() can have a parameter size, which tell the terminal only read the size of bytes
#there are other functions like readline() and readlines()