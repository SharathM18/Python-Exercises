# Multiplication table
def multiplacationTable(num):
    for i in range(1,11):
        print(f'{num} * {i} = {num * i}')

ip_num = int(input("enter the number: "))
multiplacationTable(ip_num)


# Fibonacci function
def fib(num):
    count = 1
    num1, num2 = 0, 1
    while (count <= num):
        print(num1)
        num3 = num1 + num2
        num1 = num2
        num2 = num3
        count +=1

ip_num = int(input("enter the number: "))
fib(ip_num)


# Count the number of string
def CountNum(str):
    count = 0
    for i in str:
        count += 1
    return count


ip_str = input('Enter the String: ')
print(CountNum(ip_str))

# Find out the duplicate character
def DuplicateCharacter(str):
    DuplicateChar = {}
    for i in str:
        if i not in DuplicateChar:
            DuplicateChar[i] = 1
        else:
            DuplicateChar[i] +=1
    return DuplicateChar

ip_str = input('Enter the String: ')
res = DuplicateCharacter(ip_str)

for key, val in res.items():
    if (val > 1):
        print(key)

# Find out given number in words
Number_dict = {
    1:' one',
    2:' two',
    3:' three',
    4:' four',
    5:' five',
    6:' six',
    7:' seven',
    8:' eight',
    9:' nine',
    10:' ten'
}

def NumberInWords(num):
    res = ''
    for i in num:
        if int(i) in Number_dict:
            res += Number_dict[int(i)]
    return res

ip_str = input('Enter the String: ')
print(NumberInWords(ip_str))

# Decimal to binary
def DecimalToBinary(num):
    if (num >= 1):
        DecimalToBinary(num // 2) # #the floor division // rounds the result down to the nearest whole number
        # ((((10 // 2) // 2) // 2) // 2) # execute in reverse order
        print(num % 2)

DecimalToBinary(10)

# Palindrome
def palindrome(num):
    if num == num[::-1]:
        res = 0
        for i in num:
            res += int(i)
        print(f' {res} palindrome')
    else:
        print('not palindrome')

ip_str = input('Enter the Number: ')
palindrome(ip_str)

# Prime Number
def PrimeNumber(num):
    if num == 1:
        print(f'{num} is not prime number')
    elif num > 1:
        for i in range(2, num):
            if (num % i  == 0):
                print(f'{num} is not a prime number')
                break
        else:
            print(f'{num} is a prime number')

PrimeNumber(7)

# Prime number with range
def PrimeNumber(StartRange,EndRange):
    for i in range(StartRange, EndRange + 1):
        if i == 1:
            pass
        else:
            for j in range(2, i):
                if(i % j == 0):
                    break
            else:
                print(i, end=" ")

StartRange = 1
EndRange = 100
PrimeNumber(StartRange,EndRange)

# Armstrong Number
def ArmstrongNumber(num):
    res = 0
    for i in num:
        res += int(i) ** 3

    if res == int(num):
        print(f'{num} is a armstrong number')
    else:
        print(f'{num} is not a armstrong number')

ArmstrongNumber('370')
0, 1, 153, 370, 371, 407

# Armstrong number with range
def ArmstrongNumber(StartRange, EndRange):
    for num in range(StartRange, EndRange + 1):
        res = 0
        num = str(num)
        for i in num:
            res += int(i) ** 3

        if res == int(num):
            print(num)

ArmstrongNumber(1,1000)

# Perfect Number
def PerfectNumber(num):
    res = 0
    for i in range(1, num):
        if num % i ==0:
            res += i

    if res == num:
        print(f'{num} is a perfect number')
    else:
        print(f'{num} is not a perfect number')

PerfectNumber(6)