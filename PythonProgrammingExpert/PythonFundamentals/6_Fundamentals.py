#22June- Python Programming Fundamentals_6
# 17) Dictionaries 18) Sets

#################################DICTIONARIES##################################
# Key value pair, with keys being immutable

dict_1 = {10: "Saba Ruhee", "Surname": "Jagirdar"}
print(dict_1[10])
print(dict_1["Surname"])

dict_2 = {1: "One", 2: "Two", 3:"Three", 4:"Four"}
del dict_2[3]
print(dict_2)

# To check if dictions contains the key
contains = 1 in dict_2
print(contains)

# To retrieve all the valus
valuess = dict_2.values()
print(valuess)

# To retrieve all the keys
keyss = dict_2.keys()
print(keyss)


items = dict_2.items()
#Into tuples
print(items)
print(type(items))

# Converts to list
items_list = list(dict_2)
print(items_list)
print(type(items_list))

# iterate Dictionary using for loop
# Dictory is unordered list

for key in dict_2:
  # Key and value
  print(key, dict_2[key])

####OR

for key, value in dict_2.items():
  print(key, value)

print(dict_2.get(4))
print(dict_2.get(5,8))

# If values doesn't exists then get returns the second statemenet
characters = {}
string = "hello world"
for char in string:
  characters[char] = characters.get(char, 0) + 1
print(characters)

# Count the number of letters using dictionary
counts = {}

while True:
  num = input("Enter a number, press q to quit: ")
  if num == "q":
    break
  else:
    num = int(num)
    counts[num] = counts.get(num, 0) + 1
print(counts)
  
