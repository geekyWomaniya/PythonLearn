"""
<p>
    Write a function named  replace that takes in three parameters:
    lst  (a list of strings),  target  (a string), and
     swap_value  (another string).
    Your function should replace all instances of  target in
     lst with  swap_value, and it shoudn't return
    anything; in other words, your function should mutate the input list.
</p>
"""

def replace(lst, target, swap_value):
    for idx in range(len(lst)):
        if lst[idx] == target:
            lst[idx] = swap_value
    return lst

lst = ["tim", "is", "great", "is", "is", "yes", "no", "blue", "no"]
replace(lst, "is", "the")
print(lst)
# ["tim", "the", "great", "the", "the", "yes", "no", "blue", "no"]