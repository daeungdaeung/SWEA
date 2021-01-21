A, B = input().split()

if A == '1':
    if B == '2':
        winner = 'B'
    else:
        winner = 'A'
elif A == '2':
    if B == '3':
        winner = 'B'
    else:
        winner = 'A'
else:
    if B == '1':
        winner = 'B'
    else:
        winner = 'A'

print(winner)