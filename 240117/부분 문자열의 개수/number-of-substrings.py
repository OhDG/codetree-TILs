a = input()
b = input()

len_a = len(a)
len_b = len(b)
cnt = 0

for i in range(len_a):
    satisfied = True

    for j in range(len_b):    
        if i + j > len_a - 1:
            satisfied = False
            break
        if a[i+j] != b[j]:
            satisfied = False
    
    if satisfied:
            cnt += 1
        
print(cnt)