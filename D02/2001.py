T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, M = list(map(int, input().split(' ')))
    map_fly = []
    # 각 위치의 파리수 저장
    for i in range(N):
        map_fly.append(list(map(int, input().split(' '))))
    # 파리채로 내리쳤을 때 잡을 수 있는 파리 수 계산
    pre_dead_fly = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            dead_fly = 0
            # i, j로 기준점을 잡고 k 변수를 활용하여 잡은 파리수를 구함..!
            for k in range(j, j+M):
                dead_fly += sum(map_fly[k][i:i+M])
            if pre_dead_fly < dead_fly:
                pre_dead_fly = dead_fly
    print('#{} {}'.format(test_case, pre_dead_fly))

    # ///////////////////////////////////////////////////////////////////////////////////