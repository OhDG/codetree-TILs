a = list(input())
b = list(input())
while True:
    satisfied = False
    for i in range(len(a)):
        for j in range(len(b)):
            if i+j > len(a)-1:
                satisfied = False
                break
            if a[i+j] == b[j]:
                satisfied = True
            else:
                satisfied = False
    
        if satisfied:
            for m in range(len(b)):
                a.pop(i)
            break
    if not satisfied:
        break
    
for s in a:
    print(s, end="")