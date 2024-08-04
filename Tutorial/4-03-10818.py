num = int(input())
num_list = list(map(int, input().strip().split()))
print("{} {}".format(min(num_list), max(num_list)))
