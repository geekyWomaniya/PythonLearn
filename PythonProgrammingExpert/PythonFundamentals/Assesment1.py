"""
    NUMBER GUESSER
    Write a program that asks the user to enter two integers representing the
    start and the end of a range. The program should then generate a random
    number within this range (inclusively) and ask the user to guess numbers
    until they guess the randomly generated number. Once the user guesses the
    random number, the program should tell them how many attempts it took them
    to guess it.
    Your program needs to ensure that the range of numbers given is valid. For
    example, if the user enters a number for the end of the range that is less
    than the start of the range your program needs ask them to enter a valid
    number. Your program must also handle any other errors that might occur,
    like the user entering a string instead of an integer.
Sample:
Enter the start of the range: 1
Enter the end of the range: 5
Guess a number: 2
Guess a number: 3
You guessed the number in 2 attempts
"""

# from itertools import count
import random

startRange = input("Enter the start of the range: ")
while not startRange.isdigit():
    print("Please enter a valid number. ")
    startRange = input("Enter the start of the range: ")

endRange = input("Enter the end of the range: ")
while not endRange.isdigit():
    print("Please enter a valid number. ")
    endRange = input("Enter the End of the range: ")

if int(startRange) > int(endRange):
    print("Please enter a valid number. ")
    endRange = input("Enter the end of the range: ")
    while not endRange.isdigit():
        print("Please enter a valid number. ")
        endRange = input("Enter the End of the range: ")



randomInt = random.randint(int(startRange), int(endRange))
print(randomInt)
count = 0

while True:
    guess = input("Guess a number: ")
    while not guess.isdigit():
        print("Please enter a valid number. ")
        guess = input("Guess a number: ")
    count = count + 1
    if int(guess) == randomInt:
        print("You guessed the number in {0} attempts".format(count))
        break
    