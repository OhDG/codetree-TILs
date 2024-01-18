n = input()
len_n= len(n)
result = n[:1] + n[2:len_n-2] + n[len_n-1:]

print(result)