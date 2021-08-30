def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(" ")
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first wrd after popping it off."""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Prints the last wrd after popping it off."""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

"""
Study Drill:
- 1
lines 23-26: we do the same for sorted_words, making it print the first then the last words in sorted_words list
lines 27-28: tell the termial to print the list sorted_words, which "All" and "who" are not inside because we printed them out
lines 29-31: Reset sorted_words by recalling sort_sentence(sentence) and print sorted_words out. sorted_words is back to the list with "All" and "who"
lines 32-34: Call print_first_and_last() function, which break the setnece and print the 1st and last words of the sentence, with the parameter sentence
lines 35-37: Call print_first_and_last_sorted() function, which break the setnece and print the 1st and last words in the sorted words order, with the parameter sentence
-2
help(ex25) display all functions and their documentation comments
"""