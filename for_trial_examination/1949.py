import sys
sys.stdin = open(r'/Users/kangdaeyoung/Downloads/sample_input.txt', 'r')

def find_max():
    results = []
    max_v = -1e+10
    for r in range(N):
        for c in range(N):
            if brd[r][c] > max_v:
                results = [(r, c)]
                max_v = brd[r][c]
            elif brd[r][c] == max_v:
                results.append((r, c))
    return results

def dfs(r, c, n, chance):
    global max_n
    if max_n < n:
        max_n = n

    if chance == 0:  # 지금 스텝 전에 산을 깎았었다면 이후로는 깎을 일이 없기때문에
        for dr, dc in drc:
            if 0 <= r + dr < N and 0 <= c + dc < N and visited[r+dr][c+dc] == 0:
                if brd[r+dr][c+dc] < brd[r][c]:
                    visited[r][c] = 1
                    dfs(r+dr, c+dc, n+1, chance)
                    visited[r][c] = 0
    else:  # 이전에 산을 안깎았던 경우
        for dr, dc in drc:
            if 0 <= r+dr < N and 0 <= c + dc < N and visited[r+dr][c+dc] == 0:
                for k in range(K + 1):  # 산을 천천히 깎아 보장
                    if k == 0:  # 산을 안깎고 진행하는 경우,
                        if brd[r+dr][c+dc] < brd[r][c]:
                            visited[r][c] = 1
                            dfs(r+dr, c+dc, n+1, chance)
                            visited[r][c] = 0
                    else:
                        brd[r + dr][c + dc] -= k  # 산을 깎고 진행하는 경우
                        if brd[r + dr][c + dc] < brd[r][c]:
                            chance = 0
                            visited[r][c] = 1
                            dfs(r + dr, c + dc, n + 1, chance)
                            chance = 1
                            visited[r][c] = 0
                        brd[r + dr][c + dc] += k  # 원상복구하는 부분




drc = [(-1, 0), (0, 1), (1, 0), (0, -1)]
T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    brd = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    max_n = 1
    # 가장 높은 산봉우리 저장 -> max_rc
    max_rc = find_max()

    for r, c in max_rc:
        dfs(r, c, 1, 1)
    print('#{} {}'.format(tc, max_n))
