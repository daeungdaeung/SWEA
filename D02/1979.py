# -*- coding: utf-8 -*-
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, K = list(map(int, input().split()))
    puzzle = []
    cnt = 0
    # 퍼즐 받아오기
    for i in range(N):
        puzzle.append(''.join(input().split()))
    # 퍼즐에서 horizontal 방향으로 단어 크기 있는지 검색
    for i in range(N):
        empty = puzzle[i].split('0')
        cnt += empty.count('1'*K)
    # 퍼즐에서 vertical 방향으로 단어 크기 있는지 검색
    # 1. vertical 방향을 horizontal 방향으로 만들자
    new_puzzle = []
    for j in range(N):
        tmp_s = ''
        for i in range(N):
            tmp_s += puzzle[i][j]
        new_puzzle.append(tmp_s)
    # 2. horizontal 방향 검색할 때와 마찬가지로 진행하면 됨
    for i in range(N):
        empty = new_puzzle[i].split('0')
        cnt += empty.count('1'*K)
    print('#{} {}'.format(test_case, cnt))
    # ///////////////////////////////////////////////////////////////////////////////////