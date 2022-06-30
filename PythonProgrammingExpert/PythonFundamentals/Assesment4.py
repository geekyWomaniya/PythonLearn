"""
<p>
    Write a function that accepts a list of strings that represent words and a
    positive integer <span>n</span>, representing the number of words to return.
    Your function should return a new list containing the <span>n</span> longest
    unique words from the input list. Words are unique if they only appear one
    time in the input list.
</p>
<p>
    There will always be exactly <span>n</span> words to return and you may
    return the words in any order.
</p>
"""

def get_n_longest_unique_words(words, n):
    unique_words = []
    for word in words:
        if words.count(word) < 2:
            unique_words.append(word)
    unique_words.sort(key=len, reverse= True)
    n_unique_word = unique_words[:n]
    return n_unique_word
    # return unique_words

word_list = ["Hello",
            "AlgoExpert",
            "Algo",
            "Testing",
            "Programming",
            "Programming",
            "Coding",
            "Python",
            "JavaScript",
            "Coding",
            "Ruby",]
print(get_n_longest_unique_words(word_list, 5))
