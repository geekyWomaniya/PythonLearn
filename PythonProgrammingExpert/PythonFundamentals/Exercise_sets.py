"""
<p>
  Write a program that continually asks the user to enter characters until the
  user enters a previously entered character or more than one character at a
  time. After, the program should print the number of unique characters that
  were entered.
</p>
"""
# characters = set()

# while True:
#     char = input("Enter a character: ")
#     if char in characters:
#         break
    
#     characters.add(char)
#     list_char = list(characters)

# print(list_char)
# print("Number of unique characters entered: ", len(characters))
# print(list_char)

# Q- Find sum of unique numbers

# x = {1, 2,1,1,1,2,2,3,4,5,4,6}
# y = list(set(x))
# print(y)
# print(type(y))
# sum = 0
# for i in range(len(y)):
#   sum = sum + y[i]
# print(sum)

# Q- Ask user to continuosly enter characters, until its repeated. And then print the number of unique chars
from operator import le


characters = set()
while True:
  char = input("Enter a character:")

  if char in characters:
    break
  elif len(char) > 1:
      break
  else:
    characters.add(char)
print("Number of unique characters entered:", len(characters))

