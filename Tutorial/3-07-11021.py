import sys
repeat = int(input())
for i in range(repeat):
    a, b = map(int, sys.stdin.readline().strip().split())
    print("Case #{}: {}".format(i+1, a + b))

