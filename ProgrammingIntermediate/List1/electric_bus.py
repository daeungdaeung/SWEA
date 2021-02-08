T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    K, N, M = map(int, input().split())
    elec_charger = list(map(int, input().split()))
    # 현재 버스 위치를 나타냄
    pos = 0
    cnt_charge = 0
    while pos < N:
        charge = False
        # 내가 최대로 갈 수 있는 거리부터 내림차순으로 충전기가 있는지 확인
        for dx in range(K, 0, -1):
            # 충전기가 있으면
            if pos + dx in elec_charger:
                # 버스 위치를 옮기고
                pos += dx
                cnt_charge += 1
                charge = True
                # 다음 루프로 이동
                break
            # 목적지에 도착했다면,
            if pos + dx >= N:
                # 목적지로 버스의 위치를 옮기고
                pos += dx
                charge = True
                # while 루프에서 빠져나옴 (while 조건: pos < N)
                break
        # 위 루프에서 충전할 수 있는 곳이 없다고 판별난 경우
        if not charge:
            break
    if charge == False:
        print('#{} {}'.format(test_case, 0))
    else:
        print('#{} {}'.format(test_case, cnt_charge))