n = list(input())

for i in range(len(n)-1):
    k = int(input())
    if k > len(n)-1:
        n.pop(len(n)-1)
        for s in range(len(n)):
            print(n[s], end="")
        print()    
        continue
    n.pop(k)
    for m in range(len(n)):
        print(n[m], end="")
    print()