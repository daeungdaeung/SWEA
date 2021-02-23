test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
test[::2] = [0, 0, 0, 0, 0]
print(test)

primes = list(range(3163))
print(primes)
for i in range(2, 3163):
    if primes[i]:
        primes[i*i::i] = [0] * len(primes[i*i::i])
print(primes)
