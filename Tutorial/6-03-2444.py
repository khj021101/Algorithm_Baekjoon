num = int(input())
line_num = 2*num -1
for i in range(line_num):
    star_num = min(2*i+1, 2*(line_num-i-1)+1)
    print(" "*int((line_num - star_num)/2)+"*"*star_num)
