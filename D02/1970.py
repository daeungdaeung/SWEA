# -*- coding: utf-8 -*-
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    change_list = [0]*8
    money = int(input())
    while money >= 50000:
        money -= 50000
        change_list[0] += 1
    while money >= 10000:
        money -= 10000
        change_list[1] += 1
    while money >= 5000:
        money -= 5000
        change_list[2] += 1
    while money >= 1000:
        money -= 1000
        change_list[3] += 1
    while money >= 500:
        money -= 500
        change_list[4] += 1
    while money >= 100:
        money -= 100
        change_list[5] += 1
    while money >= 50:
        money -= 50
        change_list[6] += 1
    while money >= 10:
        money -= 10
        change_list[7] += 1
    result = ' '.join(list(map(str, change_list)))
    print('#{}\n{}'.format(test_case, result))
