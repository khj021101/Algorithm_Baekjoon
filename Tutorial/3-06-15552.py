#input 대신 sys.stdin.readline().rstrip() 으로 받는게 더 빠르다.
import sys
repeat = int(input())
for i in range(repeat):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(a + b)