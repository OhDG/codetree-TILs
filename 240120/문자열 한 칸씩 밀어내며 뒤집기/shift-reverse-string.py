n = input().split()
len_n = len(n[0])
for i in range(int(n[1])):
    k = int(input())
    new_n = ""
    if k == 1:
        n[0] = n[0][1:] + n[0][0]
        print(n[0])
    elif k == 2:
        n[0] = n[0][-1] + n[0][:-1]
        print(n[0])
    elif k == 3:
        for m in range(len_n):
            new_n += n[0][-(m+1)]
        n[0] = new_n
        print(n[0])