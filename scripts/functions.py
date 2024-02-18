#! /usr/bin/python3

def equal_string(str1, str2):
    """
    A function that checks if strings are equal and returns a boolean.
    Inputs: two strings
    Outputs: boolean
    example: equal_string("rat", "bat")
    False
    """
    if str1 == str2:
        return True
    else:
        return False
def word_in_sent(word, sent):
    """
    A function that checks if a word is in a sentence.
    Inputs: a word and a sentence (string)
    Output: boolean
    example: word_in_sent("Hello", "Hello World")
    True
    """
    if word in sent:
        return True
    else:
        return False
def miles_to_km(miles):
    """
    a function that convers miles to kilometers
    Inputs: Miles as an int or float
    Output: kilometers as a float
    example: miles_to_km(100)
    """
    return miles * 1.6
print(equal_string("rat", "bat"))
print(word_in_sent("Hello", "Hello World"))
print(miles_to_km(100))
