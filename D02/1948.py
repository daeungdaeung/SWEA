# -*- coding: utf-8 -*-
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
dic = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}
for test_case in range(1, T + 1):
    ymd_list = list(map(int, input().split()))
    # 두 날짜 사이에 있는 월을 리스트에 저장
    remain_m = [i + ymd_list[0] + 1 for i in range(ymd_list[2] - ymd_list[0])]
    # 두 날짜가 다른 달인 경우
    if remain_m:
        # 이번 달 남은 일수 계산
        days = dic.get(ymd_list[0]) - ymd_list[1] + 1
        # 주어진 날짜 전 달 까지 계산
        for idx in range(len(remain_m)-1):
            days += dic.get(remain_m[idx])
        # 마지막 달 남은 일수 계산
        days += ymd_list[3]


    # 두 날짜가 같은 달인 경우
    else:
        days = ymd_list[3] - ymd_list[1] + 1

    print('#{} {}'.format(test_case, days))



