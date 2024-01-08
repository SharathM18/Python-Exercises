#program to print most repeated number in a given array

#input: 1,2,4,5,6,4,3,4,5
#output: 4 is repeated 3 times 

def mostRepeatedNumber(array):
    dict1 = {}
    for i in array:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1
            
    return dict1

array = input("Enter the numbers: ").split()
array = list(map(lambda a: int(a), array))
res = mostRepeatedNumber(array)

max_value = max(res.values())
for i,j in res.items():
    if j >= max_value:
        print(f"{i} is repeating {j} times")

