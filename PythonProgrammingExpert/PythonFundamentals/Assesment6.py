"""
    Write a function that accepts a dictonary called
    frequencies and two strings named string1 and
    string2. The frequencies dictionary contains
    character keys and integer values, the value associated with each character
    represents its frequency. Your function should return 0,
    1 or 2 according to the cases below.

    Your function should return 2 if the frequency of characters
    in the dictionary is sufficient to create both string1 and
    string2 without reusing any characters.
    Your function should return 1 if the frequency of characters
    in the dictionary is sufficient to create either string1 or
    string2 without reusing any characters.
    Your function should return 0 if the frequency of characters
    in the dictionary is <b>not</b> sufficient to create either
    string1 or string2 without reusing any
    characters.
"""

def create_strings_from_characters(frequencies, string1, string2):
    first_string = created_from_freq(frequencies, string1)
    print(first_string)
    second_string = created_from_freq(frequencies, string2)
    print(second_string)

    if (not first_string) or (not second_string):
        if (not first_string) and (not second_string):
            return 0
        return 1

    for char in string1+string2:
        if frequencies[char] == 0:
            return 1
        frequencies[char] = frequencies[char] - 1
        # if frequencies[char] 


    return 2

def created_from_freq(frequencies, string_check):
    for char in set(string_check):
        if string_check.count(char) > frequencies.get(char, 0):
            return False
    return True

frequencies = {"h": 2, "e": 1, "l": 2, "r": 4, "a": 3, "o": 2, "d": 1, "w": 1}
string1 = "helloooo"
string2 = "world"
print(create_strings_from_characters(frequencies, string1, string2))
# expected = 2

# frequencies = {"h": 2, "e": 1, "l": 2, "r": 4, "a": 3, "o": 2, "d": 1, "w": 1}
# string1 = "hello"
# string2 = "world"


# expected = 1

