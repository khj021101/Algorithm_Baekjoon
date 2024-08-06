input_string = input()
alphabet_list = list(-1 for i in range(26))
for i in range(97, 123):
    try:
        alphabet_list[i-97] = input_string.index(chr(i))
    except:
        continue
result = ""
for j in range(len(alphabet_list)):
    result = result + str(alphabet_list[j])
    if j == len(alphabet_list)-1:
        break
    result += " "
print(result)