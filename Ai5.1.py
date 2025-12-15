# Write a python program to add two matrices

mat1 = []
mat2 = []
mat3 = []

r = int(input("Enter row size: "))
c = int(input("Enter column size: "))

# Input first matrix
print(f"Enter {r}x{c} first matrix elements:")
for i in range(r):
    a = []
    for j in range(c):
        a.append(int(input()))
    mat1.append(a)

# Input second matrix
print(f"Enter {r}x{c} second matrix elements:")
for i in range(r):
    a = []
    for j in range(c):
        a.append(int(input()))
    mat2.append(a)

# Addition of two matrices
for i in range(r):
    a = []
    for j in range(c):
        a.append(mat1[i][j] + mat2[i][j])
    mat3.append(a)

# Printing first matrix
print("Matrix 1:")
for i in range(r):
    for j in range(c):
        print(mat1[i][j], end=" ")
    print()

# Printing second matrix
print("Matrix 2:")
for i in range(r):
    for j in range(c):
        print(mat2[i][j], end=" ")
    print()

# Printing sum matrix
print("Sum of two matrices:")
for i in range(r):
    for j in range(c):
        print(mat3[i][j], end=" ")
    print()
  
