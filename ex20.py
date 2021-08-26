#import the module from sys the libery
from sys import argv

#unpacked argv from compiling and assaign them into script and infile
script, infile = argv

#define a function called print_all that take 1 parameters called f
def print_all(f):
    #print all infomation in the file f
    print(f.read())

#define a function called rewind that take 1 parameters called f
def rewind(f):
    #relocate the cursor to the beginning of the file f from where it writen, appended, or read
    f.seek(0)

#define a function called print_a_line that take 2 parameters called line_count and f.
def print_a_line(line_count, f):
    #print the line_count and the line that the cursor is at
    print(line_count, f.readline())

# assign a File object from infile into currfile
currfile = open(infile)

#display "First let's print the whole file:" with one extra enter key pressed in terminal
print("First let's print the whole file:\n")
#call the print_all function, given the opened File currfile
print_all(currfile)
#diplay "Now let's rewind, kind of like a tape."
print("Now let's rewind, kind of like a tape.")
#call the rewind function, given the opened File currfile
rewind(currfile)
#display "Let's print three lines:" in terminal
print("Let's print three lines:")

#loop i through 1 to 3
i=1
while i<4:
    #call function print_a_line with i as currline in the parameter and currfile as f in the parameter
    print_a_line(i,currfile)
    i+=1
    #as we just rewind() the File currfile, making the cursor to line 1, the i becomes like a line count

currfile.close()