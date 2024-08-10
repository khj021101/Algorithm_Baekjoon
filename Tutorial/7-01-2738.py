row_num, col_num = map(int, input().split())
matrix_1 = []
matrix_2 = []
for i in range(row_num):
    input_list = list(map(int, input().split()))
    matrix_1.append(input_list)
for j in range(row_num):
    input_list = list(map(int, input().split()))
    matrix_2.append(input_list)
for i in range(row_num):
    new_list = list(matrix_1[i][j]+matrix_2[i][j] for j in range(col_num))
    print(*new_list)