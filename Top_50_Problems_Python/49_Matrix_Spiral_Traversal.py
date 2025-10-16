rows, cols = list(map(int, (input('Enter the size of matrix (rows, col): ').split())))

matrix = []

for row in range(rows):
    matrix.append(list(map(int, input('').split())))

final = []

left = 0
right = cols - 1
top = 0
bottom = rows - 1

while(left<= right and top<=bottom):
    # top
    for i in range(left, right+1):
        final.append(matrix[top][i])
    top += 1

    # right
    for i in range(top, bottom+1):
        final.append(matrix[i][right])
    right -= 1

    # bottom
    for i in range(right, left-1, -1):
        final.append(matrix[bottom][i])
    bottom -= 1

    # left
    for i in range(bottom, top-1, -1):
        final.append(matrix[i][left])
    left += 1


print(final)