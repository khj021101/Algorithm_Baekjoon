num_list = [2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 9, 9, 9, 9]
word = input()
total_time = 0
for i in word:
    num = num_list[ord(i)-65]
    timedelta = num + 1
    total_time += timedelta
print(total_time)