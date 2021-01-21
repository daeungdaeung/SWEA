num = int(input())

s = '1 '
for i in range(1, num+1):
    s += str(2**i) + ' '

print(s)