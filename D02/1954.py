# -*- coding: utf-8 -*-
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    snail_map = [[0 for i in range(N)] for j in range(N)]
    # 방향을 나타내주는 리스트 생성
    way = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    # 처음은 오른쪽으로 달팽이 이동
    way_idx = 0
    # 처음에는 무조건 N번 오른쪽으로 간다.
    # 그 이후부터는 N-1 2번, N-2 2번, ... 1 2번 => 모두 2번이다.
    cur_x, cur_y = 0, 0
    initial_val = 1
    snail_map[0][0] = 1
    for i in range(N, 0, -1):
        # 첫번째 변만 N칸 같은 방향으로 기어가는거 1번 반복
        if i == N:
            way_idx %= 4
            # 초기값 1을 지정해줘서 건너 뛰어도 됨
            for running in range(i-1):
                dx, dy = way[way_idx][0], way[way_idx][1]
                cur_x, cur_y = cur_x + dx, cur_y + dy
                initial_val += 1
                snail_map[cur_x][cur_y] = initial_val
            way_idx += 1
        else:    
            # 첫번째 경우 이후부터는 방향은 바뀌지만 칸 개수가 같아서
            # 두번 반복
            for j in range(2):
                way_idx %= 4
                for running in range(i):
                    dx, dy = way[way_idx][0], way[way_idx][1]
                    cur_x, cur_y = cur_x + dx, cur_y + dy
                    initial_val += 1
                    snail_map[cur_x][cur_y] = initial_val
                way_idx += 1
    print('#{}'.format(test_case))
    for i in range(N):
        print(' '.join(map(str, snail_map[i])))



