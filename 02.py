#check whether the given string is pangram or not

def pangram(str):

    str = str.lower()

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    for i in alphabet:
        if i not in str:
            return False
        return True

str = input("Enter a String: ")

res = pangram(str)

if(res == True):
    print("The string is pangram. ")
else:
    print("The string is not a pangram. ")
