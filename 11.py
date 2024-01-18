#program to check if a string is a palindrome or not.

def ispalindrome(string):
    reversed_string = string[::-1]
    return string == reversed_string

word = input("Enter the string: ")

if ispalindrome(word):
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")