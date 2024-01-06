#Sort the words in a given string

def sortWords(str1):
    str1.sort()
    for i in str1:
        print(i, end = " ")

str1 = input("Enter a string: ").split()
sortWords(str1)