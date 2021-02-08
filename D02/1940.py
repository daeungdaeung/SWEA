# -*- coding: utf-8 -*-
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    v = 0
    l = 0
    for i in range(N):
        arr = list(map(int, input().split()))
        if arr[0] == 1:
            v += arr[1]
        elif arr[0] == 2:
            v -= arr[1]
            if v < 0:
                v = 0
        l += v
    print('#{} {}'.format(test_case, l))
