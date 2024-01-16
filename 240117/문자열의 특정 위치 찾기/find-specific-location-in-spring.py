n = input().split()
satisfied = False
for i in range(len(n[0])):
    if n[0][i] == n[1]:
        print(i)
        satisfied = True
        break

if not satisfied:
    print("No")