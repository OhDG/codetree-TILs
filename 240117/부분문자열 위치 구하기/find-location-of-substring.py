n = input()
k = input()
satisfied = False

for i in range(len(n)):
    for m in range(len(k)):
        if i + m > len(n) - 1:
            satisfied = False
            break
        if n[i+m] == k[m]:
            satisfied = True
        else:
            satisfied = False
            break
    if satisfied:
        print(i)
        break

if not satisfied:
    print(-1)