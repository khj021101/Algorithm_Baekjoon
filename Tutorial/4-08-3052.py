ModList = []
NewList = []
for l in range(10):
    num = int(input())
    ModList.append(num%42)
for mod in ModList:
    if mod not in NewList:
        NewList.append(mod)
    else:
        continue
print(len(NewList))