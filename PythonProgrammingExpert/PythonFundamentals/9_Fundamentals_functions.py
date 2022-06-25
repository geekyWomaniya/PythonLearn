#24June- Python Programming Fundamentals_8
#19) Functions
from xml.sax.handler import property_lexical_handler


def add(x,y):
    return x+y

def return_multiple_values(x,y):
    return x+1, y+1

addition = add(3,4)
print(addition)

rmv = return_multiple_values(3,4)
print(rmv)

def new_range(start,stop):
    x = start
    while x < stop:
        print(x)
        x = x+1

new_range(stop =10, start=1)

"""
Q- From base string remove the characters that is present in char.
    Eg- base- "Saba"; char: "a"; o/p:"Sb"
"""
def remove_char(base,chars):
    new_string = base
    for char in chars:
        new_string = new_string.replace(char,"")
    return new_string

resultant = remove_char("Saba","a")
print("String after Removing character")
print(resultant)
print("\n")

"""
Q- Print the odd numbers in list
"""

def find_all_odds(list1):
    final_list = []
    for i in list1:
        if list1[i] % 2 == 1:
            final_list.append(list1[i])

    return final_list

result_list = []
# result_list = find_all_odds([1,2,3,4,5,6,5,5,3,2])
result_list = find_all_odds([-1,-3,1,3,1])
print("Odd number list:")
print(result_list)
print("\n")

"""
Q- Takes input as a list of strings, and outputs the length of each string
"""

def string_lengths(strings):
    
    string_length = []
    for element in strings:
        per_length = len(element)
        string_length.append(per_length)

    return string_length

strings = ["hello","this", "a", "beard", "orange", "blue"]
string_lengths_list = string_lengths(strings)
print("Length of string: ")
print(string_lengths_list)
print("\n")

"""
Q- Compare two lists and return the unique common elements present in both the lists
"""

def compare_lists(lst1=[], lst2=[]):
    lst1_set = set(lst1)
    lst2_set = set(lst2)
    set_intersection = lst1_set.intersection(lst2_set)

    return len(set_intersection)

result = compare_lists([1,2,3],[1,3,1])
# result = compare_lists([1,2,3])
# result = compare_lists([1,1,1])
print("Compare results:")
print(result)
print("\n")

"""
Q- Trim list- Take two parameters, based on the second parameter the elements in the first list would be trimmed
"""
def trim_list(lst, elements_to_trim):
    trimmed_list = []
    range_list = int(len(lst))-int(elements_to_trim)
    # print(range_list)

    for i in range(range_list):
        trimmed_list.append(lst[i])
        # trimmed_list[i] = lst[i]
    return trimmed_list

trimm = trim_list([1, 3, 34, "hi", "yes", True, 2.3], 3)
print("Trimmed list-")
print(trimm)
print("\n")

"""
Q- Running sums
"""
def running_sums(numbers):
    summation = []
    per_element = 0
    for element in numbers:
        per_element = per_element + element
        summation.append(per_element)
    return summation

sums = running_sums([5,4,2,1,5,6,4])
print("Running Sum")
print(sums)
print("\n")
