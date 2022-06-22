"""Use nested <span>for</span> loops to iterate through the provided list,
    which contains other lists, and print the respective sums of the inner
    lists, each on a separate line.
"""

lst = [[2, 3, 4], [-2, -4, 0], [1, 2], [1, 1, 1, 5, 6], [0, 9, 8, 7]]
for i in range(len(lst)):
    # print(lst[i])
    interior_list = lst[i]
    sum = 0
    for j in range(len(interior_list)):
        # print(j)
        sum = sum + interior_list[j]
    print(sum)

"""
    Use a single FOR loop to iterate through the provided list of
    numbers, and for each number, print the sum of the number and the one
    directly to its right. In other words, print
    <span>lst[i] + lst[i + 1]</span>.
    Since the last number in the list has no number to the right of it, you
    should simply skip it.
"""

lst2 = [-2, 0, 4, 5, 1, 2]
# output -2, 4, 9, 6, 3
for idx in range(len(lst2)-1):
    current_item = lst2[idx]
    next_item = lst2[idx + 1]
    result = current_item + next_item
    print(result)
