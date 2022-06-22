#21June- Python Programming Fundamentals_3
#13) Tuples 14) For loops 

#################################TUPLES##################################
#Tuples are similar to lists, but are immutable(or unchangeable)
tuple_1 = (1, "Saba", "Ruhee")
print(tuple_1)
print(type(tuple_1))

#################################FOR LOOPS##################################
# Range

for i in range(2):
  print(i)
  
print("Range with start and end")
for i in range(2,4):
  print(i)

print("Range with step")
for i in range(3,8,2):
  print(i)

##FOR LIST
print("Access list: Iterating by index")
list_1= [1, "Saba Ruhee", "Jagirdar", 31, "July", 1995]
for idx in range(len(list_1)):
  print(list_1[idx])

print("Iterate directly through list items")
#only access to the element but not the index
list_2 = [2, "Sanjana", "Desai", 22, "January", 1994]
for element in list_2:
  print(element)

print("Enumerate: Access list using bot i.e, Index and element")
list_3 = [3, "Trupti", "Desai", 16, "December", 1994]
for i, element in enumerate(list_3):
  print(i, element)

##FOR TUPLE
print("Access tuple: Iterating by index")
tup_1 = (1, "Saba Ruhee", "Jagirdar", 31, "July", 1995)
for idx in range(len(tup_1)):
  print(idx)

print("Iterate directly through tuple items")
tup_2 = (2, "Sanjana", "Desai", 22, "January", 1994)
for element in tup_2:
  print(element)

print("Enumerate: Access tuple using bot i.e, Index and element")
list_3 = [3, "Trupti", "Desai", 16, "December", 1994]
for idx, element in enumerate(list_3):
  print(idx,element)

##FOR STRING
print("Access string using index:")
str_1 = "Saba"
for i in range(len(str_1)):
  print(str_1[i])

print("Access string using element:")
str_2 = "Sanjana"
for element in str_2:
  print(element)

print("Enumerate")
str_3 = "Trupti"
for idx, element in enumerate(str_3):
  print(idx, element)

## BREAK AND CONTINUE
#break- Breaks out of the FOR LOOP
#continue- Skips the current iteration and continues
list_5 = [1, 2, 3, 4 , 5, 6, 7, 8, 9, 10]
for element in list_5:
  if element == 2:
    continue
  print(element)
  if element == 5:
    break

## nested for loops
for i in range(2):
  print(i)
  list_6 = ["Zero", "One", "two"]
  for j in list_6:
    print(j) 

# Accessing nester for loops
list_7 = [[2,3], [1,2],[5,6,7],[9,10,11]]
for i in range(len(list_7)):
  interior_list = list_7[i]
  for j in range(len(interior_list)):
    print(interior_list[j])