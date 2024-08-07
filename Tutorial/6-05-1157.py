alphabet_count = list(0 for i in range(26))
input_string = input()
upper_string = input_string.upper()
for i in range(len(upper_string)):
    code = ord(upper_string[i])
    alphabet_count[code-65] +=1
max_index = alphabet_count.index(max(alphabet_count))
def tied(alphabet_count):
    max_value = max(alphabet_count)
    if max_index == 25:
        return False
    elif max_value in alphabet_count[max_index+1:]:
        return True
    else:
        return False
if tied(alphabet_count):
    print("?")
else:
    print(chr(max_index + 65))
    

