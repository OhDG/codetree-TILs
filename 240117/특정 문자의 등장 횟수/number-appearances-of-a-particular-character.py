n = input()

cnt1, cnt2 = 0, 0 

for i in range(len(n)-1):
    if n[i] == 'e' and n[i+1] == 'e':
        cnt1 += 1
    if n[i] == 'e' and n[i+1] == 'b':
        cnt2 += 1
    
print(cnt1, cnt2)