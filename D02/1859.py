T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    num_days = int(input())
    prices = list(map(int, input().split(' ')))
    benefit = 0
    while prices:
        max_price = max(prices)
        max_idx = prices.index(max_price)
        for i in range(max_idx):
            benefit += max_price - prices[i]
        prices = prices[max_idx+1:]
    
    print('#{} {}'.format(test_case, benefit))

    # ///////////////////////////////////////////////////////////////////////////////////
