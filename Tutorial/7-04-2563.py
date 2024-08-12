matrix = list(list(0 for i in range(100)) for j in range(100))
sheet_num = int(input())
for i in range(sheet_num):
    hor, ver = map(int, input().split())
    for j in range(hor, hor + 10):
        for k in range(ver, ver + 10):
            matrix[j][k] = 1
area = 0
for i in range(100):
    for j in range(100):
        area += matrix[i][j]
print(area)