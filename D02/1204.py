# -*- coding: utf-8 -*-
import operator
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    dic = {}
    test_case = int(input())
    arr = list(map(int, input().split()))
    while arr:
        num = arr.pop()
        dic[num] = dic.get(num, 0) + 1

    sorted_list = sorted(dic.items(), key=operator.itemgetter(1, 0), reverse=True)
    result = sorted_list[0][0]
    print('#{} {}'.format(test_case, result))