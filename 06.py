#program to find longest palindrome within a given sentence.

#example: Nonviolent civic protests were taking place during noon
#output: civic

def largestPalindrome(str1):
    word = ""
    for i in str1:
        i = i.lower()
        if i == i[::-1] and len(i) > len(word):
            word = i 
    
    return word
str1 = input("Enter a string: ").split()
res = largestPalindrome(str1)
print(res)
