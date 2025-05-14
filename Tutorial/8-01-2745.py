n, b = input().split()
digit= int(b)
result = 0
for i in range(len(n)):
    asc = ord(n[i])
    if(asc in range(48, 57)):
        result += int(n[i])*(digit**(len(n)-1-i))
    else:
        result += (asc-55)*(digit**(len(n)-1-i))
print(result)