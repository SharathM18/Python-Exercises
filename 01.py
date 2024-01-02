#check whether the given string are anagram or not (e.g. listen == silent)

def anagram(str1,str2):

    str1 = str1.lower()
    str2 = str2.lower()

    if (len(str1) == len(str2)) and (sorted(str1) == sorted(str2)):
        return f"{str1} and {str2} are anagram."
    else:
       return f"{str1} and {str2} are not anagram."

str1 = input("Enter first string: ")
str2 = input("Enter Second string: ")
print(anagram(str1,str2))