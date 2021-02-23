# -*- coding: utf-8 -*-
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    omok = []
    result = 'NO'
    for i in range(N):
        omok.append(input())
    # horizontal check
    cnt = 0
    for y in range(N):
        cnt = 0
        for x in range(N):
            # 연속으로 돌이 이어질때 cnt 증가
            if omok[y][x] == 'o':
                cnt += 1
            # 이어지지 않으면 ct 0으로 초기화
            else:
                cnt = 0
            if cnt == 5:
                result = 'YES'
                break
        if result == 'YES':
            break

    # vertical check
    # 위에서 오목판정이 나지 않은 경우에 실행
    # 위에서 오목판정이 났으면 할 필요가 없음
    if result != 'YES':
        for x in range(N):
            cnt = 0
            for y in range(N):
                if omok[y][x] == 'o':
                    cnt += 1
                else:
                    cnt = 0
                if cnt == 5:
                    result = 'YES'
                    break
            if result == 'YES':
                break

    # diagonal check
    #  - 왼쪽 위에서 오른쪽 아래로 떨어지는 diagonal
    #  - 오른쪽 위에서 왼쪽 아래로 떨어지는 diagonal
    # 위에서 오목판정이 나지 않은 경우에 실행
    # 위에서 오목판정이 났으면 할 필요가 없음
    # 오른쪽 아래를 향하는 diagonal check
    if result != 'YES':
        num_diagonal = 1 + (N - 5)*2
        # main diagonal 아래 대각선들
        left = - (N - 5)
        # main diagonal 위 대각선들
        right = N - 5
        for loop in range(left, right+1):
            if loop < 0:
                dy, dx = abs(loop), 0
            elif loop > 0:
                dy, dx = 0, loop
            else:
                dy, dx = 0, 0

            cnt = 0
            for i in range(N-abs(loop)):
                if omok[i+dy][i+dx] == 'o':
                    cnt += 1
                else:
                    cnt = 0
                if cnt == 5:
                    result = 'YES'
                    break
            if result == 'YES':
                break
    # 위에서 오목판정이 나지 않았으면 진행
    # 오른쪽 위에서 왼쪽 아래로 내려오는 대각선들
    if result != 'YES':
        num_diagonal = 1 + (N - 5) * 2
        # main diagonal 위 대각선들
        left = - (N - 5)
        # main diagonal 아래 대각선들
        right = N - 5
        for loop in range(left, right+1):
            if loop < 0:
                dy, dx = 0, N + loop - 1
            elif loop > 0:
                dy, dx = loop, N - 1
            else:
                dy, dx = 0, N-1

            cnt = 0
            for i in range(N-abs(loop)):
                if omok[i+dy][-i+dx] == 'o':
                    cnt += 1
                else:
                    cnt = 0
                if cnt == 5:
                    result = 'YES'
                    break
            if result == 'YES':
                break

    print('#{} {}'.format(test_case, result))
