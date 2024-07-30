is_x_positive = 0
is_y_positive = 0
x = int(input())
y = int(input())
is_x_positive = 0 if x > 0 else 1
is_y_positive = 0 if y > 0 else 1
if(is_x_positive == 0 and is_y_positive == 0):
    print(1)
elif(is_x_positive == 1 and is_y_positive ==0):
    print(2)
elif(is_x_positive == 1 and is_y_positive == 1):
    print(3)
else:
    print(4)
