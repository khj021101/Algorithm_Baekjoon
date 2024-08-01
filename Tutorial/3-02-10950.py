repeat = int(input())
result = ""
for i in range(repeat):
    a, b = input().split()
    a_num, b_num = int(a), int(b)
    result += "{}\n".format(a_num + b_num)
print(result)