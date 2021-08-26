#like scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print("arg1: %r, arg2: %r" %(arg1, arg2))

#another way
def print_two_again(arg1, arg2):
    print("arg1: %r, arg2: %r" %(arg1, arg2))

#only take one argument
def print_one(arg1):
    print("arg1: %r" %(arg1))

def print_none():
    print("I got nothing.")

def checklist():
    print("Checking for functions:")
    print("If checked, hit ENTER. If not, press CTRL-C.")
    input("Did you start your function definition with def?")
    input("Does your function name have only charaters and _ characters?")
    input("Did you put an open parenthesis ( right after the function name?")
    input("Did you put your arguments after the parenthesis (seoarated by commas?")
    input("Did you put your argument unique (meanung no dupicated names)?")
    input("Did you put a close parenthesis and a colon ): after the argument?")
    input("Did you indent all lines of code you want in the function four spaces?")
    input("Did you \"end\" your function by going bakc to writing with no indent (dedenting)?")
    print()

def checklist_run():
    print("Checking for running functions:")
    print("If checked, hit ENTER. If not, press CTRL-C.")
    input("Did you call/ use/ run this function by typing its name?")
    input("Did you put the ( character after the name to run it?")
    input("Dis you put the values you want into the parentheis seperated by commas?")
    input("Did you end the function call with a ) character?")
    print()

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()
checklist()
checklist_run()