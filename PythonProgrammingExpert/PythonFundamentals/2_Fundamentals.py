#17June- Python Programming Fundamentals_2
#7) Type Conversions 8) Conditions 9) Compound Conditions
#10) Conditionals 11) Lists 12) Strings

#################################TYPE CONVERSIONS##################################
num1 = input("Enter the number:")
type(num1) #str
#input by default takes string, therefore explicitly convert it to int
n1 = int(num1)
type(n1) #int
  
bool_value = bool("Saba Ruhee")
print(bool_value) #True

int(10.8) #True

#################################CONDITIONS##################################

#################################Compound Conditions##################################

#################################Conditionals##################################

#################################Lists##################################
list1 = ["Saba", "Ruhee", "AyubKhan", "Jagirdar", "Saba"]
print(list1)
print("First name is:"+ list1[0])
print("Negative Index-", list1[-1])
print("Index of Saba-",list1.index("Saba"))
print("Number of times name appeared:", list1.count("Saba"))

#################################Strings##################################
# str1 = "algoexpert".upper().replace("o", "i").capitalize().lower().split("e")
str1 = "algoexpert".upper().replace("o", "i").capitalize().lower().split("e")
print("STR:",str1)
print("foo".join(str1))

str2 = "SABARUHEE"
res2 = str2.split("A")
print("After split:",res2)

num3 = input("Enter a number:")
if num3.isdigit():
    print("Yeah! Its a digit!")
else:
    print("Sorry! Its not a digit")

##FIND
first = input("Enter first word, and let see if it is present in second:")
second = input("Enter second word:")
if first.find(second) > -1:
    print("First word is present in second")
else:
    print("Sorry not present!!!")

##LEN
sentence = input("Enter a sentence: ").split(" ")
numberOfWords = len(sentence)
print(type(sentence))
fstring = f"There are {numberOfWords} words in this sentence"
print(fstring)

print("    *\n   ***\n  *****\n *******\n  *****\n   ***\n    *\n")





