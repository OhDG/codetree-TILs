n = list(input())

n[1] = 'a'
n[len(n)-1-1] = 'a'

for i in n:
    print(i, end="")