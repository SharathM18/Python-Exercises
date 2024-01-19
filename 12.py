#Palindrome Count in Array

def count_palindrome(array):
    count = 0
    for j in array:
        if j == j[::-1]:
            count = count + 1
    return count
         
arr = []
arr_size = int(input("Enter the size of the array: "))
for i in range(1, arr_size+1):
    ele = input(f"Enter element at index {i}: ")
    arr.append(ele)

print(f"Count of the palindromes in the given array is {count_palindrome(arr)}")



