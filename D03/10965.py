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
# """
# 에라토스테네스의 체에서 루트를 이용하여 소수가 될 수 있는 범위를 10^7 을 3162로 줄였고,
# 3162개의 숫자에서 소수가 아닌 수를 제거한 후, 446개의 소수를 구하였다.
# 10^7 보다 작거나 혹은 같은 값인데, 446개의 소수로 나누어지지 않는 값이라면, 소수이다.
# """

T = int(input())
# 출력해야할 모든 문자열들을 ans에 저장하고, 한번에 출력
ans = []
for test_case in range(1, T + 1):
    A = int(input())
    result = 1
    # 완전 제곱수가 아닌경우
    if A ** 0.5 != int(A ** 0.5):
        # 소수로 주어진 수를 나누어 볼것
        for prime in primes:
            # 각 소수가 몇번 쓰였는지 확인
            tmp = 0
            # 주어진 소수로 나눌수 없거나, 주어진 수가 2보다 작 경우 while문 탈출
            # 위 문장의 의미 -> 주어진 A는 primes 안에 속하는 소수로 표현 가능하다는 의미
            while A % prime == 0:
                # // 연산자를 사용 -> 몫을 활용하는 것
                # / 연산자 사용 -> 나눗셈 활용시 정수형을 실수형으로 변환한다.
                A //= prime
                tmp += 1
            if tmp % 2 == 1:
                result *= prime
            if A < 2 or A < prime:
                break
        if A > 1:
            result *= A
        # primes에 속하는 소수로 더이상 나누어지지 않는다면 그(A) 또한 소수이다.
        # (A가 primes에 속하는 소수로 표현이 된다면 A => 1 이다. 아래 적힌 코드의 당위성 설명)

    ans.append('#{} {}'.format(test_case, int(result)))
for _ in ans:
    print(_)
