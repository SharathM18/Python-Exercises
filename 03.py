#Find the sum of two matrices

m1 = [[1,2,3],[4,6,7]]
m2 = [[2,3,4],[9,6,7]]

res = [[0,0,0],[0,0,0]]

for i in range(len(m1)):
    for j in range(len(m1[0])):
        res[i][j] = m1[i][j] + m2[i][j]

for k in res:
    print(k)