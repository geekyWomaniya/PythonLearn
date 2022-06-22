input_word = input("Enter a word: ")
word_length = len(input_word)
count = 1
if input_word == "q" and input_word == "quit":
    quit()
while True:
    if input_word=="q" or input_word=="quit":
        break
    else:
        input_word = input("Enter a word: ")
        if not input_word=="q" and not input_word=="quit":
            word_length = word_length + len(input_word)
            count = count + 1
            average_word_length = word_length / count
            print("The average word length is: {0}".format(average_word_length))