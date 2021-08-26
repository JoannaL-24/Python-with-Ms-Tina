#define a function called cheese_and_crackers that take 2 parameters(arguments), which are called cheese_count and boxes_of_crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    #print the value in cheese_count with decimal incrementation by %d
    print("You have %d cheese!" %cheese_count)
    #print the value in boxes_of_crackers with decimal incrementation by %d
    print("You have %d boxes of creckers!"%boxes_of_crackers)
    #display "Man that's enough for a party!" in the terminal
    print("Man that's enough for a party!")
    #display "Get a blanket." with extra enter key pressed in the terminal
    print("Get a blanket.\n")

#display "We can just give the function numbers directly" in the terminal
print("We can just give the function numbers directly")
#call(run) the function giving parameters that 20 as cheese_count and 30 as boxes_of_cracker
cheese_and_crackers(20,30)

#display "OR, we can use variables from our script:" in the terminal
print("OR, we can use variables from our script:")
#assign 10 to amount_of_cheese
amount_of_cheese = 10
#assign 50 to amount_of_crackers
amount_of_crackers = 50

#call(run) the function giving parameters that the value in amount_of_cheese as cheese_count and value in amount_of_crackers as boxes_of_cracker
cheese_and_crackers(amount_of_cheese,amount_of_crackers)

#display "We can even do math inside too:" in the terminal
print("We can even do math inside too:")
#call(run) the function giving parameters that (10+20) as cheese_count and (5+6) as boxes_of_cracker
#the math would be done first
cheese_and_crackers(10+20,5+6)

#display "We can combine the two, variables and math:" in the terminal
print("We can combine the two, variables and math:")
#call(run) the function giving parameters that (amount_of_cheese+100) as cheese_count and (amount_of_crackers+1000) as boxes_of_cracker
#when doing the math the varibles be accessed and the additions take place
cheese_and_crackers(amount_of_cheese+100,amount_of_crackers+1000)

#Own function
def fatorial(num):
    if not(isinstance(num,int)):
        return "not an integer"
    if num==1:
        return 1
    else:
        return(num*fatorial(num-1))

for i in range(1, 11):
    print("Factorial of %d is %d"%(i,fatorial(i)))
constant = 1
num =3.14
print("Factorial of %r is %r"%((num),fatorial(num)))
print("Factorial of %r is %r"%((num+constant),fatorial(num+constant)))
print("Factorial of %r is %r"%((num*2),fatorial(num*2)))
num ="3.14"
print("Factorial of %r is %r"%((num),fatorial(num)))
num =3/4
print("Factorial of %r is %r"%((num),fatorial(num)))
print("Factorial of %r is %r"%((num+constant),fatorial(num+constant)))
print("Factorial of %r is %r"%((num*2),fatorial(num*2)))
num =('a')
print("Factorial of %r is %r"%((num),fatorial(num)))