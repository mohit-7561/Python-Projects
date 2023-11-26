A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

B = [
    [1, 0],
    [3, 0],
    [2, 8]
]

C = [
    [0, 0],
    [0, 0],
    [0, 0]
]
#3x3  3x2 ----------> 3x2
for i in range(0, len(C)): #number of rows in matrix A is equal to matrix C(result)
    for j in range(0, len(C[0])): #number of column in matrix B is equal to matrix C(result)
        for k in range(0, len(A[0])): #number of column in matrix A is equal to number of rows in matrix B
            C[i][j] += A[i][k] * B[k][j]

for row in C:
    print(row)