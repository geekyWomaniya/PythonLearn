#22June- Python Programming Fundamentals_5
#16) Slices 

#################################SLICES##################################
# slice1 = [0, 1, 2, 3, 4, 5, 6]

# print(slice1[::])
# print(slice1[::2])
# print(slice1[2:6])
# print(slice1[:5])
# print(slice1[2:])

# print(slice1[::-1])

"""
<p>
  Modify the w, x, y, and
  z variables such that the program outputs [8, 6, 4].
</p>
"""

w = 1 # <- Change this
x = 1 # <- Change this
y = 4  # <- Change this
z = -2  # <- Change this

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print("list: ", lst[-3:-8:-2])

first_slice = lst[::z]
second_slice = first_slice[:y]
third_slice = second_slice[x:]
last_slice = third_slice[::w]

# OR- 
# w = 2
# x = 2
# y = -3
# z = -1

print(first_slice)
print(second_slice)
print(third_slice)
print(last_slice)

