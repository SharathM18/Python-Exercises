#factorial of a given number using recursion

def fact(n):
    if n == 1:
        return n
    else:
        return n * fact(n - 1)

num = int(input("Enter a number: "))

if num == 0:
    print("The factorial of 0 is 1")
else:
    print(f"The factorial of {num} is {fact(num)}")