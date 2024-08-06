answer = [1, 1, 2, 2, 2, 8]
pieces = list(map(int, input().split()))
diff = list(answer[i]-pieces[i] for i in range(6))
print(*diff)