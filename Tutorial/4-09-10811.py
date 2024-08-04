n, m = map(int, input().split())
basket = list(i+1 for i in range(n))
for l in range(m):
    i, j = map(int, input().split())
    TempList = []
    for k in range(j-i+1):
        TempList.append(basket[i-1+k])
    TempList.reverse()
    for k in range(j-i+1):
        basket[i-1+k] = TempList[k]
print(*basket)
