T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    min_val = 1e+10
    max_val = -1e+10

    for i in range(N - M + 1):
        temp_total = 0
        # 인접한 M개 원소의 합 구하기
        for j in range(M):
            temp_total += arr[i+j]
        # 기존 max 밸류보다 크면 값 교체
        if temp_total > max_val:
            max_val = temp_total
        # 기존 min 밸류보다 크면 값 교체
        if temp_total < min_val:
            min_val = temp_total

    print('#{} {}'.format(test_case, max_val-min_val))