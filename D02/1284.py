# -*- coding: utf-8 -*-
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())
    A_price = P * W
    B_price = 0
    if R >= W:
        B_price = Q
    else:
        B_price = Q + (W - R)*S
    result = min(A_price, B_price)

    print('#{} {}'.format(test_case, result))