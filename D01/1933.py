N = int(input())

s = ''
for i in range(1, N+1):
    if N % i == 0:
        s += str(i) + ' '

print(s)
