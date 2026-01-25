#025讲课后作业0
matrix = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12]]
i = len(matrix)
j = len(matrix[0])
Tmatrix = [0]*j
for a in range(j):
    Tmatrix[a] = [0]*i
    for b in range(i): 
        Tmatrix[a][b] = matrix[b][a]
print(Tmatrix)