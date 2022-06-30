# PAIRS SUM TO TARGET
"""
<p>
  Write a function that accepts two lists (list1 and
  list2) of integers and a target integer named
  target. Your function should return all pairs of indices in the
  form [x, y] where list1[x] + list2[y] == target. In
  other words, return the pairs of indices where the sum of their values equals
  target.
</p>
"""

from unittest import result


def pairs_sum_to_target(list1, list2, target):
    # Write your code here.
    resultant_list = []

    for i in range(len(list1)):
        for j in range(len(list2)):
            sum = list1[i] + list2[j]
            if sum == target:
                resultant_list.append([i,j])
    return resultant_list

list1 = [1, 2, 3, 4, 5, 6]
list2 = [6, 5, 4, 3, 2, 1]
target = 7

print(pairs_sum_to_target(list1, list2, target))