# -*- coding: utf-8 -*-

# 현재 시간초과가 발생하는 문제임...
T = int(input())
targets = list(range(0, 200+1, 20))
targets.pop(0)

for test_case in range(1, T + 1):
    N = int(input())
    distances = []
    score = 0
    for i in range(N):
        x, y = map(int, input().split())
        d = (x**2 + y**2)**(0.5)
        distances.append(d)

    # 여기서 정렬을 해주면 뒤에서 시간을 단축시킬 수 있다.
    distances = sorted(distances)
    idx = 0
    for d in distances:
        while idx < 10:
            if d <= targets[idx]:
                score += 10-idx
                break
            else:
                idx += 1
        if idx >= 10:
            break

    print('#{} {}'.format(test_case, score))
