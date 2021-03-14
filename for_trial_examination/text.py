a = 0
b = 1
c = -1
print(a)
print(-a)
print(b)
print(-b)
print(c)
print(-c)

import copy
def f(brd):
    brd[0][0] = 0
    brd[1][1] = 0

    return brd




brd = [
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
]

new_brd = f(copy.deepcopy(brd))

print(brd)
print(new_brd)