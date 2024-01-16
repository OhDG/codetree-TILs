n = list(input())

first = n[0]
second = n[1]

for i in range(len(n)):
    if n[i] == first:
        n[i] = second
    elif n[i] == second:
        n[i] = first
    print(n[i], end="")