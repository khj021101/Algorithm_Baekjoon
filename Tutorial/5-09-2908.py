a, b = input().split()
a, b = int("".join(reversed(a))), int("".join(reversed(b)))
print(a if a>b else b)
