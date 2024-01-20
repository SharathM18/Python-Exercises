#Even-Odd Number Checker.

def Checker(num):
    if (num % 2) == 0:
       print(f"{num} is Even number.")
    else:
       print(f"{num} is Odd number.")
       
num = int(input("Enter a number: "))
Checker(num)