def dp(n):
    if n <= 2:
        storage[n] = min(prices[1], prices[0] * plan[n])
        return storage[n]

    return storage[n] + min(prices[1], prices[0] * plan[n])

T = int(input())

for tc in range(1, T+1):
    prices = list(map(int, input().split()))
    plan = [0] + list(map(int, input().split()))

    storage = [0] * 13  # 12달 인덱스를 편하게 사용하기 위해서
