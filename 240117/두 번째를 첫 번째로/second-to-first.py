n = list(input())

len_n = len(n)
first = n[0]
second = n[1]
for i in range(len_n):
    if n[i] == second:
        n[i] = first
    print(n[i], end="")