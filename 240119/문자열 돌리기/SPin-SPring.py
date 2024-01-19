a = input()
len_a = len(a)
print(a)
for i in range(1, len_a):
    new_a = a[-i:] + a[:len_a-i]
    print(new_a)

print(a)