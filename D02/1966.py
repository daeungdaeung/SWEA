# -*- coding: utf-8 -*-
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = input()
    numbers = sorted(list(map(int, input().split())))
    numbers = ' '.join(list(map(str, numbers)))

    print('#{} {}'.format(test_case, numbers))

