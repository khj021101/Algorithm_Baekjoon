repeat = int(input())
num_list = list(map(int, input().strip().split()))
target_num = int(input())
target_count = 0
for i in num_list:
    if i == target_num:
        target_count += 1
print(target_count)

