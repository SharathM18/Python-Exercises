#Full Pyramid Pattern

rows = 5
for i in range(rows):
    for j in range(rows - i):
        print(" ", end = " ")
    for k in range(i + 1):
        print("*", end = " ")
    for m in range(i):
        print("*", end = " ")
    print()