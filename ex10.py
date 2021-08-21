tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
blackslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Capnip\n\t* Grass
'''

print(tabby_cat)
print(persian_cat)
print (blackslash_cat)
print (fat_cat)

for i in ["/","-","|","\\","|"]:
    print("%r\r"%i)

#Both triple "" and '' represent multiple lines string, but when the text itself has "" using triple '' would be more clear

#Using %r print in the way we write in code, while %s take each i as indivisual string
#So, "\\" displays as \ only in the terminal
