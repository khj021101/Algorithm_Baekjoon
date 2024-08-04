n, m = map(int, input().split())
basket = list(i+1 for i in range(n))
for l in range(m):
    i, j = map(int, input().split())
    basket[i-1], basket[j-1] = basket[j-1], basket[i-1]
print(*basket)
