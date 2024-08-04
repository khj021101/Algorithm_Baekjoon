checklist = list(0 for i in range(30))
for i in range(28):
    num = int(input())
    checklist[num-1] = 1
for j in range(len(checklist)):
    if checklist[j] == 0:
        print(j+1)
