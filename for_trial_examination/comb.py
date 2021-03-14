def comb(l, r):
    for i in range(len(l)):
        if r == 1:
            yield [l[i]]

        else:
            for next in comb(l[i+1:], r-1):
                yield [l[i]] + next


print(list(comb([0, 1, 2, 3, 4], 3)))