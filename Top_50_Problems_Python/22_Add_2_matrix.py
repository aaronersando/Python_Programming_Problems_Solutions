

mcols = int(input('Enter matrix col size: '))
mrows = int(input('Enter matrix row size: '))

matrix1 = []

print("Enter nums in rows for matrix 1: ")
for i in range(mrows):
    row = list(map(int, input("").split()))
    matrix1.append(row)

matrix2 = []

print("Enter nums in rows for matrix 2: ")
for i in range(mrows):
    row = list(map(int, input("").split()))
    matrix2.append(row)

finalMatrix = []
for i in range(mrows):
    init = []
    for j in range(mcols):
        total = matrix1[i][j] + matrix2[i][j]
        init.append(total)
    finalMatrix.append(init)

print(finalMatrix)


    