input_num = int(input())
def is_group(word):
    shrunk_string = ""
    alphabet_count = list(0 for i in range(26))
    for i in range(len(word)):
        if len(shrunk_string) != 0 and shrunk_string[len(shrunk_string)-1] == word[i]:
            continue
        else:
            shrunk_string += word[i]
    for j in range(len(shrunk_string)):
        ascii_code = ord(shrunk_string[j])
        alphabet_count[ascii_code-97] += 1
    for k in alphabet_count:
        if k>=2:
            return False
        else:
            continue
    return True
group_count = 0
for i in range(input_num):
    input_string = input()
    if is_group(input_string):
        group_count += 1
print(group_count)