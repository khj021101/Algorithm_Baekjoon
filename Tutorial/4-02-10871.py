n, x = map(int, input().split())
num_list = list(map(int, input().split()))
new_list = []
for i in num_list:
    if i<x:
        new_list.append(i)
print(*new_list)