input_string = input()
reversed_string = "".join(reversed(input_string))
for i in range(len(input_string)):
    if(input_string[i] != reversed_string[i]):
        print(0)
        break
    if(i == len(input_string)-1):
        print(1)