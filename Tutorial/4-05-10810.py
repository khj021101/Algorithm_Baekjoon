n, m = map(int, input().split())
basket = list(0 for i in range(n))
for a in range(m):
    i, j, k = map(int, input().split())
    for l in range(i-1, j):
        basket[l] = k
print(*basket)
