test_num = int(input())
for i in range(test_num):
    repeat, string = input().split()
    repeat_num = int(repeat)
    new_string = ""
    for j in string:
        new_string += repeat_num*j
    print(new_string)
