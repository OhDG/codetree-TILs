n = input().split()

a = ord(n[0])
b = ord(n[1])

if a > b:
    print(a+b, a-b)
else:
    print(a+b, b-a)