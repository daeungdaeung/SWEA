# -*- coding: utf-8 -*-
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    result = []
    temp = []
    for i in range(N):
        char, num = input().split()
        num = int(num)

        for j in range(num):
            temp.append(char)
            if len(temp) >= 10:
                result.append(temp)
                temp = []
    result.append(temp)

    print('#{}'.format(test_case))
    for i in range(len(result)):
        print(''.join(result[i]))
