#check whether a given number is a prime number

def primeNumber(num):
    if (num <= 1):
        print(f"{num} is not a prime number")
    else:
        for i in range(2, num):
            if(num % i) == 0:
                print(f"{num} is not a prime number")
                break
        else:
            print(f"{num} is a prime number")
            
ip_num = int(input("Enter the number: "))
primeNumber(ip_num)