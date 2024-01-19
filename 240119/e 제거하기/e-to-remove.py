a = input()
new_a = ""
for i in range(len(a)):
    if a[i] == 'e':
        new_a += a[:i] + a[i+1:]       
    break

print(new_a)