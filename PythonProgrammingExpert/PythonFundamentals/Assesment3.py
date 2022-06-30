# Sorting 
from audioop import reverse

"""
<p>
  Write a function that accepts a list of lists that contain the name, age and
  salary of specific employees and also accepts a string representing the key to
  sort employees by. Your function should return a new list that contains the
  lists representing each employee sorted in ascending order by the given key.
</p>
<p>
  The string parameter named sort_by will always be equal to one of
  the following values: "name", "age" or  "salary".
</p>
employees = 
[
  ["John", 33, 65000],
  ["Sarah", 24, 75000],
  ["Josie", 29, 100000],
  ["Jason", 26, 55000],
  ["Connor", 25, 110000]
]
sort_by = "age"
</pre>
"""

lst = [[1, 2], [3, 4], [6,4], [-9,-2], [-2, -9]]
lst.sort()
print(lst)

# Sorting elements based on second element
print("Sort based on second key- ")
def sort_secondindex(item):
    # print(item[1])
    return item[1]

lst_2 = [[1, 2], [3, 4], [6,4], [-9,-2], [-2, -9]]
lst_2.sort(key = sort_secondindex)
print(lst_2)

print("Sort based on random key- ")
def nameIndex(item0):
    return item0[0]
def ageIndex(item1):
    return item1[1]
def salaryIndex(item2):
    return item2[2]

def sort_employees(employees, sort_by):
    if(sort_by == "name"):
        employees.sort(key = nameIndex)
    elif(sort_by == "age"):
        employees.sort(key = ageIndex)
        print("Employess: ", employees)
    elif(sort_by == "salary"):
        employees.sort(key = salaryIndex)
    return employees

# def sort_employees(employees, sort_by):
#     sort_indices = ["name", "age", "salary"]
#     sort_index = sort_indices.index(sort_by)
#     # print("Sort Index- ", sort_index)
#     sorted_employees = sorted(employees, key=lambda x: x[sort_index])

#     return sorted_employees

employee_list = [  ["John", 33, 65000],  ["Sarah", 24, 75000],  ["Josie", 29, 100000],  ["Jason", 26, 55000],  ["Connor", 25, 110000]
]

sorted_list = sort_employees(employee_list , "salary")

print(sorted_list)