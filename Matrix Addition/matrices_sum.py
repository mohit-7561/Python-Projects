def matrix(r, c):
    o = []
    for i in range(r):
        row = []
        for j in range(c):
            user = int(input(f"Enter the elemnts at rows [{i}] and column [{j}]"))
            row.append(user)
        o.append(row)
    return o

def sum(A, B):
    output = []
    for i in range(len(A)): #number of rows
        row = []
        for j in range(len(A[0])): #number of columns
            row.append(A[i][j] + B[i][j])
        output.append(row)
    return output


r = int(input("Enter the rows: "))
c = int(input("Enter the column: "))
print("Enter the Matrix A")
A = matrix(r, c)
print(A)

print("Enter Matrix B")
B = matrix(r, c)
print(B)

print("The sum of two Matrices are:")
s = sum(A, B)
print(s)

