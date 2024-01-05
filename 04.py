#To remove a specific index character in a string.

def charRemove(str1, idx):
    res = ""
    for i in range(len(str1)):
        if i != idx:
            res += str1[i]
    return res

str1 = input("Enter a string: ")
idx = int(input("Enter the index a character to remove: "))
print(f"The original string: {str1}")

res = charRemove(str1, idx)

print(f"The string after removal of {idx} character: {res}")