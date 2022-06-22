#21June- Python Programming Fundamentals_3
#15) While loops
#16) Slices 17) Dictionaries 18) Sets

#################################While LOOPS##################################
# Anything that can be done by for loops can be done by while loop
# If number of iterations are unknown then its always better to use while loops
"""
num = input("Enter an integer: ")
while not num.isdigit():
    num = input("Please Enter an integer: ")

print("Enetered digit is",num)
"""


"""
<p>
    Write a program that continually asks the user to enter a number until they
    enter the number 5, at which point the program should print how many numbers
    the user has entered.
</p>
"""
"""
num_1 =int(input("Enter a number: "))
i = 1
while not num_1 == 5:
    num_1 = int(input("Enter a number::"))
    i = i + 1
    if num_1 == 5:
        break

print("You entered {0} numbers".format(i))
# print("You entered %d numbers",i)
"""

"""
<p>
    Write a program that continually asks the user to enter a word until they
    enter the word  "q"  or  "quit" , at which point the
    program should print the average length of all of the entered words,
    excluding the  "q"  or  "quit" .
    If the user doesn't enter any words (i.e., immediately enters
     "q"  or  "quit" ), your program shouldn't print
    anything.
</p>
"""

# input_word = input("Enter a word: ")
# word_length = len(input_word)
# count = 1
# if input_word == "q" and input_word == "quit":
#     exit()
# while True:
#     if input_word=="q" or input_word=="quit":
#         break
#     else:
#         input_word = input("Enter a word: ")
#         if not input_word=="q" and not input_word=="quit":
#             word_length = word_length + len(input_word)
#             count = count + 1
#             average_word_length = word_length / count
#             print("The average word length is: {0}".format(average_word_length))    
"""
words = []
while True:
    word = input("Enter a word: ")
    if word == "q" or word == "quit":
        break
    else:
        words.append(word)
# print(words)---['qqq', 'qqqqqq']
# print(len(words)) -- 2

if len(words) > 0:
    sum_word_length= 0
    for element in words:
        sum_word_length = sum_word_length + len(element)
        
    # print("Sum of word length",sum_word_length)
    average_length = sum_word_length / len(words)
    print("The average word length is: {0}".format(average_length))

"""

"""
<p>
    Use a while loop to print the squares of the numbers:
    1, 3, 6, 10, 15 and 21.
</p>
"""
list_3 = [1, 3, 6, 10, 15, 21]
idx = 0

while idx < len(list_3):
    for element in list_3:
        square = element * element
        print(square)
        idx = idx + 1
    
    
