# -*- coding: utf-8 -*-
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    num_list = list(map(int, input().split()))
    max_num = max(num_list)
    min_num = min(num_list)

    avg = round((sum(num_list) - max_num - min_num)/(len(num_list) - 2))

    print('#{} {}'.format(test_case, avg))
    # ///////////////////////////////////////////////////////////////////////////////////