# <p>
#     Write a program that asks the user to enter a string and prints the string's
#     characters and their frequencies in any order and in the following format:
#     <span>key: frequency</span>.
# </p>
counts = {}
string = input("Enter a string: ")

for char in string:
    counts[char] = counts.get(char,0) + 1
print(counts)
for key, value in counts.items():
    print(key,": ",value)