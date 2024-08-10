matrix = []
for i in range(5):
    matrix.append(list("" for i in range(15)))
    input_line = input()
    for j in  range(len(input_line)):
        matrix[i][j] = input_line[j]
result = ""
for i in range(15):
    for j in range(5):
        result += matrix[j][i]
print(result)