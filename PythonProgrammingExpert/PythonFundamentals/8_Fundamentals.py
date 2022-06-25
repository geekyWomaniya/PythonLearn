#24June- Python Programming Fundamentals_8
#19) Exceptions

# try:
#     # int("Hello")
#     x={1,2,3}
#     x[2] =3
    
# except Exception as e:
#     print("Exception!!!",e)
# finally:
#     x={1,2,3}

# print(x)

"""
Q-Write a program that asks a user for two numbers: a numerator and a
  denominator. Your program should divide the numerator by the denominator and
  handle any exceptions that might occur during the division.

  Specifically, your program should catch exceptions when either the numerator
  or the denominator isn't a number and when the denominator is
  0 (you can't divide by 0). All exceptions should
  be caught and handled, even when there are multiple.

  If the division doesn't raise any exceptions, the program should print the
  result of the division. And regardless of outcome, the program should tell
  the user goodbye!
"""
numerator = input("Enter the numeratorr: ")
denominator = input("Enter the denominator: ")

try:
    numerator = float(numerator)
except:
    print("The numerator is not a number.")

try:
    denominator = float(denominator)
except:
    print("The denominator is not a number")

try:
    res = numerator/denominator
    print("The result of this division is")
    print(res)
except ZeroDivisionError as e:
    print(e)
    print("You cannot divide by 0.")
    print("This division cannot be performed.")
except Exception as e:
    print("This division cannot be performed.")
finally:
    print("Goodbye!")


