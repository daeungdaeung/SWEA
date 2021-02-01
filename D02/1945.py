# -*- coding: utf-8 -*-
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    num_list = [2, 3, 5, 7, 11]
    result = []
    # 몫과 나머지로 접근하려함
    for num in num_list:
        q, r = 0, 0
        tmp = N
        power = 0
        while not r:
            q, r = divmod(tmp, num)
            tmp = q
            power += 1
        result.append(power-1)
    print('#{} {}'.format(test_case, ' '.join(map(str, result))))
