
path = {
    0: [],
    1: [(-1, 0), (0, 1), (1, 0), (0, -1)],
    2: [(-1, 0), (1, 0)],
    3: [(0, -1), (0, 1)],
    4: [(-1, 0), (0, 1)],
    5: [(1, 0), (0, 1)],
    6: [(0, -1), (1, 0)],
    7: [(0, -1), (-1, 0)]
}

def bfs(r, c):
    queue = [(r, c)]
    cnt = 1
    l = L-1
    while l > 0:
        for _ in range(len(queue)):
            n_r, n_c = queue.pop(0)
            visited[n_r][n_c] = 1
            for dr, dc in path.get(brd[n_r][n_c]):  # 현재 위치에서 갈 수 있는 방향
                if 0 <= n_r+dr < N and 0 <= n_c+dc < M:  # 다음 방향이 맵 안에 존재하는지
                    if (-dr, -dc) in path.get(brd[n_r+dr][n_c+dc]):  # 다음 위치와 현재 위치가 연결되어있는지
                        if visited[n_r+dr][n_c+dc] == 0:  # 다음 위치에 방문한적이 없는지
                            queue.append((n_r+dr, n_c+dc))
                            visited[n_r+dr][n_c+dc] = 1
                            cnt += 1
        l -= 1
    return cnt



T = int(input())

for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    brd = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]

    print('#{} {}'.format(tc, bfs(R, C)))