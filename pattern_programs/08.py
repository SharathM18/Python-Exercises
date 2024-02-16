# Rhombus Pattern

rows = 5 
for i in range(rows):
    for j in range(i):
        print(" ", end = " ")
    for k in range(rows):
        print("*", end = " ")
    print()