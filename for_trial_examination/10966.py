import collections
T = int(input())

drc = [(-1, 0), (0, 1), (1, 0), (0, -1)]

for tc in range(1, T+1):
    n, m = map(int, input().split())
    brd = [input().strip() for _ in range(n)]
    visited = [[0]*m for _ in range(n)]
    result = 0  # 전체 거리 합
    queue = collections.deque([])
    # 물 인곳 좌표받기
    for r in range(n):
        for c in range(m):
            if brd[r][c] == 'W':
                queue.append((r, c))
    # 물이랑 땅과의 거리 구하기
    while queue:
        r, c = queue.popleft()
        for dr, dc in drc:
            if 0 <= r+dr < n and 0 <= c+dc < m and visited[r+dr][c+dc] == 0 and brd[r+dr][c+dc] == 'L':
                visited[r+dr][c+dc] = visited[r][c] + 1
                queue.append((r+dr, c+dc))
        result += visited[r][c]

    print('#{} {}'.format(tc, result))