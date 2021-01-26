# -*- coding: utf-8 -*-
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    time_list = list(map(int, input().split()))
    minute = time_list[1] + time_list[3]
    hour = time_list[0] + time_list[2]
    if minute >= 60:
        hour += 1
        minute -= 60
    if hour > 12:
        hour -= 12
    print('#{} {} {}'.format(test_case, hour, minute))
    