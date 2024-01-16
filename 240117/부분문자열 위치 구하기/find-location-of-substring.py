n = input()
k = input()
satisfied = False

for i in range(len(n)):
    for m in range(len(k)):
        if i + m > len(n) - 1:
            break
        if n[i+m] == k[m]:
            satisfied = True
        else:
            satisfied = False
    if satisfied:
        break

if satisfied:
    for i in range(len(n)):
        if n[i] == k[0]:
            print(i)
            break
else:
    print(-1)