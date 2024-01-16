#leap year

def leapyear(year):
    if year % 4 == 0:
        print(f"{year} is Leap year")
    elif year % 100 == 0:
        print(f"{year} is not Leap year")
    elif year % 400 == 0:
        print(f"{year} is Leap year")
    else:
        print(f"{year} is not Leap year")

year = int(input("Enter the year: "))
leapyear(year)