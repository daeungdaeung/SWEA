# -*- coding: utf-8 -*-
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    # 가장 먼저 해준 것은 리스트의 길이가 랜덤이기 때문에
    # 길이가 긴 리스트와 짧은 리스트를 구별하여 저장하였다.
    if N > M:
        large_list = list(map(int, input().split()))
        small_list = list(map(int, input().split()))
    # 두 리스트의 길이가 같은 경우, 케이스는 1개
    # 바로 반환하면 됨
    elif N == M:
        large_list = list(map(int, input().split()))
        small_list = list(map(int, input().split()))
        result = 0
        for i in range(N):
            result += large_list[i]*small_list[i]
        print('#{} {}'.format(test_case, result))
        continue
    else:
        small_list = list(map(int, input().split()))
        large_list = list(map(int, input().split()))
    # 여기서 부터는 문제에서 요구하는 최댓값을 찾을 것이다.
    # 길이의 차이 + 1 만큼 반복해주면 모든 경우를 다룰 수 있다.
    loop = abs(N - M) + 1
    len_small_list = len(small_list)
    max_value = -1e+10
    for i in range(loop):
        tmp = 0
        for j in range(len_small_list):
            tmp += small_list[j] * large_list[i+j]
        if max_value < tmp:
            max_value = tmp
    # 결과 출력
    print('#{} {}'.format(test_case, max_value))