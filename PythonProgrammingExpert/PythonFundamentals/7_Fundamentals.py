#23June- Python Programming Fundamentals_7
#18) Sets

#sets- Unique elements; no duplicates. Almost similar to dictionary
x = {1, 2,1,1,1,2,2,2,1,"Hey"}

print(type(x))
print(x)

x.add(6)
x.remove(2)
print(x)
x.clear()
print(x)

# SET intersection and union
a = {1,2,3,4,5,6}
b = {1,3,6}
intersect = a.intersection(b)
union = a.union(b)
print(intersect)
print(union)

diff = a.difference(b) # a-b
print("Difference: ", diff)

# SUBSET and SUPERSET
x = a.issuperset(b) # a>=b
print(x)

print(set('hello world'))