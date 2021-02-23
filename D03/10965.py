# -*- coding: utf-8 -*-
# Sieve of Eratosthenes 를 활용
# int((10000000)**(0.5)) => 3162
# 약수를 구해보자
primes = list(range(0, 3162+1))
primes[1] = 0
for i in primes:
    if primes[i] != 0:
        # 2의 배수 모두 제거, 3의 배수 모두제거, 5의 배수 모두 제거...(계속 수행)
        primes[i*i::i] = [0] * len(primes[i*i::i])
# filter function은 첫번째 인자가 None이면 identity function으로 간주된다.
# 즉, 데이터 값이 False가 아닌경우만 값이 담겨질 것이다.
primes = list(filter(None, primes))
"""
에라토스테네스의 체에서 루트를 이용하여 소수가 될 수 있는 범위를 10^7 을 3162로 줄였고,
3162개의 숫자에서 소수가 아닌 수를 제거한 후, 446개의 소수를 구하였다.  
"""

T = int(input())
# 출력해야할 모든 문자열들을 ans에 저장하고, 한번에 출력
ans = []
for test_case in range(1, T + 1):
    A = int(input())
    sqr_A = A**0.5
    result = 1
    # 소수로 주어진 수를 나누어 볼것
    for prime in primes:
        # 각 소수가 몇번 쓰였는지 확인
        tmp = 0
        # 주어진 소수로 나눌수 없거나, 주어진 수가 2보다 작 경우 while문 탈출
        while A % prime == 0 and A >= 2:
            A /= prime
            tmp += 1
        if tmp % 2 == 1:
            result *= prime
        # A < 2 -> 이때까지 나왔던 소수들을 활용하여 모두 나눌 수 있다는 의미이므로
        # 뒤에 남아있는 소수는 신경쓸 필요 없다.
        if A < 2:
            break
        # 우리가 가지고 있는 가장 큰 소수보다 크고, 또한 우리가 가지고 있는 모든 소수로 더이상 나누어지지 않는다면 그(A) 또한 소수이다.
        # 그러므로 A > 3137 인 경우는 소수를 곱해서 반복문을 탈출한다.
        if prime == primes[-1]:
            if A > prime:
                result *= A
                break

    ans.append('#{} {}'.format(test_case, int(result)))
print(*ans, sep='\n')
