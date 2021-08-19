#create a string with four unfilled variable spaces
formatter = "{} {} {} {}"

#refer to the formatter variable and use ".format" function in string to generate string (fill the unfilled {}) with the given parameter
#in this case, 1,2,3, and 4
print(formatter.format(1, 2, 3, 4))
#refer to the formatter, generate (call function .format),results "one two three four" with four given strings
print(formatter.format("one", "two", "three", "four"))
#refer to the formatter, generate (call function .format),results "True False False True" with four given booleans
print(formatter.format(True, False, False, True))
#refer to the formatter, generate (call function .format),results "{} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {}" with four given strings, which are all "{} {} {} {}"
print(formatter.format(formatter, formatter, formatter, formatter))
#refer to the formatter, generate (call function .format),results "Try your Own text here Maybe a poem Or a song about fear" with the four strings
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))