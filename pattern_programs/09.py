# Hourglass Pattern

rows = 5 
for i in range(rows):
    for j in range(i):
        print(" ", end = " ")
    for k in range(rows - i):
        print("*", end = " ")
    for m in range(rows - (i + 1)):
        print("*", end = " ")
    print()

rows = 4
for i in range(rows):
    for j in range(rows - (i + 1)):
        print(" ", end = " ")
    for k in range(i + 2):
        print("*", end = " ")
    for m in range(i + 1):
        print("*", end = " ")
    print()

    