matrix = []
for i in range(9):
    matrix.append(list(map(int, input().split())))

max = 0
row, col = 0, 0
for i in range(9):
    for j in range(9):
        if matrix[i][j] > max:
            max = matrix[i][j]
            row, col = i, j
print(max)
print(row+1, col+1)