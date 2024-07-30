a_input, b_input, c_input = input().split()
a, b, c = int(a_input), int(b_input), int(c_input)
diff_ab = 0 if a == b else 1
diff_bc = 0 if b == c else 1
diff_ca = 0 if c == a else 1
if(diff_ab + diff_bc + diff_ca == 0):
    print(10000 + 1000*a)
elif(diff_ab + diff_bc + diff_ca == 2):
    if(diff_ab == 0 or diff_bc == 0):
        print(1000 + 100*b)
    else:
        print(1000 + 100*a)
else:
    print(100*max(a, b, c))

