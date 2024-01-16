k = input().split()
arr = list(k[0])
for i in range(int(k[1])):
    m = input().split()

    if m[0] == '1':
        arr[int(m[1])-1], arr[int(m[2])-1] =  arr[int(m[2])-1], arr[int(m[1])-1]
    else:
        for x in range(len(arr)):
            if arr[x] == m[1]:
                arr[x] = m[2]


    for z in arr:
        print(z, end="")
    
    print()